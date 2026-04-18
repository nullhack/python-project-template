# Workflow Improvement Feedback

Collected and clarified: 2026-04-17

---

## 1. PO Summarization Before Proceeding

**Problem:** The PO moves on too quickly without demonstrating understanding of what the stakeholder said.

**Research basis:** Active listening (Rogers & Farson, 1957) — the listener paraphrases what they heard in their own words, asks clarifying questions, then offers a concise summary of main points and intent before proceeding. This reduces misunderstanding, builds trust, and confirms the PO captured the right requirements.

**Proposed fix:** After each interview round, the PO must produce a "Here is what I understood" block before moving to stories or criteria:
1. Paraphrase the stakeholder's intent in the PO's own words
2. Identify any remaining ambiguities and ask targeted follow-up questions
3. Summarize the main points and confirm with the stakeholder before freezing discovery

This applies at Phase 1 (project discovery), Phase 2 (feature discovery), and before baseline.

---

## 2. Developer Avoids OO and Design Patterns — Code Smell Detection

**Problem:** The developer uses plain functions to avoid classes, SOLID, and Object Calisthenics. It does not smell the code to recognize when a simple function should be refactored into a class or design pattern.

**Root cause:** The rules list principles but do not teach the developer to recognize when complexity warrants a structural upgrade. The developer lacks a smell-triggered refactoring instinct.

**Proposed fix:** Add a code smell detection step to the REFACTOR phase. When a solution grows complex (e.g. a function accumulates state, multiple functions share data, behavior varies by type), the developer must ask: "Does this smell indicate I should refactor to a class or design pattern?" The answer drives the refactor, not just the line count or nesting rules.

See also: Item 5 (self-check examples) and Item 6 (ObjCal rule clarity).

---

## 3. Design Principle Priority Order Misleads

**Problem:** `YAGNI > KISS > DRY > SOLID > ObjCal > design patterns` implies that design patterns are a last resort and rarely needed. This is incorrect. Good design patterns are better than complex code.

**Python Zen:** The Zen of Python is missing from the priority order. Specifically: "Complex is better than complicated." This matters because:
- Good design patterns > complex code (patterns reduce complexity)
- Complex code > complicated code (complicated is hard to reason about)
- Complicated code > failing code (at least it runs)
- Failing code > no code (at least it exists)

**Proposed fix:** Replace the flat priority order with a quality hierarchy that reflects this:

```
1. No code (nothing implemented)          ← worst
2. Failing code (broken)
3. Complicated code (hard to reason about)
4. Complex code (many parts, but clear)
5. Code following YAGNI/KISS/DRY/SOLID/OC
6. Code using appropriate design patterns  ← best
```

Add the Python Zen reference: "Simple is better than complex. Complex is better than complicated." The goal is to reach level 6, not to stop at level 5 because "YAGNI says don't add patterns."

---

## 4. Architecture Approval by PO Is Hollow

**Problem:** The PO approves architecture at Step 2 but has no knowledge of ObjCal, SOLID, or whether entities are properly modeled. The PO always approves, making the gate meaningless.

**Additional problem:** The developer starts architecture for the in-progress feature without reading the full backlog. This leads to solutions that work for the current feature but require extensive rework when the next feature arrives, because the architecture did not account for the big picture.

**Proposed fix:**
- Remove PO architecture approval
- Replace with a developer self-declaration mental check covering:
  1. Read all backlog and in-progress feature files (discovery + entities sections at minimum)
  2. Identify entities, interactions, and constraints across all planned features
  3. Declare: "I have considered the full feature set. This architecture is the best design for the known requirements."
- The developer must justify the architecture against the full feature set, not just the current feature

---

## 5. Self-Check Table Lost Generalized Examples

**Problem:** The self-check table contains examples like `_x`, but the AI treats `_x` as a literal match rather than understanding it represents any short, meaningless variable name (e.g. `_val`, `_tmp`, `_data`). The rule lacks generalization guidance.

