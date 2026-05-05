---
domain: workflow
tags: [flowr, cli, commands, transitions, evidence, session, config]
last-updated: 2026-05-05
---

# Flowr Operations

## Key Takeaways

- All commands output **JSON by default** (machine-parseable). Use `--text` for human-readable output.
- Use `python -m flowr check --session` to inspect current state's attrs, owner, skills, and transitions.
- Use `python -m flowr next --session` to see **all** transitions with status markers (`"open"` / `"blocked"`) and condition hints.
- Use `python -m flowr transition <trigger> --session --evidence key=value` to advance to the next state.
- Use `python -m flowr check --session <trigger>` to see the conditions guarding a specific transition.
- Use `python -m flowr session init <flow> --name <name>` to create a session; `session init` auto-enters subflow when first state has a `flow:` field.
- Set evidence based on work completed before advancing — guarded transitions will not pass without it.
- Always activate the virtual environment first: `source .venv/bin/activate`.

## Concepts

**JSON-First Output**: All flowr commands output JSON by default. Parse the structured output to extract state metadata, transition status, and conditions programmatically. Use `--text` flag for human-readable plain text when needed.

**State Entry**: Before starting work, inspect the current state with `check --session` to confirm the owner, skills, input artifacts, output artifacts, and available transitions. The output is a JSON object with `id`, `attrs`, and `transitions` keys.

**Enhanced `next` Output**: The `next` command shows **all** transitions (open and blocked) with status markers. Each transition has `trigger`, `target`, `status` (`"open"` or `"blocked"`), and `conditions` (null if unguarded, or a dict of condition expressions). This lets you identify what evidence is needed to unblock guarded transitions.

**Evidence**: Some transitions are guarded by conditions (e.g., `feature_accepted: ==ACCEPTED`, `all_ids_have_stubs: ==true`). Set evidence with `--evidence key=value` or `--evidence-json '{"key":"value"}'` when advancing. If a transition is guarded and evidence is not set, the transition will fail.

**Choosing a Path**: After completing work, use `next` with your evidence. Transitions with `"status": "open"` are available; `"status": "blocked"` transitions show which conditions need evidence. Choose the path that matches your work outcome.

**Flow Name Resolution**: Commands accept short flow names (e.g., `architecture-flow`) or full file paths. Short names are resolved by searching the configured flows directory.

**Sessions**: Sessions persist workflow progress (current flow, state, call stack for subflows) as YAML files in `.flowr/sessions/`. Use `--session <name>` on check/next/transition to resolve flow and state from the session. `transition --session` auto-updates the session after advancing. `session init` auto-enters subflow when the first state has a `flow:` field.

**Subflow Exit Resolution**: In flowr ≥0.5, exit names resolve through the parent flow's transition map rather than being used directly as state IDs. This enables subflow chaining (e.g., discovery-flow → architecture-flow) and recursive subflow entry (3-level nesting) without manual state manipulation.

**Configuration**: flowr reads `[tool.flowr]` from `pyproject.toml`. CLI flags override pyproject.toml which overrides defaults. Use `flowr config` to inspect resolved values as a JSON array of key/value/source objects.

## Content

### Command Reference

All commands require the virtual environment: `source .venv/bin/activate`

All commands output JSON by default. Add `--text` for human-readable output.

| Command | Purpose |
|---------|---------|
| `python -m flowr validate [<flow>]` | Validate flow definition(s). Returns `{"valid", "violations"}` |
| `python -m flowr validate --session <name>` | Validate the current (sub)flow from session |
| `python -m flowr states <flow>` | List all state ids in a flow as JSON array |
| `python -m flowr states --session <name>` | List states in the current (sub)flow from session |
| `python -m flowr check <flow> <state>` | Show state attrs, owner, skills, and transitions |
| `python -m flowr check <flow> <state> <target>` | Show conditions for a specific transition |
| `python -m flowr check --session <name>` | Show current session state (read-only) |
| `python -m flowr check --session <name> <trigger>` | Show conditions for a specific transition via session |
| `python -m flowr next <flow> <state> [--evidence key=value]` | Show all transitions with status markers |
| `python -m flowr next --session <name> [--evidence key=value]` | Show transitions from session state |
| `python -m flowr transition <flow> <state> <trigger> [--evidence key=value]` | Advance to the next state |
| `python -m flowr transition <trigger> --session <name> [--evidence key=value]` | Advance using session (auto-updates) |
| `python -m flowr mermaid <flow>` | Export flow as Mermaid diagram |
| `python -m flowr config` | Show resolved configuration as JSON array |

