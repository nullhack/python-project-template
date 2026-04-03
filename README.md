# 🚀 AI-Enhanced Python Project Template

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

> **Ship production-ready Python projects faster with AI-powered development workflows**

Modern cookiecutter template delivering enterprise-grade Python projects with **OpenCode AI agents**, **TDD/BDD workflows**, and **zero-config quality standards**.

## ✨ What You Get

🤖 **AI-Powered Development** - OpenCode agents for architecture review, TDD implementation, and repository management  
🏗️ **SOLID Architecture** - Object calisthenics, dependency inversion, and protocol-based design  
⚡ **Zero-Config Setup** - UV package manager, Ruff formatting, PyTest + Hypothesis testing  
🎯 **Quality Enforced** - 100% coverage, static typing, property-based testing  
🔄 **Smart Releases** - Calver versioning with AI-generated themed names  
📋 **Complete Workflows** - 7-phase development cycle from prototype to production

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

# Start developing with AI assistance
@developer /skill feature-definition
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

### 7-Phase AI Development Cycle

1. **Feature Definition** → SOLID principles planning with acceptance criteria
2. **Prototype Validation** → Quick scripts with real data capture
3. **Test-Driven Development** → BDD-style tests using pytest + hypothesis  
4. **Signature Design** → Protocol-based interfaces with type safety
5. **Architecture Review** → AI architect validates SOLID compliance
6. **Implementation** → Method-by-method TDD with real prototype data
7. **Quality Assurance** → Automated quality gates and deployment

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

**AI Integration**  
- OpenCode agents for development automation
- Architect agent for design review and SOLID compliance
- Repository manager for releases and PR workflows

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
- [ ] 🌐 Multi-language template support (TypeScript, Rust)
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
