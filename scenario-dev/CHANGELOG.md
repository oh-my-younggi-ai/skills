# scenario-dev — Changelog

Full benchmark records: `./benchmarks/`

## 2026-07-20 - 검증 seam 분리 (벤치 미측정)

> **미측정 경고.** 이 변경은 벤치마크로 검증하지 않았다. 현재 eval 셋
> (discount-feature, signup-validator, pagination-bugfix)은 전부 순수 로직 JS 라
> 자동화 경계 문제가 발생하지 않아, 개선도 회귀도 감지할 수 없다. 기기/서드파티
> 의존이 있는 eval 케이스를 추가해 baseline 을 잡고 재측정해야 한다.
> 그전까지 이 변경의 효과는 가설이다.

- **VERIFICATION STANDARD** 에 "수동으로 부르기 전에 seam 을 쪼개라" 추가.
  "실기기가 필요하다"는 기준은 보통 자동화 가능한 단언 하나와 수동 관찰 하나가
  붙어 있는 것이라 각각 독립 시나리오로 분리한다. `manual` 은 분리 시도 후에도
  자동화할 게 없을 때 내리는 **결론**이지 출발 가정이 아니다
- **step-01** 에 seam 분리 패스를 6번 항목으로 신설. 시나리오마다 `auto` / `manual`
  표기, `manual` 은 사유 필수. 레이어 전체에 러너가 없으면 임의로 수동 처리하지 말고
  사람의 셋업 결정으로 올린다
- **step-02** 에서 수동 시나리오를 따로 모아 제시. 스위트가 보호하지 않는 범위를
  사람이 동결 전에 알고 승인하게 한다
- **step-04** 시나리오 감사자가 `manual` 사유의 유효성을 재검사. 새 분류
  `automatable_manual` 추가 (구현 후에는 자동화 가능해진 경우)
- **템플릿** 에 시나리오별 `Verification:` 줄과 Coverage Map 의 Verification 열

동기: 기기/미디어/외부 연동 작업에서 자동화 경계는 시나리오의 *내용*을 바꾸는 설계
결정인데, 기존 흐름은 step-03 구현 중에야 발견해서 동결된 계약을 되돌려야 했다.

## 2026-07-02 — 유지보수
- org 이관: 벤치 기록 경로를 repo 내 `./benchmarks/` 로 정정.

## iter-01 · 2026-06-15 — initial draft

**Pass rate:** 1.00 (20/20) vs baseline 0.50 · **Δ** +0.50 · **Token cost** ≈ 1.65×

- 스킬 첫 버전. step-file BDD 워크플로우 (capture → confirm → cover → verify → present + fast lane) 구현
- 구조적 어설션(scenario artifact, traceability, red-first)에서 baseline 대비 명확한 우위
- 행동적 커버리지(behavioral)는 Sonnet baseline과 동률 — eval set이 너무 쉬움
- **Next:** 더 어려운 eval 케이스 추가, 행동 커버리지를 실제로 측정할 어설션 보강
