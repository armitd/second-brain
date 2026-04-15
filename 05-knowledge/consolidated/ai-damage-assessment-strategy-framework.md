---
type: "consolidated-knowledge"
domain: "professional"
framework: "ai-damage-assessment-strategy"
created: "2026-04-10"
last_updated: "2026-04-15"
consolidation_id: "consolidation-2026-04-15"
source_documents: 8
status: "emerging"
tags: ["#framework", "#consolidated", "#damage-assessment", "#computer-vision", "#AI", "#build-vs-buy", "#Belron"]
---

# AI Damage Assessment Strategy Framework

## Framework Overview
A decision framework for how Belron should approach AI-powered damage assessment — covering the strategic question (build/buy/partner), the vendor landscape by layer, the prototype path, and the build window argument.

**Status:** Emerging (market intelligence gathered; strategic decision point not yet reached)
**Last Updated:** 2026-04-10
**Source Insights:** 5 documents — market scan braindump (Apr 9), competitive watchlist, daily briefs Apr 9–10

---

## The Opportunity

A customer photographs windscreen damage → AI assesses it → instant repair/replace recommendation → seamless booking. This is the AI damage assessment use case. In 2026:

- **The market is real and moving fast.** Tractable reached $1B valuation. Ravin AI expanded to the US. Audatex/Solera are embedded in insurer workflows. The competitive landscape is forming now.
- **The technology is ready for prototyping today.** Foundation models (GPT-4o, Gemini) can analyse damage photos without training data — a working prototype is an afternoon's work.
- **The build window is open but closing.** Custom models will commoditise by 2028–2029. The advantage accrues to organisations that build first and own their training data. Waiting means buying someone else's solution.

---

## The Strategic Question (Answer This First)

Everything else — vendor selection, architecture, data strategy — flows from one question:

| If the answer is... | Then the strategy is... |
|---|---|
| **Own the IP and data** | Build from scratch — custom CV model, proprietary training data. Highest cost, highest strategic value |
| **Own the customer experience but not the AI** | API into an existing model (Tractable, Ravin, or foundation model fine-tune). Faster, less differentiated |
| **Differentiate end-to-end** | Build the front-end and UX; buy or fine-tune the CV model. Best balance of speed and ownership |
| **Move fast, prove the concept** | Foundation model prototype first — then decide which path based on results |

**Recommended default sequence:** Foundation model prototype → validate the use case → then choose the strategic path. Never invest in custom model training before a prototype validates the approach.

---

## The Six-Layer Architecture

Building a custom AI damage assessment solution requires thinking in layers. Each layer has its own vendor market, risks, and quality gates.

```
┌─────────────────────────────────────────────┐
│  Layer 6: Customer-Facing App (web/mobile)  │  ← UX design + mobile engineering
├─────────────────────────────────────────────┤
│  Layer 5: API / Backend                     │  ← Image routing, confidence scoring, CRM integration
├─────────────────────────────────────────────┤
│  Layer 4: AI/CV Model (inference)           │  ← MLOps + deployment
├─────────────────────────────────────────────┤
│  Layer 3: AI/CV Model (training)            │  ← ML engineering consultancy
├─────────────────────────────────────────────┤
│  Layer 2: Training Data (labelled images)   │  ← Data annotation platform/service
├─────────────────────────────────────────────┤
│  Layer 1: Cloud Infrastructure              │  ← AWS / Azure / GCP
└─────────────────────────────────────────────┘
```

**The critical insight:** Most organisations underestimate Layers 2–3. Training data is the hardest part, not the model. High-quality labelled images of real damage, across severities, devices, lighting conditions, and glass types, takes months and significant investment. This is where most AI projects fail.

---

## Core Principles

### Principle 1: Foundation Model First — Custom Model Only If Needed

**Statement:** In 2026, a multimodal foundation model (GPT-4o or Gemini 3.1 Pro) can assess windscreen damage from a photo with no training data required. This is the fastest path to a working prototype. Only invest in custom model training if the prototype reveals clear gaps that fine-tuning or a custom model would close.

