---
domain: software-craft
tags: [code-review, adversarial-review, self-declaration, two-tier-review, inspection]
last-updated: 2026-05-14
---

# Code Review

## Key Takeaways

- The reviewer's default hypothesis is "it might be broken despite green tests (prove otherwise") adversarial review catches more defects than cooperative review (Fagan, 1976; Tetlock, 1985).
- Fail-fast: stop at the first failure, write a minimal REJECTED report. Do not continue reviewing after finding a defect: the defect may invalidate subsequent findings.
- The reviewer MUST NOT modify any files. Produce APPROVED or REJECTED report only.
- "Minor" is not a pass: code smells that are acknowledged must still be listed as findings.
- Lint and type errors are convention concerns, verified in the polish state after feature acceptance.
- Self-declaration checklists (AGREE/DISAGREE on specific criteria) force the reviewer to articulate exactly what passes and what fails, preventing vague "looks good" approval (Hattie & Timperley, 2007; Fagan, 1976).
- Two-tier review separates concerns: design (does it do the right thing?), structure (are tests good enough, does it pass functional lint?). Conventions (naming, docstrings, formatting) are enforced in a separate polish state after feature acceptance.

## Concepts

**Adversarial Review** (Fagan, 1976; Tetlock, 1985). Structured inspections detect 60–90% of defects before testing. The key mechanism is forcing the reviewer to articulate specific failures rather than offering vague approval. Accountability to an unknown audience (Tetlock, 1985) shifts the reviewer from confirmation bias ("looking for reasons it works") to adversarial search ("looking for reasons it breaks"). The reviewer MUST NOT modify any files (produce APPROVED or REJECTED report only. "Minor" is not a pass) acknowledged smells are still findings. Lint and type errors are convention concerns, not design concerns.

**Fail-Fast Protocol**. Stop reviewing at the first defect found. Write a minimal REJECTED report containing: the defect, its file:line evidence, and the required action. Do not accumulate multiple findings. The first defect may invalidate everything that follows. Fix the defect, re-submit, and the reviewer starts over.

**Two-Tier Review**. Each tier checks a different quality dimension with different knowledge. Design review verifies alignment with domain spec, ADRs, and quality attributes. Structure review verifies test coverage, test quality, abstraction level matching, and functional lint (bug-catching rules only). Conventions (naming, docstrings, formatting, type annotations) are enforced in a separate polish state after feature acceptance, not during review.

**Self-Declaration as Commitment Device** (Hattie & Timperley, 2007; Cialdini, 2001). Before handoff, the developer declares specific quality attributes as AGREE/DISAGREE. This forces explicit judgment on each criterion, preventing the "I skimmed it and nothing jumped out" pattern. DISAGREE is not automatic rejection. The developer states the reason, and the reviewer evaluates whether the reason is acceptable.


## Content

### Two-Tier Review Structure

| Tier | Checks | Key Knowledge |
|---|---|---|
| Design | Domain alignment, ADR consistency, quality attributes, design principle priority | [[architecture/reconciliation]], [[architecture/adr]] |
| Structure | Test coverage, test quality, abstraction level, observable behaviour, functional lint | [[software-craft/test-design]], [[software-craft/tdd]] |

Conventions (naming, docstrings, formatting, type annotations, full lint) are enforced in a separate polish state after feature acceptance via `task conventions`, `ruff format`, and `task static-check`.

### Review Stance Declaration

Before performing any review tier, declare:

- Adversarial stance: "I will actively search for defects, not confirm correctness."
- Fail-fast: "I will stop at the first failure and write a minimal REJECTED report."

### PASS/FAIL Report Format

For each criterion checked, the reviewer records:

- **Criterion**: Which specific quality attribute was checked
- **Verdict**: PASS or FAIL
- **Evidence**: File:line reference and specific observation
- **Action**: What must change (only on FAIL)

A REJECTED report contains: the first failure found, its evidence, and the required action. No additional findings are needed. Fix the defect and re-submit.

### Planned Code vs Dead Code

During design review, distinguish between planned code and dead code:

- **Planned code** matches the domain spec, technical design, or interview notes but has not been exercised by a test yet. Flag as WARN (planned-not-reached), not REJECT. The stubs created at feature planning time are breadcrumbs from the domain spec: the SE will reach them as TDD progresses through examples.
- **Dead code** contradicts the architecture or was superseded by a design decision. Flag as REJECT and require removal.

Before flagging code as dead or unnecessary, verify against domain spec, technical design, and interview notes. Code that matches the architecture is planned, even if no test exercises it yet.

## Related

- [[architecture/reconciliation]]: adversarial cross-document consistency checking
- [[software-craft/test-design]]: what makes a good test vs a bad test
- [[software-craft/tdd]]: the design principle priority used in design review
- [[software-craft/object-calisthenics]]: the 9 Object Calisthenics rules checked in design review
- [[software-craft/smell-catalogue]]: smells checked during review
- [[software-craft/design-patterns]]: patterns verified during review
- [[software-craft/solid]]: SOLID violations checked during review
- [[software-craft/refactoring]]: when and how to refactor, clean code, technical debt
- [[requirements/ubiquitous-language]]: naming conventions checked in conventions review