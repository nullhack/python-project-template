# Scientific Research — Documentation

Foundations for living documentation, docs-as-code, information architecture, and post-mortem practices used in this template.

---

### 59. Information Needs in Collocated Software Development Teams

| | |
|---|---|
| **Source** | Ko, A. J., DeLine, R., & Venolia, G. (2007). "Information Needs in Collocated Software Development Teams." *Proc. 29th International Conference on Software Engineering (ICSE 2007)*, pp. 344–353. IEEE. https://doi.org/10.1109/ICSE.2007.45 |
| **Date** | 2007 |
| **Alternative** | Dagenais, B., & Robillard, M. P. (2010). "Creating and evolving developer documentation." *Proc. FSE 2010*, pp. 127–136. ACM. |
| **Status** | Confirmed — empirical study; 600+ citations |
| **Core finding** | Developers spend 35–50% of their working time not writing code but searching for information — navigating code, reading past decisions, and understanding relationships between components. The most frequently sought information is: who wrote this, why was it written this way, and what does this module depend on. Direct questioning of teammates is the most common fallback when documentation is absent, creating serial bottlenecks. |
| **Mechanism** | Information seeking is triggered by a task, not by curiosity. A developer encountering an unfamiliar component has a specific decision to make. When documentation is absent, the seek-ask-wait loop (find the right person, ask, wait for a response) dominates time. Persistent documentation (ADRs, architecture diagrams, glossary) short-circuits this loop by making the answer findable without a human intermediary. |
| **Where used** | Justifies the full `update-docs` skill: C4 diagrams answer "what does this module depend on?"; the ADR record answers "why was it written this way?"; the living glossary answers "what does this term mean in this context?". Collectively these eliminate the three most frequent information needs identified by Ko et al. |

---

### 60. Software Engineering at Google — Documentation Chapter

| | |
|---|---|
| **Source** | Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google: Lessons Learned from Programming Over Time*. O'Reilly. Chapter 10: "Documentation." https://abseil.io/resources/swe-book/html/ch10.html |
| **Date** | 2020 |
| **Alternative** | Fitzpatrick, B., & Collins-Sussman, B. (2012). *Team Geek*. O'Reilly. |
| **Status** | Confirmed — large-scale industry evidence from a codebase with ~2 billion lines of code |
| **Core finding** | Documentation that lives outside the code repository decays at a rate proportional to how often the code changes — because there is no mechanism that forces the doc to be updated when the code changes. Docs-as-code (documentation in the same repo, reviewed in the same PRs, tested in the same CI pipeline) dramatically reduces divergence because the cost of updating the doc is incurred at the same moment as the cost of the code change. |
| **Mechanism** | Google's g3doc system co-locates docs with the code they describe. When a PR changes `payments/service.py`, the reviewer also sees `payments/README.md` in the diff and can flag staleness immediately. At scale, Google found that docs with no co-located tests or CI checks become stale within 3–6 months regardless of team discipline. |
| **Where used** | Justifies co-locating `docs/` within the project repository. Living docs (`docs/context.md`, `docs/container.md`, `docs/glossary.md`) are updated in the same commits as the code they describe. The `update-docs` skill is the mechanism that enforces this — it runs after Step 5 to regenerate diagrams from the current state of the codebase and discovery docs. |

---

### 61. Diátaxis — A Systematic Framework for Technical Documentation

| | |
|---|---|
| **Source** | Procida, D. (2021). "Diátaxis — A systematic approach to technical documentation." *diataxis.fr*. https://diataxis.fr |
| **Date** | 2021 |
| **Status** | Confirmed — adopted by Django, NumPy, Gatsby, Cloudflare, and the Python Software Foundation |
| **Core finding** | Technical documentation fails because it conflates four fundamentally different needs into a single undifferentiated text. The four types are: **Tutorials** (learning-oriented; guides a beginner through a complete task), **How-to guides** (task-oriented; solves a specific problem for a practitioner), **Reference** (information-oriented; describes the system accurately and completely), **Explanation** (understanding-oriented; discusses concepts and decisions). Each type has a different audience mental state and requires a different writing mode. Mixing them degrades all four. |
| **Mechanism** | The two axes of Diátaxis are: **practical ↔ theoretical** (tutorials and how-to guides are practical; reference and explanation are theoretical) and **acquiring ↔ applying** (tutorials and explanation are for acquiring knowledge; how-to guides and reference are for applying it). A document that tries to be both a tutorial and a reference simultaneously will be a poor tutorial (too much information) and a poor reference (not structured for lookup). |
| **Where used** | Documentation structure in this template maps to Diátaxis: `README.md` = tutorial (getting started), `AGENTS.md` = reference (complete description of roles, skills, commands) and explanation (why the workflow exists), `docs/context.md` and `docs/container.md` = reference (system structure), post-mortems = explanation (why decisions were made). The `update-docs` skill produces reference-type documentation (C4 diagrams, glossary) — not tutorials. |

