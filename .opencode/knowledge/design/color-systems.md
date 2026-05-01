---
domain: design
tags: [color, palette, wcag, contrast, accessibility, hue-semantics, saturation, value, colour-harmony]
last-updated: 2026-04-30
---

# Color Systems for Project Branding

## Key Takeaways

- Design monochrome-first; add colour only after the shape holds identity in pure black on white (Rand, 1985; Kare, 1984).
- Use 1–2 colours maximum in a logo mark; three or more create reproduction problems and visual noise at small sizes.
- Hue is one axis; saturation (vivid vs muted) and value (light vs dark) are independent levers that carry as much meaning. A desaturated blue signals "corporate"; a saturated blue signals "tech/digital."
- Every text–background pair must meet WCAG 2.1 SC 1.4.3 minimum contrast: 4.5:1 for normal text, 3:1 for large text (W3C, 2018).
- Verify colours on actual backgrounds, not in isolation — simultaneous contrast shifts perceived hue (Itten, 1961; Albers, 1963).
- Define each brand colour with: hex value, RGB, dark-mode counterpart, and WCAG contrast ratio against primary backgrounds.
- Choose colour harmony type based on emotional effect: analogous for calm, complementary for vibrancy, split-complementary for balanced contrast, triadic for energy.

## Concepts

**Monochrome-First Process**: Design the entire mark in black on white, then white on black. If it does not work in monochrome, colour will not save it. Only after the shape holds identity in one colour should a second colour be introduced — and only as an accent, never carrying meaning that must be read.

