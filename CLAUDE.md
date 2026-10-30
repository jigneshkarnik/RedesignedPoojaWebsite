# CLAUDE.md — Pooja Karnik website (redesign)

Static HTML/CSS/JS site for Pooja Karnik, classical homeopath (Uithoorn, Aalsmeer, online). No framework, no cookies; fonts self-hosted. Only third parties: YouTube (after click) and Web3Forms (booking form). Pages are indexable (noindex removed 2026-10-30).

## Purpose and positioning
Visitors should feel they can work with Pooja: seasoned, well educated, properly registered, and a distinctive way of working. **Quiet, plain, formal. No marketing gimmicks.**
- **Experience:** 25 years in clinical homeopathic practice; patients in India, UK, US, Netherlands.
- **Education:** BHMS (Bachelor of Homeopathic Medicine and Surgery), 5.5-year course, North Gujarat University, Vadodara, India. Diploma assessed/validated by Nuffic (NL). Moved to NL in 2017. Dutch A2, working towards B1.
- **Registrations:** NVKH 04-2075, RBCZ, CAT BO 76452022-03-23, CCH (India) CCH-2402, KvK 85796700. Practice name: "Pooja Karnik Homeopathy Consulting". NVKH practice visit (visitatie) 2 Oct 2024.
- **Unique approach (owner's words):** case-taking; about 90 minutes for the first consultation, listening to the patient; treating the whole person rather than the symptoms. Never claim "no one else does this" — unverifiable comparative claims are risky.
- **Audience:** Dutch locals and the Indian diaspora (international online patients are a smaller share). No Indian-language mention needed.
- **Headline (agreed):** "Listening first, then treatment for the whole person." Do NOT use "time" in the headline, no "Twenty-five years of … now in the Netherlands" style slogans (rejected as cheesy).

## Naming rules (decided by owner)
- **Never use "Dr"** anywhere (NL framing risk). Name appears as "Pooja Karnik", with "BHMS" after it where a credential helps.
- Use **"classical homeopath" / "klassiek homeopaat"** throughout. Avoid "doctor"/"physician" for her; "your GP/doctor" for the patient's own doctor is fine. Her Indian family-doctor role is written "family practice" / "gezinspraktijk".
- Telegram was removed completely (contact option and handle). Contact: WhatsApp, email, phone only.

## Compliance rules (from NVKH "Wat mag op de website" 2022 and RBCZ "Beoordelingscriteria websitevermelding")
Everything on the site counts as advertising. So:
1. **Never name homeopathic remedies** in text (no Arnica, Pulsatilla, etc.).
2. **Never use "genezen"/"cure"**; no promised results; keep the "not scientifically proven" statements.
3. **No self-written patient cases**; testimonials only if clearly written by the patient.
4. RBCZ/NVKH logos only for the individual therapist; registration numbers are optional but fine.
5. Must stay on the site: practice address; reachability (phone/email); how to get there (car, public transport, parking, **wheelchair yes/no**); name + KvK; education/experience; rates incl. out-of-hours; "not reimbursed from basic insurance, maybe from supplementary — check your policy"; clear info on services; quality statement (five-yearly review by RBCZ/NVKH criteria; TCZ disciplinary law); privacy statement (purpose, retention 20 yrs, security, rights, AVG, professional secrecy); complaints procedure naming the complaints officer and the recognised disputes body; HTTPS for any form; cookie rules (site uses none).
6. **Cancellation fees:** a website notice alone is not enough. The fee must be stated in the booking confirmation email (or on the invoice) before the first consultation. The site text says this is confirmed by email — keep the real confirmation email consistent.
7. Complaints: complaints officer = **Quasir Expertisecentrum klachtbehandeling** (free, handled within 6 weeks, reachable via NVKH, info@nvkh.nl, 0172-499595, 9:00–12:30). Disputes body = **Stichting Zorggeschil** (NVKH members; €50 fee per NVKH; binding ruling within 6 months). Disciplinary = **TCZ** (tcz.nu).
8. Invoices (not on the site) need: practice + therapist NAW, AGB codes, KvK, insured's details and birth date, treatment date, code 24200 (consult klassieke homeopathie), RBCZ licence no. + logo, NVKH member no. + logo, invoice number; never the BSN.

## Practice facts
- **Uithoorn:** Antoon Coolenlaan 41, 1422 GN. Parking in front of the house; tram 25, bus 174 (confirmed correct). Practice is on the 2nd floor (attic) via stairs → **not wheelchair accessible**; online is the alternative.
- **Aalsmeer:** Stationsweg 38, 1431 EG. Bus 340 from Hoofddorp/Uithoorn. **Wheelchair accessible** (confirmed).
- By appointment Mon–Fri 9:00–17:00. Phone/WhatsApp +31 6 4563 9455, info@poojakarnik.com.
- Rates: first consult (about 90 min) €90; follow-up (30–60 min) €70; acute €70; outside office hours €95; short phone call (<10 min) free. Payment by bank transfer on invoice, no PIN. Cancel ≥24 h ahead. Consultations VAT-exempt.
- Please bring a list of medication to the first consultation (added to meet RBCZ preparation-info rule).

## Languages
- English at the site root, Dutch under `nl/` (same file names). Header has an `EN / NL` switch on every page; `<link rel="alternate" hreflang>` is set.
- Dutch exists for: home, about, homeopathy, FAQ, klachtenregeling, algemene voorwaarden, privacy. **Talks & Training, Articles and Community work stay English** (Dutch menu marks them "(EN)").
- Dutch uses formal "u". Nuffic wording in Dutch: "diploma beoordeeld door Nuffic (diplomawaardering)". Dutch copy still needs a native-speaker read before launch.
- `js/site.js` picks Dutch/English booking-email text from `<html lang>`.

## How the site is built
Header/footer are duplicated across 17 pages, so they are generated. Source: `_build/` (underscore folders are ignored by GitHub Pages).
```
python3 _build/build_en.py && python3 _build/build_nl.py
```
- `build_common.py`: shared head/header/footer (EN+NL strings in `T`), lang switch. `build_en.py` / `build_nl.py`: page `<main>` content. Running them **overwrites** the generated pages — edit the scripts (not the HTML) for anything on home/about/legal pages, then rebuild. `homeopathy.html`, `faq.html`, `algemene-voorwaarden.html`, `privacy.html`, `sessions/articles/community.html` EN bodies are read from the existing HTML and only re-wrapped (edit those HTML files directly for body text).
- Styling: `css/style.css` (aubergine/amber palette, Hanken Grotesk). Credentials grid = `.creds`, language switch = `.lang-switch`.

## Booking form
`#book-form` fields: name, **email (required)**, appointment type, way to meet, phone (optional), days/times, message (optional), plus hidden Web3Forms `access_key` and a `botcheck` honeypot. `js/site.js` POSTs JSON to `https://api.web3forms.com/submit` (free plan, ~250 submissions/month, key registered to info@poojakarnik.com) and shows an inline thank-you/error message (EN/NL by `<html lang>`); without JS the form posts to the same endpoint. The access key is public by design.
- Web3Forms is a third-party processor: the privacy statements (EN `privacy.html`, NL via `_build/build_nl.py`, anchor `#website`) and the form hint say so. Keep them in sync if the service changes. Do not reintroduce "no third-party requests" claims.
- Not yet tested with a live submission (it sends a real email to the inbox) — send one test from the live page.

## Open items / to confirm
- Send one real test booking from the live page (EN and NL) and check it lands in info@poojakarnik.com (and not spam). Host must serve HTTPS.
- `algemene-voorwaarden` is a plain-language draft — owner OK for now, check against NVKH model terms eventually.
- Native-speaker review of Dutch text; decide Dutch versions of Talks/Articles later.
- Confirm production domain (`BASE` in `_build/build_common.py`, currently https://www.poojakarnik.com; also in `sitemap.xml`), then submit sitemap in Google Search Console and claim the Google Business Profile (Uithoorn + Aalsmeer).
- Local preview: `python3 -m http.server 8765` in the project folder.

## SEO and security (added 2026-10-30)
- `build_common.py` emits canonical, hreflang (absolute, with x-default; none for EN-only pages), Open Graph, JSON-LD (home pages only: MedicalBusiness + Person), and a meta-tag CSP (`CSP` constant). Keep `_headers` in sync with it.
- No inline `<script>` or `on*=` handlers allowed (CSP `script-src 'self'`). Inline `style=` is allowed.
- New third-party origin (analytics, fonts, embeds) needs a CSP update in both `CSP` and `_headers`.
- `sitemap.xml` is hand-maintained: add new pages there. `robots.txt`, `404.html`, `.well-known/security.txt` (expires 2027-10-30; renew).
- Hosting is GitHub Pages with custom domain www.poojakarnik.com (`CNAME` file). `_headers` only works on Netlify/Cloudflare Pages; GitHub Pages ignores it (then only the meta CSP, referrer and JS frame-buster apply; no HSTS/X-Frame-Options headers).
- Never use "doctor"/"Dr" for SEO — keywords use "homeopath", "classical homeopath", "klassiek homeopaat", "homeopathie" + Uithoorn/Aalsmeer.
