---
name: create-code-workflow-specialist
description: Creates or updates an internal evidence-and-planning specialist behind the code-workflow facade. Use when the user explicitly asks to create or update a code-workflow specialist.
---

# Create Code Workflow Specialist

## Establish the evidence domain

1. Read [write-a-skill](../write-a-skill/SKILL.md), the
   [specialist contract](../../code-workflow/specialists/SPECIALIST-CONTRACT.md),
   and [routing table](../../code-workflow/specialists/ROUTING.md) completely.
2. Inspect existing specialists, profiles, artifact reconciliation, and quality
   gates.
3. Define the distinct evidence domain, required sources, exclusions, validity,
   finding identifiers, confidence/severity/reach vocabulary, and stop
   conditions.
4. Check overlap. Extend an existing specialist when the new responsibility
   does not require distinct evidence, validity, and planning semantics.
5. Resolve material design decisions and obtain approval before editing.

## Create the internal module

Under `skills/code-workflow/specialists/<name>/`, create only the justified
subset of:

```text
REPORT.md
REPORT-TEMPLATE.md
PLANNER.md
PLAN-TEMPLATE.md
CATALOG.md
```

- Keep report and planner modules read-only.
- Do not add skill front matter or `SKILL.md`.
- Preserve `Valid: true|false`, stable finding IDs, complete evidence, freshness,
  exact evidence-to-plan mapping, probable-finding gates, and specialist stop
  conditions.
- Keep templates and references local to their specialist.
- Support internal `manual` and `autorun` behavior under the facade; autorun
  must reject invalid reports and material ambiguity without interactive
  fallback.

## Integrate selectively

1. Add the specialist to `specialists/ROUTING.md`.
2. Route it only from profiles with a concrete evidence need and retain the
   profile-specific selection reason.
3. Update `ARTIFACT-CONTRACT.md` so identifiers and specialist-specific fields
   survive reconciliation.
4. Update quality gates only when the specialist adds a distinct validation or
   stop requirement.
5. Keep coordination, implementation approval, execution, documentation, and
   external actions in the code-workflow facade.

## Validate

- Every internal link and template resolves.
- Report and planner responsibilities remain separate.
- Finding IDs and template fields reconcile through the artifact contract.
- `Valid: false`, stale evidence, probable findings, and autorun stops behave as
  specified.
- No generated specialist is advertised in `AGENTS.md` or exposed as a direct
  user skill.
- Perform the compact pass from `write-a-skill`.
