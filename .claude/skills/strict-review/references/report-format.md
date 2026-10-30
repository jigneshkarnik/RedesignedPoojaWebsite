# Report format

## Severity
| Level | Meaning | Examples |
|---|---|---|
| **Blocker** | Must not ship. Legal/regulatory, security, or broken site. | Remedy name in text; "cure" claim; "Dr"; inline script (CSP breaks it); wheelchair info missing; wrong price; booking form broken; secret committed |
| **Major** | Wrong or inconsistent, fix before merge. | EN/NL mismatch; hand-edit to generated file that the build overwrites; missing hreflang/canonical; broken internal link; contrast fail; JSON-LD invalid |
| **Minor** | Quality issue, fix soon. | Missing `alt` on decorative image; weak title; dead CSS; unclear link text |
| **Nit** | Optional polish. | Style, naming, comment wording. List at most five |

## Output

```
## Verdict: BLOCK | CHANGES REQUESTED | APPROVE
One sentence why.

## Scope reviewed
Files and commit range. Checks run (build, greps).

## Findings
### Blockers
1. `path:line`: what is wrong. Quote: "…". Rule: <guideline file>. Failure: <concrete consequence>. Fix: <specific change>.
### Major
…
### Minor / Nits
…

## Unverified (needs a human)
- Live form submission test (EN and NL) landing in inbox, not spam
- Native-speaker read of any new Dutch text
- Anything else that cannot be checked from the repo

## Passed
One line listing guideline files that were applied with no findings.
```

## Verdict rules
- Any Blocker → **BLOCK**.
- No Blockers but any Major → **CHANGES REQUESTED**.
- Only Minor/Nit → **APPROVE** with comments.
- Empty sections are omitted, not padded. Never say "looks good" without listing what was checked.
- Do not edit files during review. Offer to apply fixes afterwards, and if applying them, edit `_build/` sources rather than generated HTML, then rebuild.
