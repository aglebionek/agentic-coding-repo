# JS to TS Plan

## Inputs

- Report: `<path or in-context identifier>`
- Report valid: `true`
- Freshness: `<confirmed or immaterial drift>`
- Planning mode: `<planner|autoplan>`

## Outcome

- Summary: `<one definitive, behavior-preserving conversion path>`
- Converted APIs: `<JT-An>`
- Conversion entries: `<JT-Cn>`

## Finding dispositions

| Finding | Classification | Disposition | Reason |
|---|---|---|---|
| `JT-F1` | `<mechanical|required contract refactor|deferred improvement>` | `<implement|defer|reject>` | `<evidence-based reason>` |

## Decisions

| Decision | Resolution | Basis |
|---|---|---|
| `<for example, .ts versus .tsx>` | `<user-approved or autonomous answer>` | `<configuration, behavior, and tradeoff>` |

## Conversion boundary

- Allowed: `<exact targets, coupled files, symbols, and configuration>`
- Excluded: `<generated, vendored, unrelated, or separately approved work>`
- Behavior to preserve: `<observable contracts>`

## File and import map

| Source | Destination | Imports, exports, callers, and configuration |
|---|---|---|
| `<src/file.js>` | `<src/file.ts>` | `<required coupled updates>` |

## Implementation steps

1. **`<step>`** — findings `<JT-Fn>`; APIs `<JT-An>`; conversions `<JT-Cn>`
   - Files/symbols: `<exact targets>`
   - Outcome: `<observable behavior and typed contract>`
   - Work: `<specific actions, including tests-first where behavior changes>`
   - Dependencies: `<prior steps or none>`

## Contract and supporting changes

- Boundary types: `<explicit inputs, outputs, unknown validation, and exported surface>`
- Results and errors: `<typed operational outcomes and invariant failures>`
- Effects, state, and async: `<injection, transitions, concurrency, and cleanup>`
- Tests: `<preserve, add, or change with behavioral reason>`
- Configuration/tooling: `<minimal required changes or preserve>`

## Verification

| API or conversion | Proof | Command or inspection | Expected result |
|---|---|---|---|
| `JT-A1 / JT-C1` | `<type safety and behavior preservation>` | `<focused repository-native check>` | `<observable result>` |

## Risks and execution stop conditions

- `<public API, migration, architecture, destructive, security, generated-code, or semantic boundary; or none>`

## Deferred follow-ups

- `<unrelated improvement, rationale, and appropriate specialist skill; or none>`
