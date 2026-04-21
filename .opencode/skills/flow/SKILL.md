---
name: flow
version: "1.0"
description: Feature workflow protocol — read FLOW.md, auto-detect state, resume from checkpoint, update state
author: software-engineer
audience: all-agents
workflow: session-management
---

# Feature Workflow Protocol

This skill defines the single-feature-at-a-time workflow state machine. Every feature flows through 5 steps. Only ONE feature is in progress at any time. The filesystem enforces this.

## Prerequisites

Before starting any flow, verify these exist. If any are missing, stop and alert the human.

| Requirement | Verification Command | Missing Action |
|---|---|---|
| Agent: product-owner | `test -f .opencode/agents/product-owner.md` | Create agent file |
| Agent: system-architect | `test -f .opencode/agents/system-architect.md` | Create agent file |
| Agent: software-engineer | `test -f .opencode/agents/software-engineer.md` | Create agent file |
| Skill: run-session | `test -f .opencode/skills/run-session/SKILL.md` | Install skill |
| Skill: define-scope | `test -f .opencode/skills/define-scope/SKILL.md` | Install skill |
| Skill: architect | `test -f .opencode/skills/architect/SKILL.md` | Install skill |
| Skill: implement | `test -f .opencode/skills/implement/SKILL.md` | Install skill |
| Skill: verify | `test -f .opencode/skills/verify/SKILL.md` | Install skill |
| Skill: version-control | `test -f .opencode/skills/version-control/SKILL.md` | Install skill |
| Tool: uv | `command -v uv` | Install uv |
| Tool: git | `command -v git` | Install git |
| Directory: docs/features/ | `test -d docs/features/backlog` | Run setup-project |
| Directory: docs/adr/ | `test -d docs/adr` | Create directory |
| FLOW.md | `test -f FLOW.md` | Create from template |

## State Machine

States are checked IN ORDER. The first matching state is the current state.

### Detection Rules

