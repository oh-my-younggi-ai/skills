---
title: '{title}'
type: 'feature'        # feature | bugfix | refactor | chore
created: '{date}'
status: 'draft'        # draft | approved | in-progress | verifying | done
baseline_commit: ''    # set in step-03, before any change
test_command: ''       # the command that runs this artifact's scenarios
---

<!-- Remove all HTML comments when filling this in.
     Scenario ids (S1, S2, …) are STABLE: never renumber; a new scenario takes the next free id.
     Stable ids are what let the Coverage Map, traceability, and review loopbacks all refer to
     the same behavior over time. -->

<frozen-after-approval reason="human-owned contract — only the human changes this after approval">

## Intent

<!-- The "what", not the "how". -->

**Problem:** what is missing or broken, and why it matters. 1–2 sentences.

**Approach:** the high-level direction. 1–2 sentences.

## Scenarios

<!-- Each scenario: stable id + short name, then Given/When/Then.
     The Then MUST be observable — something a test can assert.
     Cover the happy path, the edge cases that matter, and the error cases. -->

### S1: <happy-path name>

- **Given** <starting state>
- **When** <action>
- **Then** <observable result>

### S2: <edge or error name>

- **Given** …
- **When** …
- **Then** …

## Out of Scope

<!-- Behaviors deliberately NOT covered, so the contract has edges. Include cases you
     considered and excluded, plus any goals split off during scoping. Delete the section
     only if there is genuinely nothing to bound. -->

- …

</frozen-after-approval>

## Coverage Map

<!-- step-03 fills this in. It is both the live status board and the traceability matrix.
     Status per scenario: pending → covered (test written & green in isolation)
     → verified (full suite green in step-04). Link targets are relative to THIS file's directory. -->

| Scenario | Status | Test | Implementation |
|----------|--------|------|----------------|
| S1 | pending | — | — |
| S2 | pending | — | — |

## Verification Log

<!-- step-04 fills this in: the full-suite result, plus any manual walkthrough written out as
     exactly what was done and observed, so it can be repeated. -->

## Notes

<!-- Optional. Design rationale, likely touch points found during step-01 investigation, or
     anything non-obvious. Delete this section if empty — don't write "N/A". -->
