# Product Definition: temple8

> **Status: ELICITING**
> Fill in each section during Step 1 Discovery. Replace placeholders with project-specific content.

---

## What temple8 IS

- A **Python project template** that gives engineers a production-ready skeleton with zero overhead
- A **delivery workflow** that enforces TDD, traceability, and adversarial review through five explicit steps
- A **documentation-first system** where Gherkin stories trace requirements to tests, ADRs preserve reasoning, and a living domain model keeps everyone aligned
- A **single-command setup** (`opencode && @setup-project`) that personalises the template for your project

## What temple8 IS NOT

- Does NOT provide a runtime engine or application logic — the spawned project defines its own domain
- Does NOT enforce a specific web framework, database, or deployment target
- Does NOT generate code from specs — the AI-assisted workflow writes code, but the human approves every shipment
- Does NOT require any specific AI tool — the workflow is defined in version-controlled YAML, but tool choice is yours

## Why does this exist

AI coding assistants generate code fast, but without tests, without traceability, and without review. Existing project templates give you a folder structure and a CI config, but no enforced delivery discipline. temple8 fills this gap: a template that treats documentation as a first-class artifact and enforces production rigor through a five-step workflow where nothing ships without explicit sign-off.

## Users

- **Developers** — use the template to scaffold a new Python project; pair with AI agents that follow the workflow
- **Product Owners** — write discovery notes, Gherkin stories, and acceptance criteria; accept or reject deliveries
- **System Architects** — design architecture, record ADRs, and adversarially verify implementation

## Out of Scope

- Runtime engine or session tracking
- Specific framework or database integration
- Multi-language support (Python only)
- CI/CD pipeline generation beyond the included GitHub Actions

## Delivery Order

1 → 2 (CLI entrypoint depends on the project being set up)