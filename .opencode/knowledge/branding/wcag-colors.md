---
domain: branding
tags: [wcag, accessibility, colors, contrast, design]
last-updated: 2026-04-26
---

# WCAG Color Compliance

## Key Takeaways

- Map project theme to a hue using the hue semantics table; use a complementary scheme (muted primary + pure accent) by default.
- Any color used as a text background must achieve at least 4.5:1 contrast with white `#FFFFFF` (WCAG 2.1 AA); darken the primary until compliant if needed.
- Convert sRGB to linear luminance using the standard formula, then calculate contrast ratio as `(L_lighter + 0.05) / (L_darker + 0.05)`.
- Accent colors on non-text surfaces are exempt from contrast requirements.

## Concepts

**Hue Semantics**: Hue carries meaning before any other element is read. Blue conveys technology, trust, precision. Green conveys growth, nature, sustainability. Orange conveys creativity, energy, community. Purple conveys innovation, premium, research. Red conveys urgency, passion, power (use sparingly). Grey conveys clarity, neutrality.

**Complementary Color Scheme**: The default scheme uses a muted primary (lower saturation, lower value) for surfaces, backgrounds, and headers, plus a pure complementary accent for links, highlights, and diagram lines. Use analogous, split-complementary, or triadic only when the stakeholder explicitly requests it.

**WCAG 2.1 AA Contrast Calculation**: Convert each sRGB channel to linear, calculate relative luminance as `0.2126*R + 0.7152*G + 0.0722*B`, then compute contrast ratio as `(L_lighter + 0.05) / (L_darker + 0.05)`. The minimum for normal text on a background is 4.5:1.

**Accent Color Exemption**: Accent colors on non-text surfaces (diagram lines, badges, icons) are exempt from contrast requirements.

## Content

### Hue Semantics

Hue carries meaning before any other element is read (Itten 1961 — hue semantics precede form perception):

| Theme / Mission | Hue | Semantic |
|---|---|---|
| Technology, trust, precision | Blue | Calm, reliable |
| Growth, nature, sustainability | Green | Life, progress |
| Creativity, energy, community | Orange | Warmth, action |
| Innovation, premium, research | Purple | Depth, curiosity |
| Urgency, passion, power | Red | Use sparingly |
| Clarity, neutrality | Grey | Professional, recedes |

### Complementary Color Scheme

Default scheme: a muted primary plus a pure complementary accent. Complementary pairs (180 degrees on the color wheel) read as distinct without competing (Albers 1963 — simultaneous contrast).

- **Primary** — muted/deep tone of chosen hue (lower saturation, lower value). Used for surfaces, backgrounds, headers.
- **Accent** — complementary hue, pure/saturated. Used for links, highlights, diagram lines only.

Example for green: Primary `#2D6A4F` (deep forest), Accent `#D4A017` (golden amber).

Use analogous, split-complementary, or triadic only when the stakeholder explicitly requests it.

### WCAG 2.1 AA Contrast Formula

Any color used as a text background must achieve at least 4.5:1 contrast with white `#FFFFFF` (WCAG 2.1 SC 1.4.3 — derived from ISO 9241-3 baseline multiplied by 1.5 acuity loss factor).

Step 1 — Convert sRGB channel to linear:

```
c_linear = c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ^ 2.4
```

Where `c` is the sRGB channel value divided by 255 (range 0.0 to 1.0).

Step 2 — Calculate relative luminance:

```
L = 0.2126 * R_linear + 0.7152 * G_linear + 0.0722 * B_linear
```

Step 3 — Calculate contrast ratio:

```
Contrast = (L_lighter + 0.05) / (L_darker + 0.05)
```

### Minimum Contrast Ratio

- **4.5:1** for normal text on background (AA level)
- If contrast is below 4.5:1, darken the primary until compliant
- Accent colors on non-text surfaces are exempt from contrast requirements

## Related

- [[branding/svg-rules]] — SVG structure rules for visual assets using project colors