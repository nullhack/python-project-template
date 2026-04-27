---
domain: software-craft
tags: [verification, review, adversarial, research-backed]
last-updated: 2026-04-26
---

# Verification Philosophy

## Key Takeaways

- Automated checks verify syntax-level correctness; human review verifies semantic-level correctness; both are required for APPROVED.
- Default to REJECTED unless correctness is proven; verification is adversarial — try to break the feature, not confirm it works.
- Run semantic review before automated commands to prevent the "all green" dopamine hit from anchoring judgment.
- Use structured PASS/FAIL tables with evidence columns as commitment devices; every item requires explicit verdict with file:line references.

## Concepts

**Two Levels of Correctness**: Automated checks (lint, typecheck, coverage) verify that code is well-formed — syntax-level correctness. Human review (semantic alignment, code review, manual testing) verifies that code does what the user needs — semantic-level correctness. All-green automated checks are necessary but not sufficient for APPROVED.

**Default to REJECTED**: The system-architect defaults to REJECTED unless correctness is proven. Verification is adversarial: the reviewer's job is to try to break the feature, not to confirm it works. System 2 before System 1 — run semantic review before automated commands to prevent the "all green" dopamine hit from anchoring judgment.

**Commitment Devices**: Structured tables with PASS/FAIL cells create commitment-device effects. The act of marking "FAIL" requires justification, making silent passes psychologically costly. Every verification item requires explicit PASS/FAIL with evidence, including specific file:line references.

**Run Semantic Review First**: Execute semantic review before automated commands. The "all green" dopamine hit from passing checks anchors judgment toward APPROVED. Reviewing with a REJECTED default prevents confirmation bias.

## Content

### Two Levels of Correctness

- **Automated checks** (lint, typecheck, coverage) verify **syntax-level** correctness — the code is well-formed.
- **Human review** (semantic alignment, code review, manual testing) verifies **semantic-level** correctness — the code does what the user needs.

Both are required. All-green automated checks are necessary but not sufficient for APPROVED.

### Default Hypothesis

The system-architect defaults to REJECTED unless correctness is proven. Verification is adversarial: the reviewer's job is to try to break the feature, not to confirm it works. (Source: Project research entries #5, #6.)

System 2 before System 1: Run semantic review before automated commands to prevent the "all green" dopamine hit from anchoring the reviewer's judgment. (Source: Kahneman, 2011; project research entry #4.)

### Commitment Devices

Structured tables with PASS/FAIL cells create commitment-device effects. The act of marking "FAIL" requires justification, making silent passes psychologically costly. Every verification item requires explicit PASS/FAIL with evidence, including specific file:line references. (Source: Cialdini, 2001; project research entry #3.)

## Related

- [[software-craft/code-quality]]
- [[software-craft/test-design]]
- [[agent-design/principles]]