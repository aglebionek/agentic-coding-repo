# Architecture Report

## Result

- Valid: `true|false`
- Summary: `<one-sentence outcome>`

## Analysis state

- Repository: `<absolute root>`
- Revision: `<commit or state identifier>`
- Worktree: `<clean or concise dirty-state summary>`
- Profile: `improve`
- Target: `<repository-relative paths or symbols>`
- Applicable instructions: `<paths>`
- Architecture and decision authority: `<paths or explicit absence>`
- Documentation profile: `<discovered roles and locations>`
- Checks run: `<commands and outcomes or none>`
- Exclusions and coverage limits: `<limits or none>`

## Responsibility inventory

| Responsibility | Observed structure | Inferred ownership | Interfaces and entrypoints | Callers/consumers | Evidence |
|---|---|---|---|---|---|
| `<name>` | `<modules and relationships>` | `<inference plus authority/confidence>` | `<public and nested surfaces>` | `<locations>` | `<files, docs, tests, history, or checks>` |

## Surface inventory

| Surface | Present evidence | Missing or ambiguous | Consequence |
|---|---|---|---|
| Responsibility/parent navigation | `<locations or none>` | `<gap or none>` | `<impact>` |
| Related technical documentation | `<locations or none>` | `<gap or none>` | `<impact>` |
| Public reading entrypoint | `<locations or none>` | `<gap or none>` | `<impact>` |
| Purpose/ownership authority | `<locations or none>` | `<gap or none>` | `<impact>` |
| Canonical decision record | `<locations or none>` | `<gap or none>` | `<impact>` |
| Tests/behavioral evidence | `<locations or none>` | `<gap or none>` | `<impact>` |
| Compatibility/consumer documentation | `<locations or none>` | `<gap or none>` | `<impact>` |

## Findings

Order findings by dependency and reach. State explicitly when there are none.

### `ARCH-1` — `<short diagnostic title>`

- Responsibility and files: `<owned responsibility and locations>`
- Observed friction: `<diagnostic statement>`
- Evidence: `<concrete traces, checks, or examples>`
- Caller burden: `<knowledge or coordination leaked to callers>`
- Maintainer burden: `<scattered change, defects, verification, or navigation>`
- Impact: `<locality, leverage, navigability, testing, compatibility, or safe change>`
- Constraints and decisions: `<applicable authority and preservation rules>`
- Reach: `<local|multi-module|subsystem|cross-system>`
- Confidence: `<high|medium|low, with reason>`
- Missing surfaces: `<attached gaps and consequence, or none>`
- Improvement direction: `<knowledge/locality/facade direction without a concrete interface or migration plan>`

## Counterevidence and limitations

`<evidence against findings, unknowns, unavailable proof, and confidence effects>`

## Out-of-scope follow-ups

`<neighboring concern and appropriate specialist/profile, or none>`

## Resolution required

Required when `Valid: false`; otherwise write `None`.

- Blocker: `<exact unresolved prerequisite>`
- Recommendation: `<recommended resolution and tradeoff>`
- Inspect: `<useful repository locations>`
- Valid rerun requires: `<condition>`
- Resume through: `code-workflow improve <target> <manual|autorun>`

## Verdict

`<diagnostic conclusion and most consequential evidence>`
