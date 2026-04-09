---
type: "braindump"
domain: "professional"
date: "2026-04-08"
created: "2026-04-08 14:26"
themes: ["customer journey", "CX", "Belron", "service model", "enterprise architecture"]
tags: ["#braindump", "#professional", "#customer-journey", "#CX", "#Belron"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-04-09]]"
consolidated_date: "2026-04-09"
energy_level: "medium"
emotional_tone: "investigative"
confidence: "medium"
---

# Braindump: Review Customer Journey Model

## Raw Thoughts
Review customer journey model.

---

## Content Analysis

### What This Means
A customer journey model maps every touchpoint a customer has with the business — from first awareness of a problem to resolution and beyond. For Belron/your company, this spans the full windscreen repair/replace experience: noticing the damage, contacting the company, booking, the technician visit, ADAS calibration, insurance claim, follow-up.

Understanding the customer journey model is foundational EA work — it shows:
- Where value is created (and where it's destroyed)
- Which systems and capabilities support each touchpoint
- Where the gaps and friction points are
- How CCOTF, front-office, and back-office systems connect to actual customer experience

### Questions to Answer
- Does a current customer journey model exist? Where does it live?
- Is it documented at the level of touchpoints, or just at a high level?
- Has it been reviewed recently — does it reflect ADAS calibration as a standard step?
- Who owns the customer journey model — CX team, marketing, operations, EA?
- Are there separate journey maps for repair vs. replace vs. calibration-only?
- Is there a separate journey for insurance customers vs. direct pay?

---

## The Belron Customer Journey (High-Level Draft)

Based on public knowledge of Belron/Autoglass — to be validated against internal documentation.

### Stage 1: Trigger
- Customer notices damage (chip, crack, shattered glass)
- May be stress-inducing, often unplanned
- Channels: direct awareness, insurance company referral, fleet manager notification

### Stage 2: First Contact / Booking
- Online (web/app), phone, or insurance portal
- Repair vs. replace assessment (chip size, crack length, location)
- Appointment scheduling: mobile (technician comes to customer) or branch
- Insurance authorisation (if applicable)

### Stage 3: Pre-Visit
- Confirmation and reminders
- Technician assignment and ETA communications
- Parts ordering / stock check

### Stage 4: The Job
- Technician arrival
- Repair (chip injection) or replacement (full glass swap)
- ADAS recalibration (if vehicle has windscreen-mounted sensors)
- Quality check and sign-off

### Stage 5: Post-Job
- Customer sign-off / satisfaction check
- Invoice / insurance claim submission
- Warranty documentation
- NPS / feedback request

### Stage 6: Retention / Relationship
- Fleet account management (B2B)
- Future service reminders
- Brand relationship (Autoglass / Belron opco)

---

## Strategic Intelligence

### Key Insights

1. **The customer journey is where every system in the business converges.** Booking system, CRM (Salesforce), EBS (ERP/finance), technician dispatch, calibration tools, insurance portals — all touch the journey. Mapping it well reveals which systems serve which steps and where the joins are broken.

2. **ADAS calibration has added a significant new step.** If the customer journey model predates widespread ADAS fitment, it may not reflect the current reality where calibration is now a standard part of most replacements. An outdated journey map is misleading.

3. **Insurance vs. direct pay is likely a fork in the journey.** Insurance customers follow a different path (pre-authorisation, direct billing to insurer) vs. self-pay customers. The model should reflect this explicitly.

4. **This connects directly to the CCOTF work.** The Contact Centre of the Future touches Stage 2 (first contact/booking) and Stage 3 (pre-visit communications) most directly. Understanding the customer journey shows what CCOTF needs to do and where front-office capabilities are required.

---

## Action Items

### Immediate (24–48 hours)
- [ ] Find the existing customer journey model — check intranet, CX team, or strategy documents 📅 2026-04-10
- [ ] If found: assess whether it includes ADAS calibration as a standard step 📅 2026-04-10
- [ ] If not found: note the gap — the absence of a documented journey model is itself an architectural finding 📅 2026-04-10

### Short-term (1–2 weeks)
- [ ] Validate the draft journey above against internal knowledge or with a CX/operations stakeholder 📅 2026-04-17
- [ ] Identify which systems support each stage — this becomes a system-to-journey map 📅 2026-04-17
- [ ] Note where the CCOTF capability fits in the journey — which stages does it own or influence? 📅 2026-04-18

### Strategic Considerations
- A validated customer journey map + a system map overlaid on it is a very powerful EA artefact — it shows leadership exactly where technology enables or impedes the customer experience
- Consider whether a journey map review should be a standing EA output — updated annually or when significant service changes are made (e.g., ADAS calibration becoming standard)

---

## Connections
- **Related braindump:** [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]] — CCOTF owns key stages of this journey; the capability overlap is visible in the journey map
- **Related braindump:** [[braindump-2026-04-08-1123-getting-closer-to-belron-business]] — the customer journey *is* how the business works, seen from the customer's perspective
- **Related braindump:** [[braindump-2026-04-08-1125-value-chains-and-wardley-mapping]] — Porter's value chain and the customer journey map are two views of the same thing
- **Related braindump:** [[braindump-2026-04-08-1352-ebs-salesforce]] — Salesforce and EBS both touch the journey; the integration points map to journey stages

## Domain Classification
- **Primary Domain:** Professional (99%)
- **Privacy Level:** private

## Processing Notes
### Confidence Assessment
- **Overall Analysis:** 85%
- **Draft journey model:** 78% — based on public Belron/Autoglass information; needs validation against internal documentation
- **Areas requiring clarification:** Does an internal journey model already exist? How mature is it?

---

*Processed by COG Braindump Analyst*
