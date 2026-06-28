---
name: grow-glossary
description: Finds glossary-worthy terminology in the current conversation and session artifacts, diffs it against GLOSSARY.md, and reports only missing terms. Use at the end of a conversation, plan, or implementation when the user wants to grow the glossary, calcify terminology, or review missing glossary candidates.
---

# grow-glossary

## Terms

**Calcify**: promote unstable session vocabulary into stable repo terminology by deciding which terms deserve entries in `GLOSSARY.md`.

## Workflow

1. Use the current conversation as the primary corpus.
2. If the session created plan or note artifacts, read those too.
3. Build a candidate list from terms that:
   - repeat across the conversation or artifacts
   - are used as if already understood
   - conflict with existing wording
   - are explicitly called out as important
4. Exclude generic engineering words and one-off incidental phrases.
5. Read `GLOSSARY.md` and compare each candidate against existing terms and definitions.
6. Drop anything already covered or clearly synonymous with an existing glossary entry.
7. Return only the missing terms.

## Output

Return a flat list. For each item include:

- `term`
- `why it seems glossary-worthy`
- `evidence/context`

Do not edit `GLOSSARY.md`.
Do not show already covered terms, near matches, or synonym notes.
If no missing terms remain after the diff, say so directly.
