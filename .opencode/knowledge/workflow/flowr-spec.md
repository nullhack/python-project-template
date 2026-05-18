---
domain: workflow
tags: [fsm, state-machine, flow, yaml, flowr, transitions, conditions, session, config]
last-updated: 2026-05-06
---

# Flowr Specification

## Key Takeaways

- Define flows as FSMs in YAML with states, transitions, guards, and exits; the flow YAML is the single source of truth for workflow routing.
- Declare `exits` on every flow as its contract with parent flows; parent `next` keys must match child `exits` exactly.
- Use `conditions` blocks on states to define named condition groups; reference them in transitions with `when`.
- Guarded transitions use `when` with expression strings (`==true`, `>=80%`); `when` accepts a dict, a named ref string, or a list mixing both; conditions are AND-combined with no inheritance.
- Carry runtime metadata in state-level `attrs` (agent, skills, input_artifacts, etc.); `attrs` is opaque to the engine and replaces flow-level attrs entirely (no merge).
- All CLI commands output **JSON by default** (structured, machine-parseable). Use `--text` flag for human-readable plain text.
- `next` command shows **all** transitions with status markers (`"open"` / `"blocked"`) and condition hints for blocked transitions.
- Sessions track workflow progress (flow, state, call stack) as YAML files in `.cache/sessions/` with atomic writes; `--session` on check/next/transition resolves flow/state automatically.
- Subflow exit names resolve through the parent flow's transition map (not used directly as state IDs). Enables subflow chaining and recursive entry up to 3 levels.
- Configuration reads `[tool.flowr]` from `pyproject.toml` (flows_dir, sessions_dir, default_flow, default_session); CLI flags override pyproject.toml which overrides defaults.
- Flow name resolution: commands accept short names (e.g., `architecture-flow`) resolved from the configured flows directory, or full file paths.
- Immutable loaded flows, closed evidence schema, isolated subflow context, filesystem wins over session on conflict. Extension fields (non-reserved keys) are allowed and not interpreted by the validator.

## Concepts

**YAML Flow Definitions**: Flows are finite state machines defined in `.flowr/flows/` as YAML files. Each flow has a name, version, exits, and states. The first state is the initial state. The flow YAML is the single source of truth for what happens at each state; agents read it to determine routing; skills define how to execute.

**JSON-First Output**: All CLI commands return JSON by default for machine-parseable structured output. The `--text` flag provides human-readable plain text. JSON output includes structured keys for programmatic extraction: `check` returns `{"id", "attrs", "transitions"}`, `next` returns `{"state", "transitions": [{"trigger", "target", "status", "conditions"}]}`, `transition` returns `{"from", "trigger", "to"}`.

**Exits as Contracts**: Every flow declares `exits`: the list of ways it can terminate. Parent flows reference these exit names in their `next` maps. This creates a typed contract between flows. Adding a new exit is a minor version bump; removing or renaming one is a major breaking change.

**Conditions and Guards**: States may define `conditions` blocks containing named condition groups. Transitions reference these groups with `when` to create guarded transitions. The `when` field accepts three forms: a dict (inline condition-map), a string (reference to a named group), or a list (mix of named refs and inline dicts). All conditions are AND-combined. A named ref that does not match a group defined on the same state causes a validation error. Condition expressions use operators `==`, `!=`, `>=`, `<=`, `>`, `<`. Numeric extraction is applied to both sides (e.g., `>=80%` vs `75%` compares 80 vs 75). Plain strings without operators are treated as `==` (implicit equality). No inheritance; every condition is explicit on the transition where it applies.

**State Attrs**: State-level `attrs` carry runtime metadata that the flowr engine ignores but agents and skills read. Common keys: `description`, `owner`, `skills`, `input_artifacts`, `edited_artifacts`, `output_artifacts`. State-level `attrs` replace flow-level attrs entirely (no merge, no deep merge). The `attrs` field is the designated extension point: implementations should place implementation-specific data inside `attrs` rather than as top-level keys.

**Subflow Invocation**: A state with a `flow:` field becomes a subflow invocation. The parent's `next` keys must match the child's `exits` exactly. Subflows use a call-stack mechanism: push on entry, pop on exit. Context is isolated: only the current flow is visible. Cross-flow cycles are forbidden.

**Subflow Exit Resolution (v1.0.0)**: Exit names resolve through the parent flow's transition map instead of being used directly as state IDs. This enables subflow chaining (atomic exit + re-enter next subflow) and recursive subflow entry up to 3 levels deep (e.g., define-flow → spec-validation-flow). Stack frames record the correct parent state (subflow wrapper, not pre-transition state).

## Content

### Top-Level Fields

