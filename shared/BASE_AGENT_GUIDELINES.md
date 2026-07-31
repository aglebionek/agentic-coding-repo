# Base Agent Guidelines

This directory is the centrally managed shared agent layer. A target project's
root instructions remain authoritative for its purpose, domain rules, safety
constraints, documentation profile, and local workflows.

## Start here

1. Read the target project's root `AGENTS.md`.
2. Read this file and the shared glossary.
3. Read `TESTING_GUIDELINES.md` when executable behavior may change.
4. Read `CODING_GUIDELINES.md` when changing JavaScript or TypeScript.
5. Load only the shared or project-local skills that match the request.

If project instructions conflict with optional shared defaults, follow the
project instructions. Do not use this layer to overwrite project-owned
decisions.

## Operating rules

- Establish the requested outcome, scope, and governing project authority before
  changing files.
- Preserve unrelated work and inspect repository state before broad edits.
- Keep destructive effects, compatibility consequences, security implications,
  and meaningful failure modes visible before acting.
- Do not infer material intended behavior when project authority is missing.
- Follow `TESTING_GUIDELINES.md` for contract-first verification, test
  preservation, and justified alternate proof.
- Use project-native validation and report checks that could not be run.
- Do not commit, push, create external artifacts, or remove worktrees unless the
  user authorizes those actions.

## Resource ownership

- Shared guidelines and reusable skills live under `.agentic/` in an installed
  project.
- Project instructions, glossary, documentation conventions, and local skills
  remain outside `.agentic/` and are never managed by the shared installer.
- Shared skills live in `.agentic/skills/`; project-specific skills normally live
  in `skills/`.

Read `AGENTIC_GLOSSARY.md` for shared workflow terms. Add domain terminology to
the project glossary instead of the shared glossary.
