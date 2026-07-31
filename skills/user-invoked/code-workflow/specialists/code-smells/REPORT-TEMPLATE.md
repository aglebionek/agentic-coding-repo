# Code Smells Report

## Result

- Valid: `true|false`
- Summary: `<one-sentence outcome>`

## Analysis state

- Repository: `<absolute root>`
- Revision: `<commit or state identifier>`
- Worktree: `<clean or concise dirty-state summary>`
- Invocation: `<exact invocation>`
- Requested target: `<repository-relative path or codebase>`
- Instructions: `<AGENTS.md and coding-guideline paths>`
- Checks run: `<commands and outcomes or none>`

## Scope inventory

- Analyzed source: `<complete paths, grouped paths with counts, or attached inventory>`
- Source-file count: `<number>`
- Excluded: `<paths or patterns, reasons, and counts>`
- Context inspected: `<callers, collaborators, history, and tests used as evidence>`
- Coverage limits: `<limits or none>`

## Catalog coverage

Use only `detected`, `no evidence`, `not applicable`, or `not verifiable`. Include all 24 canonical smells.

| Smell | Status | Evidence or explanation |
|---|---|---|
| Mysterious Name | `<status>` | `<locations, inspection, or rationale>` |
| Duplicated Code | `<status>` | `<locations, inspection, or rationale>` |
| Long Function | `<status>` | `<locations, inspection, or rationale>` |
| Long Parameter List | `<status>` | `<locations, inspection, or rationale>` |
| Global Data | `<status>` | `<locations, inspection, or rationale>` |
| Mutable Data | `<status>` | `<locations, inspection, or rationale>` |
| Divergent Change | `<status>` | `<locations, inspection, or rationale>` |
| Shotgun Surgery | `<status>` | `<locations, inspection, or rationale>` |
| Feature Envy | `<status>` | `<locations, inspection, or rationale>` |
| Data Clumps | `<status>` | `<locations, inspection, or rationale>` |
| Primitive Obsession | `<status>` | `<locations, inspection, or rationale>` |
| Repeated Switches | `<status>` | `<locations, inspection, or rationale>` |
| Loops | `<status>` | `<locations, inspection, or rationale>` |
| Lazy Element | `<status>` | `<locations, inspection, or rationale>` |
| Speculative Generality | `<status>` | `<locations, inspection, or rationale>` |
| Temporary Field | `<status>` | `<locations, inspection, or rationale>` |
| Message Chains | `<status>` | `<locations, inspection, or rationale>` |
| Middle Man | `<status>` | `<locations, inspection, or rationale>` |
| Insider Trading | `<status>` | `<locations, inspection, or rationale>` |
| Large Class | `<status>` | `<locations, inspection, or rationale>` |
| Alternative Classes with Different Interfaces | `<status>` | `<locations, inspection, or rationale>` |
| Data Class | `<status>` | `<locations, inspection, or rationale>` |
| Refused Bequest | `<status>` | `<locations, inspection, or rationale>` |
| Comments | `<status>` | `<locations, inspection, or rationale>` |

## Confirmed findings

State explicitly when there are none. Order by dependency and reach, not severity.

### `CS-F1` — `<Canonical Smell>` — `<short title>`

- Confidence: `confirmed`
- Reach: `<local|multi-file|cross-cutting>`
- Maintenance effect: `<demonstrated comprehension, change, ownership, duplication, or testing consequence>`
- Catalog fit: `<why the canonical diagnostic criterion applies>`
- Evidence: `<exact paths, symbols or lines, traces, and checks>`
- Consolidation: `<underlying cause, affected locations, and count>`
- Counterevidence: `<alternatives or false positives considered>`

## Probable findings

### `CS-P1` — `<Canonical Smell>` — `<short title>`

- Confidence: `probable`
- Reach: `<local|multi-file|cross-cutting>`
- Maintenance effect: `<evidenced consequence>`
- Evidence: `<supporting locations and traces>`
- Missing proof: `<specific inspection needed for confirmation>`
- Counterevidence: `<alternatives or false positives considered>`

## Not verifiable

`<catalog entries, source, unavailable proof, and what would resolve them; or none>`

## Resolution required

Required when `Valid: false`; otherwise write `None`.

- Blocker: `<exact unresolved prerequisite or question>`
- Reliable evidence: `<what is known>`
- Recommendation: `<recommended resolution and tradeoff>`
- Inspect: `<useful repository locations>`
- Valid rerun requires: `<condition>`
- Resume through: `<code-workflow profile and target>`

## Verdict and limitations

`<catalog assessment, planning readiness, and validation limits; no refactoring plan>`
