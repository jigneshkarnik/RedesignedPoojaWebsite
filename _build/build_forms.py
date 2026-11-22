import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_common import *

# (file stem, EN title, NL title, EN age text, NL age text, language of the file)
FORMS = [
  ("Treatment_Agreement_Clients_under_12", "Clients under 12 years", "Cliënten jonger dan 12 jaar",
   "Signed by the parent(s) or guardian.", "Wordt ondertekend door de ouder(s) of voogd."),
  ("Treatment_Agreement_Clients_12_to_16", "Clients aged 12 to 16 years", "Cliënten van 12 tot 16 jaar",
   "Signed by the client and the parent(s) or guardian.", "Wordt ondertekend door de cliënt en de ouder(s) of voogd."),
  ("Treatment_Agreement_Clients_16_and_over", "Clients aged 16 and over", "Cliënten vanaf 16 jaar",
   "Signed by the client.", "Wordt ondertekend door de cliënt."),
]
NL_FILES = {1: "Behandelingsovereenkomst_clienten_12_tot_16_jaar", 2: "Behandelingsovereenkomst_clienten_vanaf_16_jaar"}

def card(i, lang):
    en = lang == "en"
    stem, t_en, t_nl, a_en, a_nl = FORMS[i]
    p = "" if en else "../"
    nl_missing = (not en) and i not in NL_FILES
    f = stem if (en or nl_missing) else NL_FILES[i]
    title = t_en if en else t_nl
    age = a_en if en else a_nl
    tag = "" if en or not nl_missing else " (EN)"
    read = "Read the form online" if en else "Lees het formulier online"
    dl = "Download PDF" if en else "Download PDF"
    ifr = "Treatment agreement, " + t_en if (en or nl_missing) else "Behandelingsovereenkomst, " + t_nl
    note = "" if not nl_missing else '<p class="form-note">Een Nederlandse versie voor deze leeftijdsgroep volgt; tot die tijd is het formulier in het Engels beschikbaar.</p>'
    return f'''  <article class="form-card" id="form-{i+1}">
    <h2>{("Treatment agreement" if en else "Behandelingsovereenkomst")}: {title}{tag}</h2>
    <p>{age}</p>{note}
    <p class="form-actions"><a class="btn btn-primary" href="{p}Forms/{f}.pdf" download>{dl}</a></p>
    <details>
      <summary>{read}</summary>
      <iframe src="{p}Forms/{f}.html" title="{ifr}" loading="lazy"{'' if en or not nl_missing else ' lang="en"'}></iframe>
    </details>
  </article>'''

def main(lang):
    en = lang == "en"
    h1, sub = ("Forms", "Treatment agreements") if en else ("Formulieren", "Behandelingsovereenkomsten")
    intro = ("As per the age group of the patient, a particular form will need to be signed as required. "
             "Patients do not have to print anything: the provider will give you the form in the practice. "
             "Below you can read each form in full online, and download the PDF version if you need it.") if en else (
            "Afhankelijk van de leeftijd van de cliënt moet een bepaald formulier worden ondertekend. "
            "U hoeft niets uit te printen: ik geef u het formulier in de praktijk. "
            "Hieronder kunt u elk formulier volledig online lezen en, indien gewenst, de PDF-versie downloaden.")
    cards = "\n".join(card(i, lang) for i in range(3))
    return f'''<main id="main">
<section class="page-head"><div class="wrap"><h1>{h1}</h1><p>{sub}</p></div></section>
<section class="s-white"><div class="wrap narrow">
  <div class="note-box"><strong>{"Which form applies?" if en else "Welk formulier is van toepassing?"}</strong> {intro}</div>
{cards}
</div></section>
</main>'''

write("forms.html", page("en", "forms", "Forms – Treatment agreements | Pooja Karnik",
  "Treatment agreement forms by age group: read online or download as PDF. Forms are provided in the practice, no need to print.",
  main("en"), "forms.html", "nl/forms.html", "nl/forms.html"))
write("nl/forms.html", page("nl", "forms", "Formulieren – Behandelingsovereenkomsten | Pooja Karnik, klassiek homeopaat",
  "Behandelingsovereenkomsten per leeftijdsgroep: online lezen of downloaden als PDF. U hoeft niets uit te printen, de formulieren krijgt u in de praktijk.",
  main("nl"), "../forms.html", "forms.html", "../forms.html"))
