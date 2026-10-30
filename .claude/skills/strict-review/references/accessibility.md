# Accessibility (WCAG 2.2 AA)

Many visitors are older or unwell; treat these as required, not nice-to-have.

- [ ] **Contrast:** body text at least 4.5:1, large text and UI components at least 3:1, in all states (hover, focus, disabled, placeholder). Check any new colour pair.
- [ ] **Keyboard:** every interactive element is reachable and operable by keyboard in a logical order; no keyboard traps; menu and language switch work without a mouse.
- [ ] **Focus:** visible focus indicator on all focusable elements (at least 2 px, 3:1 contrast). Never `outline: none` without a replacement.
- [ ] **Target size:** at least 24×24 CSS px minimum, aim for 44×44 on touch.
- [ ] **Text resize/reflow:** usable at 200% zoom and at 320 px width with no horizontal scrolling or clipped text. Use relative units for type.
- [ ] **Images:** meaningful `alt`; decorative images `alt=""`. Logos (RBCZ, NVKH) have alt naming the organisation.
- [ ] **Forms:** each control has a programmatic label; required state is conveyed in text, not colour alone; errors are identified in text, associated with the field, and announced (`aria-live`/`role="alert"` or focus move).
- [ ] **Language:** `lang` on `<html>`; inline phrases in another language carry `lang` (for example English terms on Dutch pages).
- [ ] **Links:** link text makes sense out of context (no bare "click here"); links opening in a new tab say so; links are distinguishable beyond colour.
- [ ] **Headings and landmarks:** logical heading order; one `<main>`; nav landmarks labelled when more than one.
- [ ] **Motion:** no auto-playing media or animation; honour `prefers-reduced-motion`.
- [ ] **Embeds:** the YouTube click-to-load control is a real button with an accessible name; the iframe has a `title`.
- [ ] **Tables:** if used for rates, have `<th scope>` and a caption; never for layout.
- [ ] **Wheelchair info:** accessibility statements for each location are present and consistent (see `compliance.md`).
