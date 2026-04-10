# Python Project Template

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge)](docs/coverage/index.html)

> Python template with some awesome tools to quickstart any Python project

**AI-Enhanced Python Project** built with enterprise-grade architecture, TDD workflows, and zero-config quality standards.

---

## ⚡ Quick Start

```bash
# Clone and setup
git clone https://github.com/nullhack/python-project-template
cd python-project-template

# Install UV package manager (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize AI development environment
opencode && /init

# Setup development environment
uv venv && uv pip install -e '.[dev]'

# Validate everything works
task test && task lint && task static-check
```

## 🤖 AI-Powered Development

This project includes built-in AI agents to accelerate your development.

### Multi-Session Development

Complex projects are developed across multiple AI sessions. `TODO.md` at the root acts as the shared state — any AI agent can pick up exactly where the last session stopped.

```bash
# Start any session: read state, orient, continue
@developer /skill session-workflow

# End any session: update TODO.md, commit progress, hand off
@developer /skill session-workflow
```

### Feature Development Workflow

```bash
# Define new features with SOLID principles
@developer /skill feature-definition

# Create prototypes and validate concepts  
@developer /skill prototype-script

# Write comprehensive tests first (TDD)
@developer /skill tdd

# Get architecture review before implementing
@architect

# Implement with guided TDD workflow
@developer /skill implementation

# Create releases with smart versioning
@repo-manager /skill git-release
```

## 🏗️ Architecture & Standards

- **🎯 SOLID Principles** - Single responsibility, dependency inversion, clean interfaces
- **🔧 Object Calisthenics** - No primitives, small classes, behavior-rich objects
- **🧪 TDD Testing** - 100% coverage requirement with property-based tests
- **⚡ Modern Toolchain** - UV, Ruff, PyTest, Hypothesis, PyRight
- **🚀 Smart Releases** - Calver versioning with AI-generated themed names

## 📋 Development Commands

```bash
# Core development workflow
task run              # Execute main application
task test             # Run comprehensive test suite  
task lint             # Format and lint code
task static-check     # Type safety validation
task doc-serve        # Live pdoc documentation server
task doc-build        # Build static pdoc API docs
task doc-publish      # Publish API docs to GitHub Pages

# Quality assurance
task test-report      # Detailed coverage report
task mut-report       # Mutation testing (optional)
```

## 🎯 Project Structure

```
python-project-template/
├── python_package_template/        # Main application package
│   ├── __init__.py                       # Package initialization
│   └── python_module_template.py   # Core module
├── .opencode/                            # AI development agents
│   ├── agents/                           # Specialized AI agents
│   │   ├── developer.md                  # 7-phase development workflow
│   │   ├── architect.md                  # SOLID architecture review
│   │   └── repo-manager.md               # Release and PR management
│   └── skills/                           # Development skills
│       ├── session-workflow/             # Multi-session development state
│       ├── feature-definition/           # Requirements planning
│       ├── tdd/                          # Test-driven development
│       ├── implementation/               # Guided implementation
│       └── code-quality/                 # Quality enforcement
├── tests/                                # Comprehensive test suite
├── docs/                                 # Documentation (api/, tests/, coverage/)
├── TODO.md                               # Development roadmap & session state
├── Dockerfile                            # Multi-stage container build
└── pyproject.toml                        # Project configuration
```

## 🔧 Technology Stack

| Category | Tools |
|----------|-------|
| **Package Management** | UV (blazing fast pip/poetry replacement) |
| **Code Quality** | Ruff (linting + formatting), PyRight (type checking) |
| **Testing** | PyTest + Hypothesis (property-based testing), pytest-html-plus (BDD reports) |
| **AI Integration** | OpenCode agents for development automation |
| **Documentation** | pdoc with search functionality |
| **Containerization** | Docker with optimized multi-stage builds |

## 📈 Quality Metrics

- ✅ **100% Test Coverage** - Comprehensive test suite including edge cases
- ✅ **Static Type Safety** - Full type hints with protocol-based interfaces  
- ✅ **Zero Linting Issues** - Automated formatting and style enforcement
- ✅ **Property-Based Testing** - Hypothesis for robust validation
- ✅ **Architecture Compliance** - AI-enforced SOLID principles

## 🚀 Deployment Ready

```bash
# Production container build
docker build --target prod -t python_package_template:latest .
docker run python_package_template:latest

# Build API documentation
task doc-build  # Generates docs/api/index.html

# Publish API docs to GitHub Pages
task doc-publish  # Pushes docs/api to gh-pages branch

# Smart release management
@repo-manager /skill git-release
# Creates versioned release: v1.2.20260315 "Creative Fox"
```

## 🤝 Contributing

Built with AI-assisted development workflows:

```bash
# Start a new feature
@developer /skill feature-definition
@developer /skill prototype-script
@developer /skill tdd
@architect  # Architecture review
@developer /skill implementation
@repo-manager /skill pr-management
```

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## 🙏 Built With

- [AI-Enhanced Python Template](https://github.com/nullhack/python-project-template) - Enterprise-grade Python project template
- [OpenCode](https://opencode.ai) - AI-powered development platform
- [UV](https://astral.sh/uv/) - Modern Python package manager
- [Ruff](https://astral.sh/ruff/) - Extremely fast Python linter

---

**Author:** USER_NAME ([@nullhack](https://github.com/nullhack))  
**Project:** [python-project-template](https://github.com/nullhack/python-project-template)  
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