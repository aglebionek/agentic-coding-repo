# Purpose Adherence Report

## Result

- Valid: `true|false`
- Summary: `<one-sentence outcome>`

## Analysis state

- Repository: `<absolute root>`
- Revision: `<commit or state identifier>`
- Worktree: `<clean or concise dirty-state summary>`
- Targets: `<repository-relative paths or symbols>`
- Additional documentation paths: `<paths or none>`
- Checks run: `<commands and outcomes or none>`

## Purpose contract

- Governing notes: `<paths>`
- Applies to: `<paths and symbols>`

| Clause | Intended behavior | Source |
|---|---|---|
| `PA-C1` | `<responsibility, requirement, prohibition, or applicable contract rule>` | `<note and heading>` |

## Prerequisites and contract conflicts

`<none, or missing/inapplicable/ambiguous/conflicting contract details>`

## Clause coverage

Use only `adheres`, `mismatch`, `not verifiable`, or `not applicable`.

| Clause | Implementation | Types | Tests | Docs | Callers | Evidence |
|---|---|---|---|---|---|---|
| `PA-C1` | `<status>` | `<status>` | `<status>` | `<status>` | `<status>` | `<locations and concise trace>` |

## Findings

Order findings by severity, then dependency. State explicitly when there are none.

### `PA-F1` — `<critical|high|medium|low>` — `<short title>`

- Purpose clause: `<PA-Cn>`
- Mismatch: `<missing|excessive|contradictory|contract-surface drift>`
- Expected behavior: `<contract requirement and source>`
- Actual behavior: `<logic trace and code locations>`
- Scenario: `<concrete inputs, state, or event sequence>`
- Impact: `<observable outcome and reach>`
- Certainty: `confirmed`
- Evidence: `<files, lines, checks, types, tests, callers, or docs>`

## Not verifiable

`<clauses, suspected mismatches, unresolved assumptions, unavailable proof, and what would make them verifiable; or none>`

## Out-of-scope follow-ups

`<neighboring concerns and appropriate specialist skill; or none>`

## Resolution required

Required when `Valid: false`; otherwise write `None`.

- Blocker: `<exact unresolved prerequisite or question>`
- Recommendation: `<recommended resolution and tradeoff>`
- Inspect: `<useful repository locations>`
- Valid rerun requires: `<condition>`
- Next invocation: `<exact suggested command or prompt>`

## Verdict and limitations

`<adheres, mismatches found, or judgment blocked; include validation limits>`
