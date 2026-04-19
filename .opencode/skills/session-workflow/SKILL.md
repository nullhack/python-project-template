---
name: session-workflow
description: Session start and end protocol — read TODO.md, continue from checkpoint, update and commit
version: "3.0"
author: software-engineer
audience: all-agents
workflow: session-management
---

# Session Workflow

Every session starts by reading state. Every session ends by writing state. This makes any agent able to continue from where the last session stopped.

## Session Start

1. Read `TODO.md` — find current feature, current step, and the "Next" line.
   - If `TODO.md` does not exist, create a basic one:
     ```markdown
     # Current Work

     No feature in progress.
     Next: Run @product-owner — load skill feature-selection and pick the next BASELINED feature from backlog.
     ```
2. **If you are the PO** and Step 1 (SCOPE) is active: check `docs/discovery_journal.md` for the most recent session block.
   - If the most recent block has `Status: IN-PROGRESS` → the previous session was interrupted. Resume it before starting a new session: finish updating `.feature` files and `docs/discovery.md`, then mark the block `Status: COMPLETE`.
3. If a feature is active at Step 2–5, read:
   - `docs/features/in-progress/<name>.feature` — feature file (Rules + Examples + @id)
   - `docs/discovery.md` — project-level synthesis changelog (for context)
4. Run `git status` — understand what is committed vs. what is not
5. Confirm scope: you are working on exactly one step of one feature

**If TODO.md says "No feature in progress":**

- **PO**: Load `skill feature-selection` — it guides you through scoring and selecting the next BASELINED backlog feature. You must verify the feature has `Status: BASELINED` before moving it to `in-progress/`. Only you may move it.
- **Software-engineer or reviewer**: Update TODO.md `Next:` line to `Run @product-owner — load skill feature-selection and pick the next BASELINED feature from backlog.` Then **stop**. Never self-select a feature. Never move a `.feature` file.

## Session End

1. Update TODO.md:
   - Mark completed criteria `[x]`
   - Mark in-progress criteria `[~]`
   - Update the "Next" line with one concrete action
2. Commit any uncommitted work (even WIP):
   ```bash
   git add -A
   git commit -m "WIP(<feature-name>): <what was done>"
   ```
3. If a step is fully complete, use the proper commit message instead of WIP.

## Step Completion Protocol

When a step completes within a session:

1. Update TODO.md to reflect the completed step before doing any other work.
2. Commit the TODO.md update:
   ```bash
   git add TODO.md
   git commit -m "chore: complete step <N> for <feature-name>"
   ```
3. Only then begin the next step (in a new session where possible — see Rule 4).

## TODO.md Format

```markdown
# Current Work

Feature: <name>
Step: <1-5> (<step name>)
Source: docs/features/in-progress/<name>.feature

## Progress
- [x] `@id:<hex>`: <description>
- [~] `@id:<hex>`: <description>  ← IN PROGRESS
- [ ] `@id:<hex>`: <description>

## Next
Run @<agent-name> — <one concrete action>
```

**"Next" line format**: Always prefix with `Run @<agent-name>` so the human knows exactly which agent to invoke. Agent names are defined in `AGENTS.md` — use the name exactly as listed there. Examples:
- `Run @<software-engineer-agent> — implement @id:a1b2c3d4 (Step 3 RED)`
- `Run @<software-engineer-agent> — load skill implementation and begin Step 2 (Architecture) for <feature-name>`
- `Run @<reviewer-agent> — verify feature <feature-name> at Step 4`
- `Run @<product-owner-agent> — pick next BASELINED feature from backlog`
- `Run @<product-owner-agent> — accept feature <feature-name> at Step 5`

**Source path by step:**
- Step 1: `Source: docs/features/backlog/<name>.feature`
- Steps 2–4: `Source: docs/features/in-progress/<name>.feature`
- Step 5: `Source: docs/features/completed/<name>.feature`

Status markers:
- `[ ]` — not started
- `[~]` — in progress
- `[x]` — complete
- `[-]` — cancelled/skipped

When no feature is active:
```markdown
# Current Work

No feature in progress.
Next: Run @<product-owner-agent> — load skill feature-selection and pick the next BASELINED feature from backlog.
```

## Step 3 (TDD Loop) Cycle-Aware TODO Format

During Step 3 (TDD Loop), TODO.md **must** include a `## Cycle State` block to track Red-Green-Refactor progress.

```markdown
# Current Work

Feature: <name>
Step: 3 (TDD Loop)
Source: docs/features/in-progress/<name>.feature

## Cycle State
Test: `@id:<hex>` — <description>
Phase: RED | GREEN | REFACTOR

## Progress
- [x] `@id:<hex>`: <description>
- [~] `@id:<hex>`: <description>          ← in progress (see Cycle State)
- [ ] `@id:<hex>`: <description>          ← next

## Next
<One actionable sentence>
```

### Phase Transitions

- Move from `RED` → `GREEN` when the test fails with a real assertion
- Move from `GREEN` → `REFACTOR` when the test passes
- Move from `REFACTOR` → mark `@id` complete in `## Progress` when test-fast passes

## Rules

1. Never skip reading TODO.md at session start
2. Never end a session without updating TODO.md
3. Never leave uncommitted changes — commit as WIP if needed
4. One step per session where possible; do not start Step N+1 in the same session as Step N
5. The "Next" line must be actionable enough that a fresh AI can execute it without asking questions
6. During Step 3, always update `## Cycle State` when transitioning between RED/GREEN/REFACTOR phases
7. When a step completes, update TODO.md and commit **before** any further work
