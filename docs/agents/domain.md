# Domain docs

This repository uses a single-context domain model.

## Before exploring

Read:

- `CONTEXT.md` at the repository root;
- relevant ADRs under `docs/adr/`, when that directory exists.

If an ADR directory or relevant ADR does not exist, proceed silently. Create
`docs/adr/` only when the first architectural decision is recorded.

## File structure

```text
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       └── NNNN-<decision-name>.md
└── ...
```

## Use the domain vocabulary

When output names a domain concept—in an issue title, refactor proposal,
hypothesis, test name, or code interface—use the term defined in
`CONTEXT.md`. Do not drift to synonyms that the context explicitly avoids.

If a needed concept is missing or conflicts with existing language, call it
out as a possible `domain-modeling` task rather than silently inventing a new
term.

## Flag ADR conflicts

If proposed work contradicts an existing ADR, identify the ADR and explain why
reopening the decision may be justified. Do not silently override a documented
decision.
