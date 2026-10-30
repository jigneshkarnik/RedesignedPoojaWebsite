import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_common import *

def alts(f):  # (en url, nl url) relative to site root, used for hreflang
    return f, "nl/" + f

# ---------------------------------------------------------------- HOME
INDEX_MAIN = f'''<main id="main">

<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1><span>Pooja Karnik, BHMS · Classical homeopath in Uithoorn and Aalsmeer</span>Listening first, then treatment for the whole person.</h1>
      <p class="lead">Your first consultation lasts about 90 minutes, so that your complaints, your history and your daily life can all be heard. Trained in India (BHMS, a 5.5-year degree), diploma validated by Nuffic, registered with NVKH, RBCZ and CAT. Consultations in Uithoorn, Aalsmeer and online.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="#appointment">{CAL}Book a consultation</a>
        <a class="btn btn-ghost" href="#credentials">Qualifications and registrations</a>
      </div>
    </div>
    <figure class="plate">
      <div class="plate-img"><img src="images/pooja_karnik.jpg" width="900" height="1126" alt="Pooja Karnik, classical homeopath, wearing an orange sari"></div>
      <figcaption><strong>Pooja Karnik, BHMS</strong>Classical homeopath. Member of NVKH, registered with RBCZ and CAT.</figcaption>
    </figure>
  </div>
</section>

<div class="register">
  <dl class="wrap">
    <div class="reg-item"><dt>Experience</dt><dd>25 years<small>In clinical homeopathic practice</small></dd></div>
    <div class="reg-item"><dt>Degree</dt><dd>BHMS, India<small>Bachelor of Homeopathic Medicine and Surgery, a 5.5-year course. Diploma validated by Nuffic</small></dd></div>
    <div class="reg-item"><dt>Patients in</dt><dd>4 countries<small>India, the UK, the US and the Netherlands</small></dd></div>
    <div class="reg-item"><dt>Registered with</dt><dd>NVKH, RBCZ, CAT<small>And the Central Council of Homeopathy, India</small></dd></div>
  </dl>
</div>

<section id="method" class="s-white">
  <div class="wrap method">
    <div>
      <span class="eyebrow">My approach</span>
      <h2>The work begins with the case history</h2>
      <p class="lead">I take the time to hear your whole story, and I treat the person, not only the symptoms.</p>
      <p>Classical homeopathy asks for a full picture before any prescription is made. That is why the first consultation is long, and why I never use a standard programme.</p>
      <p><a class="btn btn-ghost" href="homeopathy.html">How homeopathy works</a></p>
    </div>
    <ul class="method-list">
      <li><h3>Listening</h3><p>The first consultation takes about 90 minutes. We go through your complaints, sleep, digestion, energy, emotions, stress and family history, at your own pace.</p></li>
      <li><h3>The whole person</h3><p>I look at the physical, emotional and lifestyle picture together, not at the symptoms in isolation. Two people with the same diagnosis can receive different prescriptions.</p></li>
      <li><h3>A considered prescription</h3><p>After the consultation I study your case and choose a remedy and potency, with clear instructions on how to take it.</p></li>
      <li><h3>Review and follow-up</h3><p>At each follow-up we look at your response and adjust the prescription as needed.</p></li>
      <li><h3>Alongside your GP</h3><p>Homeopathy is complementary. I encourage you to stay under the care of your GP or specialist and, with your consent, I will keep them informed. I see people of all ages, including those who are pregnant or breastfeeding.</p></li>
      <li><h3>Experience across cultures</h3><p>Twenty-five years of practice in India, the UK, the US and the Netherlands has shown me how differently people experience and describe illness.</p></li>
    </ul>
  </div>
</section>

<section id="expect" class="s-dark">
  <div class="wrap">
    <div class="sec-head">
      <h2>Your consultation, step by step</h2>
      <p class="lead">You can start with a short intake, or go straight to a first consultation.</p>
    </div>
    <ol class="steps">
      <li><h3>Intake</h3><span class="dur">Short, no obligation</span><p>An introduction to classical homeopathy and to how I work, so you can decide whether it suits you.</p></li>
      <li><h3>First consultation</h3><span class="dur">About 90 minutes</span><p>A detailed case history and a physical and emotional overview. Please bring a list of any medication you take. In the Netherlands this is in person; from abroad it can be online.</p></li>
      <li><h3>Prescription</h3><span class="dur">After the consultation</span><p>I study your case and choose a remedy and potency, with instructions on how to take it.</p></li>
      <li><h3>Follow-up</h3><span class="dur">30 to 60 minutes</span><p>We review your response and adjust the prescription. In my practice or by video call.</p></li>
    </ol>
  </div>
</section>

<section id="training">
  <div class="wrap career">
    <div>
      <span class="eyebrow">Education and career</span>
      <h2>Trained in India, validated and registered in the Netherlands</h2>
      <p>I completed a 5.5-year Bachelor of Homeopathic Medicine and Surgery (BHMS) at North Gujarat University, alongside anatomy and physiology. I then ran my own clinic and a family practice, caring for households of all ages and backgrounds.</p>
      <p>Since 2017 I have lived in the Netherlands. My Indian diploma was assessed and validated through Nuffic, the Dutch organisation for diploma recognition, and I practise as a registered classical homeopath.</p>
      <p style="margin-top:1.6rem"><a class="btn btn-ghost" href="about.html">Full background</a></p>
    </div>
    <ol class="timeline">
      <li><strong>BHMS, North Gujarat University</strong><span>5.5-year degree in Homeopathic Medicine and Surgery, Vadodara</span></li>
      <li><strong>Internship</strong><span>Case-taking, follow-up and daily practice under an experienced practitioner</span></li>
      <li><strong>Own clinic, Vadodara</strong><span>Clinic owner</span></li>
      <li><strong>Family practice, Pune</strong><span>Care for many households, across all ages</span></li>
      <li><strong>2017: the Netherlands</strong><span>Diploma validated by Nuffic. Registered with NVKH, CAT and the Chamber of Commerce.</span></li>
      <li><strong>Today</strong><span>25 years of experience, with patients in India, the UK, the US and the Netherlands</span></li>
    </ol>
  </div>
</section>

<section class="s-white" id="credentials">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Qualifications you can check</span>
      <h2>Validated and registered</h2>
      <p class="lead">My degree and registrations are held with recognised bodies, with numbers you can ask me about.</p>
    </div>
    <ul class="creds">
      <li><strong>BHMS</strong><span>Bachelor of Homeopathic Medicine and Surgery, North Gujarat University, India (5.5 years)</span></li>
      <li><strong>Nuffic</strong><span>Indian diploma assessed and validated for use in the Netherlands</span></li>
      <li><strong>NVKH</strong><span>Nederlandse Vereniging van Klassiek Homeopaten. Member no. 04-2075</span></li>
      <li><strong>RBCZ</strong><span>Registered with RBCZ (Registratie Beroepsbeoefenaren Complementaire Zorg)</span></li>
      <li><strong>CAT</strong><span>CAT BO 76452022-03-23</span></li>
      <li><strong>CCH, India</strong><span>Central Council of Homeopathy, registration CCH-2402</span></li>
      <li><strong>KvK</strong><span>Chamber of Commerce no. 85796700</span></li>
    </ul>
    <div class="partner-logos">
      <img src="images/affiliation5.png" alt="NVKH – Nederlandse Vereniging van Klassiek Homeopaten">
      <img src="images/affiliation6.png" alt="RBCZ – Een vrije zorgkeuze">
    </div>
    <div class="note-box" style="margin-top:2rem"><strong>Quality and complaints:</strong> my practice is reviewed every five years against the quality criteria of RBCZ and NVKH; the first NVKH practice visit took place in October 2024. As a registered therapist I fall under the independent disciplinary law (<em>tuchtrecht</em>) of TCZ. For complaints and disputes, see the <a href="klachtenregeling.html">complaints procedure</a>.</div>
  </div>
</section>

<section class="s-lichen" id="where">
  <div class="wrap">
    <div class="sec-head">
      <h2>Where to consult</h2>
      <p class="lead">By appointment, Monday to Friday, 9:00 to 17:00. Classical homeopathy in Uithoorn and Aalsmeer, and online anywhere in the Netherlands. Also convenient if you live in Mijdrecht, De Kwakel, Kudelstaart, Amstelveen or Hoofddorp.</p>
    </div>
    <div class="places">
      <article class="place">
        <h3>Uithoorn</h3>
        <address>Antoon Coolenlaan 41<br>1422 GN Uithoorn</address>
        <p><a href="https://www.google.com/maps/search/?api=1&amp;query=Antoon+Coolenlaan+41+1422+GN+Uithoorn" target="_blank" rel="noopener noreferrer">Open in Google Maps ↗</a></p>
        <ul class="tags"><li>By car: parking in front of the house</li><li>Public transport: tram 25, bus 174</li><li>Not accessible for wheelchair users: the practice is on the second floor, reached by stairs. An online consultation is an alternative</li></ul>
      </article>
      <article class="place">
        <h3>Aalsmeer</h3>
        <address>Stationsweg 38<br>1431 EG Aalsmeer</address>
        <p><a href="https://www.google.com/maps/search/?api=1&amp;query=Stationsweg+38+1431+EG+Aalsmeer" target="_blank" rel="noopener noreferrer">Open in Google Maps ↗</a></p>
        <ul class="tags"><li>Public transport: bus 340 from Hoofdorp or Uithoorn</li><li>Wheelchair accessible</li></ul>
      </article>
      <article class="place">
        <h3>Online</h3>
        <address>Google Meet or Zoom,<br>from anywhere in the world</address>
        <p>Follow-ups can be online for everyone. A first consultation from outside the Netherlands can also be online.</p>
        <ul class="tags"><li>Book by email, phone or WhatsApp</li></ul>
      </article>
    </div>
  </div>
</section>

<section id="rates">
  <div class="wrap narrow">
    <div class="sec-head">
      <h2>Fees and reimbursement</h2>
    </div>
    <table class="prices">
      <tbody>
        <tr><th scope="row">First consultation<small>Detailed case history, about 90 minutes</small></th><td>€70</td></tr>
        <tr><th scope="row">Follow-up consultation<small>30 to 60 minutes, in person or online</small></th><td>€50</td></tr>
        <tr><th scope="row">Acute consultation<small>For a new, short-term concern</small></th><td>€50</td></tr>
        <tr><th scope="row">Outside office hours<small>Urgent, after hours</small></th><td>€75</td></tr>
        <tr><th scope="row">Short phone call<small>Under 10 minutes</small></th><td>Free</td></tr>
      </tbody>
    </table>
    <div style="margin-top:1.6rem">
      <div class="note-box"><strong>Insurance:</strong> consultations are not reimbursed from the basic insurance (<em>basisverzekering</em>), but may be reimbursed under a supplementary insurance (<em>aanvullende verzekering</em>), depending on your policy. Please check your policy or ask your insurer before you book. After each consultation you receive an invoice by email that you can submit to your insurer.</div>
      <div class="note-box"><strong>Payment and cancellation:</strong> card payment (PIN) is not available at the practice; payment is by bank transfer on invoice. Please cancel at least 24 hours in advance, otherwise the consultation may be charged. I confirm this in the email I send you when you book.</div>
    </div>
  </div>
</section>

<section class="s-dark" id="appointment">
  <div class="wrap book">
    <div>
      <h2>Book a consultation</h2>
      <p class="lead">Choose whichever way is easiest. I usually reply within a working day.</p>
      <ul class="contact-list">
        <li><a href="https://wa.me/31645639455" target="_blank" rel="noopener noreferrer"><span class="ci">{WA}</span><span><strong>WhatsApp</strong><small>+31 6 4563 9455</small></span></a></li>
        <li><a href="mailto:info@poojakarnik.com"><span class="ci">{MAIL16}</span><span><strong>Email</strong><small>info@poojakarnik.com</small></span></a></li>
        <li><a href="tel:+31645639455"><span class="ci">{PHONE}</span><span><strong>Phone</strong><small>+31 6 4563 9455</small></span></a></li>
      </ul>
    </div>
    <form class="book-form" id="book-form" action="https://api.web3forms.com/submit" method="POST">
      <input type="hidden" name="access_key" value="267c9d24-6fc1-41aa-bd3e-c739932ea110">
      <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true">
      <h3>Request an appointment</h3>
      <label for="f-name">Your name</label>
      <input id="f-name" name="name" required autocomplete="name">
      <label for="f-email">Your email address</label>
      <input id="f-email" name="email" type="email" required autocomplete="email">
      <label for="f-type">I would like</label>
      <select id="f-type" name="type">
        <option>An intake (general information)</option>
        <option selected>A first consultation</option>
        <option>A follow-up consultation</option>
      </select>
      <label for="f-mode">Preferred way to meet</label>
      <select id="f-mode" name="mode">
        <option>In person – Uithoorn</option>
        <option>In person – Aalsmeer</option>
        <option>Online (Google Meet / Zoom)</option>
      </select>
      <label for="f-phone">Phone number <span style="font-weight:400">(optional)</span></label>
      <input id="f-phone" name="phone" type="tel" autocomplete="tel">
      <label for="f-when">Days or times that suit you</label>
      <input id="f-when" name="when" placeholder="e.g. Tuesday or Thursday mornings">
      <label for="f-msg">Anything you'd like me to know <span style="font-weight:400">(optional)</span></label>
      <textarea id="f-msg" name="msg"></textarea>
      <p class="form-hint">Your request is sent to me by email through the form service Web3Forms (see the <a href="privacy.html#website">privacy statement</a>). Please don't share detailed medical information here; we'll go through that in the consultation.</p>
      <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
      <button class="btn btn-primary" type="submit">{MAIL}Send request</button>
    </form>
  </div>
</section>

<section class="s-white">
  <div class="wrap">
    <p style="margin:0;color:var(--muted)">Not satisfied? Please tell me first. If we can't resolve it together, see the <a href="klachtenregeling.html">complaints procedure</a>.</p>
  </div>
</section>

</main>'''

