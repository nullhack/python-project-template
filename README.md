# Python Project Template

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge)](https://nullhack.github.io/python-project-template/coverage/)

[![CI](https://img.shields.io/github/actions/workflow/status/nullhack/python-project-template/ci.yml?style=for-the-badge&label=CI)](https://github.com/nullhack/python-project-template/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge)](https://www.python.org/downloads/)

> Python template to quickstart any project with production-ready workflow, quality tooling, and AI-assisted development.

## Quick Start

```bash
# 1. Clone the template
git clone https://github.com/nullhack/python-project-template
cd python-project-template

# 2. Install UV package manager (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Set up the development environment
uv sync --all-extras

# 4. Customize template placeholders for your project
opencode && @setup-project

# 5. Validate everything works
uv run task test && uv run task lint && uv run task static-check && timeout 10s uv run task run
```

## What This Template Provides

### Development Workflow

A **6-step Kanban workflow** with WIP=1 (one feature at a time), enforced by the filesystem:

```
docs/features/backlog/       ← features waiting to be worked on
docs/features/in-progress/   ← exactly one feature being built
docs/features/completed/     ← accepted and shipped features
```

**4 roles, 5 steps:**

| Step | Role | What happens |
|------|------|-------------|
| 1. SCOPE | Product Owner | Discovery + Gherkin stories + `@id` criteria |
| 2. ARCH | Software Engineer | Design module structure, read all backlog features |
| 3. TDD LOOP | Software Engineer | RED→GREEN→REFACTOR, one `@id` at a time |
| 4. VERIFY | Reviewer | Run all commands, adversarial code review |
| 5. ACCEPT | Product Owner | Demo, validate, move folder to completed/ |

### AI Agents

```bash
@product-owner   # Defines features, picks from backlog, accepts deliveries
@developer       # Architecture, tests, code, git, releases
@reviewer        # Runs commands, reviews code — read+bash only
@setup-project   # One-time template initialization
```

### Skills

```bash
/skill session-workflow    # Read TODO.md, continue, hand off cleanly
/skill scope               # Write user stories + acceptance criteria
/skill tdd                 # TDD: file naming, docstring format, markers
/skill implementation      # Red-Green-Refactor, architecture, ADRs
/skill code-quality        # redirects to verify (quick reference)
/skill verify              # Step 5 verification checklist
/skill pr-management       # Branch naming, PR template, squash merge
/skill git-release         # Hybrid calver versioning, themed naming
/skill create-skill        # Add new skills to the system
```

## Development Commands

```bash
uv run task run              # Run the application (humans)
timeout 10s uv run task run  # Run with timeout (agents — exit 124 = hung = FAIL)
uv run task test             # Full test suite with coverage report
uv run task test-fast        # Tests without coverage (faster iteration)
uv run task test-slow        # Only slow tests
uv run task lint             # ruff check + format
uv run task static-check     # pyright type checking
uv run task gen-id           # Generate an 8-char hex ID for @id tags
uv run task gen-tests        # Sync test stubs from .feature files
uv run task doc-build        # Generate API docs + coverage + test reports
uv run task doc-publish      # Publish unified docs site to GitHub Pages
uv run task doc-serve        # Live API doc server at localhost:8080
```

## Code Quality Standards

| Standard | Target |
|----------|--------|
| Coverage | 100% |
| Type checking | pyright, 0 errors |
| Linting | ruff, 0 issues, Google docstrings |
| Function length | ≤ 20 lines |
| Class length | ≤ 50 lines |
| Max nesting | 2 levels |
| Principles | YAGNI > KISS > DRY > SOLID > Object Calisthenics |

## Test Conventions

```python
@pytest.mark.unit
def test_bounce_physics_a3f2b1c4() -> None:
    """
    Given: A ball moving upward reaches y=0
    When: The physics engine processes the next frame
    Then: The ball velocity y-component becomes positive
    """
    # Given
    ...
    # When
    ...
    # Then
    ...
```

**Markers**: `@pytest.mark.unit` · `@pytest.mark.integration` · `@pytest.mark.slow` · `@pytest.mark.deprecated`

## Technology Stack

| Category | Tools |
|----------|-------|
| Package management | uv |
| Task automation | taskipy |
| Linting + formatting | Ruff |
| Type checking | PyRight |
| Testing | pytest + Hypothesis |
| Coverage | pytest-cov (100% required) |
| Documentation | pdoc + ghp-import |
| AI development | OpenCode agents + skills |

## Documentation Site

Published at [nullhack.github.io/python-project-template](https://nullhack.github.io/python-project-template):
- **API Reference** — pdoc-generated from source docstrings
- **Coverage Report** — line-by-line coverage breakdown
- **Test Results** — full pytest run results

## Release Versioning

Format: `v{major}.{minor}.{YYYYMMDD}`

Each release gets a unique **adjective-animal** name generated from the commit/PR content.

## Contributing

```bash
git clone https://github.com/nullhack/python-project-template
uv sync --all-extras
uv run task test && uv run task lint
```

## License

MIT — see [LICENSE](LICENSE).

---

**Author:** eol ([@nullhack](https://github.com/nullhack))
**Documentation:** [nullhack.github.io/python-project-template](https://nullhack.github.io/python-project-template)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/nullhack/python-project-template.svg?style=for-the-badge
[contributors-url]: https://github.com/nullhack/python-project-template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nullhack/python-project-template.svg?style=for-the-badge
[forks-url]: https://github.com/nullhack/python-project-template/network/members
[stars-shield]: https://img.shields.io/github/stars/nullhack/python-project-template.svg?style=for-the-badge
[stars-url]: https://github.com/nullhack/python-project-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/nullhack/python-project-template.svg?style=for-the-badge
[issues-url]: https://github.com/nullhack/python-project-template/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[license-url]: https://github.com/nullhack/python-project-template/blob/main/LICENSE
