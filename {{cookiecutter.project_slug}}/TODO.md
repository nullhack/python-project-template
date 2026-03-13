# {{cookiecutter.project_name}} - Development TODO

This file tracks all development steps across AI sessions. Each session should read this file first, pick up from the last completed step, and update statuses before finishing.

**Convention:** `[ ]` = pending, `[x]` = done, `[~]` = in progress, `[-]` = skipped

> **For AI agents:** Use `/skill session-workflow` for the full session start/end protocol.

---

## Phase 1: Project Foundation

- [x] Project created via cookiecutter template
- [ ] Review and update `README.md` with project-specific description
- [ ] Install dependencies: `uv venv && uv pip install -e '.[dev]'`
- [ ] Verify base tests pass: `task test`

---

## Phase 2: Feature Definition

- [ ] Define core features using `/skill feature-definition`
- [ ] Document requirements and acceptance criteria
- [ ] Review SOLID principles compliance in design

---

## Phase 3: Prototype & Validation

- [ ] Create prototype scripts using `/skill prototype-script`
- [ ] Validate core concepts with real data
- [ ] Document prototype outputs for implementation reference

---

## Phase 4: Test-Driven Development

- [ ] Write comprehensive test suite using `/skill tdd`
- [ ] Ensure all tests fail initially (RED phase)
- [ ] Cover unit, integration, and property-based tests

---

## Phase 5: Architecture Review

- [ ] Design interfaces using `/skill signature-design`
- [ ] Request architecture review from `@architect`
- [ ] Address any architectural concerns

---

## Phase 6: Implementation

- [ ] Implement features using `/skill implementation`
- [ ] Make tests pass one at a time (GREEN phase)
- [ ] Refactor for quality (REFACTOR phase)

---

## Phase 7: Quality Assurance

- [ ] Run linting: `task lint`
- [ ] Run type checking: `task static-check`
- [ ] Verify coverage ≥ {{cookiecutter.minimum_coverage}}%: `task test`
- [ ] Run property-based tests with Hypothesis

---

## Phase 8: Release

- [ ] Create release using `@repo-manager /skill git-release`
- [ ] Update documentation
- [ ] Deploy if applicable

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
