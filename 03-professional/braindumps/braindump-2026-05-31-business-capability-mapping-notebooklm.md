---
type: "braindump"
domain: "professional"
date: "2026-05-31"
created: "2026-05-31"
themes: ["business-capability-mapping", "enterprise-architecture", "application-rationalization", "EA-tooling", "heat-mapping"]
tags: ["#braindump", "#enterprise-architecture", "#capability-mapping", "#application-rationalization", "#EA-strategy"]
status: "raw"
source_notebooklm: "https://notebooklm.google.com/notebook/a2bc602e-331e-4cb6-b85c-120b4fb873c4"
source_note: "Synthesised from 33-source NotebookLM notebook on Business Capability Mapping"
energy_level: "high"
emotional_tone: "analytical"
confidence: "high"
---

# Braindump: Business Capability Mapping — Deep Research Synthesis

## Raw Thoughts

Pulled this from a NotebookLM notebook with 33 sources on Business Capability Mapping. Comprehensive coverage of theory, methodology, tooling, and EA integration. Capturing as a braindump for processing into knowledge base.

---

## Content Analysis

### Main Themes
1. **BCM as stable EA foundation:** Capability maps describe *what* a business does, independent of how — making them durable through org change, tech change, and process change
2. **Three-level hierarchy:** L1 Core Domains → L2 Sub-capabilities → L3 Detailed Activities — the right granularity at each level drives usability
3. **Heat mapping as the activation layer:** The static map becomes a decision tool only when overlaid with strategic importance, maturity, or risk data
4. **BCM → Application Rationalization:** The L3 capability-to-application mapping is the bridge between business strategy and IT portfolio decisions
5. **Tooling landscape:** Mature EA platforms (LeanIX, Ardoq, ServiceNow) vs. lightweight visual tools (Mural, Jibility) — choice depends on where the org is in its EA journey

### Supporting Ideas
- **MECE principle is non-negotiable:** Capabilities must be Mutually Exclusive (no overlaps) and Collectively Exhaustive (nothing missing) — otherwise the map creates confusion rather than clarity
- **Industry frameworks exist to avoid starting from scratch:** APQC PCF (general), BIAN (banking), TM Forum (telecom) — check if any apply to auto glass / mobility services
- **Capabilities ≠ Processes ≠ Value Streams:** Three distinct architectural constructs that are constantly confused. Capabilities = what (stable), Processes = how (changes), Value Streams = end-to-end customer view (e.g. "Claim to Settlement")
- **BCM is indispensable for M&A:** Standardised capability view is the fastest way to assess overlap when integrating two businesses
- **Operational Resilience connection:** Dependency analysis links recovery strategies to capabilities rather than isolated IT systems — critical for resilience planning

### Questions Raised
- Does Belron have an existing L1 capability map, or is the work starting from scratch?
- Which industry framework is most applicable to auto glass / mobility services? (APQC PCF may be the closest)
- What's the right first use case to anchor the map — investment prioritisation, app rationalisation, or TOM design?
- Is there appetite for a heat map now (e.g. strategic importance overlay) or is validating the base map the priority?

### Decisions Contemplated
- Whether to use a dedicated EAM platform (LeanIX is already in the tooling landscape per earlier research) or build the initial map in a lightweight tool
- Top-down vs. bottom-up methodology — start with strategic objectives (top-down) or existing processes (bottom-up)?
- How to handle the L3 granularity question — too deep too early kills adoption

---

## Strategic Intelligence

### Key Insights
1. **The map is only as good as its activation.** A static capability map filed in a wiki is worthless. Value comes from using it as a live lens: heat mapping for investment decisions, linking to applications for rationalisation, connecting to value streams for transformation design.
2. **BCM can save 15–20% in operational redundancies.** The mechanism: mapping applications to L3 capabilities surfaces duplication (multiple systems supporting the same function). This is a concrete ROI story for securing exec sponsorship.
3. **The TIME matrix is the decision framework for APR.** Once capabilities and applications are mapped, each app is assessed on Business Value × Technical Fit → Tolerate / Invest / Migrate / Eliminate. Simple, visual, actionable.
4. **Maturity assessment adds the third dimension.** Capabilities can be rated on a five-point maturity scale (Initial → Repeatable → Defined → Managed → Optimised). This reveals where capability relies on individuals vs. defined processes — a critical risk signal.
5. **Static documentation is a trap.** Spreadsheets and Visio diagrams go stale immediately. The organisations that extract value from BCM are those using EAM platforms where the map is a living, query-able asset.
6. **Stakeholder engagement is the hard problem.** BCM fails not because the methodology is wrong, but because it becomes an IT/EA artefact that business stakeholders don't own. The map must be co-created with business, finance, and IT.

