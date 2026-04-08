---
type: "braindump"
domain: "professional"
date: "2026-04-08"
created: "2026-04-08 14:36"
themes: ["Belron", "software development", "systems delivery", "operating model", "EA artefact", "build vs buy"]
tags: ["#braindump", "#professional", "#Belron", "#software-delivery", "#systems", "#EA-artefact"]
status: "captured"
energy_level: "high"
emotional_tone: "purposeful"
confidence: "medium"
---

# Braindump: Analyse Belron's Software Development & Systems Model

## Raw Thoughts
Analyse the way Belron develops software and systems - build a model for myself - so I can show interested parties etc.

---

## What This Is

A deliberate EA artefact-building exercise. The goal: understand and document *how Belron actually builds, buys, and delivers software and systems* — not just what systems exist, but the processes, governance, decision-making, and delivery model behind them. Then shape that understanding into something communicable to interested parties (leadership, stakeholders, new team members, opco partners).

This is both a learning exercise and a visibility opportunity.

---

## The Model — Dimensions to Understand and Map

### 1. Build vs Buy Philosophy
*How does Belron decide whether to build custom software or buy a packaged solution?*

- Is there an explicit build/buy/partner policy, or is it decided case by case?
- Which categories tend toward buy (e.g. ERP, CRM, HR) vs build (e.g. booking systems, calibration tools, fleet management)?
- Who makes build/buy decisions — central IT, opco, product team, EA?
- **Wardley lens:** Where do Belron's systems sit on the Genesis → Commodity axis? (From this morning's braindump — this is the right tool to map this)

### 2. Central vs Opco Delivery Model
*How does software development work across the Belron group vs within individual opcos (Autoglass, Carglass, Safelite, etc.)?*

- Does Belron have a central technology function that builds platforms used by all opcos?
- Or do opcos build their own systems independently?
- Or a hybrid — central platforms with opco customisation?
- Who owns the roadmap for shared platforms?
- How are opco-specific requirements handled?

### 3. Delivery Methodology
*How does Belron actually build software when it chooses to build?*

- Agile, waterfall, SAFe, or something else?
- Product teams or project teams?
- In-house engineers or outsourced development (and to whom)?
- Where are the development teams based?
- How are releases managed — continuous delivery, release trains, waterfall drops?

### 4. Key Systems Landscape
*What are the major systems in play and how do they relate?*

Categories to map:
- **CRM:** Salesforce? Other?
- **ERP / Finance:** Oracle EBS? SAP? Other?
- **Booking & Scheduling:** Proprietary? Off-the-shelf?
- **Technician / Field Service:** How are jobs dispatched, tracked, and completed?
- **ADAS Calibration:** What systems support calibration workflow and documentation?
- **Insurance Portal Integration:** How do insurers connect to the booking/claims process?
- **Customer Comms:** Contact centre platform, IVR, digital channels
- **Reporting / BI:** How is data surfaced for decision-making?

### 5. Governance and Architecture Decision-Making
*How are technology decisions made and governed?*

- Is there an Architecture Review Board (ARB) or equivalent?
- How are technology standards set — centrally, or per opco?
- What is the EA function's role in the delivery lifecycle — advisory, mandatory review, sign-off?
- How are cross-opco dependencies managed?

### 6. Integration Architecture
*How do systems talk to each other?*

- Is there a middleware/integration platform (MuleSoft, Azure Integration Services, etc.)?
- Is there an API strategy — REST, event-driven, both?
- How do opco systems integrate with central platforms?
- What is the data architecture — single source of truth, federated, duplicated?

### 7. Innovation and Emerging Technology
*How does Belron evaluate and adopt new technology?*

