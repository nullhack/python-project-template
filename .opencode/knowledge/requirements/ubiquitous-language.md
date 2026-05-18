---
domain: requirements
tags: [ubiquitous-language, glossary, ddd, genus-differentia]
last-updated: 2026-05-08
---

# Ubiquitous Language

## Key Takeaways

- Ubiquitous language is a shared vocabulary where every term has exactly one meaning within a bounded context (Evans, 2003). The same word must mean the same thing to everyone.
- Definitions use genus-differentia format: state the category, then the distinguishing characteristic. Example: "A Fill is an execution event that records price, quantity, and fee of a completed order match."
- Extract terms by scanning domain events, commands, entity names, and interview transcripts for domain-specific nouns and verbs carrying business meaning.
- The glossary is append-only: never delete entries; mark retired with a reference to the replacement. Aliases (different words for the same concept) must be documented.
- Cross-reference every term against the domain spec and feature files. A term serving double duty across contexts indicates a missing context boundary.

## Concepts

**Ubiquitous Language**. A shared vocabulary between domain experts and developers where every term has exactly one meaning within a bounded context (Evans, 2003). When a term changes meaning across contexts, that boundary must be explicit in the domain spec's context map.

**Genus-Differentia Format**. Every definition follows: "[Term] is a [genus/category] that [differentia/distinguishing characteristic]." The genus places it in a known category; the differentia distinguishes it from other category members.

**Term Extraction**. Terms come from three sources: domain events and commands (OrderPlaced → "Order", "Fill"), entity and value object names from the domain spec, and interview transcripts (domain-specific nouns stakeholders emphasize or repeat). Technical terms (API, database) are excluded unless they carry domain meaning.

**Append-Only Glossary**. When understanding shifts, the old entry is marked retired (not deleted) and a new entry is written. This preserves domain understanding history and prevents confusion with superseded terms.

**Cross-Referencing**. Verify each glossary term against domain spec and feature files. A term in glossary but not domain spec is either a missing entity, a concept that should be added, or stale. A term in domain spec but not glossary is an incomplete glossary. Cross-context ambiguity flags context boundaries.

## Content

### Term Detection Heuristics

Scan these sources for terms needing definition:

1. **Event names**: Each contains 1-2 domain nouns (FillDetected → "Fill", "Fill Detection")
2. **Command names**: Domain verbs and nouns (PlaceOrder → "Order", "Order Placement")
3. **Entity names**: Every entity and value object is a term
4. **Interview nouns**: Domain-specific nouns stakeholders repeat, emphasize, or define
5. **Interview verbs**: Domain-specific verbs describing business actions (not "store", "compute")
6. **Qualifying adjectives**: "available" balance, "locked" balance, "orphaned" order — the adjective changes meaning

Exclude: programming terms (class, method, dict), infrastructure terms (API, HTTP, JSON), generic terms (value, process) unless domain-specific.

### Definition Format

| Field | Purpose |
|---|---|
| Term | The word or phrase being defined |
| Definition | Genus-differentia format |
| Aliases | Other words meaning the same thing |
| Example | Concrete usage in context |
| Source | Where the term originated |

### Retirement Process

1. Add `Status: Retired` to the existing entry
2. Add `Superseded by: <new-term>` with a reference
3. Write a new entry for the replacement term
4. Never delete — retired entries remain for historical reference

### Cross-Reference Verification

1. **Glossary → Domain Model**: For each term, find it in entities, relationships, or context descriptions. If missing, flag it.
2. **Domain Model → Glossary**: For each entity name and relationship noun, find it in the glossary. If missing, add it.
3. **Glossary → Feature Files**: For each Phase 1 term, find it in at least one feature file. If missing, flag as potentially out of scope.
4. **Ambiguity detection**: If a term has different meanings in different contexts, document each meaning separately within its context and note the boundary.

### Cross-Context Terms

When the same word has different meanings in different bounded contexts:
- Document each meaning separately with its context
- Note the context boundary in the glossary entry
- Verify the domain spec's context map reflects this boundary

## Related

- [[domain-modeling/event-storming]]
- [[domain-modeling/event-storming]]
- [[requirements/interview-techniques]]
