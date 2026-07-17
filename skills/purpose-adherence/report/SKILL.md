---
name: purpose-adherence-report
description: Audits whether code behavior, types, tests, callers, and related docs adhere exactly to an approved Obsidian purpose contract. Use only when the user explicitly invokes "purpose-adherence report" with code targets and optional documentation paths.
---

# Purpose Adherence Report

Produce a read-only, portable report. Do not modify code, types, tests, documentation, the Git index, or snapshots. Emit the report in conversation unless the user supplies a report path.

Read [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md) completely before reporting.

## Establish scope and contract

1. Read the applicable `AGENTS.md` and root `CODING_GUIDELINES.md`.
2. Record the repository root, revision, dirty-worktree state, targets, and user-supplied documentation paths.
3. Search applicable documentation locations and supplied paths for exact `## Intended purpose` headings.
4. Accept a contract only when its `Applies to` clause unambiguously covers the target.
5. Compose compatible contracts across concept levels. A narrower contract may specialize but never silently contradict a broader one.
6. Return `Valid: false` for missing, ambiguous, conflicting, or inapplicable contracts.
7. For broad or mixed scopes, separate coherent contract groups. Return `Valid: false` with recommended narrower groups when adequate clause-level analysis is impractical.

Other docs, issues, plans, tests, types, callers, implementation, history, comments, and naming are not purpose authorities. They are surfaces to check against `## Intended purpose`; purpose inference belongs to `infer-purpose`.

## Audit adherence

1. Number every responsibility, required behavior, forbidden behavior, and applicable invariant, input, output, transition, side effect, error rule, or external contract.
2. Read enough implementation, types, imports, callers, tests, configs, and related docs to trace every clause.
3. Mark each surface `adheres`, `mismatch`, `not verifiable`, or `not applicable`, with evidence. Passing tests alone never prove adherence.
4. Report only logic-specific mismatches: missing, excessive, contradictory, or contract-inadherent behavior. Exclude generic bugs, invalid code, architecture smells, standards violations, and missing tests unless they cause, conceal, or prevent verification of a purpose mismatch.
5. Every confirmed finding must cite the purpose clause and source, actual code path, concrete scenario, observable impact, mismatch kind, certainty, and evidence locations.
6. Assign behavioral severity:
   - `critical`: security/access violation, data loss/corruption, severe external breach, or fundamentally unsafe behavior
   - `high`: core-purpose failure, common or broad impact, or serious incorrect behavior
   - `medium`: bounded or less frequent violation with limited impact or a practical workaround
   - `low`: minor missing or excessive behavior without immediate operational risk

Rate contract-surface drift by the behavior it can permit or conceal; stale documentation is not automatically low severity.

Run the smallest useful non-destructive tests or checks when they materially strengthen evidence. Never update fixtures or snapshots. Separate pre-existing failures and record commands and results; use `not verifiable` when safe proof is unavailable.

## Set validity

Use `Valid: true` when one coherent applicable contract exists and every clause received meaningful analysis, even if some dimensions remain explicitly unknown or not verifiable. Mismatches do not make the report invalid.

Use `Valid: false` when prerequisites, scope, contract meaning, or evidence prevent a coherent adherence judgment. Make the report a self-contained recovery handoff with exact blockers, recommendations, repository locations, rerun conditions, and the next invocation. Never include a speculative implementation plan.
