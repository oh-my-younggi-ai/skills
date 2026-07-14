#!/usr/bin/env python3
"""product-planning 결정론적 grader.

사용법: python3 grader.py <run_dir> [--config with_skill|without_skill]
  run_dir: outputs/ 를 포함하는 디렉토리 (with_skill/ 또는 without_skill/)

run_dir/grading.json 을 생성한다 (viewer 호환: expectations[].{text,passed,evidence}).
METRICS.md 의 스펙과 1:1 대응. LLM 판정 없음.
"""
import json
import re
import sys
from pathlib import Path

DOC_NAMES = ["00-brief.md", "01-product.md", "02-roadmap.md"]
BRIEF_SECTIONS = ["문제와 타겟", "핵심 가치", "도메인 역학", "범위와 성공 기준"]
PRODUCT_SECTIONS = ["사용자 여정", "화면 목록"]
PLACEHOLDER_RE = re.compile(r"\{[가-힣][^}]*\}")
EMPTY_STATE_RE = re.compile(r"빈|비어|empty|없을 때|없음|0개|0건|0명|초기 상태|콜드스타트", re.I)
RATIONALE_RE = re.compile(r"콜드스타트|획득|유입|리텐션|시딩|SEO|검색|커뮤니티|바이럴|수익", re.I)
NONDEV_RE = re.compile(r"시딩|모집|홍보|콘텐츠 채우|초기 데이터|런칭|오픈|배포 후 안내|인터뷰")
UNKNOWN_RE = re.compile(r"모르겠|미정|TBD|나중에 결정", re.I)
PHASE_RE = re.compile(r"^## Phase", re.M)
SCREEN_BLOCK_RE = re.compile(r"^### ", re.M)


def read(path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def collect_docs(outputs):
    """transcript 제외 모든 .md (baseline은 파일명 계약이 없으므로 전체 스캔)."""
    return {
        p.relative_to(outputs).as_posix(): read(p)
        for p in sorted(outputs.rglob("*.md"))
        if p.name != "transcript.md" and read(p)
    }


def grade_floor(outputs):
    checks = []
    planning = outputs / "docs" / "planning"
    missing = [n for n in DOC_NAMES if not (planning / n).exists()]
    checks.append(("F1 docs_exist: 문서 3종 존재", not missing,
                   f"missing: {missing}" if missing else "3/3 존재"))
    checks.append(("F2 transcript_exists: 대화 기록 존재",
                   (outputs / "transcript.md").exists(), "transcript.md"))

    brief = read(planning / "00-brief.md") or ""
    absent = [s for s in BRIEF_SECTIONS if s not in brief]
    checks.append(("F3 brief_sections: 브리프 필수 섹션", not absent,
                   f"missing: {absent}" if absent else "4/4 섹션"))

    product = read(planning / "01-product.md") or ""
    absent = [s for s in PRODUCT_SECTIONS if s not in product]
    checks.append(("F4 product_sections: 프로덕트 필수 섹션", not absent,
                   f"missing: {absent}" if absent else "2/2 섹션"))

    roadmap = read(planning / "02-roadmap.md") or ""
    n_phase = len(PHASE_RE.findall(roadmap))
    checks.append(("F5 phase_count: Phase 2~4개", 2 <= n_phase <= 4, f"{n_phase}개"))

    n_ph = sum(len(PLACEHOLDER_RE.findall(read(planning / n) or "")) for n in DOC_NAMES)
    checks.append(("F6 no_placeholder: 템플릿 잔존 없음", n_ph == 0, f"{n_ph}건"))
    return checks


def screen_blocks(text):
    """### 블록 단위로 분할 (화면 목록 문서용)."""
    parts = re.split(r"^### ", text, flags=re.M)
    return parts[1:] if len(parts) > 1 else []


def grade_metrics(outputs):
    docs = collect_docs(outputs)
    all_text = "\n".join(docs.values())

    blocks = [b for t in docs.values() for b in screen_blocks(t)]
    m1 = (sum(1 for b in blocks if EMPTY_STATE_RE.search(b)) / len(blocks)) if blocks else 0.0

    phase_blocks = []
    for t in docs.values():
        parts = re.split(r"^## (?=Phase)", t, flags=re.M)
        phase_blocks += [p for p in parts if p.startswith("Phase")]
    m2 = (sum(1 for p in phase_blocks if RATIONALE_RE.search(p)) / len(phase_blocks)) if phase_blocks else 0.0

    roadmap_texts = [t for n, t in docs.items()
                     if "roadmap" in n.lower() or "로드맵" in t[:200] or PHASE_RE.search(t)]
    m3 = sum(len(NONDEV_RE.findall(t)) for t in roadmap_texts)

    m4 = len(UNKNOWN_RE.findall(all_text))

    return {
        "empty_state_coverage": round(m1, 2),
        "phase_rationale_rate": round(m2, 2),
        "nondev_task_hits": m3,
        "unresolved_unknowns": m4,
        "screen_blocks": len(blocks),
        "phase_blocks": len(phase_blocks),
        "md_docs_scanned": len(docs),
    }


def main():
    run_dir = Path(sys.argv[1]).resolve()
    config = "without_skill" if "without" in str(run_dir) else "with_skill"
    outputs = run_dir / "outputs"
    if not outputs.is_dir():
        sys.exit(f"outputs/ not found under {run_dir}")

    metrics = grade_metrics(outputs)
    expectations = []
    if config == "with_skill":
        expectations = [
            {"text": t, "passed": p, "evidence": e} for t, p, e in grade_floor(outputs)
        ]
    expectations.append({
        "text": "M4 unresolved_unknowns: 문서에 미해결 표기 0건",
        "passed": metrics["unresolved_unknowns"] == 0,
        "evidence": f"{metrics['unresolved_unknowns']}건",
    })

    n_pass = sum(1 for e in expectations if e["passed"])
    result = {
        "config": config,
        "summary": {
            "passed": n_pass,
            "failed": len(expectations) - n_pass,
            "total": len(expectations),
            "pass_rate": round(n_pass / len(expectations), 4) if expectations else 0.0,
        },
        "expectations": expectations,
        "metrics": metrics,
    }
    (run_dir / "grading.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    passed = sum(1 for e in expectations if e["passed"])
    print(f"{run_dir.parent.name}/{run_dir.name}: {passed}/{len(expectations)} | {metrics}")


if __name__ == "__main__":
    main()