**Evidence:**
- [[braindump-2026-04-09-1136-market-scan-machine-vision-frontend]] — "The fastest and cheapest route to a working damage assessment prototype is probably a multimodal foundation model... A custom model will outperform at scale and with domain-specific tuning — but the prototype should prove the concept first"
- [[daily-brief-2026-04-09-pm]] — "Gemini 3.1 Pro dominates multimodal and image analysis (Video-MME 78.2%); for damage assessment, start with Gemini or GPT-5.4 for structured JSON output"
- [[daily-brief-2026-04-10]] — Anthropic compute backed by Google/Broadcom 3.5GW commitment; API availability improving

**Prototype test:** Take 5 real photos of windscreen damage. Submit to Gemini 3.1 Pro and GPT-5.4 with a prompt asking for structured JSON output (damage type, severity, recommendation: repair/replace, confidence score). If the output is useful, the use case is validated.

**Confidence:** High

---

### Principle 2: Training Data Is the Strategic Asset, Not the Model

**Statement:** The model is a commodity that will improve and cheapen year by year. The labelled dataset of real Belron customer damage — in real conditions, on real devices — is proprietary IP that does not depreciate. Design the data strategy as a long-term asset from day one.

**Evidence:**
- [[braindump-2026-04-09-1136-market-scan-machine-vision-frontend]] — "The labelled image dataset built during this project becomes proprietary IP... This is valuable beyond the first use case. Design the data strategy with future use cases in mind"
- [[competitive-watchlist]] — Ravin AI built their market position on 2 billion processed vehicle images. The data moat is real.
- [[braindump-2026-04-09-1136-market-scan-machine-vision-frontend]] — "A damage assessment model needs thousands of labelled images across damage types, severities, lighting conditions, and devices. Getting this data takes months and significant investment"

**How to apply:** From the first prototype, collect and label images. Even before a custom model is trained, build the dataset. The annotation work can run in parallel with prototyping.

**Privacy note:** UK/EU GDPR applies to customer photos — vehicles may contain licence plates. Data residency and anonymisation must be scoped before any external annotation partner handles images.

**Confidence:** High

---

### Principle 3: Camera UX Is a Product Problem, Not a Technical One

**Statement:** The quality of AI output is only as good as the input image. Poor photos (wrong angle, bad lighting, too far) defeat even a well-trained model. Designing the guided camera experience — teaching customers how to photograph their damage — is the highest-leverage UX challenge in this product.

**Evidence:**
- [[braindump-2026-04-09-1136-market-scan-machine-vision-frontend]] — "Studios like ustwo or Futurice are better suited to this than engineering-first shops... The camera guidance experience is a product design problem as much as an engineering problem"
- Ravin AI's competitive advantage is partly its hardware-agnostic capture approach — standard CCTV + mobile photos, guided well
- [[braindump-2026-04-09-1136-market-scan-machine-vision-frontend]] — "Mobile-first, camera integration, real-time feedback, progressive disclosure, accessibility"

**How to apply:** Any vendor selection for the front-end must include assessment of mobile camera UX experience. Ask specifically: show me a photo guidance flow you've built.

**Confidence:** High

---

### Principle 4: Build in Confidence Scoring From Day One

**Statement:** A damage assessment AI must know when it doesn't know. Low-confidence assessments must route to human review — not auto-approve or auto-reject. Confidence scoring is an architectural requirement, not a nice-to-have.

**Evidence:**
- [[braindump-2026-04-09-1136-market-scan-machine-vision-frontend]] — "Should include a confidence scoring mechanism — low-confidence assessments should route to human review, not auto-approve"
- [[competitive-watchlist]] — Mind Foundry cited as a vendor with "calibrated confidence scores" as a core capability — "directly relevant to damage assessment where low-confidence results should route to human review"
- [[daily-brief-2026-04-10]] — EU AI Act requires auditability and explainability — confidence scoring supports both

**How to apply:** Define confidence thresholds before prototype: above X% = auto-approve recommendation; below X% = route to agent/technician review. Test prototype outputs against these thresholds.

**Confidence:** High

---

## The Competitive Landscape

### Existing Solutions (Buy/Partner Option)

