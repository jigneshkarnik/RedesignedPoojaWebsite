# Languages and SEO

## EN / NL parity
- [ ] English at root, Dutch under `nl/` with the **same file names** (exceptions: location pages `homeopath-<city>.html` ↔ `nl/homeopaat-<city>.html`).
- [ ] Dutch exists for: home, about, homeopathy, FAQ, klachtenregeling, algemene voorwaarden, privacy, location pages. Talks & Training, Articles, Community work stay English; Dutch menu marks them "(EN)".
- [ ] Any content change on one language version has a matching change in the other. Facts (prices, hours, addresses, numbers, links) are identical.
- [ ] Header has the `EN / NL` switch on every page and it points to the correct counterpart (or to the language home if none exists).
- [ ] Dutch: formal "u", natural phrasing, no machine-translation artefacts, `€ 90` / `€90` formatting consistent with the rest of the Dutch site, 24-hour times.
- [ ] Dutch text is flagged "Unverified" for native-speaker review if new copy was added.

## Head tags (emitted by `build_common.py`)
- [ ] `<link rel="canonical">` absolute, on `BASE`, self-referencing.
- [ ] `hreflang` alternates absolute, reciprocal, include `x-default`; none for EN-only pages.
- [ ] Open Graph tags present and consistent with title/description; `og:locale` matches page language.
- [ ] JSON-LD: home pages carry MedicalBusiness + Person; location pages carry per-location JSON-LD (`loc_jsonld`). Valid JSON, correct address, telephone, `url`, `inLanguage`, no remedy names, no "Dr", no `sameAs` to Telegram, no review/rating markup unless real, patient-written, and compliant.
- [ ] Meta CSP present and valid.
- [ ] Pages are indexable (noindex removed 2026-10-30). Any `noindex` appearing is a finding unless deliberate (for example 404).

## Sitemap and crawl files
- [ ] `sitemap.xml` is hand-maintained: every indexable page (EN and NL, including location pages) is listed once, absolute URLs on `BASE`, `xhtml:link` alternates if used, and no URLs for deleted pages.
- [ ] `robots.txt` references the sitemap and does not block CSS/JS.
- [ ] `404.html` exists, links home, and works from any path depth (absolute or root-relative asset paths).
- [ ] If `BASE` domain changes, it is changed in `build_common.py`, `sitemap.xml`, `robots.txt`, `CNAME`, and JSON-LD together.

## Content SEO
- [ ] Keywords: "homeopath", "classical homeopath", "klassiek homeopaat", "homeopathie" with Uithoorn/Aalsmeer. Never "doctor"/"Dr".
- [ ] No keyword stuffing; titles read as plain descriptions.
- [ ] Location pages differ meaningfully from each other (address, travel, accessibility), not just a swapped city name.
