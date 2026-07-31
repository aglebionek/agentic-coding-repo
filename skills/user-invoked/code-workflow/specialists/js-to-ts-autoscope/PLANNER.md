# JS to TS Autoscope Planner

This is an internal code-workflow planner. Produce a plan, not changes. Do not
modify source, tests, configuration, documentation, generated artifacts,
snapshots, dependencies, or the Git index. Emit it in conversation unless the
work package supplies a plan path.

Read [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md) completely before planning.

## Validate The Report

1. Require a complete js-to-ts-autoscope report and identify its source.
2. Reject implementation planning when `Valid: false`.
   - In `autorun`, fail immediately without questions or interactive fallback.
   - In `manual`, optionally read
     [grill-me](../../../interaction/grill-me/SKILL.md) and
     resolve recovery decisions, but output only a clarified report-rerun
     handoff.
3. Revalidate repository state, mode, seed, tooling, selected spine, invariant, file roles, findings, exclusions, and verification readiness.
4. Record immaterial drift. Reject materially stale spine evidence, changed contracts, changed configuration, or expanded scope and recommend rerunning the report.

## Select Planning Mode

- `manual`: interactive. Read
  [grill-me](../../../interaction/grill-me/SKILL.md), resolve
  material decisions one at a time, and recommend an answer.
- `autorun`: AFK-safe. Make only evidence-backed decisions. Reject instead of
  guessing through purpose ambiguity, behavior/product/security/public-contract
  decisions, migrations, new dependencies, destructive work, architecture
  rewrites, or invalid reports.

Both modes are read-only and produce one definitive actionable path, not alternatives.

## Choose Execution Shape

1. Choose `oneshot` when the editable production spine is tightly coupled, typically up to 5 files, has limited caller impact, no unapproved boundary crossing, and can be verified in one pass.
2. Choose `sequenced` when shared types/contracts must precede callers, multiple layers are involved, verification gates differ, or the spine would be risky as one edit.
3. For every phase, define the strongest feasible checkpoint. Full typecheck after each phase is required only when the intermediate state can reasonably pass.
4. Make every deferred failure explicit and resolved by a later phase.

## Build The Plan

1. Give every `JTA-Fn` a disposition: `implement`, `verify`, `defer`, or `reject`, with evidence. Never silently omit one.
2. Preserve evidenced intended behavior and compatibility constraints. Plan guideline-aligned contract refactors only when purpose is clear and the report supports them.
3. Treat public API, route response shape, persisted data format, security/access policy, migrations, new dependencies, generated/vendor edits, broad caller rewrites, and architecture changes as stop conditions requiring separate approval.
4. Keep work within report `editable` files plus directly required tests, types, imports, and configuration. Use `inspect-only` files as evidence, not edit targets.
5. Map every action to `JTA-An`, `JTA-Cn`, `JTA-Fn`, file roles, and guideline dimensions. State exact source/destination paths, symbols, ordered edits, dependencies, and observable outcomes.
6. Apply the shared testing guideline and map credible proof to the spine
   invariant, result variants, contract refactors, and behavior risks.
7. Use repository-native type, lint, test, build, or runtime checks. Distinguish new failures from reported baseline limitations.

Keep execution, approval loops, runners, integration, commits, and pull
requests in the code-workflow facade.