write("index.html", page("en","home",
  "Classical Homeopath in Uithoorn &amp; Aalsmeer | Pooja Karnik",
  "Pooja Karnik, BHMS: classical homeopath in Uithoorn and Aalsmeer, and online across the Netherlands. 25 years of experience, first consultation about 90 minutes. Registered with NVKH, RBCZ and CAT.",
  INDEX_MAIN, "index.html", "nl/index.html", "nl/index.html"))

# ---------------------------------------------------------------- ABOUT
ABOUT_MAIN = '''<main id="main">
<section class="page-head"><div class="wrap"><h1>About me</h1><p>Education, experience and professional registrations.</p></div></section>
<section class="s-white">
  <div class="wrap meet">
    <img src="images/pooja_karnik.jpg" width="900" height="1126" alt="Pooja Karnik">
    <div class="prose">
      <h2 style="margin-top:0">Pooja Karnik, BHMS</h2>
      <p>I am a classical homeopath with 25 years of experience. I hold a BHMS (Bachelor of Homeopathic Medicine and Surgery), a 5.5-year course in India. My diploma has been validated by Nuffic, and I am registered with the Dutch professional bodies for homeopathy.</p>
      <p>I have consulted people of all ages and nationalities in India, the UK, the US and the Netherlands. That has taught me how different, and how personal, every person's needs are.</p>
      <p>What I care about most is the consultation itself. I set aside about 90 minutes for a first consultation, listen to your whole story, and treat the person rather than the symptoms.</p>
      <ul class="creds creds-compact">
        <li><strong>25 years</strong><span>of clinical practice</span></li>
        <li><strong>BHMS</strong><span>5.5-year course, India</span></li>
        <li><strong>Nuffic</strong><span>diploma validated</span></li>
        <li><strong>4 countries</strong><span>India, UK, US, NL</span></li>
      </ul>
    </div>
  </div>
</section>
<section>
  <div class="wrap narrow prose">
    <span class="eyebrow">My journey</span>
    <h2 style="margin-top:0">Education &amp; experience</h2>
    <p>I completed a BHMS (Bachelor of Homeopathic Medicine and Surgery), a 5.5-year course at North Gujarat University in Vadodara, India, covering homeopathic medicine alongside anatomy and physiology. I began my career with an internship under an experienced practitioner, where I learned case-taking, follow-up and the daily rhythm of a practice.</p>
    <p>I then opened my own clinic in Vadodara and, after a year, moved to Pune, where I ran a family practice for many households.</p>
    <p>In 2017 I moved to the Netherlands. I had my diploma assessed and validated through Nuffic, registered with CAT and NVKH, registered my practice with the Chamber of Commerce (KvK), and learned Dutch (A2 diploma, now working towards B1). I also take part in Dutch working groups for classical homeopathy, sharing perspectives from my Indian background.</p>
    <h3>Validation and registrations</h3>
    <ul>
      <li>Diploma validated by Nuffic (Netherlands)</li>
      <li>NVKH (Nederlandse Vereniging van Klassiek Homeopaten): 04-2075</li>
      <li>RBCZ (Registratie Beroepsbeoefenaren Complementaire Zorg)</li>
      <li>CAT BO: 76452022-03-23</li>
      <li>Central Council of Homeopathy (India): CCH-2402</li>
      <li>Chamber of Commerce (KvK): 85796700</li>
    </ul>
    <h3>Quality</h3>
    <p>My practice is reviewed every five years against the quality criteria of RBCZ and NVKH. As a registered therapist I fall under the independent disciplinary law (<em>tuchtrecht</em>) of TCZ.</p>
  </div>
</section>
<section class="s-peach">
  <div class="wrap center narrow">
    <h2>Beyond the practice</h2>
    <p class="lead">I volunteer in my local community, from weekly visits at an elderly care home to health-awareness talks and cultural events.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn-ghost" href="community.html">My community work</a>
      <a class="btn btn-primary" href="index.html#appointment">''' + CAL3 + '''Book an appointment</a>
    </div>
  </div>
</section>

</main>'''
write("about.html", page("en","about",
  "About Pooja Karnik – Classical Homeopath in Uithoorn &amp; Aalsmeer",
  "Pooja Karnik, BHMS (India): classical homeopath with 25 years of practice in India, the UK, the US and the Netherlands. Diploma validated by Nuffic. Registered with NVKH, RBCZ and CAT. Practising in Uithoorn and Aalsmeer.",
  ABOUT_MAIN, "about.html", "nl/about.html", "nl/about.html"))

