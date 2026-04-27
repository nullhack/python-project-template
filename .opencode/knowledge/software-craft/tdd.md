---
domain: software-craft
tags: [tdd, refactoring, red-green-refactor, testing]
last-updated: 2026-04-26
---

# TDD and Refactoring

## Key Takeaways

- Refactoring is a behaviour-preserving structural transformation; public interface changes are feature changes, not refactorings.
- Refactor only while all tests pass (the green bar rule); every step must leave `test-fast` green.
- Wear one hat at a time: the feature hat (RED-GREEN) or the refactoring hat (REFACTOR); never mix them in the same step.
- Refactor opportunistically after GREEN, or preparatorily before RED to make the next feature easier.
- Keep refactoring commits separate from feature commits; never mix structural cleanup with behaviour addition.
- When a test breaks during refactoring, diagnose first: either the test couples to internals (rewrite it) or the "refactoring" changed observable behaviour (it's a feature change — revert and RED-GREEN-REFACTOR it).

## Concepts

**The Definition**: A refactoring is a behaviour-preserving transformation of internal structure. If the transformation changes observable behaviour, it is not a refactoring — it is a feature change requiring its own RED-GREEN-REFACTOR cycle. Public interface changes (adding, removing, modifying a function's signature or observable behaviour) are feature changes, not refactorings.

**The Green Bar Rule**: Refactoring is only permitted while all existing tests pass. Every individual refactoring step must leave `test-fast` green. There are no exceptions.

**The Two-Hats Rule**: Wear one hat at a time. The feature hat allows writing a failing test and making it pass (RED to GREEN). The refactoring hat allows restructuring passing code — never adding new behaviour. Never mix hats in the same step. If you discover a refactoring is needed while making a test pass, note it, finish GREEN first, then switch hats.

**When to Refactor**: Refactor during the REFACTOR phase after GREEN (opportunistic). Refactor preparatorily before RED when the current structure would make the next `@id` awkward to implement. For preparatory refactoring: put on the refactoring hat first, refactor until the feature is easy to add, commit separately, then put on the feature hat and run RED-GREEN-REFACTOR normally.

**Commit Discipline**: Refactoring commits are always separate from feature commits. Preparatory refactoring uses `refactor(<feature-stem>): <what>`. REFACTOR phase uses the same format. Feature additions use `feat(<feature-stem>): <what>`. Never mix structural cleanup with behaviour addition in one commit — this keeps history bisectable and CI green at every commit.

**When a Refactoring Breaks a Test**: A refactoring that breaks a test is not a refactoring. Diagnose: Is the test testing internal structure rather than observable behaviour? If yes, rewrite the test to use the public interface, re-apply the refactoring, and confirm `test-fast` is green. If no, the "refactoring" changed observable behaviour — this is a feature change. Revert the step, put on the feature hat, and run RED-GREEN-REFACTOR explicitly.

## Content

### The Definition

A refactoring is a **behaviour-preserving** transformation of internal structure. If the transformation changes observable behaviour, it is not a refactoring — it is a feature change, and requires its own RED-GREEN-REFACTOR cycle.

**Public interface changes are feature changes.** Adding, removing, or modifying a function's signature or observable behaviour is not refactoring — it changes the contract that callers and tests depend on. Tests that break because the public contract changed are working correctly; update them as part of a RED-GREEN-REFACTOR cycle. See [[software-craft/test-design]] for the full refactor-safety spectrum and strategies to minimise test breakage during interface evolution.

### The Green Bar Rule (absolute)

Refactoring is only permitted while all existing tests pass. Every individual refactoring step must leave `test-fast` green. There are no exceptions.

### The Two-Hats Rule

Wear one hat at a time:

| Hat | Activity | Allowed during this hat |
|---|---|---|
| Feature hat | RED to GREEN | Write failing test, write minimum code to pass |
| Refactoring hat | REFACTOR | Restructure passing code; never add new behaviour |

Never mix hats in the same step. If you discover a refactoring is needed while making a test pass (GREEN), note it — finish GREEN first, then switch hats.

### When to Refactor

**REFACTOR phase (opportunistic)**: After GREEN — `test-fast` passes for the current `@id`. Now restructure.

**Preparatory refactoring (before RED)**: When the current structure would make the next `@id` awkward to implement:
1. Put on the refactoring hat first
2. Refactor until the feature is easy to add
3. Commit the preparatory refactoring separately
4. Then put on the feature hat and run RED-GREEN-REFACTOR normally

Beck: "For each desired change, make the change easy (warning: this may be hard), then make the easy change."

### Commit Discipline

Refactoring commits are always separate from feature commits.

| Commit type | Message format | When |
|---|---|---|
| Preparatory refactoring | `refactor(<feature-stem>): <what>` | Before RED, to make the feature easier |
| REFACTOR phase | `refactor(<feature-stem>): <what>` | After GREEN, cleaning up the green code |
| Feature addition | `feat(<feature-stem>): <what>` | After GREEN (never mixed with refactor) |

Never mix a structural cleanup with a behaviour addition in one commit. This keeps history bisectable and CI green at every commit.

### Key Catalogue Entries

**Extract Function** — Pull a cohesive fragment into a named function. Trigger: a fragment needs a comment to explain what it does. Outcome: the extracted function's name makes the comment unnecessary.

**Extract Class** — Split a class doing two jobs. Trigger: a data cluster (2-3 fields that always travel together) with related behaviour that could be named independently. Outcome: each class has one reason to change.

**Introduce Parameter Object** — Replace a recurring parameter group with a dedicated object. Trigger: the same 2+ parameters appear together across multiple function signatures. Outcome: a named type captures the concept; callers are simplified.

**Replace Primitive with Object** — Elevate a domain concept represented as a raw primitive to its own type. Trigger: a primitive has validation rules, formatting logic, or operations repeated at every call site. Outcome: behaviour moves into the type; callers are protected from invalid states.

**Decompose Conditional / Guard Clauses** — Flatten nested conditional logic to 2 or fewer levels. Trigger: OC-1 violation (nesting beyond one indent level per method). Outcome: each exit condition is an early return; the happy path is at the left margin; no `else` after `return`.

### When a Refactoring Breaks a Test

A refactoring that breaks a test is not a refactoring. Stop and diagnose:

1. Is the test testing internal structure (private methods, specific call chains, concrete types) rather than observable behaviour?
   - YES: Rewrite the test to use the public interface. Re-apply the refactoring step. Run `test-fast` — must be green.
   - NO: The "refactoring" changed observable behaviour. This is a feature change. Revert the step. Put on the feature hat. Run RED-GREEN-REFACTOR for it explicitly.

Never delete a failing test without diagnosing it first.

## Related

- [[software-craft/smell-catalogue]] — smells identified during REFACTOR phase
- [[software-craft/design-patterns]] — patterns applied during REFACTOR phase
- [[software-craft/solid]] — SOLID checks during REFACTOR
- [[software-craft/object-calisthenics]] — OC rules checked during REFACTOR
- [[software-craft/self-declaration]] — declaration checklist before exiting REFACTOR
- [[software-craft/test-design]] — refactor-safe test design, public interface evolution