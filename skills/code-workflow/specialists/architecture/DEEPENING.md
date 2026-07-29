# Architecture Deepening

Read [LANGUAGE.md](LANGUAGE.md) and the shared
[`ARCHITECTURE_GUIDELINES.md`](../../../../shared/ARCHITECTURE_GUIDELINES.md)
before applying this guidance.

## Diagnose depth

Assess whether a responsibility's current structure gives callers leverage and
maintainers locality:

- trace the knowledge callers must coordinate across modules;
- identify ordering, error recovery, state, configuration, or vendor mechanics
  that leak through the public interface;
- apply the deletion test to suspected pass-through layers;
- distinguish useful child-module structure from fragmentation;
- inspect whether the public reading entrypoint exposes the common contract and
  control flow without re-exporting implementation detail;
- locate behavior that is difficult to prove through a stable contract.

Depth is not an instruction to make modules large. Deepening is justified only
when one owner can coherently hide knowledge that would otherwise be repeated or
coordinated by callers.

## Classify dependencies and seams

Use project evidence rather than a mandatory pattern:

1. **In-process dependency** — behavior can remain behind the module interface
   without a substitutable adapter.
2. **Local substitute** — a realistic local implementation can exercise the
   contract while production mechanism stays internal.
3. **Owned remote dependency** — transport may sit behind a port when the
   owning responsibility must vary transport or support credible substitutes.
4. **External dependency** — an explicit seam may isolate a third-party
   contract, nondeterminism, or failure behavior.

Do not expose an internal seam merely to make implementation details directly
testable. Do not forbid a seam solely because only one production adapter
exists; consider test substitutes, expected variation, and the cost of the
indirection.

## Testing and compatibility

Use [`shared/TESTING_GUIDELINES.md`](../../../../shared/TESTING_GUIDELINES.md)
as the sole testing authority. Prefer proof through the primary public
interface when that is the smallest stable surface that credibly proves the
behavior. Existing valid tests remain contract evidence until replacement
proof demonstrates equivalent or stronger coverage and their removal or
expectation change receives explicit approval.

When deepening changes a public path or interface, inventory every known
consumer and select an explicit compatibility strategy. Prefer a temporary
facade when practical, migrate callers in a verified order, and leave facade
removal to a separate approved change.
