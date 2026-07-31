---
name: code-workflow
description: Orchestrates evidence, planning, implementation, validation, and documentation for issue work, bug fixes, codebase improvement, and JavaScript-to-TypeScript conversion. Use when the user invokes "code-workflow issue", "code-workflow bug-fix", "code-workflow improve", "code-workflow js-to-ts", or "code-workflow js-to-ts-autoscope", optionally with "manual" or "autorun".
---

# Code Workflow

Provide one public facade over internal evidence, planning, implementation,
validation, and documentation modules. Preserve specialist artifacts and
finding IDs through one approved work package.

## Invocation

Require one profile and an explicit target:

- `code-workflow issue <issue-number-or-url> [manual|autorun]`
- `code-workflow bug-fix <bug-hunt-report-or-file-or-directory> [manual|autorun]`
- `code-workflow improve <file-or-directory> [manual|autorun]`
- `code-workflow js-to-ts <files-or-symbols> [manual|autorun]`
- `code-workflow js-to-ts-autoscope <seed-file-or-symbol> [deep|wide] [manual|autorun]`

Default workflow mode to `manual`. For `js-to-ts-autoscope`, default scope mode to `deep`. Never interpret a bare request to write or review code as this workflow.

Read the selected profile completely before acting:

- [ISSUE.md](profiles/ISSUE.md)
- [BUG-FIX.md](profiles/BUG-FIX.md)
- [IMPROVEMENT.md](profiles/IMPROVEMENT.md)
- [JS-TO-TS.md](profiles/JS-TO-TS.md)
- [JS-TO-TS-AUTOSCOPE.md](profiles/JS-TO-TS-AUTOSCOPE.md)

Always read the [quality gates](quality/QUALITY-GATES.md),
[artifact contract](ARTIFACT-CONTRACT.md), [specialist
contract](specialists/SPECIALIST-CONTRACT.md), and [routing
table](specialists/ROUTING.md).

## Modes

- `manual`: resolve material decisions one at a time with
  [grill-me](../interaction/grill-me/SKILL.md), recommend an answer, and record
  the decision.
- `autorun`: make safe, evidence-backed decisions without questions. Stop on ambiguous intended behavior, invalid specialist reports, public-contract or migration changes, architecture changes, new dependencies, destructive work, or security/access-policy choices.

Both modes require explicit user approval of the synthesized implementation plan. Autorun resumes autonomous execution only after that approval.

## Shared workflow

1. Read applicable repository instructions, coding guidelines, shared
   architecture guidance when installed, and the project documentation profile.
   When executable behavior may change, also read the shared
   `TESTING_GUIDELINES.md` from the installed resource layer (source repository:
   `shared/TESTING_GUIDELINES.md`). Record revision and dirty state; preserve
   unrelated work.
2. Establish the source request, exact code scope, approved purpose authority if any, acceptance criteria, exclusions, and verification baseline.
3. Select only specialists justified by the profile and routing evidence. Read
   each selected internal report, planner, template, and required local
   reference completely before using it.
4. Require valid, fresh reports before using their planners. Keep reports and plans read-only.
5. Synthesize one work package and one implementation plan using the artifact
   contract. Preserve every finding disposition and specialist boundary. When
   architecture or public contracts change, include justified documentation
   impact, public reading entrypoints, and compatibility surfaces.
6. Present the plan and stop for explicit approval. Approval of requirements, a report, or this workflow is not implementation approval.
7. Implement only the approved plan. Pause at quality-gate stop conditions or newly discovered work outside the boundary.
8. Run focused verification, then the skeptical
   [current-changes audit](quality/CURRENT-CHANGES-AUDIT.md). New corrective
   edits require a supplemental approved plan.
9. Reconcile planned documentation against approved purpose and the active
   documentation profile. Do not force documentation edits when the work has no
   justified documentation impact. Report residual risks, deferred findings,
   checks, and unperformed external actions.

## Constraints

- Do not run every specialist by default; routing belongs to the selected profile.
- Do not merge unlike severity scales or convert one specialist's concern into another's finding.
- Do not infer intended purpose. Missing purpose may limit or stop work as defined by the profile.
- Do not commit, push, open a pull request, close an issue, or change issue metadata unless the user explicitly authorizes that action.
