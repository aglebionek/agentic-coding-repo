# Architecture Plan

## Inputs

- Report: `<path or in-context identifier>`
- Report valid: `true`
- Freshness: `<confirmed or immaterial drift>`
- Planning mode: `manual`
- Selected findings: `<one ARCH-* finding or inseparable cluster>`

## Finding dispositions

| Finding | Reach | Confidence | Disposition | Reason |
|---|---|---|---|---|
| `ARCH-1` | `<reach>` | `<confidence>` | `<plan|defer|reject>` | `<evidence-based reason>` |

## Authority and constraints

- Responsibility/ownership authority: `<approved source>`
- Public contract: `<source and preserved behavior>`
- Applicable decisions: `<sources or none>`
- Callers and consumers: `<complete inventory>`
- Compatibility surfaces: `<paths, interfaces, formats, or none>`
- Documentation profile and impact: `<roles, locations, and needed updates>`
- Missing authority resolved: `<decision and source, or none>`

## Compared designs

### Design A — `<name>`

- Primary interface: `<API, invariants, effects, ordering, errors>`
- Hidden implementation and nested APIs: `<knowledge and structure>`
- Seams and dependencies: `<placement, adapters, and rationale>`
- Representative caller: `<usage>`
- Compatibility/migration: `<strategy>`
- Test surface: `<stable behavioral contract>`
- Documentation impact: `<public reading and decision effects>`

### Design B — `<name>`

- Primary interface: `<API, invariants, effects, ordering, errors>`
- Hidden implementation and nested APIs: `<knowledge and structure>`
- Seams and dependencies: `<placement, adapters, and rationale>`
- Representative caller: `<usage>`
- Compatibility/migration: `<strategy>`
- Test surface: `<stable behavioral contract>`
- Documentation impact: `<public reading and decision effects>`

## Comparison and decision

| Criterion | Design A | Design B |
|---|---|---|
| Depth and leverage | `<assessment>` | `<assessment>` |
| Locality and ownership | `<assessment>` | `<assessment>` |
| Navigability | `<assessment>` | `<assessment>` |
| Testing | `<assessment>` | `<assessment>` |
| Migration cost and compatibility | `<assessment>` | `<assessment>` |

- Recommendation: `<design and rationale>`
- User decision: `<selected design and rationale>`
- Rejected tradeoffs: `<material alternatives not chosen>`

## Change boundary

- Allowed: `<exact files, symbols, callers, tests, and planned docs>`
- Preserved: `<behavior, interfaces, formats, errors, tests, dependencies, and compatibility>`
- Excluded: `<explicit exclusions including facade removal when applicable>`

## Implementation steps

1. **`<step>`** — findings `<ARCH-*>`
   - Files/symbols: `<targets>`
   - Responsibility outcome: `<knowledge made local or contract clarified>`
   - Work: `<specific approved actions>`
   - Dependencies: `<prior steps or none>`
   - Compatibility: `<consumer/facade action and proof>`

## Testing and verification

| Finding/contract | Proof | Command or inspection | Expected result |
|---|---|---|---|
| `ARCH-1` | `<red/green/hardening or behavior-preservation proof>` | `<focused check>` | `<observable result>` |

- Existing tests: `<preserve, mechanically move, or explicitly approved replacement>`
- Broader verification: `<types, integration, build, navigation, and link checks>`

## Documentation and decisions

- Approved decisions to record through grow-docs: `<items or none>`
- Navigation/public reading updates: `<items or none>`
- Canonical sources to preserve: `<sources>`

## Risks and execution stop conditions

- `<new authority, contract, compatibility, migration, dependency, destructive, security, or test-expectation decision; or none>`

## Deferred follow-ups

- `<unselected finding, facade removal, residual risk, or none>`
