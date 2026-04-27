## Brief
Multiple AI model sessions may run in parallel on this repo. 
To prevent conflicts, **every session MUST work in its own git worktree**, never in the main checkout, unless told otherwise.

## Rules
**Use the worktree directory to store plans, notes, and any files related to the conversation.**
NEVER make commits, NEVER lint the code.
When adding translations, only add keys to the en.json file.
ALWAYS ask if you're unsure about something related to solving your task.
NEVER start implementing a plan before user approval.
NEVER edit files in the main checkout — only in your worktree.
NEVER delete worktrees or branches created for your session.
If your worktree already exists (you're resuming work), just `cd` into it.

## Parameters
- branch-name: A unique name for the worktree branch (e.g., `feature/avatar-upload`, `bugfix/login-error`, `experiment/new-ui`). This is the name of the git branch that will be created for this session's worktree.
- path-to-worktree: The directory path where the worktree will be created (e.g., `/home/user/project/worktrees/feature-avatar-upload`). This should be outside the main checkout to avoid confusion.
- model-name: The AI model you used for this session (e.g., `claude-sonnet-5`).
- task: A one-line description of the task for this session (e.g., "Add user avatar upload feature").

## Model resources
### Files
- `./.worktree-session`: Contains current session parameters (branch-name, model-name, task, started, path-to-worktree) for reference.

### Docs
// path to docs

### Scripts
- `./scripts/checkIfAlreadyInWorktree.sh`: Checks if the current directory is already inside a git worktree and exits with an error if so, to prevent nesting worktrees.
- `./scripts/createWorktree.sh <branch-name> <model-name> "<one-line-task-description>"`: Creates a new git worktree for the session, sets up symlinks for shared resources, and saves session metadata.
- `./scripts/list_worktrees.sh`: Lists all existing worktrees with their branch names and paths.
- `./scripts/openWorktreeInCode.sh <path-to-worktree>`: Opens the specified worktree in VS Code.
- `./scripts/removeWorktree.sh <path-to-worktree>`: Removes the specified worktree and deletes its branch.
// other scripts

### Tests
// What tests to run and when

## Worktree Setup
1. **Run bashscript to create a new worktree** for your session (replace placeholders):
   ```bash
   ./scripts/worktree/createWorktree.sh <branch-name> <model-name> "<one-line-task-description>"
   ```

2. **Save your plan in the worktree as plan.md**

3. **Print worktree info** at the very start of your first response, before doing anything else:
   ```
   📂 Worktree: <path-to-worktree>
   🌿 Branch: <branch-name>
   🤖 Model: <model-name>
   ```
