# FLOW — Feature Development Workflow

This file defines the static state machine for feature development. **Agents never modify this file.**
Only the stakeholder (human) may change it, using `skill flow` as the design protocol.
Dynamic work tracking lives in `WORK.md`.

---

## Work Variables

Every work item tracked in `WORK.md` must carry exactly these variables:

| Variable  | Description                                           |
|-----------|-------------------------------------------------------|
| `@id`     | The work item identifier (feature-stem or test @id)   |
| `@state`  | Current state in this workflow                        |
| `@branch` | Git branch where the work lives                       |

---

## Roles

These roles must exist before the workflow can run. Each state has exactly one owner.

| Role              | Agent File                             | Responsibility                                      |
|-------------------|----------------------------------------|-----------------------------------------------------|
| `product-owner`   | `.opencode/agents/product-owner.md`   | Discovery, scope, acceptance, `.feature` file moves |
| `system-architect`| `.opencode/agents/system-architect.md`| Architecture, domain design, adversarial review     |
| `software-engineer`| `.opencode/agents/software-engineer.md`| TDD loop, implementation, git, releases            |

---

## Prerequisites

All must be satisfied before starting any session. If any are missing, stop and alert the human.

| Requirement          | Verification Command                                      |
|----------------------|-----------------------------------------------------------|
| Role: product-owner  | `test -f .opencode/agents/product-owner.md`               |
| Role: system-architect | `test -f .opencode/agents/system-architect.md`          |
| Role: software-engineer | `test -f .opencode/agents/software-engineer.md`        |
| Skill: run-session   | `test -f .opencode/skills/run-session/SKILL.md`           |
| Skill: define-scope  | `test -f .opencode/skills/define-scope/SKILL.md`          |
| Skill: architect     | `test -f .opencode/skills/architect/SKILL.md`             |
| Skill: implement     | `test -f .opencode/skills/implement/SKILL.md`             |
| Skill: verify        | `test -f .opencode/skills/verify/SKILL.md`                |
| Skill: version-control | `test -f .opencode/skills/version-control/SKILL.md`     |
| Tool: uv             | `command -v uv`                                           |
| Tool: git            | `command -v git`                                          |
| Dir: docs/features/  | `test -d docs/features/backlog`                           |
| Dir: docs/adr/       | `test -d docs/adr`                                        |
| WORK.md              | `test -f WORK.md`                                         |

---

## State Machine

States are checked **in order**. The first matching condition is the current state.

```mermaid
stateDiagram-v2
    [*] --> IDLE

    IDLE --> STEP-1-BACKLOG-CRITERIA
    IDLE --> STEP-1-DISCOVERY

    STEP-1-BACKLOG-CRITERIA --> IDLE
    STEP-1-DISCOVERY --> STEP-1-STORIES
    STEP-1-STORIES --> STEP-1-CRITERIA
    STEP-1-CRITERIA --> STEP-2-READY

    STEP-2-READY --> STEP-2-ARCH
    STEP-2-ARCH --> STEP-3-WORKING
    STEP-2-ARCH --> STEP-1-CRITERIA : failure

    STEP-3-WORKING --> STEP-3-RED
    STEP-3-RED --> STEP-3-WORKING
    STEP-3-WORKING --> STEP-4-READY

    STEP-4-READY --> STEP-5-READY
    STEP-4-READY --> STEP-3-WORKING : failure

    STEP-5-READY --> STEP-5-MERGE
    STEP-5-READY --> POST-MORTEM : failure

    POST-MORTEM --> STEP-2-ARCH

    STEP-5-MERGE --> STEP-5-COMPLETE
    STEP-5-COMPLETE --> IDLE
    STEP-5-COMPLETE --> [*]
```

### Detection Rules (evaluated in order)

1. No file in `docs/features/in-progress/` AND any `backlog/` feature has `Status: BASELINED` but no `Example:` with `@id` → **[STEP-1-BACKLOG-CRITERIA]**
2. No file in `docs/features/in-progress/` → **[IDLE]**
3. Feature in `in-progress/`, no `Status: BASELINED` → **[STEP-1-DISCOVERY]**
4. Feature has `Status: BASELINED`, no `Rule:` blocks → **[STEP-1-STORIES]**
5. Feature has `Rule:` blocks, no `Example:` with `@id` → **[STEP-1-CRITERIA]**
6. Feature has `@id` tags, no `feat/` or `fix/` branch exists → **[STEP-2-READY]**
7. On feature branch, no test stubs in `tests/features/<stem>/` → **[STEP-2-ARCH]**
8. Test stubs exist, any have `@pytest.mark.skip` OR all unskipped tests pass but skipped remain → **[STEP-3-WORKING]**
9. Unskipped test exists that fails → **[STEP-3-RED]**
10. `WORK.md @state` is `STEP-5-READY` → **[STEP-5-READY]** *(WORK.md takes precedence over rule 11 — filesystem alone cannot distinguish Step 4 done from Step 5 ready)*
11. All tests pass, no skipped tests → **[STEP-4-READY]**
12. On main branch, feature still in `in-progress/` AND `WORK.md @state = STEP-5-COMPLETE` → **[STEP-5-COMPLETE]**
13. On feature branch (`feat/` or `fix/`), feature still in `in-progress/` → **[STEP-5-MERGE]**
14. Post-mortem file exists for current feature → **[POST-MORTEM]**

