import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_common import *

def nlpage(key, title, desc, main, f):
    return page("nl", key, title, desc, main, "../" + f, f, "../" + f)

IMG = "../images/"
# ---------------------------------------------------------------- HOME
INDEX = f'''<main id="main">

<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1><span>Pooja Karnik, BHMS, India · Klassiek homeopaat in Uithoorn en Aalsmeer</span>Eerst luisteren, daarna een persoonlijke, holistische homeopathische behandeling</h1>
      <p class="lead">Een eerste consult duurt ongeveer 90 minuten, zodat uw klachten, uw voorgeschiedenis en uw dagelijks leven aan bod kunnen komen, om te komen tot een holistisch homeopathisch behandelplan. Opgeleid in India (BHMS, een opleiding van 5,5 jaar), diploma beoordeeld door Nuffic, geregistreerd bij NVKH, RBCZ en CAT. Consulten in Uithoorn, Aalsmeer en online.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="#appointment">{CAL}Maak een afspraak</a>
        <a class="btn btn-ghost" href="#credentials">Opleiding en registraties</a>
      </div>
    </div>
    <figure class="plate">
      <div class="plate-img"><img src="{IMG}pooja_karnik.jpg" width="900" height="1126" alt="Pooja Karnik, klassiek homeopaat, in een oranje sari"></div>
      <figcaption><strong>Pooja Karnik, BHMS</strong>Klassiek homeopaat. Lid van de NVKH, geregistreerd bij RBCZ en CAT.</figcaption>
    </figure>
  </div>
</section>

<div class="register">
  <dl class="wrap">
    <div class="reg-item"><dt>Ervaring</dt><dd>25 jaar<small>In de homeopathische praktijk</small></dd></div>
    <div class="reg-item"><dt>Opleiding</dt><dd>BHMS, India<small>Bachelor of Homeopathic Medicine and Surgery, een opleiding van 5,5 jaar. Diploma beoordeeld door Nuffic</small></dd></div>
    <div class="reg-item"><dt>Cliënten in</dt><dd>4 landen<small>India, het Verenigd Koninkrijk, de VS en Nederland</small></dd></div>
    <div class="reg-item"><dt>Geregistreerd bij</dt><dd>NVKH, RBCZ, CAT<small>En de Central Council of Homeopathy, India</small></dd></div>
  </dl>
</div>

<section id="method" class="s-white">
  <div class="wrap method">
    <div>
      <span class="eyebrow">Mijn werkwijze</span>
      <h2>Het werk begint met uw verhaal</h2>
      <p class="lead">Ik neem de tijd om uw hele verhaal te horen en behandel de mens, niet alleen de klachten.</p>
      <p>Klassieke homeopathie vraagt om een volledig beeld voordat er iets wordt voorgeschreven. Daarom is het eerste consult lang en werk ik nooit met een standaardprogramma.</p>
      <p><a class="btn btn-ghost" href="homeopathy.html">Hoe homeopathie werkt</a></p>
    </div>
    <ul class="method-list">
      <li><h3>Luisteren</h3><p>Het eerste consult duurt ongeveer 90 minuten. We bespreken uw klachten, slaap, spijsvertering, energie, emoties, stress en familiegeschiedenis, in uw eigen tempo.</p></li>
      <li><h3>De hele mens</h3><p>Ik kijk naar het lichamelijke, emotionele en leefstijlbeeld samen, niet naar klachten afzonderlijk. Twee mensen met dezelfde diagnose kunnen een verschillend advies krijgen.</p></li>
      <li><h3>Een zorgvuldig voorschrift</h3><p>Na het consult bestudeer ik uw casus en kies ik een middel en een potentie, met duidelijke uitleg over het gebruik.</p></li>
      <li><h3>Evaluatie en vervolg</h3><p>Bij elk vervolgconsult bekijken we uw reactie en stel ik het voorschrift zo nodig bij.</p></li>
      <li><h3>Naast uw huisarts</h3><p>Homeopathie is complementair. Ik raad u aan onder behandeling van uw huisarts of specialist te blijven en breng hen, met uw toestemming, op de hoogte. Ik zie mensen van alle leeftijden, ook tijdens zwangerschap of borstvoeding.</p></li>
      <li><h3>Ervaring in meerdere culturen</h3><p>Vijfentwintig jaar praktijk in India, het Verenigd Koninkrijk, de VS en Nederland heeft mij laten zien hoe verschillend mensen ziekte ervaren en beschrijven.</p></li>
    </ul>
  </div>
</section>

<section id="expect" class="s-dark">
  <div class="wrap">
    <div class="sec-head">
      <h2>Uw consult, stap voor stap</h2>
      <p class="lead">U kunt beginnen met een kort intakegesprek, of direct een eerste consult plannen.</p>
    </div>
    <ol class="steps">
      <li><h3>Intake</h3><span class="dur">Kort, vrijblijvend</span><p>Een kennismaking met klassieke homeopathie en mijn werkwijze, zodat u kunt bepalen of het bij u past.</p></li>
      <li><h3>Eerste consult</h3><span class="dur">Ongeveer 90 minuten</span><p>Een uitgebreide anamnese en een lichamelijk en emotioneel overzicht. Neem een lijst mee van de medicijnen die u gebruikt. In Nederland is dit consult in de praktijk; vanuit het buitenland kan het online.</p></li>
      <li><h3>Voorschrift</h3><span class="dur">Na het consult</span><p>Ik bestudeer uw casus en kies een middel en een potentie, met uitleg over het gebruik.</p></li>
      <li><h3>Vervolgconsult</h3><span class="dur">30 tot 60 minuten</span><p>We bespreken uw reactie en passen het voorschrift aan. In de praktijk of via een videogesprek.</p></li>
    </ol>
  </div>
</section>

<section id="training">
  <div class="wrap career">
    <div>
      <span class="eyebrow">Opleiding en loopbaan</span>
      <h2>Opgeleid in India, beoordeeld en geregistreerd in Nederland</h2>
      <p>Ik voltooide een opleiding van 5,5 jaar tot Bachelor of Homeopathic Medicine and Surgery (BHMS) aan de North Gujarat University, naast anatomie en fysiologie. Daarna had ik mijn eigen kliniek en een gezinspraktijk, waar ik huishoudens van alle leeftijden en achtergronden begeleidde.</p>
      <p>Sinds 2017 woon ik in Nederland. Mijn Indiase diploma is door Nuffic, de Nederlandse organisatie voor diplomawaardering, beoordeeld en gewaardeerd, en ik werk als geregistreerd klassiek homeopaat.</p>
      <p style="margin-top:1.6rem"><a class="btn btn-ghost" href="about.html">Volledige achtergrond</a></p>
    </div>
    <ol class="timeline">
      <li><strong>BHMS, North Gujarat University</strong><span>Opleiding van 5,5 jaar in Homeopathic Medicine and Surgery, Vadodara</span></li>
      <li><strong>Stage</strong><span>Anamnese, vervolgconsulten en dagelijkse praktijk onder begeleiding van een ervaren beoefenaar</span></li>
      <li><strong>Eigen kliniek, Vadodara</strong><span>Eigenaar van de kliniek</span></li>
      <li><strong>Gezinspraktijk, Pune</strong><span>Zorg voor veel huishoudens, van alle leeftijden</span></li>
      <li><strong>2017: Nederland</strong><span>Diploma beoordeeld door Nuffic. Geregistreerd bij NVKH, CAT en de Kamer van Koophandel.</span></li>
      <li><strong>Nu</strong><span>25 jaar ervaring, met cliënten in India, het Verenigd Koninkrijk, de VS en Nederland</span></li>
    </ol>
  </div>
</section>

<section class="s-white" id="credentials">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Kwalificaties die u kunt nagaan</span>
      <h2>Beoordeeld en geregistreerd</h2>
      <p class="lead">Mijn diploma en registraties zijn vastgelegd bij erkende instanties. Naar de nummers kunt u gerust vragen.</p>
    </div>
    <ul class="creds">
      <li><strong>BHMS</strong><span>Bachelor of Homeopathic Medicine and Surgery, North Gujarat University, India (5,5 jaar)</span></li>
      <li><strong>Nuffic</strong><span>Indiaas diploma beoordeeld voor gebruik in Nederland (diplomawaardering)</span></li>
      <li><strong>NVKH</strong><span>Nederlandse Vereniging van Klassiek Homeopaten. Lid nr. 04-2075</span></li>
      <li><strong>RBCZ</strong><span>Geregistreerd bij RBCZ (Registratie Beroepsbeoefenaren Complementaire Zorg)</span></li>
      <li><strong>CAT</strong><span>CAT BO 76452022-03-23</span></li>
      <li><strong>CCH, India</strong><span>Central Council of Homeopathy, registratie CCH-2402</span></li>
      <li><strong>KvK</strong><span>Kamer van Koophandel nr. 85796700</span></li>
    </ul>
    <div class="partner-logos">
      <img src="{IMG}affiliation5.png" width="1888" height="499" alt="NVKH – Nederlandse Vereniging van Klassiek Homeopaten">
      <img src="{IMG}affiliation6.png" width="180" height="89" alt="RBCZ – Een vrije zorgkeuze">
    </div>
    <div class="note-box" style="margin-top:2rem"><strong>Kwaliteit en klachten:</strong> mijn praktijkvoering wordt vijfjaarlijks beoordeeld aan de hand van de kwaliteitscriteria van RBCZ en de NVKH; de eerste visitatie door de NVKH vond plaats in oktober 2024. Als geregistreerd therapeut val ik onder de onafhankelijke tuchtrechtspraak van TCZ. Voor klachten en geschillen, zie de <a href="klachtenregeling.html">klachtenregeling</a>.</div>
  </div>
</section>

<section class="s-lichen" id="where">
  <div class="wrap">
    <div class="sec-head">
      <h2>Waar ik consulteer</h2>
      <p class="lead">Op afspraak, maandag tot en met vrijdag, 9:00 tot 17:00. Klassieke homeopathie in Uithoorn en Aalsmeer, en online overal in Nederland. Ook handig als u in Mijdrecht, De Kwakel, Kudelstaart, Amstelveen of Hoofddorp woont.</p>
    </div>
    <div class="places">
      <article class="place">
        <h3>Uithoorn</h3>
        <address>Antoon Coolenlaan 41<br>1422 GN Uithoorn</address>
        <p><a href="homeopaat-uithoorn.html">Meer over Uithoorn →</a></p>
        <p><a href="https://www.google.com/maps/search/?api=1&amp;query=Antoon+Coolenlaan+41+1422+GN+Uithoorn" target="_blank" rel="noopener noreferrer">Open in Google Maps ↗</a></p>
        <ul class="tags"><li>Met de auto: parkeren voor de deur</li><li>Openbaar vervoer: tram 25, bus 174</li><li>Niet toegankelijk voor rolstoelgebruikers: de praktijk bevindt zich op de tweede verdieping, bereikbaar via een trap. Een online consult is een alternatief</li></ul>
      </article>
      <article class="place">
        <h3>Aalsmeer</h3>
        <address>Stationsweg 38<br>1431 EG Aalsmeer</address>
        <p><a href="homeopaat-aalsmeer.html">Meer over Aalsmeer →</a></p>
        <p><a href="https://www.google.com/maps/search/?api=1&amp;query=Stationsweg+38+1431+EG+Aalsmeer" target="_blank" rel="noopener noreferrer">Open in Google Maps ↗</a></p>
        <ul class="tags"><li>Openbaar vervoer: bus 340 vanaf Hoofddorp of Uithoorn</li><li>Toegankelijk voor rolstoelgebruikers</li></ul>
      </article>
      <article class="place">
        <h3>Online</h3>
        <address>Google Meet of Zoom,<br>vanaf elke plek ter wereld</address>
        <p>Vervolgconsulten kunnen voor iedereen online. Een eerste consult vanuit het buitenland kan ook online.</p>
        <ul class="tags"><li>Afspraak maken via e-mail, telefoon of WhatsApp</li></ul>
      </article>
    </div>
  </div>
</section>

<section id="rates">
  <div class="wrap narrow">
    <div class="sec-head">
      <h2>Tarieven en vergoeding</h2>
    </div>
    <table class="prices">
      <tbody>
        <tr><th scope="row">Eerste consult<small>Uitgebreide anamnese, ongeveer 90 minuten</small></th><td>€90</td></tr>
        <tr><th scope="row">Vervolgconsult<small>30 tot 60 minuten, in de praktijk of online</small></th><td>€70</td></tr>
        <tr><th scope="row">Acuut consult<small>Voor een nieuwe, kortdurende klacht</small></th><td>€70</td></tr>
        <tr><th scope="row">Buiten kantooruren<small>Spoed, na werktijd</small></th><td>€95</td></tr>
        <tr><th scope="row">Kort telefoongesprek<small>Minder dan 10 minuten</small></th><td>Gratis</td></tr>
      </tbody>
    </table>
    <div style="margin-top:1.6rem">
      <div class="note-box"><strong>Vergoeding:</strong> consulten worden niet vergoed uit de basisverzekering, maar mogelijk wel uit een aanvullende verzekering, afhankelijk van uw polis. Raadpleeg uw polis of vraag het uw zorgverzekeraar voordat u een afspraak maakt. Na elk consult ontvangt u per e-mail een factuur die u kunt indienen bij uw verzekeraar.</div>
      <div class="note-box"><strong>Betaling en annuleren:</strong> pinnen is in de praktijk niet mogelijk; u betaalt per bankoverschrijving op factuur. Annuleer minimaal 24 uur van tevoren, anders kan het consult in rekening worden gebracht. Dit bevestig ik in de e-mail die u bij het maken van de afspraak ontvangt.</div>
    </div>
  </div>
</section>

<section class="s-dark" id="appointment">
  <div class="wrap book">
    <div>
      <h2>Maak een afspraak</h2>
      <p class="lead">Kies de manier die u het beste uitkomt. Ik reageer meestal binnen een werkdag.</p>
      <ul class="contact-list">
        <li><a href="https://wa.me/31645639455" target="_blank" rel="noopener noreferrer"><span class="ci">{WA}</span><span><strong>WhatsApp</strong><small>+31 6 4563 9455</small></span></a></li>
        <li><a href="mailto:info@poojakarnik.com"><span class="ci">{MAIL16}</span><span><strong>E-mail</strong><small>info@poojakarnik.com</small></span></a></li>
        <li><a href="tel:+31645639455"><span class="ci">{PHONE}</span><span><strong>Telefoon</strong><small>+31 6 4563 9455</small></span></a></li>
      </ul>
    </div>
    <form class="book-form" id="book-form" action="https://api.web3forms.com/submit" method="POST">
      <input type="hidden" name="access_key" value="267c9d24-6fc1-41aa-bd3e-c739932ea110">
      <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true">
      <h3>Afspraak aanvragen</h3>
      <label for="f-name">Uw naam</label>
      <input id="f-name" name="name" required autocomplete="name">
      <label for="f-email">Uw e-mailadres</label>
      <input id="f-email" name="email" type="email" required autocomplete="email">
      <label for="f-type">Ik wil graag</label>
      <select id="f-type" name="type">
        <option>Een intakegesprek (algemene informatie)</option>
        <option selected>Een eerste consult</option>
        <option>Een vervolgconsult</option>
      </select>
      <label for="f-mode">Voorkeur voor de afspraak</label>
      <select id="f-mode" name="mode">
        <option>In de praktijk – Uithoorn</option>
        <option>In de praktijk – Aalsmeer</option>
        <option>Online (Google Meet / Zoom)</option>
      </select>
      <label for="f-phone">Telefoonnummer <span style="font-weight:400">(optioneel)</span></label>
      <input id="f-phone" name="phone" type="tel" autocomplete="tel">
      <label for="f-when">Dagen of tijden die u schikken</label>
      <input id="f-when" name="when" placeholder="bijv. dinsdag- of donderdagochtend">
      <label for="f-msg">Wat ik verder moet weten <span style="font-weight:400">(optioneel)</span></label>
      <textarea id="f-msg" name="msg"></textarea>
      <p class="form-hint">Uw aanvraag wordt per e-mail naar mij verstuurd via de formulierdienst Web3Forms (zie de <a href="privacy.html#website">privacyverklaring</a>). Deel hier liever geen uitgebreide medische gegevens; die bespreken we tijdens het consult.</p>
      <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
      <button class="btn btn-primary" type="submit">{MAIL}Verstuur aanvraag</button>
    </form>
  </div>
</section>

<section class="s-white">
  <div class="wrap">
    <p style="margin:0;color:var(--muted)">Niet tevreden? Laat het mij dan eerst weten. Komen we er samen niet uit, zie dan de <a href="klachtenregeling.html">klachtenregeling</a>.</p>
  </div>
</section>

</main>'''
write("nl/index.html", nlpage("home",
  "Klassiek homeopaat in Uithoorn &amp; Aalsmeer | Pooja Karnik",
  "Pooja Karnik, BHMS: klassiek homeopaat in Uithoorn, Aalsmeer en online. 25 jaar ervaring; eerste consult ongeveer 90 minuten.",
  INDEX, "index.html"))