- Is there a formal innovation process or lab?
- How did ADAS calibration capability get built — central programme or opco-led?
- Where does AI fit — is there a strategy, pilots, production deployments?
- How does Belron track technologies like A2A, MCP, agentic AI? (From this morning's research)

---

## The Deliverable — What "The Model" Looks Like

The output is not a document — it's a communicable *view* that can be shown to different audiences. Different audiences need different versions:

| Audience | What They Need | Format |
|---|---|---|
| Leadership / exec | Strategic picture — are we building the right things, the right way? | One-page diagram + narrative |
| New team members / opco partners | How does technology work at Belron? | Explainer document or deck |
| Technical stakeholders | Detailed system landscape + integration model | Architecture diagram |
| EA peers | Governance model + decision rights | Capability/RACI model |

**Start with one version: the one-page strategic picture.** It forces the most important choices about what to include, and it's the most useful for leadership conversations.

---

## Strategic Intelligence

### Key Insights

1. **This model doesn't exist in a communicable form yet — which is the gap.** Most companies have some version of this knowledge in people's heads and scattered documents. Making it explicit and shareable is significant EA work.

2. **The model is a forcing function for the Belron business understanding goal.** You can't build this without talking to the people who know. Every conversation needed to fill a gap in this model is a stakeholder engagement. This connects directly to the stakeholder visibility and business proximity braindumps from this morning.

3. **A Wardley Map of the Belron systems landscape is a natural output of this work.** Once you know what systems exist and what they do, mapping them on Genesis → Commodity reveals where Belron is over-investing in commodity capabilities and under-investing in differentiating ones.

4. **This is a foundation for everything else.** The CCOTF capability overlap, the Salesforce/EBS integration question, the customer journey system map — all of them require this model as context. Building it once and maintaining it pays dividends across every EA conversation.

---

## How to Build It

### Phase 1 — Desk Research (1–2 weeks)
- [ ] Gather existing architecture documentation from the intranet or EA team 📅 2026-04-15
- [ ] Find any existing systems landscape diagrams — even outdated ones are a starting point 📅 2026-04-15
- [ ] Review John Prodgers' DLD presentations for relevant systems context 📅 2026-04-11
- [ ] Review the customer journey model (once found) and map which systems support each stage 📅 2026-04-17

### Phase 2 — Stakeholder Interviews (2–4 weeks)
- [ ] Identify 4–5 people who collectively know the most about how Belron builds systems — CTO/CIO level, senior developers, delivery managers, opco tech leads 📅 2026-04-18
- [ ] Conduct structured 30-minute conversations: "Help me understand how we build and deliver software" 📅 2026-04-25
- [ ] Specifically ask about: build/buy decisions, central vs opco model, key systems, integration approach, governance

### Phase 3 — Draft the Model (1 week)
- [ ] Synthesise desk research and interviews into a draft one-page view 📅 2026-04-30
- [ ] Share draft with 1–2 stakeholders for validation: "Does this match your understanding?" 📅 2026-05-05

### Phase 4 — Socialise (ongoing)
- [ ] Share with manager/sponsor as a conversation piece 📅 2026-05-07
- [ ] Offer as an onboarding resource for new team members
- [ ] Keep it live — update when systems change or new programmes launch

---

## Connections
- **Related braindump:** [[braindump-2026-04-08-1125-value-chains-and-wardley-mapping]] — Wardley Map of the Belron systems landscape is the natural EA output
- **Related braindump:** [[braindump-2026-04-08-1123-getting-closer-to-belron-business]] — building this model requires business proximity; the interviews are the bridge
- **Related braindump:** [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]] — this model provides the context that makes CCOTF/front-office overlap resolvable
- **Related braindump:** [[braindump-2026-04-08-1352-ebs-salesforce]] — EBS/Salesforce integration is one dimension of this model
- **Related braindump:** [[braindump-2026-04-08-1426-review-customer-journey-model]] — customer journey system map is an output of this work
- **Related braindump:** [[braindump-2026-04-08-0937-passive-to-active-stakeholder-visibility]] — the interviews needed are exactly the stakeholder rotation in action

## Domain Classification
- **Primary Domain:** Professional (99%)
- **Privacy Level:** private

## Processing Notes
### Confidence Assessment
- **Overall Analysis:** 85%
- **Model dimensions:** 88% — standard EA framework applied to Belron context; comprehensive coverage
- **Belron-specific content:** 60% — the dimensions are right but the answers are unknown until research is done; this is a research plan as much as a braindump

---

*Processed by COG Braindump Analyst*
