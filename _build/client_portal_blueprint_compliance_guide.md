# Client Records & Portal: Decision Guide and Compliance Blueprint (NL)

Status: draft v2, 2026-10-30. Replaces the earlier Gemini draft. Not legal advice; confirm points marked **[verify]** with NVKH/RBCZ or a privacy adviser.

This file lives in `_build/` so GitHub Pages does not publish it. Never move it to the site root.

## 1. Decision first: buy or build

Pooja is a solo practitioner. A custom medical-records system carries the liability for data loss, breaches, patching, backups and key management. **Default recommendation: buy a practice system, build nothing.** Build only if no vendor passes section 3.

| Option | What it is | Rough cost [verify, from vendor-side blogs] | Notes |
|---|---|---|---|
| EviCare | Practice software for complementary therapists (NL) | from about €23.50/month excl. VAT, one-off €75 setup | Closest fit by target group |
| Praktijkflow | Practice software, EU servers (Frankfurt), follows NEN 7510 principles (not certified) | about €19/month (Starter) | Check Starter has records and client portal |
| inEPD | EPD for paramedics, states NEN 7510 certificate | about €29/month | Aimed at paramedics; check fit |
| Custom build (section 5) | Own portal on a VPS | VPS about €5/month plus a lot of maintenance time | Highest risk, only if needed |

No option found at about €10/month. Realistic floor is €19 to €30/month. Prices must be confirmed on the vendors' own sites.

The need may also be smaller than a full portal. If the goal is only intake forms or secure document exchange, a records system plus its intake feature may be enough, and the website keeps its current Web3Forms booking form.

## 2. Legal framework (summary)

- **AVG (GDPR):** health data is special-category data (art. 9). Legal basis for treatment records: art. 9(2)(h) with professional secrecy, plus UAVG art. 30. **[verify]**
- **WGBO (Book 7 BW, art. 7:446 ff.):** the treatment file (art. 7:454) must be kept 20 years. The patient has the right of access and copy (7:456) and may ask for destruction (7:455), with limited exceptions.
- **UAVG art. 46:** the BSN may only be used where a law allows it. Not needed for this practice; do not collect it. Invoices never carry it (see site CLAUDE.md).
- **NEN 7510 / 7512 / 7513:** information-security norms for care providers. 7513 covers logging of access to patient records. The Dutch Data Protection Authority (AP) expects care providers to follow them; they are not themselves statutes.
- **Also needed:** processing register, DPIA (recommended for health data), data-breach procedure (notify the AP within 72 hours when required), processing agreement with every processor, privacy statement kept in sync with reality.

## 3. Requirements any solution must meet (vendor checklist)

Ask the vendor for written confirmation of each:

1. Signed processing agreement (verwerkersovereenkomst); data stored in the EU/EEA; list of sub-processors.
2. Current NEN 7510 certificate with validity date, or a clear statement of what they do instead.
3. Encryption in transit and at rest; vendor staff access to content documented.
4. Two-factor login for the practitioner; for patients if a portal exists.
5. Access log of who viewed or changed a record (NEN 7513 style), kept by the vendor.
6. Retention: records can be kept 20 years, and a single record can be destroyed on request.
7. Export of the full file in a usable format (patient copy and exit from the vendor); data returned or deleted at contract end.
8. Backups and restore; breach notification duty to Pooja.
9. Dutch-language interface or support is useful; Dutch invoice support (code 24200, AGB, RBCZ/NVKH numbers per site CLAUDE.md) is a plus.
10. Patient-facing parts (intake form, portal) work without third-party trackers, or the privacy statement names them.

## 4. What the record must contain

Whether bought or built, the file should cover:

1. **Client details:** name, date of birth, contact details, GP details if given. No BSN.
2. **Consent and agreements:** consent to treatment and to record keeping, acknowledgement of terms including the cancellation fee (see site CLAUDE.md rule 6), date.
3. **Consultation notes:** the case-taking record (about 90 minutes at the first consultation), follow-ups, the treatment plan and remedies given.
4. **Medication and health information reported by the patient**, including the medication list asked for before the first consultation.
5. **Documents** supplied by the patient or by other care providers.
6. **Invoices and payment status** (invoice content per site CLAUDE.md rule 8).
7. **Access log** (system-generated, not editable by users).

