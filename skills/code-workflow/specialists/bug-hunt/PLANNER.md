# Bug Hunt Planner

This is an internal code-workflow planner. Produce a plan, not changes. Do not
modify source, tests, configuration, documentation, generated artifacts,
snapshots, dependencies, or the Git index. Emit the plan in conversation unless
the work package supplies a plan path.

Read [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md) completely before planning.

## Validate the report

1. Require a complete bug-hunt report and identify its source.
2. Reject implementation planning when `Valid: false`.
   - In `autorun`, fail immediately without questions or interactive fallback.
   - In `manual`, optionally grill through recovery decisions, but output only a clarified report-rerun handoff.
3. Revalidate the repository, scope inventory, cited behavior, evidence, and
   analysis state. Record immaterial drift; reject materially stale or
   incomplete findings and rerun this specialist's report through the active
   profile.
4. Keep weak suspicions, unrelated pre-existing leads, style, unsupported smells, architecture preferences, generic coverage gaps, and purpose-adherence concerns outside the correction plan.

## Select mode

- `manual`: read [grill-me](../../../grill-me/SKILL.md), resolve material
  decisions one question at a time, and recommend an answer.
- `autorun`: make safe decisions independently. Never ask questions or guess
  through ambiguous intended behavior, public-contract changes, migrations, new
  dependencies, architecture changes, destructive work, or security/access
  policy choices; reject planning with an actionable reason instead.

Both modes are read-only and produce one definitive actionable path, not a menu of alternatives.

## Build the plan

1. Give every confirmed finding a `fix`, `defer`, or `reject` disposition with current evidence. Give every probable finding a `verify`, `defer`, or `reject` disposition; verification must precede any conditional fix. Never silently omit a finding.
2. Include `critical` and `high` findings immediately unless blocked. Include `medium` by default. Include locally safe `low` findings; otherwise defer them explicitly.
3. Map every action to `BH-Fn` or verified `BH-Pn`. State the correct behavior, exact files and symbols, ordered edits, dependencies, smallest correction, preservation requirements, regression proof, and verification.
4. Change behavior only to correct the evidenced bug. Preserve unrelated behavior, public interfaces, data formats, valid tests, dependencies, architecture, compatibility, and established error semantics.
5. Keep work within the report target plus directly coupled callers, tests, types, configuration, and documentation required for the correction. Treat public contracts, migrations, new dependencies, architecture changes, destructive work, and security/access-policy choices as execution stop conditions requiring separate approval.
6. Apply the shared testing guideline. Map every corrected `BH-*` finding to
   credible regression proof and identify any evidenced bug that makes an
   existing expectation false.
7. Define finding-level verification that proves the trigger is corrected, the invariant holds, regression coverage is credible, and unrelated behavior remains intact. Passing tests alone do not prove correctness.

Record unrelated improvements and pre-existing issues only as deferred
follow-ups with a suitable code-workflow profile and target.
