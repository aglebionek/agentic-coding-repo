# Architecture and Documentation Guidelines

These guidelines help humans and coding agents find the common path quickly
without flattening a system's implementation. Treat them as shared defaults;
each project owns its exact structure, public entrypoint names, documentation
profile, and automated guardrails.

## Progressive disclosure

Organize code and documentation so the first visible layer gives a small,
complete mental model. Deeper layers should reveal implementation detail only
when a reader or caller needs it.

This improves navigability for humans and agents alike: both work best when
purpose, contract, common control flow, and meaningful failure modes are visible
before storage formats, framework wiring, and vendor mechanics. Do not hide
security constraints, destructive effects, compatibility requirements, or other
facts needed for a safe decision.

## Organize by responsibility

At the highest useful level, group modules by the knowledge or responsibility
they own and their reason to change. Reveal language and technical mechanism
inside that responsibility.

Prefer:

```text
catalog/
  index.ts
  parsing/
  storage/
notifications/
  api.py
  delivery/
  preferences/
```

over:

```text
python/
typescript/
validators/
helpers/
```

A language-oriented directory can still be appropriate when the language or
runtime is itself the responsibility, but it should not obscure the domain by
default.

Group by owned knowledge, not by a shared verb. Generic scalar validation and
validation of one domain message have different reasons to change and usually
belong to different owners.

## Use nested interfaces and explicit facades

Each responsibility should expose a narrow contract to its callers. Child
modules may expose narrower contracts to their enclosing responsibility, while
the responsibility's facade protects outside consumers from internal parsing,
storage, orchestration, or vendor details.

A facade should make the common behavior legible and complete. It should not
re-export every internal symbol. Apply the deletion test: if removing a layer
would not leak meaningful complexity into callers, the layer may be
fragmentation rather than useful information hiding.

## Identify a public reading entrypoint

Every substantial responsibility should have one conventional place where a
reader can learn its public contract and common control flow. Choose a filename
that fits the ecosystem, such as `api.py`, `index.ts`, `mod.rs`, or `api.lua`;
do not impose one filename across languages.

The entrypoint should expose:

- the responsibility and supported common operation;
- inputs, outputs, effects, and meaningful failure modes;
- the small public surface;
- links to deeper implementation or technical documentation when needed.

Callers should not need to coordinate internal ordering, state fields, or
recovery steps that the owning module can encapsulate.

## Separate shared primitives from domain rules

Keep truly generic primitives small and stable. Domain-specific rules belong
with the responsibility that knows why they exist, even when their mechanism
resembles a generic helper. A shared primitive should not accumulate policy from
unrelated domains.

## Provide two documentation depths

Projects should make both of these roles discoverable when the subject warrants
them:

- **Approachable documentation** explains purpose, navigation, relationships,
  and common examples in plain language.
- **Technical documentation** records exact contracts, invariants, decisions,
  operations, tests, and evidence.

`docs/overview/` and `docs/technical/` are useful defaults, not required names.
The project documentation profile may choose established equivalents such as
`guide/` and `reference/`, a wiki, or another format.

Do not force both roles for every concept. Write the minimal coherent cluster,
and organize it around stable responsibilities rather than producing one prose
file per source file. Approachable material should lead to technical detail
without duplicating its normative contract.

## Make abstraction traceable

Use concrete examples in public API contracts and documentation. Show a
representative input, output, state transition, or real-life scenario instead of
relying only on abstract prose.

Link in both directions where project conventions allow:

- approachable documentation to the public reading entrypoint and technical
  material;
- technical material to code, decisions, tests, and evidence;
- code-entrypoint documentation back to the relevant maintained docs.

Maintain one canonical location for each normative claim. Other layers should
summarize and link to it.

## Migrate incrementally

When reorganizing an established responsibility, preserve existing consumers
through a compatibility facade when practical. Move behavior behind the new
entrypoint, migrate callers deliberately, and remove compatibility only through
a separate, explicitly approved cleanup.

Make compatibility surfaces and removal conditions visible in the plan. Do not
silently combine an architectural move with a breaking cleanup.

## Documentation profile discovery

Generic tools should discover project conventions in this order:

1. Read the target project's root `AGENTS.md`.
2. Read the documentation root or index it identifies.
3. Use explicitly documented approachable and technical roots and formats.
4. Preserve an evident equivalent structure already present.
5. If no profile exists and inventing one would be material, ask the user.

A project may document a lightweight profile directly in `AGENTS.md`:

```md
## Documentation profile

- Approachable documentation: `docs/overview/`
- Technical documentation: `docs/technical/`
- Documentation mirrors responsibilities, not individual source files.
```

The roles matter more than the directory names.

## Warning signs

- Top-level language splits hide the responsibilities readers seek.
- Generic `utils`, `helpers`, or `validators` directories become junk drawers.
- A facade exposes every implementation detail.
- Overview documentation merely restates technical specifications.
- Technical contracts are duplicated in multiple canonical locations.
- A directory tree requires readers to guess where to start.

Research context is available in
[`Documentation and structure`](../notes/AI/Key%20Ideas/Documentation%20and%20structure.md)
and [`Modularity`](../notes/AI/Key%20Ideas/Modularity.md). This guideline is the
shared operational authority; the notes are supporting research.