**Hue, Saturation, and Value as Independent Axes**: Hue (which colour) is one dimension. Saturation (how vivid vs muted) and value (how light vs dark) carry as much meaning as hue and are independent levers. A single hue can express different personalities by varying saturation and value:
- High saturation + medium value: "digital, energetic, modern" (e.g., #3B82F6)
- Low saturation + medium value: "corporate, professional, subdued" (e.g., #6B7280)
- High saturation + dark value: "premium, deep, authoritative" (e.g., #1E3A5F)
- Low saturation + light value: "calm, approachable, subtle" (e.g., #DBEAFE)

Choose personality → hue → saturation/value, not hue first then wonder why it doesn't feel right.

**Hue Semantics**: Colours carry cultural associations. Blue signals trust and stability (most common in tech). Green signals growth and nature. Red signals energy and urgency. Orange signals creativity and enthusiasm. Purple signals innovation and premium quality. Yellow signals optimism and warmth. Choose a primary hue that reinforces the project's personality adjectives, not one that clashes with them.

**Saturation–Value Personality Map**: The same hue communicates different personalities depending on saturation and value:

| Personality | Hue | Saturation | Value | Example hex |
|-------------|-----|-----------|-------|------------|
| Precise, technical | Blue | Medium | Dark | #1E3A5F |
| Trustworthy, stable | Blue | Medium | Medium | #3B82F6 |
| Bold, disruptive | Red | High | Medium | #DC2626 |
| Warm, creative | Orange | High | Medium | #F97316 |
| Calm, approachable | Green | Low–Medium | Light–Medium | #86EFAC |
| Premium, innovative | Purple | Medium | Dark | #7C3AED |

**Colour Harmony Types**: Choose the harmony type based on the emotional effect you want:

| Harmony type | Wheel relationship | Angle | Effect | Use when |
|-------------|-------------------|-------|--------|----------|
| Complementary | Opposite on wheel | 180° | Maximum contrast, vibrant tension | Accent needs to pop against primary |
| Split-complementary | Complement ± 30° | 150° + 30° | Balanced contrast, less harsh than direct complement | Most versatile for branding |
| Analogous | Adjacent on wheel | ± 30° | Calm, harmonious, unified | Personality is "calm, cohesive, subtle" |
| Triadic | Evenly spaced 3 | 120° | Energetic, diverse, playful | Need 3 distinct brand colours |
| Tetradic (square) | Evenly spaced 4 | 90° | Complex, rich, hard to balance | Only with experienced colour sense |

For 2-colour brand marks, use complementary or split-complementary. Analogous palettes lack enough contrast for accent visibility. Triadic requires 3 colours, violating the 2-colour maximum rule.

**Itten's Seven Contrast Types**: Each contrast type is a design tool that produces a different emotional effect (Itten, 1961). The three most useful for branding:

1. **Light-Dark contrast**: Black on white. Maximum clarity. Foundation of WCAG accessibility. Use for text–background pairs where legibility is paramount.
2. **Complementary contrast**: Opposite hues placed together (red–green, blue–orange). Maximum visual tension and vibrancy. Risk: at similar saturation, complements vibrate uncomfortably. Mitigation: vary the value (one lighter/darker) or desaturate one.
3. **Saturation contrast**: A vivid colour next to a muted one. The vivid colour appears to glow. This is the primary tool for accent hierarchy — a saturated accent on a desaturated primary draws the eye precisely without requiring hue contrast.

The other four (cold-warm, simultaneous, hue, extension) are documented in the research (see `docs/research/design/visual/itten_1961.md`) and are useful for advanced palette refinement.

**Complementary Palette Construction**: A brand palette has 5 roles: (1) primary — the dominant colour; (2) accent — a contrasting highlight; (3) background — the surface colour; (4) text-primary — the main text colour; (5) text-secondary — muted text. Primary and accent are typically complementary or split-complementary. Background and text colours must achieve ≥4.5:1 contrast (WCAG AA).

**WCAG Contrast Calculation**: Relative luminance L = 0.2126R + 0.7152G + 0.0722B (after gamma linearisation). Contrast ratio = (L_lighter + 0.05) / (L_darker + 0.05). Ratio ranges from 1:1 to 21:1. Normal text requires ≥4.5:1 (AA) or ≥7:1 (AAA). Large text (≥18pt or ≥14pt bold) requires ≥3:1 (AA) or ≥4.5:1 (AAA).

**Dark-Mode Counterparts**: For each light-theme colour, define a dark-theme counterpart that maintains the same relative visual weight and contrast ratio. Do not simply invert (white-on-black is harsh). Use off-white (#e0e0e0) on dark backgrounds instead of pure white, and adjust accent saturation for dark contexts.

**Simultaneous Contrast**: A neutral grey on a red background appears greenish; on a green background it appears reddish (Itten, 1961). Always test brand colours against both light and dark backgrounds before finalising. Adjust hex values to compensate for the perceptual shift, not the theoretical value.

## Content

### Hue Semantics Table

| Hue | Signal | Common In | Avoid If |
|-----|--------|-----------|----------|
| Blue | Trust, stability, professionalism | Tech, finance, enterprise | Project personality is "bold, disruptive" |
| Green | Growth, nature, health | Environment, fintech, health | Project personality is "precise, minimal" |
| Red | Energy, urgency, danger | News, entertainment, alerts | Project personality is "calm, reliable" |
| Orange | Creativity, enthusiasm, warmth | Creative tools, education | Project personality is "serious, formal" |
| Purple | Innovation, premium, luxury | Design tools, premium SaaS | Project personality is "accessible, simple" |
| Yellow | Optimism, warmth, caution | Children's products, warnings | Used as small accent only (low contrast on white) |
| Teal | Balance, sophistication | Health tech, lifestyle | Combined with similar-value greens |
| Grey | Neutrality, professionalism | Enterprise, documentation | Used as primary (no personality signal) |

### Complementary Pair Examples

| Primary | Accent | Relationship | Contrast on White |
|---------|--------|-------------|-------------------|
| #1a1a2e (dark navy) | #e94560 (warm red) | Split-complementary | Navy 15.7:1, Red 4.7:1 |
| #2d5016 (forest green) | #c9a84c (antique gold) | Split-complementary | Green 7.2:1, Gold 3.1:1 (large text only) |
| #0f3460 (mid blue) | #e94560 (warm red) | Triadic | Blue 11.4:1, Red 4.7:1 |
| #3b2410 (deep brown) | #7baabf (steel blue) | Complementary | Brown 14.2:1, Blue 3.7:1 |

### Visual Weight Proportions (Itten's Contrast of Extension)

When balancing colour areas in a composition, visual weight depends on inherent brightness:

| Colour pair | Visual weight ratio (area for equal perceived weight) |
|------------|------------------------------------------------------|
| Yellow : Violet | 1 : 3 |
| Orange : Blue | 1 : 2 |
| Red : Green | 1 : 1 |
| Yellow : Orange | 1 : 1.5 |
| Light grey : Dark navy | 1 : 2 |

A thin gold line on a navy field reads as "balanced" because the yellow's visual weight per unit area is 3× the violet's.

### WCAG Contrast Verification Checklist

For each colour in the palette, verify contrast ratio against:

1. **Primary on background** — must be ≥4.5:1 for normal text
2. **Accent on background** — must be ≥3:1 for large text or ≥4.5:1 if carrying meaning
3. **Secondary on background** — must be ≥3:1 minimum
4. **Dark-mode primary on dark background** — must be ≥4.5:1
5. **Dark-mode accent on dark background** — must be ≥3:1
6. **Logo mark on white** — must be clearly legible (no numeric threshold, but test by squinting)
7. **Logo mark on dark** — must be clearly legible in dark mode variant

## Related

- [[design/project-assets]]
- [[design/identity-design]]
- [[design/visual-harmony]]