---
name: run-session
version: "5.0"
description: Session start and end protocol — read flow definitions, auto-detect state, resume from checkpoint, update and commit
author: software-engineer
audience: all-agents
workflow: session-management
---

# Session Workflow

Every session starts by reading state. Every session ends by writing state. This makes any agent able to continue from where the last session stopped.

State is tracked across two locations: `docs/flows/feature-flow.yaml` (static flow definition — never modified by agents) and `.flowception/session-*.yaml` (dynamic session state — updated every session). Agents read `docs/flows/feature-flow.yaml` to understand the workflow; they read and update `.flowception/session-*.yaml` to track the active feature.

## Read Policy

Each agent reads only what is operationally necessary for their current step. Do not read files "for context" unless the step explicitly requires it.

| Agent | Reads |
|---|---|
| PO (Step 1) | `.flowception/session-*.yaml`, `docs/flows/feature-flow.yaml`, `scope_journal.md` (resume check), `system.md` (Domain Model section, read-only), `glossary.md`, `docs/post-mortem/` (selective scan), in-progress `.feature` |
| SA (Step 2) | `.flowception/session-*.yaml`, `docs/flows/feature-flow.yaml`, `system.md`, `glossary.md`, in-progress `.feature`, targeted `.py` files |
| SE (Step 3) | `.flowception/session-*.yaml`, `docs/flows/feature-flow.yaml`, `system.md`, `glossary.md`, in-progress `.feature`, targeted `.py` files |
| SA (Step 4) | `.flowception/session-*.yaml`, `docs/flows/feature-flow.yaml`, `system.md`, `glossary.md`, in-progress `.feature`, ADR files referenced in `system.md` |

## Session Start

1. **Read session file from `.flowception/`** — find the active session YAML: `@id`, `@state`, `@branch`.
   - If no session file exists in `.flowception/`, create one from `.opencode/skills/flow/session.yaml.template`
2. **Read flow definition from `docs/flows/feature-flow.yaml`** — understand the static workflow (roles, states, detection rules, transitions).
   - If `docs/flows/feature-flow.yaml` does not exist, create it from `.opencode/skills/flow/feature-flow.yaml.template`
   - If `docs/flows/feature-flow.yaml` exists but is empty or malformed, recreate from template
3. **Run `detect-state`** — execute the auto-detection rules from `docs/flows/feature-flow.yaml` to determine the actual workflow state from filesystem and git state.
   - If detected state differs from session file `@state`, update the session file to match reality. **Never modify `docs/flows/feature-flow.yaml`.**
4. **Check prerequisites** — verify the Prerequisites table in `docs/flows/feature-flow.yaml`. If any are unchecked, stop and report.
5. **If you are the PO** and Step 1 (SCOPE) is active: check `docs/scope_journal.md` for the most recent session block.
   - If the most recent block has `Status: IN-PROGRESS` → the previous session was interrupted. Resume it before starting a new session: finish updating `.feature` files and `docs/discovery.md`, then mark the block `Status: COMPLETE`.
6. If a feature is active at Step 2–5, read:
   - `docs/features/in-progress/<feature-stem>.feature` — feature file (Rules + Examples + @id)
   - `docs/system.md` — current system overview and constraints
7. Run `git status` — understand what is committed vs. what is not
8. **If Step 3–5 is active**: run `git branch --show-current` and verify:
    - **SA at Step 4**: must be on `feat/<stem>` or `fix/<stem>`. If on `main`, stop — load `skill version-control` and switch to the branch first.
    - **SE at Step 3 (TDD `setup` state)**: may be on `main` — the `setup` state will create the branch. If already on `feat/<stem>` or `fix/<stem>`, proceed to `red`.
    - **SE at Step 3 (red/green/refactor) or Step 5 merge**: must be on `feat/<stem>` or `fix/<stem>`. If on `main`, stop — load `skill version-control` and create/switch to the branch first.
   Note: Step 2 (arch-cycle) does not require a feature branch — the SA works on design, ADRs, and stubs before the SE creates the branch at Step 3 setup.
9. Confirm scope: you are working on exactly one step of one feature

**If session file `@state` is [IDLE] or no active item exists:**

- **PO**: Load `skill select-feature` — it guides you through scoring and selecting the next BASELINED backlog feature. You must verify the feature has `Status: BASELINED` before moving it to `in-progress/`. Only you may move it.
- **Software-engineer or system-architect**: Update session file `@state` to `[IDLE]` if it is not already, then **stop**. Never self-select a feature. Never create, edit, or move a `.feature` file.

## Session End

1. Update session file in `.flowception/`:
   - Set `@state` to the detected state
2. Commit any uncommitted work (even WIP):
   ```bash
   git add -A
   git commit -m "WIP(<feature-stem>): <what was done>"
   ```
3. If a step is fully complete, use the proper commit message instead of WIP.

## Step Completion Protocol

When a step completes within a session:

1. Update the session file in `.flowception/` to reflect the completed step before doing any other work.
2. Commit the session file update:
   ```bash
   git add .flowception/
   git commit -m "chore: complete step <N> for <feature-stem>"
   ```
3. Only then begin the next step (in a new session where possible — see Rule 4).

## Session YAML Format

```yaml
active_items:
  id: <feature-stem>
  state: <state>
  branch: <branch-name> | NONE
```

## Rules

1. Never skip reading the session file in `.flowception/` and `docs/flows/feature-flow.yaml` at session start
2. Never end a session without updating the session file in `.flowception/`
3. Never leave uncommitted changes — commit as WIP if needed
4. One step per session where possible; do not start Step N+1 in the same session as Step N
5. When a step completes, update the session file in `.flowception/` and commit **before** any further work
6. If `docs/flows/feature-flow.yaml` is missing, create it from `.opencode/skills/flow/feature-flow.yaml.template` before doing any other work
7. If detected state differs from session file `@state`, trust the detected state and update the session file. **Never modify `docs/flows/feature-flow.yaml`.**
8. Output is minimal-signal: findings, status, decisions, blockers only. Use the fewest, least verbose tool calls necessary. Report results, not process. No redundant prose.

## Output Style

Use minimal output. Every message must contain only what the next agent or stakeholder needs to continue — findings, status, decisions, blockers.

- Use the fewest, least verbose tool calls necessary to achieve the step's goal
- Report results, not process ("3 files changed" not "I ran git status and it showed...")
- No narration before or after tool calls
- No restating tool output in prose
- No summaries of what was just done
