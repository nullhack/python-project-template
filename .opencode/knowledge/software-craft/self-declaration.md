---
domain: software-craft
tags: [self-declaration, verification, quality-gate, handoff]
last-updated: 2026-04-27
---

# Self-Declaration

## Key Takeaways

- Complete a 25-item design declaration covering YAGNI, KISS, DRY, SOLID, Object Calisthenics, pattern smells, and semantic alignment before handing off for Step 4 (Design Verification).
- Complete a 4-item completion declaration covering coverage, lint, type checking, and docstrings before handing off for Step 4B (Completion Verification).
- A DISAGREE answer is not automatic rejection; state the reason and fix before handoff.
- The system-architect audits every claim with file:line evidence; missing or unjustified claims result in REJECT.
- The architect also declares their adversarial stance: actively trying to find failure modes, not confirming passing.

## Concepts

**Design Self-Declaration (Step 3A)**: Before handing off for design review, the software-engineer declares design correctness across 25 items covering YAGNI (items 1-2), KISS (items 3-4), DRY (items 5-6), SOLID (items 7-11), Object Calisthenics (items 12-20), pattern smells (items 21-24), and semantic alignment (item 25). Each item requires AGREE or DISAGREE with a file:line reference. This declaration covers design only — not lint, coverage, type checking, or docstrings.

**Completion Declaration (Step 3B)**: Before handing off for completion verification, the software-engineer declares four items covering cosmetic tooling: coverage threshold met, lint clean, type checking clean, and public API documented. Each item requires AGREE or DISAGREE with evidence.

**DISAGREE Is Not Automatic Rejection**: A DISAGREE answer requires a reason but is not automatic rejection. State the reason for the disagreement. If the constraint genuinely falls outside the SE's control, the disagreement is accepted. If the justification is weak or missing, it results in REJECT.

**Self-Declaration Audit (Step 4)**: The system-architect audits the SE's declaration during Step 4 verification. First, a completeness check (hard gate): verify every claim is present and numbered. Then for each AGREE claim, find the file:line and verify it holds. For each DISAGREE claim, read the justification and accept or reject.

**Architect Review Stance Declaration**: The system-architect writes their own declaration before the decision: adversarial stance, architecture preservation, manual trace, boundary check, semantic read, and independence. Every DISAGREE must include an inline explanation; a DISAGREE with no explanation auto-forces REJECTED.

## Content

### Design Self-Declaration (Step 3A handoff)

Communicate verbally to the system-architect at Step 3A handoff. Cover design correctness only — not lint, coverage, type checking, or docstrings.

As a software-engineer I declare:
* 1. YAGNI: no code without a failing test — AGREE/DISAGREE | file:line
* 2. YAGNI: no speculative abstractions — AGREE/DISAGREE | file:line
* 3. KISS: simplest solution that passes — AGREE/DISAGREE | file:line
* 4. KISS: no premature optimization — AGREE/DISAGREE | file:line
* 5. DRY: no duplication — AGREE/DISAGREE | file:line
* 6. DRY: no redundant comments — AGREE/DISAGREE | file:line
* 7. SOLID-S: one reason to change per class — AGREE/DISAGREE | file:line
* 8. SOLID-O: open for extension, closed for modification — AGREE/DISAGREE | file:line
* 9. SOLID-L: subtypes substitutable — AGREE/DISAGREE | file:line
* 10. SOLID-I: no forced unused deps — AGREE/DISAGREE | file:line
* 11. SOLID-D: depend on abstractions, not concretions — AGREE/DISAGREE | file:line
* 12. OC-1: one level of indentation per method — AGREE/DISAGREE | deepest: file:line
* 13. OC-2: no else after return — AGREE/DISAGREE | file:line
* 14. OC-3: primitive types wrapped — AGREE/DISAGREE | file:line
* 15. OC-4: first-class collections — AGREE/DISAGREE | file:line
* 16. OC-5: one dot per line — AGREE/DISAGREE | file:line
* 17. OC-6: no abbreviations — AGREE/DISAGREE | file:line
* 18. OC-7: ≤20 lines per function, ≤50 per class — AGREE/DISAGREE | longest: file:line
* 19. OC-8: ≤2 instance variables per class (behavioural classes only; dataclasses, Pydantic models, value objects, and TypedDicts are exempt) — AGREE/DISAGREE | file:line
* 20. OC-9: Tell, Don't Ask — no getters/setters, no external decision-making on another object's data — AGREE/DISAGREE | file:line
* 21. Patterns: no good reason remains to refactor using OOP or Design Patterns — AGREE/DISAGREE | file:line
* 22. Patterns: no creational smell — AGREE/DISAGREE | file:line
* 23. Patterns: no structural smell — AGREE/DISAGREE | file:line
* 24. Patterns: no behavioural smell — AGREE/DISAGREE | file:line
* 25. Semantic: tests operate at same abstraction as AC — AGREE/DISAGREE | file:line

