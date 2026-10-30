# JavaScript (`js/site.js`)

## Rules
- [ ] Loaded as an external file only (`<script src="…" defer>`); never inline (CSP).
- [ ] No frameworks or libraries added. No `eval`, `new Function`, `document.write`, `innerHTML` with dynamic data, or `setTimeout("string")`.
- [ ] Site works without JS: the booking form still posts natively to the Web3Forms endpoint, navigation is usable, and content is not hidden behind JS.
- [ ] Language comes from `document.documentElement.lang`; every user-visible string has both EN and NL variants. Adding a string to one language only is a finding.
- [ ] Network calls: only `https://api.web3forms.com/submit`. Check `fetch` errors (`!response.ok`, network failure) and show the inline error message; re-enable the submit button in `finally`.
- [ ] Prevents double submission (disable button while pending).
- [ ] Honeypot `botcheck` is never filled or removed by script.
- [ ] Failure messages tell the user an alternative (email or phone), not just "error".
- [ ] No console logging of form data. No `console.log` left in.
- [ ] Event listeners attach to elements that exist on every page the script loads on; null-guard optional elements (`if (!el) return;`) so a missing node on one page does not break the rest.
- [ ] Accessibility: status messages use `role="status"` or `aria-live`; focus moves sensibly after submit; menu toggles update `aria-expanded`.
- [ ] No storage, cookies, fingerprinting, or analytics.
- [ ] `'use strict'` or module semantics; no implicit globals; `const`/`let` only.

## Style
- Match the existing file: formatting, quote style, comment density, naming. Small functions, early returns, no dead code.
