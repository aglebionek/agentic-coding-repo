# JavaScript-to-TypeScript Workflow

Use for `code-workflow js-to-ts <files-or-symbols> [manual|autorun]`, primarily in `instago-app`.

## Conversion spine

1. Require explicit `.js`/`.jsx` files or symbols and resolve their imports, exports, callers, tests, runtime consumers, and effective toolchain.
2. Read and run [js-to-ts report](../js-to-ts/report/SKILL.md) as the primary evidence authority.
3. Use [js-to-ts planner](../js-to-ts/planner/SKILL.md) in manual mode or `js-to-ts autoplan` in autorun mode.
4. Preserve the report's behavior/API inventory, conversion map, classifications, baseline, and stop conditions in the work package.

Do not substitute a generic quality plan for the JS-to-TS report/planner pair.

## Conditional specialists

- Run [purpose-adherence report](../purpose-adherence/report/SKILL.md) when an approved purpose contract covers the targets and behavioral or contract choices must be checked.
- Run [bug-hunt report](../bug-hunt/report/SKILL.md) when runtime behavior, invalid outcomes, state, effects, or lifecycle semantics are unclear or risky.
- Use [testable-module](../testable-module/SKILL.md) when a sound typed contract requires extracting a pure input-to-output API. Establish and approve its API and fixtures in the synthesized plan.
- Defer unrelated code smells. Run [code-smells report](../code-smells/report/SKILL.md) only when evidenced structure directly blocks a safe atomic conversion.
- Do not run a full pre-conversion coding-standards report by default: JS-to-TS already assesses the applicable guideline dimensions. Use [coding-standards-accordance report](../coding-standards-accordance/report/SKILL.md) for an explicit standards audit or a bounded post-conversion audit.

Missing approved purpose does not automatically block a strictly mechanical, evidenced behavior-preserving conversion. It does block an ambiguous required contract refactor or product-behavior decision.

## Plan and implement

1. Limit the plan to mechanical conversion and the smallest contract refactors required for sound types. Defer unrelated cleanup.
2. Map source-to-destination paths, exports, callers, boundary validation, typed outcomes, effects, state, async contracts, tests, and minimal configuration changes.
3. Establish behavior proof before any behavior-affecting contract refactor. Mechanical type-only changes need tests only when they prove meaningful behavior.
4. Present the synthesized plan and stop for approval before renaming or editing files.
5. After approval, convert atomically and run focused type, test, lint, and build checks against the recorded baseline.
6. Apply the shared current-changes audit. Update approved-purpose documentation only when planned paths, APIs, behavior, or contracts changed.

## Completion

Report converted APIs and files, type-safety outcomes, preserved behavior, contract refactors, checks, baseline differences, deferred improvements, documentation impact, and any stop conditions reached.