---

### 62. Blameless Post-Mortems and a Just Culture

| | |
|---|---|
| **Source** | Allspaw, J. (2012). "Blameless PostMortems and a Just Culture." *code.etsy.com* (archived). https://www.etsy.com/codeascraft/blameless-postmortems/ |
| **Date** | 2012 |
| **Alternative** | Dekker, S. (2006). *The Field Guide to Understanding Human Error*. Ashgate. |
| **Status** | Confirmed — foundational DevOps/SRE practice; referenced in Google SRE Book (2016) |
| **Core finding** | Post-mortems that assign blame produce less information and lower long-term system reliability than blameless post-mortems. When individuals believe they will be blamed, they withhold information about contributing factors, preventing the systemic causes from being identified and fixed. A blameless post-mortem treats the incident as a system failure, not an individual failure — asking "what conditions allowed this to happen?" not "who caused this?" |
| **Mechanism** | Allspaw's model separates two questions: (1) what happened? (factual, blameless) and (2) what changes would prevent recurrence? (systemic). The post-mortem document records both. The output is not an individual's performance review but a list of system changes — process improvements, documentation gaps, tooling additions. Etsy's incident rate fell after adopting blameless post-mortems because engineers began reporting near-misses that they previously concealed. |
| **Where used** | `docs/post-mortem/` directory. Post-mortems in this template follow the blameless model: they report workflow gaps found, not who made the mistake. The output of each post-mortem is a list of improvements to skills, agents, or workflow documentation. The `update-docs` skill is one such improvement — it emerged from the discovery that architecture and glossary documentation were falling behind the codebase. |

---

### 69. arc42 — Architecture Documentation Template

| | |
|---|---|
| **Source** | Starke, G., & Hruschka, P. (2022). *arc42 — Pragmatic, practical and proven: Template for documentation of software and system architecture*. https://arc42.org |
| **Date** | 2005 (first release); 2022 (current edition) |
| **Alternative** | Rozanski, N., & Woods, E. (2011). *Software Systems Architecture: Working with Stakeholders Using Viewpoints and Perspectives* (2nd ed.). Addison-Wesley. |
| **Status** | Confirmed — ISO 25010-aligned; widely adopted in European enterprise software; open-source; used by Siemens, Deutsche Telekom, and others |
| **Core finding** | Architecture documentation fails when it conflates two distinct audiences: those who need to understand the system now (operators, new developers, AI agents) and those who need to trace historical decisions (auditors, architects). arc42 separates these explicitly: Section 1 (Introduction and Goals) and Section 4 (Solution Strategy) describe the current state — what the system does and the key decisions governing it — while Section 9 (Architectural Decisions) is the append-only ADR log. Both sections exist simultaneously but serve different readers. |
| **Mechanism** | arc42 provides 12 numbered sections with defined scope for each. The critical separation: current-state sections (1, 4, 5, 6) are rewritten when the system changes; historical sections (9) are append-only. This prevents the common failure mode of treating all architecture documentation as a changelog, which makes it unusable as a reference for onboarding. |
| **Where used** | Justifies the `docs/system.md` pattern: a rewritten current-state snapshot (equivalent to arc42 Sections 1 + 4) that the SA updates at Step 2, distinct from any append-only decision history. Git history provides the audit trail without requiring a separate ADR log file. |

---

### 70. Google Design Docs — Living Specification Pattern

