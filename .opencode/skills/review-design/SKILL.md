---
name: review-design
description: "Verify implementation aligns with domain model, architectural decisions, and quality attributes"
---

# Review Design

Load [[architecture/reconciliation]], [[architecture/adr]], [[software-craft/code-review]], [[software-craft/refactoring]], [[software-craft/object-calisthenics]], [[software-craft/smell-catalogue]], [[software-craft/design-patterns]], [[software-craft/solid]], and [[software-craft/tdd]] before starting. 

1. Declare adversarial stance per [[software-craft/code-review#concepts]] — default hypothesis: "it might be broken despite green tests."
2. Verify implementation aligns with domain model and bounded contexts per [[architecture/reconciliation#concepts]].
3. Verify architectural decisions from ADRs are respected per [[architecture/adr#key-takeaways]].
4. Verify Object Calisthenics per [[software-craft/object-calisthenics#key-takeaways]] — check each OC rule for violations.
5. Check for code smells per [[software-craft/smell-catalogue#key-takeaways]] — Bloaters, OO Abusers, Change Preventers, Dispensables, Couplers. Check detection heuristics per [[software-craft/smell-catalogue#concepts]].
6. Before flagging code as dead or unnecessary, verify against domain model, technical design, and interview notes. Code that matches the architecture but hasn't been exercised by a test yet is **planned code** — flag as WARN (planned-not-reached), not REJECT. Only code that contradicts the architecture or was superseded is **dead code** — REJECT.
7. IF a smell is found → list it in findings per [[software-craft/code-review#key-takeaways]]. "Minor" is not a pass — acknowledged smells are still findings for the SE to evaluate.
8. IF multiple `if/elif` on type/state → check for missing State or Strategy pattern per [[software-craft/design-patterns#concepts]].
9. IF technical debt is identified → verify it is tracked or being paid down per [[software-craft/refactoring#concepts]].
10. IF a quality attribute from the product definition has no corresponding design decision → flag it as a gap.
11. Stop at the first failure per [[software-craft/code-review#key-takeaways]] — write a minimal REJECTED report with file:line evidence.
12. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
13. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.