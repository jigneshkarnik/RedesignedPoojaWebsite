---
name: strict-review
description: Stringent code review for the Pooja Karnik website. Use when asked to review, audit, or check a diff, branch, file, or PR, or before committing or deploying changes to HTML, CSS, JS, or the _build scripts. Checks correctness, security/CSP, healthcare-advertising compliance (NVKH/RBCZ), naming rules, EN/NL parity, accessibility, SEO, and generated-file hygiene.
---

# Strict review

Review the target (default: `git diff` against `main`, including untracked files) against every guideline file in `references/`. Be adversarial: assume each change is wrong until checked against the files. Report only what you verified in the code.

## Procedure

1. **Scope.** Run `git status` and `git diff main...HEAD` (plus `git diff` for uncommitted work). List the changed files and classify each: generated page, build script, hand-edited HTML, CSS, JS, config (`_headers`, `sitemap.xml`, `CNAME`, `robots.txt`).
2. **Rebuild check.** If any `_build/*.py` or a generated page changed, run `python3 _build/build_en.py && python3 _build/build_nl.py && python3 _build/build_locations.py` and then `git status`. Any generated HTML that differs from what was committed is a finding (hand-edit that will be overwritten, or stale output).
3. **Mechanical greps.** Run the checks in `references/mechanical-checks.md` over the changed files and the whole site.
4. **Read each guideline file** and apply the ones relevant to the changed file types. Always apply `compliance.md` and `naming-and-tone.md` to any change that touches visible text.
5. **EN/NL parity.** For every changed EN page, confirm the NL counterpart changed consistently (or is intentionally English-only per `i18n-and-seo.md`).
6. **Report** using `references/report-format.md`. Do not fix anything unless the user asks.

## Guideline files

| File | Covers |
|---|---|
| `references/compliance.md` | NVKH/RBCZ advertising rules, required information, cancellation fees, complaints |
| `references/naming-and-tone.md` | Name/title rules, banned words, headline rules, voice |
| `references/security-and-csp.md` | CSP, inline script ban, third parties, form handling, links |
| `references/html-css.md` | Markup validity, semantics, CSS conventions |
| `references/javascript.md` | `js/site.js` standards |
| `references/build-scripts.md` | `_build/` Python scripts and generated output |
| `references/i18n-and-seo.md` | EN/NL parity, hreflang, canonical, JSON-LD, sitemap |
| `references/accessibility.md` | WCAG 2.2 AA checks |
| `references/mechanical-checks.md` | Copy-paste grep/shell checks |
| `references/report-format.md` | Severity levels and output format |

## Standards of evidence

- Every finding cites `path:line` and quotes the offending text.
- No finding without a concrete failure scenario. "Could be cleaner" is not a finding unless it breaks a rule in these files.
- If a rule cannot be checked from the repo (for example a live form submission or a native-speaker Dutch read), list it under "Unverified", never as passed.