# ---------------------------------------------------------------- HOMEOPATHY (edit existing)
m = old_main("homeopathy.html")
m = (m.replace("about 1.5 hours", "about 90 minutes")
      .replace("Working with your doctor", "Working with your GP")
      .replace("I never advise you to stop or change medication prescribed by your doctor.", "I never advise you to stop or change medication prescribed by your doctor or specialist.")
      .replace("a detailed conversation in which I get to know you and your situation.", "a detailed conversation in which I listen to your whole story and get to know you and your situation. Please bring a list of any medication you take."))
t, d = old_meta("homeopathy.html")
write("homeopathy.html", page("en","homeo", t, d, m, "homeopathy.html", "nl/homeopathy.html", "nl/homeopathy.html"))

# ---------------------------------------------------------------- FAQ
m = old_main("faq.html")
m = (m.replace("It takes about 1.5 hours.", "It takes about 90 minutes.")
      .replace("It takes about 90 minutes. We talk about you:", "It takes about 90 minutes, so there is time to listen. We talk about you:")
      .replace("Rates are on the <a href=\"index.html#rates\">home page</a>.", "Rates are on the <a href=\"index.html#rates\">home page</a>.")
      .replace("Homeopathic consultations are not covered by the basic insurance. Some supplementary insurers reimburse part of the cost, depending on your policy, so please check with your insurer.", "Consultations are not reimbursed from the basic insurance, but may be reimbursed under a supplementary insurance, depending on your policy. Please check your policy or ask your insurer."))
