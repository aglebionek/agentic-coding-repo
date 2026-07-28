# Phase 1: Finalize obsolete skill cleanup

## Expected baseline

This cleanup was already implemented in the planning session and is currently
present as local changes. Do not repeat or broaden it.

Expected changes:

- delete `skills/review-changes/SKILL.md`;
- delete `skills/handoff-to-worktree/SKILL.md`;
- delete `skills/implement-strategy/SKILL.md`;
- delete `skills/implement-strategy/EXAMPLE.md`;
- remove their catalog entries from `AGENTS.md`;
- remove the legacy `handoff-to-worktree` trigger from
  `skills/handoff/SKILL.md`.

At handoff creation, the repository reported exactly these relevant changes:

```text
 M AGENTS.md
 D skills/handoff-to-worktree/SKILL.md
 M skills/handoff/SKILL.md
 D skills/implement-strategy/EXAMPLE.md
 D skills/implement-strategy/SKILL.md
 D skills/review-changes/SKILL.md
```

If the baseline differs because the user already committed the cleanup, inspect
the committed state and validate it rather than recreating changes.

## Reason

- `review-changes` was a thin overlap with stronger validation workflows.
- `handoff-to-worktree` was an obsolete compatibility alias for `handoff`
  worktree mode.
- `implement-strategy` was an unreferenced orchestration wrapper whose duties
  already belonged to other workflows.

## Scope

Do not remove any other skill in this phase. In particular, later phases own
the retirement or conversion of:

- `testable-module`;
- `validate-current-changes`;
- `review-intent-and-coverage`;
- `improve-codebase-architecture`;
- report/planner skill entrypoints.

## Gates

Verify no stale reference remains:

```bash
rg -n "review-changes|handoff-to-worktree|implement-strategy" \
  AGENTS.md README.md skills shared fetch-agent-assets.sh
```

The command should return no matches.

Verify the `AGENTS.md` catalog exactly matches remaining `SKILL.md` entrypoints
and every listed path resolves. At handoff creation, the expected count after
cleanup was 32 skills.

Run the common gates from the ordered handoff.

## End-of-phase GCM

After all gates pass, invoke `give-commit-message` and produce a commit message
for this cleanup only. Do not commit. Stop for the user's checkpoint before
Phase 2.
