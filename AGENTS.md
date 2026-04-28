## Brief
Multiple AI model sessions may run in parallel on this repo. 
When a user mentions a skill to use, look at the available skills.
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

### Skills
Keeping skills here instead of loading them on every session start to save tokens/shrink context window. These are the skills available to the model for this session, which can be used to solve the task:
- `./.aglebionek/skills/answer-and-stop/SKILL.md`: Answer the user's question and stop. Use when the user wants a direct answer without further questioning, or types a&s.
- `./.aglebionek/skills/caveman/SKILL.md`: Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler, articles, and pleasantries while keeping full technical accuracy. Use when user says "caveman mode", "talk like caveman", "use caveman", or invokes /caveman.
- `./.aglebionek/skills/domain-model/SKILL.md`: Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions.
- `./.aglebionek/skills/grill-me/SKILL.md`: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
- `./.aglebionek/skills/handoff-to-worktree/SKILL.md`: Crystallise the current conversation into a plan, save it to the session workspace, and give the user an exact prompt to paste into a fresh session to implement it. Use when the user wants to hand off a plan to a new session, or says "handoff", "save plan", or "start in new session".
- `./.aglebionek/skills/improve-codebase-architecture/SKILL.md`: Identify and present opportunities to deepen the architecture of the codebase for better locality and leverage. Use when user wants to improve codebase architecture, or says "improve architecture", "deepen architecture", "refactor for locality", or "refactor for leverage".

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

3. **Print worktree info** 
   ```
   📂 Worktree: <path-to-worktree>
   🌿 Branch: <branch-name>
   🤖 Model: <model-name>
   ```
