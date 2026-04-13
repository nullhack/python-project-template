# Python Project Template - Development TODO

This file tracks current feature development. For full feature list, see docs/roadmap.md and docs/features/business/backlog/ and docs/features/architecture/backlog/.
Each session should read TODO.md and docs/roadmap.md to understand current state.

**Convention:** `[ ]` = pending, `[x]` = done, `[~]` = in progress, `[-]` = skipped

> **For AI agents:** Use `/skill session-workflow` and `/skill epic-workflow` for proper workflow management.

---

## Current Feature: Project Setup

### Phase 0: Initial Setup
- [x] Project created via template
- [ ] Review and update `README.md` with project-specific description
- [ ] Install dependencies: `uv venv && uv pip install -e '.[dev]'`
- [ ] Verify base tests pass: `task test`
- [ ] Create first feature in docs/features/business/backlog/

### QA Checkpoint
- [ ] @overseer: Review project setup completeness
- [ ] QA Status: ⏸️ Pending

---

## Feature Development Phases (8-Phase Template)

When starting a new feature, copy these phases:

### Phase 1: Requirements Review
- [ ] Read feature from docs/features/[architecture|business]/backlog/
- [ ] Validate acceptance criteria completeness and UUIDs
- [ ] Confirm feature alignment with requirements
- [ ] QA: @overseer reviews requirements completeness

### Phase 2: Feature Definition
- [ ] Read and understand feature acceptance criteria
- [ ] Identify technical scope and integration points
- [ ] Confirm feature is ready for test signature creation

### Phase 3: Architecture Analysis
- [ ] @architect /skill architectural-analysis (if architecture feature)
- [ ] Analyze component responsibilities and interfaces
- [ ] Document architectural decisions (ADRs) if significant
- [ ] QA: @overseer reviews architectural soundness

### Phase 4: Test Development (TDD)
- [ ] @manager creates test signatures from feature UUIDs
- [ ] @developer implements test bodies from signatures
- [ ] /skill prototype-script (if validation needed - optional)
- [ ] Use @pytest.mark based on test content, hypothesis for pure functions
- [ ] Write acceptance criteria tests with Given/When/Then
- [ ] QA: @overseer reviews test quality

### Phase 5: Design & Signatures
- [ ] @developer /skill signature-design
- [ ] @architect: Review and approve design
- [ ] Address architectural feedback

### Phase 6: Implementation
- [ ] @developer /skill implementation
- [ ] Implement using TDD (Red-Green-Refactor)
- [ ] Replace NotImplementedError with actual test logic
- [ ] QA: @overseer reviews SOLID/DRY/KISS compliance

### Phase 7: Final Quality Assurance
- [ ] @developer /skill code-quality
- [ ] Run all quality checks (lint, type-check, test)
- [ ] QA: @overseer final approval

### Phase 8: Feature Completion
- [ ] Move feature to docs/features/[architecture|business]/completed/ when done
- [ ] @developer /skill epic-workflow next-feature
- [ ] Proceed to next feature

---

## Session Log

| Date       | Session Summary                                    |
|------------|----------------------------------------------------|
| (date)     | Project scaffolded via template, TODO created  |

---

## Notes for Next Session

- Start with **Phase 1**: update `README.md` with project-specific content
- Then proceed to **Phase 2**: define the core features
- Run `task test` to verify the base template tests pass before making changes
- See `AGENTS.md` for project details and available commands
