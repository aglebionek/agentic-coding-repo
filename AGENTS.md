---
allowed-tools: Bash
---

## Brief
Multiple AI model sessions may run in parallel on this repo. 
To prevent conflicts, **every session MUST work in its own git worktree**, never in the main checkout.

## Parameters
- branch-name: A unique name for the worktree branch (e.g., `feature/avatar-upload`, `bugfix/login-error`, `experiment/new-ui`). This is the name of the git branch that will be created for this session's worktree.
- path-to-worktree: The directory path where the worktree will be created (e.g., `../worktrees/feature-avatar-upload`). This should be outside the main checkout to avoid confusion.
- model-name: The AI model you used for this session (e.g., `claude-sonnet-5`).
- task: A one-line description of the task for this session (e.g., "Add user avatar upload feature").

## Model resources
### Files
- `./.worktree-session`: Contains current session parameters (branch-name, model-name, task, started, path-to-worktree) for reference.

### Docs
// put paths to docfiles, that briefly describe existing systems, their locations, relations and minutiae

### Scripts
- `./.aglebionek/scripts/checkIfAlreadyInWorktree.sh`: Checks if the current directory is already inside a git worktree and exits with an error if so, to prevent nesting worktrees.
- `./.aglebionek/scripts/createWorktree.sh <branch-name> <model-name> "<one-line-task-description>"`: Creates a new git worktree for the session, sets up symlinks for shared resources, and saves session metadata.
- `./.aglebionek/scripts/list_worktrees.sh`: Lists all existing worktrees with their branch names and paths.
- `./.aglebionek/scripts/openWorktreeInCode.sh <path-to-worktree>`: Opens the specified worktree in VS Code.
- `./.aglebionek/scripts/removeWorktree.sh <path-to-worktree>`: Removes the specified worktree and deletes its branch.

### Tests
// brief description on what to run to test things, and what not to do
- DO NOT build the app to test your work.

### Worktree Setup
1. **Run bashscript to create a new worktree** for your session (replace placeholders):
   ```bash
   ./.aglebionek/scripts/worktree/createWorktree.sh <branch-name> <model-name> "<one-line-task-description>"
   ```

2. **Save your plan and your resume command in text files** inside the worktree (e.g., `../worktrees/<branch-name>/plan.md` and `../worktrees/<branch-name>/resume_command.sh`) so the user can easily understand your approach and resume the session later if needed.

3. **Print worktree info** at the very start of your first response, before doing anything else:
   ```
   📂 Worktree: ../worktrees/<branch-name>
   🌿 Branch: <branch-name>
   🤖 Model: <model-name>
   ```

### Rules
- **ALWAYS ask if you're unsure about something related to solving your task**.
- **ALWAYS save your plan and resume command in text files** inside the worktree main directory.
- **NEVER start implementing a plan before user approval**.
- **NEVER edit files in the main checkout** (`/home/aglebionek/work/instago/app`) — only in your worktree.
- **NEVER commit anything unless asked to**.
- **Do NOT delete worktrees until asked to**.
- **Do NOT run `git worktree prune`** or modify other worktrees.
- If your worktree already exists (you're resuming work), just `cd` into it.
