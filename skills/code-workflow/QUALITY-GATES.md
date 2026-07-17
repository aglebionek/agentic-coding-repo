# Code Workflow Quality Gates

## Gate 1 — Coherent intake

- Resolve the source request to one repository and a credible, explicit code target.
- Record applicable `AGENTS.md`, `CODING_GUIDELINES.md`, revision, and dirty state.
- Separate unrelated local changes and pre-existing check failures.
- State observable acceptance criteria, preservation requirements, and non-goals.

Stop when the target, ownership, or intended outcome is materially ambiguous. Manual mode uses `grill-me`; autorun returns the recommended resolution and exact input needed.

## Gate 2 — Purpose and contract

- Search applicable Obsidian documentation for an approved `## Intended purpose` whose `Applies to` covers the target.
- Never infer purpose from implementation, tests, issue text, comments, names, or history.
- Reconcile proposed behavior with approved purpose and external contracts.

Missing purpose blocks purpose-adherence and new concept documentation. It also blocks behavioral or contract refactoring whose correctness cannot otherwise be established. A strictly mechanical, evidenced behavior-preserving change may continue if its profile permits it.

## Gate 3 — Evidence and planning

- Run only the specialist reports selected by the profile.
- Require complete inventories and `Valid: true`; resolve or rerun invalid or stale reports.
- Use the matching planner mode and preserve every disposition, verification gate, boundary, and stop condition.
- Synthesize one plan under [ARTIFACT-CONTRACT.md](ARTIFACT-CONTRACT.md).

## Gate 4 — Implementation approval

Present the complete synthesized plan and stop. Begin edits only after the user explicitly approves that plan. An earlier agreement about architecture, requirements, mode, report, or workflow does not satisfy this gate.

Use [worktree](../worktree/SKILL.md) only when the user requests an isolated worktree. Never commit unless asked. Never delete a worktree unless asked.

## Gate 5 — Controlled execution

- Implement only approved steps and preserve unrelated work.
- Follow repository-native test, type, lint, and build commands, starting with focused checks.
- For testable-module work, obtain its required API and fixture agreement during planning; the approved synthesized plan records those decisions.
- Stop before unapproved behavior, public-interface, data-format, error-semantic, test-expectation, dependency, migration, architecture, destructive, or security/access-policy changes.
- Stop on material repository drift or when evidence invalidates the plan.

Create a supplemental plan for newly necessary edits. Do not disguise scope expansion as implementation detail.

## Gate 6 — Validation and documentation

1. Run the approved focused verification and compare against the recorded baseline.
2. Use [validate-current-changes](../validate-current-changes/SKILL.md) for a skeptical, read-only audit of logic, states, integration, complexity, and test credibility.
3. Use [review-intent-and-coverage](../review-intent-and-coverage/SKILL.md) when user confirmation of diff intent is needed. Any test or code edits it proposes require an approved supplemental plan.
4. Use [grow-docs](../grow-docs/SKILL.md) only for planned documentation backed by approved purpose. Do not use it to invent a missing purpose contract.
5. Report findings before fixes. Residual findings remain deferred until the user approves a correction plan.

## Gate 7 — External actions

Treat commits, pushes, pull requests, issue comments, labels, assignments, transitions, and closure as separate external mutations. Perform only the actions explicitly authorized by the user and report all actions left undone.
