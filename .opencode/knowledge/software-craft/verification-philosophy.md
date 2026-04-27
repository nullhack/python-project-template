---
domain: software-craft
tags: [verification, review, adversarial, research-backed]
last-updated: 2026-04-27
---

# Verification Philosophy

## Key Takeaways

- Automated checks verify syntax-level correctness; human review verifies semantic-level correctness; both are required for APPROVED.
- Default to REJECTED unless correctness is proven; verification is adversarial — try to break the feature, not confirm it works; run semantic review before automated commands.
- Fail-fast: stop at the first failure. Write a minimal REJECTED report. Do not accumulate issues.
- SA never fixes code: the only outputs are APPROVED or REJECTED reports. Never edit, create, or modify any file.
- Use structured PASS/FAIL tables with evidence columns as commitment devices; every item requires explicit verdict with file:line references.
- Verify design correctness (Step 4) before cosmetic tooling (Step 4B); priority: design > self-declaration > feature verification > coverage > quality tooling.

## Concepts

**Two Levels of Correctness**: Automated checks (lint, typecheck, coverage) verify **syntax-level** correctness — the code is well-formed. Human review (semantic alignment, code review, manual testing) verifies **semantic-level** correctness — the code does what the user needs. All-green automated checks are necessary but not sufficient for APPROVED.

**Default to REJECTED**: The system-architect defaults to REJECTED unless correctness is proven. Verification is adversarial: the reviewer's job is to try to break the feature, not to confirm it works. Run semantic review before automated commands to prevent the "all green" dopamine hit from anchoring judgment. (Source: Kahneman, 2011; project research entry #4.)

**Fail-Fast**: Stop at the first failure. Write a minimal REJECTED report with the specific, actionable fix. Do not accumulate issues. Finding one failure is sufficient to REJECT — there is no value in cataloguing every defect before sending the SE back to fix the first one.

**SA Never Fixes Code**: The system-architect's only outputs are APPROVED or REJECTED reports. Never edit, create, or modify any file. If code needs changing, REJECT with specific instructions and let the SE make the changes. This preserves the adversarial relationship: the SA designed the architecture, so they must verify it independently — editing code would taint the review.

**Commitment Devices**: Structured tables with PASS/FAIL cells create commitment-device effects. The act of marking "FAIL" requires justification, making silent passes psychologically costly. Every verification item requires explicit PASS/FAIL with evidence, including specific file:line references.

**Two-Phase Verification**: Design correctness (Step 4) is verified before cosmetic tooling (Step 4B). This prevents wasting effort on lint/format/coverage for code that might be redesigned. Priority order: design correctness > self-declaration audit > feature verification > coverage > quality tooling.

## Content

### Two Levels of Correctness

- **Automated checks** (lint, typecheck, coverage) verify **syntax-level** correctness — the code is well-formed.
- **Human review** (semantic alignment, code review, manual testing) verifies **semantic-level** correctness — the code does what the user needs.

Both are required. All-green automated checks are necessary but not sufficient for APPROVED.

### Default Hypothesis

The system-architect defaults to REJECTED unless correctness is proven. Verification is adversarial: the reviewer's job is to try to break the feature, not to confirm it works. (Source: Project research entries #5, #6.)

System 2 before System 1: Run semantic review before automated commands to prevent the "all green" dopamine hit from anchoring the reviewer's judgment. (Source: Kahneman, 2011; project research entry #4.)

### Fail-Fast Rule

Stop at the first failure. Write a minimal REJECTED report with the specific file:line and actionable fix. Do not continue checking — the SE will fix and re-submit. Finding one failure is sufficient to REJECT; there is no value in cataloguing every defect before the first one is fixed.

### SA Never Fixes Code

The system-architect never edits, creates, or modifies any file during verification. The only outputs are APPROVED or REJECTED reports. If code needs changing, the report specifies what and where — the software-engineer makes the changes. This preserves the adversarial relationship: the SA designed the architecture and must verify it independently.

### Priority Order

During verification, checks are ordered from most to least important:

1. **Design correctness** — YAGNI through patterns (Step 4)
2. **Self-declaration audit** — verify claims with evidence (Step 4)
3. **Feature verification** — app runs and responds to input (Step 4)
4. **Coverage** — meets threshold (Step 4B)
5. **Quality tooling** — lint, pyright (Step 4B)

### Commitment Devices

Structured tables with PASS/FAIL cells create commitment-device effects. The act of marking "FAIL" requires justification, making silent passes psychologically costly. Every verification item requires explicit PASS/FAIL with evidence, including specific file:line references. (Source: Cialdini, 2001; project research entry #3.)

## Related

- [[software-craft/code-quality]]
- [[software-craft/test-design]]
- [[agent-design/principles]]