# skills

내가 만든 Claude Code 스킬 모음. **eval 정의 → 측정 → 실패모드 분석 → 개선 → 재측정** 루프를
지향한다. 개선 이력은 각 스킬의 `CHANGELOG.md`에 남기고, 측정까지 이뤄진 스킬(product-planning,
scenario-dev, cs-interview 의 cs-wiki)은 `evals/`·`benchmarks/`를 함께 보관한다. 나머지는 순차 도입 중.

## 스킬 목록

| 스킬 | 설명 |
|---|---|
| [product-planning](./product-planning/) | 흐릿한 아이디어 → 기획 문서 3종 (intake → discovery 4스테이지 → 화면·플로우 → 도메인 역학 기반 로드맵) · 📊 [벤치](./product-planning/benchmarks/) |
| [scenario-dev](./scenario-dev/) | BDD 시나리오 주도 개발 (capture → confirm → cover → verify → present) · 📊 [벤치](./scenario-dev/benchmarks/) |
| [iterative-refactor](./iterative-refactor/) | 배치 → 테스트 게이트 → 커밋 리팩터링 |
| [design-doc](./design-doc/) | 설계 문서 작성 (topic → clarify → draft & review) |
| [bmad-quick-dev](./bmad-quick-dev/) | 빠른 개발 워크플로우 (clarify → plan → implement → review) |
| [blog-voice](./blog-voice/) | 블로그 문체 가이드 — 회고·기술 에세이 작성/퇴고 시 내 말투를 유지 |

## 별도 프로젝트

- **cs-interview** — CS 지식 위키 구축(cs-wiki) + 그 위키 기준 모의면접(cs-interviewer).
  한 쌍이라 독립 repo 로 분리: https://github.com/oh-my-younggi-ai/cs-interview

## 설치

Claude Code 는 스킬을 `~/.claude/skills/<name>/SKILL.md` 로 인식한다. 원하는 스킬 폴더를 복사:

```bash
cp -R scenario-dev ~/.claude/skills/
```

## 벤치마킹

각 스킬의 변경은 **수치로 개선을 입증**한 뒤에만 받아들인다 — 방법론은
[BENCHMARKING.md](./BENCHMARKING.md), 실측 기록은 각 스킬의 `benchmarks/` 참고.
(예: scenario-dev, 그리고 cs-interview repo 의 cs-wiki 기록)

## 컨벤션

- 스킬은 `<name>/SKILL.md` + step-file 아키텍처로 설치 가능한 단위를 유지한다.
- 개선 이력은 각 스킬의 `CHANGELOG.md`, 측정 수치는 `evals/`·`benchmarks/` 에 둔다.
