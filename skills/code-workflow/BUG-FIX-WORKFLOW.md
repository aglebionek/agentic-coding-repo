# Bug Fix Workflow

Use for `code-workflow bug-fix <bug-hunt-report-or-file-or-directory> [manual|autorun]`.

## Intake

1. Accept either a complete bug-hunt report or an explicit source target.
2. If the input is a report, verify its validity, freshness, repository, scope, cited behavior, evidence, and drift before planning from it.
3. If the input is a source target, run [bug-hunt report](../bug-hunt/report/SKILL.md) for that target before planning.
4. Treat reported current behavior as evidence, not purpose authority. Reconcile intended correction with approved purpose, public contracts, compatibility, and established error semantics.
5. Record the exact bug trigger, violated invariant, observable impact, affected consumers, non-goals, and any missing reproduction facts.

If the bug target, intended correct behavior, or reproduction path is materially ambiguous, manual mode grills one material question at a time. Autorun stops with the smallest recommended clarification or verification step.

## Route specialists

Use [bug-hunt report](../bug-hunt/report/SKILL.md) as the primary evidence authority and its matching planner as the primary correction plan.

Select additional reports only when required by the bug evidence:

- [purpose-adherence report](../purpose-adherence/report/SKILL.md) when an approved purpose contract covers the target and the correction may affect that purpose
- [coding-standards-accordance report](../coding-standards-accordance/report/SKILL.md) when JS/TS guideline violations directly block or risk the bug fix
- [code-smells report](../code-smells/report/SKILL.md) when an evidenced Fowler smell directly prevents a small, reliable correction
- [js-to-ts report](../js-to-ts/report/SKILL.md) only when the bug fix explicitly requires `.js`/`.jsx` conversion

Do not broaden a bug fix into general cleanup, architecture improvement, standards cleanup, or conversion work. Record unrelated findings as deferred follow-ups.

Use each selected report's matching `planner` in manual mode and `autoplan` in autorun mode. `autoplan-force` is never implied by bug-fix autorun.

## Plan and implement

1. Map every accepted bug-hunt finding to one disposition and preserve all `BH-*` IDs.
2. For each fixed confirmed finding, require a specific regression test, focused reproduction check, or justified non-test proof.
3. For each probable finding selected for correction, run the planned verification gate first. Only verified probable findings may become fix steps, and they then require the same regression proof as confirmed findings.
4. Prefer repository-native tests at the smallest credible level, but use integration, contract, type-level, migration, or reproduction checks when they prove the bug trigger and invariant more directly.
5. If no durable test is reasonable, state why in the synthesized plan and name the alternate proof. Do not leave regression proof implicit.
6. Keep the correction to the smallest behavior change that restores the violated invariant. Preserve unrelated behavior, public interfaces, data formats, valid tests, dependencies, architecture, compatibility, and established error semantics.
7. Present the synthesized plan and stop for approval before editing.

After approval, implement the approved correction and its regression proof, run focused checks, and apply the shared validation and documentation gates.

## Completion

Report fixed and deferred `BH-*` findings, bug triggers covered, regression proof added or executed, changed behavior, preserved contracts, checks, validation findings, documentation impact, and residual risks.