# ---------------------------------------------------------------- ABOUT
ABOUT = f'''<main id="main">
<section class="page-head"><div class="wrap"><h1>Over mij</h1><p>Opleiding, ervaring en beroepsregistraties.</p></div></section>
<section class="s-white">
  <div class="wrap meet">
    <img src="{IMG}pooja_karnik.jpg" width="900" height="1126" alt="Pooja Karnik">
    <div class="prose">
      <h2 style="margin-top:0">Pooja Karnik, BHMS</h2>
      <p>Ik ben klassiek homeopaat met 25 jaar ervaring. Ik heb een BHMS (Bachelor of Homeopathic Medicine and Surgery), een opleiding van 5,5 jaar in India. Mijn diploma is door Nuffic beoordeeld en ik ben geregistreerd bij de Nederlandse beroepsorganisaties voor homeopathie.</p>
      <p>Ik heb mensen van alle leeftijden en nationaliteiten gezien in India, het Verenigd Koninkrijk, de VS en Nederland. Daardoor weet ik hoe verschillend, en hoe persoonlijk, de behoeften van ieder mens zijn.</p>
      <p>Het consult zelf vind ik het belangrijkst. Voor een eerste consult maak ik ongeveer 90 minuten vrij, ik luister naar uw hele verhaal en behandel de mens in plaats van de klachten.</p>
      <ul class="creds creds-compact">
        <li><strong>25 jaar</strong><span>klinische praktijkervaring</span></li>
        <li><strong>BHMS</strong><span>opleiding van 5,5 jaar, India</span></li>
        <li><strong>Nuffic</strong><span>diploma beoordeeld</span></li>
        <li><strong>4 landen</strong><span>India, VK, VS, NL</span></li>
      </ul>
    </div>
  </div>
</section>
<section>
  <div class="wrap narrow prose">
    <span class="eyebrow">Mijn route</span>
    <h2 style="margin-top:0">Opleiding &amp; ervaring</h2>
    <p>Ik voltooide een BHMS (Bachelor of Homeopathic Medicine and Surgery), een opleiding van 5,5 jaar aan de North Gujarat University in Vadodara, India, met homeopathische geneeskunde naast anatomie en fysiologie. Mijn loopbaan begon met een stage onder begeleiding van een ervaren beoefenaar, waar ik anamnese, vervolgconsulten en het dagelijkse ritme van een praktijk leerde.</p>
    <p>Daarna opende ik mijn eigen kliniek in Vadodara en verhuisde ik na een jaar naar Pune, waar ik een gezinspraktijk had voor veel huishoudens.</p>
    <p>In 2017 verhuisde ik naar Nederland. Ik liet mijn diploma beoordelen door Nuffic, registreerde mij bij CAT en NVKH, schreef mijn praktijk in bij de Kamer van Koophandel (KvK) en leerde Nederlands (A2-diploma, nu op weg naar B1). Ook neem ik deel aan Nederlandse werkgroepen voor klassieke homeopathie, waar ik perspectieven vanuit mijn Indiase achtergrond deel.</p>
    <h3>Diplomawaardering en registraties</h3>
    <ul>
      <li>Diploma beoordeeld door Nuffic (Nederland)</li>
      <li>NVKH (Nederlandse Vereniging van Klassiek Homeopaten): 04-2075</li>
      <li>RBCZ (Registratie Beroepsbeoefenaren Complementaire Zorg)</li>
      <li>CAT BO: 76452022-03-23</li>
      <li>Central Council of Homeopathy (India): CCH-2402</li>
      <li>Kamer van Koophandel (KvK): 85796700</li>
    </ul>
    <h3>Kwaliteit</h3>
    <p>Mijn praktijkvoering wordt vijfjaarlijks beoordeeld aan de hand van de kwaliteitscriteria van RBCZ en de NVKH. Als geregistreerd therapeut val ik onder de onafhankelijke tuchtrechtspraak van TCZ.</p>
  </div>
</section>
<section class="s-peach">
  <div class="wrap center narrow">
    <h2>Buiten de praktijk</h2>
    <p class="lead">Ik zet mij in als vrijwilliger in mijn omgeving, van wekelijkse bezoeken aan een verzorgingshuis tot voorlichting over gezondheid en culturele evenementen.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn-ghost" href="../community.html">Mijn vrijwilligerswerk (EN)</a>
      <a class="btn btn-primary" href="index.html#appointment">{CAL3}Maak een afspraak</a>
    </div>
  </div>
</section>

</main>'''
write("nl/about.html", nlpage("about", "Over Pooja Karnik – Klassiek homeopaat in Uithoorn &amp; Aalsmeer",
  "Pooja Karnik, BHMS: klassiek homeopaat met 25 jaar praktijkervaring in India, het Verenigd Koninkrijk, de VS en Nederland. Aangesloten bij NVKH en RBCZ.", ABOUT, "about.html"))