t, d = old_meta("faq.html")
write("faq.html", page("en","faq", t, d, m, "faq.html", "nl/faq.html", "nl/faq.html"))

# ---------------------------------------------------------------- unchanged-content pages (new shell only)
for f, key in (("sessions.html","sessions"),("articles.html","articles"),("community.html","community")):
    t, d = old_meta(f)
    write(f, page("en", key, t, d, old_main(f), f, "nl/index.html", "nl/index.html"))

# ---------------------------------------------------------------- PRIVACY (EN page keeps its Dutch section)
m = old_main("privacy.html")
t, d = old_meta("privacy.html")
write("privacy.html", page("en","privacy", t, d, m, "privacy.html", "nl/privacy.html", "nl/privacy.html"))

# ---------------------------------------------------------------- COMPLAINTS
KL = '''<main id="main">
<section class="page-head"><div class="wrap"><h1>Klachtenregeling</h1><p>Complaints procedure (Wet kwaliteit, klachten en geschillen zorg – Wkkgz)</p></div></section>
<section class="s-white"><div class="wrap narrow prose">
  <h2 style="margin-top:0">Not satisfied? Please tell me.</h2>
  <p>I do my best to give you good care. If you are not satisfied with a consultation, with the treatment or with how you were treated, please talk to me first. Most of the time we can find a solution together. If it is difficult to say it in person, you can also put it in writing.</p>
  <h3>1. Talk to me</h3>
  <p>Contact me by email at <a href="mailto:info@poojakarnik.com">info@poojakarnik.com</a> or by phone on <a href="tel:+31645639455">+31 6 4563 9455</a>. I will respond to your complaint carefully and as soon as possible. Complaints can be about the treatment, the way you were treated, or accessibility.</p>
  <h3>2. Independent complaints officer</h3>
  <p>If you do not feel able to discuss your complaint with me, or we cannot resolve it together, you can contact the independent complaints officer (<em>klachtenfunctionaris</em>) of <strong>Quasir Expertisecentrum klachtbehandeling</strong>, free of charge. The complaints officer supports you in formulating your complaint and in looking for solutions, is independent and impartial, and your complaint is handled within six weeks. I will be informed that you have made a complaint. You can reach the complaints officer through the NVKH: <a href="https://www.nvkh.nl/contact/ik-heb-een-klacht/" target="_blank" rel="noopener noreferrer">nvkh.nl/contact/ik-heb-een-klacht</a>.</p>
  <p>If you do not wish to file a complaint but would like to share your dissatisfaction with my professional association, you can contact the NVKH secretariat at <a href="mailto:info@nvkh.nl">info@nvkh.nl</a> or by phone on 0172-499595 (9:00–12:30).</p>
  <h3>3. Disputes body</h3>
  <p>If you feel your complaint has not been resolved, a dispute can arise. In accordance with the Wkkgz, all homeopaths who are members of the NVKH, including me, are affiliated with the government-recognised disputes body <strong>Stichting Zorggeschil</strong> (<em>geschilleninstantie</em>). According to the NVKH, submitting a dispute costs €50 at the time of writing, and the disputes committee gives a binding ruling within six months. More information: <a href="https://www.zorggeschil.nl" target="_blank" rel="noopener noreferrer">zorggeschil.nl</a>.</p>
  <h3>4. Disciplinary law</h3>
  <p>As an RBCZ-registered therapist I fall under the independent disciplinary law (<em>tuchtrecht</em>) of <strong>Tuchtrecht Complementaire Zorg (TCZ)</strong>. In case of a serious complaint about my actions, the complaints officer may advise you to submit it to TCZ, to the Dutch Healthcare Inspectorate (<em>Inspectie Gezondheidszorg en Jeugd</em>) or to a civil court. More information: <a href="https://www.tcz.nu" target="_blank" rel="noopener noreferrer">tcz.nu</a>.</p>
</div></section>

</main>'''
write("klachtenregeling.html", page("en","klacht",
  "Klachtenregeling – Complaints procedure | Pooja Karnik",
  "Complaints procedure of Pooja Karnik, classical homeopath: complaints officer, disputes body and disciplinary law.",
  KL, "klachtenregeling.html", "nl/klachtenregeling.html", "nl/klachtenregeling.html"))

# ---------------------------------------------------------------- TERMS
m = old_main("algemene-voorwaarden.html")
m = m.replace("Appointments cancelled later, or missed, may be charged in full.", "Appointments cancelled later, or missed, may be charged. I confirm this in my appointment confirmation email, before your first consultation.")
t, d = old_meta("algemene-voorwaarden.html")
write("algemene-voorwaarden.html", page("en","av", t, d, m, "algemene-voorwaarden.html", "nl/algemene-voorwaarden.html", "nl/algemene-voorwaarden.html"))
print("EN built")