Remedy names are allowed inside the private record. The rule against naming remedies applies to public website text, which counts as advertising.

Wording: use "practitioner" or "classical homeopath". Never "doctor" or "Dr".

## 5. Custom build blueprint (only if buying fails)

### 5.1 Architecture

- **Frontend:** static JS app served from the **same host as the API** (not GitHub Pages), on a subdomain such as `portal.poojakarnik.com`. GitHub Pages cannot send HSTS, X-Frame-Options or `frame-ancestors`, and a compromised page there would expose keys. Serve with a strict CSP and security headers via Caddy or nginx.
- **Backend:** one small service on an EU VPS (Hetzner, Germany or Finland) with encrypted disk. Pick one stack before starting (PocketBase or a small Node API). PocketBase was pre-1.0 at last check, so confirm stability and its MFA support **[verify]**.
- **Cookies:** session in an httpOnly, Secure, SameSite cookie on the same site. No tokens in `localStorage`. Functional cookies must be named in the privacy statement.
- **Operations:** OS patching, automatic encrypted off-site backups, tested restores, uptime and log monitoring, fail2ban or equivalent. The admin signs a confidentiality agreement and the processing agreement covers Hetzner.

### 5.2 Encryption (client-side, envelope model)

- Each record gets its own random 256-bit AES-GCM **data key**, 96-bit random IV per encryption, record ID bound in as additional authenticated data.
- The data key is **wrapped separately** for each party allowed to read it: the practitioner and, if the portal is used, the patient. A patient token alone cannot decrypt anything.
- Practitioner key: derived from a passphrase (PBKDF2-SHA256 at 600,000 iterations or more, or Argon2 via WASM) and/or a passkey (WebAuthn). **Mandatory offline recovery key** (printed, stored in a safe by the owner), because losing the key loses every record and breaks the 20-year duty.
- **Crypto-shredding:** deleting a record's wrapped keys destroys it, which supports the patient's destruction right.
- Server-visible metadata (record ID, patient ID, timestamps, sizes) is still personal data and is covered by the processing agreement. "Server sees only ciphertext" applies to content only.
- Encryption protects against server theft, not against XSS or a malicious script served to the browser; hence the CSP and same-host serving above.

### 5.3 Authentication and access

- **Practitioner:** passkey or password plus TOTP; short sessions; re-authenticate for export and delete.
- **Patient:** email plus password plus TOTP or passkey; account creation by invitation; recovery only after identity check by Pooja. A paper or email alternative remains available, and the portal is optional.
- **Rights requests:** access and copy within one month, identity verified. The portal supports this but does not replace the process.

### 5.4 Audit log

- Fields: timestamp, actor ID, action (view, create, edit, export, delete, login success/failure), record ID. Patient access is logged too.
- Tamper-evident: hash-chained entries or append-only storage, with the chain head backed up off the server.
- IP addresses: truncate or omit. Hashing alone is not protective.
- Retention period for logs to be decided and written into the privacy statement.

## 6. Website changes when any solution goes live

- Update the privacy statement (EN `privacy.html`, NL via `_build/build_nl.py`, anchor `#website` and the records section): processor name, location, purpose, retention (20 years), rights, security. Keep EN and NL in sync.
- If the website itself talks to a new origin (custom build or embedded vendor form): add it to both `CSP` in `build_common.py` and `_headers`, and remove "no third-party requests" claims.
- Booking confirmation email must still state the cancellation fee (site CLAUDE.md rule 6).
- Record the processor and DPIA in the processing register.

## 7. Open decisions

1. Buy or build (recommended: buy). Shortlist EviCare, Praktijkflow, inEPD; request the section 3 answers and a processing agreement from each.
2. Is a patient portal required, or only intake and document exchange?
3. Who holds the offline recovery key and who is the VPS admin (build option only).
4. Whether to commission a short DPIA review from a privacy adviser.
