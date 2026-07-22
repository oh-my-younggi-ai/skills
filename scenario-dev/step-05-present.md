# Step 5: Present

## RULES

- Communicate in the user's language.
- NEVER auto-push.

## INSTRUCTIONS

### Build the traceability summary

Append a `## Scenario Traceability` section to the artifact, after the existing sections. For each scenario, one row mapping the promised behavior to the proof it works:

```markdown
## Scenario Traceability

| Scenario | Verified by | Implementation |
|----------|-------------|----------------|
| S1: name | [`auth.test.ts:31`](../../src/auth.test.ts#L31) ✓ | [`auth.ts:88`](../../src/auth.ts#L88) |
| S2: name | manual walkthrough (see Verification Log) | [`auth.ts:120`](../../src/auth.ts#L120) |
```

This is the headline output of a scenario-driven run: a reviewer reads straight down it and confirms that every behavior the contract promised has a passing test (or a recorded walkthrough) and can see exactly where it lives. Links are relative to the artifact's directory, with `#L` anchors (see PATH CONVENTIONS). The `../../` above is illustrative - compute the real relative path.

### Finish up

1. Resolve the skill root, then run `python3 "{skill_root}/scripts/check_scenario_artifact.py" "{scenario_file}"`. Fix every reported completion-evidence gap before changing the artifact status.
2. Set status `done`, then rerun the same command with `--require-done`. This checks the final state without treating the prose itself as the contract.
3. If version control is available and the tree is dirty, create a local commit with a conventional message derived from the title. Never push.
4. Open the artifact in the human's editor so they can click through the traceability: resolve the repo root (`git rev-parse --show-toplevel`, falling back to the current working directory) and the artifact's absolute path, then run `code -r "{root}" "{artifact}"` (root first, both double-quoted). If `code` isn't available, just tell them the path.
5. **Summarize in chat** (paths CWD-relative, with `:line`):
   - scenarios verified (count), calling out any that used a manual walkthrough rather than a test;
   - files changed, one line each;
   - review outcome: patches applied, items deferred;
   - a note that the artifact now carries a Scenario Traceability table and is open in their editor (or the path, if it couldn't open);
   - **navigation tip:** "Cmd/Ctrl-click the links in Scenario Traceability to jump to each test and implementation."
   - an offer to push and/or open a pull request.

Workflow complete.