**Proposed fix:** For each ObjCal rule (and SOLID rule), add:
- A plain-English explanation of what the rule means
- A "bad" code example showing a violation
- A "good" code example showing compliance
- A generalization note: e.g. "This applies to any single-letter or abbreviation variable name, not just `_x`"

This makes the rules learnable and independently verifiable by both the developer and the reviewer.

---

## 6. Self-Declaration Accountability Format

**Problem:** The current self-declaration checklist is passive. The developer ticks boxes without being accountable for each claim.

**Proposed format:**

```
As a [agent-alias] I declare [item] follows [rule] — YES | NO
```

**If NO:**
- The developer generates a self-correction plan for the failed item
- The developer restarts the Red-Green-Refactor cycle from the affected tests
- Affected tests are marked as rework in TODO.md (format: open to proposal — consider `[R]` prefix or a `## Rework` section, respecting the 15-line limit)
- The cycle does not proceed to the reviewer until all declarations are YES

**If all YES:** proceed to reviewer as normal.

---

## 7. Reviewer Must Independently Verify — No Blind Acceptance

**Problem:** The reviewer accepts self-declared YES claims without independently verifying them. Worse, when the reviewer does not understand a rule (e.g. "types are first class" in ObjCal), it skips the check or accepts the developer's claim unchallenged.

**Two-part fix:**

1. **ObjCal (and SOLID) rules must have plain-English explanations + code examples** (see Item 5). The reviewer should never accept a claim it cannot independently verify.

2. **Reviewer scope:** The reviewer only audits YES declarations. Self-declared NO items are already known failures — the reviewer does not need to re-report them. The reviewer's job is to try to break what the developer claims is correct.

---

## 8. PO Not Refining Enough Before Proceeding

**Problem:** The PO moves through discovery phases without pushing back, asking follow-up questions, or confirming understanding. Stories and criteria are written on incomplete understanding.

**Proposed fix:** Enforce the active listening summarization protocol (Item 1) at every phase transition. The PO must not move to Phase 3 (Stories) until the stakeholder has confirmed the PO's paraphrase is accurate. The PO must not move to Phase 4 (Criteria) until each Rule has been validated against the stakeholder's intent.

---

## 9. Workflow Verbosity — Test Output and Fail-Fast

**Problem:** The workflow has unnecessary checks, fast test output is too verbose, and there is no fail-fast limit.

**Proposed fixes:**
- Fast test path (`test-fast`) should suppress passing test output — show only failures. Follow pytest best practice: use `-q` (quiet) flag or equivalent for the fast path.
- Add a fail-fast threshold configurable in `pyproject.toml` (e.g. `--maxfail=N`). Suggested default: 5.
- Remove redundant checks that are already covered by tooling (see Item 13).

---

## 10. Offload Templated Checks to Scripts

**Problem:** Repetitive checks (e.g. verifying `@id` uniqueness, orphan detection) are performed manually by agents, consuming context and introducing error.

**Proposed fix:** Identify all templated checks currently done by agents and create scripts for them. Agents invoke the script and act on the result. Candidates include:
- `@id` uniqueness check (already partially done by `gen-tests`)
- Orphan test detection (`gen-tests --orphans`)
- Self-declaration formatting validation
- Session state consistency check

---

## 11. docs/workflow.md Is Out of Date

**Problem:** `docs/workflow.md` does not reflect the current workflow. Specifically:
- It references a separate `discovery.md` file; discovery is now merged into `.feature` files
- The feature folder structure and conventions have changed
- The self-declaration section references a 21-item checklist that may no longer match

**Proposed fix:** Update `docs/workflow.md` to reflect the current state of the workflow, including:
- Discovery merged into `.feature` file description section
- Current folder structure (`backlog/`, `in-progress/`, `completed/`)
- Current self-declaration format (post Item 6 changes)
- Removal of references to `discovery.md` as a separate file

---

## 12. Squash on Merge for Feature Branches

**Problem:** Feature branches produce many small commits (one per test). Merging into `main` with a standard merge commit preserves all of them, making history noisy.

**Proposed fix:** Feature branches into `main` should be squashed. Document this in the `pr-management` skill as a required step. One squash commit per feature, with a summary message covering all tests implemented.

