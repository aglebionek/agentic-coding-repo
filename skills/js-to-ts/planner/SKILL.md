---
name: js-to-ts-planner
description: Converts a valid js-to-ts report into one read-only, behavior-preserving TypeScript conversion plan. Use only when the user explicitly invokes "js-to-ts planner" for interactive planning or "js-to-ts autoplan" for non-interactive AFK planning.
---

# JS to TS Planner

Produce a plan, not changes. Do not modify code, types, tests, configuration, snapshots, generated artifacts, or the Git index. Emit it in conversation unless the user supplies a plan path.

Read [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md) completely before planning.

## Validate the report

1. Require a complete js-to-ts report and identify its source.
2. Reject implementation planning when `Valid: false`.
   - In `autoplan`, fail immediately without questions or interactive fallback.
   - In `planner`, optionally grill through recovery decisions, but output only a clarified report-rerun handoff until the report is valid.
3. Revalidate targets, effective configuration, dependencies, callers, behavior, and baseline checks against the report state.
4. Continue after immaterial drift and record it. Reject materially stale scope, contracts, configuration, or findings and recommend rerunning `js-to-ts report`.

## Select mode

- `js-to-ts planner`: read [grill-me](../../grill-me/SKILL.md) and resolve material decisions one question at a time, always recommending an answer.
- `js-to-ts autoplan`: make safe decisions independently. Never ask questions or guess through behavioral ambiguity, public-contract change, migration, broad architecture, destructive work, generated code, or security/access policy; reject planning with an actionable reason instead.

Both modes produce one definitive actionable path, not alternatives.

## Build the plan

1. Give every finding a disposition: implement, defer, or reject as no longer applicable, with evidence. Never silently omit one.
2. Preserve observable behavior. Include only mechanical conversion and the smallest contract refactors required for sound types; defer unrelated guideline improvements.
3. Map every action to finding, API, and conversion IDs. State exact source/destination paths, symbols, ordered work, dependencies, and observable outcomes.
4. Plan `.ts` or `.tsx` renames, imports and exports, explicit boundary types, trust-boundary validation, typed outcomes, effects, state and async contracts, callers, tests, and configuration only where required.
5. Preserve valid tests. Add contract or regression coverage before behavior-affecting refactors; type-only, mechanical, and presentation-only changes need tests only when they prove meaningful behavior.
6. Use repository-native type, test, lint, and build checks. Define focused proof for every converted API and ensure the plan distinguishes new failures from the report baseline.
7. Treat public API changes, migrations, broad architectural work, destructive operations, security/access policy, generated-code edits, and unresolved runtime semantics as execution stop conditions requiring separate approval.

Keep execution, approval loops, runners, and orchestration outside this skill.
