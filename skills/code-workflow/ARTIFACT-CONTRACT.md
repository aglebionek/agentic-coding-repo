# Code Workflow Artifact Contract

## Work package

Maintain one work package throughout the workflow:

| Field | Required content |
|---|---|
| Profile and mode | `issue`, `bug-fix`, `improve`, `js-to-ts`, or `js-to-ts-autoscope`; `manual` or `autorun`; include `deep` or `wide` for `js-to-ts-autoscope` |
| Source | Issue URL/number, bug-hunt report or target, improvement target, conversion targets, or autoscope seed and scope mode |
| Analysis state | Repository, revision, dirty state, instructions, checks, and known baseline failures |
| Scope | Exact editable boundary, inspected context, exclusions, and directly coupled surfaces |
| Purpose | Governing approved notes and clauses, or explicit absence and its consequence |
| Acceptance | Observable required outcomes, preservation requirements, and non-goals |
| Documentation | Active profile and justified impact, including public reading entrypoints and canonical sources when applicable |
| Evidence | Complete specialist report identifiers, validity, freshness, and artifact locations |
| Decisions | User-approved or autonomous decisions with evidence and tradeoffs |
| Plan | One ordered implementation path mapped to source requirements and specialist IDs |
| Approval | Exact plan version and explicit user approval state |
| Execution | Completed steps, deviations, pauses, and supplemental approvals |
| Verification | Commands, inspections, expected results, actual results, and baseline comparison |
| Follow-ups | Deferred findings, residual risks, documentation gaps, and external actions not performed |

Emit the work package in conversation unless the user requests a path. Do not write planning artifacts into the source tree by default.

## Specialist artifact rules

Apply the [specialist contract](specialists/SPECIALIST-CONTRACT.md).

1. Keep each report and plan intact and attributable. Reference `BH-*`, `CS-*`,
   `CSA-*`, `PA-*`, `ARCH-*`, `JT-*`, and `JTA-*` IDs exactly.
2. A synthesized plan must disposition every finding accepted from every input plan. Never silently drop, rename, or merge findings.
3. Preserve each specialist's confidence, severity or reach, validity, scope, preservation rules, and stop conditions. Do not compare unlike severity schemes.
4. Probable findings retain their verification gates. They cannot become implementation steps until the named proof confirms them.
5. `Valid: false`, material staleness, or incompatible scopes block synthesis from that artifact. Record recovery and rerun the specialist instead.

Architecture findings retain their own reach and confidence fields; do not
convert them into another specialist's severity system. Preserve the compared
designs, selected structure, authority, consumer inventory, compatibility
strategy, and interactive decisions from an architecture plan.

## Bug regression proof

Every synthesized plan that fixes a bug-hunt finding must include durable regression proof mapped to the original finding ID.
Apply the shared `TESTING_GUIDELINES.md` as the canonical testing policy.

- Fixed confirmed findings, such as `BH-Fn`, require a specific regression test, focused reproduction check, or explicitly justified non-test proof.
- Fixed probable findings, such as verified `BH-Pn`, require the pre-fix confirmation gate first, then the same regression-proof requirement as confirmed findings.
- Select the proof level and any justified alternate proof under the shared
  testing guideline, then preserve the decision through implementation and
  completion reporting.

## Authority and conflict resolution

Use this order to detect conflicts, not to silently override them:

1. Explicit user decisions and approved purpose contracts
2. Public interfaces, data contracts, migrations, security/access policy, and established compatibility constraints
3. Accepted issue outcomes reconciled with purpose
4. Evidenced runtime invariants and correctness findings
5. Governing coding guidelines and accepted deviations
6. Catalogued maintainability findings
7. Documentation statements outside an approved `## Intended purpose` contract

When two authorities conflict, stop and expose the contradiction. Manual mode grills toward one approved answer. Autorun records the evidence and returns the exact decision required.

## Synthesized plan requirements

The plan must state:

- intended observable outcome and exact change boundary
- source acceptance criteria and specialist IDs addressed by each step
- files, symbols, ordered edits, dependencies, and preservation requirements
- tests, types, callers, configuration, and documentation affected
- applicable architecture constraints, public reading entrypoints, and
  compatibility or migration surfaces when they materially apply
- focused proof for each acceptance criterion and finding
- bug regression proof for every fixed `BH-*` finding, including justified non-test proof when applicable
- risks, execution stop conditions, deferred findings, and external actions

The plan is versioned by its content. Any new edit, expanded boundary, or changed behavior discovered during execution requires a supplemental plan and explicit approval.
