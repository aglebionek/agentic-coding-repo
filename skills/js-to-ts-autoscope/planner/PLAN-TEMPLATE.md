# JS to TS Autoscope Plan

## Inputs

- Report: `<path or in-context identifier>`
- Report valid: `true`
- Freshness: `<confirmed or immaterial drift>`
- Planner mode: `<planner|autoplan>`
- Autoscope mode: `<deep|wide>`
- Seed: `<file, symbol, or small seed set>`

## Outcome

- Summary: `<one definitive conversion path>`
- Execution shape: `<oneshot|sequenced>`
- Spine invariant: `<behavior or exported hub contract to make explicit>`
- Converted APIs: `<JTA-An>`
- Conversion entries: `<JTA-Cn>`

## Finding Dispositions

| Finding | Classification | Disposition | Reason |
|---|---|---|---|
| `JTA-F1` | `<mechanical|required contract refactor|verification gap|stop condition>` | `<implement|verify|defer|reject>` | `<evidence-based reason>` |

## Decisions

| Decision | Resolution | Basis |
|---|---|---|
| `<for example, result contract shape>` | `<user-approved or autonomous answer>` | `<purpose evidence, guidelines, compatibility, tradeoff>` |

## Conversion Boundary

- Allowed editable files: `<exact paths from report plus justified additions>`
- Inspect-only evidence: `<paths not to edit>`
- Excluded: `<generated, vendor, static, template, broad registries, callers, or other exclusions>`
- Behavior and compatibility to preserve: `<purpose, route/API shape, data formats, error semantics, security/access constraints>`
- Guideline outcomes: `<explicit APIs, typed results, boundaries, effects, async/state, readability>`

## File And Import Map

| Source | Destination | Role | Imports, exports, callers, and configuration |
|---|---|---|---|
| `<src/file.js>` | `<src/file.ts>` | `<core|callee|caller|boundary|type-support|test-support>` | `<required coupled updates>` |

## Implementation Steps

For `oneshot`, use one ordered section. For `sequenced`, repeat this section per phase.

### Phase `<n>` - `<name>`

- Files/symbols: `<exact targets>`
- Findings: `<JTA-Fn>`
- APIs/conversions: `<JTA-An / JTA-Cn>`
- Work: `<specific edits, tests-first when behavior or contract changes>`
- Outcome: `<observable behavior and typed contract>`
- Dependencies: `<prior phases or none>`
- Checkpoint: `<strongest feasible verification and expected result>`
- Deferred known failures: `<what remains failing until a later phase, or none>`

## Contract And Supporting Changes

- Boundary types: `<inputs, outputs, unknown validation, exported surface>`
- Results and errors: `<typed operational outcomes and invariant failures>`
- Effects, state, and async: `<injection, transitions, concurrency, cleanup>`
- Tests: `<preserve, add, or change with behavioral reason>`
- Configuration/tooling: `<minimal required changes or preserve>`

## Verification

| API or conversion | Proof | Command or inspection | Expected result |
|---|---|---|---|
| `JTA-A1 / JTA-C1` | `<type safety, invariant, or behavior preservation>` | `<focused repository-native check>` | `<observable result>` |

## Risks And Stop Conditions

- `<public API, route shape, data format, security/access policy, migration, new dependency, generated/vendor edit, broad caller rewrite, architecture change, or none>`

## Deferred Follow-ups

- `<standards audit, broader conversion, purpose contract, unrelated improvement, or none>`
