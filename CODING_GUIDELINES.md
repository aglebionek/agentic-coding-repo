# Coding Guidelines

Repo-specific rules for writing clean, readable, maintainable code in this app.

## Module Boundaries

- Keep domain decisions in small typed modules under `src/domain`; UI, native bridges, storage, and ML adapters should call into those modules instead of owning business rules.
- Preserve the existing layer direction: app code may depend on domain and infrastructure; domain code should not depend on React Native, storage, native modules, or UI components.
- Keep side effects at the edges: React hooks/components, bridge adapters, stores, notification publishers, timers, and model loading should wrap pure or narrowly stateful logic.
- Parse and validate external data at boundaries before it reaches domain logic. Storage and native bridge adapters should normalize malformed or missing data.

## Contracts And State

- Prefer explicit input and output types for module contracts, especially discriminated unions for states, decisions, and unavailable/error outcomes.
- Avoid hidden global state. If state must live across calls, keep it inside a class/controller with clear methods and observable state transitions.
- Use dependency injection for code that touches native APIs, storage, timers, detection models, or notifications so behavior can be tested with fakes.
- Make defaults and limits named constants near the module that owns them; use clamp/normalization helpers when settings can come from UI or storage.

## Readability

- Keep functions boring and direct. Split code when a condition owns a separate decision, side effect, or state transition.
- Comments should explain intent, invariants, and platform constraints, not restate the code.
- Do not add abstractions just to reduce line count. Add them when they clarify ownership, isolate a side effect, or remove meaningful duplication.
- Keep changes scoped to the behavior being changed. Avoid unrelated formatting churn and opportunistic rewrites.

## React Native Code

- React components should focus on rendering and local interaction wiring.
- Move durable state logic into hooks or controller classes when it needs tests.
- UI helpers such as labels, slider math, filters, and formatting should be extracted when they carry behavior that can regress.

## Tests

- Tests should target public module contracts: inputs, outputs, state snapshots, saved values, and calls to injected dependencies.
- New domain behavior should have focused unit tests before or alongside implementation.
- Bug fixes should add regression coverage when practical.
- Prefer hand-written fakes over broad mocking for storage, orchestration, native providers, and detection dependencies unless a framework mock is already required.
