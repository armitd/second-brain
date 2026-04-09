---
type: "consolidated-knowledge"
domain: "professional"
framework: "belron-business-understanding"
created: "2026-04-09"
last_updated: "2026-04-09"
consolidation_id: "consolidation-2026-04-09"
source_documents: 8
status: "emerging"
tags: ["#framework", "#consolidated", "#Belron", "#business-understanding", "#EA", "#value-chain", "#Wardley"]
---

# Belron Business Understanding Framework

## Framework Overview
A structured approach to building deep knowledge of how Belron operates — moving from strategic tools (Porter, Wardley) through the customer journey to the systems landscape and capability map. Designed specifically for an EA practitioner who needs to build credibility and decision-making ability grounded in operational reality.

**Status:** Emerging (approach defined; execution begins April 2026)
**Last Updated:** 2026-04-09
**Source Insights:** 8 documents — braindumps on getting closer to Belron, value chains + Wardley, customer journey, CCOTF overlap, software delivery model, EBS/Salesforce, Salesforce packages, John Prodgers DLD

---

## Why This Matters

The most common failure mode in enterprise architecture is producing technically correct recommendations that the business doesn't adopt — because the architect didn't understand the business well enough to frame them in terms that landed. An EA who speaks fluently about booking conversion rates, technician utilisation, and insurance partnership dynamics is taken seriously in a way a purely technical architect is not.

**Business acumen compounds.** Every hour spent understanding how Belron actually operates makes every subsequent EA decision sharper, every stakeholder conversation richer, and every artefact more credible.

---

## The Five Layers of Understanding

Build these layers in sequence. Each layer informs the next.

---

### Layer 1: Strategic Value Creation (Porter's Value Chain)

**Purpose:** Understand *what* the business does and where value is created — independent of who does it, how it's structured, or what systems support it.

**The Belron Value Chain (draft — to be validated):**

