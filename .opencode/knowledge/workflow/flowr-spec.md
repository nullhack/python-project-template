---
domain: workflow
tags: [fsm, state-machine, flow, yaml, flowr, transitions, conditions, session, config]
last-updated: 2026-05-02
---

# Flowr Specification

## Key Takeaways

- Define flows as FSMs in YAML with states, transitions, guards, and exits; the flow YAML is the single source of truth for workflow routing.
- Declare `exits` on every flow as its contract with parent flows; parent `next` keys must match child `exits` exactly.
- Use `conditions` blocks on states to define named condition groups; reference them in transitions with `when`.
- Guarded transitions use `when` dicts with expression strings (`==true`, `>=80%`, `~=100`); conditions are AND-combined with no inheritance.
- Carry runtime metadata in state-level `attrs` (agent, skills, input_artifacts, etc.); `attrs` is opaque to the engine.
- Sessions track workflow progress (flow, state, call stack) as YAML files in `.flowr/sessions/` with atomic writes; `--session` on check/next/transition resolves flow/state automatically.
- Configuration reads `[tool.flowr]` from `pyproject.toml` (flows_dir, sessions_dir, default_flow, default_session); CLI flags override pyproject.toml which overrides defaults.
- Flow name resolution: commands accept short names (e.g., `planning-flow`) resolved from the configured flows directory, or full file paths.
- Immutable loaded flows, closed evidence schema, isolated subflow context, filesystem wins over session on conflict.

## Concepts

**YAML Flow Definitions**: Flows are finite state machines defined in `.flowr/flows/` as YAML files. Each flow has a name, version, exits, and states. The first state is the initial state. The flow YAML is the single source of truth for what happens at each state; agents read it to determine routing; skills define how to execute.

**Exits as Contracts**: Every flow declares `exits` — the list of ways it can terminate. Parent flows reference these exit names in their `next` maps. This creates a typed contract between flows. Adding a new exit is a minor version bump; removing or renaming one is a major breaking change.

**Conditions and Guards**: States may define `conditions` blocks containing named condition groups. Transitions reference these groups with `when` to create guarded transitions. Condition expressions use operators like `==value`, `!=value`, `>=N`, `<=N`, `>N`, `<N`, `~=value`. All conditions in a `when` dict are AND-combined with no inheritance — every condition must be explicit.

**State Attrs**: State-level `attrs` carry runtime metadata that the flowr engine ignores but agents and skills read. Common keys: `description`, `owner`, `skills`, `input_artifacts`, `edited_artifacts`, `output_artifacts`. State-level `attrs` replace flow-level attrs entirely (no merge, no deep merge).

**Subflow Invocation**: A state with a `flow:` field becomes a subflow invocation. The parent's `next` keys must match the child's `exits` exactly. Subflows use a call-stack mechanism: push on entry, pop on exit. Context is isolated: only the current flow is visible. Cross-flow cycles are forbidden.

## Content

### Top-Level Fields

| Field | Required | Description |
|---|---|---|
| `flow` | yes | Unique name string, used for subflow references |
| `version` | yes | Semver (e.g., `1.2.0`) |
| `params` | no | List of parameter declarations |
| `exits` | yes | List of exit names — the contract this flow offers to parent flows |
| `attrs` | no | Opaque dict for project-specific data; the library ignores this entirely |
| `states` | yes | Ordered list of state objects; first state is the initial state |

### State Fields

| Field | Required | Description |
|---|---|---|
| `id` | yes | Unique identifier within this flow |
| `next` | yes* | Trigger → target mapping; required unless exit-only |
| `flow` | no | If present, makes this state a subflow invocation |
| `flow-version` | no | Semver constraint for the referenced flow (e.g., `"^1"`) |
| `attrs` | no | Opaque dict; replaces flow-level attrs entirely (no merge) |
| `conditions` | no | Named condition groups for guarded transitions |

*States must have `next` or be referenced only by exit targets.

### Transition Format (`next` values)

| Form | Syntax | Description |
|---|---|---|
| Simple | `approved: step-5` | String target, no conditions |
| Guarded | `approved: { to: step-5, when: {...} }` | Mapping with conditions |
| Mixed | Both in same `next` | Simple and guarded targets coexist |

### Condition Syntax (`when` values)

