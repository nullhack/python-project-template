---
name: workflow-coordination
description: Enforce 7-step development cycle with proper phase progression and QA gates
license: MIT
compatibility: opencode
metadata:
  audience: project-manager
  workflow: development-cycle
---

## What I do
Manage the complete 7-step development cycle with proper phase progression, mandatory QA gates, and feature/TODO alignment with requirements.

## When to use me
- When coordinating feature development
- During phase transitions in the development cycle
- When managing feature progression
- When validating workflow compliance

## 8-Phase Development Cycle

### Phase 1: Requirements Review
**Duration**: Variable
**Primary Agent**: @requirements-gatherer
**QA Checkpoint**: @overseer

```
Phase 1: Requirements Review
├── [ ] Review feature from docs/features/[architecture|business]/backlog/
├── [ ] Validate acceptance criteria completeness and UUIDs
├── [ ] Verify business value alignment
├── [ ] Confirm feature alignment with requirements
└── QA: @overseer reviews requirements
```

**QA Gate Checklist**:
- [ ] Feature has UUID-based acceptance criteria
- [ ] Each acceptance criteria has Given/When/Then format
- [ ] Dependencies identified
- [ ] Edge cases documented

### Phase 2: Feature Definition
**Duration**: Variable
**Primary Agent**: @manager (selection) + @developer
**QA Checkpoint**: @overseer

```
Phase 2: Feature Definition
├── [ ] Read feature acceptance criteria
├── [ ] Understand technical scope
├── [ ] Confirm feature is ready for test signature creation
├── [ ] Identify integration points
└── QA: @overseer reviews definition
```

**QA Gate Checklist**:
- [ ] Acceptance criteria fully understood
- [ ] Technical scope clearly defined
- [ ] Integration points identified

### Phase 3: Architecture Analysis
**Duration**: Variable
**Primary Agent**: @architect (using architectural-analysis skill)
**QA Checkpoint**: @overseer

```
Phase 3: Architecture Analysis
├── [ ] @architect /skill architectural-analysis (if architecture feature)
├── [ ] Analyze component responsibilities
├── [ ] Define interfaces and contracts
├── [ ] Document architectural decisions (ADRs) if significant
├── [ ] Create/update docs/features/architecture/backlog/<feature>/
└── QA: @overseer reviews architectural soundness
```

**QA Gate Checklist**:
- [ ] Component responsibilities are single-purpose
- [ ] Architecture decisions documented with rationale
- [ ] Integration points explicitly defined
- [ ] Technical acceptance criteria have UUIDs

### Phase 4: Test Development (TDD)
**Duration**: Variable
**Primary Agent**: @developer (using tdd skill)
**QA Checkpoint**: @overseer

```
Phase 4: Test Development (TDD)
├── [ ] /skill prototype-script (if validation needed - optional)
├── [ ] Implement test bodies from manager-created signatures
├── [ ] Write BDD tests with UUID format:
│   """[UUID]: [Test description].
│   
│   Given: [Preconditions]
│   When: [Action/trigger]
│   Then: [Expected outcome]
│   """
├── [ ] Use @pytest.mark based on test content (not feature type)
├── [ ] Use @given() for pure functions when appropriate
├── [ ] Use @example() for specific test cases
├── [ ] Use assume() to filter invalid inputs in hypothesis tests
├── [ ] Ensure test naming: test_<condition>_should_<outcome>
├── [ ] Ensure file naming: *_test.py
└── QA: @overseer reviews test quality
```

**QA Gate Checklist**:
- [ ] All acceptance criteria have test coverage
- [ ] BDD docstrings use proper format with newlines
- [ ] Test naming follows convention
- [ ] File naming follows convention
- [ ] Hypothesis used appropriately for pure functions
- [ ] @example() used for specific boundary cases
- [ ] assume() used to filter invalid hypothesis inputs
- [ ] Edge cases covered
- [ ] Test isolation maintained

### Phase 5: Design & Signatures
**Duration**: Variable
**Primary Agent**: @developer (using signature-design) + @architect
**QA Checkpoint**: @overseer

```
Phase 5: Design & Signatures
├── [ ] /skill signature-design
├── [ ] Design interfaces with type hints
├── [ ] Define protocols for abstractions
├── [ ] @architect reviews design
├── [ ] Address architectural feedback
├── [ ] Validate SOLID compliance
└── QA: @overseer validates architecture
```

**QA Gate Checklist**:
- [ ] SOLID principles followed
- [ ] Type hints on public APIs
- [ ] Protocols defined where appropriate
- [ ] Dependencies injected
- [ ] No over-engineering
- [ ] Design supports testability

### Phase 6: Implementation
**Duration**: Variable
**Primary Agent**: @developer (using implementation skill)
**QA Checkpoint**: @overseer

```
Phase 6: Implementation
├── [ ] /skill implementation
├── [ ] Implement using TDD (Red-Green-Refactor)
├── [ ] Write production code to pass tests
├── [ ] Replace NotImplementedError with actual test logic
├── [ ] Refactor for quality
├── [ ] Ensure 100% test coverage
├── [ ] Run quality checks: task lint, task static-check
└── QA: @overseer reviews implementation
```

**QA Gate Checklist**:
- [ ] All tests pass
- [ ] 100% test coverage
- [ ] Linting passes (no noqa)
- [ ] Type checking passes (no type: ignore without justification)
- [ ] DRY principle followed
- [ ] KISS principle applied
- [ ] No TODOs or FIXMEs left

