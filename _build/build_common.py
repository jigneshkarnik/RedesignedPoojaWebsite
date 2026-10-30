import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SV = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
SV16 = SV.replace('stroke-width="1.8"', 'stroke-width="1.6"')
CAL = f'<svg {SV}><rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/></svg>'
CAL3 = f'<svg {SV}><rect x="4" y="5" width="16" height="15" rx="3"/><path d="M4 10h16M9 3v4M15 3v4"/></svg>'
MAIL = f'<svg {SV}><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/></svg>'
MENU = f'<svg {SV}><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
WA = f'<svg {SV16}><path d="M12 3a9 9 0 0 0-7.700 13.600L3 21l4.500-1.200A9 9 0 1 0 12 3z"/><path d="M9 8.500c0 3 2.500 5.500 5.500 5.500l1-1.500-2-1-.8.800c-.8-.3-1.800-1.300-2.100-2.100l.8-.8-1-2L9 8.500z"/></svg>'
MAIL16 = f'<svg {SV16}><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/></svg>'
PHONE = f'<svg {SV16}><path d="M6 3h3l1.500 4-2 1.300a11 11 0 0 0 6.200 6.200L16 12.500l4 1.500v3a2 2 0 0 1-2 2A15 15 0 0 1 4 5a2 2 0 0 1 2-2z"/></svg>'
TG = f'<svg {SV16}><path d="M21 4L3 11l5 2 2 6 3-4 5 4 3-15z"/><path d="M8 13l9-6"/></svg>'

T = {
 "en": dict(
  lang="en", home="Home", about="About me", homeo="Homeopathy", faq="FAQ", sessions="Talks & Training",
  articles="Articles", cta="Book a consultation", skip="Skip to content", role="Classical homeopath",
  menu="Menu", main_nav="Main", brand_aria="Pooja Karnik, home", lang_label="Language",
  f_about="Classical homeopath (BHMS) with 25 years of experience. Registered with NVKH and RBCZ. Consultations in Uithoorn, Aalsmeer and online.",
  f_practice="Practice", f_biz="Business details", f_know="Good to know",
  f_vat="Homeopathic consultations are exempt from VAT.",
  f_links=[("homeopath-uithoorn.html","Homeopath in Uithoorn"),("homeopath-aalsmeer.html","Homeopath in Aalsmeer"),("klachtenregeling.html","Klachtenregeling (complaints)"),("privacy.html","Privacyverklaring (privacy)"),("algemene-voorwaarden.html","Algemene voorwaarden (terms)"),("community.html","Community work")],
  f_disc="Homeopathy is a complementary approach and does not replace care from your GP or specialist. Please never stop or change prescribed medication without speaking to your doctor. In an emergency call 112.",
  f_copy="&copy; 2026 Pooja Karnik. This website uses no tracking cookies.",
  f_cch="Central Council of Homeopathy (India)",
  nvkh_alt="NVKH – Nederlandse Vereniging van Klassiek Homeopaten", rbcz_alt="RBCZ – Een vrije zorgkeuze"),
 "nl": dict(
  lang="nl", home="Home", about="Over mij", homeo="Homeopathie", faq="Veelgestelde vragen", sessions="Lezingen &amp; trainingen (EN)",
  articles="Artikelen (EN)", cta="Maak een afspraak", skip="Ga naar de inhoud", role="Klassiek homeopaat",
  menu="Menu", main_nav="Hoofdmenu", brand_aria="Pooja Karnik, home", lang_label="Taal",
  f_about="Klassiek homeopaat (BHMS) met 25 jaar ervaring. Geregistreerd bij NVKH en RBCZ. Consulten in Uithoorn, Aalsmeer en online.",
  f_practice="Praktijk", f_biz="Bedrijfsgegevens", f_know="Goed om te weten",
  f_vat="Homeopathische consulten zijn vrijgesteld van btw.",
  f_links=[("homeopaat-uithoorn.html","Homeopaat in Uithoorn"),("homeopaat-aalsmeer.html","Homeopaat in Aalsmeer"),("klachtenregeling.html","Klachtenregeling"),("privacy.html","Privacyverklaring"),("algemene-voorwaarden.html","Algemene voorwaarden"),("../community.html","Vrijwilligerswerk (EN)")],
  f_disc="Homeopathie is een complementaire benadering en vervangt niet de zorg van uw huisarts of specialist. Stop of wijzig nooit voorgeschreven medicatie zonder overleg met uw arts. Bel bij nood 112.",
  f_copy="&copy; 2026 Pooja Karnik. Deze website gebruikt geen trackingcookies.",
  f_cch="Central Council of Homeopathy (India)",
  nvkh_alt="NVKH – Nederlandse Vereniging van Klassiek Homeopaten", rbcz_alt="RBCZ – Een vrije zorgkeuze"),
}

