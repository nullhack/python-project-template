# Python Project Template

Python template with some awesome tools to quickstart any Python project

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
- **epic-workflow**: Manage epic-based development with automatic feature progression and mandatory QA gates

### Workflow Coordination
- **workflow-coordination**: Orchestrate 7-phase development cycle with agent delegation and checkpoint enforcement
- **delegation-coordination**: Agent delegation matrix and routing rules for proper task assignment

### Development Workflow
- **feature-definition**: Define features with SOLID principles and clear requirements
- **prototype-script**: Create quick validation scripts with real data capture
- **gherkin-validation**: Validate Gherkin syntax with Example format preference for BDD scenarios
- **tdd**: Write comprehensive tests using TDD with pytest/hypothesis — includes decision guide for when to use plain TDD, Hypothesis (property-based), or Hypothesis stateful testing
- **signature-design**: Design modern Python interfaces with protocols and type hints
- **implementation**: Implement using TDD methodology with real prototype data
- **code-quality**: Enforce quality with ruff, coverage, hypothesis, and cosmic-ray mutation testing

### Requirements Management
- **requirements-management**: Create and maintain REQUIREMENTS.md with hybrid business+technical format

### Repository Management
- **git-release**: Create semantic releases with hybrid major.minor.calver versioning and themed naming
- **pr-management**: Create and manage pull requests with proper formatting and workflow integration

### Meta Skills
- **create-skill**: Creates new OpenCode skills following the skill definition standard
- **create-agent**: Creates new OpenCode subagents following the agent definition standard

## Available Agents

- **manager**: Development workflow coordinator orchestrating 7-phase development cycle with proper delegation
- **developer**: Main development agent with complete 7-phase TDD workflow and QA integration
- **architect**: Software architect for design review, pattern selection, and SOLID compliance
- **requirements-gatherer**: Business analyst for requirements elicitation and feature analysis
- **overseer**: Quality assurance specialist enforcing standards at mandatory checkpoints with zero tolerance
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

## Docker Commands

```bash
# Development with Docker
docker-compose up                              # Start development environment
docker-compose --profile test up               # Run test suite
docker-compose --profile quality up            # Code quality checks

# Production
docker build --target production -t app:prod . # Build production image
docker-compose -f docker-compose.prod.yml up   # Production testing
docker-compose -f docker-compose.prod.yml --profile security up  # Security scan
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

### Test File Naming

Test filenames should follow <descriptive-group-name>_test.py

### Test Function Naming
```python
# Format: test_<condition>_should_<outcome>
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

**Preferred Format**: Use `Example:` instead of `Scenario:` with mandatory newlines:
```python
def test_federation_created_should_have_active_status():
    """
    Example: Federation creation with valid data
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
- **pytest-html report**: `docs/tests/report.html` - BDD docstrings displayed
- **Coverage report**: `docs/coverage/index.html` - View coverage by file

## Code Quality Standards

- **Linting**: ruff with Google style conventions (D205, D212, D415 disabled for test files to allow BDD docstrings)
- **Type Checking**: pyright
- **Test Coverage**: Minimum 100%
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

The AI analyzes PR content and generates creative, unique names containing a characteristic/adjectiv and an animal name

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

### Example Workflows

#### Starting a new project
```bash
# 1. Start with requirements gathering
@requirements-gatherer  # Interview stakeholders, create analysis
@architect             # Review requirements and approve approach
@developer /skill epic-workflow start-epic "Core Features"
```

#### Epic-based feature development with QA gates

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

# 2. Requirements & Analysis
@requirements-gatherer  # Gather detailed requirements
@overseer              # QA checkpoint: requirements review

# 3. Test Development
@developer /skill tdd  # Write BDD tests
@overseer             # QA checkpoint: test quality review

# 4. Design & Architecture  
@developer /skill signature-design
@architect            # Approve design and patterns

# 5. Implementation
@developer /skill implementation
@overseer             # QA checkpoint: SOLID/DRY/KISS review

# 6. Final Quality
@developer /skill code-quality
@overseer             # QA checkpoint: final approval

# 7. Feature completion - system auto-progresses to next
@developer /skill epic-workflow next-feature
```

#### Creating releases
```bash
# After all epic features complete
@overseer             # Final pre-release QA review
@repo-manager /skill pr-management
@repo-manager /skill git-release
```

#### Session management
```bash
# Start of session
@developer /skill session-workflow  # Read TODO.md, understand state

# End of session
@developer /skill session-workflow  # Update TODO.md, commit changes
```

### Quality Assurance Protocol

**The @overseer agent enforces mandatory QA checkpoints with zero tolerance:**
1. After requirements gathering - completeness review
2. After TDD phase - test quality review (BDD docstrings, naming conventions)
3. After signature design - SOLID/DRY/KISS review
4. After implementation - Object Calisthenics compliance
5. Before feature completion - final approval

**Development cannot proceed without @overseer approval at each gate.**

The @overseer agent also provides auto-delegation recovery for single-shot tasks and enforces all 9 Object Calisthenics rules strictly.
