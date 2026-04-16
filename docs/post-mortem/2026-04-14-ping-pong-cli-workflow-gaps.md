# Post-Mortem: ping-pong-cli — Workflow Gaps (v3.1)

## Release Details

| Field | Value |
|-------|-------|
| Version | v3.1.20260414 |
| Date | April 14, 2026 |
| Feature | ping-pong-cli |
| Status | APPROVED and shipped |
| Broken | Yes — game doesn't work |

---

## What Was Shipped

`ping_pong_cli/game.py` — 240 lines:

- 15 top-level functions, zero classes
- No keyboard input (`get_input()` always returns `""`)
- Runs a hardcoded 100-frame demo then exits
- Uses raw `int` and `tuple[int,int]` — no value objects
- `render_game` has 3 levels of nesting
- 8-parameter function signatures

Yet it passed: lint, typecheck, 100% coverage, 31 tests, reviewer APPROVED.

---

## What Failed

The acceptance criteria said:
> Given: The game is running and waiting for input
> When: The left or right arrow key is pressed
> Then: The paddle moves

The implementation maps this to a unit test of `update_player("W")`. That test proves the function works in isolation. No test verifies that keyboard input actually reaches `update_player`.

The game shipped with the acceptance criterion satisfied in a narrow technical sense ("paddle moves when 'W' is passed to the function") but broken in the broad user sense ("paddle doesn't move when I press W in the running game").

---

## Gap 1: Acceptance Criteria Don't Require End-to-End Verification

### Problem

The `scope` skill defines "Then must be a single observable, measurable outcome" but doesn't define **observable by whom**. The developer interpreted this as "observable in a unit test" — test calls `update_player("W")` returns expected result.

### Fix

In `scope` skill, add:

> **Observable means observable by the end user.** If the criterion says "When the user presses W", the test must verify that pressing W in the running app produces the expected result — not just that calling `update_player("W")` returns the right number. If end-to-end testing isn't feasible, the criterion must explicitly state the boundary (e.g., "When update_player receives 'W'") so the gap is visible.

In `verify` skill, add:

> **Acceptance Criteria vs. Reality Check**
>
> For each criterion whose Given/When/Then describes user-facing behavior:
> - Read the test that covers it
> - If the test only exercises an internal function without going through the actual user-facing entry point, flag it as **COVERED BUT NOT VERIFIED**
> - A criterion that says "When the user presses W" is NOT verified by `test_update_player("W")` — it's verified by a test or manual check that sends W to the running app
>
> Any COVERED BUT NOT VERIFIED criterion → REJECTED

---

## Gap 2: Object Calisthenics Listed But Not Enforced by Reviewer

### Problem

The `verify` skill listed all 9 Object Calisthenics rules. The reviewer read them but approved code with:

| # | Rule | Violation in shipped code |
|---|------|--------------------------|
| 3 | Wrap primitives | `PlayerPosition = int`, `BallState = tuple[int,int]` are type aliases, not value objects |
| 4 | First-class collections | No collection classes |
| 7 | Small entities | `run_game_loop` is ~40 lines |
| 8 | ≤ 2 instance vars | No classes at all, but 8-parameter function signatures |

The skill didn't say **what to do when violations are found**. Violations were treated as observations, not blockers.

### Fix

In `verify` skill, replace ObjCal prose with a structured table:

> **Object Calisthenics — ANY violation is a REJECT**
>
> | # | Rule | How to check | PASS/FAIL |
> |---|------|-------------|-----------|
> | 1 | One level of indentation | Check nest depth in source |
> | 2 | No `else` after return | Search for `else` inside functions |
> | 3 | Wrap primitives | Bare `int`, `str` as domain concepts = FAIL |
> | 4 | First-class collections | `list[Type]` not wrapped = FAIL |
> | 5 | One dot per line | `a.b.c()` = FAIL |
> | 6 | No abbreviations | `calc`, `mgr` = FAIL |
> | 7 | Small entities | Lines per function >20 or class >50 = FAIL |
> | 8 | ≤ 2 instance vars | More than 2 per class = FAIL |
> | 9 | No getters/setters | `get_x()`, `set_x()` = FAIL |

---

## Gap 3: REFACTOR Step Has No Verification Gate

### Problem

The `implementation` skill says to apply DRY, SOLID, Object Calisthenics during REFACTOR, but when done, it only runs `task test`, `task lint`, `task static-check`. None of those tools check nesting depth, function length, or value objects. The developer skips the self-check, runs the three commands, they all pass.

### Fix

In `implementation` skill, add after REFACTOR section:

> **REFACTOR Self-Check (MANDATORY before commit)**
>
> 1. Count lines per function you changed. Any >20 → extract helper
> 2. Check nesting. Any >2 levels → extract function
> 3. Check bare primitives as domain concepts. `int` for paddle position → value object
> 4. Check parameters per function. >4 positional → group into dataclass
>
> If you skip this step, the reviewer WILL reject your code.

---

## Gap 4: `timeout 10s uv run task run` Is Not a Playability Test

### Problem

The `verify` skill said: "check that startup completes without error before the timeout." The demo ran for 1.6 seconds and exited cleanly — startup completed, no error. The app passed without being interactive at all.

### Fix

In `verify` skill, replace the timeout check with:

> **For apps with user interaction** (games, CLIs with prompts, web servers):
> - Run the app, provide sample input via stdin/subprocess
> - Verify output changes in response to input
> - A hardcoded demo that auto-plays without input is NOT a playability test
>
> If the app doesn't respond to user input → REJECTED

---

## Gap 5: Tests Verify Functions, Not Behavior

### Problem

The `tdd` skill produces unit tests. Every test calls an isolated function. No test sends input to the running game. No test verifies the game loop integrates these functions correctly. 31 tests pass with 100% coverage but none test the actual gameplay loop.

### Fix

In `tdd` skill, add:

> **Integration Test Requirement**
>
> For features with multiple components (game loops, handlers, pipelines):
> - Add at least ONE `@pytest.mark.integration` test
> - Test must exercise the full path from entry point to observable outcome
> - Must NOT call internal helpers directly — use the public entry point

---

## Summary

| Gap | Skill | Problem | Fix |
|-----|-------|---------|-----|
| 1 | scope + verify | "Observable" undefined = unit test passes | Define user-observable; add COVERED BUT NOT VERIFIED |
| 2 | verify | Object Calisthenics listed = suggestions | Any rule FAIL = REJECTED (table) |
| 3 | implementation | REFACTOR has no self-check gate | Add mandatory line/nesting check |
| 4 | verify | `timeout` = "doesn't hang" not "works" | Must accept and respond to input |
| 5 | tdd | All unit, no integration | Require one integration test |

---

## Root Cause

The skills already contained the right standards. The problem is that violations were treated as observations, not blockers. Each check needs a clear **FAIL = REJECTED** consequence with a structured table to fill in — so violations can't be glossed over in prose.
