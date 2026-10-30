import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_common import *

# Location landing pages (Uithoorn, Aalsmeer), EN + NL. Run after build_en.py / build_nl.py.
# EN: homeopath-<city>.html   NL: nl/homeopaat-<city>.html

MAPS = "https://www.google.com/maps/search/?api=1&amp;query="

C = {
 "uithoorn": dict(
  name="Uithoorn", other="aalsmeer", other_name="Aalsmeer", street="Antoon Coolenlaan 41", zip="1422 GN",
  en_near="Mijdrecht, De Kwakel, Amstelhoek and Aalsmeer", nl_near="Mijdrecht, De Kwakel, Amstelhoek en Aalsmeer",
  en_travel=["By car: parking in front of the house", "Public transport: tram 25, bus 174"],
  nl_travel=["Met de auto: parkeren voor de deur", "Openbaar vervoer: tram 25, bus 174"],
  en_access="Not accessible for wheelchair users: the practice is on the second floor (attic), reached by stairs. An online consultation is an alternative, and the Aalsmeer practice is wheelchair accessible.",
  nl_access="Niet toegankelijk voor rolstoelgebruikers: de praktijk bevindt zich op de tweede verdieping (zolder), bereikbaar via een trap. Een online consult is een alternatief, en de praktijk in Aalsmeer is wel rolstoeltoegankelijk."),
 "aalsmeer": dict(
  name="Aalsmeer", other="uithoorn", other_name="Uithoorn", street="Stationsweg 38", zip="1431 EG",
  en_near="Kudelstaart, Rijsenhout, Hoofddorp, Amstelveen and Uithoorn", nl_near="Kudelstaart, Rijsenhout, Hoofddorp, Amstelveen en Uithoorn",
  en_travel=["Public transport: bus 340 from Hoofddorp or Uithoorn"],
  nl_travel=["Openbaar vervoer: bus 340 vanaf Hoofddorp of Uithoorn"],
  en_access="Wheelchair accessible.",
  nl_access="Toegankelijk voor rolstoelgebruikers."),
}

def li(items): return "".join(f"<li>{x}</li>" for x in items)

def en_main(c):
    n, o = c["name"], c["other_name"]
    return f'''<main id="main">

<section class="page-head"><div class="wrap"><h1>Classical homeopath in {n}</h1><p>Pooja Karnik, BHMS · consultations by appointment, Monday to Friday, 9:00 to 17:00.</p></div></section>

<section class="s-white">
  <div class="wrap narrow prose">
    <p class="lead">I am Pooja Karnik, a classical homeopath with 25 years of experience. In {n} I see adults and children for a first consultation of about 90 minutes, in which I listen to your whole story and look at the person, not only the symptoms.</p>
    <p>Patients come from {c["en_near"]}, and from further away. If a visit is not practical, I also consult online anywhere in the Netherlands.</p>

    <h2>Address</h2>
    <address>Pooja Karnik Homeopathy Consulting<br>{c["street"]}<br>{c["zip"]} {n}</address>
    <p><a href="{MAPS}{c["street"].replace(" ", "+")}+{c["zip"].replace(" ", "+")}+{n}" target="_blank" rel="noopener noreferrer">Open in Google Maps ↗</a></p>

    <h2>Getting there</h2>
    <ul class="tags">{li(c["en_travel"])}</ul>
    <h2>Accessibility</h2>
    <p>{c["en_access"]}</p>

    <h2>What to expect</h2>
    <p>The first consultation takes about 90 minutes. We go through your complaints, sleep, digestion, energy, emotions, stress and family history, at your own pace. Afterwards I study your case and choose a remedy, with clear instructions on how to take it. Follow-up consultations take 30 to 60 minutes. Please bring a list of any medication you take.</p>
    <p>Homeopathy is a complementary approach. It is not scientifically proven to be effective beyond placebo and does not replace care from your GP or specialist. Please never stop or change prescribed medication without speaking to your doctor.</p>

    <h2>Fees</h2>
    <table class="prices">
      <tbody>
        <tr><th scope="row">First consultation<small>About 90 minutes</small></th><td>€90</td></tr>
        <tr><th scope="row">Follow-up consultation<small>30 to 60 minutes</small></th><td>€70</td></tr>
        <tr><th scope="row">Acute consultation<small>A new, short-term concern</small></th><td>€70</td></tr>
        <tr><th scope="row">Outside office hours<small>Urgent, after hours</small></th><td>€95</td></tr>
      </tbody>
    </table>
    <div class="note-box"><strong>Insurance:</strong> consultations are not reimbursed from the basic insurance, but may be reimbursed under a supplementary insurance, depending on your policy. Please check your policy before you book. Payment is by bank transfer on invoice; please cancel at least 24 hours in advance. Consultations are exempt from VAT.</div>

    <h2>Registered and qualified</h2>
    <p>BHMS (Bachelor of Homeopathic Medicine and Surgery, 5.5 years), diploma validated by Nuffic. Member of NVKH (04-2075), registered with RBCZ and CAT (BO 76452022-03-23), KvK 85796700. See <a href="about.html">about me</a> and the <a href="klachtenregeling.html">complaints procedure</a>.</p>

    <h2>Book a consultation</h2>
    <p>Contact me by WhatsApp or phone on <a href="tel:+31645639455">+31 6 4563 9455</a>, by email at <a href="mailto:info@poojakarnik.com">info@poojakarnik.com</a>, or use the <a href="index.html#appointment">booking form</a>. I usually reply within a working day.</p>
    <p>I also practise in <a href="homeopath-{c["other"]}.html">{o}</a>.</p>
  </div>
</section>

</main>'''

