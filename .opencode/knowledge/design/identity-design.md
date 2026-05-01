---
domain: design
tags: [brand, identity, naming, interview, personality, logo-type]
last-updated: 2026-04-30
---

# Identity Design

## Key Takeaways

- Brand identity has five components: name, tagline, personality (3 adjectives), visual mark, and wording rules. All are captured in `docs/branding.md`.
- Choose logo type based on project recognition and visual metaphor: combination mark for new brands, abstract mark for established names, pictogram for strong metaphors, letterform for compact marks.
- Release naming convention lives in `docs/branding.md` under the Release Naming section — it is part of the brand identity, not separate from it.
- Wording rules (words to avoid, words to prefer) are brand identity constraints, not style preferences — they prevent the brand voice from drifting.
- The interview for brand identity uses [[requirements/interview-techniques#key-takeaways]] but focuses on personality, visual metaphor, and wording rather than requirements.

## Concepts

**Brand Identity Components**: A project's brand identity is the combination of (1) name — the project identifier; (2) tagline — one sentence describing what the project does; (3) personality — 3 adjectives that define tone and visual style; (4) visual mark — logo, banner, colour palette; (5) wording rules — words to avoid and prefer. These are captured in `docs/branding.md` per the template at `.templates/docs/branding/branding.md.template`.

**Logo Type Selection**: Four logo types are appropriate for open-source projects. (1) Combination mark (symbol + wordmark) — best for new brands where the name is not yet widely known. (2) Abstract mark — best for established names that need a unique symbol. (3) Pictogram — best when the project name suggests a strong visual metaphor (e.g., Docker = whale). (4) Letterform/monogram — best for projects with long names needing a compact avatar mark. Choose based on: is the name well-known? (no → combination mark). Does the name suggest a metaphor? (yes → pictogram). Is the primary context small? (yes → letterform).

**Personality Adjectives**: Three adjectives define the brand personality. They drive every design and writing decision: colour choices (warm vs cool, saturated vs muted), logo style (geometric vs organic, bold vs delicate), and wording (direct vs friendly, technical vs approachable). Examples: "precise, calm, reliable" → cool blues, geometric shapes, direct wording. "Bold, fast, disruptive" → warm reds, angular shapes, punchy wording.

**Release Naming Convention**: Stored in `docs/branding.md` under the Release Naming section. Convention format (e.g., `adjective-greek-figure`), theme (e.g., Greek antiquity), rationale, and excluded words. This is part of brand identity because release names are public-facing communications that reinforce (or contradict) the project's personality. See [[software-craft/versioning#key-takeaways]] for the versioning scheme.

**Wording Rules**: Two lists: words to avoid and words to prefer. These prevent brand voice drift across releases, documentation, and README. Example: avoid "easy, simple, just" (these are subjective and often false); prefer "minimal, precise, production-ready" (these are verifiable). Wording rules are identity constraints, not stylistic preferences — they define what the project sounds like.

**Brand Interview Structure**: The interview for brand identity is structured in three phases: (1) personality — what 3 adjectives describe the project? what must it NOT convey? where will the logo appear most? (2) visual metaphor — does the project name suggest a visual? what are 5 peer/competitor logos? how should yours differ? (3) wording — what words should the project avoid? what words should it prefer? what is the tagline? See [[requirements/interview-techniques#concepts]] for interview techniques (CIT for specific examples, Laddering for climbing from surface preferences to real constraints).

## Related

- [[design/color-systems]]
- [[design/project-assets]]
- [[design/visual-harmony]]
- [[requirements/interview-techniques]]