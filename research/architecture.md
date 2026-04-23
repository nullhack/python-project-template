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
| **Mechanism** | An ADR is written at decision time, never edited afterward. If the decision changes, a new ADR is written that retires the old one in favour of the new (the old ADR's status becomes `Deprecated`). The append-only record becomes a reliable audit trail. The constraint "one sentence per field" forces clarity — if you can't state the reason in one sentence, the decision is not yet understood. ADRs include an Interview section with the self-interview Q&A that produced the decision. |
| **Where used** | `docs/adr/ADR-YYYY-MM-DD-<slug>.md` (one file per related decision group). SA drafts ADRs after self-interview at Step 2, then presents a validation table to the stakeholder before committing. The `update-docs` skill reads ADRs as input for context/container table annotations. |

---

### 56. The 4+1 View Model of Architecture

| | |
|---|---|
| **Source** | Kruchten, P. B. (1995). "The 4+1 View Model of Architecture." *IEEE Software*, 12(6), 42–50. https://doi.org/10.1109/52.469759 |
| **Date** | 1995 |
| **Alternative** | Bass, L., Clements, P., & Kazman, R. (2021). *Software Architecture in Practice* (4th ed.). Addison-Wesley. |
| **Status** | Confirmed — 3,000+ citations; foundational IEEE reference for architectural documentation |
| **Core finding** | A single architectural diagram cannot communicate all relevant aspects of a system. Four distinct views are required: **Logical** (domain objects and relationships), **Process** (runtime behaviour and concurrency), **Development** (module organisation and dependencies), **Physical** (deployment topology). A fifth **Scenarios** view (use cases) ties the four together by showing how each scenario exercises each view. |
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

---

### 59. Architecture Tradeoff Analysis Method (ATAM)

| | |
|---|---|
| **Source** | Kazman, R., Klein, M., & Clements, P. (2000). "ATAM: Method for Architecture Evaluation" (CMU/SEI-2000-TR-004). Software Engineering Institute, Carnegie Mellon University. https://resources.sei.cmu.edu/asset_files/TechnicalReport/2000_005_001_13706.pdf |
| **Date** | 2000 (updated 2018) |
| **Alternative** | Bass, L., Clements, P., & Kazman, R. (2021). *Software Architecture in Practice* (4th ed.). Addison-Wesley. (Chapters 21–23) |
| **Status** | Confirmed — SEI standard; used by NASA, DoD, and Fortune 500 organisations |
| **Core finding** | Architecture should be evaluated early through structured scenario analysis. ATAM discovers **trade-offs** and **sensitivity points** before implementation begins, when change cost is minimal. The method produces a risk-mitigation roadmap rather than a pass/fail verdict. |
| **Mechanism** | Nine-step process: (1) present ATAM, (2) present business drivers, (3) present architecture, (4) identify architectural approaches, (5) generate quality-attribute utility tree, (6) analyse architectural approaches, (7) brainstorm and prioritise scenarios, (8) re-analyse with broader stakeholder input, (9) present results. Key output: a ranked list of **risk themes** with sensitivity points (architectural decisions that most affect quality attributes). |
| **Where used** | Step 4 (Verify): the system-architect applies ATAM-style adversarial review — testing the implemented architecture against the quality-attribute scenarios identified in Step 2. The SA who designed the architecture reviews it, eliminating the context-loss problem of external reviewers. |

---

### 60. Conway's Law and the Inverse Conway Maneuver

| | |
|---|---|
| **Source** | Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4), 28–31. https://www.melconway.com/Home/Committees_Paper.html |
| **Date** | 1968 (dubbed "Conway's Law" by Brooks, 1975) |
| **Alternative** | Fowler, M. (2022). "Conway's Law." *martinfowler.com*. https://martinfowler.com/bliki/ConwaysLaw.html |
| **Status** | Confirmed — universally accepted; Brooks called it "the most important law in software engineering" |
| **Core finding** | Any organisation that designs a system will produce a design whose structure is a copy of the organisation's communication structure. The **Inverse Conway Maneuver** deliberately alters team organisation to encourage the desired software architecture — aligning Conway's Law with architectural intent rather than fighting it. |
| **Mechanism** | Three responses to Conway's Law: (1) **Ignore** — architecture clashes with team structure, producing friction; (2) **Accept** — ensure architecture does not conflict with existing communication patterns; (3) **Inverse Conway** — restructure teams (and agent roles) to match the desired architecture. In AI-assisted development, this means the agent who designs a module should be the same agent who reviews it, preserving architectural intent through the build-and-review cycle. |
| **Where used** | AGENTS.md role design: the system-architect → software-engineer → system-architect loop implements a closed communication path. The SA designs the module boundary; the SE builds within it; the SA verifies the boundary was respected. No external reviewer introduces misaligned mental models. |

---

### 61. The Architect as Decision-Maker

