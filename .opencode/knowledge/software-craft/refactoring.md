---
domain: software-craft
tags: [refactoring, clean-code, technical-debt, fowler, code-quality]
last-updated: 2026-04-30
---

# Refactoring

## Key Takeaways

- Clean code is obvious for other programmers, contains no duplication, has a minimal number of moving parts, passes all tests, and is cheaper to maintain (Shvets, 2014).
- Technical debt is the accumulated cost of shortcuts; like financial debt, it compounds — the longer you wait to refactor, the more dependent code must be reworked (Cunningham; Shvets, 2014).
- Refactor when: Rule of Three (third duplication triggers refactor), when adding a feature, when fixing a bug, during code review (Fowler, 1999; Shvets, 2014).
- Refactor how: small steps, tests green after each step, one refactoring at a time, never mix refactoring with feature changes (Fowler, 1999; Shvets, 2014).

## Concepts

**Clean Code** — The goal of refactoring is to transform messy code into clean code without changing its external behaviour. Clean code is: (1) obvious for other programmers — good naming, no magic numbers, no bloated classes or methods; (2) free of duplication — each change point has a single source; (3) minimal — fewer classes and moving parts means less to keep in your head, less maintenance, fewer bugs; (4) tested — code that passes all tests, not just 95% of them; (5) cheaper to maintain — the economic justification for refactoring (Shvets, 2014).

**Technical Debt** — Ward Cunningham's metaphor: like a bank loan, shortcuts let you move faster now but you pay interest — the extra effort required to work around the messy code. The debt compounds because new code is written on top of the messy code, increasing the amount that must be reworked when you eventually refactor. Causes: business pressure (roll out before ready), lack of understanding of debt consequences, tight component coupling (monolith), lack of tests (enables risky workarounds), lack of documentation, lack of team interaction, long-lived branches, delayed refactoring, lack of coding standards, developer incompetence (Shvets, 2014).

**When to Refactor** — (1) Rule of Three: first time just do it, second time cringe but repeat, third time refactor. (2) When adding a feature: refactor first to understand the existing code and to make the new feature easier to add (prepared refactoring). (3) When fixing a bug: bugs live in the dirtiest code; clean it and the bugs surface. (4) During code review: the last chance to tidy up before code goes public (Fowler, 1999; Shvets, 2014).

**How to Refactor** — Refactoring is a series of small changes, each of which makes the code slightly better while keeping the program in working order. Checklist: (1) Code should become cleaner — if it doesn't, you wasted time; this usually happens when you mix multiple refactorings into one big change. (2) No new functionality during refactoring — separate refactoring from feature development, at minimum within individual commits. (3) All existing tests must pass after refactoring — if tests break, either you made an error or the tests were too low-level (testing private methods) (Fowler, 1999; Shvets, 2014).

## Content

### Technical Debt Causes and Countermeasures

| Cause | Signal | Countermeasure |
|---|---|---|
| Business pressure | Patches and kludges hiding unfinished parts | Negotiate time for refactoring in the sprint |
| Lack of understanding of consequences | Management won't dedicate time to refactoring | Quantify debt interest (time lost to workarounds) |
| Tight component coupling | Changes in one part affect many others | Extract modules, define interfaces, decouple |
| Lack of tests | Risky workarounds deployed without verification | Write tests first (TDD), require green tests before merge |
| Lack of documentation | New people take too long to onboard | Write minimal docs, keep them close to code |
| Lack of team interaction | People work with outdated understanding | Pair programming, code reviews, knowledge sharing |
| Long-lived branches | Merge debt accumulates | Short-lived branches, frequent integration |
| Delayed refactoring | Obsolete code has more dependent code built on it | Refactor continuously during TDD REFACTOR phase |
| Lack of coding standards | Everyone writes code as they see fit | Adopt and enforce coding standards (lint, OC, SOLID) |
| Developer incompetence | Developer doesn't know how to write decent code | Training, mentoring, pair programming |

### When to Refactor — Trigger Table

| Trigger | What to Do | Knowledge Reference |
|---|---|---|
| Third occurrence of duplication | Extract Method, Pull Up Method | [[software-craft/smell-catalogue#concepts]] (Duplicate Code) |
| Adding a feature to messy code | Refactor first, then add feature (prepared refactoring) | [[software-craft/tdd#concepts]] (REFACTOR phase) |
| Bug found in dirty code | Clean the code, the bug will surface | [[software-craft/smell-catalogue#key-takeaways]] |
| Code review | Refactor as part of review, pair with author | [[software-craft/code-review#concepts]] |
| Code smell identified | Apply the corresponding refactoring technique | [[software-craft/smell-catalogue#concepts]], [[software-craft/refactoring-techniques#key-takeaways]] |

### Refactoring Process Checklist

1. Ensure tests exist and are green before starting.
2. Identify the smell per [[software-craft/smell-catalogue#key-takeaways]].
3. Choose the refactoring technique per [[software-craft/refactoring-techniques#key-takeaways]].
4. Apply one small step of the refactoring.
5. Run tests — they must pass.
6. Repeat until the refactoring is complete.
7. Commit the refactoring separately from any feature change per [[software-craft/git-conventions#concepts]].
8. If code doesn't become cleaner, consider rewriting — but only with tests and dedicated time.

## Related

- [[software-craft/smell-catalogue]] — smells trigger refactoring
- [[software-craft/refactoring-techniques]] — the techniques to apply when refactoring
- [[software-craft/design-patterns]] — patterns are applied when refactoring techniques are insufficient
- [[software-craft/tdd]] — refactoring is the REFACTOR phase of TDD
- [[software-craft/object-calisthenics]] — OC rules guide refactoring toward clean code
- [[software-craft/solid]] — SOLID violations are resolved by refactoring
- [[software-craft/git-conventions]] — refactoring commits are separate from feature commits
- [[software-craft/code-review]] — code review is a trigger for refactoring