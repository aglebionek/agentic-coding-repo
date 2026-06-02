## Brief
This is a personal repo for agentic coding workflows — configurations, scripts, and skills for working with AI coding agents (primarily GitHub Copilot CLI). 

## Contents
- `AGENTS.md`: This file, used when working on this repo.
- `GLOSSARY.md`: Shared glossary for stable terminology across sessions. Read it at session start when it exists.

### Skills
Whenever a user mentions a skill to use, look at the available skills in the `skills/` directory and use the relevant one.

- `./skills/answer-and-stop/SKILL.md`: Answer the user's question and stop. Use when the user wants a direct answer without further questioning.
- `./skills/glossary-handoff/SKILL.md`: Turn pending glossary backlog items into one aggregated handoff for a later session. Use when user wants to defer glossary work, asks for a glossary handoff, or wants the backlog batched into a prompt.
- `./skills/glossary-backlog-cleanup/SKILL.md`: Reconcile pending glossary backlog items against `GLOSSARY.md` and mark clearly completed items resolved. Use when user asks to clean up, reconcile, or resolve glossary backlog items after glossary work.
- `./skills/grill-me/SKILL.md`: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
- `./skills/grow-docs/SKILL.md`: Writes and expands an Obsidian knowledge vault at docs/obsidian/ for this repo. Creates clusters of brief, wikilinked notes from codebase exploration, then audits the vault for broken wikilinks and surfaces gaps. Use when user wants to document, expand, or map the codebase in Obsidian, or says "grow docs", "document X", "add obsidian docs", or "expand the vault".
- `./skills/handoff/SKILL.md`: Use when user mentions "handoff". Used to create a handoff prompt for a fresh session.
- `./skills/write-a-skill/SKILL.md`: Write a new skill based on user instructions. Use when user wants to create a new skill, or says "write a skill", "create a skill", or "new skill".

### Glossary workflow
1. At session start, if `./GLOSSARY.md` exists, read it before planning or answering so terminology stays consistent.
2. During normal work, do not derail the session into glossary editing. When you notice a strong glossary candidate, capture it to the deferred backlog and continue the main task.
3. A glossary candidate is worth capturing only when at least one of these is true:
   - repeated term usage suggests a concept should be defined
   - a term conflicts with existing glossary language
   - an important term is missing from `GLOSSARY.md`
   - the user explicitly asks for a glossary change
4. Capture only a minimal note: term, why it looks glossary-worthy, and evidence/context. Merge repeated sightings into the same backlog item instead of creating duplicates.
5. Use `python3 ./scripts/glossary_backlog.py capture ...` with the default backlog path, unless the user or repo instructions override it.
6. After capture, send only a short deferral notice. Do not start a glossary discussion unless the user asks for it.
7. Do not update `GLOSSARY.md` automatically during unrelated work. Use the glossary handoff skill to batch pending items for later, and the glossary backlog cleanup skill to mark items resolved after glossary work is done.