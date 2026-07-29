# Agentic Coding Repo

A source repository for reusable coding-agent guidelines, skills, terminology,
and distribution tooling.

## Shared base and project overlay

The repository uses an explicit ownership model:

- The **shared base** contains project-agnostic guidance and reusable skills
  maintained here.
- The **project overlay** contains a target project's purpose, domain rules,
  documentation conventions, glossary, local skills, and automated guardrails.

Updating the shared base replaces only the managed `.agentic/` directory. It
does not edit or delete the project overlay.

## Source tree

```text
agentic-coding-repo/
├── AGENTS.md
├── README.md
├── GLOSSARY.md
├── fetch-agent-assets.sh
├── shared/
│   ├── BASE_AGENT_GUIDELINES.md
│   ├── ARCHITECTURE_GUIDELINES.md
│   ├── CODING_GUIDELINES.md
│   ├── TESTING_GUIDELINES.md
│   └── AGENTIC_GLOSSARY.md
├── skills/
└── notes/
```

- Root `AGENTS.md` and `GLOSSARY.md` describe this repository itself.
- `shared/` is the canonical source for distributable guidelines and generic
  terminology.
- `skills/` contains distributable shared skills. `skills/code-workflow/` is a
  deep public facade whose profiles, specialists, quality checks, and guidance
  remain internal to that workflow.
- `notes/` contains supporting research, not installed operational authority.
- Root `CODING_GUIDELINES.md` is a compatibility pointer to the canonical file
  under `shared/`.

## Installed tree

Running the installer in a target project produces:

```text
target-project/
├── AGENTS.md                 # project-owned
├── GLOSSARY.md               # project-owned
├── skills/                   # project-owned local skills
└── .agentic/
    ├── BASE_AGENT_GUIDELINES.md
    ├── ARCHITECTURE_GUIDELINES.md
    ├── CODING_GUIDELINES.md
    ├── TESTING_GUIDELINES.md
    ├── AGENTIC_GLOSSARY.md
    └── skills/               # centrally managed shared skills
```

The installer owns all of `.agentic/` and replaces that directory on each
successful update. It never manages root `AGENTS.md`,
`CODING_GUIDELINES.md`, `GLOSSARY.md`, `skills/`, documentation, or other
project files.

## Install or update

From the root of the target project:

```bash
curl -fsSL https://raw.githubusercontent.com/aglebionek/agentic-coding-repo/main/fetch-agent-assets.sh | bash
```

The script downloads the configured repository branch, validates every required
source asset, stages the complete managed tree, and then replaces `.agentic/`.
It prints each installed managed asset.

For local validation or development, bypass the download:

```bash
AGENTIC_SOURCE_DIR=/path/to/agentic-coding-repo \
AGENTIC_TARGET_DIR=/path/to/disposable-target \
bash fetch-agent-assets.sh
```

`AGENTIC_SOURCE_DIR` must point to a source tree containing `shared/` and
`skills/`. `AGENTIC_TARGET_DIR` defaults to the current directory.

## Opt in from a project

Installation does not modify project instructions. Add an adoption section to
the target project's own `AGENTS.md`:

```md
## Shared agent resources

Read and follow:

- `.agentic/BASE_AGENT_GUIDELINES.md`
- `.agentic/ARCHITECTURE_GUIDELINES.md`
- `.agentic/TESTING_GUIDELINES.md` when executable behavior may change
- `.agentic/CODING_GUIDELINES.md` when applicable
- `.agentic/AGENTIC_GLOSSARY.md`

Shared skills live under `.agentic/skills/`. Project-specific skills live under
`skills/`.
```

The project's instructions decide how shared defaults interact with local
authority.

`shared/TESTING_GUIDELINES.md` is the canonical project-agnostic testing
authority and is installed as `.agentic/TESTING_GUIDELINES.md`. Language- and
workflow-specific resources link to it instead of restating its policy.

## Skills and glossaries

Shared skills are updated as one managed set under `.agentic/skills/`.
Project-specific skills remain under root `skills/`; the installer neither
moves nor compares them automatically.

Use the public `code-workflow` profiles for issue work, bug fixes, improvement,
and JavaScript-to-TypeScript conversion. Its report/planner specialists and
current-changes audit are internal modules, not independently invocable skills.

Shared workflow terms belong in `.agentic/AGENTIC_GLOSSARY.md`. A project's
domain language belongs in its root `GLOSSARY.md`. Projects should reference the
shared glossary rather than copying it into their local glossary.

## Documentation profiles

Generic documentation skills discover conventions from the project instead of
assuming one layout:

1. Read the project `AGENTS.md`.
2. Read the documentation root or index it identifies.
3. Use declared approachable and technical roots and formats.
4. Preserve an evident equivalent structure.
5. Ask before inventing a material profile when none exists.

Projects may use `docs/overview/` and `docs/technical/`, but those are only
defaults. Project-specific link formats, purpose contracts, and automated
architecture or documentation guardrails remain local.

## Migration from the legacy installer

Older versions copied root `AGENTS.md`, `CODING_GUIDELINES.md`, `GLOSSARY.md`,
and the entire root `skills/` directory into target projects. The current
installer does not delete, move, merge, or overwrite those legacy paths.

After installing `.agentic/`:

1. Add the opt-in section to the project-owned `AGENTS.md`.
2. Review legacy root copies manually.
3. Keep project-specific content in root files and `skills/`.
4. Remove obsolete legacy copies only through a separate, project-approved
   cleanup.

Older shared versions advertised standalone report/planner pairs,
`testable-module`, `validate-current-changes`, and
`review-intent-and-coverage`. Those entrypoints were intentionally removed.
Use the matching `code-workflow` profile; its facade now owns specialist
routing, contract and fixture planning, and final diff auditing. External
automation that invoked the retired standalone skills must migrate atomically
to a `code-workflow` invocation.

When a root coding-guidelines file or local skills tree exactly matches the
current shared source, the installer reports it as a possible legacy copy for
manual review. It never removes it.
