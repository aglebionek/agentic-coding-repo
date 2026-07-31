# Continue ordered agent-assets restructure: Phases 4–5

## Mode and target

Default handoff sequence.

- Repository: `/home/aglebionek/personal/knowledgebase/agentic-coding-repo`
- Branch: `refactor`
- Starting revision: `04af7cf`
- Starting worktree: clean
- Implementation approval: the user approved the ordered sequence in
  `2026-07-29-00-ordered-agent-assets-restructure.md`.
- Do not create a branch, worktree, commit, push, or external artifact unless
  the user asks.
- Preserve unrelated work.

## Resume state

Phases 1–3 are complete and committed:

1. `60bd514` — obsolete overlapping skills removed.
2. `e1cacfa` — `shared/TESTING_GUIDELINES.md` established as the canonical
   testing authority and added to the managed installer.
3. `04af7cf` — report/planner pairs and validation helpers internalized behind
   the `code-workflow` facade.

At this handoff:

- `skills/user-invoked/code-workflow/SKILL.md` is the sole public code-workflow facade.
- Five profiles live under `skills/user-invoked/code-workflow/profiles/`.
- Six internal specialists live under
  `skills/user-invoked/code-workflow/specialists/`; none contains `SKILL.md` or skill front
  matter.
- Shared specialist rules live in
  `skills/user-invoked/code-workflow/specialists/SPECIALIST-CONTRACT.md`.
- Selective routing lives in
  `skills/user-invoked/code-workflow/specialists/ROUTING.md`.
- Quality modules live under `skills/user-invoked/code-workflow/quality/`.
- Contract/fixture guidance lives under `skills/user-invoked/code-workflow/guidance/`.
- `skills/user-invoked/skill-authoring/create-code-workflow-specialist/SKILL.md` is the
  public authoring entrypoint.
- Root `AGENTS.md` advertises 17 public skills, matching the 17 existing
  `SKILL.md` files exactly.

Do not recreate retired standalone report/planner skills,
`testable-module`, `validate-current-changes`,
`review-intent-and-coverage`, or compatibility stubs.

## Governing plans

Read these files completely before editing:

1. `codex/handoffs/2026-07-29-00-ordered-agent-assets-restructure.md`
2. `codex/handoffs/2026-07-29-04-architecture-specialist.md`
3. `codex/handoffs/2026-07-29-05-public-skill-directories.md`

Implement only Phases 4 and 5, strictly in order. The detailed phase files are
the authority; the summary below is a navigation aid.

## Phase 4 — Internal architecture specialist

### Problem and approach

Retire the public `improve-codebase-architecture` skill after migrating its
valuable analytical vocabulary and design guidance into an internal,
read-only architecture specialist used selectively by
`code-workflow improve`.

Create:

```text
skills/user-invoked/code-workflow/specialists/architecture/
├── REPORT.md
├── REPORT-TEMPLATE.md
├── PLANNER.md
├── PLAN-TEMPLATE.md
├── LANGUAGE.md
├── DEEPENING.md
└── INTERFACE-DESIGN.md
```

Remove `skills/improve-codebase-architecture/` only after its compliant,
valuable content is represented in the internal module. Remove its public
catalog entry and direct trigger.

### Interfaces and routing

- Findings use stable `ARCH-*` identifiers.
- The report is diagnostic only: it records responsibility, files, friction,
  evidence, maintainer/caller burden, impact, constraints, reach, confidence,
  missing surfaces, and improvement direction without designing a concrete
  interface.
- The planner accepts a valid fresh report, selects one coherent finding or
  inseparable cluster, establishes authority and compatibility, compares at
  least two materially different module/interface structures, resolves material
  decisions interactively, and emits one read-only evidence-mapped plan.
- Route it only from `skills/user-invoked/code-workflow/profiles/IMPROVEMENT.md`.
- Select it for explicit architecture/depth/locality/leverage/facade/navigation
  requests or evidenced multi-module structural friction.
- In autorun, the report may run read-only; the first confirmed architecture
  finding stops autorun, and planning remains interactive.
- Parallel agents are optional and only allowed when the user explicitly asks
  for delegation.

### Architecture constraints

- Combine useful module, interface, implementation, depth, seam, adapter,
  leverage, locality, deletion-test, and interface-as-test-surface concepts
  with `shared/ARCHITECTURE_GUIDELINES.md`.
- Treat these terms as a preferred analytical lens, not exclusive vocabulary.
  `API` and `boundary` remain valid shared terms.
- A module may expose a primary public interface plus nested internal APIs and
  child-module interfaces.
