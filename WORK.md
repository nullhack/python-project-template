# WORK — Active Work Tracking

This file is a redirect. Dynamic work state is now tracked in flowception session files.

**Read `.flowception/session-*.yaml`** for the current session state.

Each session tracks:
- `current.flow` — which flow is active (e.g. `feature-flow`)
- `current.state` — which state the work item is in
- `params` — work item parameters (feature_slug, branch_name)
- `stack` — subflow context (for TDD cycle)
- `transitions` — transition history (sparse, only counts >= 2)

---

## Active Items

<!-- This section is kept for backwards compatibility. The authoritative source is .flowception/session-*.yaml -->

- @id: [IDLE]
  @state: idle
  @branch: [NONE]