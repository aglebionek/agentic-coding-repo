## Base
This repository root is the orchestration layer for a unified platform monorepo, named **Platform**.

The current directory structure is as follows:
- `./compose/`: Contains docker-compose files for different environments.
- `./docs-internal/`: Internal documentation for the platform.
- `./instago-app`: The main application codebase for Instago - a website builder platform.
- `./instago-auth`: Authentication service for Instago.
- `./instago-telemetry`: Telemetry service for Instago.
- `./packages`: Shared packages and libraries used across different services.
- `./skills/`: A collection of skills that can be used by AI agents to perform

## Environments
### Local
Hosts all services under .local, like app.instago.local or auth.instago.local.
### Dev
Hosts all services under .dev domain. Currently instago.dev and leadme.dev.
### Ai
Hosts all services under .ai domain. Currently instago.ai and leadme.ai. Additionally, instago-domains serves websites via *.instago.page.

## Rules
- ALWAYS use grill-me if you're unsure about something.
- NEVER start implementing a plan before user approval.
- NEVER commit anything unless asked to.
- NEVER delete worktrees until asked to.
## Model resources

### Docs
#### Instago docs
- `./instago-docs/`:

#### Obsidian docs
- `./instago-app/docs/obsidian/`: Obsidian documentation for Instago

### Skills
When you want to invoke a skill, read the appropriate skill file.
- `./skills/answer-and-stop/SKILL.md`: Answer the user's question and stop. Use when the user wants a direct answer without further questioning, or types a&s.
- `./skills/bug-hunt/report/SKILL.md`: Hunts for evidenced runtime bugs, edge cases, invalid states, and uncovered correctness risks. Use only when the user invokes "bug-hunt report <file-or-directory>", "bug-hunt report codebase", or "bug-hunt report current changes".
- `./skills/bug-hunt/planner/SKILL.md`: Creates one read-only correction plan from a bug-hunt report. Use only when the user invokes "bug-hunt planner" or "bug-hunt autoplan" with a report.
- `./skills/caveman/SKILL.md`: Use when user says "caveman mode", "talk like caveman", "use caveman", or invokes /caveman.
- `./skills/code-smells/report/SKILL.md`: Identifies Fowler catalog code smells in an explicit source target. Use only when the user invokes "code-smells report <file-or-directory>" or "code-smells report codebase".
- `./skills/code-smells/planner/SKILL.md`: Creates one read-only refactoring plan from a valid code-smells report. Use only when the user invokes "code-smells planner", "code-smells autoplan", or "code-smells autoplan-force" with a report.
- `./skills/coding-standards-accordance/report/SKILL.md`: Audits JavaScript and TypeScript against `CODING_GUIDELINES.md`. Use only when the user invokes "coding-standards-accordance report <file-or-directory>", "coding-standards-accordance report codebase", or "coding-standards-accordance report current changes".
- `./skills/coding-standards-accordance/planner/SKILL.md`: Creates one read-only correction plan from a coding-standards-accordance report. Use only when the user invokes "coding-standards-accordance planner" or "coding-standards-accordance autoplan" with a report.
- `./skills/code-workflow/SKILL.md`: Orchestrates evidence, planning, approved implementation, validation, and documentation for issue work, codebase improvement, and JavaScript-to-TypeScript conversion. Use when the user invokes "code-workflow issue", "code-workflow improve", or "code-workflow js-to-ts", optionally with "manual" or "autorun".
- `./skills/create-gh-issue/SKILL.md`: Uses gh cli to create an issue in the repo. Use when asked to create an issue.
- `./skills/create-report-planner-skill/SKILL.md`: Creates or updates nested read-only report/planner skill pairs. Use only when the user explicitly says "create report/planner skill" or asks to update an existing report/planner skill pair.
- `./skills/grill-me/SKILL.md`: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
- `./skills/grow-docs/SKILL.md`: Expands documentation. Use when user mentions "grow-docs".
- `./skills/grow-glossary/SKILL.md`: Finds glossary-worthy terms from the current conversation and session artifacts, diffs them against `GLOSSARY.md`, and reports only missing terms. Use at the end of a conversation, plan, or implementation when the user wants to grow the glossary, calcify terminology, or review missing glossary candidates.
- `./skills/give-commit-message/SKILL.md`: Produces a concise commit message for completed coding work, emphasizing why the change was made. Use when the user says "GCM", "give commit message", "give me a commit message", or asks for a commit message.
- `./skills/handoff/SKILL.md`: Crystallise the current conversation into a saved implementation plan and give the user an exact fresh-session prompt. Use when the user says "handoff", "handoff branch", "handoff worktree", "save plan", or "start in new session".
- `./skills/improve-codebase-architecture/SKILL.md`: Identify and present opportunities to deepen the architecture of the codebase for better locality and leverage. Use when user wants to improve codebase architecture, or says "improve architecture", "deepen architecture", "refactor for locality", or "refactor for leverage".
- `./skills/js-to-ts/report/SKILL.md`: Analyzes JavaScript or JSX targets for a safe, guideline-compliant TypeScript conversion. Use only when the user explicitly invokes "js-to-ts report".
- `./skills/js-to-ts/planner/SKILL.md`: Creates a read-only TypeScript conversion plan from a valid js-to-ts report. Use only when the user explicitly invokes "js-to-ts planner" or "js-to-ts autoplan".
- `./skills/list-dont-modify/SKILL.md`: When invoked, only list what the user asked for, without making any file changes or trying to fix anything. Use when user says "list don't modify", "list only" or "LDM".
- `./skills/purpose-adherence/report/SKILL.md`: Audits code and contract surfaces against an approved Obsidian purpose contract. Use only when the user explicitly invokes "purpose-adherence report".
- `./skills/purpose-adherence/planner/SKILL.md`: Creates one read-only action plan from a valid purpose-adherence report. Use only when the user explicitly invokes "purpose-adherence planner" or "purpose-adherence autoplan".
- `./skills/review-intent-and-coverage/SKILL.md`: Use when user asks for a review of current changes, to validate intent, or to check whether tests and coverage are sufficient.
- `./skills/testable-module/SKILL.md`: Guides refactoring code as a testable module with a clear pure-function API. Follows a TDD flow: agree on contract → write tests → implement. Use when user wants to make code testable, extract a module API, says "make testable", "module API", or "rewrite as module".
- `./skills/validate-current-changes/SKILL.md`: Performs a skeptical, read-only audit of all current local changes for bad logic, invalid states, unnecessary complexity, regressions, and misleading test coverage. Use when user says "validate current changes", "audit this diff", "review without fixing", or asks to look for bad logic or overcomplication.
- `./skills/worktree/SKILL.md`: A set of instructions and scripts for creating and managing git worktrees for this repository. Use when user wants to create a worktree for agent sessions/code changes/plan implementation.
- `./skills/write-a-skill/SKILL.md`: Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill.
