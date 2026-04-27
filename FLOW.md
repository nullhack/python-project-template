# FLOW — Feature Development Workflow

This file is a redirect. The workflow state machine is now defined as YAML flow definitions.

**Agents never modify flow definition files.** Only the stakeholder (human) may change them.

## Where to Find Things

| Artifact | Location | Description |
|---|---|---|
| Flow definitions | `docs/flows/*.yaml` | Static state machine definitions (YAML) |
| Session state | `.flowception/session-*.yaml` | Dynamic work tracking (YAML) |
| Workflow knowledge | [[workflow/state-machine]] | FSM fundamentals, YAML format, contracts, session protocol |

## Active Flows

| Flow | File | Description |
|---|---|---|
| `feature-flow` | `docs/flows/feature-flow.yaml` | Full feature development lifecycle (7 states + 3 subflows) |
| `scope-cycle` | `docs/flows/scope-cycle.yaml` | Scope subflow: backlog-criteria → discovery → stories → criteria (4 states) |
| `arch-cycle` | `docs/flows/arch-cycle.yaml` | Architecture subflow: read → interview → validate → design → stubs (5 states) |
| `tdd-cycle` | `docs/flows/tdd-cycle.yaml` | TDD subflow: setup → red → green → refactor (4 states) |

## Quick Reference

Read `docs/flows/feature-flow.yaml` for state definitions, transitions, and contracts.
Read `.flowception/session-*.yaml` for current work state.
Read [[workflow/state-machine]] for FSM theory, YAML schema, and transition protocol.

## Detection Rules

States are detected from filesystem and git state. The session file is the source of truth for `current` state; if filesystem and session disagree, trust the filesystem and update the session.

Run these to verify workspace consistency:

```bash
# 1. Is there a feature in progress?
ls docs/features/in-progress/*.feature 2>/dev/null | grep -v ".gitkeep"

# 2. Are we on the correct branch?
git branch --show-current

# 3. Do test stubs exist when they should?
ls tests/features/*/ 2>/dev/null | head -1
```

## Prerequisites

All must be satisfied before starting any session. If any are missing, stop and alert the human.

| Requirement | Verification Command |
|---|---|
| Role: product-owner | `test -f .opencode/agents/product-owner.md` |
| Role: system-architect | `test -f .opencode/agents/system-architect.md` |
| Role: software-engineer | `test -f .opencode/agents/software-engineer.md` |
| Flow definition | `test -f docs/flows/feature-flow.yaml` |
| Session file | `ls .flowception/session-*.yaml 2>/dev/null` |
| Tool: uv | `command -v uv` |
| Tool: git | `command -v git` |
| Dir: docs/features/ | `test -d docs/features/backlog` |
| Dir: docs/adr/ | `test -d docs/adr` |