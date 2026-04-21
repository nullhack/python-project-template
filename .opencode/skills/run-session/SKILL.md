---
name: run-session
version: "5.0"
description: Session start and end protocol — read FLOW.md, auto-detect state, resume from checkpoint, update and commit
author: software-engineer
audience: all-agents
workflow: session-management
---

# Session Workflow

Every session starts by reading state. Every session ends by writing state. This makes any agent able to continue from where the last session stopped.

The single source of state is `FLOW.md` in the project root. It tracks the current feature, branch, detected workflow state, and next action.

## Read Policy

Each agent reads only what is operationally necessary for their current step. Do not read files "for context" unless the step explicitly requires it.

| Agent | Reads |
|---|---|
| PO (Step 1) | `FLOW.md`, `scope_journal.md` (resume check), `system.md`, `glossary.md`, `domain-model.md` (read-only, entity check), `docs/post-mortem/` (selective scan), in-progress `.feature` |
| SA (Step 2) | `FLOW.md`, `system.md`, `glossary.md`, in-progress `.feature`, targeted `.py` files |
| SE (Step 3) | `FLOW.md`, `system.md`, `glossary.md`, in-progress `.feature`, targeted `.py` files |
| SA (Step 4) | `FLOW.md`, `system.md`, `glossary.md`, `domain-model.md`, in-progress `.feature`, ADR files referenced in `system.md` |

## Session Start

1. **Read `FLOW.md`** — find current feature, current branch, detected status, and the "Next" line.
   - If `FLOW.md` does not exist, create it from `.opencode/skills/flow/flow.md.template`
   - If `FLOW.md` exists but is empty or malformed, recreate from template
2. **Run `detect-state`** — execute the auto-detection rules from `skill flow` to determine the actual workflow state from filesystem and git state.
   - If detected state differs from `FLOW.md` Status, update `FLOW.md` to match reality
3. **Check prerequisites** — verify the Prerequisites table in `FLOW.md`. If any are unchecked, stop and report.
4. **If you are the PO** and Step 1 (SCOPE) is active: check `docs/scope_journal.md` for the most recent session block.
   - If the most recent block has `Status: IN-PROGRESS` → the previous session was interrupted. Resume it before starting a new session: finish updating `.feature` files and `docs/discovery.md`, then mark the block `Status: COMPLETE`.
5. If a feature is active at Step 2–5, read:
   - `docs/features/in-progress/<feature-stem>.feature` — feature file (Rules + Examples + @id)
   - `docs/system.md` — current system overview and constraints
6. Run `git status` — understand what is committed vs. what is not
7. **If Step 2–5 is active**: run `git branch --show-current` and verify:
   - **SA at Step 2 or Step 4**: must be on `feat/<stem>` or `fix/<stem>`. If on `main`, stop — load `skill version-control` and create the branch first.
   - **SE at Step 3**: must be on `feat/<stem>` or `fix/<stem>`. If on `main`, stop — load `skill version-control` and create/switch to the branch first.
8. Confirm scope: you are working on exactly one step of one feature

**If FLOW.md Status is [IDLE] or says "No feature in progress":**

- **PO**: Load `skill select-feature` — it guides you through scoring and selecting the next BASELINED backlog feature. You must verify the feature has `Status: BASELINED` before moving it to `in-progress/`. Only you may move it.
- **Software-engineer or system-architect**: Update `FLOW.md` `Next:` line to `Run @product-owner — load skill select-feature and pick the next BASELINED feature from backlog.` Then **stop**. Never self-select a feature. Never create, edit, or move a `.feature` file.

## Session End

1. Update `FLOW.md`:
   - Set Status to the detected state
   - Append to Session Log with timestamp, agent, state, and action
   - Update the "Next" line with one concrete action
2. Commit any uncommitted work (even WIP):
   ```bash
   git add -A
   git commit -m "WIP(<feature-stem>): <what was done>"
   ```
3. If a step is fully complete, use the proper commit message instead of WIP.

## Step Completion Protocol

When a step completes within a session:

1. Update `FLOW.md` to reflect the completed step before doing any other work.
2. Commit the `FLOW.md` update:
   ```bash
   git add FLOW.md
   git commit -m "chore: complete step <N> for <feature-stem>"
   ```
3. Only then begin the next step (in a new session where possible — see Rule 4).

## FLOW.md Format

```markdown
# FLOW Protocol

## Current Feature
**Feature**: <feature-stem> | [NONE]
**Branch**: <branch-name> | [NONE]
**Status**: <state>

## Prerequisites
- [x] Agents: product-owner, system-architect, software-engineer
- [x] Skills: run-session, define-scope, architect, implement, verify, version-control
- [x] Tools: uv, git
- [x] Directories: docs/features/, docs/adr/

## Session Log
**YYYY-MM-DD HH:MM** — <agent> — <state> — <action>

## Next
Run @<agent-name> — <one concrete action>
```

**"Next" line format**: Always prefix with `Run @<agent-name>` so the human knows exactly which agent to invoke. Agent names are defined in `AGENTS.md` — use the name exactly as listed there. Examples:
- `Run @software-engineer — implement @id:a1b2c3d4 (Step 3 RED)`
- `Run @system-architect — load skill architect and begin Step 2 (Architecture) for <feature-stem>`
- `Run @system-architect — verify feature <feature-stem> at Step 4`
- `Run @product-owner — pick next BASELINED feature from backlog`
- `Run @product-owner — accept feature <feature-stem> at Step 5`

## Rules

1. Never skip reading `FLOW.md` at session start
2. Never end a session without updating `FLOW.md`
3. Never leave uncommitted changes — commit as WIP if needed
4. One step per session where possible; do not start Step N+1 in the same session as Step N
5. The "Next" line must be actionable enough that a fresh AI can execute it without asking questions
6. When a step completes, update `FLOW.md` and commit **before** any further work
7. The Session Log is append-only — never delete old entries
8. If `FLOW.md` is missing, create it from `.opencode/skills/flow/flow.md.template` before doing any other work
9. If detected state differs from `FLOW.md` Status, trust the detected state and update `FLOW.md`
10. Output is minimal-signal: findings, status, decisions, blockers, Next: line only. Use the fewest, least verbose tool calls necessary. Report results, not process. No redundant prose.

## Output Style

Use minimal output. Every message must contain only what the next agent or stakeholder needs to continue — findings, status, decisions, blockers, and the Next: line.

- Use the fewest, least verbose tool calls necessary to achieve the step's goal
- Report results, not process ("3 files changed" not "I ran git status and it showed...")
- No narration before or after tool calls
- No restating tool output in prose
- No summaries of what was just done
- Always close with Next:
