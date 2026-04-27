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
| `handoff-to-worktree` | Crystallise a conversation into a plan and hand it off to a fresh session |
|||
| `caveman` | Ultra-compressed communication mode (~75% fewer tokens) |
| `grill-me` | Relentlessly interview the user about a plan or design |
| `domain-model` | Stress-test a plan against the project's domain model and update docs |
| `improve-codebase-architecture` | Find deepening/refactoring opportunities informed by the domain language |

The `caveman`, `grill-me`, `domain-model`, and `improve-codebase-architecture` skills were copied from [mattpocock/skills](https://github.com/mattpocock/skills).

