---
name: design-colors
description: Select and validate a project color palette with WCAG contrast compliance
version: "1.0"
author: designer
audience: designer
workflow: branding
---

# Design Colors

Select a color palette for the project and validate it for accessibility. Write the result to `docs/branding.md`.

## When to Use

- Stakeholder provides a theme word or asks for a color palette
- `docs/branding.md` exists but has no colors yet
- Stakeholder requests a color change

## Step-by-Step

### 1. Read branding context

Read `docs/branding.md`. If colors are already set and the stakeholder has not asked to change them, stop — do not overwrite.

### 2. Select primary hue

Map the project theme or mission to a hue. Hue carries meaning before any other element is read (Itten 1961 — hue semantics precede form perception):

| Theme / Mission | Hue | Semantic |
|---|---|---|
| Technology, trust, precision | Blue | Calm, reliable |
| Growth, nature, sustainability | Green | Life, progress |
| Creativity, energy, community | Orange | Warmth, action |
| Innovation, premium, research | Purple | Depth, curiosity |
| Urgency, passion, power | Red | Use sparingly |
| Clarity, neutrality | Grey | Professional, recedes |

### 3. Build the palette

Use a complementary scheme by default — a muted primary plus a pure complementary accent. This produces the most reliably professional result without requiring design expertise (Albers 1963 — simultaneous contrast; complementary pairs read as distinct without competing):

- **Primary** — muted/deep tone of chosen hue (lower saturation, lower value). Used for surfaces, backgrounds, headers.
- **Accent** — complementary hue (180° on color wheel), pure/saturated. Used for links, highlights, diagram lines only.

Example for green: Primary `#2D6A4F` (deep forest), Accent `#D4A017` (golden amber).

Use analogous, split-complementary, or triadic only when the stakeholder explicitly requests it.

### 4. Validate WCAG 2.1 AA

Any color used as a text background must achieve ≥ 4.5:1 contrast with white `#FFFFFF` (WCAG 2.1 SC 1.4.3 — derived from ISO 9241-3 baseline × 1.5 acuity loss factor):

```
sRGB → linear: c ≤ 0.04045 ? c/12.92 : ((c+0.055)/1.055)^2.4
L = 0.2126·R + 0.7152·G + 0.0722·B
Contrast = (L_lighter + 0.05) / (L_darker + 0.05)
```

If contrast < 4.5:1, darken the primary until compliant. Accent colors on non-text surfaces are exempt.

### 5. Write to branding

Update `docs/branding.md` under `## Visual`:

```markdown
- **Primary color:** `#XXXXXX`  — <hue> (<semantic rationale>)
- **Accent color:** `#XXXXXX`   — <hue> (<semantic rationale>)

> Colors meet WCAG 2.1 AA (X.X:1 contrast) when white text is placed on the primary.
```

## Checklist

- [ ] Existing colors checked before proceeding
- [ ] Hue chosen from theme/mission semantics
- [ ] Primary is muted/deep (not pure saturated)
- [ ] Accent is complementary or stakeholder-specified
- [ ] White-on-primary contrast ≥ 4.5:1 calculated and reported
- [ ] `docs/branding.md` updated with hex codes, rationale, and contrast note
