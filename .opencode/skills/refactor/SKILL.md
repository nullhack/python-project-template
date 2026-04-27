---
name: refactor
description: Safe refactoring protocol for TDD — green bar rule, two-hats discipline, preparatory refactoring, and smell catalogue
version: "2.0"
author: software-engineer
audience: software-engineer
workflow: feature-lifecycle
---

# Refactor

Load this skill when entering the REFACTOR phase of a TDD cycle, or before starting RED on a new `@id` when preparatory refactoring is needed.

Sources: Fowler *Refactoring* 2nd ed. (2018); Beck *Canon TDD* (2023); Beck *Tidy First?* (2023); Martin *SOLID* (2000); Bay *Object Calisthenics* (2005); Shvets *Refactoring.Guru* (2014–present). See `docs/research/oop-design.md` entries 33–36 and `docs/research/refactoring-empirical.md`.

---

## The Definition

A refactoring is a **behaviour-preserving** transformation of internal structure. If the transformation changes observable behaviour, it is not a refactoring — it is a feature change, and requires its own RED-GREEN-REFACTOR cycle. See [[software-craft/tdd]] for the full definition and rules.

---

## The Green Bar Rule (absolute)

Refactoring is only permitted while all existing tests pass. Every individual refactoring step must leave `test-fast` green. There are no exceptions. See [[software-craft/tdd]] for the full rule.

---

## The Two-Hats Rule

Wear one hat at a time. Never mix the feature hat (RED-GREEN) and the refactoring hat (REFACTOR) in the same step. If you discover a refactoring is needed while making a test pass, note it — finish GREEN first, then switch hats. See [[software-craft/tdd]] for the full rule.

---

## When to Use

### 1. REFACTOR phase (opportunistic)

After GREEN: `test-fast` passes for the current `@id`. Now restructure.

### 2. Preparatory refactoring (before RED)

When the current structure would make the next `@id` awkward to implement:
- Put on the **refactoring hat first**
- Refactor until the feature is easy to add
- Commit the preparatory refactoring separately (see Commit Discipline)
- Then put on the feature hat and run RED-GREEN-REFACTOR normally

Beck: *"For each desired change, make the change easy (warning: this may be hard), then make the easy change."*

---

## Step-by-Step

### Step 1 — Identify the smell

Run the smell checklist from your Self-Declaration or from the Architecture Smell Check. See [[software-craft/smell-catalogue]] for the full smell catalogue (Bloaters, OO Abusers, Change Preventers, Dispensables, Couplers) with signals and likely catalogue entries.

If pattern smell detected: load `skill apply-patterns` and see [[software-craft/design-patterns#concepts]] for pattern selection guidance.

### Step 2 — Apply one catalogue entry at a time

Apply a **single** catalogue entry, then run `test-fast` before moving to the next.

Never batch multiple catalogue entries into one step — you lose the ability to pinpoint which step broke something.

### Step 3 — Run after each step

```bash
uv run task test-fast
```

All tests green → proceed to next catalogue entry.
Any test red → see "When a Refactoring Breaks a Test" below.

### Step 4 — Commit when smell-free

Once no smells remain and `test-fast` is green:

```bash
uv run task test-fast   # must pass
```

Commit (see Commit Discipline below).

---

## When a Refactoring Breaks a Test

A refactoring that breaks a test is **not a refactoring**. Stop. Diagnose using the flow in [[software-craft/tdd]]. Never delete a failing test without diagnosing it first.

If the test is coupled to implementation details (private methods, internal state, specific call chains, concrete types), rewrite the test to use the public interface. See [[software-craft/test-design]] for refactor-safe test design patterns and the refactor-safety spectrum.

---

## Commit Discipline

Refactoring commits are always **separate** from feature commits. See [[software-craft/tdd]] for the full commit message format table.

Never mix a structural cleanup with a behaviour addition in one commit. This keeps history bisectable and CI green at every commit.

---

## Self-Declaration Check (before exiting REFACTOR)

Before marking the `@id` complete, verify all items in the 25-item Self-Declaration. Each failed item is a smell — apply the catalogue entry, run `test-fast`, then re-check. See [[software-craft/self-declaration]] for the full checklist.

### Green Bar
- [ ] `test-fast` passes
- [ ] No smell from the checklist in Step 1 remains

### Object Calisthenics
See [[software-craft/object-calisthenics]] for all nine rules and violation signals.

### SOLID
See [[software-craft/solid]] for all five principles, checks, and violation signals.

### Law of Demeter / Tell, Don't Ask / CQS
See [[software-craft/tdd]] for these principles and their violation signals.

### Design Clarity Signals
See [[software-craft/code-quality]] for the full set of design clarity principles.

### Type and documentation hygiene
- [ ] Type annotations present on all public signatures
- [ ] Documentation present on all public classes and methods