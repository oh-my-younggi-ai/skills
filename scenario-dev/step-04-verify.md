---
loop_iteration: 1
---

# Step 4: Verify & Hunt Gaps

## RULES

- Communicate in the user's language.
- Review sub-agents get NO conversation context. Anchoring on your own reasoning is exactly what makes a reviewer blind to your mistakes — a cold read is the point.

## INSTRUCTIONS

Set status `verifying`.

### Run everything together

Run `test_command` — the full suite, not just the tests you touched. Every scenario's automated test must pass *together*; mark each passing scenario `verified` in the Coverage Map. For manual-fallback scenarios, execute the documented walkthrough and record the result in the Verification Log. If anything fails, fix it (back into step-03's red→green loop for that scenario) and re-run before continuing.

### Hunt for what the tests can't see

Construct the diff since `baseline_commit` (read-only — do NOT `git add`). Then launch reviewers with NO conversation context. If sub-agents aren't available, write each reviewer's prompt into `{scenario_dir}` and HALT, asking the human to run them in a separate session (ideally a different model) and paste back findings.

- **Scenario auditor** — gets the diff + the scenario artifact. Asks: does each test *actually assert its Then*, or is it hollow / tautological (e.g. asserts a mock it set up, or `expect(true)`)? Does the implementation genuinely satisfy each frozen scenario, or merely pass a weak test?
- **Gap hunter** — gets the intent + the scenario set + read access to the project. Asks: what in-scope behavior has **no scenario** at all? Which edge or error case does the intent clearly imply that the set silently omits?

### Classify and route

Deduplicate the findings, then classify each. The first three are *this work's problem*; the last two are not.

- **missing_scenario** — a real, in-scope behavior with no scenario. The contract is incomplete, and the contract is human-owned, so present it and HALT: add it, or declare it Out of Scope. If added, give it the next free stable id (never renumber existing scenarios) and loop back to `./step-03-cover.md` to cover it.
- **unmet_scenario** — a frozen scenario the implementation doesn't truly satisfy. Fix the code → back to `./step-03-cover.md` for that scenario.
- **hollow_test** — the test passes but doesn't really verify the Then. Strengthen it; if the stronger test now fails, fix the code too.
- **patch** — a trivial bug introduced by this change. Auto-fix it.
- **defer** — a pre-existing issue not caused by this work, surfaced incidentally. Note it (in Out of Scope, or a deferred-work note) for separate attention. When unsure between defer and reject, prefer reject.
- **reject** — noise. Drop it.

Increment `loop_iteration` on each loopback. If it climbs past 5, HALT and escalate to the human — repeated looping usually means the intent itself is still unsettled, which is a conversation, not a code fix.

Proceed only when the full suite is green, every scenario is `verified` (or walked through), and no blocking findings remain.

## NEXT

Read fully and follow `./step-05-present.md`.
