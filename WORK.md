# WORK — Active Work Tracking

This file tracks live work items. The workflow rules live in `FLOW.md`.

Each item carries exactly the variables defined by `FLOW.md`:
- `@id` — work item identifier (feature-stem)
- `@state` — current state in the workflow
- `@branch` — git branch where the work lives

---

## Active Items

<!-- One entry per in-flight work item. Remove when state reaches IDLE. -->

- @id: cli-entrypoint
  @state: STEP-2-READY
  @branch: [NONE — SA creates feat/cli-entrypoint at Step 2 start]

---

## Session Log

### 2026-04-22 — Session 1 (Discovery)

- Resumed interrupted Stage 1 discovery session (Q1–Q8 were pre-captured).
- Completed Block B cross-cutting questions (Q9–Q11): confirmed scope is one demonstration feature.
- Completed Block C feature discovery: stakeholder chose CLI entrypoint (`--help` + `--version`) as the demonstration feature.
- Created `docs/features/backlog/cli-entrypoint.feature` — Status: BASELINED (2026-04-22).
- Created `docs/features/in-progress/` and `docs/features/completed/` directories.
- Created `docs/glossary.md`, `docs/discovery.md`.
- Marked `docs/scope_journal.md` Session 1 as COMPLETE.

**Next:** Run `@system-architect` — begin Step 2 (ARCH) for `cli-entrypoint`. PO must first move `docs/features/backlog/cli-entrypoint.feature` → `docs/features/in-progress/cli-entrypoint.feature`.

### 2026-04-22 — PO: Move cli-entrypoint to in-progress

- Stakeholder confirmed: move `cli-entrypoint.feature` to `in-progress/`.
- Moved `docs/features/backlog/cli-entrypoint.feature` → `docs/features/in-progress/cli-entrypoint.feature`.
- Updated WORK.md: `@state: STEP-2-READY`.

**Next:** Run `@system-architect` — load skill `architect` and begin Step 2 (Architecture) for `cli-entrypoint`.

