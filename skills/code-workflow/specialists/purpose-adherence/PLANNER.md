# Purpose Adherence Planner

This is an internal code-workflow planner. Produce a plan, not changes. Do not
modify code, types, tests, callers, documentation, snapshots, or the Git index.
Emit the plan in conversation unless the work package supplies a plan path.

Read [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md) completely before planning.

## Validate the report

1. Require a complete purpose-adherence report and identify its source.
2. Reject implementation planning when `Valid: false`.
   - In `autorun`, fail immediately without questions or fallback to interactive planning.
   - In `manual`, optionally grill through recovery questions, but output only a clarified report-rerun handoff.
3. Revalidate the repository, purpose contract, targets, and cited behavior against the report's analysis state.
4. Continue after immaterial drift and record it. Reject materially stale
   findings or contracts and rerun this specialist's report through the active
   profile.

Never repair, reinterpret, or plan changes to `## Intended purpose`; contract correction belongs to `infer-purpose`.

## Select mode

- `manual`: read [grill-me](../../../grill-me/SKILL.md) and resolve material
  decisions one question at a time, always recommending an answer.
- `autorun`: make safe action decisions independently. Never ask questions,
  start an interactive session, or guess through material behavioral ambiguity,
  scope expansion, public-contract change, migration, destructive work, or
  security/access-policy choice; reject planning with an actionable reason.

Both modes must produce one definitive actionable path, not a menu of alternatives.

## Build the plan

1. Give every confirmed finding a disposition: fix, defer, or reject as no longer applicable, with evidence.
2. Include `critical` and `high` findings immediately unless explicitly blocked. Include `medium` by default. Include locally safe `low` findings; otherwise defer them explicitly. Never silently omit a mismatch.
3. Map every action to finding and purpose-clause IDs. State the intended behavioral outcome, exact files and symbols, ordered work, dependencies, and verification.
4. Keep changes within `Applies to` plus directly coupled callers, types, tests, and existing docs. Flag public contracts, migrations, architectural changes, destructive work, and broader ownership as execution stop conditions requiring separate approval.
5. Preserve supporting artifacts unless the report proves they are wrong or a required correction would make them false:
   - apply the shared testing guideline and map proof to the governing purpose
     clauses
   - change types only when they permit, require, or describe behavior contrary to purpose
   - change related docs only when contradictory or made stale by the correction
6. Follow root `CODING_GUIDELINES.md` for planned code changes without turning general standards issues into adherence work.
7. Define clause-level verification that proves required behavior, forbidden behavior, and absence of accidental drift.

Broader test design, architectural refactoring, new documentation clusters, and unrelated problems belong in deferred follow-ups for specialist skills.