| Operator | Meaning | Example |
|---|---|---|
| `==value` | Equality match | `==true`, `==BASELINED` |
| `!=value` | Inequality match | `!=false` |
| `>=N` | Greater than or equal | `>=80%` (compares 80) |
| `<=N` | Less than or equal | `<=5`, `<=8` |
| `>N` | Greater than | `>0` |
| `<N` | Less than | `<3` |
| `~=value` | Approximate numeric match (5% tolerance) | `~=100` |

Numeric portion is extracted from both condition and evidence values before comparison. Plain strings without operators are treated as `==value`. Evidence keys must exactly match `when` keys — closed schema, no extra or missing keys. `~=` applies only to numeric values; it is not valid for string matching.

### Conditions Block

States may define a `conditions` block (sibling of `attrs` and `next`) containing named condition groups:

```yaml
conditions:
  invest_passed:
    independent: ==true
    negotiable: ==true
    valuable: ==true
next:
  done:
    to: bdd-features
    when: invest_passed
```

Named condition references in `when` clauses must resolve to a key in the same state's `conditions` block. Unknown references are validation errors.

### Exit System

- `exits` is a flat list at flow level, always required
- Any state can reference an exit name in its `next` map
- A `next` target that matches both a state id and an exit name is a validation error (ambiguous reference)
- Every `next` target must resolve to either a state id or an exit name
- Multiple exits can map to the same parent state

### Subflow Model

- `flow: <name>` on a state makes it a subflow (no `type` field needed)
- `flow-version: "^1"` constrains which versions are compatible
- Parent `next` keys must match child's `exits` list exactly
- Subflows use a call-stack: push on entry, pop on exit
- Context is isolated: only current flow visible
- Cross-flow cycles are forbidden (detected via DFS at load time)

### Semver Conventions

| Change | Version impact |
|---|---|
| Adding a new exit | Minor bump |
| Adding states or requirements | Patch (non-breaking) |
| Removing or renaming exits | Major (breaking) |

### Validation Rules (Load-Time)

Violations are categorized by severity: **MUST** (blocking errors) and **SHOULD** (non-blocking warnings).

1. (MUST) Every `next` target resolves to a state id or an exit name
2. (MUST) No `next` target is ambiguous (matches both a state id and an exit name)
3. (MUST) Parent `next` keys match child's `exits` list exactly
4. (MUST) No cross-flow cycles (DFS detection)
5. (SHOULD) Exit names in `exits` are referenced by at least one state transition
6. (MUST) Named condition references in `when` must resolve to the same state's `conditions` block
7. (SHOULD) All defined condition groups are referenced by at least one transition
8. (MUST) Flow definition has at least one exit
9. (MUST) Flow definition has at least one state
10. Params without defaults must be provided at invocation time

### Session Model

Sessions persist workflow progress as YAML files in `.flowr/sessions/` with atomic writes (temp-file-then-rename). Each session tracks:

| Field | Description |
|-------|-------------|
| `flow` | Current flow name |
| `state` | Current state id |
| `name` | Session identifier (used as filename stem) |
| `created_at` | ISO 8601 timestamp |
| `updated_at` | ISO 8601 timestamp (updated on every transition) |
| `stack` | List of `{flow, state}` frames for subflow nesting |
| `params` | Per-flow parameter overrides |

Subflow entry pushes a `SessionStackFrame(flow, state)` onto the stack and updates the session's flow/state to the subflow. Subflow exit pops the frame and restores the parent flow/state.

### Configuration

flowr reads `[tool.flowr]` from `pyproject.toml`. Resolution priority: CLI flags > pyproject.toml > defaults.

| Key | Default | Description |
|-----|---------|-------------|
| `flows_dir` | `.flowr/flows` | Directory containing flow YAML files |
| `sessions_dir` | `.flowr/sessions` | Directory for session YAML files |
| `default_flow` | `main-flow` | Flow name used when none specified |
| `default_session` | `default` | Session name used with bare `--session` |

### Design Principles

1. **Immutable loaded flows** — edits produce copies
2. **Closed evidence schema** — keys must exactly match
3. **Isolated subflow context** — only current flow visible
4. **Session truth assumption** — filesystem wins over session on conflict
5. **Thin enforcement** — validate only, no execution
6. **No auto-rollback** — no transition limits
7. **Atomic session writes** — temp-file-then-rename prevents corruption

## Related

- [[agent-design/principles]]
- [[skill-design/principles]]
- [[knowledge-design/principles]]