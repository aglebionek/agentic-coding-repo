# <Project Name>

## Purpose

<Describe why this project exists, who it serves, and the outcomes it owns.>

## Project rules

- ALWAYS use `grill-me-with-docs` if requirements or intended behavior are
  materially uncertain.
- NEVER start implementing a plan before user approval.
- NEVER commit anything unless asked to.
- NEVER delete worktrees unless asked to.
- <Add project-specific safety, security, and access constraints.>
- <Add compatibility, migration, and destructive-action constraints.>
- <Add domain or architecture rules that shared guidance must not override.>
- <Add project-specific external-action authorization rules when needed.>

## Shared agent resources

Read and follow:

- `.agentic/BASE_AGENT_GUIDELINES.md`
- `.agentic/TESTING_GUIDELINES.md` when executable behavior may change
- `.agentic/CODING_GUIDELINES.md` when changing JavaScript or TypeScript
- `.agentic/AGENTIC_GLOSSARY.md` for shared workflow terminology

Project instructions and approved project decisions override optional shared
defaults. Keep project-owned instructions, documentation, glossaries, and local
skills outside `.agentic/`.

## Skills

Read the referenced `SKILL.md` completely after selecting a skill. Load only
skills whose trigger matches the request.

Skills under `.agentic/skills/user-invoked/` run only when the user explicitly
invokes them. Skills under `.agentic/skills/agent-invoked/` may also be selected
automatically when their trigger matches the task.

### Code workflow
These skills are groupings of related skills that implement a complete code workflow.

- `.agentic/skills/user-invoked/code-workflow/SKILL.md` — Use when the user invokes
  `code-workflow` with the `issue`, `bug-fix`, `improve`, `js-to-ts`, or
  `js-to-ts-autoscope` profile.

### Engineering workflows

- `.agentic/skills/user-invoked/engineering/grill-with-docs/SKILL.md` — Use
  when the user invokes `grill-with-docs` or asks to preserve decisions during
  a design interview.
- `.agentic/skills/user-invoked/engineering/to-spec/SKILL.md` — Use when the
  user invokes `to-spec` to synthesize the current conversation into a
  published specification.
- `.agentic/skills/user-invoked/engineering/to-tickets/SKILL.md` — Use when the
  user invokes `to-tickets` to split approved work into tracer-bullet tickets.
- `.agentic/skills/user-invoked/engineering/implement/SKILL.md` — Use when the
  user invokes `implement` with an approved spec or set of tickets.
- `.agentic/skills/user-invoked/engineering/wayfinder/SKILL.md` — Use when the
  user invokes `wayfinder` for work too large or uncertain for one agent
  session.

### Engineering disciplines

- `.agentic/skills/agent-invoked/engineering/domain-modeling/SKILL.md` — Use
  when domain terminology or architectural decisions need to be challenged or
  recorded.
- `.agentic/skills/agent-invoked/engineering/testable-module/SKILL.md` — Use
  when behavior needs a stable public module contract and deterministic test
  seam before TDD.
- `.agentic/skills/agent-invoked/engineering/tdd/SKILL.md` — Use when
  implementing behavior test-first with a red-green loop at agreed seams.
- `.agentic/skills/agent-invoked/engineering/code-review/SKILL.md` — Use when
  reviewing changes against both repository standards and an originating
  specification.

### Interaction

- `.agentic/skills/agent-invoked/productivity/grilling/SKILL.md` — Use when a
  plan, decision, or idea needs a one-question-at-a-time stress test.
- `.agentic/skills/user-invoked/interaction/answer-and-stop/SKILL.md` — Use when the user
  wants a direct answer with no follow-up questions or types `a&s`.
- `.agentic/skills/user-invoked/interaction/caveman/SKILL.md` — Use when the user says
  `caveman mode`, `talk like caveman`, `use caveman`, or `/caveman`.
- `.agentic/skills/user-invoked/interaction/grill-me/SKILL.md` — Use when the user asks to
  be grilled or wants to stress-test a plan or design through questioning.
- `.agentic/skills/user-invoked/interaction/list-dont-modify/SKILL.md` — Use when the user
  says `list don't modify`, `list only`, or `LDM`.

### Productivity

- `.agentic/skills/user-invoked/productivity/teach/SKILL.md` — Use when the
  user invokes `teach` or asks for a stateful, multi-session learning workflow.

### Knowledge

- `.agentic/skills/knowledge/domain-model/SKILL.md` — Use when the user wants
  to stress-test a plan against the project's domain language and documented
  decisions.
- `.agentic/skills/knowledge/grill-me-with-docs/SKILL.md` — Use when the user
  asks to be grilled with docs or wants settled design decisions preserved in
  documentation.
- `.agentic/skills/knowledge/grow-docs/SKILL.md` — Use when the user invokes
  `grow-docs`, asks to document or expand a responsibility, improve
  documentation navigation, run a documentation link or gap pass, or record an
  already-approved decision.
- `.agentic/skills/knowledge/grow-glossary/SKILL.md` — Use when the user asks
  to grow a glossary, calcify terminology, or review missing glossary
  candidates.

### Delivery

- `.agentic/skills/user-invoked/delivery/create-gh-issue/SKILL.md` — Use when the user asks
  to create, draft, or turn work into a GitHub issue.
- `.agentic/skills/user-invoked/delivery/create-gh-pr/SKILL.md` — Use when the user asks to
  create or draft a GitHub pull request.
- `.agentic/skills/user-invoked/delivery/give-commit-message/SKILL.md` — Use when the user
  says `GCM`, `give commit message`, or otherwise asks for a commit message.
- `.agentic/skills/user-invoked/delivery/handoff/SKILL.md` — Use when the user says
  `handoff`, `handoff branch`, `handoff worktree`, `save plan`, or asks to
  continue in a new session.
- `.agentic/skills/user-invoked/delivery/handoff/worktree/SKILL.md` — Use when the user asks to
  create or manage a Git worktree for agent sessions, code changes, or plan
  implementation.

### Skill authoring

- `.agentic/skills/user-invoked/skill-authoring/create-code-workflow-specialist/SKILL.md` —
  Use when the user explicitly asks to create or update a code-workflow
  specialist.
- `.agentic/skills/user-invoked/skill-authoring/write-a-skill/SKILL.md` — Use when the user
  asks to create, write, build, or update an agent skill.

## Documentation profile

- Approachable documentation: `<path or none>`
- Technical documentation: `<path or none>`
- Supporting research or notes: `<path or none>`
- Canonical decision format/location: `<path, convention, or none>`
- Documentation organization:
  `<describe the stable responsibilities mirrored by docs>`

## Project validation

- Tests: `<command or not applicable>`
- Lint: `<command or not applicable>`
- Type checking: `<command or not applicable>`
- Build: `<command or not applicable>`
- Additional required checks: `<commands or none>`

## Project glossary

- Project terminology: `<path such as GLOSSARY.md, or none>`
- Domain/context documentation: `<paths or none>`

## Local skills

Project-specific skills live under root `skills/`, outside the managed
`.agentic/` directory.

- `<skills/project-skill/SKILL.md>` — <Describe its trigger, or remove this
  placeholder when the project has no local skills.>
