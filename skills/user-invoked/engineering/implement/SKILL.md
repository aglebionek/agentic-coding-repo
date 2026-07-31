---
name: implement
description: Implements a piece of work from a spec or set of tickets. Use when the user invokes `implement` with an approved source of work.
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use the `tdd` skill where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, use the `code-review` skill to review the work.

Commit only when the user explicitly asks.
