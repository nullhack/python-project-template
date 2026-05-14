---
name: define-ubiquitous-language
description: "Extract domain terms from the behavioral spec, domain model, and interview notes, define them in genus-differentia format, and cross-reference"
---

# Define Ubiquitous Language

Available knowledge: [[requirements/ubiquitous-language]]. `in` artifacts: read all before starting work.

1. Read `domain_model.md`, `behavioral_spec.md`, and all interview notes. If `glossary.md` already exists, read it for cumulative editing.
2. Extract terms per [[requirements/ubiquitous-language#content]]: scan entity names, External Contract fields, data shape attributes, and interview nouns/verbs for domain-specific terms carrying business meaning.
3. Filter out technical and generic terms per [[requirements/ubiquitous-language#content]] exclusion rules.
4. For each term, write a genus-differentia definition per [[requirements/ubiquitous-language#key-takeaways]]. Document aliases where multiple words refer to the same concept.
5. If existing glossary entries conflict with new understanding, retire the old entry per [[requirements/ubiquitous-language#key-takeaways]] rather than deleting.
6. Cross-reference per [[requirements/ubiquitous-language#content]]: verify glossary → behavioral spec, behavioral spec → glossary, glossary → feature files. Flag any gaps.
7. If a term has different meanings across bounded contexts, document each meaning separately within its context and note the context boundary.
8. Write all definitions into `glossary.md`. If the file already exists, edit cumulatively — preserve valid entries, update based on new information.
