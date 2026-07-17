---
name: handoff-to-worktree
description: Legacy compatibility entry for worktree handoff. Use only when a reference explicitly points to handoff-to-worktree; otherwise use the handoff skill's worktree mode.
---

# Handoff to Worktree

This skill is a compatibility pointer. Use [handoff](../handoff/SKILL.md) in **worktree handoff** mode.

Do not follow the older worktree-only behavior from this file. The canonical behavior is:

- Preserve or synthesize a plan.
- Save it under `./codex/handoffs/`.
- Print the worktree handoff block with `./scripts/createWorktree.sh <BRANCH_NAME> <MODEL_NAME> "<TASK_DESCRIPTION>"`.
- Stop without implementing.
