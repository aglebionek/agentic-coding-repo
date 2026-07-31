# Issue tracker: GitHub

Specs, tickets, and Wayfinder maps for this repository live as GitHub issues.
Use the `gh` CLI for all operations. Infer the repository from `git remote -v`;
`gh` does this automatically when run inside this clone.

## Conventions

- **Create an issue**:
  `gh issue create --title "..." --body "..."`.
- **Read an issue**:
  `gh issue view <number> --comments`.
- **List issues**:
  `gh issue list --state open --json number,title,body,labels,comments`.
- **Comment on an issue**:
  `gh issue comment <number> --body "..."`.
- **Apply or remove a structural label**:
  `gh issue edit <number> --add-label "..."` or
  `gh issue edit <number> --remove-label "..."`.
- **Close an issue**:
  `gh issue close <number> --comment "..."`.

Use a file or heredoc for multi-line issue bodies and comments.

## Skill behavior

When a skill says to publish to the issue tracker, create a GitHub issue in
this repository. When a skill says to fetch a ticket, run
`gh issue view <number> --comments`.

`to-spec` publishes one spec per issue. `to-tickets` publishes one issue per
approved ticket in dependency order. Neither skill applies triage labels.

## Wayfinding operations

`wayfinder` uses GitHub's native sub-issue and dependency relationships. Do
not fall back to task lists or textual `Blocked by:` conventions.

- **Map**: Create one issue labelled `wayfinder:map`. Its body contains the
  destination, notes, decisions so far, unspecified work, and out-of-scope
  work.
- **Child ticket**: Create a GitHub sub-issue of the map and apply one
  structural label: `wayfinder:research`, `wayfinder:prototype`,
  `wayfinder:grilling`, or `wayfinder:task`.
- **Blocking**: Add a native dependency with
  `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-database-id>`.
  Obtain the database ID with
  `gh api repos/<owner>/<repo>/issues/<number> --jq .id`.
- **Frontier**: Consider the map's open child issues in map order. A ticket is
  available when it has no open blockers and no assignee.
- **Claim**: Assign the ticket to the authenticated GitHub user with
  `gh issue edit <number> --add-assignee @me` before starting work.
- **Resolve**: Post the full answer as a comment, close the ticket, and append
  a one-line summary linked to the closed ticket under the map's
  `Decisions so far` section.

The five `wayfinder:*` structural labels are expected to exist before
Wayfinder first publishes a map. Setup documents but does not create them.