### Session Commands

| Command | Purpose |
|---------|---------|
| `python -m flowr session init <flow> [--name <name>]` | Create session at initial state; auto-enters subflow if first state has `flow:` |
| `python -m flowr session show [--name <name>] [--format yaml\|json]` | Display session state, call stack, params |
| `python -m flowr session set-state <state> [--name <name>]` | Manually update session state (validates state exists in flow) |
| `python -m flowr session list [--format yaml\|json]` | List all sessions |

### Output Formats

**`check`** returns:
```json
{
  "id": "feature-selection",
  "attrs": {
    "description": "...", "owner": "PO", "git": "main",
    "skills": ["select-feature"], "in": [...], "out": [...]
  },
  "transitions": ["selected", "needs_architecture", "no_features"]
}
```

**`next`** returns all transitions with status markers:
```json
{
  "state": "feature-breakdown",
  "transitions": [
    {
      "trigger": "done",
      "target": "feature-examples",
      "status": "blocked",
      "conditions": {
        "independent": "==no_shared_data_or_side_effects",
        "negotiable": "==scope_negotiated",
        "valuable": "==user_value_clear"
      }
    },
    {
      "trigger": "needs_respecification",
      "target": "feature-breakdown",
      "status": "open",
      "conditions": null
    }
  ]
}
```

**`check <target>`** returns transition conditions:
```json
{
  "from": "feature-breakdown",
  "target": "done",
  "conditions": {
    "independent": "==no_shared_data_or_side_effects",
    "negotiable": "==scope_negotiated"
  }
}
```

**`transition`** returns the computed state change:
```json
{
  "from": "feature-selection",
  "trigger": "selected",
  "to": "feature-breakdown"
}
```

**`config`** returns resolved configuration with sources:
```json
[
  {"key": "flows_dir", "value": ".flowr/flows", "source": "pyproject.toml"},
  {"key": "default_session", "value": "default", "source": "default"}
]
```

### Configuration

flowr reads configuration from `[tool.flowr]` in `pyproject.toml`, falling back to defaults:

| Key | Default | Description |
|-----|---------|-------------|
| `flows_dir` | `.flowr/flows` | Directory containing flow YAML files |
| `sessions_dir` | `.flowr/sessions` | Directory for session YAML files |
| `default_flow` | `main-flow` | Flow name used when none specified |
| `default_session` | `default` | Session name used when `--session` is given without a value |

CLI `--flows-dir` overrides `pyproject.toml` which overrides defaults.

### Evidence Syntax

Evidence can be provided two ways:

- `--evidence key=value` — multiple flags for individual pairs
- `--evidence-json '{"key":"value"}'` — single JSON object for all pairs

Condition operators: `==value`, `!=value`, `>=N`, `<=N`, `>N`, `<N`, `~=value` (approximate numeric match within 5%).

### Workflow Pattern

Every state follows the same pattern:

1. **Enter**: `python -m flowr check --session` — confirm owner, skills, attrs, and transitions. Parse `attrs.owner` to determine dispatch target.
2. **Work**: Execute the skill, reading `in` artifacts and writing `out` artifacts.
3. **Evidence**: Set any evidence required by guarded transitions based on work completed.
4. **Choose**: `python -m flowr next --session --evidence key=value` — see all transitions with status. `"status": "open"` transitions are available; `"status": "blocked"` shows which conditions need evidence.
5. **Advance**: `python -m flowr transition <trigger> --session --evidence key=value` — move to the next state.

### Session-Based Workflow

For ongoing work, use sessions to track progress:

1. **Init**: `python -m flowr session init <flow> --name <name>` — create session at initial state (auto-enters subflow if first state has `flow:`).
2. **Check**: `python -m flowr check --session` — inspect current state (read-only).
3. **Work**: Execute the skill for the current state.
4. **Advance**: `python -m flowr transition <trigger> --session --evidence key=value` — transition and auto-update session.

### Session Protocol Integration

- The `owner` field from `check` output determines which agent to dispatch to (PO → product-owner, SE → software-engineer, SA → system-architect, DE → domain-expert, R → reviewer, Design Agent → design-agent, Setup Agent → setup-agent).
- The `skills` field lists which skills to load and execute.
- The `in` and `out` fields define the artifact contract — what you may read and what you may write.
- Do not skip the check step or guess transitions. Always verify the current state before starting work.

## Related

- [[workflow/flowr-spec]]