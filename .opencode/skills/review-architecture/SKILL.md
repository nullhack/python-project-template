---
name: review-architecture
description: "Independently verify architecture alignment with domain model and requirements, and cross-document consistency"
---

# Review Architecture

Available knowledge: [[architecture/reconciliation#key-takeaways]], [[architecture/adr#key-takeaways]]. `in` artifacts: read all before starting work. 

1. Declare adversarial stance per [[architecture/reconciliation#concepts]].
2. Run cross-document consistency checks per [[architecture/reconciliation#concepts]].
3. Verify ADR consistency per [[architecture/adr#concepts]].
4. Verify architectural style satisfies quality attribute priorities per
   [[architecture/quality-attributes#concepts]].
5. If any inconsistency is found, resolve per [[architecture/reconciliation#concepts]].
6. When flagging issues, include file:line references (e.g., "product_definition.md:34 contradicts domain_model.md:12"). Vague findings create rework.