### Pattern Recognition
- **Connects directly to previous braindump** (2026-04-07): The internal education strategy for BCM at Belron — this research provides the methodological depth to back that up
- **Connects to CCOTF work:** Contact Centre of the Future needs a capability view of the front office — this research provides the methodology
- **Connects to AI Damage Assessment PoC:** Damage assessment is a capability. Heat mapping it for strategic importance + current state maturity creates the investment case language
- **Recurring pattern:** Every EA framework eventually arrives at the same point — you can't govern what you can't name. BCM is the naming convention for the business.

### Strategic Implications
- Belron's pre-IPO context makes BCM more urgent: investors will want to see a clear picture of what the business *does* and where technology investment is going — a capability map with a heat overlay is exactly that artefact
- A well-executed BCM exercise positions EA as the strategic governance layer, not a technical support function — which is the longer-term objective
- The APR use case (TIME matrix) is potentially the highest-ROI first application — it creates a defensible, financially-grounded conversation about IT investment
- LeanIX is already in the market (per sources) — if Belron doesn't have an EAM platform, this is worth a serious evaluation

---

## The Methodology in Brief

### Six-Step Build Process
1. **Understand strategic objectives** — review strategy docs, SWOT, transformation programmes
2. **Identify L1 capabilities (7–10 core domains)** — top-down from strategy + bottom-up from existing processes
3. **Decompose to L2/L3** — granular enough for application mapping, not so deep it becomes a process map (max 3 levels)
4. **Apply MECE** — no overlap, no gaps
5. **Assess and prioritise** — maturity, financial impact, strategic importance
6. **Link to applications and resources** — bridge to IT portfolio, org units, data objects

### Heat Map Overlays (in priority order for Belron)
| Overlay | What it shows | Decision it enables |
|---|---|---|
| Strategic Importance | Which capabilities drive competitive advantage | Where to invest / protect |
| Maturity | Where capability relies on individuals vs. process | Where to standardise / build resilience |
| Risk | Capabilities supported by end-of-life or unstable tech | Where to modernise urgently |
| Application density | How many systems support each capability | Where to rationalise |

### TIME Matrix (APR Decision Framework)
| Business Value | Technical Fit | Decision |
|---|---|---|
| High | Low | **Migrate** — modernise, high risk |
| High | High | **Invest** — expand and enhance |
| Low | High | **Tolerate** — maintain, don't grow |
| Low | Low | **Eliminate** — decommission |

---

## Tooling Landscape

| Category | Tools | Best for |
|---|---|---|
| Comprehensive EAM | SAP LeanIX, Ardoq, ServiceNow SPM, BOC ADOIT | Full lifecycle, living maps, APR |
| Visual collaboration | Mural | Initial brainstorming and workshop facilitation |
| Roadmap-linked | Jibility | Connecting capability planning to delivery roadmaps |
| Transformation planning | Orbus Software, ValueBlue BlueDolphin | Application inventory and TOM design |

---

## Common Pitfalls to Avoid
- **Confusing capabilities with processes** — capabilities are nouns (what), processes are verbs (how)
- **Going too deep too fast** — more than 3 levels becomes a process map; nobody uses it
- **Static documentation** — a map in a PowerPoint is dead on arrival
- **EA-only ownership** — if business stakeholders don't co-own it, it won't be used for decisions
- **Too much theory, not enough company context** — always ground in the organisation's own business language

---

## Action Items

### Immediate
- [ ] Cross-reference with existing BCM work in Belron — what exists already? 📅 2026-06-07
- [ ] Check whether LeanIX is on the radar / in evaluation for EA tooling 📅 2026-06-07

### Short-term
- [ ] Use this research to draft an L1/L2 capability map for Belron (auto glass service business) — connect to CCOTF and Damage Assessment PoC 📅 2026-06-14
- [ ] Build the investment case narrative: BCM → APR → 15–20% redundancy savings — useful for IPO readiness framing 📅 2026-06-14

### Strategic Considerations
- Consider anchoring BCM adoption to a specific business problem (e.g. Contact Centre rationalisation or ADAS calibration investment) rather than launching it as a standalone EA exercise
- The maturity assessment overlay may land better with business stakeholders than a technical fitness overlay — it speaks to organisational capability, not IT health
- Pre-IPO timing is an accelerator: the due diligence process will surface BCM gaps — better to have the map before that happens

---

## Connections
- **Related braindump:** [[braindump-2026-04-07-1520-business-capability-modelling]] — internal education strategy for BCM at Belron
- **Related braindump:** [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]] — CCOTF front office capability overlap
- **Relevant frameworks:** TOGAF Business Architecture, BIZBOK, ArchiMate capability notation, APQC PCF
- **Active projects:** Contact Centre of the Future, AI Damage Assessment PoC
- **Follow-up skills:** `/knowledge-consolidation` to synthesise across all BCM braindumps

## Domain Classification
- **Primary Domain:** Professional (100%)
- **Reasoning:** Core EA methodology directly applicable to Belron EA strategy and active projects
- **Privacy Level:** Professional — shareable internally

---

*Synthesised from NotebookLM notebook: Business Capability Mapping (33 sources)*
*Processed by COG — 2026-05-31*