BASE = "https://www.poojakarnik.com"   # production origin: canonical, hreflang, sitemap, structured data
EN_ONLY = {"sessions", "articles", "community"}   # no Dutch twin, so no hreflang pair

# Meta-tag CSP: works on any static host (GitHub Pages cannot send headers). Keep in sync with _headers.
CSP = ("default-src 'none'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; "
       "font-src 'self'; connect-src https://api.web3forms.com; frame-src https://www.youtube-nocookie.com; "
       "form-action https://api.web3forms.com; base-uri 'self'; object-src 'none'; upgrade-insecure-requests")

def url(path):
    path = "" if path in ("", "index.html") else path
    path = path[:-len("index.html")] if path.endswith("/index.html") else path
    return f"{BASE}/{path}"

def jsonld(lang):
    import json
    nl = lang == "nl"
    data = {
      "@context": "https://schema.org",
      "@graph": [{
        "@type": ["MedicalBusiness", "ProfessionalService"],
        "@id": BASE + "/#practice",
        "name": "Pooja Karnik Homeopathy Consulting",
        "alternateName": ["Pooja Karnik, klassiek homeopaat" if nl else "Pooja Karnik, classical homeopath"],
        "description": ("Klassiek homeopaat in Uithoorn en Aalsmeer, ook online. Eerste consult van ongeveer 90 minuten."
                        if nl else "Classical homeopath in Uithoorn and Aalsmeer, also online. First consultation of about 90 minutes."),
        "url": url("nl/" if nl else ""),
        "image": BASE + "/images/pooja_karnik.jpg",
        "logo": BASE + "/images/logo.png",
        "telephone": "+31645639455", "email": "info@poojakarnik.com",
        "taxID": "85796700",
        "priceRange": "EUR 50 - EUR 75",
        "medicalSpecialty": "Homeopathy",
        "address": {"@type": "PostalAddress", "streetAddress": "Antoon Coolenlaan 41", "postalCode": "1422 GN",
                    "addressLocality": "Uithoorn", "addressCountry": "NL"},
        "location": [
          {"@type": "Place", "name": "Uithoorn", "address": {"@type": "PostalAddress", "streetAddress": "Antoon Coolenlaan 41", "postalCode": "1422 GN", "addressLocality": "Uithoorn", "addressCountry": "NL"}},
          {"@type": "Place", "name": "Aalsmeer", "address": {"@type": "PostalAddress", "streetAddress": "Stationsweg 38", "postalCode": "1431 EG", "addressLocality": "Aalsmeer", "addressCountry": "NL"}}],
        "areaServed": [{"@type": "City", "name": "Uithoorn"}, {"@type": "City", "name": "Aalsmeer"}, {"@type": "Country", "name": "Netherlands"}],
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"},
        "knowsLanguage": ["en", "nl"],
        "founder": {"@id": BASE + "/#pooja"}
      }, {
        "@type": "Person", "@id": BASE + "/#pooja", "name": "Pooja Karnik",
        "jobTitle": "Klassiek homeopaat" if nl else "Classical homeopath",
        "image": BASE + "/images/pooja_karnik.jpg",
        "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": "BHMS (Bachelor of Homeopathic Medicine and Surgery)"}],
        "worksFor": {"@id": BASE + "/#practice"}
      }]}
    return json.dumps(data, ensure_ascii=False, indent=2)

