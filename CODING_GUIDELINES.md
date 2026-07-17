# Coding Guidelines

These guidelines describe how to design readable, testable JavaScript and
TypeScript. Treat them as defaults unless a concrete constraint justifies a
different design.

## Every Unit Is An API

A module is any unit of code that can be described by a contract: a function,
class, file, helper, or service. Every module should answer one clear question
through defined inputs, outputs, behavior, and effects.

- Give each module the smallest input that fully describes its question.
- Return an output that fully describes the answer. Prefer plain typed data over
  hidden mutation or control flow.
- Make invalid and unavailable outcomes visible in the contract.
- Keep the intentionally exported surface small. Exported symbols are stable
  contracts; internal helpers remain replaceable implementation details.
- Name parameters after their role in the module contract, especially when two
  values share the same primitive type or structure. Prefer names that explain
  why each value exists in the decision.
- Do not bypass private boundaries in tests. If an internal helper contains
  behavior worth testing directly, promote it to a module with its own explicit
  API.
- Prefer explicit input and output types at module boundaries, even when TypeScript
  could infer them.

Prefer a contract that states the question directly:

```ts
type PriceInput = {
  subtotal: number;
  discountPercent: number;
};

type PriceResult = {
  total: number;
  discountApplied: number;
};

export function calculatePrice(input: PriceInput): PriceResult {
  const discountRate = Math.min(Math.max(input.discountPercent, 0), 100) / 100;
  const discountApplied = input.subtotal * discountRate;

  return {
    total: input.subtotal - discountApplied,
    discountApplied,
  };
}
```

Prefer parameter names that distinguish domain roles:

```ts
findDuplicateWikiEntryName({
  candidateTitles,
  existingEntryNames,
});
```

Avoid names that only repeat raw shapes:

```ts
findDuplicateWikiEntryName({
  titles,
  existingNames,
});
```

Avoid APIs whose real inputs or outputs are implicit:

```ts
let currentDiscount = 0;

export function updatePrice(order: Order): void {
  order.total *= 1 - currentDiscount;
}
```

## Functional Core And Effectful Boundaries

- Put decisions, transformations, validation, filtering, and calculations in pure
  functions whenever practical.
- Pure decision APIs receive all required data as arguments and return plain data.
  They do not read global state, mutate their inputs, perform I/O, or return UI
  elements.
- Keep storage, network access, clocks, randomness, timers, notifications, and
  framework APIs at explicit effect boundaries.
- An effectful API may return a promise or own a lifecycle, but its effects must be
  part of its contract.
- Inject external capabilities so the module can be tested with deterministic
  fakes.
- Do not hide a business decision inside an adapter or callback when it can be
  represented as an input-to-output function.

Prefer separating the decision from its effect:

```ts
type ReminderDecision =
  | { kind: "skip" }
  | { kind: "send"; message: string };

export function decideReminder(input: ReminderInput): ReminderDecision {
  return input.isDue
    ? { kind: "send", message: `Review ${input.title}` }
    : { kind: "skip" };
}

export async function publishReminder(
  decision: ReminderDecision,
  notifications: NotificationPublisher,
): Promise<void> {
  if (decision.kind === "send") {
    await notifications.publish(decision.message);
  }
}
```

## Boundaries And Dependencies

- High-level policy should not depend on UI frameworks, persistence formats,
  native bridges, or vendor SDKs.
- Wrap external systems in narrow adapters that expose application-shaped types.
- Parse and validate untrusted data at the boundary. Use `unknown` until data has
  been checked; do not spread `any` into trusted code.
- Normalize missing, malformed, or legacy values once at the boundary instead of
  scattering defensive checks through decision logic.
- Dependencies should point toward stable policy. Pass volatile capabilities into
  the modules that use them.
- Avoid hidden singleton and global state. A caller should be able to identify a
  module's dependencies from its API.
- Read environment variables through the application's centralized configuration
  module. Use required environment access for configuration necessary to provide
  valid application behavior. Use optional environment access only when absence is
  an intentional operational state represented by the consuming API. Domain
  utilities must not read `process.env` or environment adapters directly.
- Keep defaults, limits, and normalization rules near the module that owns the
  corresponding contract.

## Results And Errors

- Model expected operational outcomes as typed results. Examples include missing
  input, denied permission, unavailable data, validation failure, and a rejected
  external operation.
- Use discriminated unions when callers must handle distinct outcomes.
- When a discriminated union represents meaningful domain states, use an exported
  string enum for the discriminant values. Producers and callers must reference
  enum members instead of repeating raw string literals, so the valid state set is
  discoverable and cannot drift across modules.
- When a union represents meaningful domain states, define every member as a
  separate, uniquely named type that explains the state's meaning, then compose
  the final result type from those named states. Keep trivial mechanical unions
  inline when naming them would not add domain meaning.
- Design result unions around outcomes callers must distinguish, not around every
  literal combination produced by the current implementation. Keep shared factual
  fields broad unless their exact correlation is part of the public contract. When
  one field exists only for a particular outcome, discriminate on that outcome and
  require the field only in that variant.
