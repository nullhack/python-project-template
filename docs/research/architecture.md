# Scientific Research — Architecture

Foundations for the architectural decisions and patterns used in this template.

---

### 42. Hexagonal Architecture — Ports and Adapters

| | |
|---|---|
| **Source** | Cockburn, A. (2005). "Hexagonal Architecture." *alistair.cockburn.us*. https://alistair.cockburn.us/hexagonal-architecture/ |
| **Date** | 2005 |
| **Alternative** | Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley. (Chapter 7: "Ports and Adapters") |
| **Status** | Confirmed — foundational; widely adopted as Clean Architecture, Onion Architecture |
| **Core finding** | The application domain should have no knowledge of external systems (databases, filesystems, network, UI). All contact between the domain and the outside world passes through a **port** (an interface / Protocol) and an **adapter** (a concrete implementation of that port). The domain is independently testable without any infrastructure. The key structural rule: dependency arrows point inward — domain code never imports from adapters; adapters import from domain. |
| **Mechanism** | Two distinct sides of any application: the "driving side" (actors who initiate action — tests, UI, CLI) and the "driven side" (actors the application drives — databases, filesystems, external services). Each driven-side dependency is hidden behind a port. Tests supply a test adapter; production supplies a real adapter. Substituting adapters requires no domain code changes. This is SOLID-D at the architectural layer. |
| **Where used** | Step 2 (Architecture): if an external dependency is identified during domain analysis, assign it a Protocol. `ports/` and `adapters/` folders emerge when a concrete dependency is confirmed — do not pre-create them. The dependency-inversion principle (SOLID-D) is the goal; the folder names are convention, not law. |

---

### 55. Architecture Decision Records (ADRs)

| | |
|---|---|
| **Source** | Nygard, M. T. (2011). "Documenting Architecture Decisions." *cognitect.com*. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions |
| **Date** | 2011 |
| **Alternative** | Keeling, M. (2017). *Design It!: From Programmer to Software Architect*. Pragmatic Bookshelf. (Chapter 6: "Architectural Decisions") |
| **Status** | Confirmed — widely adopted industry standard; tooled by adr-tools, ADR Manager, Log4Brains |
| **Core finding** | Architectural decisions should be recorded as short, immutable documents capturing: what was decided, why, and what alternatives were rejected. Without this record, decisions get re-litigated by every new developer (or AI agent) who encounters the codebase, producing rework and re-divergence. |
| **Mechanism** | An ADR is written at decision time, never edited afterward. If the decision changes, a new ADR is written that supersedes the old one. The append-only record becomes a reliable audit trail. The constraint "one sentence per field" forces clarity — if you can't state the reason in one sentence, the decision is not yet understood. |
| **Where used** | `docs/adr/ADR-YYYY-MM-DD-<slug>.md` (one file per decision). SE creates one file per non-obvious decision after Step 2. The `update-docs` skill reads ADRs as input for C4 diagram annotations. |

---

### 56. The 4+1 View Model of Architecture

| | |
|---|---|
| **Source** | Kruchten, P. B. (1995). "The 4+1 View Model of Architecture." *IEEE Software*, 12(6), 42–50. https://doi.org/10.1109/52.469759 |
| **Date** | 1995 |
| **Alternative** | Bass, L., Clements, P., & Kazman, R. (2021). *Software Architecture in Practice* (4th ed.). Addison-Wesley. |
| **Status** | Confirmed — 3,000+ citations; foundational IEEE reference for architectural documentation |
| **Core finding** | A single architectural diagram cannot communicate all relevant aspects of a system. Four distinct views are required: **Logical** (domain objects and relationships), **Process** (runtime behavior and concurrency), **Development** (module organisation and dependencies), **Physical** (deployment topology). A fifth **Scenarios** view (use cases) ties the four together by showing how each scenario exercises each view. |
| **Mechanism** | Different stakeholders need different views: a developer needs the Development view; an operator needs the Physical view; a domain expert needs the Logical view. Conflating views into one diagram produces a cluttered diagram that satisfies nobody. The 4+1 model assigns each concern to its appropriate view and cross-validates them through scenarios. |
| **Where used** | Theoretical foundation for the C4 model (entry 57). The `update-docs` skill generates C4 diagrams that map to: Context diagram (Scenarios view), Container diagram (Physical + Development views), Component diagram (Logical + Development views). |