| Field | Required | Description |
|---|---|---|
| `flow` | yes | Unique name string, used for subflow references |
| `version` | yes | Semver (e.g., `1.2.0`) |
| `params` | no | List of parameter declarations (strings or `{name, default?}` objects) |
| `exits` | yes | List of exit names: the contract this flow offers to parent flows |
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
| `==value` | Equality match (implicit for plain values) | `==true`, `==BASELINED`, `approved` |
| `!=value` | Inequality match | `!=false` |
| `>=N` | Greater than or equal | `>=80%` (compares 80) |
| `<=N` | Less than or equal | `<=5`, `<=8` |
| `>N` | Greater than | `>0` |
| `<N` | Less than | `<3` |

Numeric portion is extracted from both condition and evidence values before comparison. Plain values without operator prefix are treated as `==` (implicit equality). Evidence keys must exactly match `when` keys (closed schema, no extra or missing keys). Multiple conditions in a `when` dict are AND-combined.

### `when` Forms

The `when` field on a transition accepts three forms:

| Form | Syntax | Description |
|---|---|---|
| Dict | `when: { score: ">=80" }` | Inline condition-map |
| String | `when: quality_gate` | Reference to a named condition group |
| List | `when: [quality_gate, { override: "==yes" }]` | Mix of named refs and inline dicts, AND-combined |

Named refs must resolve to a condition group defined on the same state. Unknown references are validation errors.

### Conditions Block

States may define a `conditions` block (sibling of `attrs` and `next`) containing named condition groups:

```yaml
conditions:
  invest-passed:
    independent: ==true
    negotiable: ==true
    valuable: ==true
next:
  done:
    to: next-state
    when: invest-passed
  partial:
    to: review
    when:
      - invest-passed
      - { override: "==yes" }
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
- Exit names resolve through parent flow's transition map (not used directly as state IDs)
- Subflow chaining: atomic exit + re-enter next subflow without manual state manipulation
- Recursive entry: supports up to 3-level nesting (define-flow → discovery-flow, develop-flow → development-flow, etc.)
- Stack frames record the subflow wrapper state (not the pre-transition state)
- `.yaml` extension fallback: flow references without extension are resolved automatically
- `session init` auto-enters subflow when first state has a `flow:` field

### Semver Conventions

| Change | Version impact |
|---|---|
| Adding a new exit | Minor bump |
| Adding states or requirements | Patch (non-breaking) |
| Removing or renaming exits | Major (breaking) |

### Validation Rules (Load-Time)

A conforming validator MUST check all of the following at load time:

1. Every `next` target resolves to a state id or exit name
2. No `next` target is ambiguous (matches both a state id and an exit name)
3. Parent `next` keys match child `exits` exactly
4. No cross-flow cycles (detected via DFS)
5. Exit names in `exits` are referenced by at least one state
6. Named condition references in `when` resolve to a group defined on the same state
7. Params without defaults are provided at flow invocation time

### Conformance Levels

| Level | Meaning | Requirement |
|---|---|---|
| MUST | Required for all conforming implementations | Immutable loaded flows, closed evidence schema, validation rules |
| SHOULD | Recommended but optional | Filesystem wins over session cache on conflict, semver for flows |
| MAY | Optional extension | Per-state attrs, flow params, Mermaid export |

### Extension Fields and Reserved Keys

A flow definition MAY contain fields not specified in the specification. Such extension fields are not interpreted by a conforming validator. The reserved keys are: `flow`, `version`, `params`, `exits`, `attrs`, `states`, `id`, `next`, `to`, `when`, `conditions`, `flow-version`. Implementations MUST NOT assign semantics to reserved keys beyond what the specification defines. Implementation-specific data SHOULD be placed inside `attrs`.

### Session Model

Sessions persist workflow progress as YAML files in `.cache/sessions/` with atomic writes (temp-file-then-rename). Each session tracks:

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
| `sessions_dir` | `.cache/sessions` | Directory for session YAML files |
| `default_flow` | `define-flow` | Flow name used when none specified |
| `default_session` | `default` | Session name used with bare `--session` |

### Design Principles

1. **Immutable loaded flows**: edits produce copies
2. **Closed evidence schema**: keys must exactly match
3. **Isolated subflow context**: only current flow visible
4. **Session truth assumption**: filesystem wins over session on conflict
5. **Thin enforcement**: validate only, no execution
6. **No auto-rollback**: no transition limits
7. **Atomic session writes**: temp-file-then-rename prevents corruption
8. **JSON-first output**: structured data by default; `--text` for human-readable
9. **Complete transition visibility**: `next` shows all transitions with status markers
10. **Extension-friendly**: non-reserved keys are ignored by the validator; `attrs` is the designated extension point

## Related

- [[agent-design/principles]]
- [[skill-design/principles]]
- [[knowledge-design/principles]]