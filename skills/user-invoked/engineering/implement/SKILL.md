---
name: implement
description: Implements a piece of work from a spec or set of tickets. Use when the user invokes `implement` with an approved source of work.
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Before changing code, read `.agentic/ARCHITECTURE_GUIDELINES.md` when
installed, or the repository's canonical equivalent in a shared source tree.

Use the `tdd` skill where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, use the `code-review` skill to review the work.

Commit only when the user explicitly asks.
