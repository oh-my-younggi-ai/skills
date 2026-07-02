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

## Decision → next iteration

- <what to change next, and why the numbers/feedback point there>
