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
| `caveman` | Switch to an ultra-compressed communication style. |
| `create-gh-issue` | Create GitHub issues with the `gh` CLI and repository issue templates. |
| `create-gh-pr` | Create GitHub pull requests with the `gh` CLI and the repository PR template. |
| `domain-model` | Stress-test a plan against domain language and record context or ADR decisions. |
| `grill-me` | Interview the user about a plan or design until the open decisions are resolved. |
| `grow-docs` | Expand an Obsidian documentation vault with short linked notes and gap audits. |
| `grow-glossary` | Find glossary-worthy missing terms from the current conversation or artifacts. |
| `handoff` | Crystallise a conversation into a plan for a fresh session. |
| `handoff-to-worktree` | Save a plan and prepare a worktree-oriented handoff prompt. |
| `implement-strategy` | Turn a strategy-file step into an implementation plan and handoff. |
| `improve-codebase-architecture` | Surface architecture-deepening opportunities for locality, leverage, and testability. |
| `list-dont-modify` | List what the user asked for without making any file changes or trying to fix anything. |
| `review-changes` | Review pointed-to changes for plan adherence, quality, completeness, and docs/tests. |
| `review-intent-and-coverage` | Inspect current changes, validate intended behavior, then verify or expand tests. |
| `testable-module` | Refactor toward a pure-function module API using a TDD flow. |
| `worktree` | Guide creation and use of per-session git worktrees. |
| `write-a-skill` | Create new skills with the expected structure, metadata, and supporting resources. |

The `caveman`, `grill-me`, `domain-model`, `improve-codebase-architecture`, and `write-a-skill` skills were copied from [mattpocock/skills](https://github.com/mattpocock/skills).

Some skills refer to files that are expected to exist in the target project where the skill is used, such as GitHub issue templates, a pull request template, `docs/obsidian/`, `CONTEXT.md`, ADR directories, or worktree scripts.

### Potential additions
- Triage skill - would require a set of defined github label.
- More multishot components - workflows/skills (from triage to issue review, tests, implementation, docs update to the final PR, with intermediate code reviews and checks, adhering to the coding guidelines like module testability).
- More strict and interconnected core guidelines (e.g. "always write tests first (red/green)", "always update docs at the end", "read the related docs from...", "make sure the module is testable") and skills to enforce them.
- More defined worktree lifecycle management (e.g. automatic cleanup of old worktrees, reminders to delete worktree after session ends, etc.). Alternatively, use something else than git worktrees? Docker containers maybe?
- Docs expansions - deepen the glossary and related note graph now that the shared glossary/backlog flow exists.