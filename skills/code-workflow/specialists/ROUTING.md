# Specialist Routing

Select only specialists justified by the active profile and evidence. Read the
specialist's `REPORT.md`, report template, `PLANNER.md`, plan template, and
applicable local references completely before use.

| Specialist | Report | Planner | Select when |
|---|---|---|---|
| Bug hunt | [REPORT.md](bug-hunt/REPORT.md) | [PLANNER.md](bug-hunt/PLANNER.md) | Runtime correctness, invalid states, edge cases, regressions, or lifecycle/integration risk requires evidence. |
| Code smells | [REPORT.md](code-smells/REPORT.md) | [PLANNER.md](code-smells/PLANNER.md) | A demonstrated Fowler catalog maintenance effect materially affects the requested change. |
| Coding standards accordance | [REPORT.md](coding-standards-accordance/REPORT.md) | [PLANNER.md](coding-standards-accordance/PLANNER.md) | JavaScript or TypeScript guideline deviations directly affect safe implementation. |
| Purpose adherence | [REPORT.md](purpose-adherence/REPORT.md) | [PLANNER.md](purpose-adherence/PLANNER.md) | An approved purpose contract covers the target and proposed behavior must be reconciled with it. |
| Architecture | [REPORT.md](architecture/REPORT.md) | [PLANNER.md](architecture/PLANNER.md) | The request explicitly concerns architecture, depth, locality, leverage, facades, navigability, or public entrypoints, or initial exploration evidences multi-module structural friction. |
| JavaScript to TypeScript | [REPORT.md](js-to-ts/REPORT.md) | [PLANNER.md](js-to-ts/PLANNER.md) | Explicit `.js` or `.jsx` targets require bounded conversion analysis. |
| JavaScript to TypeScript autoscope | [REPORT.md](js-to-ts-autoscope/REPORT.md) | [PLANNER.md](js-to-ts-autoscope/PLANNER.md) | A seed must be expanded into one bounded `deep` or `wide` conversion spine. |

Profiles retain the reason for each selection and may impose narrower routing.
The routing table never authorizes running every specialist by default.
Architecture is routed only by the improvement profile. Its read-only report
may run in autorun, but the first confirmed finding stops autorun before its
interactive planner.
