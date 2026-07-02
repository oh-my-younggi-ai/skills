# Fast Lane: Single Trivial Scenario

For a lone, low-risk behavior where the full ceremony would cost more than it protects. You arrive here only from step-01's routing — if more than one scenario is really in play, or there's any real blast radius, go back to the full flow.

## RULES

- Communicate in the user's language.
- NEVER auto-push. Still test-backed — "trivial" means low-risk, not unverified.

## INSTRUCTIONS

1. **Implement** the change directly.
2. **Prove it.** Write at least one automated test encoding the scenario's Given/When/Then. Confirm it passes now and would have failed without the change (run it against the old behavior, or reason briefly about why it's red without the fix) — otherwise the test isn't really pinning the behavior. If the behavior genuinely can't be automated, do a documented walkthrough instead and record what you observed.
3. **Quick review.** If sub-agents are available, have one (no conversation context) sanity-check the diff for obvious bugs. Apply trivial fixes. If something non-trivial surfaces, HALT and tell the human — it probably wasn't fast-lane material after all, and the full flow's review would serve it better.
4. **Trace it.** Write `{scenario_dir}/scenario-{slug}.md` from `./scenario-template.md` with status `done`: the one scenario, an `## Out of Scope` if it helps bound things, and a `## Scenario Traceability` row mapping the scenario to its test and implementation. Add `route: 'fast-lane'` to the frontmatter.
5. **Commit & present.** If the tree is dirty, make a local commit with a conventional message. Summarize the change and the test that proves it, then offer to push or open a pull request.

Workflow complete.