# ---------------------------------------------------------------- HOMEOPATHY
IC1 = f'<svg {SV}><path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14"/><path d="M5 19c2-5 5-8 9-10"/></svg>'
IC2 = f'<svg {SV}><path d="M8 10a4 4 0 1 1 8 0c0 2-2 3-2 5a3 3 0 0 1-6 0"/><path d="M12 10a1.5 1.5 0 0 1 1.5 1.5"/></svg>'
IC3 = f'<svg {SV}><circle cx="9" cy="8" r="3"/><path d="M3 19c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.3"/><path d="M16 13.2c2.8-.3 5 1.7 5 4.8"/></svg>'
IC4 = f'<svg {SV}><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg>'
HOMEO = f'''<main id="main">
<section class="page-head"><div class="wrap"><h1>Over homeopathie</h1><p>Hoe klassieke homeopathie werkt en hoe ik in de praktijk te werk ga.</p></div></section>
<section class="s-white">
  <div class="wrap narrow prose">
    <h2 style="margin-top:0">Wat is homeopathie?</h2>
    <p>Homeopathie is een complementair systeem van gezondheidszorg, ontwikkeld door de Duitse arts Samuel Hahnemann in 1796. Het is gebaseerd op het idee van "gelijke met gelijke" en kijkt naar ieder mens als individu, niet alleen naar een diagnose.</p>
    <p>Twee mensen met dezelfde klacht kunnen daarom een heel verschillend consult hebben, omdat uw eigen ervaring telt: hoe u zich voelt, hoe u slaapt, hoe u op stress reageert en wat uw klachten beter of erger maakt.</p>
    <div class="note-box"><strong>Goed om te weten:</strong> homeopathie is geen vervanging van reguliere zorg. De werking is niet wetenschappelijk bewezen en ik beloof geen resultaten. Ik adviseer u nooit om medicijnen te stoppen of te wijzigen die uw huisarts of specialist heeft voorgeschreven.</div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Hoe ik werk</span><h2>Vier dingen waarop u kunt rekenen</h2></div>
    <div class="grid g2">
      <article class="card"><div class="icon">{IC1}</div><h3>De hele mens</h3><p>Ik kijk naar lichamelijke, emotionele en leefstijlaspecten. Uw klacht maakt deel uit van een groter geheel en ik wil dat hele beeld zien.</p></article>
      <article class="card"><div class="icon">{IC2}</div><h3>Een individuele aanpak</h3><p>Er is geen standaardprogramma. Ons gesprek bepaalt wat we doen, en we evalueren het samen in de loop van de tijd.</p></article>
      <article class="card"><div class="icon">{IC3}</div><h3>Voor elke leeftijd</h3><p>Baby's, kinderen, volwassenen en ouderen zijn welkom, ook tijdens zwangerschap of borstvoeding. Eventuele vragen bespreek ik eerst met u.</p></article>
      <article class="card"><div class="icon">{IC4}</div><h3>Samen met uw huisarts</h3><p>Veel mensen gebruiken homeopathie naast de reguliere zorg. Met uw toestemming houd ik uw huisarts of specialist graag op de hoogte.</p></article>
    </div>
  </div>
</section>
<section class="s-sage">
  <div class="wrap narrow prose">
    <h2 style="margin-top:0">Wat gebeurt er tijdens een consult?</h2>
    <ul>
      <li><strong>Intake:</strong> algemene informatie over de homeopathische methode en mijn werkwijze.</li>
      <li><strong>Eerste consult (ongeveer 90 minuten):</strong> een uitgebreid gesprek waarin ik naar uw hele verhaal luister en kennismaak met u en uw situatie. Neem een lijst mee van de medicijnen die u gebruikt. In Nederland is dit in de praktijk; vanuit het buitenland kan het online.</li>
      <li><strong>Vervolgconsulten (30–60 minuten):</strong> in de praktijk of online, wat het beste uitkomt.</li>
    </ul>
    <p>Uw gegevens worden vertrouwelijk behandeld, zoals beschreven in de <a href="privacy.html">privacyverklaring</a>.</p>
    <div class="btn-row"><a class="btn btn-primary" href="index.html#appointment">{CAL3}Maak een afspraak</a><a class="btn btn-ghost" href="faq.html">Lees de veelgestelde vragen</a></div>
  </div>
</section>

</main>'''
write("nl/homeopathy.html", nlpage("homeo", "Over homeopathie – Pooja Karnik, klassiek homeopaat",
  "Hoe klassieke homeopathie werkt en hoe Pooja Karnik in de praktijk te werk gaat.", HOMEO, "homeopathy.html"))

