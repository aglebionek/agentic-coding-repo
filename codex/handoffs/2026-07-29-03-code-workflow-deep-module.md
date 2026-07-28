# Phase 3: Make code-workflow a deep module

## Problem

`code-workflow` coordinates many globally advertised specialist skills and
quality helpers. Callers must understand internal report/planner pairs,
testability mechanics, and validation ordering that the workflow should own.

## Public contract

`skills/code-workflow/SKILL.md` remains the single public facade for:

- `code-workflow issue <issue-number-or-url> [manual|autorun]`;
- `code-workflow bug-fix <report-or-target> [manual|autorun]`;
- `code-workflow improve <file-or-directory> [manual|autorun]`;
- `code-workflow js-to-ts <files-or-symbols> [manual|autorun]`;
- `code-workflow js-to-ts-autoscope <seed> [deep|wide] [manual|autorun]`.

All report/planner pairs become internal instruction modules. They preserve
their evidence and planning contracts but cease being independently advertised
skills.

## Desired module tree

```text
skills/code-workflow/
├── SKILL.md
├── ARTIFACT-CONTRACT.md
├── profiles/
│   ├── ISSUE.md
│   ├── BUG-FIX.md
│   ├── IMPROVEMENT.md
│   ├── JS-TO-TS.md
│   └── JS-TO-TS-AUTOSCOPE.md
├── specialists/
│   ├── SPECIALIST-CONTRACT.md
│   ├── ROUTING.md
│   ├── bug-hunt/
│   ├── code-smells/
│   ├── coding-standards-accordance/
│   ├── purpose-adherence/
│   ├── js-to-ts/
│   └── js-to-ts-autoscope/
├── quality/
│   ├── QUALITY-GATES.md
│   └── CURRENT-CHANGES-AUDIT.md
└── guidance/
    └── CONTRACT-AND-FIXTURES.md
```

Phase 4 adds `specialists/architecture/`.

Each specialist directory contains the applicable subset of:

```text
REPORT.md
REPORT-TEMPLATE.md
PLANNER.md
PLAN-TEMPLATE.md
CATALOG.md
```

Supporting files remain local to the specialist that owns them.

## Internalize report/planner pairs

Move and adapt these existing pairs:

- `skills/bug-hunt/{report,planner}`;
- `skills/code-smells/{report,planner}`;
- `skills/coding-standards-accordance/{report,planner}`;
- `skills/purpose-adherence/{report,planner}`;
- `skills/js-to-ts/{report,planner}`;
- `skills/js-to-ts-autoscope/{report,planner}`.

Rules:

- Rename report `SKILL.md` entrypoints to `REPORT.md`.
- Rename planner `SKILL.md` entrypoints to `PLANNER.md`.
- Remove skill front matter and direct user triggers.
- Preserve finding IDs, validity rules, templates, severity/reach/confidence,
  evidence requirements, planner modes, and stop conditions.
- Update code-workflow profiles to read the exact internal report and planner
  files.
- Remove registration metadata that exists only to advertise a standalone
  specialist skill.
- Do not merge unlike specialist vocabularies or severity systems.

## Specialist contract

Create `specialists/SPECIALIST-CONTRACT.md` from the reusable parts of the
current artifact contract and `create-report-planner-skill`:

- report scope and evidence requirements;
- `Valid: true|false` semantics;
- stable finding identifiers;
- freshness and repository/scope identity;
- report template requirements;
- planner input validation;
- exact evidence-to-plan mapping;
- manual and autorun behavior;
- probable-finding verification gates;
- preservation of specialist confidence, reach, and stop conditions.

Create `specialists/ROUTING.md` as the canonical internal routing table. Profiles
link to it but retain the profile-specific reason for selecting a specialist.

## Replace the authoring skill

Replace `skills/create-report-planner-skill/` with:

```text
skills/skill-authoring/create-code-workflow-specialist/
└── SKILL.md
```

This remains a public authoring skill. It:

1. establishes a distinct evidence domain and checks overlap;
2. reads `specialists/SPECIALIST-CONTRACT.md`;
3. creates internal `REPORT.md`, `PLANNER.md`, and templates;
4. adds selective routing to the correct profiles;
5. updates artifact reconciliation and quality gates when necessary;
6. validates links, templates, finding IDs, and stop behavior;
7. never advertises the generated specialist as a direct user skill.

## Retire testable-module

Delete the standalone `skills/testable-module/` skill and its catalog entry.

Preserve only workflow-specific mechanics in
`guidance/CONTRACT-AND-FIXTURES.md`:

- establish and approve the public contract during planning;
- identify realistic fixtures before implementation;
- map contract examples and edges into the approved testing plan.

Do not duplicate shared testing rules. Contract-first TDD, verified red/green,
hardening, test preservation, fakes, and exceptions come exclusively from
`shared/TESTING_GUIDELINES.md`.

Module/interface architecture remains in the shared architecture and coding
guidelines.

## Consolidate quality helpers

Delete standalone:

- `skills/validate-current-changes/`;
- `skills/review-intent-and-coverage/`.

Create `quality/CURRENT-CHANGES-AUDIT.md` from the useful skeptical, read-only
audit behavior in `validate-current-changes`.

Distribute `review-intent-and-coverage` responsibilities:

- behavioral intent confirmation belongs in workflow intake and validation;
- test hardening belongs in `shared/TESTING_GUIDELINES.md`;
- test or implementation edits require the approved plan or supplemental
  approval.

Do not retain a separate review-intent internal module unless evidence shows a
distinct responsibility after this distribution.

## Move workflow-owned references

- Move existing profile files into `profiles/` with the names shown above.
- Move `QUALITY-GATES.md` into `quality/`.
- Keep `ARTIFACT-CONTRACT.md` at the code-workflow root as the facade's durable
  work-package contract.
- Update every relative link after moves.
- Keep `SKILL.md` concise and route deeper capability through profiles,
  specialist modules, quality gates, and guidance.

## Catalog and documentation

- Remove all internal report/planner entries from the `AGENTS.md` public skills
  catalog.
- Remove standalone entries for `testable-module`,
  `validate-current-changes`, and `review-intent-and-coverage`.
- Add `create-code-workflow-specialist` with its exact trigger.
- Keep `code-workflow` as the public entrypoint for specialist capabilities.
- Update README descriptions that imply the internal modules are directly
  invocable.

## Compatibility

This is an explicitly approved breaking cleanup of skill invocation paths.
Do not create compatibility `SKILL.md` stubs because runtimes may discover them
as duplicate public skills.

The installer replaces `.agentic/skills/` as part of the managed tree, so stale
installed skill paths disappear on update. Document the public invocation
change in the README migration section.

## Gates

- No `SKILL.md` exists beneath `code-workflow/specialists/`.
- No old report/planner path remains.
- No stale standalone trigger remains in `AGENTS.md`, README, or internal docs.
- Every profile resolves its report, planner, template, quality, artifact, and
  shared-guideline references.
- Specialist IDs and template fields remain unchanged unless this plan
  explicitly requires a structural location update.
- `code-workflow` still preserves explicit implementation approval.
- Autorun stop conditions remain at least as strict as before.
- The shared testing guideline is the only canonical testing policy.
- Run relevant internal content/link audits and the common gates.

## End-of-phase GCM

After all gates pass, invoke the current `give-commit-message` skill and produce
a commit message for the code-workflow internalization only. Do not commit. Stop
for the user's checkpoint before Phase 4.