**Primary Activities:**
1. **Inbound Logistics** — glass, adhesives, and parts arriving at fitting centres and technician vans
2. **Operations** — the technician repairing or replacing the windscreen (this happens at the customer's location — the "outbound logistics" model is inverted for a mobile service business)
3. **Outbound Logistics** — technician dispatch; the van going to the customer
4. **Marketing & Sales** — insurance partnerships, direct booking channels, fleet account management, brand (Autoglass UK, Carglass Europe, Safelite USA)
5. **Service** — ADAS calibration, warranty, customer satisfaction, NPS, fleet renewal

**Support Activities:**
- Firm Infrastructure — finance, legal, management, EA (your function sits here)
- HRM — technician recruitment, training, upskilling (particularly ADAS)
- Technology Development — booking systems, calibration equipment, scheduling tools
- Procurement — glass supply chain, adhesives, calibration equipment

**The key insight for Belron:** The Operations step happens *at the customer's location*. This inverts the typical value chain — outbound logistics is not getting the product to the customer; it is *the service delivery itself*. The technician is simultaneously the operations step and the outbound logistics step. Every system decision needs to account for this mobile-first delivery model.

**Source:** [[braindump-2026-04-08-1125-value-chains-and-wardley-mapping]]

---

### Layer 2: Strategic Positioning (Wardley Mapping)

**Purpose:** Understand *where* Belron's capabilities sit on the evolution axis — which are differentiating (invest), which are commodity (minimise cost), and which are emerging (watch or invest now).

**Belron Capability Wardley Map (draft):**

| Capability | Visibility | Evolution Stage | Implication |
|---|---|---|---|
| Technician repair skill | High (customer-facing) | Custom → Product | Core — invest in training and quality |
| ADAS calibration | High (customer-facing) | Custom (moving to Product) | Growing differentiator — build now, before it commoditises |
| Insurance partnership management | High | Product | Maintain; this is how most customers arrive |
| Customer booking experience | Mid | Product | Buy, don't build — unless differentiation is possible |
| Technician dispatch / scheduling | Mid | Product → Commodity | Optimise; AI scheduling is the emerging edge |
| Glass supply chain | Low | Commodity | Minimise cost; standard suppliers |
| CRM (Salesforce) | Mid | Product → Commodity | Buy; customise carefully |
| ERP / Finance (EBS or equivalent) | Low | Commodity | Buy and integrate; never build |
| AI agents / agentic workflow | Mid | Genesis → Custom | Early-stage differentiator — watch and invest selectively |

**The strategic insight:** Belron should be investing heavily in ADAS calibration capability (still custom, becoming more valuable as vehicle fleet evolves) and exploring AI scheduling optimisation (Genesis stage — early mover advantage available). It should be buying commodity capabilities (ERP, CRM, cloud infrastructure) and not customising them beyond necessity.

**Source:** [[braindump-2026-04-08-1125-value-chains-and-wardley-mapping]]

---

### Layer 3: Customer Experience (Customer Journey Map)

**Purpose:** Understand how the business looks from the customer's perspective — which systems, capabilities, and people touch each stage of the experience.

**The Belron Customer Journey (draft — needs internal validation):**

| Stage | What Happens | Systems Involved | Key Capabilities |
|---|---|---|---|
| 1. Trigger | Customer notices damage — chip, crack, shattered | — | Brand awareness, insurance partner relationships |
| 2. First Contact & Booking | Web, phone, insurance portal. Repair vs. replace assessment. Scheduling. | CRM (Salesforce), booking system, insurance portals | Booking, insurance authorisation, assessment |
| 3. Pre-Visit | Confirmation, reminders, tech assignment, parts check | Scheduling, comms platform, parts/inventory | Dispatch, customer comms, parts management |
| 4. The Job | Technician arrival, repair or replace, ADAS calibration, quality check | Calibration tools, field service app | Technical repair, ADAS calibration, quality assurance |
| 5. Post-Job | Sign-off, invoice/insurance claim, warranty, NPS | CRM (Salesforce), EBS/finance, claims system | Claims processing, warranty, customer satisfaction |
| 6. Retention | Fleet account management, service reminders | CRM, marketing platform | Account management, relationship maintenance |

**Two critical forks to map explicitly:**
- **Insurance vs. direct pay:** Insurance customers follow a different path (pre-authorisation, direct billing to insurer) — the systems and stakeholders differ materially
- **Repair vs. replace vs. calibration-only:** Each is a different operational workflow; "calibration-only" is a growing segment as ADAS retrofitting increases

**Where CCOTF sits:** Stages 2 and 3 — first contact, booking, and pre-visit communications. This is the scope of the Contact Centre of the Future programme.

**Source:** [[braindump-2026-04-08-1426-review-customer-journey-model]], [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]]

---

### Layer 4: Systems Landscape

**Purpose:** Understand which systems support which steps in the value chain and customer journey — and how they connect.

**Known / Suspected System Landscape (to be confirmed):**

| Domain | System | Type | Status |
|---|---|---|---|
| CRM / Front-office | Salesforce | Product (managed + unlocked packages) | Suspected confirmed |
| ERP / Back-office | Oracle EBS (or equivalent) | Commodity | To be confirmed |
| Integration / Middleware | MuleSoft or equivalent | Product | To be confirmed |
| Booking & Scheduling | Proprietary or off-the-shelf | Product → Custom | Unknown |
| Field Service / Dispatch | Unknown | Custom → Product | Unknown |
| ADAS Calibration | Specialist tooling | Custom | Unknown |
| Insurance Portals | Integration layer | Custom | Unknown |
| Comms / Contact Centre | CCOTF in progress | Custom → Product | In transformation |
| Reporting / BI | Unknown | Product → Commodity | Unknown |

**Key architectural questions outstanding:**
- Is there a live Salesforce ↔ EBS integration? What is the middleware layer?
- Are there unlocked packages in Salesforce or still change-set deployments?
- Does CCOTF own a separate comms platform or sit within existing systems?
- What are the integration points between opco systems and Belron centre platforms?

**Source:** [[braindump-2026-04-08-1352-ebs-salesforce]], [[braindump-2026-04-08-1349-salesforce-managed-unlocked-packages]], [[braindump-2026-04-08-1436-belron-software-development-model]]

