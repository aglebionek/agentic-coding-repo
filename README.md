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
│   ├── AGENTS_TEMPLATE.md
│   ├── BASE_AGENT_GUIDELINES.md
│   ├── ARCHITECTURE_GUIDELINES.md
│   ├── CODING_GUIDELINES.md
│   ├── TESTING_GUIDELINES.md
│   └── AGENTIC_GLOSSARY.md
├── skills/
│   ├── code-workflow/
│   ├── interaction/
│   ├── knowledge/
│   ├── delivery/
│   └── skill-authoring/
└── notes/
```

- Root `AGENTS.md` and `GLOSSARY.md` describe this repository itself.
- `shared/` is the canonical source for distributable guidelines and generic
  terminology.
- `skills/` contains distributable shared skills grouped by responsibility.
  `interaction/`, `knowledge/`, `delivery/`, and `skill-authoring/` contain
  complete public skill bundles; their group roots are organizational and are
  not skills themselves. `skills/code-workflow/` remains a deep public facade
  whose profiles, specialists, quality checks, and guidance are internal to
  that workflow.
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
    ├── AGENTS_TEMPLATE.md
    ├── BASE_AGENT_GUIDELINES.md
    ├── ARCHITECTURE_GUIDELINES.md
    ├── CODING_GUIDELINES.md
    ├── TESTING_GUIDELINES.md
    ├── AGENTIC_GLOSSARY.md
    └── skills/               # centrally managed shared skills
```

The installer owns all of `.agentic/`, including `AGENTS_TEMPLATE.md`, and
replaces that directory on each successful update. It never manages root
`AGENTS.md`, `CODING_GUIDELINES.md`, `GLOSSARY.md`, `skills/`, documentation,
or other project files.

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

## Create project instructions

Installation does not create or modify project instructions. For a new project
without root instructions, copy the managed template:

```bash
cp .agentic/AGENTS_TEMPLATE.md AGENTS.md
```

Fill the purpose, project rules, documentation profile, validation commands,
glossary locations, and optional local-skill entries in the root copy. It
already contains the installed `.agentic/` resource paths and the complete
public shared-skill catalog.

The root `AGENTS.md` is project-owned and survives every managed update.
`.agentic/AGENTS_TEMPLATE.md` is shared and replaceable; changes made directly
to it are discarded by the next install. Existing projects should adopt useful
template sections manually rather than overwriting their root instructions.
The project's instructions decide how shared defaults interact with local
authority.

`shared/TESTING_GUIDELINES.md` is the canonical project-agnostic testing
authority and is installed as `.agentic/TESTING_GUIDELINES.md`. Language- and
workflow-specific resources link to it instead of restating its policy.

## Skills and glossaries

Shared skills are updated as one managed set under `.agentic/skills/`.
Project-specific skills remain under root `skills/`; the installer neither
moves nor compares them automatically.

Root `AGENTS.md` is the canonical catalog for public source skill locations.
External consumers that hardcode paths into this source repository must use
the responsibility-grouped locations from that catalog. Installed projects do
not migrate individual skill paths: the next managed update replaces the
complete `.agentic/skills/` tree atomically.

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

1. Copy or manually adopt `.agentic/AGENTS_TEMPLATE.md` into the project-owned
   root `AGENTS.md`.
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

Current shared skill bundles are grouped by interaction, knowledge, delivery,
and skill-authoring responsibility. External automation with hardcoded paths
from the earlier flat source tree must update those paths using the root
`AGENTS.md` catalog. Managed installations receive the reorganized tree as a
complete replacement, so stale managed flat paths disappear without touching a
project-owned root `skills/` directory.

When a root coding-guidelines file or local skills tree exactly matches the
current shared source, the installer reports it as a possible legacy copy for
manual review. It never removes it.
