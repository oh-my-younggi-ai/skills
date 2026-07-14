# product-planning — 측정 정의 (grader 스펙)

채점은 전부 `grader.py`의 결정론적 predicate로 한다. LLM 판정 없음.
내용 품질(아이디어가 좋은가)은 BENCHMARKING.md 원칙에 따라 점수에서 제외.

실행: `python3 benchmarks/grader.py <run_dir>` — run_dir은 `outputs/`를 포함하는
`with_skill/` 또는 `without_skill/` 디렉토리. `grading.json`을 run_dir에 생성.

## ① 회귀 바닥 (floor) — with_skill 전용, 전부 green 목표

스킬의 산출 계약. baseline은 이 계약을 모르므로 floor는 with_skill에만 적용.

| ID | 검사 | predicate |
|---|---|---|
| F1 `docs_exist` | 문서 3종 존재 | `docs/planning/{00-brief,01-product,02-roadmap}.md` 파일 존재 |
| F2 `transcript_exists` | 대화 기록 존재 | `transcript.md` 존재 |
| F3 `brief_sections` | 브리프 필수 섹션 | 00-brief에 `문제와 타겟`·`핵심 가치`·`도메인 역학`·`범위와 성공 기준` 헤더 전부 |
| F4 `product_sections` | 프로덕트 필수 섹션 | 01-product에 `사용자 여정`·`화면 목록` 헤더 전부 |
| F5 `phase_count` | Phase 2~4개 | 02-roadmap의 `## Phase` 개수 ∈ [2,4] |
| F6 `no_placeholder` | 템플릿 잔존 없음 | 문서 3종에서 정규식 `\{[가-힣][^}]*\}` 매치 0건 |

## ② 진행 지표 (metrics) — with/without 공통 측정, 델타가 신호

baseline은 파일명 계약이 없으므로 `outputs/` 아래 모든 `.md`(transcript 제외)를
스캔해 같은 정규식을 적용한다.

| ID | 지표 | 측정식 | 방향 |
|---|---|---|---|
| M1 `empty_state_coverage` | 화면 정의 중 빈 상태(콜드스타트 화면) 명시 비율 | `###` 화면 블록 중 상태 줄에 `빈\|비어\|empty\|없을 때\|없음\|0개\|0건\|0명\|초기 상태\|콜드스타트` 매치 비율. 화면 블록 0개면 0 (iter-01에서 undercount 발견 후 보정) | ↑ |
| M2 `phase_rationale_rate` | Phase 중 도메인 근거가 달린 비율 | `## Phase` 블록 중 `콜드스타트\|획득\|유입\|리텐션\|시딩\|SEO\|검색\|커뮤니티\|바이럴\|수익` 매치 비율. Phase 0개면 0 | ↑ |
| M3 `nondev_task_hits` | 로드맵 내 비개발 작업 언급 수 | 로드맵 문서에서 `시딩\|모집\|홍보\|콘텐츠 채우\|초기 데이터\|런칭\|오픈\|배포 후 안내\|인터뷰` 매치 수 (문서에 로드맵 없으면 0) | ↑ |
| M4 `unresolved_unknowns` | 문서에 남은 미해결 표기 | 산출 문서(transcript 제외)에서 `모르겠\|미정\|TBD\|나중에 결정` 매치 수. "모르겠다"는 가설로 채워져야 함 | ↓ (0 목표) |
| M5 `token_ratio` | 토큰 비용 | with_skill tokens ÷ without_skill tokens (timing.json) | 참고치 |

주의: M1~M3은 키워드 기반이라 게임 가능 — 절대값이 아니라 **baseline 대비 델타**와
iter 간 추이로만 읽는다 (cs-wiki density와 같은 취급).

## ③ 확장 eval 셋

iter마다 더 어려운 페르소나를 추가한다. 현재 3종:
`cold-start-two-sided` / `seo-single-player` / `very-vague-idea`.
후보: 기존 대안이 압도적으로 강한 아이디어(차별점 압박), B2B 양면, 규제 도메인.
