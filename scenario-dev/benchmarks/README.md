# scenario-dev — Benchmark Trajectory

Behavior-first (BDD) development workflow skill. This index tracks every benchmarked update; each row links to its full record.

| Iter | Date | Change | Comparison | Pass rate (skill) | Δ vs baseline | Record |
|------|------|--------|------------|-------------------|---------------|--------|
| 01 | 2026-06-15 | initial draft | vs no-skill | 1.00 (20/20) | +0.50 (base 0.50) | [iter-01](./iter-01-initial.md) |

> **iter-01 caveat:** the +0.50 is entirely *structural* (scenario artifact, traceability, red-first) — on *behavioral* coverage the Sonnet baseline ties the skill. The eval set is too easy to show whether the skill lifts correctness. iter-02 must harden the evals. Token cost ≈ 1.65×.

## Eval set

3 cases — defined canonically in `skills/scenario-dev/evals/evals.json`:

1. **discount-feature** — coupon rules + threshold edges + invalid/negative input. Greenfield feature.
2. **signup-validator** — multi-rule validation, "collect all errors at once". Error-rich.
3. **pagination-bugfix** — reproduction-scenario bug fix on an existing buggy function.

## Comparison strategy

- **iter-01:** `with_skill` vs **no-skill** — establishes the absolute value of the skill and the first numbers.
- **iter-02+:** new version vs **previous version** — proves each update helps (regression guard). Periodically re-baseline against no-skill to keep the north star honest.

## Assertions (what we quantify)

Objective, per-run checks graded against each output:

- `scenario_artifact` — a Given/When/Then scenario file with `status` frontmatter was produced.
- `covers_happy_edge_error` — the scenario set spans at least one happy, one edge, and one error scenario.
- `tests_pass` — an automated test suite exists and runs green.
- `error_case_tested` — the error scenario has a dedicated test (red-before / green-after).
- `traceability` — scenarios map to their tests/implementation (Coverage Map / Scenario Traceability).

Numbers are filled in as each iteration runs.
