# Contract and Fixtures Guidance

Use this guidance during planning when executable behavior is being introduced,
corrected, or extracted behind a clearer module boundary.

When the current responsibility has no credible behavioral seam, read
[testable-module](../../../agent-invoked/engineering/testable-module/SKILL.md)
before establishing the contract and fixtures.

## Establish the public contract

Describe the question the module answers and agree on:

- the smallest input that fully describes the question;
- the complete output, including invalid or unavailable outcomes;
- observable effects, failure behavior, state transitions, and lifecycle rules;
- the intentionally public interface and compatibility expectations.

Do not begin implementation until material contract decisions are part of the
approved synthesized plan.

## Identify realistic fixtures

Choose representative examples that exercise the approved contract and its
meaningful boundaries. Use realistic repository-native fixtures:

- inline typed data for compact value contracts;
- existing builders or local substitutes for domain and integration contracts;
- focused files such as HTML, payloads, migrations, or configuration only when
  the real boundary requires them.

Map each contract example, negative path, edge, failure mode, transition, and
result variant into the testing plan. Record fixture ownership and setup so
implementation does not invent new behavior through test data.

The shared `TESTING_GUIDELINES.md` remains the sole authority for test-first
sequencing, verified red and green phases, hardening, test preservation,
dependency control, and justified exceptions.
