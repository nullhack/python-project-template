---
domain: software-craft
tags: [tdd, yagni, kiss, red-green-refactor, test-first]
last-updated: 2026-04-30
---

# Test-Driven Development

## Key Takeaways

- TDD follows three phases: RED (write a failing test), GREEN (write the minimum code to pass), REFACTOR (improve structure while keeping tests green) — Beck, 2002.
- "Minimum code" means no speculative generalization, no premature abstraction, no future-proofing — only what the test requires right now.
- YAGNI (You Aren't Gonna Need It — Beck & Jeffries, 1999) is the highest-priority design principle: never add functionality until it is required by a failing test.
- KISS (Keep It Simple, Stupid) is the second priority: choose the simplest implementation that passes the test.
- Tests specify observable behaviour, not implementation — a test that breaks during refactoring is coupled to the wrong thing (Meszaros, 2007).
- TDD has two quality phases: Design Phase (test-fast only, design correctness) followed by Conventions Phase (coverage, lint, pyright, docstrings) — only after design approval.

## Concepts

**RED-GREEN-REFACTOR Cycle** (Beck, 2002; Freeman & Pryce, 2009) — The TDD cycle has three phases: RED (write a test that specifies desired behavior and fails), GREEN (write the minimum production code to make the test pass), REFACTOR (improve the code's structure without changing behavior, keeping all tests green). Never skip RED — a test written after the code doesn't drive design.

**Minimum Code (GREEN phase)** — Write the simplest code that makes the failing test pass. This means: no speculative generalization (don't add parameters "for later"), no premature abstraction (don't extract a base class for one implementation), no future-proofing (don't handle cases the test doesn't require). If the test says "return 42", write `return 42` — not a configurable constant.

**Design Principle Priority** — When writing code or refactoring, follow this priority order (Beck & Jeffries, 1999; Martin, 2000): YAGNI > KISS > DRY > OC > SOLID > Design Patterns. YAGNI overrides everything: if the test doesn't require it, don't write it. KISS overrides DRY: sometimes a small duplication is simpler than the wrong abstraction.

**Test as Specification** (North, 2006) — In TDD, tests are specifications, not verification. Each test specifies one observable behavior. The test is written first because it drives the design of the production code, not because it verifies implementation after the fact.

**Specific Feedback Drives Improvement** (Hattie & Timperley, 2007) — The most effective feedback is specific about what needs to change and how. Self-declaration checklists (AGREE/DISAGREE on specific criteria) are more effective than vague "looks good" reviews because they force the reviewer to articulate exactly what passes and what fails.

**Test List Mechanics** — Build the test list from `@id` tags in the feature file. Order tests by dependency: fewest dependencies first, most impactful within that set. Work on one `@id` at a time (WIP limit of 1 per `@id`). Each `@id` gets a full RED-GREEN-REFACTOR cycle before moving to the next.

**Commit Discipline** — Refactor commits are separate from feature commits. Never mix a structural change with a behavior addition in one commit — this keeps history bisectable and every commit leaves tests green. See [[software-craft/git-conventions]] for granular and squashed commit formats.

**Design-Only Refactoring** — During REFACTOR, apply only design transformations (SOLID, OC, DRY, KISS, YAGNI, pattern catalogue entries). Do not apply convention compliance (import ordering, docstring additions, type annotations, format changes) — those belong in the Conventions Phase after design approval.

**Two-Phase Quality Gate** — TDD operates in two distinct phases with different tooling and goals. **Design Phase** (during tdd-cycle): run `test-fast` only; no lint, no pyright, no docstring checks, no coverage unit tests. Write minimum code following best design principles (YAGNI > KISS > DRY > OC > SOLID > patterns). The goal is proving design correctness — never waste convention work on code that might be redesigned. Exit is gated by the `design_declared` condition. **Conventions Phase** (after design approval): add coverage unit tests, run lint, run pyright, add docstrings. These are convention concerns that the reviewer explicitly requests only after design is approved. Running lint or coverage on code that might be redesigned is wasted effort.

## Content

### RED Phase Rules

- Write exactly one test for the next unimplemented behavior
- The test must fail for the right reason (not a syntax error)
- The test must express the desired behavior from the user's perspective

### GREEN Phase Rules

- Write the minimum code to pass the test
- Hard-coded values are acceptable if the test only requires that value
- Do not add parameters, abstractions, or features the test doesn't require
- If the test is trivially satisfied, write a more specific test

### REFACTOR Phase Rules

- All tests must remain green throughout refactoring
- Only refactor if there is a test that would break if the refactoring is wrong
- Apply design principles in priority order: YAGNI > KISS > DRY > OC > SOLID > patterns
- If no improvement is needed, skip refactoring and proceed to the next test
- Design-only refactoring: no convention compliance during this phase

### Test List

- List all `@id` tags from the feature file before starting
- Order by fewest dependencies first; most impactful within that set
- Mark each `@id` as pending, in-progress, or done
- WIP limit: exactly one `@id` in-progress at a time

### Design Phase Rules (during tdd-cycle)

- Run `test-fast` only — no lint, no pyright, no docstring checks, no coverage unit tests
- Write minimum code following design principle priority: YAGNI > KISS > DRY > OC > SOLID > patterns
- Refactor for design correctness only — no convention compliance
- The goal is proving design correctness, not convention compliance
- Exit gated by `design_declared` condition (all 6 checks == true)

### Conventions Phase Rules (after design approval)

- Add coverage unit tests for uncovered branches in `tests/unit/` — never in `tests/features/`. The `tests/features/` directory is exclusively for `@id`-linked BDD scenario tests. Coverage-boosting tests for implementation branches are unit contract tests, not feature tests
- Run lint (`uv run task lint`), pyright (`uv run task static-check`), full test suite
- Add docstrings to all public classes and methods
- Add type annotations to all public signatures
- Only after design approval — never before

### Commit Strategy

- Feature commits: one per `@id` achievement (RED→GREEN→REFACTOR)
- Refactor commits: separate from feature commits, one per catalogue entry
- See [[software-craft/git-conventions]] for commit message format

## Related

- [[requirements/gherkin]]
- [[architecture/technical-design]]
- [[software-craft/test-design]]
- [[software-craft/git-conventions]]
- [[software-craft/object-calisthenics]]
- [[software-craft/smell-catalogue]] — smells are identified and resolved during REFACTOR phase
- [[software-craft/design-patterns]] — patterns are applied during REFACTOR when smells trigger them
- [[software-craft/refactoring-techniques]] — refactoring techniques are applied during REFACTOR phase
- [[software-craft/solid]] — SOLID is part of the design principle priority
- [[software-craft/refactoring]] — when and how to refactor, clean code, technical debt