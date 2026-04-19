# Scientific Research — Domain Modeling

Foundations for bounded context identification, ubiquitous language, and feature decomposition used in this template.

---

### 31. Domain-Driven Design — Bounded Contexts and Feature Identification

| | |
|---|---|
| **Source** | Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley. |
| **Date** | 2003 |
| **Alternative** | Context Mapper (2025). Rapid Object-Oriented Analysis and Design. https://contextmapper.org/docs/rapid-ooad |
| **Status** | Confirmed — foundational DDD literature |
| **Core finding** | A Bounded Context is a boundary within which a particular ubiquitous language is consistent. Features are identified by grouping related user stories that share the same language. The decomposition criterion is "single responsibility per context" + "consistency of language." |
| **Mechanism** | In DDD: (1) Extract ubiquitous language from requirements → (2) Group by language consistency → (3) Each group is a candidate bounded context → (4) Each bounded context maps to a feature. Context Mapper automates this: User Stories → Subdomains (via noun/verb extraction) → Bounded Contexts of type FEATURE. |
| **Where used** | Stage 1 Discovery: after session synthesis, verify each feature has consistent language. Noun/verb extraction from discovery answers builds the Domain Model in `docs/discovery.md`. The `Rules (Business):` section in `.feature` files captures the ubiquitous language rules that govern each feature. |

---

## Bibliography

1. Context Mapper. (2025). Rapid Object-Oriented Analysis and Design. https://contextmapper.org/docs/rapid-ooad
2. Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley.
