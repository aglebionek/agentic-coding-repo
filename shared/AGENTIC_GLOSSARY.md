# Shared Agentic Glossary

These are canonical, project-agnostic terms distributed with the shared agent
layer. Target projects keep domain terminology in their own `GLOSSARY.md`.

## Agent session

A single AI working conversation with its own task context, instructions, and
usually its own workspace or worktree.

## Approachable documentation

Plain-language documentation that helps a reader understand purpose,
relationships, navigation, and common examples before exact implementation
detail.

## Calcify

To promote unstable session vocabulary into stable shared or project
terminology by deciding that it deserves a glossary entry.

## Documentation profile

A project-owned declaration or evident convention that identifies its
documentation roots, formats, and the locations serving approachable and
technical roles.

## Focused glossary session

A session whose main goal is reviewing and updating glossary terminology rather
than interrupting unrelated implementation or planning work.

## Glossary backlog

A deferred list of terminology candidates kept outside the project by default
until a focused glossary session reviews them.

## Glossary candidate

A repeated, conflicting, missing, or explicitly important term worth evaluating
for a shared or project glossary.

## Grill me

A workflow that interviews the user about a plan or design until material open
decisions and their reasons are explicit.

## Grow docs

A profile-driven workflow that maintains navigable, responsibility-level
documentation and audits its links, depth transitions, and canonical sources.

## Handoff

A durable transfer of context into a fresh agent session, normally consisting
of a saved implementation plan and an exact continuation prompt.

## Nested API

An API structure in which child modules expose narrow contracts to their
enclosing responsibility while only that responsibility's facade is exposed to
outside consumers.

## Progressive disclosure

An organization principle in which code, APIs, and documentation present the
smallest complete mental model first and reveal deeper capability only as
needed.

## Project overlay

The project-owned instructions, glossary, documentation conventions, local
skills, and domain constraints that specialize the shared agent layer without
being overwritten by it.

## Public reading entrypoint

The ecosystem-appropriate file or module where a reader first encounters a
responsibility's public contract and common control flow.

## Responsibility-first organization

Grouping code and documentation by the knowledge or outcome they own and their
reason to change, with languages and mechanisms revealed at deeper levels.

## Session plan

A saved planning artifact that lets another agent session continue without
depending on chat memory.

## Shared agent layer

The centrally managed, project-agnostic guidelines, glossary, and reusable
skills installed under `.agentic/`.

## Skill

A reusable instruction bundle with a `SKILL.md` entrypoint that teaches an agent
a named workflow and when to use it.

## Technical documentation

Precise documentation of contracts, invariants, decisions, gates, operations,
tests, and evidence.

## Testable module

A refactoring target with a clear public contract and deterministic test surface
that can be verified without reaching through private implementation details.

## Worktree workflow

A convention in which concurrent agent sessions use separate Git worktrees to
isolate branches and file changes.
