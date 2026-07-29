# Current Changes Audit

Perform a skeptical, read-only audit after approved implementation. Do not
modify, stage, unstage, commit, revert, or generate correction artifacts.

## Establish evidence

1. Read applicable instructions, contracts, the approved work package, and
   coding and testing guidance.
2. Inventory staged, unstaged, and relevant untracked changes. Preserve the
   index exactly.
3. Compare the diff with approved behavior, acceptance criteria, finding
   dispositions, purpose authority, and preservation requirements.
4. Inspect unchanged callers, contracts, history, configuration, and tests where
   they clarify the changed behavior.
5. Run only non-mutating focused checks. Separate baseline failures from failures
   introduced by the implementation.

## Audit focus

### Logic and state

- Verify every state tells the truth and represents a valid domain outcome.
- Look for missing, impossible, redundant, overlapping, or context-relative
  states.
- Trace initial, success, denial, missing-input, missing-resource, error,
  cancellation, redirect, unmount, and identity-change transitions.
- Check that stale results cannot affect a newer route, entity, or request.
- Confirm defaults and fallbacks do not hide programmer errors or broaden
  access.

### Design and integration

- Look for duplicated sources of truth, contradictory booleans, unnecessary
  state, effects, refs, callbacks, or wrappers.
- Check callers for consistent interpretation and preserved behavior.
- Verify identifiers, URLs, payloads, data formats, errors, and external
  contracts remain exact.
- Ensure protected effects cannot start before the required decision permits
  them.

### Test credibility

- Confirm tests prove approved public behavior and regression prevention.
- Inspect meaningful positive, negative, error, transition, identity-change,
  and no-side-effect paths.
- Identify mocks that bypass the real boundary or make impossible states valid.
- Treat passing tests as evidence, not proof.

## Output

Report:

1. behavioral summary of the complete diff;
2. findings ordered by severity, with location, violated invariant, concrete
   scenario, and smallest correction direction;
3. unnecessary complexity and safe simplification opportunities;
4. missing or misleading proof;
5. verdict and residual risks.

Report findings before fixes. Any corrective code or test edit requires a
supplemental approved plan.