---

## States

### [STEP-1-BACKLOG-CRITERIA]
**Owner**: `product-owner`
**Entry condition**: No file in `in-progress/` AND one or more `backlog/` features have `Status: BASELINED` but no `Example:` with `@id`
**Action**: Write `Rule:` blocks and `Example:` blocks with `@id` tags for BASELINED backlog features. Files stay in `backlog/` — do **not** move to `in-progress/`. No `WORK.md` entry required.
**Exit**: All BASELINED backlog features have `@id` tags → transition to `[IDLE]`
**Commit**: `feat(criteria): write acceptance criteria for <feature-stem>` per feature
**Note**: This state exists specifically for bulk Stage 2 work before a feature is selected for development. It does not consume the WIP slot. `run-session` must **not** treat this state as `[IDLE]` — there is work to do.

---

### [IDLE]
**Owner**: `product-owner`
**Entry condition**: No file in `docs/features/in-progress/` AND all BASELINED backlog features already have `@id` tags (or no BASELINED features exist)
**Action**: Select next BASELINED feature from `backlog/`; move it to `in-progress/`
**Exit**: Feature moved → create `WORK.md` entry; initial `@state` depends on feature content:
- Feature has no `Rule:` blocks → `@state: STEP-1-DISCOVERY`
- Feature has `Rule:` blocks but no `@id` Examples → `@state: STEP-1-CRITERIA`
- Feature has `@id` Examples → `@state: STEP-2-READY`

---

### [STEP-1-DISCOVERY]
**Owner**: `product-owner`
**Entry condition**: Feature in `in-progress/`, no `Status: BASELINED`
**Action**: Interview stakeholder; update `scope_journal.md`, `discovery.md`, `glossary.md`
**Exit**: Feature baselined → update `@state: STEP-1-STORIES` in `WORK.md`
**Stay**: More discovery needed → remain in `[STEP-1-DISCOVERY]`

---

### [STEP-1-STORIES]
**Owner**: `product-owner`
**Entry condition**: Feature has `Status: BASELINED`, no `Rule:` blocks
**Action**: Write `Rule:` blocks with INVEST criteria
**Exit**: Stories committed → update `@state: STEP-1-CRITERIA` in `WORK.md`

---

### [STEP-1-CRITERIA]
**Owner**: `product-owner`
**Entry condition**: Feature has `Rule:` blocks, no `Example:` blocks with `@id`
**Action**: Write `Example:` blocks with `@id` tags; MoSCoW triage per example
**Exit**: Criteria committed → update `@state: STEP-2-READY` in `WORK.md`
**Commit**: `feat(criteria): write acceptance criteria for @id`

---

### [STEP-2-READY]
**Owner**: `software-engineer`
**Entry condition**: Feature has `@id` tags, no `feat/<stem>` or `fix/<stem>` branch
**Action**: Load `skill version-control`; create branch `feat/<stem>` from `main`; set `@branch` in `WORK.md`
**Exit**: Branch created → update `@state: STEP-2-ARCH` in `WORK.md`

---

### [STEP-2-ARCH]
**Owner**: `system-architect`
**Entry condition**: On `@branch`, no test stubs in `tests/features/<stem>/`
**Action**: Read feature; design domain stubs; draft ADRs; present ADR validation table to stakeholder; commit approved ADRs; update `system.md` (domain model + Context + Container sections); run `uv run task test-fast` to generate stubs
**Exit**: Stubs generated → update `@state: STEP-3-WORKING` in `WORK.md`
**Failure**: Spec unclear → escalate to `product-owner`; update `@state: STEP-1-CRITERIA` in `WORK.md`; document the gap for the PO
**Commit**: `feat(arch): design @id architecture`

---