LOCS = {
  "uithoorn": dict(name="Uithoorn", street="Antoon Coolenlaan 41", zip="1422 GN", q="Antoon+Coolenlaan+41+1422+GN+Uithoorn"),
  "aalsmeer": dict(name="Aalsmeer", street="Stationsweg 38", zip="1431 EG", q="Stationsweg+38+1431+EG+Aalsmeer"),
}

def loc_jsonld(lang, city, self_url):
    import json
    nl = lang == "nl"
    L = LOCS[city]
    data = {
      "@context": "https://schema.org",
      "@type": ["MedicalBusiness", "ProfessionalService"],
      "@id": f"{BASE}/#practice-{city}",
      "name": f"Pooja Karnik Homeopathy Consulting, {L['name']}",
      "description": (f"Klassiek homeopaat in {L['name']}. Eerste consult van ongeveer 90 minuten, op afspraak."
                      if nl else f"Classical homeopath in {L['name']}. First consultation of about 90 minutes, by appointment."),
      "url": self_url,
      "image": BASE + "/images/pooja_karnik.jpg",
      "telephone": "+31645639455", "email": "info@poojakarnik.com",
      "medicalSpecialty": "Homeopathy",
      "address": {"@type": "PostalAddress", "streetAddress": L["street"], "postalCode": L["zip"],
                  "addressLocality": L["name"], "addressCountry": "NL"},
      "hasMap": "https://www.google.com/maps/search/?api=1&query=" + L["q"],
      "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"},
      "parentOrganization": {"@id": BASE + "/#practice"},
      "knowsLanguage": ["en", "nl"],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)

def head(lang, title, desc, alt_en, alt_nl, key=""):
    p = "../" if lang == "nl" else ""
    # root-relative paths of the two language versions
    en_path = alt_en[3:] if alt_en.startswith("../") else alt_en
    nl_path = alt_nl if lang == "nl" else alt_nl
    nl_path = nl_path if nl_path.startswith("nl/") else "nl/" + nl_path
    self_url = url(en_path if lang == "en" else nl_path)
    alts = "" if key in EN_ONLY else (
        f'  <link rel="alternate" hreflang="en" href="{url(en_path)}">\n'
        f'  <link rel="alternate" hreflang="nl" href="{url(nl_path)}">\n'
        f'  <link rel="alternate" hreflang="x-default" href="{url(en_path)}">\n')
    ld = f'  <script type="application/ld+json">\n{jsonld(lang)}\n  </script>\n' if key == "home" else ""
    if key.startswith("loc-"):
        ld = f'  <script type="application/ld+json">\n{loc_jsonld(lang, key[4:], self_url)}\n  </script>\n'
    loc, loc_alt = ("nl_NL", "en_GB") if lang == "nl" else ("en_GB", "nl_NL")
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="{CSP}">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="author" content="Pooja Karnik">
  <meta name="theme-color" content="#3a1a31">
  <link rel="canonical" href="{self_url}">
{alts}  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{self_url}">
  <meta property="og:site_name" content="Pooja Karnik Homeopathy Consulting">
  <meta property="og:locale" content="{loc}">
  <meta property="og:image" content="{BASE}/images/pooja_karnik.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" href="{p}images/logo.png">
  <link rel="preload" href="{p}fonts/hanken-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{p}css/style.css">
{ld}</head>
'''

def header(lang, page, alt_href):
    t = T[lang]
    p = "../" if lang == "nl" else ""
    def a(key, href, label):
        cur = ' aria-current="page"' if page == key else ''
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    if lang == "en":
        links = [("home","index.html",t["home"]),("about","about.html",t["about"]),("homeo","homeopathy.html",t["homeo"]),("faq","faq.html",t["faq"]),("sessions","sessions.html",t["sessions"]),("articles","articles.html",t["articles"])]
        cta = "index.html#appointment"
    else:
        links = [("home","index.html",t["home"]),("about","about.html",t["about"]),("homeo","homeopathy.html",t["homeo"]),("faq","faq.html",t["faq"]),("sessions","../sessions.html",t["sessions"]),("articles","../articles.html",t["articles"])]
        cta = "index.html#appointment"
    lis = "".join(a(*l) for l in links)
    if lang == "en":
        sw = f'<li class="lang-switch" role="group" aria-label="{t["lang_label"]}"><a class="on" href="" aria-current="true" lang="en" hreflang="en">EN</a><span aria-hidden="true">/</span><a href="{alt_href}" lang="nl" hreflang="nl">NL</a></li>'
    else:
        sw = f'<li class="lang-switch" role="group" aria-label="{t["lang_label"]}"><a href="{alt_href}" lang="en" hreflang="en">EN</a><span aria-hidden="true">/</span><a class="on" href="" aria-current="true" lang="nl" hreflang="nl">NL</a></li>'
    return f'''<body>
