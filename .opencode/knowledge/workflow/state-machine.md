---
domain: workflow
tags: [fsm, state-machine, flow, work-tracking, yaml, flowr]
last-updated: 2026-04-26
---

# State Machine Workflow

## Key Takeaways

- Flows are FSMs defined in YAML with states, transitions, guards, and exits; design principles: determinism, reachability, termination, single responsibility per state.
- Flow definitions are static YAML in `.flowr/flows/`; session files in `.flowr/sessions/` track dynamic state; agents read flows for what to do and sessions for what is active.
- Transitions are atomic: actor sends trigger + evidence, library validates against contracts, session updates and persists only on success.
- The filesystem is the source of truth; if session state and filesystem disagree, update the session to match.
- `exits` is always required — it declares a flow's contract with parent flows; `when` guards are always explicit, no inheritance.

## Concepts

**FSM Fundamentals**: A finite state machine consists of states, transitions, guards, and exits. Design principles: determinism, reachability, termination, single responsibility per state. Every `next` target resolves to either a state id (internal transition) or an exit name (subflow exit). The library validates this at load time.

**YAML Flow and Session Pattern**: Flow definitions are static YAML files in `.flowr/flows/` — only the stakeholder may modify them. Session files in `.flowr/sessions/` are dynamic work trackers updated by agents at every transition. Agents read flow files to know what to do, read session files to know what is active, and write only to session files during normal operation.

**Transition Protocol**: Transitions are atomic. The actor sends a trigger plus evidence. The library validates: transition exists from current state, evidence keys match, each `when` condition is satisfied. Valid transitions update session state and persist. Invalid transitions return a warning with no state change.

**Filesystem Is Source of Truth**: If session state and filesystem disagree, update the session to match the filesystem. The filesystem is authoritative; the session file is a cache.

**Exits and Contracts**: Every flow declares `exits` — the list of ways it can terminate. Parent flows reference these exit names in their `next` maps. This creates a typed contract between flows. Adding a new exit is a minor version bump; removing or renaming one is a major breaking change.

## Content

### Flow Definition Format (v1)

```yaml
flow: feature-flow
version: 1.2.0
params: [feature_slug, branch_name]
exits: [complete, blocked, cancelled]
attrs:
  description: "Main workflow for feature development"

states:
  - id: idle
    next:
      discover: step-1-scope
      select_feature: step-1-scope

  - id: step-1-scope
    flow: scope-cycle
    flow-version: "^1"
    next:
      complete: step-2-arch
      blocked: idle

  - id: step-2-arch
    next:
      approved:
        to: step-3-working
        when: { all_tests_pass: "==true", coverage: ">=80%" }
      needs_rework: step-3-working

  - id: step-3-working
    next:
      review_ready:
        to: step-4-ready
        when: { status: "~=pass" }
      cancel: cancelled

  - id: step-4-ready
    attrs:
      agent: system-architect
    next:
      approved: step-5-ready
      rejected: step-3-working

  - id: step-5-ready
    flow: merge-cycle
    flow-version: "^1"
    next:
      merged: step-5-complete
      rejected: step-3-working
      cancelled: step-3-working
```

### Top-Level Fields

| Field | Required | Description |
|-------|----------|-------------|
| `flow` | yes | Unique name string, used for subflow references |
| `version` | yes | Semver (e.g., `1.2.0`) |
| `params` | no | List of parameter names this flow expects (plain strings) |
| `exits` | yes | List of exit names — the contract this flow offers to parent flows |
| `attrs` | no | Opaque dict for project-specific data; the library ignores this entirely |
| `states` | yes | Ordered list of state objects; first state is the initial state |

### State Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Unique identifier within this flow |
| `next` | yes* | Trigger → target mapping; required unless the state only references exits |
| `flow` | no | If present, makes this state a subflow invocation |
| `flow-version` | no | Semver constraint for the referenced flow (e.g., `"^1"`) |
| `attrs` | no | Opaque dict for state-specific data; overrides/extends flow-level attrs |
| `when` | no | Guard conditions on a transition (see Transition Format) |

*States must have `next` or be referenced only by exit targets.

### Transition Format (`next` values)

Three forms:

| Form | Syntax | Description |
|------|--------|-------------|
| Simple | `approved: step-5` | String target, no conditions |
| Guarded | `approved: { to: step-5, when: {...} }` | Mapping with conditions |
| Mixed | Both in same `next` | Simple and guarded targets coexist |

