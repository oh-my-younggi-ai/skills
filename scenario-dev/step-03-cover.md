# Step 3: Cover Each Scenario

## RULES

- Communicate in the user's language.
- No push, no remote operations. Local work only; the single optional commit happens in step 5.
- The `<frozen-after-approval>` block is read-only. If implementation reveals the contract itself is wrong, do NOT quietly edit it — that's a step-04 loopback to the human, because the contract is theirs.

## PRECONDITION

`{scenario_file}` resolves to an existing artifact with status `approved` or `in-progress`. If it's empty or missing, HALT and ask the human for the path before doing anything.

## SET UP

1. **Baseline.** Record `baseline_commit` (current HEAD, or `NO_VCS` if there's no version control) in the artifact frontmatter before you change a single file. step-04 builds its review diff from here.
2. **Test command.** Confirm the project's test runner and record `test_command` in the frontmatter — this is the exact command step-04 will run to prove every scenario. If the project has *no* test setup at all, treat it as an **Ask First**: propose the smallest reasonable harness and get the human's go-ahead, or (if they decline) fall back to documented manual walkthroughs for verification.
3. Set status `in-progress`.

## COVER THE SCENARIOS

Order the scenarios by dependency. For each one, work automation-first:

1. **Write the test that encodes its Given/When/Then, and run it red.** Watch it fail first — a test that passes *before* you've implemented anything isn't actually exercising the behavior. The red step is what proves the test has teeth. (For a bug-fix scenario, red = the test reproduces the bug.)
2. **Implement the minimum** that makes the test pass (green). Resist gold-plating beyond what the scenario asks — extra behavior nobody specified is untested behavior.
3. If the behavior genuinely resists automation (visual layout, subjective feel), write a precise manual walkthrough into the Verification Log instead, and note *why* a test didn't fit. Use this sparingly — see the VERIFICATION STANDARD.
4. **Record it in the Coverage Map**: scenario id → test `path:line` → implementation `path:line` → status `covered`. Links written into the artifact are relative to the artifact's directory (see PATH CONVENTIONS).

Keep scenarios at `covered`, not `verified`. "Verified" means the *whole* suite passes together, which step-04 checks — a scenario that's green in isolation but quietly breaks another is exactly what that final run is there to catch.

## SELF-CHECK

Every scenario is `covered` (or has a documented manual walkthrough). If any isn't, finish it before leaving this step.

## NEXT

Read fully and follow `./step-04-verify.md`.