# ---------------------------------------------------------------- FAQ
QA = [
 ("Wat is klassieke homeopathie?", "Klassieke homeopathie is een complementaire benadering, gegrondvest door Samuel Hahnemann in 1796 en gebaseerd op het idee van \"gelijke met gelijke\". Het kijkt naar de hele mens, dus geen twee consulten zijn hetzelfde."),
 ("Werkt homeopathie?", "Veel mensen waarderen homeopathie en voelen zich erdoor gesteund. De werking is echter niet wetenschappelijk bewezen en ik kan geen bepaalde uitkomst beloven. Ik wil dat u een weloverwogen keuze maakt en praat altijd graag open over wat homeopathie wel en niet kan bieden."),
 ("Kan ik homeopathie combineren met mijn gewone medicijnen?", "Ja, veel mensen doen dat. Blijf de medicijnen gebruiken die uw arts heeft voorgeschreven en stop of wijzig ze nooit zonder overleg met uw huisarts of specialist. Als u dat wilt, houd ik hen met uw toestemming op de hoogte."),
 ("Hoe verloopt een eerste consult?", "Het duurt ongeveer 90 minuten, dus er is tijd om te luisteren. We praten over u: uw gezondheid, uw dagelijks leven, uw slaap, uw emoties en wat u belangrijk vindt. Er is geen druk en geen fout antwoord. Neem een lijst mee van de medicijnen die u gebruikt. Als u liever eerst meer wilt weten over de methode, kunt u beginnen met een intake."),
 ("Waarom krijgen twee mensen met dezelfde klacht een verschillend advies?", "Homeopathie kijkt naar het individu en niet naar het etiket. Uw ervaring, uw geschiedenis en uw manier van reageren zijn allemaal onderdeel van het beeld, en die verschillen per persoon."),
 ("Waarom zitten er soms weken tussen vervolgconsulten?", "Tijd geven hoort bij het proces. Samen met u bepaal ik per geval wanneer we weer afspreken en wat er nodig is."),
 ("Is homeopathie hetzelfde als kruidengeneeskunde?", "Nee. Homeopathie is een zelfstandig systeem van complementaire zorg en verschilt van kruidengeneeskunde in uitgangspunten en bereiding."),
 ("Ziet u ook kinderen?", "Ja, kinderen van alle leeftijden zijn welkom. Ouders zijn een belangrijk deel van het gesprek en ik neem de tijd om de kleintjes op hun gemak te stellen."),
 ("Is een online consult net zo goed als een consult in de praktijk?", "Voor vervolgconsulten werkt online voor de meeste mensen goed. Een eerste consult in Nederland vindt in de praktijk plaats; vanuit het buitenland kan het per videogesprek."),
 ("Wat kost het en wordt het vergoed?", "De tarieven staan op de <a href=\"index.html#rates\">homepage</a>. Consulten worden niet vergoed uit de basisverzekering, maar mogelijk wel uit een aanvullende verzekering, afhankelijk van uw polis. Raadpleeg uw polis of vraag het uw zorgverzekeraar. Na elk consult ontvangt u per e-mail een factuur die u kunt indienen."),
 ("Wat als ik moet annuleren?", "Laat het mij minimaal 24 uur van tevoren weten, anders kan de afspraak in rekening worden gebracht. Zie de <a href=\"algemene-voorwaarden.html\">algemene voorwaarden</a>."),
 ("Wat als ik niet tevreden ben?", "Laat het mij dan eerst weten, zodat we erover kunnen praten. Komen we er samen niet uit, dan kunt u gebruikmaken van de <a href=\"klachtenregeling.html\">klachtenregeling</a>."),
]
details = "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in QA)
FAQ = f'''<main id="main">
<section class="page-head"><div class="wrap"><h1>Veelgestelde vragen</h1><p>Eerlijke antwoorden op de vragen die mensen het vaakst stellen.</p></div></section>
<section class="s-white"><div class="wrap narrow">{details}</div></section>
<section><div class="wrap narrow center"><p class="lead" style="margin-inline:auto">Nog een vraag? <a href="mailto:info@poojakarnik.com">Stuur mij een e-mail</a>; ik help u graag.</p></div></section>

</main>'''
write("nl/faq.html", nlpage("faq", "Veelgestelde vragen – Pooja Karnik, klassiek homeopaat",
  "Antwoorden op veelgestelde vragen over klassieke homeopathie, het eerste consult, kosten, vergoeding en annuleren.", FAQ, "faq.html"))

