# Testing Guidelines

These guidelines are the canonical project-agnostic testing authority for
shared agent workflows. Treat them as defaults unless a project's approved
instructions or contracts require a stricter standard.

## Establish the contract before code

Before implementing executable behavior, establish:

- the public behavior and contract;
- inputs, outputs, effects, and meaningful failure behavior;
- representative examples and important boundaries;
- the smallest stable test surface that can credibly prove the behavior.

For new executable behavior, bug fixes, and extracted logic, write the smallest
credible behavioral test before implementation.

## Verify the red phase

Run the new test before implementation whenever technically feasible. Confirm
that it fails because the intended behavior is absent, not because of a syntax
error, broken import, invalid fixture, environment failure, or unrelated
problem.

If the test cannot run until minimal scaffolding exists, document the exception
and add only the scaffolding required to obtain a meaningful red result.

## Reach the first green pass

Implement the minimum coherent behavior that satisfies the approved contract.
Run the focused test and reach green. Do not weaken a correct test to match an
incorrect implementation.

## Harden after green

After the first green pass:

- add useful unit tests where they protect stable behavior;
- strengthen boundary-level or contract tests;
- cover meaningful negative paths, edge cases, failure modes, transitions, and
  result variants;
- rerun the implementation against the expanded suite;
- refactor without changing behavior, then rerun focused and relevant broader
  checks.

Do not add tests merely to increase line coverage. Every test must protect a
meaningful contract, risk, boundary, or regression.

If hardening exposes an edge case already implied by the approved contract,
correct the implementation within that plan. New behavior or contract expansion
requires supplemental approval.

## Choose the credible test level

Use the smallest stable test surface that credibly proves the behavior. Do not
mandate unit tests universally.

Use integration, contract, migration, type-level, end-to-end, or focused
reproduction tests when they prove the real boundary more directly. Numeric
coverage thresholds remain project-owned.

## Preserve contract evidence

Existing valid tests are contract evidence. Deleting a valid test or changing
its behavioral expectations requires explicit approval.

Approved mechanical moves, renames, deduplication, or framework migrations may
proceed only when assertion meaning remains unchanged. Replacement tests must
demonstrate equivalent or stronger coverage before old tests are removed.

## Control dependencies and nondeterminism

- Test through public contracts.
- Prefer real local substitutes or hand-written fakes over framework mocks.
- Mock true external or framework boundaries when necessary.
- Inject clocks, randomness, scheduling, filesystem, network, and similar
  capabilities when deterministic tests require control.

## Exceptions and alternate proof

Mechanical wiring, type-only changes, configuration-only changes, and
presentation-only changes do not require tests unless a test would prove
meaningful behavior.

When meaningful automated testing is not technically reasonable, the approved
plan must:

- explain the technical reason;
- name a repeatable alternate proof;
- identify the residual regression risk.

“Too difficult” is not a sufficient reason.
