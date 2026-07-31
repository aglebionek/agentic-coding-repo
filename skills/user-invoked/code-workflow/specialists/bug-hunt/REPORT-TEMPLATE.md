# Bug Hunt Report

## Result

- Valid: `true|false`
- Summary: `<one-sentence outcome>`

## Analysis state

- Repository: `<absolute root>`
- Revision: `<commit or state identifier>`
- Worktree: `<clean or concise dirty-state summary>`
- Invocation: `<exact invocation>`
- Requested target: `<path, codebase, or current changes>`
- Instructions: `<AGENTS.md and coding-guideline paths>`
- Checks run: `<commands and outcomes or none>`

## Scope inventory

- Analyzed artifacts: `<complete paths, grouped paths with counts, or attached inventory>`
- Artifact count: `<number>`
- Excluded: `<paths or patterns, reasons, and counts>`
- Context inspected: `<callers, callees, tests, contracts, history, and configuration>`
- Coverage limits: `<limits or none>`

For `current changes` also record:

- Changed artifacts: `<staged, unstaged, and relevant untracked inventory>`
- Directly affected behavior: `<boundary used for formal findings>`
- Deferred pre-existing leads: `<locations and suggested rerun invocations or none>`

## Audit coverage

Use only `analyzed`, `no evidence`, `not applicable`, or `not verifiable`.

| Category | Status | Evidence or explanation |
|---|---|---|
| Inputs and boundaries | `<status>` | `<inspection and locations>` |
| State and transitions | `<status>` | `<inspection and locations>` |
| Branches and invariants | `<status>` | `<inspection and locations>` |
| Errors and recovery | `<status>` | `<inspection and locations>` |
| Time and concurrency | `<status>` | `<inspection and locations>` |
| Data integrity | `<status>` | `<inspection and locations>` |
| Integration contracts | `<status>` | `<inspection and locations>` |
| Lifecycle and resources | `<status>` | `<inspection and locations>` |
| Tests as evidence | `<status>` | `<inspection and locations>` |

## Confirmed findings

State explicitly when there are none. Order by severity, then realistic reach.

### `BH-F1` — `<severity>` — `<short title>`

- Confidence: `confirmed`
- Violated invariant: `<truth the behavior must preserve>`
- Trigger: `<concrete inputs, state, timing, or sequence>`
- Execution path: `<relevant control and data flow>`
- Observable impact: `<incorrect behavior and affected consumers>`
- Evidence: `<exact paths, symbols or lines, traces, and checks>`
- Counterevidence: `<alternatives considered>`
- Correction direction: `<smallest behavioral correction, not an implementation plan>`

## Probable findings

### `BH-P1` — `<severity>` — `<short title>`

- Confidence: `probable`
- Violated invariant: `<expected truth>`
- Trigger and likely path: `<scenario and control or data flow>`
- Potential impact: `<realistic consequence and reach>`
- Evidence: `<supporting locations, traces, and checks>`
- Missing proof: `<one fact or safe verification step needed>`
- Counterevidence: `<alternatives considered>`
- Correction direction: `<conditional direction, not an implementation plan>`

## Investigated and dismissed

`<credible candidates examined, evidence that refuted them, or none>`

## Not verifiable

`<category or behavior, unavailable proof, materiality, and resolution; or none>`

## Resolution required

Required when `Valid: false`; otherwise write `None`.

- Blocker: `<exact unresolved prerequisite or question>`
- Reliable evidence: `<what is known>`
- Recommendation: `<recommended resolution and tradeoff>`
- Inspect: `<useful repository locations>`
- Valid rerun requires: `<condition>`
- Resume through: `<code-workflow profile and target>`

## Verdict and limitations

`<correctness assessment, planning readiness, and validation limits; no implementation plan>`
