# Architecture Language

Use this vocabulary as a preferred analytical lens alongside the project's
established domain terms and the shared
[`ARCHITECTURE_GUIDELINES.md`](../../../../shared/ARCHITECTURE_GUIDELINES.md).
It is not an exclusive naming system.

## Terms

**Module**
: A responsibility-bearing unit with an interface and an implementation. It
  may be a function, class, package, subsystem, or tier-spanning slice.

**Interface**
: Everything a caller must know to use a module correctly: its callable API,
  types, invariants, ordering, effects, error modes, configuration, and relevant
  performance constraints.

**Implementation**
: The behavior and mechanism hidden behind an interface.

**Depth**
: Leverage at an interface. A deep module provides substantial coherent
  behavior through a comparatively small interface; a shallow module exposes
  nearly as much complexity as it hides.

**Seam**
: A place where behavior can vary or be substituted without editing the caller
  at that place.

**Adapter**
: A concrete implementation satisfying an interface at a seam. The term names
  a role, not the size or technology of the implementation.

**Leverage**
: The capability callers gain per unit of interface they must learn.

**Locality**
: The concentration of related knowledge, change, defects, and verification in
  the responsibility that owns them.

**Deletion test**
: A diagnostic thought experiment: if removing a module merely spreads its
  complexity among callers, it was hiding useful knowledge; if the complexity
  disappears, the module may be pass-through structure.

## Relationships and qualifications

- A module may expose one primary public interface while containing nested
  internal APIs and child-module interfaces.
- An API is the concrete callable surface within the broader interface.
- A seam describes substitutability. A boundary remains valid for process,
  trust, domain, deployment, and system divisions.
- Depth is judged by coherent responsibility and caller burden, not line-count
  ratios or implementation size.
- The public interface is the preferred behavioral test surface when it is the
  smallest stable surface that credibly proves the contract.
- One adapter can indicate a hypothetical seam and two can evidence real
  variation, but adapter count is a heuristic rather than a prohibition.
- Shared architecture guidance, active project instructions, approved
  decisions, public contracts, and established domain language remain
  authoritative.