| | |
|---|---|
| **Source** | Fowler, M. (2003). "Who Needs an Architect?" *IEEE Software*, 20(5), 11–13. https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf |
| **Date** | 2003 |
| **Alternative** | Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall. (Chapters 1–3) |
| **Status** | Confirmed — IEEE standard reference; Martin's "Clean Architecture" extends to policy/detail separation |
| **Core finding** | The architect's job is not to draw diagrams — it is to make **significant decisions** that are hard to change later. The architect is a facilitator who builds consensus around technical direction, not a dictator who issues edicts. The best architects are also programmers who understand implementation constraints firsthand. |
| **Mechanism** | Fowler distinguishes four architect archetypes: (1) **Architect as decision-maker** — owns the hard-to-change choices; (2) **Architect as expert** — provides technical depth the team lacks; (3) **Architect as facilitator** — brings stakeholders to consensus; (4) **Architect as gatekeeper** — enforces standards. The template's system-architect role combines (1) and (4): making architectural decisions (ADRs) and enforcing them through adversarial review. Martin adds the **policy/detail** separation: the architect owns policy (business rules, interfaces); the developer owns detail (algorithms, data structures). |
| **Where used** | `system-architect.md` agent definition: the SA owns `docs/domain-model.md`, `docs/system.md`, and `docs/adr/ADR-*.md` (policy layer). The SE owns the implementation code (detail layer). The SA reviews to ensure policy was not violated by detail decisions. |

---

### 62. Team Topologies and Cognitive Load

| | |
|---|---|
| **Source** | Skelton, M., & Pais, M. (2019). *Team Topologies: Organizing Business and Technology Teams for Fast Flow*. IT Revolution Press. |
| **Date** | 2019 |
| **Alternative** | Narayan, S. (2015). *Agile IT Organization Design*. Addison-Wesley. |
| **Status** | Confirmed — widely adopted in DevOps and platform engineering; 4.5+ star ratings across retailers |
| **Core finding** | Team structure should minimise **cognitive load** — the total mental effort required to operate within a system. Cognitive load has three types: (1) **intrinsic** (fundamental complexity of the problem), (2) **extraneous** (unnecessary complexity from poor tooling/process), (3) **germane** (effort to build reusable abstractions). The goal is to maximise germane load (learning) while minimising extraneous load (friction). |
| **Mechanism** | Four team types: **Stream-aligned** (delivers customer value end-to-end), **Platform** (provides internal services), **Enabling** (helps stream teams adopt new capabilities), **Complicated-subsystem** (owns complex domain expertise). Three interaction modes: **Collaboration** (joint discovery), **X-as-a-Service** (clean handoff), **Facilitating** (temporary assistance). The SA→SE→SA loop is a **Collaboration** interaction between policy owner (SA) and detail owner (SE), with the SA providing **X-as-a-Service** interfaces (stubs, ADRs) that the SE consumes. |
| **Where used** | AGENTS.md workflow design: the SA is a **complicated-subsystem** team (architectural expertise) and the SE is **stream-aligned** (feature delivery). The verify step is a **Collaboration** interaction where the SA reviews whether the SE respected the X-as-a-Service boundaries (stubs, protocols, ADRs). |

---

## Bibliography

1. Bass, L., Clements, P., & Kazman, R. (2021). *Software Architecture in Practice* (4th ed.). Addison-Wesley.
2. Brown, S. (2018). *The C4 Model for Software Architecture*. Leanpub. https://c4model.com
3. Cockburn, A. (2005). Hexagonal Architecture. *alistair.cockburn.us*. https://alistair.cockburn.us/hexagonal-architecture/
4. Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4), 28–31.
5. Fowler, M. (2003). "Who Needs an Architect?" *IEEE Software*, 20(5), 11–13.
6. Fowler, M. (2022). "Conway's Law." *martinfowler.com*. https://martinfowler.com/bliki/ConwaysLaw.html
7. Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley.
8. Kazman, R., Klein, M., & Clements, P. (2000). "ATAM: Method for Architecture Evaluation" (CMU/SEI-2000-TR-004). SEI, CMU.
9. Keeling, M. (2017). *Design It!: From Programmer to Software Architect*. Pragmatic Bookshelf.
10. Kruchten, P. B. (1995). The 4+1 View Model of Architecture. *IEEE Software*, 12(6), 42–50.
11. Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.
12. Nygard, M. T. (2011). Documenting Architecture Decisions. *cognitect.com*.
13. Parnas, D. L. (1972). On the criteria to be used in decomposing systems into modules. *CACM*, 15(12), 1053–1058.
14. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution Press.
3. Cockburn, A. (2005). Hexagonal Architecture. *alistair.cockburn.us*. https://alistair.cockburn.us/hexagonal-architecture/
4. Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley.
5. Keeling, M. (2017). *Design It!: From Programmer to Software Architect*. Pragmatic Bookshelf.
6. Kruchten, P. B. (1995). The 4+1 View Model of Architecture. *IEEE Software*, 12(6), 42–50. https://doi.org/10.1109/52.469759
7. Nygard, M. T. (2011). Documenting Architecture Decisions. *cognitect.com*. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
8. Parnas, D. L. (1972). On the criteria to be used in decomposing systems into modules. *CACM*, 15(12), 1053–1058. https://doi.org/10.1145/361598.361623
