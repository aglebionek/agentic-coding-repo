# Issue Workflow

Use for `code-workflow issue <issue-number-or-url> [manual|autorun]`.

## Intake

1. Read the issue and relevant comments, labels, linked artifacts, and acceptance evidence from `HAERGI-PL/instago-app-issues` unless the URL names another repository.
2. Resolve the implementation repository and exact target. The issue repository is an intake source, not automatically the code repository.
3. Treat issue text as a proposed outcome, not purpose authority. Reconcile it with approved purpose, public contracts, and current behavior.
4. Record reproducibility, environment, observed versus expected behavior, affected consumers, explicit non-goals, and missing facts.

If the issue is not actionable, manual mode grills one material question at a time. Autorun stops with the smallest recommended clarification or reproduction step.

## Route specialists

Select the smallest evidence set:

| Evidence need | Specialist |
|---|---|
| Runtime bug, invalid state, edge case, regression, or correctness risk | [bug-hunt report](../bug-hunt/report/SKILL.md) |
| Mismatch with an applicable approved purpose contract | [purpose-adherence report](../purpose-adherence/report/SKILL.md) |
| Explicit JS/TS guideline concern | [coding-standards-accordance report](../coding-standards-accordance/report/SKILL.md) |
| Evidenced Fowler smell materially affecting the correction | [code-smells report](../code-smells/report/SKILL.md) |
| Explicit `.js`/`.jsx` conversion in the issue outcome | [js-to-ts report](../js-to-ts/report/SKILL.md) |

Do not use code smells as a substitute for bug evidence. Do not broaden a bounded issue into a general cleanup audit.

Use each selected report's matching `planner` in manual mode and `autoplan` in autorun mode. `autoplan-force` is never implied by issue autorun.

## Plan and implement

1. Map issue acceptance criteria and specialist findings into one work package.
2. If the solution needs a pure module boundary, read [testable-module](../testable-module/SKILL.md). Establish its API and fixture contract during planning, not after implementation approval.
3. Prefer the smallest correction that satisfies purpose and restores evidenced behavior. Preserve unrelated behavior and contracts.
4. Include regression proof for the reported trigger, negative and error paths, and absence of unintended side effects.
5. Present the synthesized plan and stop for approval before editing.
6. After approval, implement, run focused checks, and apply the shared validation and documentation gates.

## Completion

Report issue criteria satisfied, finding dispositions, changed behavior, checks, validation findings, documentation impact, and residual risks. Do not comment on, label, assign, close, or otherwise mutate the issue without explicit authorization.