- Throw only for violated invariants or failures that cannot be handled meaningfully
  at the current boundary.
- Do not use `null`, magic strings, or swallowed exceptions to represent multiple
  distinct outcomes.
- Before propagating an error, a stateful module must restore or preserve a valid,
  documented state.

Prefer an exhaustive result contract:

```ts
export enum LoadSettingsResultKind {
  Loaded = "loaded",
  Missing = "missing",
  Invalid = "invalid",
}

type LoadSettingsLoaded = {
  kind: LoadSettingsResultKind.Loaded;
  settings: Settings;
};

type LoadSettingsMissing = {
  kind: LoadSettingsResultKind.Missing;
};

type LoadSettingsInvalid = {
  kind: LoadSettingsResultKind.Invalid;
  issues: string[];
};

type LoadSettingsResult =
  | LoadSettingsLoaded
  | LoadSettingsMissing
  | LoadSettingsInvalid;

function describeResult(result: LoadSettingsResult): string {
  switch (result.kind) {
    case LoadSettingsResultKind.Loaded:
      return "Settings loaded";
    case LoadSettingsResultKind.Missing:
      return "No settings found";
    case LoadSettingsResultKind.Invalid:
      return result.issues.join(", ");
  }
}
```

Prefer variants that express outcome-specific data without mirroring every branch:

```ts
type AccessResult =
  | {
      mode: EditorAccessMode.Current | EditorAccessMode.Blocked;
      redirectUrl?: never;
    }
  | {
      mode: EditorAccessMode.Legacy;
      redirectUrl: string;
    };
```

## State And Classes

- Default to pure functions and plain data.
- Use a class or another stateful abstraction only when a unit must keep mutable
  state coherent across calls or own a lifecycle, subscription, timer, or resource.
- Keep state private and expose narrow commands and immutable snapshots.
- Define valid state transitions as part of the API. Callers should not need to
  coordinate internal fields in a particular order.
- Inject effects through the constructor or factory rather than importing mutable
  dependencies directly.
- Keep optimistic updates reversible. If persistence or another required effect
  fails, restore a consistent state before reporting the failure.
- Do not introduce a stateful abstraction merely to group related functions.

## Async Work And Lifecycles

- Define whether asynchronous calls may overlap, queue, replace one another, or be
  rejected. Do not leave concurrency behavior accidental.
- Prevent stale asynchronous results from overwriting newer state.
- Give every timer, subscription, listener, and debounced task a clear owner and a
  cleanup path.
- Make lifecycle operations such as `start`, `stop`, and `dispose` safe to call in
  every documented state. Prefer idempotence when repeated calls have no useful
  meaning.
- Specify when state becomes observable relative to awaited effects.
- Keep time and scheduling injectable when behavior depends on them.

## UI And State Management

- UI components should focus on rendering and local interaction wiring.
- Keep durable state transitions, asynchronous workflows, and recoverable effects
  in a testable controller, state module, or hook with an explicit API.
- Extract labels, formatting, filters, ranges, and other UI decisions into pure
  functions when their behavior can regress.
- A pure decision module should return data describing what the UI needs, not a UI
  component.
- Keep transient presentation state local when no other module needs to observe or
  coordinate it.

## Readability

- Keep functions direct. Split code when a condition represents a separate
  decision, effect, or state transition with its own contract.
- Name modules and functions after the question they answer or the operation they
  perform.
- Prefer exhaustive branching over boolean combinations when states have distinct
  meanings.
- Comments should explain intent, invariants, and constraints, not restate the code.
- Use string enums for closed, named domain vocabularies that require both a runtime
  value and an exported type. Prefer an enum over an exported constant object when
  consumers conceptually use the values as one domain type. Continue using
  `as const` for local lookup tables, configuration maps, and values that are not a
  domain vocabulary.
- Add an abstraction when it clarifies ownership, isolates an effect, establishes a
  useful contract, or removes meaningful duplication. Do not add one only to reduce
  line count.
- Keep changes scoped to the behavior being changed. Avoid unrelated formatting
  churn and opportunistic rewrites.

## Tests

- Agree on the API contract before implementation: the question being answered,
  minimal input, complete output, expected effects, and failure behavior.
- For new behavior, bug fixes, and extracted logic, write tests against the agreed
  contract before implementing it.
- Mechanical wiring, type-only changes, and presentation-only changes do not need a
  unit test unless a test would validate meaningful behavior.
- Test public behavior through inputs, outputs, state snapshots, saved values, and
  calls to injected dependencies. Do not mirror implementation steps in assertions.
- Cover the main case, meaningful edge cases, and every result variant that callers
  must handle.
- Add a regression test for a bug before fixing it when the behavior can be expressed
  through a stable API.
- Prefer hand-written fakes for application dependencies. Use framework mocks only
  where the framework itself is the boundary under test.
- Keep tests deterministic by injecting time, randomness, scheduling, and external
  capabilities.
- If a test requires reaching into private state, reconsider the public contract or
  extract the behavior into a separate testable module.