Guarded transitions use `when` — a dict of condition expressions, AND-combined. No inheritance: every condition must be explicitly declared.

### Exit System

- `exits` is a flat list at flow level, always required
- Any state can reference an exit name in its `next` map: `cancel: cancelled`
- The library resolves `next` targets at load time: found in states → internal transition; found in exits → subflow exit
- Every `next` target must resolve to either a state id or an exit name (never neither)
- Multiple exits can map to the same parent state: `rejected: step-3` / `cancelled: step-3`

### Condition Syntax

The `when` dict uses expression strings as values:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==value` | Equality match | `==true`, `==pass` |
| `!=value` | Inequality match | `!=false` |
| `>=N` | Greater than or equal | `>=80%` (compares 80) |
| `<=N` | Less than or equal | `<=5` |
| `>N` | Greater than | `>0` |
| `<N` | Less than | `<3` |
| `~=value` | Approximate match | `~=pass` — strings: case-insensitive substring; numbers: within 5% tolerance |

Numeric portion is extracted before comparison. Plain strings without operators are treated as `==value`. Evidence keys must exactly match `when` keys — closed schema, no extra or missing keys.

### Subflow Model

- `flow: <name>` on a state makes it a subflow (no `type` field needed)
- `flow-version: "^1"` constrains which versions are compatible
- Parent `next` keys must match child's `exits` list exactly
- Subflows use a call-stack mechanism: push on entry, pop on exit
- Context is isolated: only current flow visible in responses

### Semver for Flows

| Change | Version impact |
|--------|---------------|
| Adding a new exit | Minor bump |
| Adding states or requirements | Patch (non-breaking) |
| Removing or renaming exits | Major (breaking) |

Parent flows constrain compatibility: `flow-version: "^1"`

### Validation Rules (Load-Time)

1. Every `next` target resolves to a state id or an exit name
2. Parent `next` keys match child's `exits` list exactly
3. No cross-flow cycles (DFS detection)
4. Exit names in `exits` must have at least one state referencing them

### Session Format

```yaml
session: a1b2c3d4-...
started: "2026-04-25T10:00:00Z"
current:
  flow: arch-cycle
  state: interview
  stack:
    - flow: feature-flow
      state: step-2-arch
params:
  feature-flow:
    feature_slug: user-auth
    branch_name: feat/user-auth
  arch-cycle:
    feature_slug: user-auth
    branch_name: feat/user-auth
transitions:
  feature-flow:
    "idle->step-1-scope": 2
```

Fields: `session` (UUID), `started` (ISO 8601), `current` (flow + state), `stack` (for subflows; push on entry, pop on exit), `params` (per-flow variable namespace), `transitions` (sparse; only counts >= 2 are persisted).

### Transition Protocol

1. Actor sends a **trigger** (transition name) plus **evidence** (key-value dict matching `when` keys).
2. Library validates: transition exists from current state, evidence keys match, each condition expression is satisfied.
3. **Valid**: session `current` updates, transition counter increments, session file persisted.
4. **Invalid**: warning returned, no state change. Actor must resolve the guard failure.

Transitions are atomic — session file updates, then commit, then proceed.

### Self-Healing Rule

If session state and filesystem disagree, the filesystem is the source of truth. Update the session file to match. Never "correct" the filesystem to match session state.

Detection rules are ordered: earlier rules eliminate more states quickly. Each rule is a single, fast filesystem or git command. No rule requires running tests.

### Design Principles

1. **Immutable loaded flows** — edits produce copies
2. **Closed evidence schema** — keys must exactly match
3. **Isolated subflow context** — only current flow visible
4. **Session truth assumption** — filesystem wins over session
5. **Thin enforcement** — validate only, no execution
6. **No auto-rollback** — no transition limits (counts recorded, not enforced)

### v1 Out of Scope

- Jinja/string templating or `${param}` interpolation
- `type` field on states (removed; `flow` presence implies subflow)
- Named requirement groups (removed; `when` is always inline)
- Condition inheritance (removed; all conditions explicit)
- Auto-rollback, transition attempt limits, session history
- Parallel/fork-join states
- Action execution

## Related

- [[git/protocol]] — git operations that correspond to state transitions
- [[requirements/wsjf]] — scoring model for selecting the next work item