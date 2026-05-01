---
name: review-architecture
description: "Independently verify architecture alignment with domain model and requirements, and cross-document consistency"
---

# Review Architecture

Load [[architecture/reconciliation#key-takeaways]] and [[architecture/adr#key-takeaways]] before starting. 

1. Declare adversarial stance per [[architecture/reconciliation#concepts]].
2. Run cross-document consistency checks per [[architecture/reconciliation#concepts]].
3. Verify ADR consistency per [[architecture/adr#concepts]].
4. Verify architectural style satisfies quality attribute priorities per
   [[architecture/quality-attributes#concepts]].
5. If any inconsistency is found, resolve per [[architecture/reconciliation#concepts]].
6. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
7. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
