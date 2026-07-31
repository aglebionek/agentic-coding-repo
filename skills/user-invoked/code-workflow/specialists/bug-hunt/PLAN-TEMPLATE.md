# Bug Hunt Correction Plan

## Inputs

- Report: `<path or in-context identifier>`
- Report valid: `true`
- Freshness: `<confirmed or immaterial drift>`
- Planning mode: `<manual|autorun>`
- Target: `<report target>`

## Outcome

- Summary: `<one definitive correction path>`
- Correct behavior: `<invariants and observable outcomes restored>`

## Finding dispositions

| Finding | Severity | Confidence | Disposition | Reason |
|---|---|---|---|---|
| `BH-F1` | `<severity>` | `confirmed` | `<fix|defer|reject>` | `<evidence-based reason>` |
| `BH-P1` | `<severity>` | `probable` | `<verify|defer|reject>` | `<evidence-based reason>` |

## Decisions

| Decision | Resolution | Basis |
|---|---|---|
| `<material decision>` | `<user-approved or autonomous answer>` | `<evidence and tradeoff>` |

## Change boundary

- Allowed: `<exact files, symbols, and directly coupled artifacts>`
- Preserved: `<unrelated behavior, interfaces, formats, errors, tests, dependencies, architecture, and compatibility>`
- Excluded: `<explicit exclusions>`

## Verification gates for probable findings

| Finding | Inspection or check | Confirmation evidence | If not confirmed |
|---|---|---|---|
| `BH-P1` | `<exact pre-fix verification>` | `<required observation>` | `<defer or reject>` |

## Correction steps

1. **`<step>`** — findings `<BH-Fn or verified BH-Pn>`
   - Files/symbols: `<exact targets>`
   - Intended behavior: `<invariant and observable outcome>`
   - Work: `<specific ordered edits and smallest correction>`
   - Dependencies: `<prior steps or none>`
   - Preservation requirements: `<contracts and unaffected behavior>`
   - Regression proof: `<test or focused reproduction>`

## Supporting artifacts

- Tests: `<preserve, add, or justified expectation change>`
- Types and interfaces: `<preserve or approved correction>`
- Callers and integrations: `<necessary work or preserve>`
- Configuration and data: `<necessary work or preserve>`
- Documentation: `<necessary factual update or preserve>`

## Verification

| Finding | Trigger proof | Invariant proof | Regression command or inspection | Expected result |
|---|---|---|---|---|
| `BH-F1` | `<failure no longer occurs>` | `<correct behavior established>` | `<focused check>` | `<observable result>` |

## Risks and execution stop conditions

- `<destructive work, security/access policy, unapproved boundary, material drift, or none>`

## Deferred follow-ups

- `<finding or unrelated lead, rationale, and suggested capability or invocation; or none>`
