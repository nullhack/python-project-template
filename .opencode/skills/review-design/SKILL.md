---
name: review-design
description: "Verify implementation aligns with domain model, architectural decisions, and quality attributes"
---

# Review Design

Available knowledge: [[architecture/reconciliation]], [[architecture/adr]], [[software-craft/code-review]], [[software-craft/refactoring]], [[software-craft/object-calisthenics]], [[software-craft/smell-catalogue]], [[software-craft/design-patterns]], [[software-craft/solid]], [[software-craft/tdd]]. `in` artifacts: discover and read on demand as needed. 

1. This review tier checks design correctness ONLY. Do not flag lint, coverage, docstring, or naming issues — those belong to structure or conventions review.
2. Declare adversarial stance per [[software-craft/code-review#concepts]] — default hypothesis: "it might be broken despite green tests."
3. Verify implementation aligns with domain model and bounded contexts per [[architecture/reconciliation#concepts]].
4. Verify architectural decisions from ADRs are respected per [[architecture/adr#key-takeaways]].
5. Verify Object Calisthenics per [[software-craft/object-calisthenics#key-takeaways]] — check each rule for violations.
6. Check for code smells per [[software-craft/smell-catalogue#key-takeaways]] — Bloaters, OO Abusers, Change Preventers, Dispensables, Couplers. Check detection heuristics per [[software-craft/smell-catalogue#concepts]].
7. Before flagging code as dead or unnecessary, verify against domain model, technical design, and interview notes. Code that matches the architecture but hasn't been exercised by a test yet is **planned code** — flag as WARN (planned-not-reached), not REJECT. Only code that contradicts the architecture or was superseded is **dead code** — REJECT.
8. IF a smell is found → list it in findings per [[software-craft/code-review#key-takeaways]]. "Minor" is not a pass — acknowledged smells are still findings.
9. IF multiple `if/elif` on type/state → check for missing State or Strategy pattern per [[software-craft/design-patterns#concepts]].
10. IF technical debt is identified → verify it is tracked or being paid down per [[software-craft/refactoring#concepts]].
11. IF a quality attribute from the product definition has no corresponding design decision → flag it as a gap.
12. Stop at the first failure per [[software-craft/code-review#key-takeaways]] — write a minimal REJECTED report with file:line evidence.
13. When flagging issues, include file:line references — e.g., "domain_model.md:23 conflicts with login.feature:15". Vague findings create rework.
14. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
15. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.