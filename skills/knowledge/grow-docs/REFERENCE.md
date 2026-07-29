# Grow Docs Audit Reference

Use the project's existing tools and link format. Do not introduce a new
documentation system solely to run this audit.

## Navigation

- Start at the documented root or index and follow links to every changed page.
- Confirm each new page is reachable through all necessary parent indexes.
- Confirm the overview hierarchy follows stable codebase responsibilities and
  reveals nested responsibilities progressively rather than flattening them or
  reproducing the source tree file-for-file.
- Confirm parent overview docs link to warranted nested overview docs and that
  nested docs provide a clear route back to broader context.
- Confirm a reader can identify the responsibility's public reading entrypoint.
- Confirm deeper technical material is discoverable from overview material
  when both roles exist.

## Links

- Resolve every changed relative Markdown link from the file that contains it.
- Validate project-specific links, anchors, or wiki links with the project's
  established tooling when available.
- Confirm code links point to the maintained public entrypoint rather than a
  replaceable implementation detail unless the detail is the subject.
- Confirm overview docs link to related code files that materially help a reader
  move from the responsibility to its implementation.
- Confirm overview docs link to related technical documentation only when it
  adds warranted depth, rather than as mandatory boilerplate.
- Prefer stable repository-relative links where the publishing system supports
  them.

## Overview and technical depth

- Identify the canonical source for every load-bearing contract or decision.
- Flag duplicated normative claims that could drift.
- Confirm overview docs explain purpose and common use instead of restating
  technical specifications.
- Confirm technical docs link back to the relevant overview and onward to code,
  decisions, tests, and evidence.
- Flag missing transitions where an overview names deeper behavior but provides
  no route to its contract.

## Decisions

- Confirm every newly recorded decision was explicitly approved before this
  workflow.
- Record the decision and its rationale in the project's canonical technical
  documentation, ADR system, or decision format.
- Link summaries to the canonical decision instead of copying the full decision
  into overview and technical pages.
- Return unresolved choices to the user or decision-owning skill; documentation
  placement does not grant authority to settle them.

## Evidence

Report:

- audit commands or inspections performed;
- broken or ambiguous links;
- unreachable pages;
- duplicated canonical claims;
- missing public-entrypoint links;
- missing overview-to-nested, overview-to-code, or warranted
  overview-to-technical transitions;
- decisions lacking approval, rationale, or a canonical location;
- deferred gaps and why they were not filled.
