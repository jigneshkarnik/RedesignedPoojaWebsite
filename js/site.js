// Mobile menu, scroll reveal, click-to-load videos and the appointment-request form.
// Nothing here sets cookies. The only third-party contacts are the YouTube player after a click
// and the Web3Forms service when an appointment request is sent.
document.documentElement.classList.add('js');

// Clickjacking defence for hosts that cannot send X-Frame-Options / frame-ancestors.
if (window.top !== window.self) { try { window.top.location = window.self.location; } catch (e) { document.documentElement.style.display = 'none'; } }

(function () {
  var btn = document.getElementById('menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Privacy-friendly video: the YouTube player only loads after a click.
  document.querySelectorAll('.video[data-yt]').forEach(function (box) {
    var b = box.querySelector('button');
    b.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + box.getAttribute('data-yt') + '?autoplay=1';
      f.title = box.getAttribute('data-title') || 'Video';
      f.allow = 'autoplay; encrypted-media; picture-in-picture';
      f.allowFullscreen = true;
      box.innerHTML = '';
      box.appendChild(f);
    });
  });

  // Appointment request: sent by email to info@poojakarnik.com through Web3Forms.
  // Without JavaScript the form still posts to the same address (see the form's action).
  var form = document.getElementById('book-form');
  if (form) {
    var nl = document.documentElement.lang === 'nl';
    var status = document.getElementById('form-status');
    var submit = form.querySelector('button[type="submit"]');
    var text = nl ? {
      sending: 'Bezig met verzenden…',
      ok: 'Bedankt. Uw aanvraag is verstuurd. Ik reageer meestal binnen een werkdag.',
      err: 'Helaas is uw aanvraag niet verstuurd. Mail naar info@poojakarnik.com of bel +31 6 4563 9455.',
      subject: 'Afspraakaanvraag - '
    } : {
      sending: 'Sending…',
      ok: 'Thank you. Your request has been sent. I usually reply within a working day.',
      err: 'Sorry, your request could not be sent. Please email info@poojakarnik.com or call +31 6 4563 9455.',
      subject: 'Appointment request - '
    };
    function say(msg, cls) { status.textContent = msg; status.className = 'form-status' + (cls ? ' ' + cls : ''); }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var lines = nl ? [
        'Naam: ' + d.get('name'),
        'E-mailadres: ' + d.get('email'),
        'Type afspraak: ' + d.get('type'),
        'Voorkeur voor de afspraak: ' + d.get('mode'),
        'Telefoon (optioneel): ' + (d.get('phone') || '-'),
        'Voorkeursdagen/-tijden: ' + (d.get('when') || '-'), '',
        (d.get('msg') || '')
      ] : [
        'Name: ' + d.get('name'),
        'Email: ' + d.get('email'),
        'Appointment type: ' + d.get('type'),
        'Preferred way to meet: ' + d.get('mode'),
        'Phone (optional): ' + (d.get('phone') || '-'),
        'Preferred days/times: ' + (d.get('when') || '-'), '',
        (d.get('msg') || '')
      ];
      var payload = {
        access_key: d.get('access_key'),
        botcheck: d.get('botcheck') ? 'on' : '',
        subject: text.subject + d.get('name'),
        from_name: 'poojakarnik.com',
        name: d.get('name'),
        email: d.get('email'),
        message: lines.join('\n')
      };
      submit.disabled = true;
      say(text.sending);
      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(payload)
      }).then(function (r) { return r.json(); }).then(function (j) {
        if (j && j.success) { form.reset(); say(text.ok, 'ok'); }
        else { say(text.err, 'err'); }
      }).catch(function () { say(text.err, 'err'); })
        .then(function () { submit.disabled = false; });
    });
  }
})();
