---
name: grow-docs
description: Maintains progressively disclosed overview and technical documentation around stable codebase responsibilities, including navigation, approved decisions, links, and gap audits. Use when the user invokes grow-docs, asks to document or expand a responsibility, improve documentation navigation, record an approved decision, or run a documentation link or gap pass.
---

# Grow Docs

Maintain the smallest coherent documentation cluster that makes a responsibility
discoverable from overview to implementation.

## Documentation roles

- **Overview documentation** provides the approachable path: purpose, mental
  model, responsibility hierarchy, navigation, relationships, and concrete
  common examples. It should follow the codebase's responsibility structure,
  link progressively to nested overview docs, link related code files, and lead
  to technical documentation when deeper contracts or evidence are warranted.
- **Technical documentation** records exact contracts, invariants, failure
  modes, operations, tests/evidence, and approved load-bearing decisions with
  their rationale. It links back to the relevant overview, public code
  entrypoint, implementation, and canonical decision source.

Use the paths and names declared by the project documentation profile.
`docs/overview/` and `docs/technical/` are recommended defaults, not mandatory
directories.

## Workflow

1. Read the repository's `AGENTS.md`. Read
   `.agentic/ARCHITECTURE_GUIDELINES.md` when installed, or the repository's
   canonical equivalent when working in its source tree.
2. Discover the documentation profile from project instructions, its docs
   root/index, and evident existing conventions. Preserve established paths and
   Markdown/link formats. If no profile exists and creating one would be
   material, ask before inventing it.
3. Establish the responsibility or concept, its approved purpose, and any
   approved decisions supplied by the user or another skill. Preserve existing
   contracts and decisions. Do not infer material intended behavior or resolve
   open decisions; report missing authority instead.
4. Explore the codebase responsibility hierarchy, public reading entrypoint,
   related code files, existing overview and technical docs,
   decisions, tests, and evidence.
5. Choose the justified depth: overview only, technical only, or both
   cross-linked.
6. Update the minimal coherent cluster around the responsibility. Include a
   concrete input/output, state transition, or real-life example where useful.
   Record approved load-bearing decisions and rationale in the project's
   canonical technical or decision format when documentation authority and
   placement are clear.
7. Update every necessary parent index and nested overview link so navigation
   follows the responsibility hierarchy without mirroring source files
   one-for-one.
8. Link overview docs to nested docs, relevant code files, the public
   entrypoint, and warranted technical material. Link technical docs to the
   overview, code, canonical decisions, tests, and evidence. Add code-to-doc
   links only when project convention permits them.
9. Run the format-appropriate audit in [REFERENCE.md](REFERENCE.md).
10. Report changed documents, updated indexes, preserved canonical sources, and
    deferred gaps.

## Rules

- Do not hardcode a documentation root, domain directory, or link syntax.
- Do not force both documentation roles for every concept.
- Mirror stable responsibilities, not individual source files.
- Do not duplicate normative contracts into overview docs.
- Do not create speculative documentation for behavior that does not exist.
- Do not turn an open question into a recorded decision; return it to the user
  or the decision-owning skill.
- Keep one canonical source for each load-bearing claim and link other layers to
  it.
