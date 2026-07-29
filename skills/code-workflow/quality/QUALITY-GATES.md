# Code Workflow Quality Gates

## Gate 1 — Coherent intake

- Resolve the source request to one repository and a credible, explicit code target.
- Record applicable `AGENTS.md`, coding and architecture guidance,
  documentation profile, revision, and dirty state.
- Separate unrelated local changes and pre-existing check failures.
- State observable acceptance criteria, preservation requirements, and non-goals.

Stop when the target, ownership, or intended outcome is materially ambiguous. Manual mode uses `grill-me`; autorun returns the recommended resolution and exact input needed.

## Gate 2 — Purpose and contract

- Search the project's configured documentation for an approved purpose contract
  whose scope covers the target.
- Never infer purpose from implementation, tests, issue text, comments, names, or history.
- Reconcile proposed behavior with approved purpose and external contracts.

Missing purpose blocks purpose-adherence and new concept documentation. It also blocks behavioral or contract refactoring whose correctness cannot otherwise be established. A strictly mechanical, evidenced behavior-preserving change may continue if its profile permits it.

## Gate 3 — Evidence and planning

- Run only the specialist reports selected by the profile.
- Require complete inventories and `Valid: true`; resolve or rerun invalid or stale reports.
- Use the matching planner mode and preserve every disposition, verification gate, boundary, and stop condition.
- Apply the [specialist contract](../specialists/SPECIALIST-CONTRACT.md) and
  synthesize one plan under the
  [artifact contract](../ARTIFACT-CONTRACT.md).

## Gate 4 — Implementation approval

Present the complete synthesized plan and stop. Begin edits only after the user explicitly approves that plan. An earlier agreement about architecture, requirements, mode, report, or workflow does not satisfy this gate.

Use [worktree](../../delivery/worktree/SKILL.md) only when the user requests an
isolated worktree. Never commit unless asked. Never delete a worktree unless
asked.

## Gate 5 — Controlled execution

- Implement only approved steps and preserve unrelated work.
- Follow repository-native test, type, lint, and build commands, starting with focused checks.
- Follow the shared `TESTING_GUIDELINES.md` as the sole testing authority for
  contract-first tests, verified red and green phases, hardening, preservation,
  and justified alternate proof.
- When a clearer module contract is required, apply
  [contract and fixtures guidance](../guidance/CONTRACT-AND-FIXTURES.md) during
  planning; the approved synthesized plan records those decisions.
- For fixed bug-hunt findings, add or run the approved finding-level regression proof before considering the correction complete. Stop if the approved proof is not viable or no longer matches the bug trigger.
- Stop before unapproved behavior, public-interface, data-format, error-semantic, test-expectation, dependency, migration, architecture, destructive, or security/access-policy changes.
- Stop on material repository drift or when evidence invalidates the plan.

Create a supplemental plan for newly necessary edits. Do not disguise scope expansion as implementation detail.

## Gate 6 — Validation and documentation

1. Run the approved focused verification and compare against the recorded baseline.
2. Confirm every fixed `BH-*` finding has its mapped regression proof, including the exact command or inspection result. A fixed bug without approved durable proof remains incomplete unless the plan already justified a non-test proof.
3. Run the [current-changes audit](CURRENT-CHANGES-AUDIT.md) for a skeptical,
   read-only review of logic, states, integration, complexity, and test
   credibility.
4. Confirm the complete diff matches the approved work package and acceptance
   criteria. Any corrective test or implementation edit requires a supplemental
   approved plan.
5. Use [grow-docs](../../knowledge/grow-docs/SKILL.md) only for justified, planned
   documentation backed by approved purpose and the active documentation
   profile. Do not use it to invent a missing purpose contract or force docs for
   a change with no documentation impact.
6. Report findings before fixes. Residual findings remain deferred until the user approves a correction plan.

## Gate 7 — External actions

Treat commits, pushes, pull requests, issue comments, labels, assignments, transitions, and closure as separate external mutations. Perform only the actions explicitly authorized by the user and report all actions left undone.
