# Codebase Improvement Workflow

Use for `code-workflow improve <file-or-directory> [manual|autorun]`.

## Establish a work package

1. Inventory the requested target and its directly coupled behavior-bearing artifacts.
2. Reject an exhaustive claim over a scope too broad or mixed for every selected specialist. Recommend one coherent subsystem, concept, change boundary, or sequence of narrow reruns.
3. Identify the maintenance or quality outcome sought. If the user supplied no focus, inspect read-only evidence and recommend the narrowest high-leverage starting scope.
4. Establish applicable approved purpose before proposing behavioral change or new concept documentation.

Autorun may select a narrow safe scope, but must stop rather than guess between materially different product, architecture, or ownership priorities.

## Route specialists

Use the [specialist routing table](../specialists/ROUTING.md) and select reports
independently from evidence:

- [Bug hunt](../specialists/bug-hunt/REPORT.md) for runtime correctness and uncovered invalid states
- [Code smells](../specialists/code-smells/REPORT.md) for demonstrated Fowler catalog maintenance effects
- [Coding standards accordance](../specialists/coding-standards-accordance/REPORT.md) for JS/TS deviations from `CODING_GUIDELINES.md`
- [Purpose adherence](../specialists/purpose-adherence/REPORT.md) for code and contract surfaces covered by approved purpose

Use [grow-docs](../../grow-docs/SKILL.md) when documentation is the requested outcome or approved implementation changes make existing notes incomplete. Grow-docs is not a purpose-discovery mechanism.

Use each selected report's matching internal planner in `manual` or `autorun`
mode. A forced code-smell boundary crossing requires explicit user approval;
general autorun never implies it.

## Consolidate and plan

1. Keep report scopes coherent and findings attributable. Do not relabel bugs as smells, standards violations as purpose mismatches, or documentation gaps as implementation defects.
2. Resolve overlapping actions once while retaining mappings and dispositions for every specialist ID.
3. Order work by prerequisite: purpose and contract contradictions, correctness, standards needed for safe change, then maintainability improvements and documentation.
4. Use [contract and fixtures guidance](../guidance/CONTRACT-AND-FIXTURES.md)
   when evidence supports extracting a clear public contract. Establish and
   approve the contract and realistic fixtures in the synthesized plan.
5. Prefer one bounded improvement slice that can be verified independently. Defer unrelated findings with their recommended next invocation.
6. Present the synthesized plan and stop for approval before editing.

## Implement and complete

After approval, execute the bounded slice, run finding-level structural and behavioral proof, and apply the shared validation and documentation gates. Report improvements achieved, preserved behavior, every finding disposition, remaining gaps, and the recommended next coherent slice.
