# Architecture Planner

This is an internal code-workflow planner. Produce one read-only,
evidence-mapped architecture plan, not changes. Do not modify code, tests,
callers, documentation, snapshots, the Git index, or external state.

Read [PLAN-TEMPLATE.md](PLAN-TEMPLATE.md), [LANGUAGE.md](LANGUAGE.md),
[DEEPENING.md](DEEPENING.md), and
[INTERFACE-DESIGN.md](INTERFACE-DESIGN.md) completely before planning.

## Validate and select

1. Require a complete architecture report and identify its source.
2. Reject `Valid: false`, materially stale evidence, incompatible repository or
   target identity, and incomplete responsibility or consumer inventory.
3. Revalidate cited callers, contracts, decisions, documentation profile,
   tests, public paths, and compatibility surfaces. Record immaterial drift.
4. Select exactly one coherent `ARCH-*` finding or inseparable cluster. Give
   every report finding an explicit plan, defer, or reject disposition.
5. Establish the selected responsibility, ownership authority, constraints,
   callers, public contract, compatibility intent, and documentation impact.
   Stop rather than invent missing responsibility boundaries, public contracts,
   migration intent, or decision authority.

## Require interactive architecture design

Architecture planning is always interactive. `code-workflow improve autorun`
must stop at the first confirmed `ARCH-*` finding after the read-only report
and request manual continuation; it must not enter this planner autonomously.

In manual mode, read [grill-me](../../../interaction/grill-me/SKILL.md).
Compare at least two materially different module/interface structures under
[INTERFACE-DESIGN.md](INTERFACE-DESIGN.md). Resolve material decisions one at a
time, recommend an answer, and record the user's choice and rationale.
Parallel agents are optional and allowed only when the user explicitly requests
delegation.

## Build one plan

1. Recommend one selected design and map it to the chosen `ARCH-*` evidence.
2. State exact files and symbols, responsibility ownership, public and nested
   interfaces, hidden knowledge, seam and dependency choices, ordered caller
   migration, preservation requirements, and verification.
3. Inventory every consumer of a changed public path or interface. Choose an
   explicit compatibility strategy, prefer a temporary facade when practical,
   and make facade removal separate approved work.
4. Apply
   [`shared/TESTING_GUIDELINES.md`](../../../../shared/TESTING_GUIDELINES.md) as
   the sole testing authority. Plan proof through stable public contracts,
   preserve valid tests, and require replacement proof plus explicit approval
   before deleting tests or changing behavioral expectations. Include verified
   red/green and post-green hardening when behavior changes.
5. Identify documentation impact and decision records without editing them.
   After implementation approval, route approved decision recording and
   navigation updates through
   [grow-docs](../../../knowledge/grow-docs/SKILL.md) under the active
   documentation profile.
6. Emit one definitive implementation path for code-workflow synthesis. Treat
   new responsibility, contract, compatibility, migration, destructive,
   dependency, security, or test-expectation decisions as execution stop
   conditions requiring supplemental approval.