| Company | What They Do | Relevance | Notes |
|---|---|---|---|
| **Tractable** | AI for accident/vehicle damage assessment. $1B valuation. Used by insurers globally | Very high — adjacent market | Already in insurer ecosystem that touches Belron customers |
| **Ravin AI** | AI vehicle inspection platform. 2B images processed. Hardware-agnostic | High — direct reference architecture | US MSO pilot underway; IAG-backed; no proprietary hardware |
| **Audatex / Solera** | Automotive claims AI embedded in insurer workflows | High — may already be in Belron's value chain | Most important to check: do Belron insurance partners already use this? |

**The key question before committing to custom build:** Do any of Belron's major insurance referral partners already use Tractable, Ravin, or Audatex/Solera for their own damage assessment? If yes, the argument becomes partnership + integration, not build.

### Build Partners (Custom Build Option)

**For the model layer:**
- **Faculty AI** (UK) — Best UK ML consultancy for computer vision at enterprise scale
- **Datatonic** (UK, GCP specialist) — Best choice if Belron is GCP-first; Gemini expertise
- **Roke** (UK) — Deep CV capability, security-conscious approach to data
- **Mind Foundry** (Oxford spin-out) — Academic rigour + confidence scoring expertise

**For the data annotation layer:**
- **Encord** (UK) — Best fit: UK-headquartered, strong in inspection use cases, GDPR-friendly
- **Scale AI** — Market leader but US-based; data residency questions apply

**For the front-end layer:**
- **ustwo** (London) — Best consumer-facing mobile UX
- **Futurice** (UK/Finland) — Strong in mobile + ML together; European = GDPR-aligned
- **Zühlke** (UK/Switzerland) — Engineering + UX + regulated industry experience

---

## The Wardley Lens

Mapping damage assessment layers on the evolution axis:

| Layer | Evolution Stage | Implication |
|---|---|---|
| Cloud infrastructure (AWS/Azure/GCP) | Commodity | Buy — don't build your own cloud |
| Foundation model APIs (GPT-4o, Gemini) | Product → Commodity | Use for prototype; plan to own fine-tuned model later |
| Customer front-end app | Product | Partner or buy — commodity UX capability available |
| Custom damage assessment CV model | Custom → Product | Build now — differentiating; will commoditise by 2028 |
| Proprietary training data | Genesis | Build and own — this is the lasting competitive asset |

The build window for a differentiating custom model is **2026–2027.** After that, fine-tuned foundation models will do what custom-trained CV models do today — at a fraction of the cost and time.

---

## Applications & Use Cases

### Use Case 1: Foundation Model Prototype (Week 1)
**Objective:** Validate the concept. Costs nothing except time.

**Steps:**
1. Take 5–10 real photos of windscreen damage across repair/replace cases
2. Submit to Gemini 3.1 Pro and GPT-5.4 with structured prompt: "Analyse this windscreen photo. Return JSON: {damage_type, severity, recommendation: repair|replace|unclear, confidence: 0-100, reason}"
3. Compare outputs against known correct answers
4. If accuracy is >70% on repair vs. replace, the use case is validated

**Decision gate:** >70% = proceed to strategic path decision. <70% = investigate whether prompt engineering or additional context improves it.

### Use Case 2: Strategic Path Decision Briefing
**Objective:** Get leadership alignment on build/partner/buy before any investment

**Format:** One-page briefing — opportunity, three paths (build/partner/buy), recommendation, decision needed
**Audience:** Senior sponsor / CTO equivalent

### Use Case 3: Data Strategy Design
**Objective:** Define how training data will be collected, labelled, stored, and governed

**Key decisions:**
- Which jobs generate images suitable for labelling? (All replacements? Specific damage types?)
- Internal labelling (technicians label their own jobs?) vs. external annotation partner
- Data residency: UK/EU only for GDPR compliance
- Ownership: ensure contractual clarity that Belron owns all labelled data

---

## Boundaries & Limitations

**This framework works when:**
- The organisation controls the customer interaction point where photos are taken
- There is appetite to invest in data collection as a multi-year programme
- Regulatory environment for customer data handling is understood and compliant

