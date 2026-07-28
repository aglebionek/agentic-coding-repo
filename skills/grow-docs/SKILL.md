---
name: grow-docs
description: Maintains project documentation around stable responsibilities, including approachable explanations, technical contracts, navigation, links, and gap audits. Use when the user invokes grow-docs, asks to document or expand a responsibility, improve documentation navigation, or run a documentation link or gap pass.
---

# Grow Docs

Maintain the smallest coherent documentation cluster that makes a responsibility
discoverable from overview to implementation.

## Workflow

1. Read the repository's `AGENTS.md`. Read
   `.agentic/ARCHITECTURE_GUIDELINES.md` when installed, or the repository's
   canonical equivalent when working in its source tree.
2. Discover the documentation profile from project instructions, its docs
   root/index, and evident existing conventions. Preserve established paths and
   Markdown/link formats. If no profile exists and creating one would be
   material, ask before inventing it.
3. Establish the responsibility or concept and its approved purpose. Preserve
   approved contracts and decisions. Do not infer material intended behavior;
   report missing authority instead of writing speculative documentation.
4. Explore the public reading entrypoint, implementation, existing approachable
   and technical docs, decisions, tests, and evidence.
5. Choose the justified depth: approachable documentation only, technical
   documentation only, or both cross-linked.
6. Update the minimal coherent cluster around the responsibility. Include a
   concrete input/output, state transition, or real-life example where useful.
7. Update every necessary parent index so navigation remains continuous.
8. Link approachable docs to the public code entrypoint and deeper technical
   material. Link technical docs to code, decisions, tests, and evidence. Add a
   code-entrypoint link back to docs only when project convention permits it.
9. Run the format-appropriate audit in [REFERENCE.md](REFERENCE.md).
10. Report changed documents, updated indexes, preserved canonical sources, and
    deferred gaps.

## Rules

- Do not hardcode a documentation root, domain directory, or link syntax.
- Do not force both documentation roles for every concept.
- Mirror stable responsibilities, not individual source files.
- Do not duplicate normative contracts into approachable docs.
- Do not create speculative documentation for behavior that does not exist.
- Keep one canonical source for each load-bearing claim and link other layers to
  it.
