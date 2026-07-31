---
name: testable-module
description: Designs or refines a module boundary so behavior has a stable public contract and deterministic test surface without exposing private implementation details. Use when logic is tangled with framework code, effects, hidden state, or nondeterminism; when tests would otherwise require private access or excessive mocking; or when implementation needs an agreed seam before TDD.
---

# Testable Module

Create a testable module only when the current responsibility lacks a credible
behavioral seam. Treat testability as feedback about design, not a reason to
publish internals or force every operation into a pure function.

Read `.agentic/ARCHITECTURE_GUIDELINES.md` when installed, or the repository's
canonical equivalent in a shared source tree, before designing or changing the
module boundary.

## Diagnose the missing seam

Inspect callers, current public interfaces, effects, state, dependencies, and
existing tests. Prefer an existing stable boundary when it can prove behavior
credibly.

Consider a new or refined module boundary when evidence shows one or more of:

- business decisions are entangled with framework or transport wiring;
- clocks, randomness, scheduling, I/O, or global state prevent deterministic proof;
- tests would need private access, implementation-coupled mocks, or unrelated setup;
- callers coordinate knowledge that one responsibility should own.

Do not extract a module merely to shorten a file or make a private helper
directly testable.

## Establish the contract

Name the responsibility and the question its public interface answers. Record:

- the smallest sufficient inputs and complete outputs;
- effects, failures, state transitions, ordering, and lifecycle rules;
- dependencies that remain internal and capabilities that require control;
- production callers, compatibility expectations, and preserved behavior;
- representative examples and the smallest credible test surface.

Resolve material uncertainty through the project's decision workflow. Do not
invent behavior, responsibility, or compatibility intent.

## Design the seam

Choose the smallest boundary that gives production callers a coherent contract:

1. Keep framework and transport adaptation at the edge.
2. Isolate deterministic decisions where that reflects a real responsibility.
3. Inject only capabilities whose control is necessary, such as a clock or
   external service; do not turn every collaborator into a test seam.
4. Keep necessary effects explicit instead of pretending the module is pure.
5. Return plain data when it expresses the contract well, not as a universal rule.

For example, if a request handler validates input, chooses a notification, and
sends it, keep transport and delivery at the edge. Extract the choice only when
it is a coherent production responsibility with a contract callers actually use.

For a material architecture choice, compare credible alternatives and obtain
approval for the selected contract and migration plan before editing. Keep
compatibility removal separate unless explicitly approved.

## Hand off to implementation

Map approved examples, boundaries, failures, and result variants into the plan
with realistic repository-native fixtures. Then read and apply
[TDD](../tdd/SKILL.md) for seam agreement and the red-green loop. Follow the
project's canonical testing guidance for test level, dependency control,
hardening, preservation, and exceptions; do not restate those policies here.

After implementation, verify the focused contract, relevant integration wiring,
and preserved callers. Report the established interface, protected behaviors,
effects, fixtures, and any residual risk.