**This framework does NOT work when:**
- The insurance partner controls the damage assessment process (then it's a partnership conversation)
- Time-to-market pressure is very high (6 months) — buy/partner is faster
- Budget for data annotation is unavailable — no data = no custom model

---

## Evolution & History

### April 9, 2026: Market Scan
Full six-layer vendor ecosystem mapped. Key insight: building from scratch means owning the problem in layers. The strategic question (build/buy/partner) was identified as the single most important decision.

**Source:** [[braindump-2026-04-09-1136-market-scan-machine-vision-frontend]]

### April 9, 2026 (PM): Competitive Intelligence
Tractable reached $1B; Ravin AI entering US collision market with hardware-agnostic architecture; Gemini 3.1 Pro confirmed as strongest image analysis model. Foundation model prototype validated as fastest first step.

**Sources:** [[daily-brief-2026-04-09-pm]], [[competitive-watchlist]]

### April 10, 2026: Competitive Signals
Ravin AI confirmed piloting with US MSO; IAG-backed; 2B images processed. Anti-China AI coalition tightening frontier model API access — strengthens case for open-source/EU model (LLaMA, Mistral) for data-sensitive use cases.

**Source:** [[daily-brief-2026-04-10]]

### April 14–15, 2026: Edge Deployment Now Practical + Gemma 4 as Privacy-Safe Option

**Two new signals that materially update the foundation model strategy:**

**1. Gemma 4 ships — runs on-device on low-power hardware.**
Google's Gemma 4 is confirmed with a "runs locally on low-power devices" capability. For the damage assessment use case, this means a technician's tablet in a van is no longer an aspirational edge deployment — it is technically feasible today. On-device inference eliminates the cloud round-trip latency and, critically, means customer vehicle photos (which contain personal data — licence plates, location context) are assessed locally without leaving the device. This directly addresses the GDPR data residency concern in Principle 2.

**2. Local AI has crossed the practicality threshold.**
Multiple sources confirm that autonomous agents are running on consumer hardware (Mac M-series, mid-range PCs) with performance matching frontier API calls. The enabling factor: open-weights models at frontier capability. For Belron, the "technician using their own device in a van" scenario is no longer speculative.

**Updated Principle 1 implication:** The prototype sequence is now: (1) cloud foundation model (GPT-4o / Gemini) to validate the use case → (2) Gemma 4 local prototype to validate on-device performance and privacy compliance → (3) custom fine-tuned model only if Gemma 4 performance is insufficient. This adds an intermediate step that may eliminate the need for a custom model entirely.

**ARC-AGI-3 context:** All frontier AI models scored below 1% on the new ARC-AGI-3 benchmark, which tests novel reasoning. For damage assessment (a well-defined, repetitive classification task within training distribution), this is not a concern — the task does not require novel reasoning. It is reassuring confirmation that the use case is appropriate for current AI capability.

**Sources:** [[daily-brief-2026-04-14-post]], [[daily-brief-2026-04-15]]

---

## Related Frameworks

- [[belron-business-understanding-framework]] — Customer journey Stage 2 (booking/assessment) is the entry point for this use case
- [[agentic-ai-governance-framework]] — A damage assessment flow is a candidate multi-agent pipeline (assessment agent → booking agent → dispatch agent)
- [[ea-effectiveness-framework]] — This is a dual-purpose artefact: strategic analysis AND the basis for a high-visibility EA presentation to leadership

---

## Future Development

**Immediate actions:**
- [ ] Run the foundation model prototype — 5 photos, Gemini 3.1 Pro vs GPT-5.4, structured JSON output 📅 2026-04-11
- [ ] Research which Belron insurance partners already use Tractable/Ravin/Audatex 📅 2026-04-17
- [ ] Answer the strategic question: own IP → build; own UX → buy/API; differentiate end-to-end → hybrid 📅 2026-04-17

**Questions to resolve:**
- What is Belron's cloud platform? (Azure/GCP/AWS — this determines which foundation model API is most compliant)
- Do any insurance partners already use an AI damage assessment tool in their claims workflow?
- Is there internal momentum for a damage assessment initiative, or is this an EA-proposed idea needing a sponsor?

---

*Consolidated from 5 sources | First version: April 10, 2026 | Status: Emerging*