### Phase 7: Final Quality Assurance
**Duration**: Variable
**Primary Agent**: @developer (using code-quality skill)
**QA Checkpoint**: @overseer

```
Phase 7: Final Quality Assurance
├── [ ] /skill code-quality
├── [ ] Run: task lint
├── [ ] Run: task static-check
├── [ ] Run: task test
├── [ ] Verify 100% coverage maintained
├── [ ] Run security checks
├── [ ] Validate performance
└── QA: @overseer final approval
```

**QA Gate Checklist**:
- [ ] All quality checks pass
- [ ] 100% test coverage
- [ ] No security vulnerabilities
- [ ] Performance acceptable
- [ ] Documentation complete
- [ ] Ready for PR

### Phase 8: Feature Completion
**Duration**: Fixed
**Primary Agent**: @developer + @manager
**QA Checkpoint**: None (completion)

```
Phase 8: Feature Completion
├── [ ] Move feature to docs/features/[architecture|business]/completed/
├── [ ] /skill epic-workflow next-feature
├── [ ] Move to next feature OR close session
├── [ ] Update TODO.md
├── [ ] Session handoff if needed
└── Feature Complete
```

## QA Checkpoint Integration

### Mandatory Checkpoint Structure
Every phase includes mandatory @overseer review:

```
### Phase X: [Phase Name]
- [ ] Primary tasks completed
- [ ] Additional tasks...
└── QA: @overseer reviews [focus area]
```

### Checkpoint Request Template
```markdown
## QA Checkpoint Request: Phase [X] - [Feature Name]

**Phase**: [X] - [Phase Name]
**Feature**: [Feature from docs/roadmap.md]
**QA Focus**: [What overseer should review]

**Completed Tasks**:
- [ ] Task 1
- [ ] Task 2

**Validation Requested**:
- [ ] Quality standards compliance
- [ ] [Specific validation needed]

**Next Phase**: Will proceed to Phase [X+1] upon approval
```

## Epic/TODO Alignment

### TODO Structure
Each feature in TODO.md follows this structure:

```markdown
## Current Feature: [Feature from docs/roadmap.md]
## Current Feature: [Feature Name]

### Phase 1: Requirements Review
- [ ] @requirements-gatherer reviews REQUIREMENTS.md
- [ ] Validates business value alignment
- [ ] QA: @overseer reviews requirements completeness

### Phase 2: Feature Definition
- [ ] @developer /skill feature-definition
- [ ] Updates docs/roadmap.md technical details
- [ ] QA: @overseer reviews definition quality

[... all 7 phases ...]

### QA History
| Phase | Agent | Status | QA Status |
|-------|-------|--------|----------|
| 1 | @requirements | Complete | @overseer Approved |
| 2 | @developer | Complete | @overseer Approved |
| 3 | @developer | In Progress | @overseer Pending |
```

### Roadmap Integration
- Feature progress updates docs/roadmap.md status
- Feature completion moves to docs/features/[architecture|business]/completed/
- QA history tracked in TODO.md session log
- Requirements traceability maintained

## Session Workflow Integration

### Start of Session
```markdown
# 1. Read TODO.md - Understand current state
# 2. Read docs/roadmap.md - Review feature breakdown
# 3. Identify current phase
# 4. Continue from checkpoint
```

### End of Session
```markdown
# 1. Update TODO.md with progress
# 2. Mark completed tasks
# 3. Document blockers/issues
# 4. Note QA status for next session
# 5. Prepare handoff notes
```

## Phase Progression Rules

### Can Proceed to Next Phase When
- [ ] All phase tasks marked complete
- [ ] @overseer approval received
- [ ] No blocking issues
- [ ] Next phase resources available

### Cannot Proceed When
- [ ] Tasks incomplete
- [ ] @overseer approval missing
- [ ] Blocking issues exist
- [ ] Dependencies unresolved
- [ ] Quality standards not met

## Quality Enforcement at Phase Transitions

### Transition Rules
1. **Complete current phase tasks**
2. **Request @overseer QA review**
3. **Wait for approval**
4. **If approved**: Proceed to next phase
5. **If rejected**: Fix issues, request re-review
6. **Repeat until approved**

### QA Gate Failure Response
```markdown
## QA Checkpoint Failed: Phase [X]

**Issues Detected**:
1. [Issue 1]: [Description]
2. [Issue 2]: [Description]

**Required Fixes**:
- [ ] Fix 1
- [ ] Fix 2

**Next Steps**:
1. Fix identified issues
2. Request @overseer re-review
3. Proceed upon approval
```

## Workflow Validation Checklist

### Pre-Development Validation
- [ ] REQUIREMENTS.md exists in docs/requirements/
- [ ] docs/roadmap.md updated with technical design
- [ ] TODO.md created with 8-phase structure
- [ ] QA checkpoints embedded

### During Development Validation
- [ ] Phase tasks progressing per plan
- [ ] QA checkpoints triggered at boundaries
- [ ] Epic alignment maintained
- [ ] Requirements traceability clear

### Post-Development Validation
- [ ] All phases complete
- [ ] All QA approvals received
- [ ] docs/roadmap.md updated
- [ ] TODO.md updated for session handoff

Remember: The 8-phase development cycle ensures quality at every step. Never bypass QA checkpoints - they exist to maintain standards and catch issues early.