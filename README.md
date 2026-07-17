# Agentic Coding Repo

A personal repo for agentic coding workflows: agent instructions, reusable skills, and research notes for working with AI coding agents.

## What's in here

### `AGENTS.md`
Repository-level instructions for agent sessions. It lists the active repo rules, stable docs, and the local skills an agent can invoke.

### `GLOSSARY.md`
Stable terminology for this repo and its workflows. Use it to keep repeated concepts consistent across sessions, plans, and docs.

### `fetch-agent-assets.sh`
Bootstrap script that downloads `AGENTS.md`, `GLOSSARY.md`, and `skills/` from this repository into the current directory.

### `notes/`
Obsidian-style notes from AI coding research, including maps for key ideas, terminology, sources, and pasted image assets.

### `skills/`
Reusable agent skills. Each skill is a directory with a `SKILL.md` entrypoint and, when needed, supporting references or scripts.

| Skill | Description |
|---|---|
| `answer-and-stop` | Answer directly and stop when the user wants no follow-up. |
| `bug-hunt-planner` | Convert a bug-hunt report into one read-only correction and verification plan. |
| `bug-hunt-report` | Hunt for evidenced runtime bugs, edge cases, invalid states, and uncovered correctness risks. |
| `caveman` | Switch to an ultra-compressed communication style. |
| `code-smells-planner` | Convert a valid code-smells report into one read-only refactoring plan. |
| `code-smells-report` | Identify Fowler catalog code smells in an explicit source target. |
| `code-workflow` | Orchestrate evidence, planning, implementation, validation, and documentation for issue work, codebase improvement, and JavaScript-to-TypeScript conversion. |
| `coding-standards-accordance-planner` | Convert a coding-standards-accordance report into one read-only correction plan. |
| `coding-standards-accordance-report` | Audit JavaScript and TypeScript against the governing `CODING_GUIDELINES.md`. |
| `create-gh-issue` | Create GitHub issues with the `gh` CLI and repository issue templates. |
| `create-gh-pr` | Create GitHub pull requests with the `gh` CLI and the repository PR template. |
| `create-report-planner-skill` | Create or update nested, read-only report/planner skill pairs. |
| `domain-model` | Stress-test a plan against domain language and record context or ADR decisions. |
| `give-commit-message` | Produce a concise commit message for completed coding work. |
| `grill-me` | Interview the user about a plan or design until the open decisions are resolved. |
| `grow-docs` | Expand an Obsidian documentation vault with short linked notes and gap audits. |
| `grow-glossary` | Find glossary-worthy missing terms from the current conversation or artifacts. |
| `handoff` | Crystallise a conversation into a plan for a fresh session. |
| `handoff-to-worktree` | Legacy compatibility entry for worktree handoffs; prefer `handoff` worktree mode. |
| `implement-strategy` | Turn a strategy-file step into an implementation plan and handoff. |
| `improve-codebase-architecture` | Surface architecture-deepening opportunities for locality, leverage, and testability. |
| `js-to-ts-planner` | Convert a valid JS-to-TS report into one read-only TypeScript conversion plan. |
| `js-to-ts-report` | Analyze JavaScript or JSX targets for a safe, guideline-compliant TypeScript conversion. |
| `list-dont-modify` | List what the user asked for without making any file changes or trying to fix anything. |
| `purpose-adherence-planner` | Convert a valid purpose-adherence report into one actionable correction and verification plan. |
| `purpose-adherence-report` | Audit code and contract surfaces against an approved Obsidian purpose contract. |
| `review-changes` | Review pointed-to changes for plan adherence, quality, completeness, and docs/tests. |
| `review-intent-and-coverage` | Inspect current changes, validate intended behavior, then verify or expand tests. |
| `testable-module` | Refactor toward a pure-function module API using a TDD flow. |
| `validate-current-changes` | Skeptically audit current local changes for logic errors, invalid states, unnecessary complexity, regressions, and misleading tests. |
| `worktree` | Guide creation and use of per-session git worktrees. |
| `write-a-skill` | Create new skills with the expected structure, metadata, and supporting resources. |

### Code workflow

`code-workflow` is the main orchestration skill for multi-step coding work. Use it when a request needs coordinated evidence gathering, specialist reports, planning, approved implementation, validation, and documentation rather than a single direct edit.

It supports three profiles:
- `code-workflow issue <issue-number-or-url> [manual|autorun]`
- `code-workflow improve <file-or-directory> [manual|autorun]`
- `code-workflow js-to-ts <files-or-symbols> [manual|autorun]`

`manual` mode resolves material decisions one at a time with `grill-me`, then stops for explicit implementation approval. `autorun` mode makes safe, evidence-backed decisions without questions, but still stops for approval before implementation and at any quality-gate stop condition.

The workflow coordinates specialist skills such as `bug-hunt-report`, `code-smells-report`, `coding-standards-accordance-report`, `js-to-ts-report`, their planners, `testable-module`, `grow-docs`, and `validate-current-changes`. It does not replace those skills; it preserves their artifacts and finding IDs while turning them into one approved work package.

The `caveman`, `grill-me`, `domain-model`, `improve-codebase-architecture`, and `write-a-skill` skills were copied from [mattpocock/skills](https://github.com/mattpocock/skills).

Some skills refer to files that are expected to exist in the target project where the skill is used, such as GitHub issue templates, a pull request template, `docs/obsidian/`, `CONTEXT.md`, ADR directories, or worktree scripts.

### Potential additions
- Triage skill - would require a set of defined github label.
- More multishot components - workflows/skills (from triage to issue review, tests, implementation, docs update to the final PR, with intermediate code reviews and checks, adhering to the coding guidelines like module testability).
- More strict and interconnected core guidelines (e.g. "always write tests first (red/green)", "always update docs at the end", "read the related docs from...", "make sure the module is testable") and skills to enforce them.
- More defined worktree lifecycle management (e.g. automatic cleanup of old worktrees, reminders to delete worktree after session ends, etc.). Alternatively, use something else than git worktrees? Docker containers maybe?
- Docs expansions - deepen the glossary and related note graph now that the shared glossary/backlog flow exists.