### [STEP-3-WORKING]
**Owner**: `software-engineer`
**Entry condition**: Test stubs exist; at least one has `@pytest.mark.skip` OR all unskipped tests pass but skipped remain
**Action**:
1. Pick the next skipped `@id`; remove `@pytest.mark.skip`; write the test body (RED)
2. Write minimal production code until the test passes (GREEN)
3. Refactor if needed (REFACTOR)
4. Repeat from 1 for the next `@id`
**Exit (more @ids)**: Skipped tests still remain → stay in `[STEP-3-WORKING]`
**Exit (all done)**: No skipped tests remain → update `@state: STEP-4-READY` in `WORK.md`
**Commit**: After each `@id` or logical group

---

### [STEP-3-RED]
**Owner**: `software-engineer`
**Entry condition**: An unskipped test exists that fails (mid-cycle sub-state within STEP-3-WORKING)
**Action**: Write minimal production code to pass the failing test
**Exit**: Test passes → return to `[STEP-3-WORKING]`
**Note**: This sub-state is detected automatically during the TDD cycle. `WORK.md @state` stays `STEP-3-WORKING` unless the session ends mid-RED; in that case update to `STEP-3-RED` so the next session knows a test is currently failing.

---

### [STEP-4-READY]
**Owner**: `system-architect`
**Entry condition**: All tests implemented (no `@skip`) and passing
**Action**: Run all quality checks; semantic review against acceptance criteria
**Exit**: All checks pass → update `@state: STEP-5-READY` in `WORK.md`
**Failure**: Issues found → update `@state: STEP-3-WORKING` in `WORK.md`; document issues for the SE

---

### [STEP-5-READY]
**Owner**: `product-owner`
**Entry condition**: `WORK.md @state = STEP-5-READY` (set by SA after Step 4 approval)
**Action**: Demo and validate against acceptance criteria
**Exit**: Feature accepted → update `@state: STEP-5-MERGE` in `WORK.md`
**Failure**: Not accepted → update `@state: POST-MORTEM` in `WORK.md`

---

### [STEP-5-MERGE]
**Owner**: `software-engineer`
**Entry condition**: Feature accepted; on `feat/<stem>` or `fix/<stem>` branch; feature still in `in-progress/`
**Action**: Merge `@branch` to `main` with `--no-ff`; delete `@branch`
**Exit**: Merged → update `@state: STEP-5-COMPLETE` in `WORK.md`

---

### [STEP-5-COMPLETE]
**Owner**: `product-owner`
**Entry condition**: On `main`; `WORK.md @state = STEP-5-COMPLETE`; feature still in `in-progress/`
**Action**: Move feature from `in-progress/` to `completed/`
**Exit**: Feature moved → remove item from `WORK.md` active items; return to `[IDLE]`

---

### [POST-MORTEM]
**Owner**: `product-owner` (post-mortem doc) + `software-engineer` (fix branch)
**Entry condition**: Post-mortem file exists for current feature
**Action**: PO writes post-mortem in `docs/post-mortem/`; SE loads `skill version-control` and creates `fix/<stem>` branch from original start commit; PO updates `WORK.md`
**Exit**: Post-mortem committed, fix branch created → update `@state: STEP-2-ARCH`, `@branch: fix/<stem>` in `WORK.md`

---

## Session Protocol

### Session Start
1. Read `WORK.md` — find the active item; note `@id`, `@state`, `@branch`
2. Run auto-detection commands below to verify `@state` is correct
3. If detected state differs from `@state` in `WORK.md`, update `WORK.md` to match reality
4. Check prerequisites table above — if any missing, stop and report
5. Read the in-progress `.feature` file for `@id`
6. Run `git status` and `git branch --show-current` to confirm workspace matches `@branch`

### Session End
1. Update `WORK.md`: set `@state` to the new state
2. Commit any uncommitted work:
   ```bash
   git add -A && git commit -m "WIP(@id): <what was done>"
   ```
3. If a step is fully complete, use the proper commit message instead of WIP

### State Transition Rule
Every state transition is owned by the agent who completes the current state.
Before doing any further work: update `WORK.md` first, then commit the update.

```bash
git add WORK.md && git commit -m "chore: @id transition to @state"
```

---

## Auto-Detection Commands

Run these three checks to verify workspace consistency. Finer-grained state
verification happens during normal agent session work (reading the `.feature`
file, running tests, etc.).

```bash
# 1. Is there a feature in progress?
ls docs/features/in-progress/*.feature 2>/dev/null | grep -v ".gitkeep"

# 2. Are we on the correct branch?
git branch --show-current

# 3. Do test stubs exist when they should?
ls tests/features/*/ 2>/dev/null | head -1
```

---

## Output Style

- Report results, not process
- No narration around tool calls
- No restating tool output in prose
- No summaries of what was just done