<a class="skip" href="#main">{t["skip"]}</a>
<header class="site-header">
  <div class="wrap header-in">
    <a class="brand" href="index.html" aria-label="{t["brand_aria"]}">
      <img src="{p}images/logo.png" alt="" width="76" height="52">
      <span>Pooja Karnik<small>{t["role"]}</small></span>
    </a>
    <button class="menu-btn" id="menu-btn" aria-label="{t["menu"]}" aria-expanded="false" aria-controls="nav">{MENU}</button>
    <nav class="nav" id="nav" aria-label="{t["main_nav"]}">
      <ul>{lis}{sw}<li class="nav-cta"><a href="{cta}">{t["cta"]}</a></li></ul>
    </nav>
  </div>
</header>
'''

def footer(lang):
    t = T[lang]
    p = "../" if lang == "nl" else ""
    lis = "\n".join(f'          <li><a href="{h}">{l}</a></li>' for h, l in t["f_links"])
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h3>Pooja Karnik</h3>
        <p>{t["f_about"]}</p>
        <div class="foot-logos">
          <img src="{p}images/affiliation5.png" alt="{t["nvkh_alt"]}">
          <img src="{p}images/affiliation6.png" alt="{t["rbcz_alt"]}">
        </div>
      </div>
      <div>
        <h3>{t["f_practice"]}</h3>
        <p>Pooja Karnik Homeopathy Consulting<br>Antoon Coolenlaan 41<br>1422 GN Uithoorn</p>
        <p>Stationsweg 38<br>1431 EG Aalsmeer</p>
        <p><a href="tel:+31645639455">+31 6 4563 9455</a><br><a href="mailto:info@poojakarnik.com">info@poojakarnik.com</a></p>
      </div>
      <div>
        <h3>{t["f_biz"]}</h3>
        <p>KvK: 85796700<br>NVKH: 04-2075<br>CAT BO: 76452022-03-23<br>{t["f_cch"]}: CCH-2402</p>
        <p>{t["f_vat"]}</p>
      </div>
      <div>
        <h3>{t["f_know"]}</h3>
        <ul>
{lis}
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <p>{t["f_disc"]}</p>
      <p>{t["f_copy"]}</p>
    </div>
  </div>
</footer>
<script src="{p}js/site.js" defer></script>
</body>
</html>
'''

def page(lang, page_key, title, desc, main, alt_en, alt_nl, alt_href):
    return head(lang, title, desc, alt_en, alt_nl, page_key) + header(lang, page_key, alt_href) + main + "\n" + footer(lang)

def old_main(fname):
    s = open(os.path.join(ROOT, fname)).read()
    m = re.search(r'<main id="main">.*?</main>', s, re.S)
    return m.group(0)

def old_meta(fname):
    s = open(os.path.join(ROOT, fname)).read()
    fix = lambda x: x.replace("Dr Pooja Karnik", "Pooja Karnik").replace("Dr Pooja", "Pooja")
    return fix(re.search(r'<title>(.*?)</title>', s).group(1)), fix(re.search(r'<meta name="description" content="(.*?)">', s).group(1))

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)
