# JS to TS Autoscope Report

## Result

- Valid: `true|false`
- Summary: `<one-sentence outcome>`

## Analysis State

- Repository: `<absolute root>`
- Revision: `<commit or state identifier>`
- Worktree: `<clean or concise dirty-state summary>`
- Invocation: `code-workflow js-to-ts-autoscope <seed> [deep|wide] [manual|autorun]`
- Mode: `<deep|wide>`
- Seed: `<file, symbol, or small seed set>`
- Instructions consulted: `<AGENTS.md, CODING_GUIDELINES.md, related skills>`
- Discovery and checks run: `<commands and outcomes or none>`

## Scope And Tooling

- Supported target: `<why the seed is acceptable>`
- Rejected scope: `<broad, generated, vendor, static, template, or unsupported scope; or none>`
- Effective configuration: `<tsconfig, package/module mode, lint, test, build sources>`
- Destination convention: `<.ts or .tsx and path rules>`
- Verification commands available: `<repository-native checks>`

## Selected Spine

- Spine name: `<short behavior/codepath name>`
- Shape: `<deep|wide>`
- Spine invariant: `<single behavior or exported hub contract the conversion must make explicit>`
- Purpose evidence: `<inferred or approved purpose, with locations>`
- Value: `<contained leverage, boundary value, guideline relevance, and why this is worth converting>`
- Traversal summary: `<seed, upward/downward hops, fan-out limits, and why expansion stops>`

## File Roles

| File | Role | Editability | Why Included Or Excluded | Evidence |
|---|---|---|---|---|
| `<path>` | `<seed|core|callee|caller|boundary|type-support|test-support|inspect-only>` | `<editable|inspect-only|excluded>` | `<coupling and conversion reason>` | `<locations>` |

## Behavior And API Inventory

| ID | File or symbol | Current contract | Effects and failures | Dependencies and consumers | Evidence |
|---|---|---|---|---|---|
| `JTA-A1` | `<path#symbol>` | `<inputs, outputs, outcomes>` | `<I/O, mutation, thrown/returned errors, async/lifecycle>` | `<imports, exports, callers, runtime wiring>` | `<locations>` |

## Conversion Map

| ID | Source | Destination | Required coupled changes | Classification |
|---|---|---|---|---|
| `JTA-C1` | `<file.js>` | `<file.ts>` | `<imports, callers, tests, types, or config>` | `<mechanical|required contract refactor|verification support>` |

## Guideline Assessment

Use `adheres`, `finding`, `not verifiable`, or `not applicable`.

| Dimension | Status | Evidence and required outcome |
|---|---|---|
| Explicit APIs | `<status>` | `<boundary inputs, outputs, invalid outcomes, exports>` |
| Functional core and effects | `<status>` | `<decision/effect separation>` |
| Boundaries and dependencies | `<status>` | `<trust validation, dependency direction, env/config use>` |
| Results and errors | `<status>` | `<typed outcomes, sentinels, thrown errors>` |
| State, async, and lifecycle | `<status>` | `<transitions, concurrency, cleanup>` |
| Readability | `<status>` | `<ownership, naming, scope>` |
| Tests | `<status>` | `<verification readiness only; not selection value>` |

## Findings

State explicitly when there are none. Order by conversion dependency, then impact.

### `JTA-F1` - `<mechanical|required contract refactor|verification gap|stop condition>` - `<short title>`

- Applies to: `<JTA-An and JTA-Cn>`
- Scenario: `<concrete input, state, event, import, or call path>`
- Impact: `<type-safety, guideline, runtime, compatibility, or verification consequence>`
- Required outcome: `<behavior/purpose-preserving conversion requirement or stop>`
- Evidence: `<files, lines, configuration, callers, tests, or check output>`

## Verification Readiness

- Existing proof: `<tests, runtime path, contracts, or none>`
- Missing proof: `<what the planner must add or verify>`
- Non-test proof: `<inspection or command that may be enough, or none>`
- Baseline limitations: `<pre-existing failures or not verifiable items>`

## Resolution Required

Required when `Valid: false`; otherwise write `None`.

- Blocker: `<exact unresolved prerequisite>`
- Recommendation: `<recommended resolution and tradeoff>`
- Suggested seeds: `<only for broad/invalid seed scope>`
- Inspect: `<useful repository locations>`
- Valid rerun requires: `<condition>`
- Resume through: `code-workflow js-to-ts-autoscope <seed> [deep|wide] [manual|autorun]`

## Verdict And Limits

`<planning readiness, selected spine limits, explicit exclusions, and stop conditions>`
