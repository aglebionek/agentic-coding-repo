---
name: handoff
description: Crystallise the current conversation into a saved implementation plan and give the user an exact fresh-session prompt. Use when the user says "handoff", "handoff branch", "handoff worktree", "save plan", or "start in new session".
---

# Handoff

You are closing out a planning conversation and handing it off to a fresh implementation session. Do not implement.

## Modes

- **Default** — `handoff`, `save plan`, or similar with no branch/worktree mode. Save the plan and prompt a fresh session to implement it.
- **Branch** — `handoff branch` or any request for a fresh agent to create a branch first. Save the plan and prompt the next agent to create the branch before implementation.
- **Worktree** — `handoff worktree` or `handoff to worktree`. Save the plan and prompt the next agent to create/use a worktree before implementation.

## Steps

### 1. Determine plan source

Preserve an existing approved or coherent implementation plan. If no plan exists, synthesize one from the conversation before saving. Do not re-litigate decisions.

### 2. Pick metadata

- **Plan slug** — kebab-case, scoped when useful, e.g. `anonymous-landing-project-owner`.
- **Branch name** — required for branch/worktree modes; optional suggestion for default mode. Use kebab-case with a prefix when useful, e.g. `fix/anonymous-landing-project-owner`.
- **Model name** — for worktree mode only, use `claude-sonnet-4.6` unless the user specified another model.
- **Task description** — for worktree mode only, one short shell-quoted sentence for `createWorktree.sh`.

Ask only if branch mode was requested and there is not enough context to choose a branch name safely.

### 3. Write the plan

From the conversation so far, extract:

- **Problem** — what is broken or missing, and why it matters.
- **Approach** — chosen solution strategy, not alternatives.
- **Provider / module tree** — if architectural, show nesting/dependency order.
- **Interfaces** — new public hooks, functions, and types with fields.
- **Files to create/modify** — exhaustive list with one-line descriptions.
- **Key decisions** — decisions not to re-litigate, with reasons.
- **Migration strategy** — if applicable, how existing consumers/callers are handled.
- **Validation** — tests, checks, or manual verification to run.
- **Mode instructions** — default, branch, or worktree instructions.
- **Branch name** — chosen or suggested branch name.
- **Worktree setup** — worktree mode only:
  `./scripts/createWorktree.sh <BRANCH_NAME> <MODEL_NAME> "<TASK_DESCRIPTION>"`

When they materially apply, also record:

- **Architecture constraints** — governing shared/project guidance and the
  responsibility boundaries the implementation must preserve.
- **Public reading entrypoints** — existing or planned files where callers and
  maintainers first encounter each changed responsibility.
- **Documentation impact** — the active documentation profile, affected
  approachable/technical material, indexes, and canonical sources.
- **Canonical terminology** — shared or project glossary terms that must remain
  consistent.
- **Compatibility surfaces** — existing consumers, temporary facades, migration
  order, and separately approved removals.

Omit conditional fields that do not help the next session. Do not add empty
ceremony to a simple task.

Be exhaustive. The fresh session will have no memory of this conversation.

### 4. Save the plan

Save the plan under `./codex/handoffs/<YYYY-MM-DD>-<plan-slug>.md`. Create the directory if needed. Use the absolute path in the handoff block.

### 5. Print the handoff block

Use this wrapper for every mode:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 HANDOFF READY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Open a new chat and paste:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  <MODE_PROMPT>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Default `<MODE_PROMPT>`:

```text
Read <PLAN_FILE_PATH> and implement it.
```

Branch `<MODE_PROMPT>`:

```text
Read <PLAN_FILE_PATH>.
Create this branch before implementation:
  <BRANCH_NAME>
Then implement the plan.
```

Worktree `<MODE_PROMPT>`:

```text
Read <PLAN_FILE_PATH>.
Create/use a worktree first:
  ./scripts/createWorktree.sh <BRANCH_NAME> <MODEL_NAME> "<TASK_DESCRIPTION>"
Then switch to that worktree and implement the plan.
Branch: <BRANCH_NAME>
Model: <MODEL_NAME>
```

Replace `<PLAN_FILE_PATH>` with the actual absolute path to the saved plan file, and every other placeholder with selected metadata.

### 6. Stop

Print the handoff block and stop the conversation.
