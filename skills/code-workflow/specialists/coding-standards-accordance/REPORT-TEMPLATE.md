# Coding Standards Accordance Report

## Result

- Valid: `true|false`
- Summary: `<one-sentence outcome>`

## Analysis state

- Repository: `<absolute root>`
- Revision: `<commit or state identifier>`
- Worktree: `<clean or concise dirty-state summary>`
- Invocation: `<exact report invocation>`
- Target: `<repository-relative path, codebase, or current changes>`
- Instructions: `<AGENTS.md and CODING_GUIDELINES.md paths>`
- Checks run: `<commands and outcomes or none>`

## Inventory

- Included: `<complete JS/TS file list or a path to an embedded grouped inventory>`
- Excluded: `<paths or categories with reasons>`
- Supporting evidence outside inventory: `<paths and purpose or none>`

## Guideline coverage

Use only `accords`, `violation`, `accepted deviation`, `not applicable`, or `not verifiable`.

| Guideline | Requirement | Status | Evidence |
|---|---|---|---|
| `CSA-G1` | `<concise rule>` | `<status>` | `<locations and analysis>` |

## Accepted deviations

State explicitly when there are none.

### `CSA-D1` — `<short title>`

- Guideline: `<CSA-Gn>`
- Constraint: `<concrete reason the default design is unsuitable>`
- Evidence: `<repository locations or checks>`
- Preserved intent: `<how the alternative fulfills the guideline's purpose>`
- Scope: `<affected files and symbols>`

## Findings

Order by severity, then dependency. State explicitly when there are none.

### `CSA-F1` — `<high|medium|low>` — `<short title>`

- Guideline: `<CSA-Gn and CODING_GUIDELINES.md section>`
- Violation: `<actual design and why it does not accord>`
- Scenario: `<concrete inputs, state, or change sequence where useful>`
- Impact: `<behavioral or maintenance consequence and reach>`
- Evidence: `<paths, symbols or lines, checks, callers, types, or tests>`
- Counterevidence: `<evidence considered or none>`
- Correction direction: `<smallest standards-aligned direction, not a plan>`

## Not verifiable

`<guidelines, missing proof, impact on the judgment, and what would make them verifiable; or none>`

## Out-of-scope follow-ups

`<neighboring concern, evidence, and suitable code-workflow profile; or none>`

## Resolution required

Required when `Valid: false`; otherwise write `None`.

- Blocker: `<exact unresolved prerequisite or question>`
- Recommendation: `<recommended resolution and tradeoff>`
- Inspect: `<useful repository locations>`
- Valid rerun requires: `<condition>`
- Resume through: `<code-workflow profile and target>`

## Verdict and limitations

`<accords, violations found, or judgment blocked; include validation limits>`
