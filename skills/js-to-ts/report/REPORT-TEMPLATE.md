# JS to TS Report

## Result

- Valid: `true|false`
- Summary: `<one-sentence outcome>`

## Analysis state

- Repository: `<absolute root>`
- Revision: `<commit or state identifier>`
- Worktree: `<clean or concise dirty-state summary>`
- Requested targets: `<repository-relative .js/.jsx paths or symbols>`
- Checks run: `<commands and outcomes or none>`

## Scope and toolchain

- Conversion boundary: `<targets and directly coupled surfaces>`
- Excluded: `<generated, vendored, unrelated, or other excluded surfaces>`
- Destinations: `<for example, src/price.js -> src/price.ts>`
- Effective configuration: `<tsconfig, package/module mode, lint, test, and build sources>`
- Verification commands: `<repository-native commands>`

## Behavior and API inventory

| ID | Target or symbol | Inputs and outputs | Effects and failures | Dependencies and consumers | Evidence |
|---|---|---|---|---|---|
| `JT-A1` | `<path#symbol>` | `<observable contract>` | `<effects, outcomes, async/lifecycle rules>` | `<imports, callers, runtime consumers>` | `<locations>` |

## Conversion map

| ID | Source | Destination | Required coupled changes | Classification |
|---|---|---|---|---|
| `JT-C1` | `<file.js>` | `<file.ts>` | `<imports, callers, tests, or config>` | `<mechanical|required contract refactor>` |

## Coding-guideline assessment

Use `adheres`, `finding`, `not verifiable`, or `not applicable`.

| Dimension | Status | Evidence and required outcome |
|---|---|---|
| Explicit APIs | `<status>` | `<inputs, outputs, invalid outcomes, export surface>` |
| Functional core and effects | `<status>` | `<decision/effect boundary>` |
| Boundaries and dependencies | `<status>` | `<trust validation and dependency direction>` |
| Results and errors | `<status>` | `<expected outcomes and invariants>` |
| State, async, and lifecycle | `<status>` | `<transitions, concurrency, cleanup>` |
| UI and state management | `<status>` | `<rendering versus durable behavior>` |
| Readability | `<status>` | `<ownership and scoped changes>` |
| Tests | `<status>` | `<public behavior and deterministic coverage>` |

## Findings

State explicitly when there are none. Order by conversion dependency, then impact.

### `JT-F1` — `<mechanical|required contract refactor|deferred improvement>` — `<short title>`

- Applies to: `<JT-An and JT-Cn>`
- Scenario: `<concrete input, state, or event sequence>`
- Impact: `<runtime, contract, type-safety, or verification consequence>`
- Required outcome: `<behavior-preserving conversion requirement>`
- Evidence: `<files, lines, configuration, callers, tests, or check output>`

## Baseline and not verifiable

- Baseline: `<focused checks and pre-existing failures>`
- Not verifiable: `<unknowns, unavailable proof, and what would resolve them; or none>`

## Resolution required

Required when `Valid: false`; otherwise write `None`.

- Blocker: `<exact unresolved prerequisite or question>`
- Recommendation: `<recommended resolution and tradeoff>`
- Inspect: `<useful repository locations>`
- Valid rerun requires: `<condition>`
- Next invocation: `js-to-ts report <targets>`

## Verdict and limitations

`<planning readiness, key conversion constraints, and validation limits>`
