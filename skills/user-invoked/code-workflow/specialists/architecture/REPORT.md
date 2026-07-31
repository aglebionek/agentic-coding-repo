# Architecture Report

This is an internal code-workflow specialist. Produce a read-only, portable
diagnostic report for a selectively routed `code-workflow improve` target. Do
not modify code, tests, documentation, snapshots, the Git index, or external
state. Do not design a concrete interface or migration plan.

Read [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md), [LANGUAGE.md](LANGUAGE.md), and
[DEEPENING.md](DEEPENING.md) completely before reporting.

## Establish scope and authority

1. Record repository, revision, dirty state, target, applicable instructions,
   checks, exclusions, and coverage limits.
2. Read the shared architecture guideline, the active documentation profile,
   applicable approved decisions and contracts, and established domain
   language. Discover locations from project instructions and navigation; do
   not require a particular documentation root, decision format, or link style.
3. Inventory the target responsibility, its implementation files, public and
   nested interfaces, callers, tests, configuration, related documentation,
   history when useful, and compatibility consumers.
4. Separate observed structure from inferred intended ownership. Missing or
   ambiguous purpose and ownership authority lowers confidence and becomes an
   explicit planning constraint; return `Valid: false` only when it prevents a
   coherent diagnostic inventory.
5. Narrow a broad or mixed target to coherent responsibility groups, or return
   a recovery handoff when credible coverage is impractical.

## Diagnose architectural friction

Use [LANGUAGE.md](LANGUAGE.md) as a preferred lens, not a filesystem linter.
Trace concrete maintainer and caller burden involving:

- fragmented responsibility or knowledge spread across coupled modules;
- shallow pass-through layers and low-leverage interfaces;
- leaked ordering, state, error recovery, configuration, or vendor mechanics;
- misplaced or hypothetical seams and adapters;
- poor locality, navigability, or public reading entrypoints;
- test friction caused by an unstable or overly exposed behavioral surface;
- compatibility risk from unclear consumers or public paths.

For missing surfaces, inventory responsibility or parent navigation, related
technical documentation, a public reading entrypoint, approved purpose or
ownership authority, canonical decision records, relevant tests and behavioral
evidence, and compatibility or consumer documentation. Create a standalone
finding only when the absence independently harms navigability, safe change, or
decision authority; otherwise attach it to the primary finding.

Each finding uses a stable `ARCH-*` identifier and records the affected
responsibility and files, observed friction, concrete evidence, caller and
maintainer burden, impact, applicable constraints, reach, confidence, missing
surfaces, and an improvement direction. The direction may name knowledge that
should become local or a responsibility that needs a clearer facade, but must
not specify methods, types, parameters, file moves, adapter shapes, or an
ordered migration.

Exclude generic bugs, catalog smells, coding-style deviations, and unsupported
architectural preferences. Record neighboring concerns as out-of-scope routing
suggestions.

## Set validity

Use `Valid: true` when the inventory credibly supports a coherent diagnostic
judgment, including a report with no findings. Findings do not make a report
invalid.

Use `Valid: false` when repository identity, scope, evidence access, or missing
authority prevents a coherent report. Provide a self-contained recovery
handoff, exact inspection locations, rerun conditions, and the
`code-workflow improve` target to resume. Never include a speculative design.
