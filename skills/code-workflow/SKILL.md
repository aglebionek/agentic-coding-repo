---
name: code-workflow
description: Orchestrates evidence, planning, implementation, validation, and documentation for issue work, bug fixes, codebase improvement, and JavaScript-to-TypeScript conversion. Use when the user invokes "code-workflow issue", "code-workflow bug-fix", "code-workflow improve", "code-workflow js-to-ts", or "code-workflow js-to-ts-autoscope", optionally with "manual" or "autorun".
---

# Code Workflow

Coordinate existing specialist skills; never reproduce or weaken their rules. Preserve specialist artifacts and finding IDs through one approved work package.

## Invocation

Require one profile and an explicit target:

- `code-workflow issue <issue-number-or-url> [manual|autorun]`
- `code-workflow bug-fix <bug-hunt-report-or-file-or-directory> [manual|autorun]`
- `code-workflow improve <file-or-directory> [manual|autorun]`
- `code-workflow js-to-ts <files-or-symbols> [manual|autorun]`
- `code-workflow js-to-ts-autoscope <seed-file-or-symbol> [deep|wide] [manual|autorun]`

Default workflow mode to `manual`. For `js-to-ts-autoscope`, default scope mode to `deep`. Never interpret a bare request to write or review code as this workflow.

Read the selected profile completely before acting:

- [ISSUE-WORKFLOW.md](ISSUE-WORKFLOW.md)
- [BUG-FIX-WORKFLOW.md](BUG-FIX-WORKFLOW.md)
- [IMPROVEMENT-WORKFLOW.md](IMPROVEMENT-WORKFLOW.md)
- [JS-TO-TS-WORKFLOW.md](JS-TO-TS-WORKFLOW.md)
- [JS-TO-TS-AUTOSCOPE-WORKFLOW.md](JS-TO-TS-AUTOSCOPE-WORKFLOW.md)

Always read [QUALITY-GATES.md](QUALITY-GATES.md) and [ARTIFACT-CONTRACT.md](ARTIFACT-CONTRACT.md).

## Modes

- `manual`: resolve material decisions one at a time with [grill-me](../grill-me/SKILL.md), recommend an answer, and record the decision.
- `autorun`: make safe, evidence-backed decisions without questions. Stop on ambiguous intended behavior, invalid specialist reports, public-contract or migration changes, architecture changes, new dependencies, destructive work, or security/access-policy choices.

Both modes require explicit user approval of the synthesized implementation plan. Autorun resumes autonomous execution only after that approval.

## Shared workflow

1. Read applicable repository instructions and coding guidelines. Record revision and dirty state; preserve unrelated work.
2. Establish the source request, exact code scope, approved purpose authority if any, acceptance criteria, exclusions, and verification baseline.
3. Select only specialists justified by the profile and evidence. Read each selected skill and its required references completely before invoking it.
4. Require valid, fresh reports before using their planners. Keep reports and plans read-only.
5. Synthesize one work package and one implementation plan using the artifact contract. Preserve every finding disposition and specialist boundary.
6. Present the plan and stop for explicit approval. Approval of requirements, a report, or this workflow is not implementation approval.
7. Implement only the approved plan. Pause at quality-gate stop conditions or newly discovered work outside the boundary.
8. Run focused verification, then a skeptical current-changes audit. New corrective edits require a supplemental approved plan.
9. Reconcile planned documentation against approved purpose. Report residual risks, deferred findings, checks, and unperformed external actions.

## Constraints

- Do not run every specialist by default; routing belongs to the selected profile.
- Do not merge unlike severity scales or convert one specialist's concern into another's finding.
- Do not infer intended purpose. Missing purpose may limit or stop work as defined by the profile.
- Do not commit, push, open a pull request, close an issue, or change issue metadata unless the user explicitly authorizes that action.
