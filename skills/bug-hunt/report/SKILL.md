---
name: bug-hunt-report
description: Hunts for evidenced runtime bugs, edge cases, invalid states, and uncovered correctness risks in an explicit source scope. Use only when the user invokes "bug-hunt report <file-or-directory>", "bug-hunt report codebase", or "bug-hunt report current changes".
---

# Bug Hunt Report

Produce a read-only, portable report. Do not modify source, tests, configuration, documentation, generated artifacts, snapshots, dependencies, or the Git index. Emit the report in conversation unless the user supplies a report path.

Read [REPORT-TEMPLATE.md](REPORT-TEMPLATE.md) completely before reporting.

## Establish scope

1. Require an explicit file, directory, `codebase`, or `current changes` target. Resolve `codebase` to the repository root; never guess an omitted target.
2. Read applicable `AGENTS.md` files and coding guidelines. Record the repository, revision, dirty state, exact invocation, checks, and instructions consulted.
3. Inventory every in-scope human-authored behavior-bearing artifact: source, tests, scripts, configuration, schemas, migrations, infrastructure definitions, and API contracts.
4. Exclude generated, vendored, minified, lock, build-output, and snapshot artifacts unless explicitly targeted. Return `Valid: false` for an unsupported explicit target.
5. For `current changes`, inventory staged, unstaged, and relevant untracked source changes. Inspect directly coupled unchanged context as evidence; formal findings must be introduced, exposed, or directly affected by the changes. Record unrelated pre-existing leads only as deferred rerun targets.
6. Return `Valid: false` with recommended coherent subscopes when an exhaustive pass over a broad or mixed target is not credible. Never present sampling as complete analysis.

## Hunt for bugs

Assess every scope item across:

1. inputs and boundaries: absent, malformed, extreme, duplicate, or unexpected values
2. state and transitions: impossible, ambiguous, stale, partial, initial, and terminal states
3. branches and invariants: missing combinations, wrong conditions, fallthroughs, and invalid assumptions
4. errors and recovery: swallowed failures, fallback, cleanup, retry, cancellation, and partial success
5. time and concurrency: races, ordering, idempotency, duplicate work, stale results, and timeouts
6. data integrity: conversion, mutation, persistence, precision, serialization, and migration compatibility
7. integration contracts: callers, APIs, events, configuration, permissions, and external side effects
8. lifecycle and resources: initialization, teardown, subscriptions, handles, transactions, and leaks
9. tests as evidence: risk-bearing gaps, misleading mocks, ineffective assertions, and false confidence

Trace callers, callees, types, tests, contracts, history, and configuration where they establish or refute a concrete risk. Run only the smallest useful non-destructive checks; never update fixtures or snapshots. Separate pre-existing tool failures from evidence.

## Classify evidence

- `confirmed`: a concrete execution path, contradiction, failing check, or reproducible scenario establishes incorrect behavior.
- `probable`: evidence strongly implies failure, but one named fact or safe verification step is unavailable.

Exclude weak suspicions, pure style, smells without failure risk, architecture preferences, generic coverage gaps, and purpose-adherence concerns. Include security or access-control findings only when inspected logic evidences unsafe behavior. A test defect is a finding only when it can conceal a production bug or invalidate verification.

Rate severity independently of confidence:

- `critical`: security breach, authorization bypass, data loss or corruption, or broadly catastrophic failure
- `high`: core or common behavior fails, or impact has broad reach
- `medium`: bounded or uncommon incorrect behavior with meaningful impact or a workaround
- `low`: narrow correctness failure with minor operational impact

Every finding must identify the violated invariant, trigger, execution path, observable impact, evidence, counterevidence, and smallest correction direction without becoming an implementation plan.

## Set validity

Use `Valid: true` only when the complete inventory and every audit category received meaningful analysis. Narrow, recorded `not verifiable` results are allowed when they do not prevent a coherent overall assessment. Findings do not affect validity.

Use `Valid: false` when ambiguous intent, missing access, unavailable dependencies, incoherent or excessive scope, incomplete inventory, or major evidence gaps make the hunt materially incomplete. Provide reliable evidence, exact recovery steps and questions with recommendations, useful locations, rerun conditions, and the next invocation. Do not include a speculative plan.
