# Grow Docs Audit Reference

Use the project's existing tools and link format. Do not introduce a new
documentation system solely to run this audit.

## Navigation

- Start at the documented root or index and follow links to every changed page.
- Confirm each new page is reachable through all necessary parent indexes.
- Confirm a reader can identify the responsibility's public reading entrypoint.
- Confirm deeper technical material is discoverable from approachable material
  when both roles exist.

## Links

- Resolve every changed relative Markdown link from the file that contains it.
- Validate project-specific links, anchors, or wiki links with the project's
  established tooling when available.
- Confirm code links point to the maintained public entrypoint rather than a
  replaceable implementation detail unless the detail is the subject.
- Prefer stable repository-relative links where the publishing system supports
  them.

## Authority and depth

- Identify the canonical source for every load-bearing contract or decision.
- Flag duplicated normative claims that could drift.
- Confirm approachable docs explain purpose and common use instead of restating
  technical specifications.
- Confirm technical docs link to relevant decisions, tests, and evidence.
- Flag missing transitions where an overview names deeper behavior but provides
  no route to its contract.

## Evidence

Report:

- audit commands or inspections performed;
- broken or ambiguous links;
- unreachable pages;
- duplicated canonical claims;
- missing public-entrypoint links;
- deferred gaps and why they were not filled.
