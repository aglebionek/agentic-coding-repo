# JS to TS Report

This is an internal code-workflow specialist. Produce a read-only, portable
report for the targets selected by the active profile. Do not modify code,
types, tests, configuration, snapshots, generated artifacts, or the Git index.
Emit it in conversation unless the work package supplies a report path.

Read [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md) completely before reporting.

## Establish scope

1. Read the applicable `AGENTS.md` files and root `CODING_GUIDELINES.md`.
2. Record the repository root, revision, dirty state, user-supplied `.js` or `.jsx` targets, and checks run.
3. Include imports, exports, callers, tests, configuration, build tooling, and runtime consumers only where needed for an atomic conversion.
4. Identify generated, vendored, public-contract, cross-package, or deployment-sensitive boundaries; never treat generated or vendored files as editable targets.
5. Inspect the effective TypeScript, module, package, lint, test, and build configuration. Determine `.ts` versus `.tsx` destinations and the repository's actual verification commands.

## Analyze conversion

1. Describe each target's observable behavior, inputs, outputs, effects, failures, exports, dependencies, state, async semantics, and lifecycle ownership.
2. Trace values across trust boundaries. Require `unknown` until validation; flag unsupported assertions, implicit `any`, unsafe narrowing, and types that hide invalid or unavailable outcomes.
3. Assess the applicable coding-guideline dimensions: explicit APIs, functional core and effects, dependency direction, results and errors, state, async work, UI boundaries, readability, and tests.
4. Classify every proposed need as:
   - `mechanical`: rename, syntax, import, or configuration work that preserves behavior
   - `required contract refactor`: the smallest change needed for a sound typed API, such as replacing an implicit sentinel with a discriminated result
   - `deferred improvement`: unrelated cleanup or architectural work
5. For each confirmed finding, record the concrete scenario, runtime or type-safety impact, evidence locations, classification, and required outcome. Do not invent an implementation plan.
6. Establish a non-mutating baseline with the smallest useful type, test, lint, and build checks. Separate pre-existing failures and use `not verifiable` when safe proof is unavailable.

## Set validity

Use `Valid: true` when the conversion scope is coherent and behavior, dependencies, tooling, and contracts are sufficiently evidenced for safe planning. Findings and guideline violations do not make the report invalid.

Use `Valid: false` for missing or ambiguous targets, generated or vendored scope, unresolved effective configuration, inaccessible required dependencies, materially untraceable behavior, or another prerequisite that prevents reliable planning. Provide exact blockers, recommended resolutions, repository locations, rerun conditions, and the next invocation. Never include a speculative plan.
