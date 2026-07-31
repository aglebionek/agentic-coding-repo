# Phase 2: Establish shared testing guidelines

## Problem

Test-first behavior currently exists in the JavaScript/TypeScript coding
guidelines, the standalone `testable-module` skill, workflow fragments, and a
research note. There is no project-agnostic canonical testing authority.

## Approach

Create `shared/TESTING_GUIDELINES.md` as the language-agnostic testing
authority. Make other guidance link to it rather than duplicating its normative
rules.

Do not retire `testable-module` in this phase. Phase 3 internalizes its remaining
workflow-specific value after the shared authority exists.

## Required testing contract

### Contract before code

- Establish the behavior, public contract, effects, failure behavior, and
  meaningful examples before implementation.
- For new executable behavior, bug fixes, and extracted logic, write the
  smallest credible behavioral test first.

### Verified red phase

- Run the new test before implementation whenever technically feasible.
- Confirm it fails because the intended behavior is absent, not because of
  syntax, imports, invalid fixtures, environment failure, or an unrelated error.
- If a test cannot run until minimal scaffolding exists, document the exception
  and add only the minimum scaffolding needed to obtain a meaningful red result.

### First green pass

- Implement the minimum coherent behavior that satisfies the approved contract.
- Run the focused test and reach green.
- Do not weaken the test to match an incorrect implementation.

### Hardening pass

After the first green pass:

- add useful unit tests;
- strengthen boundary-level or contract tests;
- cover negative paths, edge cases, failure modes, transitions, and result
  variants;
- rerun the implementation against the expanded suite;
- refactor without changing behavior and rerun focused and relevant broader
  checks.

Do not add tests merely to increase line coverage. Every test must protect a
meaningful contract, risk, boundary, or regression.

If hardening exposes an edge case already implied by the approved contract, the
implementation may be corrected within that plan. New behavior or contract
expansion requires supplemental approval.

### Test level

- Use the smallest stable test surface that credibly proves the behavior.
- Do not mandate unit tests universally.
- Use integration, contract, migration, type-level, end-to-end, or focused
  reproduction tests when they prove the real boundary more directly.
- Numeric coverage thresholds remain project-owned.

### Test preservation

- Existing valid tests are contract evidence.
- Deleting a valid test or changing its behavioral expectations requires
  explicit approval.
- Approved mechanical moves, renames, deduplication, or framework migration may
  proceed only when assertion meaning remains unchanged.
- Replacement tests must demonstrate equivalent or stronger coverage before old
  tests are removed.

### Dependencies and determinism

- Test through public contracts.
- Prefer real local substitutes or hand-written fakes over framework mocks.
- Mock true external or framework boundaries when necessary.
- Inject clocks, randomness, scheduling, filesystem, network, and similar
  capabilities when deterministic tests require control.

### Exceptions

Mechanical wiring, type-only changes, configuration-only changes, and
presentation-only changes do not require tests unless a test would prove
meaningful behavior.

When meaningful automated testing is not technically reasonable, the approved
plan must:

- explain the technical reason;
- name a repeatable alternate proof;
- identify the residual regression risk.

“Too difficult” is not sufficient.

## Files to create or modify

- Create `shared/TESTING_GUIDELINES.md`.
- Update `shared/BASE_AGENT_GUIDELINES.md` to route agents to the testing
  guideline for executable behavior changes.
- Update `shared/CODING_GUIDELINES.md` so its Tests section points to the shared
  testing authority and retains only genuinely JavaScript/TypeScript-specific
  additions.
- Keep root `CODING_GUIDELINES.md` as the existing compatibility pointer.
- Update root `AGENTS.md` model resources.
- Update `README.md` source tree, installed tree, opt-in snippet, and ownership
  explanation.
- Update `fetch-agent-assets.sh` so `.agentic/TESTING_GUIDELINES.md` is required,
  installed, and printed.
- Update `skills/user-invoked/code-workflow/SKILL.md` setup so every profile reads the testing
  guideline when executable behavior may change.
- Update code-workflow quality/artifact references only as needed to point to the
  canonical testing authority without yet moving files.

## Architecture and documentation constraints

- Testing guidance is its own deep shared module, not an overloaded architecture
  subsection.
- Do not duplicate the full testing contract in coding guidelines or skills.
- Technical documentation may link to tests and evidence; it does not become the
  canonical testing policy.
- Research in `notes/AI/Key Ideas/Testing.md` remains supporting material, not
  operational authority.

## Installer gates

Run:

```bash
bash -n fetch-agent-assets.sh
```

Run the installer twice against a disposable target containing byte-hashed
sentinels:

- `AGENTS.md`;
- `CODING_GUIDELINES.md`;
- `GLOSSARY.md`;
- `skills/local-only/SKILL.md`;
- arbitrary documentation.

Verify:

- every sentinel remains byte-identical;
- `.agentic/TESTING_GUIDELINES.md` exists and matches the source;
- every other managed asset remains present;
- the second run is idempotent;
- a stale managed file is removed;
- a source missing `TESTING_GUIDELINES.md` fails clearly before replacing the
  managed directory.

## Content gates

- Search for competing normative TDD/test-first definitions.
- Confirm the coding guideline points to the shared testing guideline.
- Confirm code-workflow reads it across all profiles that change executable
  behavior.
- Confirm exceptions are explicit rather than implied.
- Run the common gates from the ordered handoff.

## End-of-phase GCM

After all gates pass, invoke `give-commit-message` and produce a commit message
for the shared testing authority only. Do not commit. Stop for the user's
checkpoint before Phase 3.
