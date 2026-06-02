---
name: glossary-handoff
description: Turns deferred glossary backlog items into one aggregated handoff for a later session. Use when the user asks for a glossary handoff, wants to batch terminology updates for later, or wants the backlog turned into a prompt.
---

# Glossary Handoff

## Config

- Glossary path: `./GLOSSARY.md`
- Backlog path: `python3 ./scripts/glossary_backlog.py path`
- Default backlog file today: `/tmp/agentic-coding-glossary-backlog.json`

Edit the backlog path if this repo later wants a different location.

## Workflow

1. Read the glossary if it exists.
2. Read the backlog with:
   ```bash
   python3 ./scripts/glossary_backlog.py handoff --glossary ./GLOSSARY.md
   ```
3. Build one aggregated handoff covering all pending backlog items.
4. Save the handoff plan to the session plan file.
5. Print a handoff block for a fresh session. Suggest a branch name like `docs/glossary-backlog`.

## Rules

- Do not edit `GLOSSARY.md` in this workflow.
- Do not resolve backlog items here.
- If the backlog is empty, say so briefly and stop.
- Keep each backlog item minimal: term, why it matters, evidence/context.
- Preserve the backlog path in the handoff so the next session can reconcile it later.
