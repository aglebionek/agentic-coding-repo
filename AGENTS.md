# Agentic Coding Repo

## Purpose

This repository is the source for reusable agent instructions, skills,
architecture and coding guidelines, shared workflow terminology, and the
bootstrap tooling that distributes them to other projects.

Root files govern maintenance of this repository. They are not templates for a
target project's root files.

## Rules

- ALWAYS use `grill-me-with-docs` if requirements or intended behavior are
  materially uncertain.
- NEVER start implementing a plan before user approval.
- NEVER commit anything unless asked to.
- NEVER delete worktrees unless asked to.
- Preserve the shared-base/project-overlay ownership boundary:
  - reusable managed assets belong in `shared/` and `skills/`;
  - installed shared assets belong under `.agentic/`;
  - a target project's root instructions, glossary, docs, and local skills are
    project-owned and must not be overwritten.
- Keep shared material project-agnostic. Project-domain rules and automated
  guardrails remain in the project that owns them.
- Treat compatibility removal as a separate, explicitly approved change.

## Model resources

- `shared/BASE_AGENT_GUIDELINES.md` — compact operating guidance for installed
  projects.
- `shared/ARCHITECTURE_GUIDELINES.md` — canonical shared architecture and
  documentation principles.
- `shared/CODING_GUIDELINES.md` — canonical reusable JavaScript and TypeScript
  coding guidance.
- `shared/AGENTIC_GLOSSARY.md` — canonical project-agnostic workflow terms.
- `skills/` — reusable skill sources. Read the matching `SKILL.md` completely
  before using or changing a skill.
- `notes/AI/Key Ideas/` — research context; shared guidelines remain the
  operational authority.
- `README.md` — installation, ownership, migration, and adoption guide.

## Skills

Read the referenced `SKILL.md` completely after selecting a skill.

- `skills/answer-and-stop/SKILL.md` — Use when the user wants a direct answer
  with no follow-up questions or types `a&s`.
- `skills/bug-hunt/planner/SKILL.md` — Use only when the user invokes
  `bug-hunt planner` or `bug-hunt autoplan` with a bug-hunt report.
- `skills/bug-hunt/report/SKILL.md` — Use only when the user invokes
  `bug-hunt report` for a file, directory, current changes, or the codebase.
- `skills/caveman/SKILL.md` — Use when the user says `caveman mode`,
  `talk like caveman`, `use caveman`, or `/caveman`.
- `skills/code-smells/planner/SKILL.md` — Use only when the user invokes
  `code-smells planner`, `code-smells autoplan`, or
  `code-smells autoplan-force` with a report.
- `skills/code-smells/report/SKILL.md` — Use only when the user invokes
  `code-smells report` for a file, directory, or the codebase.
- `skills/code-workflow/SKILL.md` — Use when the user invokes `code-workflow`
  with the `issue`, `bug-fix`, `improve`, `js-to-ts`, or `js-to-ts-autoscope`
  profile.
- `skills/coding-standards-accordance/planner/SKILL.md` — Use only when the user
  invokes `coding-standards-accordance planner` or
  `coding-standards-accordance autoplan` with a report.
- `skills/coding-standards-accordance/report/SKILL.md` — Use only when the user
  invokes `coding-standards-accordance report` for JavaScript or TypeScript
  files, a directory, current changes, or the codebase.
- `skills/create-gh-issue/SKILL.md` — Use when the user asks to create, draft,
  or turn work into a GitHub issue.
- `skills/create-gh-pr/SKILL.md` — Use when the user asks to create or draft a
  GitHub pull request.
- `skills/create-report-planner-skill/SKILL.md` — Use only when the user asks
  to create or update a report/planner skill pair.
- `skills/domain-model/SKILL.md` — Use when the user wants to stress-test a
  plan against the project's domain language and documented decisions.
- `skills/give-commit-message/SKILL.md` — Use when the user says `GCM`,
  `give commit message`, or otherwise asks for a commit message.
- `skills/grill-me/SKILL.md` — Use when the user asks to be grilled or wants to
  stress-test a plan or design through questioning.
- `skills/grill-me-with-docs/SKILL.md` — Use when the user asks to be grilled
  with docs or wants settled design decisions preserved in documentation.
- `skills/grow-docs/SKILL.md` — Use when the user invokes `grow-docs`, asks to
  document or expand a responsibility, improve documentation navigation, or run
  a documentation link or gap pass, or record an already-approved decision.
- `skills/grow-glossary/SKILL.md` — Use when the user asks to grow a glossary,
  calcify terminology, or review missing glossary candidates.
- `skills/handoff/SKILL.md` — Use when the user says `handoff`,
  `handoff branch`, `handoff worktree`, `save plan`, or asks to continue in a
  new session.
- `skills/improve-codebase-architecture/SKILL.md` — Use when the user asks to
  improve architecture, deepen modules, increase locality or leverage,
  consolidate tightly coupled modules, or improve testability and navigability.
- `skills/js-to-ts/planner/SKILL.md` — Use only when the user invokes
  `js-to-ts planner` or `js-to-ts autoplan` with a valid report.
- `skills/js-to-ts/report/SKILL.md` — Use only when the user invokes
  `js-to-ts report` with JavaScript or JSX files or symbols.
- `skills/js-to-ts-autoscope/planner/SKILL.md` — Use only when the user invokes
  `js-to-ts-autoscope planner` or `js-to-ts-autoscope autoplan` with a report.
- `skills/js-to-ts-autoscope/report/SKILL.md` — Use only when the user invokes
  `js-to-ts-autoscope report` with a seed file or small seed set.
- `skills/list-dont-modify/SKILL.md` — Use when the user says
  `list don't modify`, `list only`, or `LDM`.
- `skills/purpose-adherence/planner/SKILL.md` — Use only when the user invokes
  `purpose-adherence planner` or `purpose-adherence autoplan` with a valid
  report.
- `skills/purpose-adherence/report/SKILL.md` — Use only when the user invokes
  `purpose-adherence report` with code targets and an approved purpose contract.
- `skills/review-intent-and-coverage/SKILL.md` — Use when the user asks whether
  current changes match intended behavior or whether tests and coverage are
  sufficient.
- `skills/testable-module/SKILL.md` — Use when the user asks to make code
  testable, extract a module API, or rewrite code as a module.
- `skills/validate-current-changes/SKILL.md` — Use when the user asks to
  validate or audit current changes without fixing them, especially for bad
  logic, invalid states, regressions, or overcomplication.
- `skills/worktree/SKILL.md` — Use when the user asks to create or manage a Git
  worktree for agent sessions, code changes, or plan implementation.
- `skills/write-a-skill/SKILL.md` — Use when the user asks to create, write,
  build, or update an agent skill.

## Documentation profile

- Approachable documentation: `README.md`
- Technical guidance: `shared/`
- Supporting research: `notes/`
- Documentation mirrors stable responsibilities rather than individual files.

When modifying the distribution model, validate it against a disposable target
with sentinel project-owned files. Never test the network bootstrap against a
real project.
