---
name: grow-glossary
description: Finds glossary-worthy terms in the current conversation and session artifacts, compares them with shared and project glossaries, and reports only missing terminology. Use when the user wants to grow a glossary, calcify terminology, or review missing glossary candidates.
---

# Grow Glossary

## Workflow

1. Use the current conversation as the primary corpus and read relevant plan or
   note artifacts created during the session.
2. Build candidates from terms that repeat, are used as established vocabulary,
   conflict with existing wording, or are explicitly important.
3. Exclude generic engineering words and incidental phrases.
4. Read `.agentic/AGENTIC_GLOSSARY.md` when present and the project's
   `GLOSSARY.md` when present. In this shared source repository, read
   `shared/AGENTIC_GLOSSARY.md` and root `GLOSSARY.md`.
5. Treat shared terms as covered. Drop candidates already defined or clearly
   synonymous with an existing entry.
6. Report only project-specific terms or genuinely missing generic terms. Mark
   which glossary should own each genuinely missing term.

## Output

Return a flat list containing:

- `term`;
- `suggested owner` (`shared` or `project`);
- `why it seems glossary-worthy`;
- `evidence/context`.

Do not edit a glossary. Do not copy the shared glossary into a project glossary.
If no missing terms remain, say so directly.
