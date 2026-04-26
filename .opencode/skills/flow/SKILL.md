---
name: flow
version: "2.0"
description: Flow protocol — design and operate state machine workflows with YAML flow definitions and session tracking
author: software-engineer
audience: all-agents
workflow: session-management
---

# Flow Protocol

This skill defines how to **operate** a state machine workflow using YAML flow definitions and session tracking.

- **Flow definitions** (`docs/flows/*.yaml`) — static state machine definitions (never change during execution)
- **Session files** (`.flowception/session-*.yaml`) — dynamic work trackers (updated by agents at every transition)

The project's current workflow is defined in `docs/flows/`. Load this skill when:
- Starting any session (to understand the operating protocol)
- Creating a new workflow from scratch
- Modifying an existing workflow

See [[workflow/state-machine]] for FSM fundamentals, YAML flow format, and transition protocol.

---

## Operating Protocol

### Session Start (all agents)

1. Read the active flow definition from `docs/flows/feature-flow.yaml`
2. Read the active session from `.flowception/session-*.yaml` — note current flow, state, and params
3. Run auto-detection to verify the session state matches the filesystem
4. If detected state differs from the session file, update the session file to match reality (filesystem wins)
5. Check prerequisites from the flow definition — if any missing, stop and report
6. Read the work item artifact (e.g. `.feature` file) for context
7. Verify git workspace matches the branch in session params

### Session End (all agents)

1. Update the session file:
   - Set current state to the new state
2. Commit session file update before any further work:
   ```bash
   git add .flowception/ && git commit -m "chore: transition to <state>"
   ```
3. Commit any remaining work as WIP if not fully complete:
   ```bash
   git add -A && git commit -m "WIP(<feature>): <what was done>"
   ```

### State Transition Rule

The agent who **completes** a state is responsible for updating the session file to the next state **before** doing any other work. Transitions are atomic: update session file, commit, then proceed.

### Self-Healing Rule

If the session file and auto-detection disagree, the filesystem is the source of truth. Update the session file to match. Never "correct" the filesystem to match the session file.

---

## Designing a Workflow

Flow definitions are YAML files in `docs/flows/`. Use the flowception format. See `docs/flows/feature-flow.yaml` as an example. See [[workflow/state-machine]] for the full schema, contract syntax, and state definition fields.

---

## Session Format

Session files live in `.flowception/` and track the active flow, current state, parameter namespace, and transition history. See [[workflow/state-machine]] for the full session schema.

---

## Creating a New Workflow

Use the templates bundled with this skill as reference:

- `flow.md.template` — legacy FLOW.md skeleton (for reference only)
- `work.md.template` — legacy WORK.md skeleton (for reference only)

Steps:
1. Create a new YAML file in `docs/flows/` following the flowception format
2. Define states, transitions, contracts, and params per the schema in [[workflow/state-machine]]
3. Verify the detection rules are ordered correctly
4. Verify all agent references have corresponding agent files

---

## Rules

1. Never skip reading the flow definition and session file at session start
2. Never end a session without updating the session file and committing
3. Never commit directly to `main`
4. If the session file is missing, create it before any other work
5. If detected state differs from the session file, trust the filesystem and update the session file
6. One step per session where possible; do not start Step N+1 in the same session as Step N
