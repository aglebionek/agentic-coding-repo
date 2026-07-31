---
name: handoff
description: Crystallise the current conversation into a handoff document for another agent to pick up.
---

# Handoff

You are closing out a conversation and handing it off to a fresh implementation session.

## Modes

- **Default** — `handoff`, or similar with no branch/worktree mode.
- **Branch** — `handoff branch` or any request for a fresh agent to create a branch first.
- **Worktree** — `handoff worktree` or `handoff to worktree`. Link instructions

## Steps

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

### 2. Save the file

Save the file under `./codex/handoffs/<YYYY-MM-DD>-<file-slug>.md`. Create the directory if needed. Use the absolute path in the handoff block.

### 3. Print the handoff block

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
Read worktree setup instructions in `skills/user-invoked/delivery/handoff/worktree/SKILL.md` and setup the worktree for this session.
Read <PLAN_FILE_PATH>.
Then switch to that worktree and implement the plan.
Branch: <BRANCH_NAME>
Model: <MODEL_NAME>
```

Replace `<PLAN_FILE_PATH>` with the actual absolute path to the saved plan file, and every other placeholder with selected metadata.

### 4. Stop

Print the handoff block and stop the conversation.
