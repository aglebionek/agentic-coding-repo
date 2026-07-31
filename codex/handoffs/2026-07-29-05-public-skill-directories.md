# Phase 5: Group public skills by responsibility

## Problem

After code-workflow internalization, the remaining public skills are still
presented as one mostly flat directory. The structure does not reveal why a
reader would use each skill.

## Desired tree

Keep `code-workflow` as its own deep top-level module and group the remaining
public skills:

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

The group directories are organizational responsibilities, not invocable
wrapper skills. Do not add `SKILL.md` files at group roots.

## Migration

- Move each complete skill bundle, including scripts, examples, references, and
  metadata.
- Preserve each public skill's `name` and trigger contract unless an earlier
  phase explicitly changed it.
- Update all relative links across skills and supporting Markdown.
- Update code-workflow links to the new locations for shared public helpers such
  as `grill-me`, `grow-docs`, and `worktree`.
- Rewrite the `AGENTS.md` catalog under responsibility headings while retaining
  one concise trigger sentence per public skill.
- Update README source-tree and skill-location documentation.
- Keep `fetch-agent-assets.sh` behavior unchanged unless validation exposes a
  path assumption; it should already copy the complete `skills/` tree.

## Public reading and discovery

- Root `AGENTS.md` remains the canonical public skill catalog.
- `skills/user-invoked/code-workflow/SKILL.md` remains the code-workflow facade.
- Every public skill remains reachable directly from the catalog.
- Internal code-workflow modules remain discoverable only through the
  code-workflow facade and routing files.
- Do not duplicate detailed skill instructions in group indexes.
- Add a minimal group README only if it hides meaningful navigation complexity;
  do not create pass-through documentation by default.

## Compatibility

This is an approved atomic path migration. Do not leave duplicate compatibility
`SKILL.md` files at old paths.

Before moving, search the entire repository for links to each old path. After
moving, update every repository-owned reference.

Document that external consumers with hardcoded source-repository skill paths
must update them. Installed projects receive the complete replacement
`.agentic/skills/` tree on their next managed update.

## Gates

- Every `SKILL.md` is under one intended public group or the code-workflow
  facade.
- No group root contains `SKILL.md`.
- Every advertised skill path exists exactly once.
- Every remaining public skill is advertised exactly once.
- No internal code-workflow report/planner appears in the public catalog.
- All relative Markdown links in `skills/`, `AGENTS.md`, and README resolve.
- No old public skill path remains in repository-owned documentation.
- Skill front-matter names and descriptions remain valid and trigger-focused.
- The installer disposable test still produces the complete reorganized skills
  tree while preserving project-owned root `skills/`.
- Run `bash -n fetch-agent-assets.sh` and the common gates.

## End-of-phase GCM

After all gates pass, invoke
`skills/user-invoked/delivery/give-commit-message/SKILL.md` and produce a commit message for
the public skill-directory migration only. Do not commit.

Report the deferred architecture-glossary option from Phase 4 and stop for the
user's final review.
