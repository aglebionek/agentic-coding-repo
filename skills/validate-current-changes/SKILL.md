---
name: validate-current-changes
description: Performs a skeptical, read-only audit of current local code changes for logic errors, invalid state models, unnecessary complexity, ambiguous naming, regressions, and misleading test coverage. Use when the user says "validate current changes," "audit this diff," "review without fixing," asks to look for bad logic or overcomplication, or wants findings before approving fixes.
---

# Validate Current Changes

Audit the change as a behavioral contract, not as an implementation to endorse. Do not modify, stage, unstage, commit, revert, or generate fix artifacts.

## Workflow

1. Read the applicable repository instructions and coding guidelines.
2. Establish scope with `git status`, unstaged and staged diffs, and relevant untracked files. Default to all local changes unless the user narrows the scope. Preserve the index exactly.
3. Reconstruct the intended behavior from the request, issue, plan, documentation, and surrounding code. State assumptions when intent is incomplete.
4. Summarize the diff behaviorally before judging it.
5. Inspect relevant unchanged callers, contracts, history, and comparison branches where they clarify behavior.
6. Run only non-mutating checks. Prefer focused tests, lint, type checks, and diff checks; separate pre-existing failures from findings caused by the change.
7. Report findings without implementing corrections. Wait for explicit approval before planning or fixing them.

## Audit Focus

### Logic and state

- Verify every state tells the truth and unambiguously answers the variable's domain question.
- Look for missing, impossible, redundant, overlapping, or context-relative states.
- Reject conversions where "not loading" or "finished" is silently treated as success or authorization.
- Trace initial, success, denial, missing-input, missing-resource, error, cancellation, redirect, unmount, and identity-change transitions.
- Check that stale results cannot authorize or load data for a new route, entity, or request.
- Confirm defaults and fallbacks do not hide programmer errors or broaden access.

### Design and integration

- Look for duplicated sources of truth, contradictory booleans, unnecessary state, effects, refs, callbacks, and wrapper abstractions.
- Ask whether each state must be stored or can be derived, and whether each responsibility belongs in the module that owns it.
- Check all callers for consistent interpretation and preserved behavior.
- Verify identifiers, URLs, payloads, and external contracts remain exact across edge cases.
- Ensure protected I/O cannot start before the required decision permits it.

### Test credibility

- Check that tests prove user-visible contracts and failure prevention rather than restating implementation details.
- Cover positive, negative, error, transition, identity-change, and no-side-effect paths where relevant.
- Identify mocks that bypass the real integration boundary or make an impossible state look valid.
- Treat passing tests as evidence, not proof that the design is sound.

## Report Format

1. **Behavioral summary** — what the change actually does.
2. **Findings** — ordered by severity; include file and line, violated invariant, concrete failure scenario, and smallest recommended correction.
3. **Complexity** — unnecessary mechanisms and safe simplification opportunities.
4. **Coverage** — missing cases and tests that provide false confidence.
5. **Verdict** — proceed as-is, revise, or redesign, with residual risks.

If there are no findings, say so explicitly and still report validation limits. Keep unrelated and pre-existing problems separate.

## Example Requests

- "Validate all current changes and do not fix anything."
- "Audit this diff for bad logic, unnecessary states, and overcomplication."
- "Review the implementation skeptically before I approve a fix pass."