---

## 13. Code Smell in Self-Declaration

**Problem:** The self-declaration checklist does not include code smell detection. A developer can declare all SOLID/ObjCal rules as YES while the code is full of smells.

**Proposed fix:** Add a code smell section to the self-declaration, covering both categories:

**Standard smells (language-agnostic):**
- Long method
- Feature envy (method uses another class's data more than its own)
- Data clumps (same group of variables appear together repeatedly)
- Primitive obsession (using primitives instead of small objects)
- Shotgun surgery (one change requires many small changes across many classes)
- Divergent change (one class changed for many different reasons)
- Middle man (class delegates most of its work)

**Python-specific smells:**
- Bare `except:` clauses
- Mutable default arguments
- LBYL (Look Before You Leap) where EAFP (Easier to Ask Forgiveness than Permission) is idiomatic
- Using `type()` instead of `isinstance()`
- Overuse of `*args` / `**kwargs` hiding interface contracts

---

## 14. Session Continuity — Pick Up Where Left Off

**Problem:** When a session ends and a new one begins, the agent cannot reliably determine the current step, cycle phase, and next action. TODO.md provides some context but lacks precision for mid-cycle resumption.

**Proposed fix:** Open to proposal. Consider extending TODO.md with a `## Cycle State` section that captures:
- Current step (1-6)
- Current `@id` under work
- Current phase (RED / GREEN / REFACTOR / SELF-DECLARE / REVIEWER / COMMITTED)
- Last completed action
- Exact next action

The session-workflow skill should enforce reading and updating this section at session start and end. The goal: any agent, in any session, can read TODO.md and know exactly what to do next without re-reading the entire feature file.

---

## 15. ID Checks Are Redundant for Agents

**Problem:** Agents manually verify `@id` uniqueness and coverage. This is already done by `gen-tests`. Duplicating this check wastes context and distracts agents from implementation cycles.

**Proposed fix:** Remove manual `@id` verification from all agent checklists. Rely on `gen-tests` for ID validation. Agents should only run `gen-tests` and act on its output.

---

## 16. Session Memory and State Tracking

**Problem:** Agents lose session state between sessions. TODO.md is a 15-line bookmark but may not capture enough metadata to track complex multi-session features reliably.

**Proposed fix:** Open to proposal. Evaluate whether TODO.md extensions (Item 14) are sufficient, or whether a separate lightweight state file (e.g. `CYCLE.md` or `.opencode/state.json`) is needed. The artifact should be:
- Machine-readable by agents
- Human-readable for debugging
- Minimal — only what is needed to resume a session

---

## 17. AGENTS.md Is Generally Outdated

**Problem:** `AGENTS.md` does not fully reflect the current workflow, conventions, and tooling.

**Proposed fix:** After all other items are resolved, perform a full pass on `AGENTS.md` to align it with:
- Current feature file structure (discovery merged into `.feature`)
- Updated self-declaration format
- Updated principle priority order
- Removal of hollow PO architecture approval
- Any new scripts or tools added

---

## 18. Developer Does Not Read Full Backlog Before Architecture

**Problem:** The developer starts implementing the in-progress feature without reading the full backlog. This produces a working solution that requires extensive rework when the next feature arrives, because the architecture did not account for future requirements.

**Concrete example:** A feature was implemented correctly in isolation, but the next feature required significant structural changes because the original architecture assumed a design that did not compose well.

**Proposed fix:** At Step 2 (Architecture), the developer must:
1. Read the discovery and entities sections of every feature in `backlog/` and `in-progress/`
2. Identify cross-feature entities, shared interfaces, and likely extension points
3. Design the architecture to accommodate the known future, not just the current feature
4. Self-declare: "I have read all backlog features and this architecture accounts for the full known feature set"

This is distinct from Item 4 (hollow PO approval) — the fix here is about the developer's reading obligation before making architectural decisions.

---

## 19. Workflow Diagram — Redundancies and Late Error Detection

### Redundancies

**19a. Step 3 reviewer gate is a subset of Step 4's per-test reviewer gate**

Step 3 stops for reviewer approval of test design and semantic alignment before any implementation starts. Step 4 then repeats the same semantic alignment check per-test cycle. The Step 3 check reviews all tests at once before any code exists — but semantic alignment is best verified when both the test and the implementation can be seen side by side. The Step 3 review is premature and likely re-done anyway during Step 4.

**19b. Step 5 code review overlaps heavily with Step 4 self-declaration + per-test reviewer**

Step 5 checks Correctness, KISS, SOLID, ObjCal, Design Patterns, Tests, Code Quality (4a–4g). All of these except tooling (lint/coverage) were already covered by the 21-item self-declaration and per-test reviewer in Step 4. Step 5 implies a full re-audit of already-reviewed work, rather than a targeted spot-check of what is novel or risky.

**19c. `gen-tests --check` listed as a separate pre-step that nothing uses**

The `--check` dry-run appears in the tools table as "Before gen-tests" but is never referenced in the actual workflow steps. Either make it a mandatory gate or remove it.

**19d. Step 2 architecture commit and Step 3 gen-tests commit are always consecutive**

These two commits are always paired and never independently useful. Step 2 commits architecture, Step 3 immediately runs `gen-tests` and commits stubs. Combining them into one step would reduce overhead without losing traceability.

### Late Error Detection

**19e. Architecture locked before test bodies reveal structural problems**

Test bodies are written in Step 3 after the architecture is committed in Step 2. If a test body reveals an architectural flaw (wrong abstraction, missing entity), the developer must return to Step 2 — but the diagram has no explicit back-arrow from Step 3 to Step 2. The diagram implies Step 3 is always forward.

**19f. Decomposition check happens at the end of Phase 2, after all discovery is done**

If a feature is too large (>2 concerns, >8 examples), the split happens after discovery questions are already answered. The check should happen earlier — at Phase 1 when the feature list is identified, or at the start of Phase 2 before generating questions.

**19g. `lint + static-check` run only at handoff (end of Step 4)**

A type error or lint violation introduced in cycle 3 is not caught until all cycles are complete. Running these tools only at handoff means multiple commits may need to be unwound.

**19h. Production-grade input→output check first appears in Step 5**

Step 5 verifies that "output changes with input". This basic correctness property is not checked by the developer until the reviewer finds it. The developer's pre-mortem at end of Step 4 exists but is vague — it does not mandate the input→output check explicitly.

### Proposed Improvements

| # | Issue | Proposed change |
|---|---|---|
| A | Step 3 reviewer gate redundant with Step 4 | Merge Step 3 into Step 2: after architecture commit, run `gen-tests` to create stubs. Test body writing becomes the first action of Step 4 (write test → RED → GREEN → REFACTOR → SELF-DECLARE → REVIEWER → COMMIT). Removes one full reviewer interaction. |
| B | Step 5 is a full re-audit of already-reviewed work | Reframe Step 5 as a spot-check + tooling run: skip re-checking items covered by per-test reviewers; focus on (a) tooling — lint, static-check, coverage, orphans, (b) integration/system behavior, (c) semantic alignment of the feature as a whole. |
| C | Decomposition check too late | Move to Phase 1 (when feature stubs are created) and add a lightweight re-check at the start of Phase 2 (before generating questions). |
| D | `lint + static-check` run only at handoff | Run `lint + static-check` (not coverage) after each Step 4 commit as a fast sanity check. Keep full `test` with coverage at handoff only. |
| E | Step 2 + Step 3 always consecutive | Merge into one step: architecture + `gen-tests` stubs in one commit. Test bodies are the opening move of Step 4. |
| F | No back-arrow from Step 3 to Step 2 | Add explicit "if test body reveals arch flaw → back to Step 2" path in the diagram. |
| G | Input→output check first found by reviewer | Make it explicit in the developer's Step 4 self-verification (before handoff): run with two different inputs, confirm output differs. |

**Highest-value change: A + E combined.** Collapsing Steps 2+3 removes a full reviewer interaction. Test body writing as the opening move of Step 4 means architectural flaws are discovered immediately when the developer cannot make the test fail for the right reason.
