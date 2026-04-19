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
| **Where used** | Justifies the full `living-docs` skill: C4 diagrams answer "what does this module depend on?"; the ADR record answers "why was it written this way?"; the living glossary answers "what does this term mean in this context?". Collectively these eliminate the three most frequent information needs identified by Ko et al. |

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
| **Where used** | Justifies co-locating `docs/` within the project repository. Living docs (`docs/architecture/c4/`, `docs/glossary.md`) are updated in the same commits as the code they describe. The `living-docs` skill is the mechanism that enforces this — it runs after Step 5 to regenerate diagrams from the current state of the codebase and discovery docs. |

---

### 61. Diátaxis — A Systematic Framework for Technical Documentation

| | |
|---|---|
| **Source** | Procida, D. (2021). "Diátaxis — A systematic approach to technical documentation." *diataxis.fr*. https://diataxis.fr |
| **Date** | 2021 |
| **Status** | Confirmed — adopted by Django, NumPy, Gatsby, Cloudflare, and the Python Software Foundation |
| **Core finding** | Technical documentation fails because it conflates four fundamentally different needs into a single undifferentiated text. The four types are: **Tutorials** (learning-oriented; guides a beginner through a complete task), **How-to guides** (task-oriented; solves a specific problem for a practitioner), **Reference** (information-oriented; describes the system accurately and completely), **Explanation** (understanding-oriented; discusses concepts and decisions). Each type has a different audience mental state and requires a different writing mode. Mixing them degrades all four. |
| **Mechanism** | The two axes of Diátaxis are: **practical ↔ theoretical** (tutorials and how-to guides are practical; reference and explanation are theoretical) and **acquiring ↔ applying** (tutorials and explanation are for acquiring knowledge; how-to guides and reference are for applying it). A document that tries to be both a tutorial and a reference simultaneously will be a poor tutorial (too much information) and a poor reference (not structured for lookup). |
| **Where used** | Documentation structure in this template maps to Diátaxis: `README.md` = tutorial (getting started), `AGENTS.md` = reference (complete description of roles, skills, commands) and explanation (why the workflow exists), `docs/c4/` = reference (system structure), post-mortems = explanation (why decisions were made). The `living-docs` skill produces reference-type documentation (C4 diagrams, glossary) — not tutorials. |

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
| **Where used** | `docs/post-mortem/` directory. Post-mortems in this template follow the blameless model: they report workflow gaps found, not who made the mistake. The output of each post-mortem is a list of improvements to skills, agents, or workflow documentation. The `living-docs` skill is one such improvement — it emerged from the discovery that architecture and glossary documentation were falling behind the codebase. |

---

## Bibliography

1. Allspaw, J. (2012). Blameless PostMortems and a Just Culture. *code.etsy.com*. https://www.etsy.com/codeascraft/blameless-postmortems/
2. Dagenais, B., & Robillard, M. P. (2010). Creating and evolving developer documentation. *Proc. FSE 2010*, pp. 127–136. ACM.
3. Dekker, S. (2006). *The Field Guide to Understanding Human Error*. Ashgate.
4. Ko, A. J., DeLine, R., & Venolia, G. (2007). Information Needs in Collocated Software Development Teams. *Proc. ICSE 2007*, pp. 344–353. https://doi.org/10.1109/ICSE.2007.45
5. Procida, D. (2021). Diátaxis — A systematic approach to technical documentation. *diataxis.fr*. https://diataxis.fr
6. Winters, T., Manshreck, T., & Wright, H. (2020). *Software Engineering at Google*. O'Reilly. Chapter 10. https://abseil.io/resources/swe-book/html/ch10.html
