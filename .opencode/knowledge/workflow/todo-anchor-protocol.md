---
domain: workflow
tags: [todo, anchor, protocol, execution-contract, state-isolation, loop-prevention]
last-updated: 2026-05-05
---

# Todo Anchor Protocol

## Key Takeaways

- The todo list is the execution contract between orchestrator and agent: every item must be marked `[X]` before the next `[ ]` becomes `in_progress`.
- The anchor item `[~]` is mandatory and always last; it prevents state-skipping by requiring `flowr next` → `flowr transition` → todo rewrite.
- One state per todo. Never generate a todo that spans multiple flow states or includes steps from adjacent states.
- Loops (review → fix → re-review) are separate dispatches with separate flowr transitions; the todo must not collapse them.

## Concepts

**Todo as Execution Contract**: The todo list generated at state entry is not a suggestion. It is the procedural checklist. The orchestrator creates it from `flowr check` output, dispatches the owner agent to do the work, then uses the anchor to advance. Every `[X]` must be complete before the anchor fires.

**One State Per Todo**: A todo covers exactly one flow state. When a flow has multiple states (e.g., design-review → structure-review → conventions-review), each state gets its own todo, its own dispatch, and its own flowr transition. Never generate a todo that includes items from the next state or collapses loop iterations.

**Anchor Item**: The last item in every todo is marked `[~]` and reads: "flowr next → pick transition → flowr transition → rewrite todo from next state." The anchor must:
- Run `flowr next --session --evidence key=value` to see all transitions with status markers (`"open"` / `"blocked"`)
- For `"blocked"` transitions, check `conditions` dict to understand what evidence is needed
- Present options to the stakeholder if multiple `"open"` paths exist
- Run `flowr transition <trigger> --session --evidence key=value`
- Generate a new todo list from the next state's metadata via `flowr check --session`
- Never be skipped. It is the guardrail that prevents state-skipping

**Loop Prevention**: When a review tier rejects and the flow loops back (e.g., `fail` → `tdd-cycle`), the orchestrator must:
1. Complete the current state's anchor (transition `fail`)
2. Enter the new state (e.g., `tdd-cycle`)
3. Generate a fresh todo from the new state's metadata
4. Dispatch the owner agent with only the new state's skills
5. Never carry items from the review state into the fix state's todo

**State Isolation**: The todo must not include steps from adjacent states. If the work reveals that an artifact outside the `out` contract needs changes, flag it in output notes. Do not add it to the current todo.

## Content

### Todo Generation Rules

At state entry, generate the todo from the state's `flowr check` output:

1. **Preparation items** (`[ ]`): list available `in` artifacts (discover via `ls`/`find`)
2. **Dispatch item** (`[ ]`): call the state's owner agent with skills loaded
3. **Output items** (`[ ]`): one per `out` artifact to create/update
4. **Verification items** (`[ ]`): check constraints, run tests/lint if applicable
5. **Anchor item** (`[~]`, always last): "flowr next → pick transition → flowr transition → rewrite todo"

Only one `[ ]` item should be `in_progress` at a time. Mark `[X]` immediately upon completion.

### Anchor Checklist (FAA AC 120-71b)

Before exiting a state, confirm each item:

- **Dispatch completed:** Exactly one agent dispatch happened with exactly the skills listed.
- **Single-state scope:** No work from adjacent states was performed during this dispatch.
- **Flowr next checked:** `flowr next --session` ran. JSON output parsed. Transitions with `"status": "open"` are available; `"status": "blocked"` transitions show required evidence in `conditions`.
- **Transition executed:** `flowr transition <trigger> --session` ran successfully.
- **Todo rewritten:** New todo list generated from the next state's metadata via `flowr check --session`.
- **No state skipped:** Every item above the anchor is marked `[X]`.

### Anti-Patterns

**Collapsing states**: A todo that includes items like "review design" AND "review structure" AND "review conventions" collapses three states into one. Each is a separate state requiring its own todo, dispatch, and transition.

**Pre-generating loop iterations**: A todo that includes "fix issues from review" alongside the review items pre-generates a loop iteration that may not happen. The fix state only gets a todo if the review rejects.

**Carrying state forward**: After transitioning, the old todo is replaced entirely. The new todo is generated fresh from `flowr check --session` output. Never append to the previous todo.

### Owner Mapping

Owner dispatch mapping per AGENTS.md Session Protocol.

## Related

- [[workflow/flowr-operations]]
- [[skill-design/principles]]
