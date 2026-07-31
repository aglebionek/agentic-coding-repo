# JS to TS Autoscope Report

This is an internal code-workflow specialist. Produce a read-only, portable
report for the seed selected by the active profile. Do not modify source, tests,
configuration, documentation, generated artifacts, snapshots, dependencies, or
the Git index. Emit it in conversation unless the work package supplies a
report path.

Read [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md) completely before reporting.

## Establish Scope

1. Require an explicit JS/JSX seed file, symbol with discoverable file, or small coherent seed set. Default missing mode to `deep`; require explicit `wide`.
2. Reject `current changes`, `codebase`, broad project or package directories,
   generated/vendor/static/template-only targets, and unsupported files with
   `Valid: false`.
3. For invalid broad targets, use cheap static heuristics and minimal spot checks to suggest concrete seed reruns; do not build a speculative spine.
4. In `deep`, allow up to 3 adjacent seed files already in one obvious codepath. In `wide`, allow exactly 1 primary hub seed, plus at most 1 named local helper.
5. Read applicable `AGENTS.md`, root `CODING_GUIDELINES.md`, package/tooling
   configuration, and the internal JavaScript-to-TypeScript specialist only as
   compatibility context.
6. Record repository root, revision, dirty state, invocation, mode, seed, instructions consulted, discovery commands, and checks run.

## Select One Spine

1. Produce exactly one conversion spine for the requested mode. Do not produce rankings or near-miss lists unless the report is invalid and suggests rerun seeds.
2. `deep`: select a narrow, behavior-coherent path with one main responsibility. Prefer the smallest logically complete traversal; 2-4 production files is typical.
3. `wide`: select one high-fanout module whose exported API can be typed behind a stable boundary while keeping caller edits minimal.
4. Assess value by codepath coherence, contained traversal, dependency or boundary value, guideline relevance, and mode fit. Do not use existing test presence to prefer or reject a spine.
5. Inspect route/API, middleware, cron, webhook, event, validation, service, and config wiring when it proves value or purpose. Do not make broad registries editable by default.
6. Stop expansion at broad fan-out, sibling features, route registries, app/server bootstraps, barrels, generated/vendor/static/template surfaces, and public-contract boundaries unless inclusion is critical to type soundness.

## Analyze The Spine

1. Name one spine invariant. Mark `Valid: false` if no coherent behavior or stable wide hub contract can be identified.
2. Classify files as `seed`, `core`, `callee`, `caller`, `boundary`, `type-support`, `test-support`, or `inspect-only`, and as `editable`, `inspect-only`, or `excluded`.
3. Trace current inputs, outputs, effects, errors, async/lifecycle behavior, trust boundaries, imports, exports, direct callers, direct callees, and runtime consumers.
4. Assess relevant `CODING_GUIDELINES.md` dimensions lightly for the selected spine: explicit APIs, effects, boundaries, results/errors, state/async, readability, and tests.
5. Preserve evidenced intended behavior and compatibility constraints. Do not preserve accidental API weaknesses when a bounded, approved, guideline-aligned contract refactor is required for honest TypeScript.
6. Identify mechanical conversion needs, required guideline-aligned contract refactors, verification gaps, and stop conditions. Keep full coding-standards audits as optional follow-ups.

## Set Validity

Use `Valid: true` when the seed, mode, tooling, spine invariant, file roles, traversal boundary, purpose evidence, guideline assessment, and verification readiness are sufficiently evidenced for planning.

Use `Valid: false` for missing or excessive seed scope, unsupported/generated/vendor/static/template targets, unresolved tooling, materially untraceable purpose, incoherent deep path, unstable wide hub contract, required generated/vendor edits, inaccessible dependencies, or another blocker. Provide exact recovery steps, suggested seeds when useful, rerun conditions, and the next invocation. Never include a speculative plan.
