# Agentic Coding Repo

A personal repo for agentic coding workflows — configurations, scripts, and skills for working with AI coding agents (primarily GitHub Copilot CLI).

## What's in here

### `AGENTS.md`
Instructions injected into every AI agent session. Enforces a git worktree workflow so multiple parallel agent sessions don't conflict with each other. Each session gets its own branch and worktree directory.

### `scripts/`
Shell scripts for managing git worktrees:
- `createWorktree.sh` — creates a new worktree + branch for an agent session
- `removeWorktree.sh` — removes a worktree and deletes its branch
- `list_worktrees.sh` — lists all active worktrees
- `openWorktreeInCode.sh` — opens a worktree in VS Code
- `checkIfAlreadyInWorktree.sh` — guard script to prevent nested worktrees

### `.agents/skills/`
Reusable skills for the GitHub Copilot CLI agent. Skills are invoked by name during a session to activate specialised behaviour.

| Skill | Description |
|---|---|
| `answer-and-stop` | Answer the user's question briefly and directly, then stop the conversation |
| `create-gh-issue` | Create GitHub issues with the `gh` CLI. Assumes the existance of issue templates. |
| `create-gh-pr` | Create GitHub pull requests with the `gh` CLI. Assumes the existance of a pull request template. |
| `grow-docs` | Meant to be used at the end of coding sessions to document the codebase and changes made. It creates clusters of brief, wikilinked notes, then audits the vault for broken links and doc gaps to fill next.
| `handoff-to-worktree` | Crystallise a conversation into a plan and hand it off to a fresh session |
| `implement-strategy` | Guides an implementation of a strategy. Mentions the [docs](../grow-docs/SKILL.md) and [testable-module](../testable-module/SKILL.md) strategies as part of the implementation steps, and grills the user for any missing details to create a complete plan.
| `review-changes` | A WIP code reviewer for multishot AI workflows.
| `testable-module` | Inspired by the `improve-codebase-architecture`, it tries to refactor already existing code not the improve it, but to rewrite it in a more testable way. Using Test-Driven Development approach, it writes tests first and then refactors the code to make it pass the tests. Great for making the codebase more AI-friendly and improving test coverage.
|||
| `caveman` | Ultra-compressed communication mode (~75% fewer tokens) |
| `grill-me` | Relentlessly interview the user about a plan or design |
| `domain-model` | Stress-test a plan against the project's domain model and update docs |
| `improve-codebase-architecture` | Find deepening/refactoring opportunities informed by the domain language |
| `write-a-skill` | Write a new skill based on user instructions |

The `caveman`, `grill-me`, `domain-model`, `improve-codebase-architecture`, and `write-a-skill` skills were copied from [mattpocock/skills](https://github.com/mattpocock/skills).


### Potential additions
- Triage skill - would require a set of defined github label.
- More multishot components - workflows/skills (from triage to issue review, tests, implementation, docs update to the final PR, with intermediate code reviews and checks, adhering to the coding guidelines like module testability).
- More strict and interconnected core guidelines (e.g. "always write tests first (red/green)", "always update docs at the end", "read the related docs from...", "make sure the module is testable") and skills to enforce them.
- More defined worktree lifecycle management (e.g. automatic cleanup of old worktrees, reminders to delete worktree after session ends, etc.). Alternatively, use something else than git worktrees? Docker containers maybe?
- Docs expansions - something like a glossary for the calcified terminology and concepts - no more than one or two sentences per term, with links to examples and more detailed explanations in seperate notes. It's annoying that you have to reexplain the same concepts over and over again in every session, and a shared glossary would speed things up and improve consistency across sessions. Might want to combine it with skills like grill me and grow docs, or even mention the glossary and add an auto-updating instruction directly to AGENTS.md.