---

### 57. The C4 Model for Software Architecture

| | |
|---|---|
| **Source** | Brown, S. (2018). *The C4 Model for Software Architecture*. Leanpub. https://c4model.com |
| **Date** | 2018 (ongoing) |
| **Alternative** | Brown, S. (2023). "The C4 model for visualising software architecture." *InfoQ*. |
| **Status** | Confirmed — widely adopted; tooled by Structurizr, PlantUML C4, Mermaid C4 |
| **Core finding** | Software architecture can be communicated at four zoom levels: **Level 1 — System Context** (who uses the system and what external systems it talks to), **Level 2 — Container** (major runnable/deployable units), **Level 3 — Component** (major structural building blocks within a container), **Level 4 — Code** (classes, interfaces; usually auto-generated). Each level answers a specific question; mixing levels in one diagram creates confusion. |
| **Mechanism** | C4 operationalises the 4+1 View Model (entry 56) into a lightweight notation that can be expressed in text (PlantUML, Mermaid) and version-controlled alongside code. The notation is deliberately constrained: boxes (people, systems, containers, components) and unidirectional arrows with labels. No UML formalism required. Context + Container diagrams cover >90% of communication needs for most teams. |
| **Where used** | The `update-docs` skill generates and updates C4 diagrams in `docs/context.md` and `docs/container.md`. Context diagram (L1) always generated; Container (L2) generated when multiple containers are identified; Component (L3) generated on demand. Source files are Mermaid so they render in GitHub and are version-controlled. |

---

### 58. Information Hiding — Module Decomposition Criterion

| | |
|---|---|
| **Source** | Parnas, D. L. (1972). "On the criteria to be used in decomposing systems into modules." *Communications of the ACM*, 15(12), 1053–1058. https://doi.org/10.1145/361598.361623 |
| **Date** | 1972 |
| **Alternative** | Parnas, D. L. (1974). "On a 'buzzword': Hierarchical structure." *Proc. IFIP Congress 74*, 336–339. |
| **Status** | Confirmed — 4,000+ citations; foundational criterion for all modular decomposition in software engineering |
| **Core finding** | The correct criterion for decomposing a system into modules is **information hiding**: each module hides a design decision that is likely to change. A module's interface reveals only what callers need; its implementation hides how. Decomposing by execution steps (procedure-based) creates tight coupling to implementation order; decomposing by change-prone decisions (information-hiding) allows each decision to be changed independently. |
| **Mechanism** | Identify which decisions are most likely to change (data structures, algorithms, I/O formats, external service protocols). Each such decision becomes a module boundary. The module's public interface is defined to be change-stable; the implementation is change-free from the caller's perspective. This is the theoretical basis for SOLID-D (depend on abstractions), Hexagonal Architecture (hide external decisions behind ports), and DDD bounded contexts (hide language decisions behind context boundaries). |
| **Where used** | Step 2 Architecture: bounded context check ("same word, different meaning across features? → module boundary") and external dep Protocol assignment both apply the information-hiding criterion. The `update-docs` skill uses module boundaries as container/component boundaries in `docs/container.md`. |

---

## Bibliography

1. Bass, L., Clements, P., & Kazman, R. (2021). *Software Architecture in Practice* (4th ed.). Addison-Wesley.
2. Brown, S. (2018). *The C4 Model for Software Architecture*. Leanpub. https://c4model.com
3. Cockburn, A. (2005). Hexagonal Architecture. *alistair.cockburn.us*. https://alistair.cockburn.us/hexagonal-architecture/
4. Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley.
5. Keeling, M. (2017). *Design It!: From Programmer to Software Architect*. Pragmatic Bookshelf.
6. Kruchten, P. B. (1995). The 4+1 View Model of Architecture. *IEEE Software*, 12(6), 42–50. https://doi.org/10.1109/52.469759
7. Nygard, M. T. (2011). Documenting Architecture Decisions. *cognitect.com*. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
8. Parnas, D. L. (1972). On the criteria to be used in decomposing systems into modules. *CACM*, 15(12), 1053–1058. https://doi.org/10.1145/361598.361623
