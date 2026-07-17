---
name: create-report-planner-skill
description: Creates or updates nested, read-only report/planner skill pairs with interoperable Markdown artifacts and interactive or AFK-safe planning. Use only when the user explicitly says "create report/planner skill" or asks to update an existing report/planner skill pair.
---

# Create Report/Planner Skill

## Start

1. Read [grill-me](../grill-me/SKILL.md) and [write-a-skill](../write-a-skill/SKILL.md) completely.
2. Inspect `AGENTS.md`, related skills, repository conventions, and an existing pair when updating one.
3. Ask one question at a time, recommend an answer, and inspect the repository instead of asking discoverable questions.
4. Do not create or edit the pair until the user approves the completed design and implementation plan.

## Gather the contract

Resolve:

- capability name and whether to create or update it
- report's read-only analytical responsibility and evidence sources
- planner's planning responsibility and preservation boundaries
- explicit report, planner, and autoplan invocation phrases
- what makes the report `Valid: true`
- capability-specific report sections and plan requirements
- concrete need for templates, examples, references, or scripts

When updating a pair, summarize its current behavior and preserve capability-specific content unless the approved design changes it.

## Design the pair

Use this default layout:

```text
skills/<capability>/
├── report/SKILL.md   # name: <capability>-report
└── planner/SKILL.md  # name: <capability>-planner
```

See the canonical pair: [purpose-adherence report](../purpose-adherence/report/SKILL.md) and [purpose-adherence planner](../purpose-adherence/planner/SKILL.md).

Require explicit invocations; do not trigger on generic review or planning requests. Add resources only when the approved design demonstrates a concrete need. Keep every reference one level deep from its `SKILL.md`.

### Report contract

Make the report portable, self-contained Markdown beginning with:

```md
# <Capability> Report

## Result
- Valid: `true|false`
- Summary: <one-sentence outcome>
```

Define validity for the capability. A false result must remain an actionable recovery handoff: explain blockers, reliable evidence, exact resolution steps and questions with recommendations, useful repository locations, rerun conditions, and the suggested next invocation. Do not include a speculative plan.

### Planner contract

Support both modes in the same planner skill:

- `<capability> planner`: explicitly interactive; use `grill-me` to resolve decisions.
- `<capability> autoplan`: non-interactive and AFK-safe; reject `Valid: false` immediately without asking questions or falling back to `grill-me`.

Both modes are read-only and produce one definitive actionable path. Require the plan to identify its source report and mode, map actions to findings, define scope and verification, and record autonomous or user-approved decisions. An explicitly invoked interactive planner may resolve an invalid report's blockers before planning.

Keep execution, approval loops, runners, and orchestration outside the pair. Record them only as separate follow-up capabilities when needed.

## Review and implement

1. Present the completed design and a file-by-file implementation plan.
2. Wait for explicit approval of the whole plan; incorporate partial approval into a revised plan first.
3. Create or update only approved files and add both exact skill paths and triggers to `AGENTS.md`.
4. Change glossary terminology only with explicit approval. Never commit unless asked.
5. Verify both descriptions have explicit triggers, each `SKILL.md` is under 100 lines, terms are consistent, resources are justified, references are one level deep, and `AGENTS.md` matches.
6. Perform the compact pass required by `write-a-skill` and report validation results.
