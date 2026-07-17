# Fowler Code-Smell Catalog

Use only these 24 smells from Martin Fowler's *Refactoring, 2nd Edition*. The criteria below are diagnostic paraphrases, not automatic thresholds. Confirm a smell only when contextual evidence shows the named structure creates a maintenance effect; record relevant counterevidence.

| Canonical smell | Diagnostic criterion | Evidence required | Common false positive |
|---|---|---|---|
| Mysterious Name | A name fails to communicate the role or behavior readers need. | Show the misleading or opaque name and the meaning recoverable only from other evidence. | An unfamiliar but precise domain term. |
| Duplicated Code | Substantially the same knowledge or behavior is maintained in multiple places. | Trace the repeated logic and the shared reason it would change. | Superficially similar code encoding different decisions. |
| Long Function | A function combines enough distinct steps or knowledge that its intent is hard to grasp locally. | Identify the mixed responsibilities or explanatory sections and their comprehension cost. | A linear, cohesive function whose extraction would hide its story. |
| Long Parameter List | Callers must supply excessive or repeatedly grouped context to invoke a function correctly. | Show caller burden, recurring groups, derivable values, or parameters belonging to an object. | Explicit independent inputs that keep dependencies honest. |
| Global Data | Mutable data is broadly reachable without a narrow owner controlling access. | Trace mutation and access paths and the resulting hidden coupling. | Immutable constants or state behind a controlled interface. |
| Mutable Data | In-place changes make values, timing, or ownership difficult to reason about. | Show mutations whose ordering, aliasing, or lifecycle increases maintenance effort. | Local mutation with narrow ownership and no escaped aliases. |
| Divergent Change | One module changes for several unrelated reasons. | Cite distinct change axes concentrated in the same module, supported by responsibilities or history. | Several edits serving one cohesive responsibility. |
| Shotgun Surgery | One conceptual change routinely requires coordinated edits across many locations. | Map the single change reason to scattered affected sites or historical examples. | A one-off migration or generated mechanical update. |
| Feature Envy | Behavior relies more on another object or module's data than on its own owner's knowledge. | Compare accessed knowledge and show why responsibility is misplaced. | An adapter intentionally translating at a seam. |
| Data Clumps | The same meaningful group of values repeatedly travels or is declared together without a shared abstraction. | Show repeated groupings and the concept or invariant they jointly represent. | Coincidental parameter overlap without shared meaning. |
| Primitive Obsession | Primitive values repeatedly encode a domain concept, rules, units, or valid states. | Show duplicated validation, formatting, interpretation, or invalid combinations. | A primitive whose meaning and validation are genuinely trivial. |
| Repeated Switches | The same type or state distinction drives branching in multiple places. | Trace repeated cases and the change amplification caused by adding or changing a variant. | One exhaustive branch at the behavior's natural owner. |
| Loops | An imperative loop obscures a recognizable transformation or selection pipeline. | Show the simpler intent hidden by control state, mutation, or mixed loop duties. | A performance-critical or stateful traversal clearer as a loop. |
| Lazy Element | A named element adds indirection without enough behavior, policy, or reuse to justify itself. | Apply the deletion test and show that removing it reduces knowledge required by callers. | A small element that owns a real seam, invariant, or domain name. |
| Speculative Generality | Flexibility exists for hypothetical use cases and increases present-day complexity. | Show unused extension points, parameters, abstractions, or implementations and their carrying cost. | A demonstrated second use or an explicit required contract. |
| Temporary Field | An object's field is meaningful only during limited phases, leaving other states confusing or invalid. | Trace when the field is populated, consumed, and meaningless, plus the conditional reasoning required. | Explicit optional state modeled with clear lifecycle semantics. |
| Message Chains | A caller traverses a sequence of objects and thereby learns their navigation structure. | Show the chain and how intermediate structure leaks into callers or amplifies changes. | A short fluent interface intentionally designed for chaining. |
| Middle Man | A module mostly delegates and adds little policy, translation, or protection. | Compare its interface and implementation, and show the indirection's maintenance cost. | An adapter that isolates a volatile dependency or enforces a seam. |
| Insider Trading | Modules exchange excessive internal knowledge or reach around their intended interfaces. | Show leaked internals, privileged access, or reciprocal coupling and its change cost. | Deliberate collaboration through a narrow, stable interface. |
| Large Class | A class owns too much state or too many responsibilities to remain cohesive. | Group fields and methods by responsibility and show independent change reasons or hidden subsets. | A large but cohesive class with a small, stable interface. |
| Alternative Classes with Different Interfaces | Classes perform equivalent roles through unnecessarily different interfaces. | Show substitutable intent, caller branching or adapters, and the avoidable vocabulary mismatch. | Similar outcomes belonging to distinct domain contracts. |
| Data Class | A class mainly exposes data while behavior that belongs with that data lives elsewhere. | Locate the external behavior and show the class lacks ownership of relevant rules. | A deliberate immutable value, DTO, event, or serialization shape. |
| Refused Bequest | A subtype inherits behavior or data it cannot honor or meaningfully use. | Show ignored, rejected, overridden, or invariant-breaking inherited features. | A subtype using a small but valid portion of a stable abstraction. |
| Comments | A comment compensates for code whose intent or structure should be made clear directly. | Show the obscured code and what design problem the comment is carrying. | Rationale, constraints, public documentation, or warnings code cannot express. |

## Coverage statuses

Use `detected`, `no evidence`, `not applicable`, or `not verifiable` in catalog coverage. `No evidence` means the complete pass found no qualifying instance; it does not prove permanent absence. Explain every `not applicable` and `not verifiable` status.
