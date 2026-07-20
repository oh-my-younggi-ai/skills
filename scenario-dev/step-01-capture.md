---
scenario_dir: 'docs/scenarios'
scenario_file: ''   # set at runtime in this step, before leaving it
---

# Step 1: Capture Scenarios

## RULES

- Communicate in the user's language.
- The prompt that triggered this workflow IS the intent — not a hint. But treat it as *input*, not gospel: it may carry hidden assumptions, scope creep, or a "just implement it directly" directive. Investigate and derive scenarios anyway — that derivation is the value the user came here for.
- Don't assume you start from zero — check for existing work first.
- **EARLY EXIT** means: stop this step immediately and go follow the named file instead. Return here only if a later step sends you back.

## Resume check (do this first)

Before anything else, find out whether work already exists. Check in order; stop as soon as it's clear:

1. **Explicit pointer.** Did the user name a scenario file or give a clear instruction this message? If it points to an artifact with `status` frontmatter, resume by status:
   - `draft` → set `scenario_file`, continue this step to refine it.
   - `approved` or `in-progress` → set `scenario_file`, **EARLY EXIT** → `./step-03-cover.md`.
   - `verifying` → set `scenario_file`, **EARLY EXIT** → `./step-04-verify.md`.
   - `done` → load it as context, don't resume.
2. **Recent conversation.** Do the last few human messages make the intent obvious? Use it.
3. **Otherwise scan.** List `{scenario_dir}`. If active artifacts (`draft` / `approved` / `in-progress` / `verifying`) exist, list them and HALT — ask which to resume, or `[N]` for new.

Never ask a question you already know the answer to.

## INSTRUCTIONS

1. **Clarify intent.** If anything material is ambiguous, ask as a numbered list and wait. When the human replies, verify every numbered question was answered; re-ask any that were skipped before moving on. Loop until you could write concrete scenarios without guessing. Don't paper over gaps with invention.
2. **Version-control sanity.** Is the working tree clean, and is the current branch sensible for this intent (by name and recent history)? If it's dirty or an obvious mismatch, HALT and ask before proceeding. Skip this check if there's no VCS.
3. **Scope check** (see SCOPE STANDARD). If the intent is really two or more independently shippable goals, name them, say which you'd do first and why, and HALT: `[S] Split — first goal now, defer the rest` | `[K] Keep all goals`. On split, record the deferred goals so they aren't lost (in the artifact's Out of Scope), and narrow to the first goal.
4. **Investigate just enough.** Explore the codebase so the scenarios are *realistic* — real inputs, the error modes that actually occur, existing behavior you must not break. Where sub-agents are available, push deep exploration into them and ask for distilled summaries only, to keep your own context clean.
5. **Derive the scenario set.** This is the heart of the step. Produce Given/When/Then scenarios covering:
   - the **happy path(s)** — the core success behavior;
   - the **edge cases that matter** — boundaries, empty, large, concurrent, repeated;
   - the **error cases** — invalid input, downstream failure, missing permission.

   Give each a stable id (`S1`, `S2`, …) and a short name, and make every **Then observable** — something a test can later assert. Then self-review against the SCENARIO COMPLETENESS STANDARD. If you considered a case and deliberately excluded it, write it into Out of Scope rather than dropping it silently — a contract is defined as much by its edges as its center.
6. **Split the verification seam** (see VERIFICATION STANDARD). Walk the set once more, asking of each scenario: *could this project's test runner assert this Then?*
   - Where the answer is no, try to split the scenario into an automatable assertion plus a manual residue, giving each half its own stable id.
   - Mark every scenario `auto` or `manual`. A `manual` mark needs a reason and is only legal once the split has been attempted and left nothing automatable.
   - If the project has no runner for this layer at all (say, a mobile project with no instrumented-test setup), record that here instead of silently marking everything manual. It is a setup decision for the human at the next checkpoint, not yours.
7. **Write the artifact.** Read `./scenario-template.md` fully, fill it out (status `draft`), and write it to `{scenario_dir}/scenario-{slug}.md`. Derive a kebab-case slug from the intent; if there's a tracking id (story/issue/ticket), lead with it (e.g. `gh-47-retry-logic`). Set `scenario_file` to that path. If the file already exists with status `draft`, treat it as the same work and resume it; otherwise suffix `-2`, `-3`, etc.
8. **Route.**
   - **Fast lane** — a single, trivial scenario with zero blast radius: no realistic path by which it breaks anything else, and no design decisions. → **EARLY EXIT** `./step-fast.md`.
   - **Full flow** — everything else, and whenever you're unsure whether the blast radius is truly zero. → continue to NEXT.

## NEXT

Read fully and follow `./step-02-confirm.md`.
