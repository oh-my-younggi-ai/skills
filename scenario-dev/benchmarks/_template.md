# scenario-dev — iter-NN: <short title>

- **Date:** YYYY-MM-DD
- **Skill commit:** <git short sha of skills/scenario-dev at this iteration>
- **Comparison:** `with_skill` vs `<no_skill | iter-(NN-1)>`
- **Eval set:** N cases (<names>)
- **Runner model:** <model id powering the eval subagents>

## What changed this iteration

- <skill change + the hypothesis / why it should help>

## Headline result

> One-line verdict, e.g. "pass_rate 0.62 → 0.81 (+0.19) at ~1.7× tokens vs no-skill."

## Quantitative results

| Config | Pass rate | Avg tokens | Avg duration |
|--------|-----------|------------|--------------|
| with_skill | x.xx ± x.xx | … | … |
| baseline   | x.xx ± x.xx | … | … |
| **Δ** | +x.xx | +… | +… |

### Per-eval

| Eval | with_skill | baseline | notes |
|------|-----------|----------|-------|
| <name> | n/N | n/N | … |

### Per-assertion (with_skill)

| Assertion | Pass | Notes |
|-----------|------|-------|
| scenario_artifact | n/N | … |
| covers_happy_edge_error | n/N | … |
| tests_pass | n/N | … |
| error_case_tested | n/N | … |
| traceability | n/N | … |

## Qualitative findings

- <analyst observations: non-discriminating assertions, high-variance/flaky evals, time/token tradeoffs, notable transcript behavior>

## 이 수치가 증명하지 못하는 것

숫자만 남기면 다음 회차의 내가 과신한다. 아래를 명시한다.

- **측정하지 않은 것** - eval 셋 밖의 시나리오, 돌리지 않은 설정
- **프록시 지표의 한계** - 각 지표가 과소/과대 계수하는 경우.
  보정한 이력이 있으면 무엇을 왜 고쳤는지
- **환경 요인** - 이 변경과 무관하게 실패한 항목. baseline 에서도 동일하게
  재현되는지 확인했는지
- **남은 회귀 리스크** - 이번 변경으로 깨질 수 있는데 검사되지 않는 것

## Decision → next iteration

- <what to change next, and why the numbers/feedback point there>
