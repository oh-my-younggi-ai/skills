# scenario-dev — iter-01: initial draft

- **Date:** 2026-06-15
- **Skill commit:** uncommitted draft (working tree, pre–first-commit)
- **Comparison:** `with_skill` vs `no_skill` (baseline)
- **Eval set:** 3 cases (discount-feature, signup-validator, pagination-bugfix)
- **Runner model:** claude-sonnet-4-6 (eval subagents) · analysis: claude-opus-4-8

## What this iteration is

First end-to-end draft of the scenario-dev skill (step-file BDD workflow: capture → confirm/freeze → cover → verify → present, + fast lane). Establishes the baseline numbers the skill must beat going forward.

## Headline result

> **with_skill 20/20 assertions (1.00) vs baseline 10/20 (0.50), Δ +0.50** — but every baseline failure is a *structural* assertion the baseline can't satisfy (no scenario set). On *behavioral* coverage the Sonnet baseline already ties the skill. The skill's demonstrated value at iter-01 is **structure, traceability, and verification discipline**, not raw correctness. Cost ≈ **1.65× tokens**.

## Quantitative results

| Config | Pass rate | Avg tokens | Avg duration |
|--------|-----------|------------|--------------|
| with_skill | 1.00 ± 0.00 | 85,887 ± 1,972 | 1232.4s ± 888s ⚠️ |
| baseline (no-skill) | 0.50 ± 0.07 | 52,125 ± 1,896 | 521.9s ± 79s |
| **Δ** | **+0.50** | **+33,761 (~1.65×)** | +710.5s ⚠️ (see note) |

⚠️ **Duration is distorted by one outlier** (signup/with_skill = 2254.8s) caused by retry-thrashing an intermittent permission gate — an environment artifact, not skill cost. **Excluding it: with_skill ≈ 721s vs baseline ≈ 522s (+199s, ~1.38×).** Tokens (~1.65×) are the reliable cost signal.

### Per-eval

| Eval | with_skill | baseline | notes |
|------|-----------|----------|-------|
| discount-feature | 7/7 (1.00) | 4/7 (0.57) | baseline strong: 26 tests incl. boundaries + negative input |
| signup-validator | 6/6 (1.00) | 3/6 (0.50) | baseline strong: 37 tests, collect-all-errors covered |
| pagination-bugfix | 7/7 (1.00) | 3/7 (0.43) | baseline lacks red-first + scenario structure |

### Per-assertion (with_skill / baseline)

| Assertion | with | base | discriminating? |
|-----------|------|------|-----------------|
| scenario_artifact | 3/3 | 0/3 | structural (skill-only by construction) |
| covers_happy_edge_error | 3/3 | 0/3 | structural |
| traceability | 3/3 | 0/3 | structural |
| red_before_green (pagination) | 1/1 | 0/1 | structural/process |
| tests_pass | 3/3 | 3/3 | **non-discriminating** (guardrail) |
| threshold/unknown (discount) | 2/2 | 2/2 | **non-discriminating** |
| collect_all/each_rule (signup) | 2/2 | 2/2 | **non-discriminating** |
| empty_list/page_range (pagination) | 2/2 | 2/2 | **non-discriminating** |
| error_case_tested (discount) | 1/1 | 1/1 | **non-discriminating** |

## Qualitative findings

- **The skill's wins are structural, not behavioral (yet).** Baseline Sonnet already writes thorough edge/error tests on these small tasks, so every *behavioral* assertion ties. All 10 baseline "failures" are the skill producing a scenario contract + traceability the baseline simply doesn't author. Real but unsurprising.
- **Gap-hunter works.** discount/with_skill's step-04 gap-hunter flagged untested whitespace-trimming → loopback added **S11** with the next stable id. The missing_scenario→cover mechanism fired end-to-end. (Baseline happened to test whitespace too, so no unique-coverage gain — but the machinery is proven.)
- **Verification discipline held under failure.** Subagents mostly couldn't run tests live (gate). 2/3 with_skill runs honestly left scenarios `covered` (not `verified`) and recorded `NO_VCS` instead of faking a green run. The skill refused to claim unproven success — exactly the intended behavior.
- **Non-discriminating assertions dominate.** 8 of the per-eval assertion *types* pass in both configs. They're fine as guardrails but don't measure skill value. The eval set is too easy to expose where structure changes *correctness*.

## Environment caveats (affecting this benchmark only)

- Detached subagents **could not execute code** (the `PermissionRequest` hook at `127.0.0.1:23333` is unreachable for background agents). **All `tests_pass` numbers were measured by the orchestrator running each suite directly** (`node --test`) post-hoc — every suite green: discount 26/14, signup 37/9, pagination 15/7 (base/skill).
- Subagents were **blocked from writing `summary*.md`**; summaries were reconstructed from each agent's final result text.
- One run (signup/with_skill) burned 37.6 min retrying the gate → its time/tokens are an outlier, excluded from the corrected duration figure.

## Decision → next iteration

1. **Harden the eval set.** Add tasks where the baseline *drops behavioral coverage* — subtle concurrency, multi-step state, an underspecified spec with a non-obvious edge — so assertions test whether the skill lifts *correctness*, not just documentation. Retire or de-weight the non-discriminating behavioral assertions, or split "skill produced X structure" (structural) from "behavior is correct" (behavioral) into two tracked sub-scores.
2. **Add a process/quality assertion the baseline can't fake**, e.g. "the gap-hunter surfaced ≥1 real missing/edge scenario the first-pass draft lacked" — to credit the loopback mechanism that pass/fail currently misses.
3. **Watch token cost.** 1.65× is acceptable for the artifact + adversarial review on real features; confirm the **fast lane** keeps trivial changes cheap (not exercised here — add a trivial eval to test routing).
4. **Skill text:** no change forced by the data yet — the skill behaved as designed. Hold edits until iter-02's harder evals reveal a real gap, to avoid overfitting to 3 easy cases.
