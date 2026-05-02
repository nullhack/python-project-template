---
name: design-technical-solution
description: "Design the technical solution — architectural style, stack, module structure, API/event contracts, interface definitions"
---

# Design Technical Solution

Available knowledge: [[architecture/quality-attributes#key-takeaways]], [[architecture/technical-design#key-takeaways]], [[architecture/contract-design#key-takeaways]]. `in` artifacts: discover and read on demand as needed.

1. Rank quality attributes by business priority per [[architecture/quality-attributes#concepts]].
2. Select architectural style per the quality-attribute-to-style mapping in
   [[architecture/quality-attributes#concepts]].
3. Define the stack.
4. Define module structure per [[architecture/technical-design#concepts]].
5. For each integration point in the context map, define a contract per
   [[architecture/contract-design#concepts]].
6. Draw C4 diagrams per [[architecture/technical-design#concepts]].
7. Document dependencies and configuration keys.
8. Update system overview sections to reflect the current design.
9. If a decision is architecturally significant per [[architecture/adr#key-takeaways]],
   route to needs_decisions.
10. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
11. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
