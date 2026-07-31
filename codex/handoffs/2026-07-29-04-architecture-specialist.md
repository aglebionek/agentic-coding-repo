# Phase 4: Replace improve-codebase-architecture with an internal specialist

## Problem

The existing `improve-codebase-architecture` skill contains valuable terminology
and design ideas but conflicts with the shared architecture:

- it hardcodes `CONTEXT.md` and `docs/adr/`;
- it rejects terms such as API and boundary that have valid shared meanings;
- it assumes one module has exactly one interface;
- it forces sub-agent use;
- it writes documentation during design;
- it treats test deletion too casually;
- it makes absolute deepening claims.

It also overlaps the public orchestration already owned by
`code-workflow improve`.

## Approach

Retire the standalone skill after migrating its valuable content into:

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

This specialist is internal-only. It is loaded exclusively by
`code-workflow improve`.

## Selective routing

Run the architecture report only when:

- the request explicitly concerns architecture, module depth, responsibility
  organization, locality, leverage, facades, navigability, or public
  entrypoints; or
- initial exploration provides evidence of multi-module or structural friction.

Do not run it for every improvement.

`code-workflow improve autorun` may run the read-only report. The first confirmed
architecture finding triggers the existing architecture stop condition; the
planner always requires interactive user participation before design choices.

## Combined analytical scope

Preserve the useful nomenclature:

- module;
- interface;
- implementation;
- depth;
- seam;
- adapter;
- leverage;
- locality;
- deletion test;
- interface as the preferred behavioral test surface.

Combine it with the shared architecture:

- progressive disclosure;
- responsibility-first organization;
- grouping by owned knowledge/reason to change;
- nested APIs;
- explicit facades;
- public reading entrypoints;
- overview/technical documentation structure;
- traceability from abstraction to code, decisions, tests, and evidence;
- incremental compatibility migrations.

The report identifies evidence-backed opportunities, not rigid filesystem
violations. Project instructions, profiles, contracts, and approved decisions
remain authoritative.

## Terminology rules

Use the nomenclature as a preferred analytical lens, not an exclusive
vocabulary:

- `Interface` includes everything a caller must know.
- `API` may name the concrete callable surface within the broader interface.
- `Seam` identifies where behavior can vary or be substituted.
- `Boundary` remains valid for process, trust, domain, and system boundaries.
- A module may have one primary public interface plus nested internal APIs and
  child-module interfaces.
- “One adapter means hypothetical; two adapters mean real” is a heuristic, not a
  prohibition.
- Use established project domain terms rather than replacing them.

## Report contract

The report is strictly diagnostic. Each finding uses a stable `ARCH-*` ID and
contains:

- affected responsibility and files;
- observed architectural friction;
- concrete evidence and current caller/maintainer burden;
- impact on locality, leverage, navigability, testing, compatibility, or safe
  change;
- applicable project decisions and architecture constraints;
- reach and confidence;
- an improvement direction without a concrete interface or migration plan.

The report must distinguish observed structure from inferred intended ownership.
It may report evidenced friction without formal architecture documentation, but
missing purpose or ownership authority lowers confidence and becomes an
explicit planner decision.

## Missing surfaces

Inventory missing:

- responsibility overview or parent navigation;
- related technical documentation;
- public reading entrypoint;
- approved purpose or ownership contract;
- canonical architecture decision or ADR equivalent;
- relevant tests and behavioral evidence;
- compatibility and consumer documentation.

Respect the active documentation profile; do not require both overview and
technical docs for every responsibility.

Create a standalone `ARCH-*` finding only when a missing surface independently
harms navigability, safe change, or decision authority. Otherwise attach the gap
to the primary finding as evidence or documentation impact.

## Planner contract

The planner:

1. accepts a valid, fresh architecture report;
2. selects one coherent finding or inseparable finding cluster;
3. establishes callers, constraints, authority, compatibility surfaces, and
   documentation impact;
4. produces at least two materially different module/interface structures;
5. compares them by depth, locality, leverage, responsibility ownership,
   navigability, testing, and migration cost;
6. recommends one design;
7. resolves material decisions interactively;
8. produces one read-only, evidence-mapped implementation plan for
   code-workflow synthesis.

Parallel agents are optional and may be used only when the user explicitly asks
for delegation. They are never required by this specialist.

The planner must stop rather than invent responsibility boundaries, public
contracts, migration intent, or missing authority.

## Testing

Delete architecture-specific test policy from the old skill. The planner:

- uses `shared/TESTING_GUIDELINES.md` as the sole testing authority;
- plans tests through public contracts;
- preserves existing tests until replacement proof exists;
- requires explicit approval for test deletion or expectation changes;
- includes verified red/green and post-green hardening where behavior changes.

## Documentation and decisions

The report reads the documentation profile, existing overview hierarchy,
technical contracts, and approved decisions as evidence.

The planner identifies documentation impact and required decision records but
does not edit them.

After implementation approval, `grow-docs` owns:

- recording approved architecture decisions and rationale;
- updating overview hierarchy to match changed responsibilities;
- linking nested overview docs, public reading entrypoints, related code, and
  technical contracts;
- preserving one canonical source per decision.

## Compatibility

Every finding that changes a public path or interface must inventory consumers
and choose an explicit compatibility strategy.

Preserve existing entrypoints through temporary facades when practical. Order
and verify caller migration. Facade removal is a separate approved cleanup.

## Files to remove or update

- Delete `skills/improve-codebase-architecture/` only after all valuable,
  compliant material is migrated.
- Remove its public catalog entry.
- Add the internal specialist and its routing to
  `code-workflow/profiles/IMPROVEMENT.md` and
  `code-workflow/specialists/ROUTING.md`.
- Update artifact contracts for `ARCH-*` preservation without merging its reach
  or confidence into unrelated severity systems.

## Deferred glossary option

Do not copy the nomenclature into `shared/AGENTIC_GLOSSARY.md` in this phase.
At completion, explicitly remind the user that they may want to promote module,
interface, depth, seam, adapter, leverage, locality, and deletion test into the
shared glossary. If later approved, choose one canonical definition source and
link from the other; do not duplicate competing definitions.

## Gates

- No direct `improve-codebase-architecture` trigger remains.
- No hardcoded `CONTEXT.md`, `docs/adr/`, docs root, or link format is required.
- No mandatory sub-agent instruction remains.
- Report and planner responsibilities remain separate.
- The report contains no concrete interface design.
- The planner compares at least two designs.
- Testing links only to the shared testing authority.
- Documentation writes are delegated to approved implementation/grow-docs.
- Compatibility surfaces and missing documentation surfaces are explicit.
- Internal routing is selective and autorun stops before planning.
- Run template/link audits and the common gates.

## End-of-phase GCM

After all gates pass, invoke the current `give-commit-message` skill and produce
a commit message for the architecture specialist migration only. Do not commit.
Stop for the user's checkpoint before Phase 5.
