# JavaScript-to-TypeScript Autoscope Workflow

Use for `code-workflow js-to-ts-autoscope <seed-file-or-symbol> [deep|wide] [manual|autorun]`.

Default scope mode to `deep`. Default workflow mode to `manual`.

## Conversion spine discovery

1. Require an explicit JS/JSX seed file, symbol with discoverable file, or small coherent seed set accepted by the autoscope report skill.
2. Read the [specialist routing table](../specialists/ROUTING.md), then run the
   internal [autoscope report](../specialists/js-to-ts-autoscope/REPORT.md) as
   the scope-discovery and evidence authority.
3. Use its [planner](../specialists/js-to-ts-autoscope/PLANNER.md) in the
   workflow's `manual` or `autorun` mode.
4. Preserve the report's seed, scope mode, selected spine invariant, file roles, editable boundary, inspect-only context, exclusions, findings, verification baseline, and stop conditions in the work package.

Do not substitute a generic JS-to-TS report for the autoscope report/planner pair. Do not expand beyond the selected spine during implementation.

## Conditional specialists

- Run [purpose adherence](../specialists/purpose-adherence/REPORT.md) when an approved purpose contract covers the selected spine and behavioral or contract choices must be checked.
- Run [bug hunt](../specialists/bug-hunt/REPORT.md) when runtime behavior, invalid outcomes, state, effects, or lifecycle semantics are unclear or risky within the selected spine.
- Use [contract and fixtures guidance](../guidance/CONTRACT-AND-FIXTURES.md) when a sound typed contract requires extracting a clearer public interface. Establish and approve its contract and fixtures in the synthesized plan.
- Defer unrelated code smells. Run [code smells](../specialists/code-smells/REPORT.md) only when evidenced structure directly blocks the selected spine conversion.
- Do not run a full pre-conversion standards report by default: autoscope already assesses the applicable guideline dimensions. Use [coding standards accordance](../specialists/coding-standards-accordance/REPORT.md) for an explicit standards audit or a bounded post-conversion audit.

Missing approved purpose does not automatically block a strictly mechanical, evidenced behavior-preserving conversion. It does block an ambiguous required contract refactor, product-behavior decision, or expansion beyond the selected spine.

## Plan and implement

1. Limit the plan to the selected autoscope spine, mechanical conversion, and the smallest contract refactors required for sound types. Defer unrelated cleanup.
2. For `deep`, preserve the narrow behavior path and avoid broad caller or sibling-feature edits unless the autoscope plan marks them directly required.
3. For `wide`, type the stable exported boundary and minimize caller churn unless caller edits are required for type soundness.
4. Map source-to-destination paths, exports, callers, boundary validation, typed outcomes, effects, state, async contracts, tests, and minimal configuration changes.
5. Apply the shared testing guideline and establish credible behavior or
   type-level proof for each contract refactor.
6. Present the synthesized plan and stop for approval before renaming or editing files.
7. After approval, convert according to the planner's `oneshot` or `sequenced` execution shape and run focused type, test, lint, and build checks against the recorded baseline.
8. Apply the shared current-changes audit. Update approved-purpose documentation only when planned paths, APIs, behavior, or contracts changed.

## Completion

Report the seed, scope mode, selected spine invariant, converted APIs and files, type-safety outcomes, preserved behavior, contract refactors, checks, baseline differences, deferred improvements, documentation impact, and any stop conditions reached.
