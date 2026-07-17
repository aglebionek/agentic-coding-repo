---
name: bug-hunt-planner
description: Converts a bug-hunt report into one read-only, evidence-mapped correction and verification plan. Use only when the user invokes "bug-hunt planner" for interactive planning or "bug-hunt autoplan" for non-interactive AFK planning with a report.
---

# Bug Hunt Planner

Produce a plan, not changes. Do not modify source, tests, configuration, documentation, generated artifacts, snapshots, dependencies, or the Git index. Emit the plan in conversation unless the user supplies a plan path.

Read [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md) completely before planning.

## Validate the report

1. Require a complete bug-hunt report and identify its source.
2. Reject implementation planning when `Valid: false`.
   - In `autoplan`, fail immediately without questions or interactive fallback.
   - In `planner`, optionally grill through recovery decisions, but output only a clarified report-rerun handoff.
3. Revalidate the repository, scope inventory, cited behavior, evidence, and analysis state. Record immaterial drift; reject materially stale or incomplete findings and recommend rerunning `bug-hunt report`.
4. Keep weak suspicions, unrelated pre-existing leads, style, unsupported smells, architecture preferences, generic coverage gaps, and purpose-adherence concerns outside the correction plan.

## Select mode

- `bug-hunt planner`: read [grill-me](../../grill-me/SKILL.md), resolve material decisions one question at a time, and recommend an answer.
- `bug-hunt autoplan`: make safe decisions independently. Never ask questions or guess through ambiguous intended behavior, public-contract changes, migrations, new dependencies, architecture changes, destructive work, or security/access-policy choices; reject planning with an actionable reason instead.

Both modes are read-only and produce one definitive actionable path, not a menu of alternatives.

## Build the plan

1. Give every confirmed finding a `fix`, `defer`, or `reject` disposition with current evidence. Give every probable finding a `verify`, `defer`, or `reject` disposition; verification must precede any conditional fix. Never silently omit a finding.
2. Include `critical` and `high` findings immediately unless blocked. Include `medium` by default. Include locally safe `low` findings; otherwise defer them explicitly.
3. Map every action to `BH-Fn` or verified `BH-Pn`. State the correct behavior, exact files and symbols, ordered edits, dependencies, smallest correction, preservation requirements, regression proof, and verification.
4. Change behavior only to correct the evidenced bug. Preserve unrelated behavior, public interfaces, data formats, valid tests, dependencies, architecture, compatibility, and established error semantics.
5. Keep work within the report target plus directly coupled callers, tests, types, configuration, and documentation required for the correction. Treat public contracts, migrations, new dependencies, architecture changes, destructive work, and security/access-policy choices as execution stop conditions requiring separate approval.
6. Preserve valid tests. Change them only when an evidenced bug makes an expectation false or regression coverage is required; never weaken a test merely to permit a fix.
7. Define finding-level verification that proves the trigger is corrected, the invariant holds, regression coverage is credible, and unrelated behavior remains intact. Passing tests alone do not prove correctness.

Record unrelated improvements and pre-existing issues only as deferred follow-ups with a suitable next capability or `bug-hunt report <target>` invocation.
