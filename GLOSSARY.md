# Glossary

This file holds stable terminology for this repo and its workflows. Keep entries short: one or two sentences per term, with links to notes or examples when useful.

## Entry format

Use one heading per term:

```md
## Term
Short canonical definition.

- Example: Optional link or concrete example
- Related: Optional related term or note
```

## Terms

## Agent session
A single AI working conversation with its own task context, instructions, and usually its own worktree or session workspace.

- Example: A fresh implementation chat created from a handoff prompt
- Related: [[#Handoff|Handoff]], [[#Worktree workflow|Worktree workflow]]

## Agentic coding repo
This repository itself: a personal toolbox of instructions, scripts, and skills for running AI-assisted coding workflows, primarily around GitHub Copilot CLI.

- Example: `AGENTS.md`, `skills/`, and `scripts/` together define the workflow surface
- Related: [[#Skill|Skill]], [[#Worktree workflow|Worktree workflow]]

## Focused glossary session
A session where the main goal is updating `GLOSSARY.md`, instead of interrupting unrelated implementation or planning work with terminology cleanup.

- Example: A later docs pass that reviews deferred glossary items and updates definitions
- Related: [[#Glossary backlog|Glossary backlog]], [[#Handoff|Handoff]]

## Glossary backlog
A deferred list of terminology candidates stored outside the repo by default, so sessions can note glossary drift without switching topics.

- Example: `/tmp/agentic-coding-glossary-backlog.json`
- Related: [[#Glossary candidate|Glossary candidate]], [[#Focused glossary session|Focused glossary session]]

## Glossary candidate
A term or concept worth capturing for later glossary work because it is repeated, conflicting, missing, or explicitly requested by the user.

- Example: A concept like "handoff" appearing often enough that new sessions should not need it re-explained
- Related: [[#Glossary backlog|Glossary backlog]]

## Grow docs
A documentation skill that expands the Obsidian vault as clusters of short, linked notes and then audits for broken links and doc gaps.

- Example: `skills/grow-docs/SKILL.md`
- Related: [[#Skill|Skill]]

## Grill me
A skill that interviews the user aggressively about a plan or design until the open decisions are explicit and the approach is sharp enough to execute.

- Example: Used when requirements are still fuzzy and the agent should not guess
- Related: [[#Skill|Skill]]

## Handoff
A compact but complete transfer of context from the current session into a new one, usually by saving a plan and printing an exact prompt to continue later.

- Example: `handoff` and `handoff-to-worktree`
- Related: [[#Agent session|Agent session]], [[#Session plan|Session plan]]

## Session plan
A durable planning artifact saved in the session workspace so a later session can continue the work without relying on chat memory.

- Example: `plan.md` in the Copilot session-state directory
- Related: [[#Handoff|Handoff]]

## Skill
A reusable instruction bundle with a `SKILL.md` entrypoint that teaches the agent a named behavior and when to invoke it.

- Example: `write-a-skill`, `grow-docs`, `testable-module`
- Related: [[#Agentic coding repo|Agentic coding repo]]

## Testable module
A refactoring target shaped around a clear pure-function interface and TDD-style implementation so the code becomes easier to verify and easier for agents to change safely.

- Example: `skills/testable-module/SKILL.md`
- Related: [[#Skill|Skill]]

## Worktree workflow
The repo convention that parallel AI sessions should usually work in separate git worktrees to avoid clobbering each other's files and branches.

- Example: `AGENTS-worktree.md` plus the scripts in `scripts/`
- Related: [[#Agent session|Agent session]], [[#Handoff|Handoff]]
