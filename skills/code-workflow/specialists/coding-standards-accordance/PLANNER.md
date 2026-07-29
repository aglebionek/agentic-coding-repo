# Coding Standards Accordance Planner

This is an internal code-workflow planner. Produce a plan, not changes. Do not
modify source, tests, configuration, documentation, generated artifacts,
snapshots, dependencies, or the Git index. Emit the plan in conversation unless
the work package supplies a plan path.

Read [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md) completely before planning.

## Validate the report

1. Require a complete coding-standards-accordance report and identify its source.
2. Reject correction planning when `Valid: false`.
   - In `autorun`, fail immediately without questions or interactive fallback.
   - In `manual`, optionally grill through recovery decisions, but output only a clarified report-rerun handoff.
3. Revalidate the repository, governing `CODING_GUIDELINES.md`, target inventory, accepted deviations, findings, and analysis state. Record immaterial drift; reject materially stale or incomplete analysis and recommend rerunning the report.
4. Keep generic bugs, vulnerabilities, purpose mismatches, catalog smells, broad architecture preferences, and unrelated coverage gaps outside the correction plan.

## Select mode

- `manual`: read [grill-me](../../../grill-me/SKILL.md), resolve material
  decisions one question at a time, and recommend an answer.
- `autorun`: make safe decisions independently. Never ask questions or guess
  through runtime-behavior changes, public-interface changes, data-format
  changes, altered error semantics, invalidated tests, new dependencies,
  architecture changes, migrations, destructive work, or security/access-policy
  choices; reject planning with an actionable reason instead.

Both modes are read-only and produce one definitive actionable path, not a menu of alternatives.

## Build the plan

1. Give every `CSA-Fn` a `correct`, `defer`, or `reject` disposition with current evidence. Never silently omit a finding.
2. Include `high` findings immediately unless blocked and `medium` findings by default. Include locally safe `low` findings; otherwise defer them explicitly.
3. Preserve accepted deviations whose constraints and intent remain valid. If correction work invalidates a deviation, disposition it explicitly and reassess its guideline before planning dependent changes.
4. Map every action to findings and `CSA-Gn` rules. State the standards-aligned outcome, exact files and symbols, ordered edits, dependencies, and verification.
5. Prefer the smallest change that restores accordance. Preserve runtime behavior, public interfaces, data formats, error semantics, valid tests, dependencies, and architecture unless the interactive user explicitly approves a boundary crossing.
6. Keep work within the report target plus directly coupled callers, tests, types, configuration, and documentation needed for correction. Treat behavior or contract changes, migrations, new dependencies, architecture changes, destructive work, and security/access-policy choices as execution stop conditions requiring separate approval.
7. Apply the shared testing guideline and map standards-aligned proof to each
   corrected finding.
8. Define guideline- and finding-level verification proving accordance and preservation. Passing tests alone do not prove the design meets the guidelines.

Record unrelated improvements and pre-existing concerns only as deferred
follow-ups with a suitable code-workflow profile and target.
