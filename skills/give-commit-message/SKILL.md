---
name: give-commit-message
description: Produces a concise commit message for completed coding work, emphasizing why the change was made. Use when the user says "GCM", "give commit message", "give me a commit message", or asks for a commit message.
---

# Give Commit Message

Produce only a commit message unless the user asks for explanation. Do not commit anything.

## Steps

1. Review the completed work from the conversation and inspect current changes if needed.
2. Identify the user-facing, architectural, or maintenance reason for the change.
3. Write 1-3 sentences that emphasize why the change was made more than what files changed.

## Style

- Prefer a direct sentence or short subject plus body.
- Avoid bullets, markdown headings, file lists, and generated-by language.
- Mention implementation details only when they clarify the reason or risk being addressed.
- Keep the message specific enough to distinguish this change from nearby work.
