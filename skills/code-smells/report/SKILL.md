---
name: code-smells-report
description: Identifies and consolidates evidence of Martin Fowler's Refactoring, 2nd Edition code smells in an explicit source target. Use only when the user invokes "code-smells report <file-or-directory>" or "code-smells report codebase".
---

# Code Smells Report

Produce a read-only, portable report. Do not modify source, tests, configuration, documentation, generated artifacts, snapshots, or the Git index. Emit the report in conversation unless the user supplies a report path.

Read [CATALOG.md](CATALOG.md) and [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md) completely before reporting. Use only the catalog's canonical smells; do not broaden the audit into bugs, vulnerabilities, style preferences, or general architecture review.

## Establish scope

1. Require `code-smells report <file-or-directory>` or `code-smells report codebase`. Resolve `codebase` to the current repository root; never guess an omitted target.
2. Read applicable `AGENTS.md` files and coding guidelines. Record the repository root, revision, dirty state, requested target, checks run, and instructions consulted.
3. Inventory every in-scope human-authored executable source file before analysis.
4. Exclude configuration, markup, generated, vendored, minified, build, lock, and snapshot artifacts unless explicitly targeted. Return `Valid: false` when the explicit target is not human-authored executable source.
5. For mixed or impractically broad targets, return `Valid: false` with recommended coherent subscopes when a meaningful catalog-wide pass is not possible.

## Analyze smells

1. Assess all 24 catalog entries against the complete inventory. Inspect callers, collaborators, history, and tests only where they materially establish or refute a smell.
2. Judge structure in context. A metric or pattern is a search lead, never proof; apply the catalog's evidence requirement and false-positive check.
3. Consolidate occurrences caused by one design problem into one finding. Record representative locations and the known affected-file or occurrence count; do not merge independent causes merely because they share a smell name.
4. Mark confidence `confirmed` when direct contextual evidence establishes the smell and its maintenance effect. Mark it `probable` when evidence is strong but a stated missing inspection prevents confirmation.
5. Describe reach as `local`, `multi-file`, or `cross-cutting`. Describe the concrete maintenance effect—such as duplicated change effort, comprehension burden, scattered responsibility, or test friction—without severity labels.
6. Cite exact paths and symbols or lines, explain why the canonical criteria apply, record counterevidence considered, and distinguish pre-existing tool failures from evidence.
7. Run only the smallest useful non-mutating checks. Never update fixtures or snapshots.

## Set validity

Use `Valid: true` only when the target resolves, applicable instructions were read, exclusions and the full source inventory are recorded, and every catalog entry received a meaningful evidence pass. Findings, probable findings, and absent smells do not affect validity.

Use `Valid: false` for missing or ambiguous targets, unreadable or unsupported source, incoherent scope, incomplete inventory, or incomplete catalog coverage. Provide reliable evidence, exact recovery steps and questions with recommendations, useful locations, rerun conditions, and the next invocation. Do not include a speculative refactoring plan.
