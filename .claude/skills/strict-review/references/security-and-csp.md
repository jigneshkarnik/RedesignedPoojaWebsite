# Security and CSP (blocking)

## Content Security Policy
- [ ] **No inline `<script>` blocks and no `on*=` attributes** (`onclick`, `onload`, `onsubmit`, …). CSP is `script-src 'self'`. Inline `style=` is allowed.
- [ ] Any new third-party origin (analytics, fonts, embeds, maps, chat widgets) requires updating **both** the `CSP` constant in `_build/build_common.py` and `_headers`, and a privacy-statement update (EN `privacy.html`, NL via `build_nl.py`). Default answer to a new third party: reject, and ask the owner.
- [ ] Only permitted third parties today: YouTube (loaded after click, use the privacy-enhanced domain) and Web3Forms (`api.web3forms.com`). Anything else is a finding.
- [ ] `CSP` in `build_common.py` and `_headers` are identical in substance.
- [ ] Fonts are self-hosted. No Google Fonts links, no CDN scripts or stylesheets, no `@import url(http…)`.
- [ ] No tracking pixels, analytics snippets, or cookies. No `document.cookie`, `localStorage`, `sessionStorage` use unless added to the privacy statement and justified.
- [ ] Do not reintroduce claims of "no third-party requests"; the privacy text must stay accurate.

## Links and embeds
- [ ] Every `target="_blank"` has `rel="noopener noreferrer"`.
- [ ] External links use `https://`. No mixed content. No `http://` except inside XML namespaces and schema.org `@context` values (which should still be `https://schema.org`).
- [ ] YouTube embeds are click-to-load; no iframe loads before user action.
- [ ] No `javascript:` URLs. `mailto:` and `tel:`/WhatsApp links use the correct number/address (`+31 6 4563 9455`, `info@poojakarnik.com`).

## Booking form
- [ ] `#book-form` keeps: name, email (required), appointment type, way to meet, phone (optional), days/times, message (optional), hidden `access_key`, `botcheck` honeypot.
- [ ] Form posts over HTTPS only. Action URL is `https://api.web3forms.com/submit`.
- [ ] The Web3Forms access key is public by design; do not flag it as a leaked secret, but flag any *other* key, token, password, or private email in the repo.
- [ ] All user-provided input rendered back to the DOM uses `textContent`, never `innerHTML`.
- [ ] Form hint names Web3Forms as processor in EN and NL.

## Secrets and files
- [ ] No credentials, API tokens, private keys, `.env`, or personal data (patient names, BSN, health details) committed. Check new files and diff.
- [ ] `.well-known/security.txt` `Expires:` is in the future (currently 2027-10-30) and valid.
- [ ] `CNAME` still contains `www.poojakarnik.com`.

## Hosting caveat
GitHub Pages ignores `_headers`; only meta CSP applies. Do not rely on HTTP-only protections (HSTS, X-Frame-Options, `frame-ancestors` in a meta tag, which is ignored). Note when a change assumes headers that will not be served.
