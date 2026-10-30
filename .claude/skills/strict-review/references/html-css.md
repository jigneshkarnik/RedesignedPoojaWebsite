# HTML and CSS

## HTML
- [ ] `<!doctype html>`, `<html lang="en">` or `lang="nl"` matching the folder (`js/site.js` reads it to choose email text).
- [ ] One `<h1>` per page; headings do not skip levels.
- [ ] `<title>` unique per page, under about 60 characters; meta description unique, under about 160, plain-spoken, no remedy names or cure claims.
- [ ] Landmarks present: `<header>`, `<nav>` with label, `<main id>`, `<footer>`. Skip link points to a real id.
- [ ] Every `<img>` has `alt` (empty only for decorative), explicit `width`/`height`, and `loading="lazy"` below the fold.
- [ ] No duplicate `id`s; every `for=`, `aria-labelledby`, `aria-controls`, and `href="#…"` points to an existing id.
- [ ] Internal links are valid: run the link check in `mechanical-checks.md`. NL pages link to NL targets where a Dutch page exists, and to the EN page (with "(EN)" marked) where it does not.
- [ ] Buttons are `<button>`, links are `<a href>`. No clickable `<div>`/`<span>`.
- [ ] Form controls have visible `<label>`s, correct `type`, `autocomplete`, and `required` only where the spec says (email).
- [ ] Tags closed and nested correctly; no deprecated tags; no stray template artefacts (`{{`, `None`, `%s`, `TODO`, `lorem`).
- [ ] Generated pages are not hand-edited when the body comes from `_build/` (see `build-scripts.md`).

## CSS (`css/style.css`)
- [ ] Palette uses existing custom properties (aubergine/amber). No new hard-coded colours without adding a variable; text/background contrast stays at WCAG AA.
- [ ] Font is Hanken Grotesk, self-hosted via `@font-face` with `font-display: swap`. No remote font URLs.
- [ ] Reuse existing classes (`.creds`, `.lang-switch`, …) before adding new ones. No duplicate or dead selectors introduced.
- [ ] No `!important` unless commented why. No `id` selectors for styling.
- [ ] Mobile-first: check layout at 320 px, 768 px, 1280 px. No horizontal scroll. Tap targets at least 44×44 px.
- [ ] Respects `prefers-reduced-motion`; visible `:focus-visible` styles are never removed.
- [ ] Print styles (if any) still hide navigation and show contact details.
- [ ] No unused large assets added; images are compressed and in modern formats where supported.
