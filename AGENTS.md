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

- `shared/AGENTS_TEMPLATE.md` — copyable project-owned instruction template
  installed under `.agentic/`.
- `shared/BASE_AGENT_GUIDELINES.md` — compact operating guidance for installed
  projects.
- `shared/ARCHITECTURE_GUIDELINES.md` — canonical shared architecture and
  documentation principles.
- `shared/CODING_GUIDELINES.md` — canonical reusable JavaScript and TypeScript
  coding guidance.
- `shared/TESTING_GUIDELINES.md` — canonical project-agnostic testing guidance.
- `shared/AGENTIC_GLOSSARY.md` — canonical project-agnostic workflow terms.
- `skills/` — reusable skill sources. Read the matching `SKILL.md` completely
  before using or changing a skill.
- `notes/AI/Key Ideas/` — research context; shared guidelines remain the
  operational authority.
- `README.md` — installation, ownership, migration, and adoption guide.

## Skills

Read the referenced `SKILL.md` completely after selecting a skill.
Load only skills whose trigger matches the request.

### Code workflow
These skills are groupings of related skills that implement a complete code workflow.

- `skills/user-invoked/code-workflow/SKILL.md` — Use when the user invokes `code-workflow`
  with the `issue`, `bug-fix`, `improve`, `js-to-ts`, or `js-to-ts-autoscope`
  profile.

### Interaction

- `skills/user-invoked/interaction/answer-and-stop/SKILL.md` — Use when the user wants a direct answer
  with no follow-up questions or types `a&s`.
- `skills/user-invoked/interaction/caveman/SKILL.md` — Use when the user says `caveman mode`,
  `talk like caveman`, `use caveman`, or `/caveman`.
- `skills/user-invoked/interaction/grill-me/SKILL.md` — Use when the user asks to be grilled
  or wants to stress-test a plan or design through questioning.
- `skills/user-invoked/interaction/list-dont-modify/SKILL.md` — Use when the user says
  `list don't modify`, `list only`, or `LDM`.

### Knowledge

- `skills/knowledge/domain-model/SKILL.md` — Use when the user wants to
  stress-test a plan against the project's domain language and documented
  decisions.
- `skills/knowledge/grill-me-with-docs/SKILL.md` — Use when the user asks to be
  grilled with docs or wants settled design decisions preserved in
  documentation.
- `skills/knowledge/grow-docs/SKILL.md` — Use when the user invokes `grow-docs`,
  asks to document or expand a responsibility, improve documentation
  navigation, run a documentation link or gap pass, or record an
  already-approved decision.
- `skills/knowledge/grow-glossary/SKILL.md` — Use when the user asks to grow a
  glossary, calcify terminology, or review missing glossary candidates.

### Delivery

- `skills/user-invoked/delivery/create-gh-issue/SKILL.md` — Use when the user asks to create, draft,
  or turn work into a GitHub issue.
- `skills/user-invoked/delivery/create-gh-pr/SKILL.md` — Use when the user asks to create or draft a
  GitHub pull request.
- `skills/user-invoked/delivery/give-commit-message/SKILL.md` — Use when the user says `GCM`,
  `give commit message`, or otherwise asks for a commit message.
- `skills/user-invoked/delivery/handoff/SKILL.md` — Use when the user says `handoff`,
  `handoff branch`, `handoff worktree`, `save plan`, or asks to continue in a
  new session.
- `skills/user-invoked/delivery/handoff/worktree/SKILL.md` — Use when the user asks to create or
  manage a Git worktree for agent sessions, code changes, or plan
  implementation.

### Skill authoring

- `skills/user-invoked/skill-authoring/create-code-workflow-specialist/SKILL.md` — Use when
  the user explicitly asks to create or update a code-workflow specialist.
- `skills/user-invoked/skill-authoring/write-a-skill/SKILL.md` — Use when the user asks to
  create, write, build, or update an agent skill.

## Documentation profile

- Approachable documentation: `README.md`
- Technical guidance: `shared/`
- Supporting research: `notes/`
- Documentation mirrors stable responsibilities rather than individual files.

When modifying the distribution model, validate it against a disposable target
with sentinel project-owned files. Never test the network bootstrap against a
real project.