A DISAGREE answer is not automatic rejection — state the reason and fix before handing off.

### Completion Declaration (Step 3B handoff)

Communicate verbally to the system-architect at Step 3B handoff. Cover cosmetic tooling only — design correctness was already declared at Step 3A.

1. Coverage threshold met — `uv run task test-coverage` exits 0 — AGREE/DISAGREE | evidence
2. Lint clean — `uv run task lint` exits 0, no `noqa` or `type: ignore` — AGREE/DISAGREE | evidence
3. Type checking clean — `uv run task static-check` exits 0, 0 pyright errors — AGREE/DISAGREE | evidence
4. Public API documented — all public classes and methods have docstrings — AGREE/DISAGREE | evidence

### Self-Declaration Audit (Step 4 and Step 4B)

The system-architect audits the SE's Design Self-Declaration during Step 4 (Design Verification) and the Completion Declaration during Step 4B (Completion Verification).

**Step 4 — Design Declaration Audit**:

**Completeness check (hard gate — REJECT if failed)**: Verify that every claim is present and numbered. If any claim is missing, or the declaration is empty, REJECT immediately — do not proceed to item-level audit.

For every AGREE claim:
- Find the `file:line` — does it hold?

For every DISAGREE claim:
- Read the justification carefully.
- If the constraint genuinely falls outside the SE's control (e.g. external library forces method chaining, dataclass/Pydantic/TypedDict exemption for OC-8): accept with a note in the report and suggest the closest compliant alternative if one exists.
- If the justification is weak, incomplete, or a best-practice alternative exists that the SE did not consider: REJECT with the specific alternative stated.
- If there is no justification: REJECT.

Undeclared violations found during semantic review → REJECT.

**Step 4B — Completion Declaration Audit**: Verify each completion claim independently by running the commands.

### Architect Review Stance Declaration

Written by the system-architect before the decision. Every DISAGREE must include an inline explanation. A DISAGREE with no explanation auto-forces REJECTED.

As a system-architect I declare:
* Adversarial: I actively tried to find a failure mode, not just confirm passing — AGREE/DISAGREE | note:
* Architecture preservation: I verified that stubs, Protocols, and ADR decisions from Step 2 were respected — AGREE/DISAGREE | violations:
* Manual trace: I traced at least one execution path manually beyond automated output — AGREE/DISAGREE | path:
* Boundary check: I checked the boundary conditions and edge cases of every Rule — AGREE/DISAGREE | gaps:
* Semantic read: I read each test against its AC and confirmed it tests the right observable behaviour — AGREE/DISAGREE | mismatches:
* Independence: my verdict was not influenced by how much effort has already been spent — AGREE/DISAGREE

## Related

- [[software-craft/solid]] — items 7-11
- [[software-craft/object-calisthenics]] — items 12-20
- [[software-craft/design-patterns]] — items 21-24
- [[software-craft/test-conventions]] — item 25 (semantic alignment)
- [[software-craft/verification-philosophy]] — adversarial verification principles
- [[software-craft/test-design]] — refactor-safe test design (informs item 25)