---
domain: design
tags: [logo, banner, favicon, svg, dark-mode, assets, delivery, progressive-simplification]
last-updated: 2026-04-30
---

# Project Asset Design

## Key Takeaways

- Design favicon-first: if the mark cannot hold identity at 16×16, it is not strong enough (Kare, 1984).
- Design monochrome-first: if it does not work in pure black on white, colour will not save it (Rand, 1985).
- Progressive simplification: each size tier gets its own optimised version, not a scaled-down copy (Hicks, 2011).
- Pass the 5-second test, blur test, monochrome test, scalability test, and proximity test before finalising (Airey, 2010).
- SVG assets must use presentation attributes (not CSS classes), be self-contained (no external references), and be optimised with SVGO.
- Provide dark-mode variants: embedded `@media (prefers-color-scheme: dark)` in SVGs, or separate files.
- Minimum favicon delivery set: favicon.ico, icon.svg, apple-touch-icon.png, icon-192.png, icon-512.png.
- Social preview image: 1280×640px minimum, critical content centred in 60–70% of frame.

## Concepts

**Favicon-First Design**: Design at the smallest target size (16×16 or 32×32) first, then scale up and add detail. Kare designed all original Macintosh icons on a 32×32 grid because "every pixel must carry meaning." If a mark cannot be recognised at favicon size, it relies on detail that will vanish in real usage. The favicon version is not a simplification of a larger design — it is the core identity, and the larger versions are elaborations of it.

**Monochrome-First Process**: The mark must work in a single colour on a single background before any colour is applied. Rand tested his logos by blurring them (Gaussian blur 3–5px) to verify the silhouette held. If the blurred mark is still identifiable, the shape is strong. If not, it relies on detail that will fail at small sizes, in print, or on dark backgrounds.

**Progressive Simplification**: Each size tier gets its own optimised version: Master (512px, full detail), Standard (180px, remove thin strokes, simplify curves), Small (32px, only core silhouette, strokes→fills), Tiny (16px, single bold shape, often hand-redrawn). Do not simply scale a 512px icon to 16px — it produces a muddy, unrecognisable mark.

**Evaluation Checklist**: (1) 5-second test — show for 5 seconds, remove, ask "what did you see?"; (2) blur test — Gaussian blur 3–5px, silhouette must remain identifiable; (3) monochrome test — pure black on white, pure white on black; (4) scalability test — legible at 16px and 500px; (5) proximity test — distinguishable from 5 competitor logos; (6) "one thing" test — there should be one dominant feature.

**SVG Construction Rules**: Use presentation attributes (`fill="#1a1a2e"`) not CSS classes (GitHub strips inline `<style>`). All content must be self-contained — no `<use href="external">`, no external fonts, no `<style>` blocks in production SVGs. Use a square `viewBox` (e.g., `0 0 512 512`) with 5–10% padding. Convert all strokes to filled paths for the production file. Optimise with SVGO (`removeMetadata`, `convertShapeToPath`, `mergePaths`, `cleanupNumericValues` at precision 1–2).

**Dark-Mode Strategy**: Modern approach: embed `@media (prefers-color-scheme: dark)` in SVG favicon with human-readable CSS classes for dark-mode targeting. Fallback: maintain separate `logo-dark.svg` and `logo-light.svg` files for non-web contexts. Dark mode is not simply inverted — use off-white (#e0e0e0) instead of pure white, and increase stroke weight by 0.5–1px.

**Favicon Delivery Set**: favicon.ico (32×32 containing 16×16 + 32×32), icon.svg (with dark-mode media query), apple-touch-icon.png (180×180), icon-192.png (Android), icon-512.png (PWA). Plus `manifest.webmanifest` referencing icon sizes. HTML: `<link rel="icon" href="/favicon.ico" sizes="32x32">`, `<link rel="icon" href="/icon.svg" type="image/svg+xml">`, `<link rel="apple-touch-icon" href="/apple-touch-icon.png">`.

**Social Preview**: GitHub social preview is 1280×640px (2:1 ratio, PNG or JPG, under 1MB). Centre critical content in 60–70% of the frame to survive different platform crops. Show the logo mark and project name in large type. Avoid screenshots or code in the preview.

**GitHub Camo**: GitHub proxies external images through Camo, which has a 5MB size limit, strips active content, and caches aggressively. Images committed directly to the repo are not proxied and update immediately on push. Always reference assets with relative paths in READMEs to avoid Camo.

## Content

### Logo Design Process

1. **Brief**: Written brief with project name, tagline, 3 personality adjectives, forbidden elements, 5 reference logos
2. **Sketch**: 20–40 rough concepts, black pen on white paper, monochrome only
3. **Select**: Pick top 3–5, refine in vector, still monochrome
4. **Colour**: Add 1 colour, then 2 maximum. Test on white, black, and mid-gray backgrounds
5. **Stress-test**: Apply evaluation checklist (5-second, blur, monochrome, scalability, proximity, "one thing")
6. **Deliver**: Export all sizes and formats per delivery checklist

### Banner Design Process

1. **Layout**: 1280×640px canvas (2:1 for social preview), centred content zone
2. **Elements**: Logo mark (left or centre), project name in large type, tagline optional
3. **Colours**: Use brand primary and background only. Accent sparingly for rules/dividers
4. **Dark variant**: Same layout, inverted palette, tested on dark backgrounds
5. **Export**: SVG for README, PNG at 1280×640 for GitHub social preview

### File Delivery Checklist

- [ ] `logo.svg` — Master SVG, square viewBox, clean paths, human-readable IDs
- [ ] `logo-dark.svg` — Dark-mode variant (or embedded media query in logo.svg)
- [ ] `logo-icon.svg` — Symbol only (no wordmark), with dark-mode support
- [ ] `favicon.ico` — 32×32 ICO (with 16×16 embedded)
- [ ] `icon.svg` — Favicon SVG with `prefers-color-scheme` media query
- [ ] `apple-touch-icon.png` — 180×180 PNG
- [ ] `icon-192.png` — 192×192 PNG for Android
- [ ] `icon-512.png` — 512×512 PNG for PWA
- [ ] `banner.svg` — README banner, SVG, tested on light and dark backgrounds
- [ ] Social preview PNG — 1280×640, critical content in centre 60–70%

## Related

- [[design/color-systems]]
- [[design/identity-design]]
- [[design/visual-harmony]]