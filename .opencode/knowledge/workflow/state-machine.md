---
domain: workflow
tags: [fsm, state-machine, flow, work-tracking, yaml, flowception]
last-updated: 2026-04-26
---

# State Machine Workflow

## Key Takeaways

- Flows are FSMs with states, transitions, guards, actions, and owners; design principles: determinism, reachability, termination, single responsibility per state, WIP limits, and filesystem observability.
- Flow definitions are static YAML in `docs/flows/`; session files in `.flowception/` track dynamic state; agents read flows for what to do and sessions for what is active.
- Transitions are atomic: actor sends trigger + evidence, library validates against contracts, session updates and persists only on success.
- The filesystem is the source of truth; if session state and filesystem disagree, update the session to match.

## Concepts

**FSM Fundamentals**: A finite state machine consists of states (discrete stages, exactly one at a time), transitions (rules for moving between states), guards (conditions that must be true for a transition to fire), actions (work performed in a state or during a transition), and owners (the role responsible for executing a state). Design principles: determinism, reachability, termination, single responsibility per state, WIP limits, and observability from the filesystem.

**YAML Flow and Session Pattern**: Flow definitions are static YAML files in `docs/flows/` — only the stakeholder may modify them. Session files in `.flowception/` are dynamic work trackers updated by agents at every transition. Agents read flow files to know what to do, read session files to know what is active and where it is, and write only to session files during normal operation.

**Transition Protocol**: Transitions are atomic. The actor sends a trigger (transition name) plus evidence (key-value dict matching the target state's `requires` contracts). The library validates: transition exists from current state, evidence keys match, each contract expression is satisfied. Valid transitions update session state and persist. Invalid transitions return a warning with no state change.

**Filesystem Is Source of Truth**: If session state and filesystem disagree, update the session to match the filesystem. The filesystem (feature file locations, git state) is authoritative; the session file is a cache.

## Content

### FSM Fundamentals

A finite state machine (FSM) consists of:

1. **States** — discrete stages a work item can be in (exactly one at a time)
2. **Transitions** — rules for moving from one state to another
3. **Guards** — conditions that must be true for a transition to fire
4. **Actions** — work performed while in a state or during a transition
5. **Owners** — the role responsible for executing a state

Design principles: determinism (one transition per guard), reachability, termination, single responsibility per state, WIP limits, observability from filesystem, minimal tracked variables.

### YAML Flow Pattern

Flow definitions are YAML files in `docs/flows/` (e.g. `feature-flow.yaml`). Session tracking uses flowception-format YAML in `.flowception/`. FLOW.md and WORK.md are replaced by these YAML artifacts.

- **Flow file** (`docs/flows/*.yaml`) — static state machine definition. Only the stakeholder may modify it.
- **Session file** (`.flowception/<uuid>.yaml`) — dynamic work tracker, updated by agents at every transition.

Agents read flow files to know **what to do**. They read session files to know **what is active and where it is**. They write only to session files during normal operation.

### Flow Definition Format

```yaml
flow: feature-flow
params:
  - feature_slug
  - branch_name
states:
  - id: idle
    agent: product-owner
    type: normal
    next:
      select-feature: step-1-scope
      discover: step-1-scope

  - id: step-1-scope
    agent: product-owner
    type: subflow
    flow: scope-cycle
    params:
      feature_slug: feature_slug
    next:
      complete: step-2-arch
      blocked: idle

  - id: step-2-arch
    agent: system-architect
    type: subflow
    flow: arch-cycle
    params:
      feature_slug: feature_slug
      branch_name: branch_name
    next:
      complete: step-3-working
      blocked: step-1-scope
exits:
  - complete
  - blocked
```

Top-level keys: `flow` (name string), `params` (list; plain string = required, `key: default` = optional), `states` (ordered list of state objects), `exits` (list of exit state ids for subflow returns).

### State Definition

Each state object has these fields:

| Field | Required | Description |
|---|---|---|
| `id` | yes | Unique state identifier within this flow |
| `agent` | no | Role responsible for this state (informational) |
| `type` | no | `normal` or `subflow` (default: `normal`) |
| `requires` | no | Contract dict (can be `{}`); see Contract Syntax |
| `params` | no | Parameters available at or passed to this state |
| `flow` | no* | Name of the referenced flow. **Required on subflow states** |
| `next` | yes | Trigger name → target state id mapping |

### Contract Syntax

The `requires` field uses expression strings as values:

| Expression | Meaning |
|---|---|
| `==value` | Equality match |
| `!=value` | Inequality match |
| `>=N` | Greater than or equal |
| `<=N` | Less than or equal |
| `>N` | Greater than |
| `<N` | Less than |

Numeric portion is extracted before comparison — values like `>=80%` compare against `80`. Plain strings without operators are treated as `==value`.

Evidence keys must exactly match `requires` keys. No extra keys accepted, no missing keys allowed.

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

1. Actor sends a **trigger** (transition name) plus **evidence** (key-value dict matching the target state's `requires`).
2. Library validates: transition exists from current state, evidence keys match, each contract expression is satisfied.
3. **Valid**: session `current` updates, transition counter increments, session file persisted.
4. **Invalid**: warning returned, no state change. Actor must resolve the guard failure.

Transitions are atomic — session file updates, then commit, then proceed.

### Self-Healing Rule

If session state and filesystem disagree, the filesystem is the source of truth. Update the session file to match. Never "correct" the filesystem to match session state.

Detection rules are ordered: earlier rules eliminate more states quickly. Each rule is a single, fast filesystem or git command. No rule requires running tests.

## Related

- [[git/protocol]] — git operations that correspond to state transitions
- [[requirements/wsjf]] — scoring model for selecting the next work item