- Adapter-count rules are heuristics, not prohibitions.
- Respect active project instructions, documentation profiles, contracts, and
  approved decisions.
- Do not hardcode `CONTEXT.md`, `docs/adr/`, documentation roots, or link
  formats.
- Do not write documentation during reporting or planning. After implementation
  approval, `grow-docs` records approved decisions and updates navigation.
- Use `shared/TESTING_GUIDELINES.md` as the sole testing authority. Existing
  valid tests remain until replacement proof and explicit approval permit a
  change.
- Inventory consumers and choose an explicit compatibility strategy whenever a
  public path or interface may change. Removing a temporary facade is separate
  approved work.

### Phase 4 validation and checkpoint

Run every gate in
`codex/handoffs/2026-07-29-04-architecture-specialist.md`, plus the common
gates from the ordered handoff. In particular verify:

- report and planner responsibilities remain separate;
- the report contains no concrete interface design;
- the planner compares at least two designs;
- routing is selective and autorun stops before planning;
- no mandatory sub-agent instruction or hardcoded documentation layout remains;
- testing routes only to the shared authority;
- missing documentation/authority surfaces and compatibility are explicit;
- no direct `improve-codebase-architecture` trigger remains;
- all templates and relative links resolve.

Invoke the current `give-commit-message` skill, print a Phase 4 commit message,
do not commit, and stop. Wait for the user to commit or explicitly authorize an
accumulated diff before Phase 5.

## Phase 5 — Group public skills by responsibility

Begin only from the user-approved Phase 4 checkpoint, preferably a clean commit.

### Target tree

Keep `code-workflow` as a deep top-level module and move complete public skill
bundles into:

```text
skills/
├── code-workflow/
├── interaction/
│   ├── answer-and-stop/
│   ├── caveman/
│   ├── grill-me/
│   └── list-dont-modify/
├── knowledge/
│   ├── domain-model/
│   ├── grill-me-with-docs/
│   ├── grow-docs/
│   └── grow-glossary/
├── delivery/
│   ├── create-gh-issue/
│   ├── create-gh-pr/
│   ├── give-commit-message/
│   ├── handoff/
│   └── worktree/
└── skill-authoring/
    ├── create-code-workflow-specialist/
    └── write-a-skill/
```

Group roots are organizational directories and must not contain `SKILL.md`.
Move complete bundles, preserve names and triggers, update all repository-owned
links, and do not leave compatibility `SKILL.md` files at old paths.

### Public reading and compatibility

- Root `AGENTS.md` remains the canonical public skill catalog and should be
  organized under responsibility headings.
- `skills/user-invoked/code-workflow/SKILL.md` remains the facade for internal specialists.
- Update code-workflow links to moved helpers such as `grill-me`, `grow-docs`,
  and `worktree`.
- Update README source-tree, skill-location, and migration documentation.
- External consumers with hardcoded source-repository paths must update them;
  installed projects receive a complete replacement `.agentic/skills/` tree.
- Do not add pass-through group skills or unnecessary group README files.

### Phase 5 validation and completion

Run every gate in
`codex/handoffs/2026-07-29-05-public-skill-directories.md`, plus the common
gates. Run `bash -n fetch-agent-assets.sh` and a disposable sentinel installer
test proving:

- project-owned root files and root `skills/` remain byte-identical;
- the complete reorganized shared skills tree is installed;
- stale managed skill paths disappear;
- the second install is idempotent.

Invoke `skills/user-invoked/delivery/give-commit-message/SKILL.md`, print the Phase 5 commit
message, and do not commit.

Report phase-by-phase outcomes, checks, commit messages, uncommitted phases,
residual risks, and confirmation that no automatic commit occurred.

## Shared gates and constraints

After each remaining phase:

```bash
git status --short
git diff --check
```

Also verify:

- every advertised `SKILL.md` exists exactly once;
- every remaining public skill is advertised exactly once;
- internal modules are not advertised as direct user skills;
- modified relative Markdown links resolve;
- removed paths have no stale repository-owned references;
- shared material remains project-agnostic;
- project-owned target files remain outside managed `.agentic/`;
- no commit, push, branch, worktree removal, or external mutation occurred.

If installed skills change, run `bash -n fetch-agent-assets.sh` and the
disposable sentinel installer test.

## Deferred decision

After Phase 4, explicitly remind the user that module, interface, depth, seam,
adapter, leverage, locality, and deletion test may be promoted into
`shared/AGENTIC_GLOSSARY.md`.

Do not promote them during Phases 4–5. If later approved, select one canonical
definition source and link from the other instead of duplicating definitions.
