---
name: design-technical-solution
description: "Select technology stack, document dependencies, and route architecturally significant decisions to ADRs"
---

# Design Technical Solution

Available knowledge: [[architecture/quality-attributes#key-takeaways]], [[architecture/technical-design#key-takeaways]]. `in` artifacts: read all before starting work.

1. Rank quality attributes by business priority per [[architecture/quality-attributes#concepts]].
2. Select architectural style per the quality-attribute-to-style mapping in
   [[architecture/quality-attributes#concepts]].
3. Define the technology stack and write to product_definition.md.
4. Document dependency rationale and write to product_definition.md.
5. If a decision is architecturally significant per [[architecture/adr#key-takeaways]],
   the draft-adr skill (next in this state's dispatch) will document it as an ADR.