def nl_main(c):
    n, o = c["name"], c["other_name"]
    return f'''<main id="main">

<section class="page-head"><div class="wrap"><h1>Klassiek homeopaat in {n}</h1><p>Pooja Karnik, BHMS · consulten op afspraak, maandag tot en met vrijdag, 9:00 tot 17:00.</p></div></section>

<section class="s-white">
  <div class="wrap narrow prose">
    <p class="lead">Ik ben Pooja Karnik, klassiek homeopaat met 25 jaar ervaring. In {n} zie ik volwassenen en kinderen voor een eerste consult van ongeveer 90 minuten, waarin ik naar uw hele verhaal luister en kijk naar de persoon, niet alleen naar de klachten.</p>
    <p>Mensen komen uit {c["nl_near"]}, en van verder weg. Als een bezoek niet uitkomt, consulteer ik ook online in heel Nederland.</p>

    <h2>Adres</h2>
    <address>Pooja Karnik Homeopathy Consulting<br>{c["street"]}<br>{c["zip"]} {n}</address>
    <p><a href="{MAPS}{c["street"].replace(" ", "+")}+{c["zip"].replace(" ", "+")}+{n}" target="_blank" rel="noopener noreferrer">Openen in Google Maps ↗</a></p>

    <h2>Bereikbaarheid</h2>
    <ul class="tags">{li(c["nl_travel"])}</ul>
    <h2>Toegankelijkheid</h2>
    <p>{c["nl_access"]}</p>

    <h2>Wat u kunt verwachten</h2>
    <p>Het eerste consult duurt ongeveer 90 minuten. We bespreken uw klachten, slaap, spijsvertering, energie, emoties, stress en familiegeschiedenis, in uw eigen tempo. Daarna bestudeer ik uw casus en kies ik een middel, met duidelijke uitleg over de inname. Vervolgconsulten duren 30 tot 60 minuten. Neemt u een lijst met uw medicatie mee.</p>
    <p>Homeopathie is een complementaire benadering. De werkzaamheid is niet wetenschappelijk bewezen en homeopathie vervangt niet de zorg van uw huisarts of specialist. Stop of wijzig nooit voorgeschreven medicatie zonder overleg met uw arts.</p>

    <h2>Tarieven</h2>
    <table class="prices">
      <tbody>
        <tr><th scope="row">Eerste consult<small>Ongeveer 90 minuten</small></th><td>€90</td></tr>
        <tr><th scope="row">Vervolgconsult<small>30 tot 60 minuten</small></th><td>€70</td></tr>
        <tr><th scope="row">Acuut consult<small>Een nieuwe, kortdurende klacht</small></th><td>€70</td></tr>
        <tr><th scope="row">Buiten kantoortijden<small>Dringend, na werktijd</small></th><td>€95</td></tr>
      </tbody>
    </table>
    <div class="note-box"><strong>Vergoeding:</strong> consulten worden niet vergoed uit de basisverzekering, maar mogelijk wel uit een aanvullende verzekering, afhankelijk van uw polis. Controleer uw polis voordat u een afspraak maakt. Betaling gebeurt per bankoverschrijving op factuur; annuleer minimaal 24 uur van tevoren. Consulten zijn vrijgesteld van btw.</div>

    <h2>Geregistreerd en gekwalificeerd</h2>
    <p>BHMS (Bachelor of Homeopathic Medicine and Surgery, 5,5 jaar), diploma beoordeeld door Nuffic (diplomawaardering). Lid van NVKH (04-2075), geregistreerd bij RBCZ en CAT (BO 76452022-03-23), KvK 85796700. Zie <a href="about.html">over mij</a> en de <a href="klachtenregeling.html">klachtenregeling</a>.</p>

    <h2>Maak een afspraak</h2>
    <p>Neem contact op via WhatsApp of telefoon, <a href="tel:+31645639455">+31 6 4563 9455</a>, per e-mail via <a href="mailto:info@poojakarnik.com">info@poojakarnik.com</a>, of gebruik het <a href="index.html#appointment">afspraakformulier</a>. Ik reageer meestal binnen een werkdag.</p>
    <p>Ik heb ook een praktijk in <a href="homeopaat-{c["other"]}.html">{o}</a>.</p>
  </div>
</section>

</main>'''

for key, c in C.items():
    n = c["name"]
    en_f, nl_f = f"homeopath-{key}.html", f"nl/homeopaat-{key}.html"
    write(en_f, page("en", f"loc-{key}",
        f"Classical Homeopath in {n} | Pooja Karnik, BHMS",
        f"Classical homeopath in {n}: Pooja Karnik, BHMS. 25 years of experience, first consultation about 90 minutes. Address, travel, accessibility and fees. Registered with NVKH, RBCZ and CAT.",
        en_main(c), en_f, nl_f, nl_f))
    write(nl_f, page("nl", f"loc-{key}",
        f"Klassiek homeopaat in {n} | Pooja Karnik, BHMS",
        f"Klassiek homeopaat in {n}: Pooja Karnik, BHMS. 25 jaar ervaring, eerste consult ongeveer 90 minuten. Adres, bereikbaarheid, toegankelijkheid en tarieven. Aangesloten bij NVKH, RBCZ en CAT.",
        nl_main(c), en_f, nl_f, "../" + en_f))
