---
domain: workflow
tags: [flowr, cli, commands, transitions, evidence, session, config]
last-updated: 2026-05-02
---

# Flowr Operations

## Key Takeaways

- Use `python -m flowr check <flow> <state>` to inspect a state's attrs, owner, skills, and transitions at state entry.
- Use `python -m flowr next <flow> <state> --evidence key=value` to see which transitions pass given your evidence.
- Use `python -m flowr transition <flow> <state> <trigger> --evidence key=value` to advance to the next state.
- Use `python -m flowr check <flow> <state> <target>` to see the conditions guarding a specific transition.
- Use `python -m flowr session init <flow>` to create a session that tracks progress; use `--session` on check/next/transition to resolve flow and state automatically.
- Use `python -m flowr config` to show resolved configuration (flows_dir, sessions_dir, default_flow, default_session) with source tracking.
- Set evidence based on work completed before advancing — guarded transitions will not pass without it.
- Always activate the virtual environment first: `source .venv/bin/activate`.

## Concepts

**State Entry**: Before starting work, inspect the current state to confirm the owner, skills, input artifacts, output artifacts, and available transitions.

**Evidence**: Some transitions are guarded by conditions (e.g., `feature_accepted: ==ACCEPTED`, `all_ids_have_stubs: ==true`). Set evidence with `--evidence key=value` or `--evidence-json '{"key":"value"}'` when advancing. If a transition is guarded and evidence is not set, the transition will fail.

**Choosing a Path**: After completing work, use `next` with your evidence to see which transitions are available. Choose the path that matches your work outcome. Do not guess transition names — check first.

**Flow Name Resolution**: Commands accept short flow names (e.g., `architecture-flow`) or full file paths (e.g., `.flowr/flows/architecture-flow.yaml`). Short names are resolved by searching the configured flows directory.

**Sessions**: Sessions persist workflow progress (current flow, state, call stack for subflows) as YAML files in `.flowr/sessions/`. Use `--session <name>` on check/next/transition to resolve flow and state from the session. `transition --session` auto-updates the session after advancing.

**Configuration**: flowr reads `[tool.flowr]` from `pyproject.toml` with keys: `flows_dir`, `sessions_dir`, `default_flow`, `default_session`. CLI flags override pyproject.toml which overrides defaults. Use `flowr config` to inspect resolved values.

## Content

### Command Reference

All commands require the virtual environment: `source .venv/bin/activate`

| Command | Purpose | Example |
|---------|---------|---------|
| `python -m flowr validate <flow>` | Validate a flow definition | `python -m flowr validate architecture-flow` |
| `python -m flowr states <flow>` | List all states in a flow | `python -m flowr states planning-flow` |
| `python -m flowr check <flow> <state>` | Show state attrs, owner, skills, and transitions | `python -m flowr check planning-flow feature-selection` |
| `python -m flowr check <flow> <state> <target>` | Show conditions for a specific transition target | `python -m flowr check planning-flow feature-selection selected` |
| `python -m flowr next <flow> <state>` | Show which transitions are available (unguarded always shown) | `python -m flowr next planning-flow feature-selection` |
| `python -m flowr next <flow> <state> --evidence key=value` | Show which transitions pass given evidence | `python -m flowr next planning-flow feature-breakdown --evidence independent=true` |
| `python -m flowr transition <flow> <state> <trigger>` | Compute next state for a trigger | `python -m flowr transition planning-flow feature-selection selected` |
| `python -m flowr transition <flow> <state> <trigger> --evidence key=value` | Advance with evidence | `python -m flowr transition planning-flow feature-breakdown done --evidence independent=true valuable=true` |
| `python -m flowr transition <trigger> --session` | Advance using session (auto-resolves flow/state) | `python -m flowr transition done --session --evidence independent=true` |
| `python -m flowr check --session` | Show current session state (read-only) | `python -m flowr check --session` |
| `python -m flowr next --session` | Show available transitions from session state | `python -m flowr next --session --evidence independent=true` |
| `python -m flowr mermaid <flow>` | Export flow as Mermaid diagram | `python -m flowr mermaid planning-flow` |
| `python -m flowr config` | Show resolved configuration with sources | `python -m flowr config` |
| `python -m flowr config --json` | Show resolved configuration as JSON | `python -m flowr config --json` |

### Session Commands

| Command | Purpose |
|---------|---------|
| `python -m flowr session init <flow> [--name <name>]` | Create a new session at the flow's initial state |
| `python -m flowr session show [--name <name>] [--format yaml\|json]` | Display current session state and call stack |
| `python -m flowr session set-state <state> [--name <name>]` | Manually update session state (validates state exists in flow) |
| `python -m flowr session list [--format yaml\|json]` | List all sessions |

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

1. **Enter**: `python -m flowr check <flow> <state>` — confirm owner, skills, attrs, and transitions.
2. **Work**: Execute the skill, reading `in` artifacts and writing `out` artifacts.
3. **Evidence**: Set any evidence required by guarded transitions based on work completed.
4. **Choose**: `python -m flowr next <flow> <state> --evidence key=value` — see which paths are available.
5. **Advance**: `python -m flowr transition <flow> <state> <trigger> --evidence key=value` — move to the next state.

### Session-Based Workflow

For ongoing work, use sessions to track progress:

1. **Init**: `python -m flowr session init <flow> --name <name>` — create session at initial state.
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