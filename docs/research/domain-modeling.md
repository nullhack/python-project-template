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
| **Where used** | Stage 1 Discovery: after session synthesis, verify each feature has consistent language. Noun/verb extraction from discovery answers produces candidate entities, formalized by the SA in `docs/domain-model.md` at Step 2. The `Rules (Business):` section in `.feature` files captures the ubiquitous language rules that govern each feature. |

---

### 63. DDD Reference — Pattern Summaries (CC-BY)

| | |
|---|---|
| **Source** | Evans, E. (2015). *DDD Reference: Definitions and Pattern Summaries*. domainlanguage.com. https://www.domainlanguage.com/ddd/reference/ |
| **Date** | 2015 |
| **Alternative** | Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley. (full book; entry #31) |
| **Status** | Confirmed — freely available CC-BY canonical summary; maintained by Evans personally |
| **Core finding** | The open-access pattern summary of all DDD patterns from the 2003 book. More precisely citable than the book for specific pattern definitions. Key patterns: Ubiquitous Language ("Use the model as the backbone of a language. Commit the team to exercising that language relentlessly in all communication within the team and in the code."), Bounded Context, Context Map, Domain Events, Aggregates, Repositories. |
| **Mechanism** | Each pattern is described with: intent, prescription, and "therefore" consequences. The Ubiquitous Language pattern prescribes: use the same terms in diagrams, writing, and especially speech. Refactor the code when the language changes. Resolve confusion over terms in conversation, the way confusion over ordinary words is resolved — by agreement and precision. |
| **Where used** | Primary reference for `docs/domain-model.md` structure and the ubiquitous language practice. `update-docs` skill glossary entries derive from this: terms must match code identifiers (Evans' "use the same language in code" prescription). `docs/research/domain-modeling.md`. `define-scope/glossary.md.template` — the living glossary format and entry structure. |
| **Note** | Replaces entry #31 as the citable source for specific pattern quotes. Entry #31 remains as the book reference. Use this entry when citing a specific Evans pattern definition. |

---

### 64. UbiquitousLanguage — Fowler Bliki

| | |
|---|---|
| **Source** | Fowler, M. (2006). "UbiquitousLanguage." *martinfowler.com*. https://martinfowler.com/bliki/UbiquitousLanguage.html |
| **Date** | 2006 |
| **Alternative** | Evans (2015) DDD Reference (entry #63) — the primary source Fowler summarises |
| **Status** | Confirmed — widely cited secondary source; Fowler wrote the DDD foreword and is considered the authoritative secondary interpreter of Evans |
| **Core finding** | The ubiquitous language is a practice, not a document. The glossary is a secondary artifact — a snapshot of the current state of the language. The language itself lives in conversation, in the code, and in all written communication. "By using the model-based language pervasively and not being satisfied until it flows, we approach a model that is complete and comprehensible." Domain experts must object to inadequate terms; developers must flag ambiguity. |
| **Mechanism** | The key test of a ubiquitous language: can a domain expert read the domain layer code and recognise their domain? If the code uses different names than the glossary, the code must be refactored — not the glossary relaxed. The language evolves through experimentation with alternative expressions, followed by code refactoring to match the new model. |
| **Where used** | `update-docs` skill — grounds the rule "verify each term matches the identifier used in the code's domain layer." `docs/glossary.md` — the glossary is explicitly secondary to the code. `docs/research/domain-modeling.md`. |

---

### 65. BoundedContext — Fowler Bliki

| | |
|---|---|
| **Source** | Fowler, M. (2014). "BoundedContext." *martinfowler.com*. https://martinfowler.com/bliki/BoundedContext.html |
| **Date** | 2014 |
| **Alternative** | Evans (2015) DDD Reference (entry #63) — Fowler cites Evans directly |
| **Status** | Confirmed — includes a direct Evans quote; the canonical accessible reference for Bounded Context as a design pattern |
| **Core finding** | "Total unification of the domain model for a large system will not be feasible or cost-effective" (Evans, quoted directly). The same word can mean different things in different Bounded Contexts — this is not a defect but a reflection of domain reality. "You need a different model when the language changes." A Bounded Context is the boundary within which a particular ubiquitous language is internally consistent. Terms must be qualified by their context when a project has more than one bounded context. |
| **Mechanism** | Fowler's electricity utility example: the word "meter" meant different things in billing, grid management, and customer service. Attempting to unify these into one definition created confusion. Each bounded context maintains its own model and its own language. Context Maps document the relationships and translation rules between bounded contexts. |
| **Where used** | `update-docs` skill — `**Bounded context:**` field in `docs/glossary.md` entries is mandatory when the project has more than one bounded context (this is the Evans/Fowler requirement). `docs/research/domain-modeling.md`. |

---

### 66. Implementing Domain-Driven Design

| | |
|---|---|
| **Source** | Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley. |
| **Date** | 2013 |
| **Alternative** | Evans (2003) DDD (entry #31) — Vernon explicitly builds on Evans |
| **Status** | Confirmed — second most cited DDD book; ~5,000 citations |
| **Core finding** | Three additions to Evans: (1) **Domain Events as first-class vocabulary** — past-tense verb phrases ("OrderPlaced," "VersionDisplayed") are part of the ubiquitous language and belong in the glossary as a distinct type. (2) **Context Maps as the organising principle** for multi-context glossaries — each bounded context has its own language documentation; the Context Map shows translation rules between contexts. (3) **Documentation co-located with the code** — docs in the same repository decay at the same rate as the code, dramatically reducing divergence. |
| **Mechanism** | Vernon's IDDD samples (github.com/VaughnVernon/IDDD_Samples) demonstrate all three in practice. The Product Owner / Business Analyst plays the domain-expert-representative role in glossary maintenance — validating semantic correctness — while developers own structural precision. Neither writes the glossary unilaterally. |
| **Where used** | `update-docs` skill — `Domain Event` added as a distinct Type value in `docs/glossary.md` entries. Grounds the PO-owned glossary with SE input via `docs/adr/ADR-YYYY-MM-DD-<slug>.md` Reason: fields. `docs/research/domain-modeling.md`. |

---

### 67. Ubiquitous Language Is Not a Glossary — Verraes

| | |
|---|---|
| **Source** | Verraes, M. (2013). "Ubiquitous Language Is Not a Glossary." *verraes.net*. https://web.archive.org/web/20131004/https://verraes.net/2013/04/ubiquitous-language-is-not-a-glossary/ |
| **Date** | 2013 |
| **Alternative** | Fowler (2006) UbiquitousLanguage (entry #64) — the same secondary-artifact point, less pointed |
| **Status** | Confirmed — original URL is 404; widely documented through community discussion and practitioner secondary accounts; thesis is uncontested in the DDD community |
| **Core finding** | A glossary is not a ubiquitous language. Teams that maintain a glossary but do not reflect its terms in the code have the *appearance* of a ubiquitous language without the substance. The glossary is a secondary artifact derived from the code and domain-expert conversations — not the reverse. The canonical source of truth is the domain layer code, not the glossary document. A glossary that diverges from the code is lying. |
| **Mechanism** | The test: can a domain expert read the domain layer code and recognise their domain without a translator? If yes, the ubiquitous language exists. If the only evidence of the language is the glossary document, it does not exist. Consequence: every term added to the glossary must be verified against the corresponding code identifier. |
| **Where used** | `update-docs` skill — grounds the checklist item "Verify each term matches the identifier used in the code's domain layer." Prevents the common failure mode of glossary-as-theatre. `docs/research/domain-modeling.md`. |

---

### 68. Whirlpool Process of Model Exploration — Evans

| | |
|---|---|
| **Source** | Evans, E. (2011). *Whirlpool Process of Model Exploration*. domainlanguage.com. https://www.domainlanguage.com/ddd/whirlpool/ |
| **Date** | 2011 |
| **Alternative** | Brandolini, A. (2013). *Introducing EventStorming*. Leanpub. — a later, more structured alternative to Whirlpool |
| **Status** | Confirmed — freely available; Evans' own post-2003 process guidance |
| **Core finding** | Model exploration is a cycle: Scenario Exploring → Harvesting Abstractions → Probing the Model → Challenging the Model → back to Scenario Exploring. New vocabulary crystallizes at the Harvesting Abstractions step — concrete scenarios surface candidate terms, which are then named, defined, and reflected in the code. The glossary grows at each Harvesting Abstractions step. |
| **Mechanism** | The Whirlpool is not a development process — it fits within most iterative processes. It is a model-exploration subprocess triggered whenever the team encounters a poorly understood domain concept. The output of each cycle is a refined model expressed in clearer language, with updated code identifiers and glossary entries. |
| **Where used** | `update-docs` skill — grounds the timing of glossary updates: after each completed feature (Step 5) corresponds to the Harvesting Abstractions step in the Whirlpool. Discovery sessions (Stage 1) correspond to Scenario Exploring. `docs/research/domain-modeling.md`. |

---

### 69. ISO 704 — Terminology Work Principles and Methods

| | |
|---|---|
| **Source** | ISO. (2022). *ISO 704:2022 — Terminology work — Principles and methods*. International Organization for Standardization. https://www.iso.org/standard/79077.html |
| **Date** | 2022 (first edition 1987; current edition 2022) |
| **Alternative** | ISO 1087:2019 — Terminology work and terminology science: vocabulary (the companion vocabulary standard) |
| **Status** | Not directly verified — paywalled standard (~CHF 158). Content described here is drawn from the publicly available ISO preview, ISO TC 37 documentation, and widely cited secondary sources in terminology science literature. Core principles (genus + differentia, monosemy, consistency) are uncontested across secondary sources and have been stable since the 1987 first edition. |
| **Core finding** | A definition should identify the concept by stating (1) a **genus** — the broader category the concept belongs to — and (2) a **differentia** — the features that distinguish it from all other concepts in the same genus. This produces a one-sentence definition that is internally consistent, non-circular, and sufficient. Definitions should avoid negation ("what it is not") and synonymy ("same as X") as primary definition strategies. |
| **Mechanism** | Genus + differentia: "A [genus] that [differentia]." Example: "A Bounded Context is a [boundary within a domain model] that [enforces consistency of a single Ubiquitous Language]." The genus locates the term in a category the reader already knows; the differentia narrows it to this specific concept. |
| **Where used** | `define-scope/glossary.md.template` — the `**Definition:**` field format. The genus + differentia pattern is the prescribed sentence structure for all glossary entries. Not cited by name in the template — Evans DDD is the headline practice; ISO 704 is the definition *format* underlying it. `docs/research/domain-modeling.md`. |

---

## Bibliography

1. Context Mapper. (2025). Rapid Object-Oriented Analysis and Design. https://contextmapper.org/docs/rapid-ooad
2. Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley.
3. Evans, E. (2011). *Whirlpool Process of Model Exploration*. domainlanguage.com. https://www.domainlanguage.com/ddd/whirlpool/
4. Evans, E. (2015). *DDD Reference: Definitions and Pattern Summaries* (CC-BY). domainlanguage.com. https://www.domainlanguage.com/ddd/reference/
5. Fowler, M. (2006). UbiquitousLanguage. martinfowler.com. https://martinfowler.com/bliki/UbiquitousLanguage.html
6. Fowler, M. (2014). BoundedContext. martinfowler.com. https://martinfowler.com/bliki/BoundedContext.html
7. Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley.
8. Verraes, M. (2013). Ubiquitous Language Is Not a Glossary. verraes.net (archived). https://web.archive.org/web/20131004/https://verraes.net/2013/04/ubiquitous-language-is-not-a-glossary/
9. ISO. (2022). *ISO 704:2022 — Terminology work — Principles and methods*. International Organization for Standardization. https://www.iso.org/standard/79077.html
