# skills

내가 만든 Claude Code 스킬 모음. 각 스킬은 **eval 정의 → 측정 → 실패모드 분석 → 개선 → 재측정**
루프로 만들어지고, 그 이력을 스킬 안에 함께 보관한다.

## 스킬 목록

| 스킬 / 프로젝트 | 설명 | 상태 |
|---|---|---|
| [**cs-interview**](./cs-interview/) | CS 지식 위키 구축(cs-wiki) + 그 위키로 모의면접(cs-interviewer). 한 쌍 프로젝트 | ✅ 벤치 측정 완료 |
| scenario-dev | BDD 시나리오 주도 개발 스킬 | 이관 예정 |
| iterative-refactor | 배치 → 테스트 게이트 → 커밋 리팩터링 스킬 | 이관 예정 |
| design-doc | 설계 문서 작성 스킬 | 이관 예정 |
| bmad-quick-dev | 빠른 개발 워크플로우 스킬 | 이관 예정 |

> "이관 예정" 스킬들은 `~/.claude/skills/` 에서 검증·정리 후 순차적으로 이 모음에 편입한다.

## 컨벤션
- 스킬은 `<project>/skills/<name>/SKILL.md` 구조로 설치 가능한 단위를 유지한다.
- 개선 이력은 각 프로젝트의 `CHANGELOG.md`, 측정 수치는 `benchmarks/` 에 둔다.
