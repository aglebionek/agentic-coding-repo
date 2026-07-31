# Code Workflow Specialist Contract

Internal specialists provide evidence and planning modules behind the
`code-workflow` facade. They are not directly invocable skills.

## Report contract

Every report is read-only and portable. It must:

- identify repository, revision, dirty state, selected profile, target,
  applicable instructions, checks, exclusions, and coverage limits;
- inventory the complete scope required by its evidence domain;
- use the specialist's exact report template and stable finding identifiers;
- distinguish observed evidence from inference and record counterevidence;
- preserve specialist-specific confidence, severity or reach, validity, scope,
  and stop conditions;
- avoid implementation plans and unrelated specialist concerns.

Begin every report with:

```md
# <Specialist> Report

## Result

- Valid: `true|false`
- Summary: `<one-sentence outcome>`
```

`Valid: true` means the report satisfied its documented scope, inventory, and
evidence requirements. Findings do not make a report invalid.

`Valid: false` is an actionable recovery handoff. It must identify the blocker,
reliable evidence, recommended resolution and tradeoff, useful locations,
conditions for a valid rerun, and the code-workflow profile/target to resume.
It must not contain a speculative plan.

## Artifact identity and freshness

The work package records the report source, repository, target or seed, revision,
dirty state, selected profile, and artifact location or in-context identifier.
Before planning, revalidate this identity plus cited contracts, evidence,
configuration, and scope.

Continue after immaterial drift and record it. Materially stale evidence,
incompatible repository or scope identity, incomplete inventory, or
`Valid: false` blocks planning and requires rerunning the report.

## Planner contract

Every planner is read-only and consumes a complete, valid, fresh report. It
must:

- use the specialist's exact plan template;
- preserve every stable finding and related clause, API, conversion, or
  guideline identifier;
- give every finding an explicit disposition;
- map every action exactly to its source evidence;
- preserve specialist confidence, severity or reach, boundaries, verification
  gates, and stop conditions;
- state exact files, symbols, ordered work, dependencies, preservation
  requirements, verification, risks, and deferred follow-ups;
- produce one definitive actionable path, not a menu of alternatives.

Probable findings remain conditional. Their named verification gate must
confirm them before they become implementation steps. If proof is unavailable
or fails, defer or reject them as the specialist requires.

## Workflow modes

- `manual` resolves material decisions interactively with `grill-me`, one
  question at a time, with a recommended answer.
- `autorun` makes only safe, evidence-backed decisions. It rejects invalid
  reports and stops rather than guessing through behavioral ambiguity,
  public-contract or migration changes, new dependencies, architecture changes,
  destructive work, or security/access-policy choices.

A specialist may define a stricter mode or stop condition. The facade and active
profile remain responsible for orchestration, approval, implementation,
validation, documentation, and external actions.

## Templates and reconciliation

Each specialist owns `REPORT.md`, `REPORT-TEMPLATE.md`, `PLANNER.md`,
`PLAN-TEMPLATE.md`, and any justified local references such as `CATALOG.md`.
Do not merge unlike identifier schemes or normalize distinct confidence,
severity, reach, classification, or validity vocabularies.

The code-workflow artifact contract reconciles specialist outputs into one work
package without rewriting them. Every accepted finding must remain attributable
and receive a final disposition.

## Testing authority

`shared/TESTING_GUIDELINES.md` is the sole testing authority. Specialists may
map evidence, findings, contracts, and risks to required proof, but they must not
restate test-first sequencing, preservation, test levels, dependency strategy,
hardening, or exception policy.
