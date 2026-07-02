# Step 2: Confirm & Freeze

## RULES

- Communicate in the user's language.
- The scenario set is human-owned. Your job in this step is to make it easy to approve or correct — not to quietly expand it.

## INSTRUCTIONS

1. **Self-review** the draft once more against the SCENARIO COMPLETENESS STANDARD. If you spot a genuine gap, fix the draft before presenting it. If closing the gap needs a human decision (e.g. "should we handle the offline case at all?"), leave it and raise it at the checkpoint.
2. **Present the scenario set** so the human can take in the whole shape at a glance — they're approving a contract, so they need to see its edges, not just its center. Show:
   - a one-line intent summary;
   - each scenario as `S1: name` with a single-line behavior summary, grouped into happy / edge / error;
   - the Out of Scope list;
   - the artifact path (CWD-relative, so it's clickable).

### CHECKPOINT

Tell the human they can edit the file directly or ask you to change it. Mention that for a harder pressure-test of the scenario set, they can review it in a separate session before approving — a fresh context spots missing scenarios more easily than the one that wrote them.

HALT and ask: `[A] Approve & freeze` | `[E] Edit`.

- **A** — Re-read `{scenario_file}` from disk.
  - **Missing?** HALT and stop — tell the user the artifact is gone and do not recreate it or proceed.
  - **Changed since you wrote it?** Acknowledge the human's edits (a brief summary of what changed) and continue with their version.
  - Set status `approved`. Everything inside `<frozen-after-approval>` — Intent, Scenarios, Out of Scope — is now the contract; from here only the human may change it. → Step 3.
- **E** — Apply the requested changes, then return to CHECKPOINT.

## NEXT

Read fully and follow `./step-03-cover.md`.
