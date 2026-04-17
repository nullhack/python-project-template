---
name: session-workflow
description: Session start and end protocol — read TODO.md, continue from checkpoint, update and commit
version: "2.1"
author: developer
audience: all-agents
workflow: session-management
---

# Session Workflow

Every session starts by reading state. Every session ends by writing state. This makes any agent able to continue from where the last session stopped.

## Session Start

1. Read `TODO.md` — find current feature, current step, and the "Next" line.
   - If `TODO.md` does not exist, run `uv run task gen-todo` to create it, then read the result.
2. If a feature is active, read:
   - `docs/features/in-progress/<name>.feature` — feature file (discovery + architecture + Rules + Examples)
   - `docs/features/discovery.md` — project-level discovery (for context)
3. Run `git status` — understand what is committed vs. what is not
4. Confirm scope: you are working on exactly one step of one feature

If TODO.md says "No feature in progress", report to the PO that backlog features are waiting. **The developer never self-selects a feature from the backlog — only the PO picks.**

## Session End

1. Update TODO.md:
   - Mark completed criteria `[x]`
   - Mark in-progress criteria `[~]`
   - Update the "Next" line with one concrete action
2. Run `uv run task gen-todo` to sync any new @id rows from .feature files into TODO.md.
3. Commit any uncommitted work (even WIP):
   ```bash
   git add -A
   git commit -m "WIP(<feature-name>): <what was done>"
   ```
4. If a step is fully complete, use the proper commit message instead of WIP.

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
Step: <1-6> (<step name>)
Source: docs/features/in-progress/<name>.feature

## Progress
- [x] `@id:<hex>`: <description>
- [~] `@id:<hex>`: <description>  ← IN PROGRESS
- [ ] `@id:<hex>`: <description>

## Next
<One sentence: exactly what to do in the next session>
```

**Source path by step:**
- Step 1: `Source: docs/features/backlog/<name>.feature`
- Steps 2–5: `Source: docs/features/in-progress/<name>.feature`
- Step 6: `Source: docs/features/completed/<name>.feature`

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

During Step 4 (Implementation), TODO.md **must** include a `## Cycle State` block to track Red-Green-Refactor-Review progress. This block is **mandatory** — missing it means the cycle is unverifiable.

When `Phase: SELF-DECLARE` or later, a `## Self-Declaration` block is also **mandatory**. The reviewer reads it directly from TODO.md. A missing or incomplete self-declaration (unchecked boxes, missing `file:line`) = automatic REJECTED.

For the full Self-Declaration checklist template (21 items), see `implementation/SKILL.md` — the "Design Self-Declaration" section under REFACTOR.

```markdown
# Current Work

Feature: <name>
Step: 4 (implement)
Source: docs/features/in-progress/<name>.feature

## Cycle State
Test: `@id:<hex>` — <description>
Phase: RED | GREEN | REFACTOR | SELF-DECLARE | REVIEWER(code-design) | COMMITTED

## Self-Declaration (@id:<hex>)
- [x] YAGNI-1: … — `file:line`
- [x] YAGNI-2: … — `file:line`
- [x] KISS-1: … — `file:line`
  … (full checklist from implementation/SKILL.md)
- [x] Semantic: test abstraction matches AC abstraction — `file:line`

## Progress
- [x] `@id:<hex>`: <description> — reviewer(code-design) APPROVED
- [~] `@id:<hex>`: <description>          ← in progress (see Cycle State)
- [ ] `@id:<hex>`: <description>          ← next

## Next
<One actionable sentence>
```

### Reviewer Scope Legend

When referencing reviewer interactions in TODO.md:
- `reviewer(code-design)` — per-test design check during Step 4 (YAGNI/KISS/DRY/SOLID/ObjCal/patterns + semantic alignment only)
- `reviewer(full-verify)` — Step 5 full verification (lint, pyright, coverage, semantic review, adversarial testing)

## gen-todo Script

`uv run task gen-todo` keeps TODO.md in sync with `.feature` files:

```bash
uv run task gen-todo              # merge-write: add missing @id rows, preserve existing status
uv run task gen-todo -- --check   # dry run — report what would change
```

**Merge rules:**
- Adds any `@id` rows from in-progress `.feature` files that are missing in `## Progress`
- Never removes or downgrades existing `[x]`, `[~]`, `[-]` rows
- Preserves the `Step:` field and `## Next` line from the current TODO.md
- If no feature is in-progress, writes the "No feature in progress" format

Run `gen-todo` at session start (after reading TODO.md) and at session end (before committing).

## Rules

1. Never skip reading TODO.md at session start
2. Never end a session without updating TODO.md
3. Never leave uncommitted changes — commit as WIP if needed
4. One step per session where possible; do not start Step N+1 in the same session as Step N
5. The "Next" line must be actionable enough that a fresh AI can execute it without asking questions
6. During Step 4, always update `## Cycle State` when transitioning between RED/GREEN/REFACTOR/SELF-DECLARE/REVIEWER phases
7. When a step completes, update TODO.md and commit **before** any further work
8. During Step 4, write the `## Self-Declaration (@id:<hex>)` block into TODO.md at SELF-DECLARE phase — every checkbox must be checked with a `file:line` or `N/A` before requesting reviewer(code-design)
