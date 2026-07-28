# Ordered agent-assets restructure

## Mode and target

Default handoff sequence.

- Repository: `C:\Users\agleb\Desktop\agentic-coding-repo`
- Implementation approval: the user approved this ordered implementation
  sequence on 2026-07-29.
- Do not create a branch, worktree, commit, or push unless the user asks.
- Preserve unrelated work.

## Purpose

Implement the approved testing-guidance and skill-architecture changes as
separate, reviewable phases. Each phase has its own scope and validation gates.
Do not collapse the phases into one undifferentiated diff.

## Completed baseline to preserve

Work completed earlier in this conversation or immediately before this sequence
is not part of the future rewrites:

- the shared-base/project-overlay distribution under `.agentic/`;
- canonical shared architecture, coding, and agentic glossary files;
- project-owned root instructions, glossary, local skills, and documentation;
- the project-agnostic `grow-docs` overview/technical workflow;
- overview documentation following responsibility hierarchy with nested-doc,
  related-code, and warranted technical links;
- `grill-me-with-docs` owning decision elicitation while `grow-docs` owns
  placement of already-approved decisions;
- the complete trigger-focused public skill catalog in `AGENTS.md`;
- the obsolete-skill cleanup captured in Phase 1.

Do not regress these contracts while moving or internalizing skills.

## Ordered phase files

1. [`2026-07-29-01-finalize-skill-cleanup.md`](2026-07-29-01-finalize-skill-cleanup.md)
2. [`2026-07-29-02-shared-testing-guidelines.md`](2026-07-29-02-shared-testing-guidelines.md)
3. [`2026-07-29-03-code-workflow-deep-module.md`](2026-07-29-03-code-workflow-deep-module.md)
4. [`2026-07-29-04-architecture-specialist.md`](2026-07-29-04-architecture-specialist.md)
5. [`2026-07-29-05-public-skill-directories.md`](2026-07-29-05-public-skill-directories.md)

Implement them strictly in order. Later phases assume the contracts and file
layout established by earlier phases.

## Per-phase execution contract

For each phase:

1. Read the phase file completely.
2. Confirm the repository state matches the phase's expected baseline.
3. Implement only that phase.
4. Run every phase gate and the common gates below.
5. Stop if a required gate fails; do not continue into later phases.
6. Inspect the complete phase diff for scope and authority drift.
7. Invoke the current `give-commit-message` skill and print a commit message for
   that phase.
8. Do not commit automatically.
9. Wait for the user to commit or explicitly authorize continuing with an
   accumulated diff. Prefer beginning each new phase from a clean committed
   baseline so its gate results and commit message remain attributable.

## Common gates

Run after every phase:

```bash
git status --short
git diff --check
```

Also verify:

- every `SKILL.md` path advertised in `AGENTS.md` exists;
- every remaining user-invocable skill appears exactly once in the catalog;
- internal instruction modules are not advertised as direct user skills;
- modified relative Markdown links resolve;
- removed paths have no stale references;
- no commit, push, branch, worktree removal, or external mutation occurred.

If `fetch-agent-assets.sh` or any file installed beneath `.agentic/` changes,
also run:

```bash
bash -n fetch-agent-assets.sh
```

and the disposable sentinel installer test documented in the relevant phase.

## Shared constraints

- Use progressive disclosure and responsibility-first organization.
- `code-workflow/SKILL.md` is the facade for code-workflow capabilities.
- Internal code-workflow modules must not leak coordination duties to callers.
- Project-owned target files remain outside the managed `.agentic/` tree.
- Do not create duplicate compatibility `SKILL.md` files; duplicate skill
  discovery is worse than a deliberate atomic path migration.
- Compatibility removal is explicit and separately scoped.
- Shared testing guidance becomes the sole canonical testing authority.
- Documentation changes follow the active documentation profile.
- Preserve one canonical location for every normative claim.

## Deferred decision

The user may later promote terminology from the architecture specialist into
`shared/AGENTIC_GLOSSARY.md`, including module, interface, depth, seam, adapter,
leverage, locality, and deletion test. Do not copy these definitions during this
sequence. After the architecture specialist is complete, report the terms as a
deferred glossary decision so the user can choose one canonical source.

## Exact continuation instruction

Read this file and every phase file it links. Implement the phases strictly in
order. Run each phase's gates, invoke `give-commit-message` at its end, do not
commit automatically, and stop at each checkpoint as directed.

## Completion

After Phase 5 passes, report:

- phase-by-phase outcomes and gate results;
- commit messages produced;
- any phase the user did not commit;
- residual risks or deferred decisions;
- confirmation that no automatic commits were made.
