---
name: session-workflow
description: Session start and end protocol — read TODO.md, continue from checkpoint, update and commit
version: "2.0"
author: developer
audience: all-agents
workflow: session-management
---

# Session Workflow

Every session starts by reading state. Every session ends by writing state. This makes any agent able to continue from where the last session stopped.

## Session Start

1. Read `TODO.md` — find current feature, current step, and the "Next" line
2. If a feature is active, read:
   - `docs/features/in-progress/<name>/discovery.md` — feature discovery
   - `docs/features/discovery.md` — project-level discovery (for context)
3. Run `git status` — understand what is committed vs. what is not
4. Confirm scope: you are working on exactly one step of one feature

If TODO.md says "No feature in progress", check `docs/features/backlog/` for feature folders. If the backlog is empty, the PO needs to define the next feature.

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

## TODO.md Format

```markdown
# Current Work

Feature: <name>
Step: <1-6> (<step name>)
Source: docs/features/in-progress/<name>/discovery.md

## Progress
- [x] `<@id:hex>`: <description>
- [~] `<@id:hex>`: <description>  ← IN PROGRESS
- [ ] `<@id:hex>`: <description>

## Next
<One sentence: exactly what to do in the next session>
```

Status markers:
- `[ ]` — not started
- `[~]` — in progress
- `[x]` — complete
- `[-]` — cancelled/skipped

When no feature is active:
```markdown
# Current Work

No feature in progress.
Next: PO picks feature from docs/features/backlog/ and moves it to docs/features/in-progress/.
```

## Step 4 Cycle-Aware TODO Format

During Step 4 (Implementation), the TODO.md format includes cycle state to track Red-Green-Refactor-Review progress:

```markdown
# Current Work

Feature: <name>
Step: 4 (implement)
Source: docs/features/in-progress/<name>/discovery.md

## Cycle State
Test: `<@id:hex>` — <description>
Phase: RED | GREEN | REFACTOR | REVIEWER(code-design) | COMMITTED

## Progress
- [x] `<@id:hex>`: <description>          ← done
- [x] `<@id:hex>`: <description> — reviewer(code-design) APPROVED
- [~] `<@id:hex>`: <description>          ← in progress (see Cycle State)
- [ ] `<@id:hex>`: <description>          ← next

## Next
<One actionable sentence>
```

### Reviewer Scope Legend

When referencing reviewer interactions in TODO.md:
- `reviewer(code-design)` — per-test design check during Step 4 (SOLID/DRY/KISS/ObjCal/patterns + semantic alignment only)
- `reviewer(full-verify)` — Step 5 full verification (lint, pyright, coverage, semantic review, adversarial testing)

## Rules

1. Never skip reading TODO.md at session start
2. Never end a session without updating TODO.md
3. Never leave uncommitted changes — commit as WIP if needed
4. One step per session where possible; do not start Step N+1 in the same session as Step N
5. The "Next" line must be actionable enough that a fresh AI can execute it without asking questions
6. During Step 4, always update `## Cycle State` when transitioning between RED/GREEN/REFACTOR/REVIEWER phases
