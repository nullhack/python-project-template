# {{cookiecutter.project_name}} - Development TODO

This file tracks current feature development within epics. For epic/feature tracking, see EPICS.md.
Each session should read both TODO.md and EPICS.md to understand current state.

**Convention:** `[ ]` = pending, `[x]` = done, `[~]` = in progress, `[-]` = skipped

> **For AI agents:** Use `/skill session-workflow` and `/skill epic-workflow` for proper workflow management.

---

## Current Epic: Project Foundation
## Current Feature: Project Setup

### Phase 0: Initial Setup
- [x] Project created via cookiecutter template
- [ ] Review and update `README.md` with project-specific description
- [ ] Install dependencies: `uv venv && uv pip install -e '.[dev]'`
- [ ] Verify base tests pass: `task test`
- [ ] Initialize EPICS.md with first business epic

### QA Checkpoint
- [ ] @overseer: Review project setup completeness
- [ ] QA Status: ⏸️ Pending

---

## Feature Development Phases (Template)

When starting a new feature, copy these phases:

### Phase 1: Requirements Gathering
- [ ] @requirements-gatherer: Conduct stakeholder interview
- [ ] Create feature analysis document
- [ ] Define acceptance criteria
- [ ] QA: @overseer reviews requirements

### Phase 2: Feature Definition  
- [ ] @developer /skill feature-definition
- [ ] Document technical requirements
- [ ] Update EPICS.md with feature details

### Phase 3: Test Development
- [ ] @developer /skill prototype-script (if needed)
- [ ] @developer /skill tdd
- [ ] Write BDD-style tests with Given/When/Then
- [ ] QA: @overseer reviews test quality

### Phase 4: Design & Architecture
- [ ] @developer /skill signature-design
- [ ] @architect: Review and approve design
- [ ] Address architectural feedback

### Phase 5: Implementation
- [ ] @developer /skill implementation
- [ ] Implement using TDD (Red-Green-Refactor)
- [ ] QA: @overseer reviews SOLID/DRY/KISS compliance

### Phase 6: Final Quality Assurance
- [ ] @developer /skill code-quality
- [ ] Run all quality checks (lint, type-check, test)
- [ ] QA: @overseer final approval

### Phase 7: Feature Completion
- [ ] Update EPICS.md - mark feature complete
- [ ] @developer /skill epic-workflow next-feature
- [ ] Proceed to next feature or close epic

---

## Session Log

| Date       | Session Summary                                    |
|------------|----------------------------------------------------|
| (date)     | Project scaffolded via cookiecutter, TODO created  |

---

## Notes for Next Session

- Start with **Phase 1**: update `README.md` with project-specific content
- Then proceed to **Phase 2**: define the core features
- Run `task test` to verify the base template tests pass before making changes
- See `AGENTS.md` for project details and available commands