# ---------------------------------------------------------------- COMPLAINTS
KL = '''<main id="main">
<section class="page-head"><div class="wrap"><h1>Klachtenregeling</h1><p>Wet kwaliteit, klachten en geschillen zorg (Wkkgz)</p></div></section>
<section class="s-white"><div class="wrap narrow prose">
  <h2 style="margin-top:0">Niet tevreden? Laat het mij weten.</h2>
  <p>Ik doe mijn best om u goede zorg te bieden. Bent u ergens niet tevreden over, bijvoorbeeld over een consult, de behandeling of de manier waarop u bent bejegend, bespreek dat dan eerst met mij. Meestal komen we er samen uit. Is het lastig om het mondeling te zeggen, dan kunt u het ook schriftelijk aan mij voorleggen.</p>
  <h3>1. Bespreek het met mij</h3>
  <p>U kunt mij bereiken via <a href="mailto:info@poojakarnik.com">info@poojakarnik.com</a> of telefonisch op <a href="tel:+31645639455">+31 6 4563 9455</a>. Ik ga zorgvuldig met uw klacht om en reageer zo snel mogelijk. Klachten kunnen gaan over de behandeling, de bejegening of de bereikbaarheid.</p>
  <h3>2. Onafhankelijke klachtenfunctionaris</h3>
  <p>Voelt u zich niet in staat uw klacht met mij te bespreken, laat de situatie dit niet toe of komen we er samen niet uit? Dan kunt u kosteloos de onafhankelijke klachtenfunctionaris van <strong>Quasir Expertisecentrum klachtbehandeling</strong> inschakelen. De klachtenfunctionaris ondersteunt u bij het formuleren van uw klacht en bij het onderzoeken van oplossingen, is onafhankelijk en onpartijdig, en uw klacht wordt binnen zes weken afgehandeld. Ik word op de hoogte gesteld dat u een klacht heeft ingediend. U bereikt de klachtenfunctionaris via de NVKH: <a href="https://www.nvkh.nl/contact/ik-heb-een-klacht/" target="_blank" rel="noopener noreferrer">nvkh.nl/contact/ik-heb-een-klacht</a>.</p>
  <p>Wilt u geen klacht indienen maar wel uw onvrede kenbaar maken bij de beroepsvereniging, dan kunt u contact opnemen met het secretariaat van de NVKH via <a href="mailto:info@nvkh.nl">info@nvkh.nl</a> of telefonisch op 0172-499595 (9.00–12.30 uur).</p>
  <h3>3. Geschilleninstantie</h3>
  <p>Wordt uw klacht naar uw mening niet opgelost, dan kan een geschil ontstaan. Conform de Wkkgz zijn alle homeopaten die lid zijn van de NVKH, dus ook ik, aangesloten bij de door de overheid erkende geschilleninstantie <strong>Stichting Zorggeschil</strong>. Volgens de NVKH kost het indienen van een geschil op het moment van schrijven €50 en doet de geschillencommissie binnen zes maanden een bindende uitspraak. Meer informatie: <a href="https://www.zorggeschil.nl" target="_blank" rel="noopener noreferrer">zorggeschil.nl</a>.</p>
  <h3>4. Tuchtrecht</h3>
  <p>Als bij RBCZ geregistreerd therapeut val ik onder de onafhankelijke tuchtrechtspraak van <strong>Tuchtrecht Complementaire Zorg (TCZ)</strong>. Bij een ernstige klacht over mijn handelen kan de klachtenfunctionaris u adviseren uw klacht in te dienen bij TCZ, bij de Inspectie Gezondheidszorg en Jeugd of bij een civiele rechter. Meer informatie: <a href="https://www.tcz.nu" target="_blank" rel="noopener noreferrer">tcz.nu</a>.</p>
</div></section>

</main>'''
write("nl/klachtenregeling.html", nlpage("klacht", "Klachtenregeling | Pooja Karnik, klassiek homeopaat",
  "Klachtenregeling van Pooja Karnik, klassiek homeopaat: klachtenfunctionaris, geschilleninstantie en tuchtrecht.", KL, "klachtenregeling.html"))

