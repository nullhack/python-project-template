# 🚀 AI-Enhanced Python Project Template

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

> **Ship production-ready Python projects faster with AI-powered development workflows**

### Latest Release: [v1.7.20260410](https://github.com/nullhack/python-project-template/releases/tag/v1.7.20260410) - Vivid Cardinal

Modern cookiecutter template delivering enterprise-grade Python projects with **OpenCode AI agents**, **TDD/BDD workflows**, and **zero-config quality standards**.

## ✨ What You Get

🤖 **Enterprise AI Team** - 5 specialized agents: Developer, Architect, Business Analyst, QA Specialist, Release Engineer  
🏗️ **SOLID Architecture** - Object Calisthenics, Dependency Inversion, Protocol-based design with architect review  
⚡ **Zero-Config Setup** - UV package manager, Ruff formatting, pytest + Hypothesis testing  
🎯 **Mandatory QA Gates** - 4 quality checkpoints enforced by QA specialist throughout development  
🔄 **Smart Releases** - Hybrid calver versioning with AI-generated themed names  
📋 **Epic-Based Workflow** - Requirements-driven development with automatic feature progression

## 🎯 Perfect For

- **Startups** building MVPs with enterprise standards
- **Teams** needing consistent code quality and architecture
- **Developers** wanting AI-assisted TDD/BDD workflows
- **Projects** requiring rapid iteration with zero technical debt

## 🚀 Quick Start

### Prerequisites

Install the required tools:

```bash
# Install OpenCode AI assistant
curl -fsSL https://opencode.ai/install.sh | sh

# Install UV package manager (replaces pip/poetry/virtualenv)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Cookiecutter
pip install cookiecutter
```

### Create Your Project

```bash
# Generate your AI-enhanced Python project
cookiecutter gh:nullhack/python-project-template

# Enter your project directory
cd your-project-name

# Initialize AI development environment
opencode
/init

# Start an epic with requirements gathering
@requirements-gatherer  # Business analysis
@developer /skill epic-workflow start-epic "MVP Features"
```

### Instant Development Ready

```bash
# Install dependencies and activate virtual environment
uv venv && uv pip install -e '.[dev]'

# Run the complete development workflow
task test     # 100% coverage + property-based tests
task lint     # Ruff formatting + static analysis  
task doc-serve # Live documentation server

# Deploy with confidence
@repo-manager /skill git-release
```

## 🏛️ Architecture & Workflow

### Epic-Based Development with Mandatory QA Gates

1. **Requirements Gathering** → Business analyst conducts stakeholder interviews
2. **QA Gate #1** → Requirements completeness review by QA specialist
3. **Test-Driven Development** → BDD-style tests with pytest + Hypothesis
4. **QA Gate #2** → Test quality and coverage review
5. **Design & Architecture** → Pattern selection and SOLID design by architect
6. **Implementation** → TDD methodology with Red-Green-Refactor cycle
7. **QA Gate #3** → SOLID/DRY/KISS compliance review
8. **Final Quality** → Comprehensive quality checks
9. **QA Gate #4** → Final approval before feature completion
10. **Automatic Progression** → System advances to next feature in epic

### Smart Release Management

- **Hybrid Versioning**: `v{major}.{minor}.{YYYYMMDD}` (same-day releases increment minor)
- **Themed Releases**: AI-generated names based on PR sentiment
  - Performance: `"Swift Cheetah"` `"Lightning Falcon"`  
  - Security: `"Vigilant Owl"` `"Guardian Bear"`
  - Features: `"Creative Fox"` `"Innovative Dolphin"`

## 🔧 Included Technology Stack

**Development**
- Python 3.13+ with modern type hints
- UV for blazing-fast dependency management
- Ruff for linting and formatting (replaces 8+ tools)
- PyTest + Hypothesis for comprehensive testing

**AI Integration - Your Enterprise Development Team**  
- **@developer**: Development Lead implementing TDD workflow with QA integration
- **@architect**: Software Architect ensuring SOLID principles and design patterns
- **@requirements-gatherer**: Business Analyst using BABOK methodology
- **@overseer**: QA Specialist enforcing mandatory quality checkpoints
- **@repo-manager**: Release Engineer handling versioning and deployments

**Quality Assurance**
- 100% test coverage requirement
- Static type checking with Pyright
- Property-based testing for edge cases
- Mutation testing with Cosmic Ray

**Documentation & Deployment**
- pdoc for API documentation with search
- pytest-html-plus with BDD docstring display
- Docker containerization
- GitHub Actions CI/CD
- Automated documentation deployment


## 📈 Template Roadmap

- [x] ✨ AI-powered development workflow with OpenCode integration
- [x] 🏗️ SOLID architecture enforcement with object calisthenics  
- [x] 🤖 Automated repository management with smart releases
- [x] ⚡ Modern toolchain (UV, Ruff, PyTest, Hypothesis)
- [x] 📋 Epic-based workflow with automatic feature progression
- [x] 🎯 Mandatory QA gates with dedicated QA specialist agent
- [x] 💼 Business analyst agent for requirements gathering
- [ ] 🔒 Advanced security scanning and SBOM generation
- [ ] 📊 Performance benchmarking and optimization workflows

## 🤝 Contributing

Contributions make this template better for everyone! We welcome:

- 🐛 Bug reports and fixes
- ✨ New agents and skills  
- 📚 Documentation improvements
- 🎯 Workflow optimizations

```bash
# Quick contribution setup
cookiecutter gh:nullhack/python-project-template
cd your-contribution
@developer /skill feature-definition
@repo-manager /skill pr-management
```

## 📄 License

MIT License - see [`LICENSE`](LICENSE) for details.

## 🙏 Credits

Built on the shoulders of giants:

- [OpenCode](https://opencode.ai) - AI-powered development platform
- [UV](https://astral.sh/uv/) - Blazing fast Python package manager  
- [Ruff](https://astral.sh/ruff/) - Extremely fast Python linter
- [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) - Modern Python practices
- [Hypothesis](https://hypothesis.readthedocs.io/) - Property-based testing framework

---

**[⭐ Star this repo](https://github.com/nullhack/python-project-template) if it powers your next breakthrough!**


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/nullhack/python-project-template.svg?style=for-the-badge
[contributors-url]: https://github.com/nullhack/python-project-template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nullhack/python-project-template.svg?style=for-the-badge
[forks-url]: https://github.com/nullhack/python-project-template/network/members
[stars-shield]: https://img.shields.io/github/stars/nullhack/python-project-template.svg?style=for-the-badge
[stars-url]: https://github.com/nullhack/python-project-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/nullhack/python-project-template.svg?style=for-the-badge
[issues-url]: https://github.com/nullhack/python-project-template/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[license-url]: https://github.com/nullhack/python-project-template/blob/main/LICENSE.txt
