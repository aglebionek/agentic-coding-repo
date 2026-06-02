---
name: glossary-backlog-cleanup
description: Reconciles deferred glossary backlog items against GLOSSARY.md and marks clearly completed ones resolved. Use when the user asks to clean up glossary backlog items, reconcile them after glossary work, or mark completed glossary items resolved.
---

# Glossary Backlog Cleanup

## Config

- Glossary path: `./GLOSSARY.md`
- Backlog path: `python3 ./scripts/glossary_backlog.py path`
- Default backlog file today: `/tmp/agentic-coding-glossary-backlog.json`

Edit the backlog path if this repo later wants a different location.

## Workflow

1. Read `./GLOSSARY.md`.
2. Read pending backlog items with:
   ```bash
   python3 ./scripts/glossary_backlog.py list
   ```
3. Compare the glossary against each pending item.
4. When the glossary clearly covers an item, mark it resolved with:
   ```bash
   python3 ./scripts/glossary_backlog.py resolve --id <item-id> --note "<why it is now resolved>"
   ```
5. Leave ambiguous items pending and report them briefly.

## Rules

- Do not edit the glossary unless the user explicitly asked for glossary edits in this session.
- Auto-resolve only when the match is clear from the glossary text.
- Prefer leaving an item pending over resolving it on weak evidence.
- If glossary work introduced a new mismatch, capture it as a fresh backlog item instead of overloading an older one.