# ---------------------------------------------------------------- TERMS
AV = '''<main id="main">
<section class="page-head"><div class="wrap"><h1>Algemene voorwaarden</h1><p>Voorwaarden van de praktijk</p></div></section>
<section class="s-white"><div class="wrap narrow prose">
  <h2 style="margin-top:0">1. Afspraken</h2>
  <p>Consulten vinden uitsluitend op afspraak plaats, maandag tot en met vrijdag van 9:00 tot 17:00, in de praktijk in Uithoorn of Aalsmeer, of online via een videogesprek.</p>
  <h2>2. Annuleren</h2>
  <p>Annuleer of verzet uw afspraak minimaal 24 uur van tevoren. Afspraken die later worden geannuleerd of waarvoor u niet verschijnt, kunnen in rekening worden gebracht. Dit bevestig ik in mijn bevestigingsmail, voorafgaand aan het eerste consult.</p>
  <h2>3. Tarieven en betaling</h2>
  <p>De actuele tarieven staan op de <a href="index.html#rates">homepage</a>. Homeopathische consulten zijn vrijgesteld van btw. Na elk consult ontvangt u per e-mail een factuur, te betalen per bankoverschrijving binnen de vermelde termijn. Pinnen is in de praktijk niet mogelijk.</p>
  <h2>4. Zorgverzekering</h2>
  <p>Consulten worden niet vergoed uit de basisverzekering. Vergoeding via een aanvullende verzekering hangt af van uw polis; het is uw eigen verantwoordelijkheid dit na te gaan. Op de factuur staan de gegevens die uw verzekeraar nodig heeft.</p>
  <h2>5. Complementaire zorg</h2>
  <p>Homeopathische zorg is complementair en vervangt niet de medische zorg van uw huisarts of specialist. Stop of wijzig voorgeschreven medicatie niet zonder overleg met uw arts.</p>
  <h2>6. Uw dossier en vertrouwelijkheid</h2>
  <p>Ik houd een cliëntendossier bij zoals de wet voorschrijft en heb een beroepsgeheim. Zie de <a href="privacy.html">privacyverklaring</a>.</p>
  <h2>7. Klachten</h2>
  <p>Bent u niet tevreden, laat het mij dan eerst weten. Zie de <a href="klachtenregeling.html">klachtenregeling</a> voor de vervolgstappen.</p>
</div></section>
</main>'''
write("nl/algemene-voorwaarden.html", nlpage("av", "Algemene voorwaarden | Pooja Karnik, klassiek homeopaat",
  "Algemene voorwaarden van de praktijk van Pooja Karnik, klassiek homeopaat.", AV, "algemene-voorwaarden.html"))