1. **No file in `docs/features/in-progress/`** → [IDLE]
2. **Feature in in-progress, no `Status: BASELINED`** → [STEP-1-DISCOVERY]
3. **Feature has `Status: BASELINED`, no `Rule:` blocks** → [STEP-1-STORIES]
4. **Feature has `Rule:` blocks, no `Example:` with @id** → [STEP-1-CRITERIA]
5. **Feature has @id tags, no feat/ or fix/ branch exists** → [STEP-2-READY]
6. **On feature branch, no test stubs in `tests/features/<stem>/`** → [STEP-2-ARCH]
7. **Test stubs exist, any have `@pytest.mark.skip`** → [STEP-3-READY]
8. **Unskipped test exists that fails** → [STEP-3-RED]
9. **All unskipped tests pass, skipped tests remain** → [STEP-3-GREEN]
10. **All tests pass, no skipped tests** → [STEP-4-READY]
11. **Manual state set by SA after Step 4 approval** → [STEP-5-READY]
12. **On main branch, feature still in in-progress/** → [STEP-5-MERGE]
13. **Post-mortem file exists for current feature** → [POST-MORTEM]

### State Details

#### [IDLE] → Waiting for feature selection
**Owner**: product-owner
**Detect**: No file in `docs/features/in-progress/`
**Action**: Select feature from backlog/ and move to in-progress/
**Next**: [STEP-1-DISCOVERY]

#### [STEP-1-DISCOVERY] → Requirements discovery
**Owner**: product-owner
**Detect**: Feature in in-progress/, no `Status: BASELINED` in file
**Action**: Interview stakeholder, update scope_journal.md, discovery.md, glossary.md
**Success**: Feature baselined → [STEP-1-STORIES]
**Failure**: More discovery needed → Stay in [STEP-1-DISCOVERY]

#### [STEP-1-STORIES] → Write user stories
**Owner**: product-owner
**Detect**: Feature has `Status: BASELINED`, no `Rule:` blocks
**Action**: Write Rule: blocks with INVEST criteria
**Success**: Stories complete → [STEP-1-CRITERIA]

#### [STEP-1-CRITERIA] → Write acceptance criteria
**Owner**: product-owner
**Detect**: Feature has `Rule:` blocks, no `Example:` blocks with @id
**Action**: Write Example: blocks with @id tags
**Success**: Criteria complete → [STEP-2-READY]
**Commit**: `feat(criteria): write acceptance criteria for <name>`

#### [STEP-2-READY] → Ready for architecture
**Owner**: system-architect
**Detect**: Feature has @id tags, no feat/<stem> branch exists
**Action**: Create branch feat/<stem> from main
**Success**: Branch created → [STEP-2-ARCH]

#### [STEP-2-ARCH] → Design architecture
**Owner**: system-architect
**Detect**: On feat/<stem> branch, no test stubs in tests/features/<stem>/
**Action**: Read feature, design stubs, write ADRs, update domain-model.md
**Success**: Run `uv run task test-fast` generates stubs → [STEP-3-READY]
**Failure**: Spec unclear → [STEP-1-DISCOVERY] (escalate to PO)
**Commit**: `feat(arch): design <feature> architecture`

#### [STEP-3-READY] → Ready for TDD
**Owner**: software-engineer
**Detect**: Test stubs exist, some have @pytest.mark.skip
**Action**: Pick first skipped @id, remove skip, write test
**Success**: Test written and fails → [STEP-3-RED]

#### [STEP-3-RED] → Test failing
**Owner**: software-engineer
**Detect**: Unskipped test exists that fails
**Action**: Write minimal code to pass
**Success**: Test passes → [STEP-3-GREEN]

#### [STEP-3-GREEN] → Test passing
**Owner**: software-engineer
**Detect**: All unskipped tests pass, more skipped tests remain
**Action**: Refactor if needed, then pick next @id
**Success**: More @ids → [STEP-3-READY]
**Success**: All @ids done → [STEP-4-READY]
**Commit**: After each @id or logical group

#### [STEP-4-READY] → Ready for verification
**Owner**: system-architect
**Detect**: All tests implemented (no @skip) and passing
**Action**: Run all quality checks, semantic review
**Success**: All checks pass → [STEP-5-READY]
**Failure**: Issues found → [STEP-3-READY] (document issues)

#### [STEP-5-READY] → Ready for acceptance
**Owner**: product-owner
**Detect**: Manual state (set after Step 4 approval)
**Action**: Demo and validate against criteria
**Success**: Feature accepted → [STEP-5-MERGE]
**Failure**: Not accepted → [POST-MORTEM]

#### [STEP-5-MERGE] → Merge to main
**Owner**: software-engineer
**Detect**: Feature accepted, still on feature branch
**Action**: Merge feat/<stem> to main with --no-ff
**Success**: Merged → [STEP-5-COMPLETE]

#### [STEP-5-COMPLETE] → Feature complete
**Owner**: product-owner
**Detect**: On main branch, feature still in in-progress/
**Action**: Move feature from in-progress/ to completed/
**Success**: Feature moved → [IDLE]

#### [POST-MORTEM] → Failed feature analysis
**Owner**: product-owner
**Detect**: Post-mortem file exists for current feature
**Action**: Write post-mortem, create fix/<stem> branch
**Success**: Post-mortem complete → [STEP-2-ARCH]

## Session Protocol

### Session Start

1. Read `FLOW.md` — find current feature, branch, status.
2. Run `detect-state` (see below) to verify the state is correct.
3. If the detected state differs from `FLOW.md` Status, update `FLOW.md` to match reality.
4. Check prerequisites table (above). If any are missing, stop and report.
5. If a feature is active, read the in-progress `.feature` file.
6. Run `git status` and `git branch --show-current` to understand workspace state.
7. Confirm scope: you are working on exactly one step of one feature.

### Session End

1. Update `FLOW.md`:
   - Set Status to the detected state
   - Update Session Log with what was done
   - Update `Next:` line with one concrete action
2. Commit any uncommitted work (even WIP):
   ```bash
   git add -A
   git commit -m "WIP(<feature-stem>): <what was done>"
   ```
3. If a step is fully complete, use the proper commit message instead of WIP.

### Step Completion Protocol

When a step completes within a session:

1. Update `FLOW.md` to reflect the completed step before doing any other work.
2. Commit the `FLOW.md` update:
   ```bash
   git add FLOW.md
   git commit -m "chore: complete step <N> for <feature-stem>"
   ```
3. Only then begin the next step (in a new session where possible).

## Auto-Detection

To detect the current state automatically, run these checks in order:

```bash
# 1. Check for in-progress feature
ls docs/features/in-progress/*.feature 2>/dev/null | grep -v ".gitkeep"
# If empty → [IDLE]

# 2. Check feature baselined
grep -q "Status: BASELINED" docs/features/in-progress/*.feature
# If no match → [STEP-1-DISCOVERY]

# 3. Check for Rule blocks
grep -q "^Rule:" docs/features/in-progress/*.feature
# If no match → [STEP-1-STORIES]

# 4. Check for Example blocks with @id
grep -q "@id:" docs/features/in-progress/*.feature
# If no match → [STEP-1-CRITERIA]

# 5. Check for feature branch
git branch --show-current | grep -E "^feat/|^fix/"
# If no match → [STEP-2-READY]

# 6. Check for test stubs
ls tests/features/*/ 2>/dev/null | head -1
# If empty → [STEP-2-ARCH]

# 7. Check for skipped tests
grep -r "@pytest.mark.skip" tests/features/*/ 2>/dev/null
# If found → [STEP-3-READY] or [STEP-3-GREEN]
# If not found → [STEP-4-READY]

# 8. Check test failures
uv run task test-fast 2>&1 | grep -E "FAILED|ERROR"
# If found → [STEP-3-RED]
# If not found and on main → [STEP-5-MERGE]
```

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
<!-- Append new entries, never delete old ones -->
**YYYY-MM-DD HH:MM** — <agent> — <state> — <action>

## Next
Run @<agent-name> — <one concrete action>
```

## Rules

1. Never skip reading `FLOW.md` at session start
2. Never end a session without updating `FLOW.md`
3. Never leave uncommitted changes — commit as WIP if needed
4. One step per session where possible; do not start Step N+1 in the same session as Step N
5. The "Next" line must be actionable enough that a fresh AI can execute it without asking questions
6. When a step completes, update `FLOW.md` and commit **before** any further work
7. The Session Log is append-only — never delete old entries
8. If `FLOW.md` is missing, create it from the template before doing any other work
9. If detected state differs from `FLOW.md` Status, trust the detected state and update `FLOW.md`

## Output Style

Use minimal output. Every message must contain only what the next agent or stakeholder needs to continue — findings, status, decisions, blockers, and the Next: line.

- Use the fewest, least verbose tool calls necessary to achieve the step's goal
- Report results, not process
- No narration before or after tool calls
- No restating tool output in prose
- No summaries of what was just done
- Always close with Next:
