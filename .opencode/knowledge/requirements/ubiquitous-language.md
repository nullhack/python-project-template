---
domain: requirements
tags: [ubiquitous-language, glossary, ddd, genus-differentia]
last-updated: 2026-04-29
---

# Ubiquitous Language

## Key Takeaways

- Ubiquitous language is a shared vocabulary between domain experts and developers — the same word must mean the same thing to everyone (Evans, 2003).
- Definitions use genus-differentia format: state the category the term belongs to, then state how it differs from other members of that category.
- The glossary is append-only — never delete entries; mark them as retired with a reference to the replacement term.
- Aliases (different words for the same concept) must be documented so teams know when terms are interchangeable.

## Concepts

**Ubiquitous Language** — A shared vocabulary between domain experts and developers where every term has exactly one meaning within a bounded context (Evans, 2003). The same word must mean the same thing to everyone. When a term changes meaning across contexts, that boundary must be made explicit.

**Genus-Differentia Format** — Every definition follows the pattern: "[Term] is a [genus/category] that [differentia/distinguishing characteristic]." For example: "A Repository is a collection-like interface that abstracts persistence behind a domain-oriented lookup." The genus (collection-like interface) places it in a known category; the differentia (abstracts persistence behind domain-oriented lookup) distinguishes it from other interfaces.

**Append-Only Glossary** — The glossary records every term the team uses. When understanding shifts and a term's definition changes, the old entry is marked retired (not deleted) and a new entry is written. This preserves the history of domain understanding and prevents confusion when old documents reference superseded terms.

**Aliases** — When two words refer to the same concept (e.g., "Order" and "Purchase" in an e-commerce domain), both are documented with one marked as the primary term and the other as an alias. This prevents parallel vocabularies from forming.

## Content

### Definition Format

Each glossary entry contains:

| Field | Purpose |
|---|---|
| Term | The word or phrase being defined |
| Definition | Genus-differentia format |
| Aliases | Other words that mean the same thing |
| Example | A concrete usage in context |
| Source | Where the term originated (interview, document, etc.) |

### Retirement Process

When a term is superseded:

1. Add `Status: Retired` to the existing entry
2. Add `Superseded by: <new-term>` with a reference
3. Write a new entry for the replacement term
4. Never delete — retired entries remain for historical reference

### Cross-Referencing

After writing or updating definitions:

- Verify each term matches how it's used in the domain model
- Verify each term matches how it's used in feature files
- Flag any term serving double duty across bounded contexts — this indicates a missing context boundary (Evans, 2003)

## Related

- [[domain-modeling/event-storming]]
- [[requirements/interview-techniques]]
- [[requirements/decomposition]]