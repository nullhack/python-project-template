---
name: session-workflow
description: Manage multi-session AI development - read TODO.md, continue from last checkpoint, update progress, and hand off cleanly to the next session
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: session-management
---
## What I do

Enable complex projects to be developed across multiple AI sessions. Each session picks up exactly where the last one stopped, using `TODO.md` as the shared state between sessions.

This solves the context-window problem for large projects: no single session needs to hold the entire project in mind. The `TODO.md` file acts as a living contract between sessions.

## When to use me

- At the **start** of every session: read `TODO.md` and orient yourself
- At the **end** of every session: update `TODO.md` with progress and handoff notes
- When a project is **too large** to complete in one session
- When you want **any AI** (not just you) to be able to continue the work

## Session Start Protocol

When beginning a new session on a project:

### 1. Read the project state
```
Read TODO.md
Read AGENTS.md
```

### 2. Identify the current phase
- Find the first `[ ]` (pending) item in `TODO.md`
- Read the **Session Log** and **Notes for Next Session** sections
- Understand what was done last and what comes next

### 3. Confirm scope for this session
- Pick ONE phase or a small, coherent set of tasks
- Do not attempt to complete everything at once
- Aim for a clean handoff point at the end of the session

### 4. Mark tasks in progress
- Update `TODO.md`: change `[ ]` to `[~]` for tasks you start
- Only mark one task `[~]` at a time when possible

## Session End Protocol

When finishing a session:

### 1. Mark completed tasks
- Change `[~]` to `[x]` for everything finished this session
- Leave `[ ]` for anything not yet started

### 2. Update the Session Log
Append a row to the Session Log table:
```markdown
| YYYY-MM-DD | Brief summary of what was done this session |
```

### 3. Update Notes for Next Session
Replace the existing notes with fresh guidance:
```markdown
## Notes for Next Session
- Start with Phase X, item: "..."
- The tricky part is [explain any complexity or gotchas]
- Run `task test` first to verify current state
- [Any other context the next session needs]
```

### 4. Commit the updated TODO.md
Always commit `TODO.md` changes so the history is preserved in git.

## TODO.md Format

Every project should have a `TODO.md` at the root with this structure:

```markdown
# <Project Name> - Development TODO

This file tracks all development steps. Each AI session should read this file first,
pick up from the last completed step, and update statuses before finishing.

**Convention:** `[ ]` = pending, `[x]` = done, `[~]` = in progress

---

## Phase 1: <Phase Name>

- [x] Completed task
- [~] In-progress task
- [ ] Pending task

---

## Phase N: <Phase Name>

- [ ] Task

---

## Session Log

| Date       | Session Summary                        |
|------------|----------------------------------------|
| YYYY-MM-DD | Initial scaffolding, TODO created      |

---

## Notes for Next Session

- Start with Phase X: "task description"
- <Any context or gotchas>
```

## Task Status Conventions

| Symbol | Meaning |
|--------|---------|
| `[ ]`  | Pending - not started |
| `[~]`  | In progress - current session is working on this |
| `[x]`  | Done - completed and verified |
| `[-]`  | Skipped - decided not to do this |

## Example: Starting a session

```
I'm starting a new session on this project.

Step 1: Read TODO.md to find where we are.
Step 2: The last session completed Phase 2 (data models).
        Notes say: "Start with Phase 3, federation_repo.py first"
Step 3: I'll tackle Phase 3.1 (Federation Repository) this session.
Step 4: Marking federation_repo tasks as [~] and starting work.
```

## Example: Ending a session

```
Session complete. I implemented Phase 3.1 and 3.2.

Updating TODO.md:
- [x] federation_repo.py - list, get, create, update
- [x] agent_repo.py - list, get, create, federations query

Session Log: 2026-03-13 | Implemented federation and agent repositories

Notes for Next Session:
- Start with Phase 3.3: membership_repo.py
- Tests are in tests/test_repositories.py, run `task test` first
- The DB schema uses TEXT for IDs (slugs), not integers
```

## Rules

1. **Never skip reading TODO.md** at the start of a session
2. **Never leave TODO.md stale** - always update before finishing
3. **One phase per session** - resist the urge to do everything
4. **Clean handoffs** - future sessions (and future AIs) should need zero context from you
5. **Commit TODO.md** - it is source code, not a scratch pad
