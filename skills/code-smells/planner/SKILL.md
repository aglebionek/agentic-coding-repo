---
name: code-smells-planner
description: Converts a valid code-smells report into one read-only, evidence-mapped refactoring plan. Use only when the user invokes "code-smells planner", "code-smells autoplan", or "code-smells autoplan-force" with a report.
---

# Code Smells Planner

Produce a plan, not changes. Do not modify source, tests, configuration, documentation, generated artifacts, snapshots, or the Git index. Emit the plan in conversation unless the user supplies a plan path.

Read [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md) completely before planning.

## Validate the report

1. Require a complete code-smells report and identify its source.
2. Reject implementation planning when `Valid: false`.
   - In `autoplan` and `autoplan-force`, fail immediately without questions or interactive fallback.
   - In `planner`, optionally grill through recovery decisions, but output only a clarified report-rerun handoff.
3. Revalidate the repository, target inventory, cited structures, catalog fit, and analysis state. Record immaterial drift; reject materially stale or incomplete findings and recommend rerunning `code-smells report`.
4. Never treat bugs, vulnerabilities, style preferences, or uncatalogued design concerns as smell findings.

## Select mode

- `code-smells planner`: read [grill-me](../../grill-me/SKILL.md), resolve material decisions one question at a time, and recommend an answer. Preserve behavior and boundaries unless the user explicitly approves an exception.
- `code-smells autoplan`: make safe decisions independently and preserve runtime behavior, public interfaces, data formats, error semantics, valid tests, dependencies, and architecture. Reject material ambiguity or required boundary crossing with an actionable reason.
- `code-smells autoplan-force`: make decisions independently and may plan justified behavioral, public-interface, data-format, error-semantic, test-expectation, dependency, migration, or architectural changes. Enumerate each crossing, impact, migration, compatibility measure, and execution approval point.

All modes are read-only and produce one definitive actionable path. No autonomous mode may choose destructive work or security/access-policy changes; record these as execution stop conditions requiring user decisions.

## Build the plan

1. Give every confirmed finding a disposition: `refactor`, `defer`, or `reject`, with current evidence. Do not silently omit findings.
2. Give every probable finding a `verify`, `defer`, or `reject` disposition. Verification must precede any conditional refactoring action; if safe verification cannot be specified, defer it and recommend a narrower report rerun. Force mode never lowers this evidence threshold.
3. Consolidate compatible work while retaining mappings to every `CS-Fn` and `CS-Pn`. Do not turn a smell cluster back into repetitive occurrence-by-occurrence work.
4. For each action, state the intended maintenance outcome, exact files and symbols, ordered edits, dependencies, preservation requirements, and verification.
5. Prefer the smallest refactoring that removes the demonstrated maintenance effect. Do not assume every smell must be removed; preserve deliberate tradeoffs supported by counterevidence.
6. Preserve valid tests. Change tests only when approved behavior or contracts change, an expectation is obsolete, or regression coverage is needed; never weaken a test merely to permit refactoring.
7. Use repository-native checks and define structural and behavioral proof for each finding. Passing tests alone do not prove a smell was removed.

## Boundaries

In `planner` and `autoplan`, limit work to the target plus directly coupled callers, tests, types, and documentation needed for behavior-preserving refactoring. Treat public contracts, behavior, migrations, new dependencies, architecture, destructive work, and security/access policy as stop conditions unless interactive approval explicitly changes the boundary.

In `autoplan-force`, include justified boundary changes in the plan but keep destructive work and security/access-policy choices as stop conditions. Keep unrelated improvements in deferred follow-ups.