# ---------------------------------------------------------------- PRIVACY (Dutch section of existing page + Dutch website/cookie text)
src = open(os.path.join(ROOT, "privacy.html")).read()
nl_sec = re.search(r'<h2>Privacyverklaring \(Nederlands\)</h2>(.*?)<hr', src, re.S).group(1)
PRIV = f'''<main id="main">
<section class="page-head"><div class="wrap"><h1>Privacyverklaring</h1><p>Hoe ik met uw gegevens omga</p></div></section>
<section class="s-white"><div class="wrap narrow prose"><h2 style="margin-top:0">Privacyverklaring</h2>{nl_sec}<h3>Uw rechten</h3><p>U heeft het recht uw gegevens in te zien, te laten corrigeren of te laten verwijderen, voor zover de wet dit toestaat. Ik leef de privacyregels van de Algemene Verordening Gegevensbescherming (AVG) na en heb een geheimhoudingsplicht ten aanzien van alle informatie die ik over u verkrijg; die doorbreek ik alleen met een erkende grond, zoals uw toestemming of een wettelijke plicht.</p><hr style="border:0;border-top:1px solid var(--line);margin:2.5rem 0"><h2 id="website">Website, cookies en contact</h2>
<p>Deze website gebruikt geen tracking- of analysecookies en laadt geen lettertypen of kaarten van derden. Video's worden pas van YouTube geladen (in privacyvriendelijke modus) nadat u op afspelen drukt, en kaartlinks openen Google Maps alleen in een nieuw tabblad wanneer u erop klikt.</p>
<p>Het afsprakenformulier verstuurt uw naam, e-mailadres, eventueel telefoonnummer en uw bericht via de formulierdienst <a href="https://web3forms.com" target="_blank" rel="noopener noreferrer">Web3Forms</a>, die het per e-mail aan mij doorstuurt. Web3Forms verwerkt deze gegevens om het bericht te bezorgen en kan het tijdelijk opslaan, zoals beschreven in het <a href="https://web3forms.com/privacy" target="_blank" rel="noopener noreferrer">privacybeleid van Web3Forms</a>. Deel via het formulier daarom geen uitgebreide medische gegevens. Wanneer u mij mailt, belt of een bericht stuurt, gebruik ik uw gegevens alleen om u te antwoorden en uw afspraak te plannen.</p>
<p>U kunt uw rechten uitoefenen via <a href="mailto:info@poojakarnik.com">info@poojakarnik.com</a>. U kunt ook een klacht indienen bij de <a href="https://autoriteitpersoonsgegevens.nl" target="_blank" rel="noopener noreferrer">Autoriteit Persoonsgegevens</a>.</p></div></section>
</main>'''
write("nl/privacy.html", nlpage("privacy", "Privacyverklaring | Pooja Karnik, klassiek homeopaat",
  "Privacyverklaring van de praktijk van Pooja Karnik, klassiek homeopaat.", PRIV, "privacy.html"))
print("NL built")
