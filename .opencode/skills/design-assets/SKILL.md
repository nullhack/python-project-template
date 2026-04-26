---
name: design-assets
description: Author and update SVG visual assets using project branding identity
version: "1.0"
author: designer
audience: designer
workflow: branding
---

# Design Assets

Create or update `docs/assets/logo.svg` and `docs/assets/banner.svg` from the project's branding identity in `docs/branding.md`.

## When to Use

- Stakeholder requests a new or updated logo or banner
- `docs/assets/` is empty after project setup

## Step-by-Step

### 1. Read branding

Read `docs/branding.md`. Extract: project name, tagline, primary/accent colors, tone of voice. If colors are absent, run `skill design-colors` first.

### 2. Apply SVG structure rules

See [[branding/svg-rules]] for the full SVG structure constraints including viewBox, CSS custom properties, font stack, accessibility attributes, and minimum display sizes.

### 3. Banner layout

See [[branding/svg-rules]] for banner layout specifications including viewBox dimensions and the three-zone layout (left accent, center text, right optional graphic).

### 4. Logo layout

See [[branding/svg-rules]] for logo layout specifications including viewBox dimensions, shape readability at small sizes, and text-in-mark rules.

### 5. Write the SVG

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" role="img" aria-label="<project-name> banner">
  <style>
    :root { --color-primary: #XXXXXX; --color-accent: #XXXXXX; }
    .bg    { fill: var(--color-primary); }
    .title { fill: #ffffff; font-family: system-ui, -apple-system, sans-serif; font-size: 56px; font-weight: 700; }
    .sub   { fill: var(--color-accent); font-family: system-ui, -apple-system, sans-serif; font-size: 22px; }
  </style>
  <rect class="bg" width="1200" height="300"/>
  <!-- content -->
</svg>
```

### 6. Commit

```bash
git add docs/assets/
git commit -m "design(assets): <create|update> <banner|logo>"
```

## Checklist

- [ ] `docs/branding.md` read before writing any SVG
- [ ] Colors sourced from `docs/branding.md`; `skill design-colors` run if absent
- [ ] `viewBox` set; no fixed `width`/`height` on `<svg>` root
- [ ] Colors use CSS custom properties with fallback hex
- [ ] System font stack; no external imports
- [ ] `role="img"` and `aria-label` present
- [ ] Banner readable at 400px wide; logo readable at 32px
- [ ] Files committed to `docs/assets/`