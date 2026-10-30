# Build scripts and generated output

Build: `python3 _build/build_en.py && python3 _build/build_nl.py && python3 _build/build_locations.py`

## Source of truth
- [ ] Header/footer/head content changes live in `_build/build_common.py` (EN and NL strings in `T`), never in individual HTML files.
- [ ] Home, about, and legal page bodies are edited in `build_en.py` / `build_nl.py`, not in the generated HTML (the build overwrites them).
- [ ] `homeopathy.html`, `faq.html`, `algemene-voorwaarden.html`, `privacy.html`, and the EN bodies of `sessions`/`articles`/`community.html` are edited directly in HTML; the build only re-wraps them. A change to one of these in a build script is probably in the wrong place.
- [ ] Location pages come from `build_locations.py` and `LOCS` in `build_common.py`. A new location also needs a sitemap entry, hreflang pair, and `loc_jsonld`.

## Reproducibility
- [ ] After running the build, `git status` shows no unexpected diff. Committed HTML equals fresh build output.
- [ ] Builds are deterministic: no timestamps, random ordering, or absolute local paths in output.
- [ ] Scripts run with the standard library only, on `python3`, from the repo root. No new dependencies without discussion.
- [ ] No absolute paths (`/Users/...`) in scripts or output.
- [ ] Files are read and written with `encoding="utf-8"`; Dutch diacritics and `€` survive.

## Code quality
- [ ] String templates escape user-facing special characters (`&`, `<`, `"`) correctly in HTML and JSON-LD (use `json.dumps` for JSON-LD, never hand-built strings).
- [ ] No duplicated EN/NL logic that should be shared; strings live in the `T` dictionary with the same keys in both languages. Missing key in one language is a finding.
- [ ] `BASE` (`https://www.poojakarnik.com`) is used for every absolute URL; no hard-coded domains elsewhere.
- [ ] `CSP` constant stays in sync with `_headers`.
- [ ] Functions are small, named for what they emit, and there is no dead code or commented-out blocks.
- [ ] `_build/` and `__pycache__` are not published (underscore folder ignored by Pages; `.gitignore` covers bytecode).

## Pages count
Header/footer are duplicated across the pages (17 at last count plus location pages). Confirm that every page that should exist is generated and that none were silently dropped.
