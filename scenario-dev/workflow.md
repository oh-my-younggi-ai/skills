---
scenario_dir: 'docs/scenarios'   # where scenario artifacts live, relative to project root; resolved in INITIALIZATION
---

# Scenario-Driven Dev Workflow

**Goal:** Turn user intent into a set of frozen, verifiable Given/When/Then scenarios, then implement and *prove* each one with an automated test before the work is done.

The organizing idea: **the scenario set is the contract, and progress is measured in scenarios verified — not tasks checked off.** A task list can lie ("done" without actually working); a scenario whose automated test fails cannot. That is why behavior is defined first, frozen together with the human, and then used to drive both the implementation and the review.

**CRITICAL:** If a step says "read fully and follow step-XX", you read and follow step-XX. No exceptions.

## SCENARIO COMPLETENESS STANDARD

A scenario set is complete enough to build when:

- **Concrete:** Every scenario is Given/When/Then with an **observable Then** — a result you could point a test at. No vague "works correctly."
- **Covers the space:** The happy path(s), the edge cases that matter (empty / boundary / large / concurrent / repeated), and the error cases (invalid input, downstream failure, missing permission). The *absence* of an edge or error scenario should be a decision, not an oversight — if a case is intentionally out of scope, say so in Out of Scope.
- **One behavior each:** Each scenario reads as a single behavior. Split compound "and then… and then…" scenarios so each can pass or fail on its own.
- **Collectively sufficient:** If every scenario passed, the intent would be satisfied. Nothing important is left unspecified.

## VERIFICATION STANDARD

Automation-first. Each scenario ends in one of two states:

- A **passing automated test** that encodes its Given/When/Then. This is the default and the strongly preferred outcome — the test is the thing that makes "done" honest.
- A **documented manual walkthrough**, used *only* when the behavior genuinely resists automation (e.g. visual layout, subjective UX feel). Record exactly what was done and observed, so the check can be repeated by someone else.

Reaching for the manual fallback when a real test was possible is the main way this workflow goes wrong — when in doubt, write the test.

## SCOPE STANDARD

Target a **single user-facing goal**. One cohesive behavior may span many files and many scenarios — that is fine and stays in one artifact. What does *not* belong together is **two independently shippable goals** — each could be its own PR without breaking the other. When you notice that, propose a split rather than letting one artifact sprawl.

A healthy artifact usually lands around a handful of scenarios. A lot more than that is often a hint that the "one goal" is really several — pause and check before continuing.

Neither the single-goal rule nor the rough scenario count is a hard gate. Both are proposals the human can override.

## WORKFLOW ARCHITECTURE

Step-file design, for disciplined execution:

- **One step at a time.** Load only the current step file, finish it, then load the next.
- **Read fully before acting.** Execute the step's sections in order.
- **Halt at checkpoints.** When a step says HALT, stop and wait for the human.
- **The artifact carries state.** Status lives in the scenario file's frontmatter and Coverage Map, so work can pause and resume across sessions.

### Critical rules

- NEVER load multiple step files at once.
- NEVER skip steps or "optimize" the sequence. The later steps — the human freeze, the adversarial gap-hunt — exist precisely to catch the blind spots you can't see from inside the work. Skipping them defeats the purpose of choosing this workflow.
- ALWAYS halt at checkpoints and wait for the human.

## PATH CONVENTIONS (apply in every step)

- **Links written *into* the scenario artifact** → relative to the artifact's own directory, so they're clickable in the editor. Use `#L<line>` anchors.
- **Paths shown in the terminal / chat** → CWD-relative, no leading `/`, with `:line` notation (e.g. `src/api/auth.ts:42`) so terminals can click them.

## INITIALIZATION

1. **Resolve context.**
   - Project root = git toplevel, or the current working directory if there's no VCS.
   - `scenario_dir` = `{scenario_dir}` under the project root. If the project clearly already has a scenarios/specs directory, prefer it; otherwise this directory is created the first time you write an artifact.
   - Note the project's test runner and command (e.g. `npm test`, `pytest`, `go test ./...`). You'll confirm and record it in step 3; surface it now if it's obvious.
   - Load `CLAUDE.md` and any project context docs if present.
   - **Communicate in the user's language** throughout the workflow.
2. **Begin.** Read fully and follow `./step-01-capture.md`.
