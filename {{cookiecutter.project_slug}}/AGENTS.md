# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Project Details

| Variable | Value |
|----------|-------|
| **Project Name** | {{cookiecutter.project_name}} |
| **Project Slug** | {{cookiecutter.project_slug}} |
| **Package Name** | {{cookiecutter.package_name}} |
| **Module Name** | {{cookiecutter.module_name}} |
| **Author** | {{cookiecutter.full_name}} |
| **Email** | {{cookiecutter.email}} |
| **GitHub** | @{{cookiecutter.github_username}} |
| **License** | {{cookiecutter.license}} |
| **Version** | {{cookiecutter.version}} |
| **Minimum Coverage** | {{cookiecutter.minimum_coverage}}% |

## Session-Based Development

This project uses a **session workflow** that allows complex development to span multiple AI sessions. Any AI agent can continue work from where the last session stopped.

### How it works

1. **`TODO.md`** at the project root is the shared state between sessions
2. Every session starts by reading `TODO.md` to find the current phase
3. Every session ends by updating `TODO.md` with progress and handoff notes
4. This makes the project AI-agnostic: any agent, any time can continue

### Starting a new session
```bash
# The developer agent reads TODO.md automatically
@developer /skill session-workflow
```

## Available Skills

This project includes custom skills for OpenCode:

### Session Management
- **session-workflow**: Manage multi-session development - read TODO.md, continue from last checkpoint, update progress and hand off cleanly

### Development Workflow
- **feature-definition**: Define features with SOLID principles and clear requirements
- **prototype-script**: Create quick validation scripts with real data capture  
- **tdd**: Write comprehensive tests using TDD with pytest/hypothesis — includes decision guide for when to use plain TDD, Hypothesis (property-based), or Hypothesis stateful testing
- **signature-design**: Design modern Python interfaces with protocols and type hints
- **implementation**: Implement using TDD methodology with real prototype data
- **code-quality**: Enforce quality with ruff, coverage, hypothesis, and cosmic-ray mutation testing

### Repository Management
- **git-release**: Create semantic releases with hybrid major.minor.calver versioning and themed naming
- **pr-management**: Create and manage pull requests with proper formatting and workflow integration

### Meta Skills
- **create-skill**: Creates new OpenCode skills following the skill definition standard
- **create-agent**: Creates new OpenCode subagents following the agent definition standard

## Available Agents

- **developer**: Main development agent with complete 7-phase TDD workflow
- **architect**: Design review and approval agent for SOLID/object calisthenics compliance
- **overseer**: Quality assurance agent - reviews work after each test implementation, requests changes if needed
- **requirements-gatherer**: Gathers project requirements, updates documentation, creates analysis for architect
- **repo-manager**: Repository management for Git operations, PRs, commits, and releases

## Development Commands

```bash
# Install dependencies
uv venv
uv pip install '.[dev]'

# Run the application
task run

# Run tests (full suite with coverage report)
task test

# Run fast tests only (skip slow tests)
task test-fast

# Run slow tests only
task test-slow

# Run linting
task lint

# Run type checking
task static-check

# Serve documentation
task doc-serve

# Build documentation
task doc-build
```

## Documentation

This project uses **pdoc** for API documentation generation:

```bash
# Serve documentation locally
task doc-serve

# Build static documentation with search
task doc-build
```

Generated docs are in `docs/api/` - open `docs/api/index.html` to browse.

## Test Conventions

This project uses BDD-style tests with the following conventions:

### Test Function Naming
```python
# Format: test_<condition>_should_<outcome>
def test_given_<context>_when_<action>_then_<result>(): ...
def test_<condition>_should_<outcome>(): ...
```

### BDD Docstrings
All test functions must have Given/When/Then docstrings:
```python
def test_federation_created_should_have_active_status():
    """
    Given: A valid federation with required fields
    When: Federation is created
    Then: Status should be active
    """
```

### Running Tests

```bash
# Run fast tests (skip slow tests)
task test-fast

# Run only slow tests
task test-slow

# Full test suite with coverage
task test
```

### Checking Test Compliance
- **pytest-html-plus report**: `docs/tests/report.html` - BDD docstrings displayed as test names
- **Coverage report**: `docs/coverage/index.html` - View coverage by file

## Code Quality Standards

- **Linting**: ruff with Google style conventions (D205, D212, D415 disabled for test files to allow BDD docstrings)
- **Type Checking**: pyright
- **Test Coverage**: Minimum {{cookiecutter.minimum_coverage}}%
- **Python Version**: >=3.13
- **Test Markers**: `slow` marks tests >50ms (SQLite, Hypothesis, web routes)

## Release Management

This project uses a hybrid versioning system: `v{major}.{minor}.{YYYYMMDD}`

### Version Examples
- `v1.2.20260302` - Version 1.2, release on March 2, 2026
- `v1.3.20260313` - Version 1.3, release on March 13, 2026
- `v1.4.20260313` - Version 1.4, second release same day (increment minor)

### Release Naming
Releases use AI-generated adjective-animal names. Each release gets a unique name based on PR content. Examples:
- `v1.5.20260403 - Crystal Jellyfish` (documentation overhaul)
- `v1.6.20260404 - Velvet Manta` (refactoring)
- `v1.7.20260405 - Electric Firefly` (performance)

The AI analyzes PR content and generates creative, unique names.

### Creating Releases
Use the repo-manager agent:
```bash
@repo-manager /skill git-release
```

## Using OpenCode

Initialize OpenCode in this project:
```bash
opencode
/opencode
```

Then run `/init` to generate a fresh `AGENTS.md` based on your project's current state.

### Example Workflow

#### Starting a session (always do this first)
```bash
# Read project state and orient for this session
@developer /skill session-workflow
```

#### Full feature development workflow
```bash
# 0. Gather requirements first (for new projects)
@requirements-gatherer  # Ask questions, create analysis, update docs
@architect              # Review analysis and approve design
@developer              # Start implementation with approved TODO

# 1. Define and implement a feature
@developer /skill feature-definition
@developer /skill prototype-script  
@developer /skill tdd
@overseer               # Review tests - request changes if needed
@developer /skill signature-design
@architect             # Review design
@developer /skill implementation
@developer /skill code-quality
@overseer               # Final review before moving on

# 2. Create PR and manage repository
@repo-manager /skill pr-management
@repo-manager /skill git-release
```

#### Ending a session (always do this last)
```bash
# Update TODO.md with progress and handoff notes, then commit
@developer /skill session-workflow
# Follow the "Session End Protocol" in the skill
```