| | |
|---|---|
| **Source** | Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google*. O'Reilly. Chapter 10. https://abseil.io/resources/swe-book/html/ch10.html |
| **Date** | 2020 |
| **Alternative** | Ousterhout, J. (2018). *A Philosophy of Software Design*. Yaknyam Press. (Chapter 15: "Write the Comments First") |
| **Status** | Confirmed — large-scale industry evidence; Google's design doc practice predates the book and is widely replicated at Stripe, Notion, Airbnb |
| **Core finding** | A design doc (also called a technical spec or RFC) is written before implementation and kept current afterward. It is not append-only — it is a living snapshot that reflects how the system works now. Its sections are: goals, non-goals, current state, design decisions, and trade-offs. When the system changes significantly, the design doc is updated (not retired in favour of a replacement) so that it remains the authoritative single reference for the system. Archived (not deleted) only when the system is entirely replaced. |
| **Mechanism** | The design doc is the canonical answer to "what is this system and why does it work this way?" New team members read the design doc, not the git log. The document is kept current because the cost of updating it is low (it is co-located in the repo) and the cost of not updating it is high (onboarding failures, wrong decisions). Unlike ADRs, design docs answer the current state question directly rather than requiring the reader to replay a sequence of decisions. |
| **Where used** | Justifies the rewrite-not-append model for `docs/system.md`. The SA rewrites `docs/system.md` at Step 2 to reflect the system after each feature — same lifecycle as a Google design doc. This entry extends entry 60 (docs-as-code) with the specific design doc pattern. |

---

### 71. RFC / Technical Spec Pattern — Authoritative Living Reference

| | |
|---|---|
| **Source** | Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google*. O'Reilly. (RFC culture at Google, Stripe, Notion, Airbnb). See also: Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution Press. (Chapter 7: "Team Interaction Modes") |
| **Date** | 2020 |
| **Alternative** | RFC 2119 (Bradner, 1997) for the formal RFC model; internal RFC practices at Stripe (public eng blog, 2021) and Notion (public eng blog, 2022) |
| **Status** | Confirmed — widely adopted industry practice; independently replicated across large engineering organizations |
| **Core finding** | A technical spec (RFC, design doc, system doc) is the authoritative description of how the system works now. It is a single document that answers: what is this, who uses it, how is it structured, what are the key constraints. It is not a changelog. When the system changes, the spec is updated in place so it always reflects current reality. When a system is retired, the spec is archived (moved, not deleted) so the record is preserved. The spec is kept current because it is the primary onboarding artifact — the first document a new engineer reads. |
| **Mechanism** | The pattern's authority comes from its singularity: there is exactly one canonical reference. Multiple documents (a design doc here, an ADR log there, a wiki page somewhere else) create the "which one is correct?" problem that degrades onboarding speed. A single rewritten document with git history for audit purposes gives onboarding speed and audit capability simultaneously. |
| **Where used** | Confirms the single-document model for `docs/system.md`. One file, always current, SA rewrites it at Step 2. Git history provides the full change record without requiring a separate append-only log. Entries 69, 70, and 71 together form the evidence base for `docs/system.md` replacing the ADR-log format of `docs/architecture.md`. |

---

## Bibliography

1. Allspaw, J. (2012). Blameless PostMortems and a Just Culture. *code.etsy.com*. https://www.etsy.com/codeascraft/blameless-postmortems/
2. Bradner, S. (1997). Key words for use in RFCs to Indicate Requirement Levels. *RFC 2119*. IETF. https://www.rfc-editor.org/rfc/rfc2119
3. Dagenais, B., & Robillard, M. P. (2010). Creating and evolving developer documentation. *Proc. FSE 2010*, pp. 127–136. ACM.
4. Dekker, S. (2006). *The Field Guide to Understanding Human Error*. Ashgate.
5. Ko, A. J., DeLine, R., & Venolia, G. (2007). Information Needs in Collocated Software Development Teams. *Proc. ICSE 2007*, pp. 344–353. https://doi.org/10.1109/ICSE.2007.45
6. Ousterhout, J. (2018). *A Philosophy of Software Design*. Yaknyam Press.
7. Procida, D. (2021). Diátaxis — A systematic approach to technical documentation. *diataxis.fr*. https://diataxis.fr
8. Rozanski, N., & Woods, E. (2011). *Software Systems Architecture: Working with Stakeholders Using Viewpoints and Perspectives* (2nd ed.). Addison-Wesley.
9. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution Press.
10. Starke, G., & Hruschka, P. (2022). arc42 — Pragmatic, practical and proven. https://arc42.org
11. Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google*. O'Reilly. Chapter 10. https://abseil.io/resources/swe-book/html/ch10.html
