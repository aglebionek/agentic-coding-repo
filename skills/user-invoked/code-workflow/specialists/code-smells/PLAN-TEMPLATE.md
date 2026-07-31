# Code Smells Refactoring Plan

## Inputs

- Report: `<path or in-context identifier>`
- Report valid: `true`
- Freshness: `<confirmed or immaterial drift>`
- Planning mode: `<manual|autorun|force>`
- Target: `<report target>`

## Outcome

- Summary: `<one definitive actionable path>`
- Maintenance effects addressed: `<concrete effects>`
- Behavior and contracts: `<preserved or explicitly crossed>`

## Finding dispositions

| Finding | Smell | Confidence | Disposition | Reason |
|---|---|---|---|---|
| `CS-F1` | `<canonical smell>` | `confirmed` | `<refactor|defer|reject>` | `<evidence-based reason>` |
| `CS-P1` | `<canonical smell>` | `probable` | `<verify|defer|reject>` | `<evidence-based reason>` |

## Decisions

| Decision | Resolution | Basis |
|---|---|---|
| `<decision>` | `<user-approved or autonomous answer>` | `<evidence and tradeoff>` |

## Change boundary

- Allowed: `<exact files, symbols, and directly coupled artifacts>`
- Preserved: `<behavior, interfaces, formats, errors, tests, dependencies, and architecture>`
- Excluded: `<explicit exclusions>`

## Boundary crossings

Required for every exception in `manual` and every crossing in `force`;
otherwise write `None`.

| Boundary | Justification | Impact | Migration or compatibility | Execution approval point |
|---|---|---|---|---|
| `<behavior, public interface, data, errors, tests, dependency, or architecture>` | `<finding evidence>` | `<consumers and consequences>` | `<required measures>` | `<when execution must stop>` |

## Verification gates for probable findings

| Finding | Inspection or check | Confirmation evidence | If not confirmed |
|---|---|---|---|
| `CS-P1` | `<exact pre-refactoring verification>` | `<required observation>` | `<defer or reject>` |

## Refactoring steps

1. **`<step>`** — findings `<CS-Fn or verified CS-Pn>`
   - Files/symbols: `<exact targets>`
   - Maintenance outcome: `<effect removed or reduced>`
   - Work: `<specific ordered edits>`
   - Preservation requirements: `<behavior and boundaries>`
   - Dependencies: `<prior steps or none>`

## Supporting artifacts

- Tests: `<preserve, add, or approved change with reason>`
- Types and interfaces: `<preserve or approved change>`
- Callers: `<necessary integration work or preserve>`
- Documentation: `<necessary factual updates or preserve>`

## Verification

| Finding | Structural proof | Behavioral proof | Command or inspection | Expected result |
|---|---|---|---|---|
| `CS-F1` | `<catalog criterion no longer applies>` | `<preserved or approved behavior>` | `<focused check>` | `<observable result>` |

## Risks and execution stop conditions

- `<destructive, security/access-policy, unapproved boundary, material drift, or none>`

## Deferred follow-ups

- `<finding or unrelated concern, rationale, and suggested capability; or none>`
