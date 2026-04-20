# Branding

All fields are optional. Blank or absent fields fall back to defaults (adjective-animal release names, Mermaid default colors, no wording constraints). Agents read this file before generating release names, C4 diagrams, README banners, or any document with visual or copy identity.

---

## Identity

- **Project name:** Python Project Template
- **Tagline:** Production-ready Python, from zero to workflow in minutes.
- **Mission:** Eliminate boilerplate so engineers ship features, not setup.
- **Vision:** The standard starting point for any serious Python project.
- **Tone of voice:** Direct, precise, minimal. No fluff.

## Visual

- **Background/parchment:** `#faf7f2` → `#ede8e0`  — warm off-white marble (primary surface)
- **Primary text:** `#5c3d1e` → `#3b2410`           — deep warm brown (body text, headings)
- **Accent/gold:** `#c9a84c` → `#e8c96a`            — antique gold (borders, highlights, lines)
- **Secondary/blue:** `#7baabf` → `#4a7a96`         — muted steel blue (labels, secondary text)
- **Stone/marble:** `#f0ece4` → `#c8c0b8`           — structural marble tone (temple columns, shapes)
- **Logo:** `docs/assets/logo.svg`
- **Banner:** `docs/assets/banner.svg`

> Color system derived from the SVG assets (classical Greek temple aesthetic — marble, parchment, antique gold). Deep brown `#3b2410` on parchment `#faf7f2` achieves > 10:1 contrast (WCAG AAA). Gold accent used for decorative lines and borders only, not body text.

## Release Naming

- **Convention:** `adjective-greek-figure`
- **Theme:** Greek antiquity — philosophers, heroes, gods, mythological figures (e.g. "Nimble Socrates", "Resolute Athena", "Precise Pythagoras")
- **Excluded words:** *(none)*

## Wording

- **Avoid:** `easy`, `simple`, `just`, `quick` — these undermine engineer credibility
- **Prefer:** `minimal`, `precise`, `production-ready`, `zero-boilerplate`

## Project Summary

A Python project template with a production-ready AI-assisted delivery workflow.
Ships with quality tooling (ruff, pyright, pytest, hypothesis), Gherkin-driven
acceptance criteria, and four specialized AI agents covering scope through release.
Use this summary in banners, release notes, and document headers.
