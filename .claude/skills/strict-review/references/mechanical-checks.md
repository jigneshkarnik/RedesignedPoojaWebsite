# Mechanical checks

Run from the repo root. Exclude `_build/`, `.git/`, `.claude/`, and `CLAUDE.md` from content greps unless checking the scripts themselves (the scripts contain the page text, so grep them too, separately). Every hit needs a human decision; some are legitimate (e.g. "doctor" in "your GP/doctor").

```bash
SITE='--include=*.html --include=*.xml --include=*.txt --include=*.js --include=*.css --exclude-dir=_build --exclude-dir=.git --exclude-dir=.claude'

# 1. Naming rules
grep -rniE '\b(dr\.?|doctor|physician|dokter|arts)\b' $SITE .
grep -rniE 'telegram' $SITE .

# 2. Compliance wording
grep -rniE 'genez|geneest|\bcure[sd]?\b|\bheals?\b|genees' $SITE .
grep -rniE 'arnica|pulsatilla|nux vomica|belladonna|sulphur|sulfur|calcarea|lycopodium|natrum|phosphorus|rhus tox|ignatia|bryonia|chamomilla|apis|aconite' $SITE .
grep -rniE 'only homeopath|no one else|best homeopath|#1|guarantee|garantie|100%' $SITE .

# 3. CSP: inline scripts and event handlers
grep -rnE '<script(?![^>]*src=)' -P --include=*.html --exclude-dir=_build .
grep -rnE '\son[a-z]+\s*=' --include=*.html --exclude-dir=_build .
grep -rnE 'javascript:' --include=*.html --exclude-dir=_build .

# 4. Third parties and insecure URLs
grep -rnoE 'https?://[^"'"'"' )<>]+' --include=*.html --include=*.js --include=*.css --exclude-dir=_build . | sed 's/.*:\(https\?:\/\/[^\/]*\).*/\1/' | sort | uniq -c | sort -rn
grep -rnE 'http://' --include=*.html --include=*.js --exclude-dir=_build . | grep -v 'www.w3.org'
grep -rnE 'target="_blank"' --include=*.html --exclude-dir=_build . | grep -v 'noopener'

# 5. Leftovers
grep -rniE 'TODO|FIXME|lorem|XXX|\{\{|\bNone\b|undefined|console\.log' $SITE .

# 6. Facts that must agree everywhere (each should show the same value on every page)
grep -rnoE '€ ?[0-9]+' --include=*.html . | sort | uniq -c
grep -rnoE '\+31 ?6 ?4563 ?9455|info@poojakarnik\.com|85796700|04-2075|CCH-2402' --include=*.html . | cut -d: -f3 | sort | uniq -c

# 7. Build is reproducible and the committed output matches
python3 _build/build_en.py && python3 _build/build_nl.py && python3 _build/build_locations.py && git status --short

# 8. JSON-LD parses
python3 - <<'PY'
import re, json, glob
for f in glob.glob('**/*.html', recursive=True):
    if f.startswith('_build'): continue
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', open(f, encoding='utf-8').read(), re.S):
        try: json.loads(m)
        except Exception as e: print('BAD JSON-LD', f, e)
PY

# 9. Internal links and ids resolve
python3 - <<'PY'
import re, glob, os
for f in glob.glob('**/*.html', recursive=True):
    if f.startswith('_build'): continue
    html = open(f, encoding='utf-8').read()
    ids = set(re.findall(r'\sid="([^"]+)"', html))
    for h in re.findall(r'href="([^"]+)"', html):
        if re.match(r'(https?:|mailto:|tel:|#$)', h): continue
        path, _, frag = h.partition('#')
        target = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        if path and path.startswith('/'): target = path.lstrip('/')
        if path and not os.path.exists(target): print('BROKEN', f, h)
        elif frag and path == '' and frag not in ids: print('NO ANCHOR', f, h)
PY

# 10. Every page in sitemap, every sitemap URL exists
python3 - <<'PY'
import re, glob, os
sm = open('sitemap.xml', encoding='utf-8').read()
urls = set(re.findall(r'<loc>https?://[^/]+/?([^<]*)</loc>', sm))
pages = {f for f in glob.glob('**/*.html', recursive=True) if not f.startswith('_build') and f != '404.html'}
for p in sorted(pages):
    if p not in urls and p.replace('index.html', '') not in urls: print('NOT IN SITEMAP', p)
for u in sorted(urls):
    if u and not os.path.exists(u) and not os.path.exists(u + 'index.html'): print('SITEMAP DEAD', u)
PY

# 11. Dutch pages: informal pronouns
grep -rnwiE 'je|jij|jouw|jou' --include=*.html nl/

# 12. Secrets
grep -rnE 'AKIA|sk-[A-Za-z0-9]{20,}|password|secret|BEGIN (RSA|PRIVATE)' --exclude-dir=.git .
```

Interpret results; do not paste raw output into the report. Quote only the offending lines.