---

### Layer 5: Capability Map

**Purpose:** The culminating layer — a structured view of *what the business does* (independent of who or how), showing ownership, maturity, and strategic importance.

**Status:** Not yet built. The Business Capability Modelling braindump (Apr 7) defines the approach; the customer journey and value chain work (Layers 1–4) are the inputs.

**First capability map — starting point:**

Top-level Belron capabilities (draft):
1. Customer Acquisition & Sales
2. Booking & Scheduling
3. Vehicle Glass Repair
4. Vehicle Glass Replacement
5. ADAS Calibration
6. Technician Dispatch & Logistics
7. Insurance Claims Processing
8. Supply Chain & Procurement
9. Fleet & Account Management
10. Customer Experience & Service
11. Technology & Systems Management (EA sits here)
12. People & Workforce Management
13. Finance & Reporting

**Note:** The CCOTF/Front-office capability overlap (Apr 8 braindump) is most likely to surface in capabilities 1, 2, and 10 — where customer contact, booking, and service experience converge.

**Source:** [[braindump-2026-04-07-1520-business-capability-modelling]], [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]]

---

## How to Build This Understanding

### Phase 1 — Document Research (April 2026)
- [ ] Find and read Belron strategy / operating model documents on the intranet 📅 2026-04-10
- [ ] Review John Prodgers' DLD presentations 📅 2026-04-11
- [ ] Find the existing customer journey model 📅 2026-04-10
- [ ] Confirm: Oracle EBS or different ERP? 📅 2026-04-10
- [ ] Confirm: Salesforce deployment model (change sets / unlocked packages) 📅 2026-04-10
- [ ] Get CCOTF programme documentation 📅 2026-04-09
- [ ] Find existing architecture or systems landscape diagrams 📅 2026-04-15

### Phase 2 — Stakeholder Conversations (April–May 2026)
- [ ] Book informal conversations with 4–5 people who know how Belron builds and operates (start with operational stakeholders) 📅 2026-04-18
- [ ] Ask one operations manager: "What keeps you up at night?" 📅 2026-04-25
- [ ] Ask one Salesforce/IT person: "Walk me through how we deploy to Salesforce" 📅 2026-04-25
- [ ] Explore technician ride-along or contact centre observation 📅 2026-04-30

### Phase 3 — Artefact Production (May 2026)
- [ ] Draft the Porter value chain for Belron (validated) 📅 2026-05-07
- [ ] Draft the Wardley Map for one capability area (booking-to-dispatch) 📅 2026-05-07
- [ ] Build a first-pass capability map (top 2 levels) 📅 2026-05-14
- [ ] Draft the "How Belron builds software" one-page model 📅 2026-05-14

---

## Connections Between Layers

```
Porter Value Chain
    → reveals where value flows and what activities matter
    → informs which capabilities are strategic vs commodity

Wardley Map
    → takes the value chain activities and shows evolution stage
    → reveals build vs buy vs wait decisions
    → shows where AI agents (A2A/MCP) should be placed

Customer Journey Map
    → shows the value chain from the customer's perspective
    → reveals which systems support which touchpoints
    → shows where CCOTF sits and what front-office capabilities it needs

Systems Landscape
    → maps the systems to the customer journey and value chain
    → reveals integration gaps (EBS ↔ Salesforce)
    → identifies where capability overlaps have a technical expression

Capability Map
    → synthesises all layers into a single authoritative view
    → enables investment prioritisation
    → resolves ownership ambiguity (CCOTF vs front-office)
```

---

## Related Frameworks
- [[ea-effectiveness-framework]] — building this framework is itself a stakeholder engagement exercise; each gap-filling conversation is a touchpoint
- The MCP/A2A knowledge doc — MCP servers can sit in front of EBS and Salesforce; Layer 4 informs where to build the first MCP integrations

---

*Consolidated from 8 sources | Confidence: Medium-High (approach strong; Belron-specific content needs validation) | Status: Emerging — Phase 1 underway April 2026*
