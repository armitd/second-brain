---
type: "consolidated-knowledge"
domain: "professional"
framework: "ccotf-technology-architecture"
created: "2026-05-12"
last_updated: "2026-06-19"
consolidation_id: "consolidation-2026-06-19"
source_documents: 19
status: "working"
tags: ["#framework", "#consolidated", "#CCOTF", "#contact-centre", "#technology-reference-model", "#enterprise-architecture"]
---

# CCOTF Technology Architecture Framework

## Framework Overview
A 12-domain technology component reference model for a Contact Centre of the Future — anchored to Belron's specific operating context (vehicle glass repair/replace, insurer relationships, VRM-based customer identification, ADAS calibration). Designed to give the EA team a standard reference against which to assess Belron's current technology estate, identify gaps and overlaps, and build the architecture target state.

**Status:** Working (reference model built from industry standards; not yet validated against Belron's actual current technology estate)
**Last Updated:** 2026-05-12
**Source:** [[braindump-2026-05-07-0934-ccotf-technology-component-model]] (primary), [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]], [[daily-brief-2026-05-07]] (Corgi AI-native insurance signal)

---

## Why This Model Matters

The Contact Centre of the Future project has a business capability model. It does not yet have a technology component reference model — the architecture layer that sits beneath the capability model, showing which systems enable which capabilities. Without this:
- Technology gaps and overlaps cannot be assessed systematically
- The investment case cannot be made concrete (what do we buy, replace, or build?)
- The integration surface cannot be defined (where does CCOTF meet AI Damage Assessment, LeanIX, MCP governance?)

This framework is the missing layer.

---

## Core Principles

### Principle 1: Domain 4 (AI & Automation) Is the Differentiating Layer — Everything Else Is Table Stakes

**Statement:** A modern contact centre can buy Domains 1–3 and 5–12 from any competent CCaaS vendor. The CCOTF competitive differentiation and vision lives in Domain 4 — specifically: LLM-powered virtual agents, real-time agent assist, agentic orchestration for multi-step workflows, and AI damage assessment integration. Prioritise architecture investment and vendor selection on Domain 4 before optimising any other domain.

**The AI layer by component:**
- Conversational AI Platform (NLU/NLP, LLM-powered) — replaces rules-based chatbot
- Real-time agent assist — surfaces guidance, KB articles, and responses live during contact
- Agentic AI orchestration — multi-step autonomous task completion, the CCOTF differentiator
- AI Quality Assurance — 100% contact coverage automated, replacing manual sample review
- Predictive contact prevention — identifies at-risk customers before they contact
- AI Damage Assessment integration — direct connection to the Damage Assessment PoC

**Evidence:**
- [[braindump-2026-05-07-0934-ccotf-technology-component-model]] — "Domain 4 is the differentiating layer — everything else is table stakes"
- [[daily-brief-2026-05-07]] — Amazon Connect rebranded as agentic AI suite with MCP support — confirms Domain 4 as the CCaaS vendor's own priority

**Confidence:** High

---

### Principle 2: The CCaaS Platform Decision Is the Single Most Consequential Technology Choice

**Statement:** Everything in the technology reference model either sits on top of, integrates with, or is constrained by the CCaaS platform. No other technology decision in the CCOTF programme has as many downstream dependencies. The CCaaS choice must be made before designing anything else in depth.

**Decision framework for Belron:**

| Platform | Best Fit If... | Strengths | Watch |
|---|---|---|---|
| **Amazon Connect** | ✅ **AWS is a confirmed Belron cloud provider (May 2026)** | Native AI/ML ecosystem (Lex, Bedrock, Connect Wisdom); MCP support confirmed (May 2026); full agentic rebrand as Amazon Connect Customer; United Airlines deployed in 3 months vs. previous 12 | Deeply AWS-tied; switching cost increases over time — but this is already Belron's cloud |
| **Genesys Cloud CX** | Cloud-neutral; best-of-breed preferred | Market leader; broad AI partner ecosystem; strongest WFM integration | Higher per-seat cost; independent of cloud infrastructure |
| **Salesforce Agentforce Contact Center** | Salesforce Service Cloud Ent/Perf/Unlimited is the CRM of record at Belron | Native CRM integration; **AGCC GA (Feb 2026, UK available)** — voice, digital, AI agents and CRM in one platform; eliminates integration tax; $2/conversation | Hard Salesforce dependency — value disappears without Service Cloud; **no WFM** (still needs Verint/NICE); UK/US/Canada only — continental Carglass markets not covered |
| **NICE CXone** | WFM and QM are the primary priorities | Strong WFM and AI QA portfolio | Less AI innovation velocity than Amazon/Salesforce |

**Cost model gap — licensing vs. consumption (June 2026):**
Current CCaaS vendor evaluation uses published per-seat/per-agent licensing costs. A critical gap exists: CCaaS vendors are shifting toward consumption-based pricing (per-interaction, per-AI-action, per-minute-of-AI-assist), not just agent seat licensing. The total cost of ownership calculation for any CCaaS platform decision must include both the licensing model AND the consumption cost model — particularly for AI-native features (virtual agents, real-time assist, automated QA). Without consumption-side modelling, Belron risks an underestimated TCO that surfaces post-contract. Action: require consumption cost modelling alongside seat licensing in any CCaaS RFP response. Source: [[braindump-2026-06-09-2215-genesys-consumption-numbers]]

**AWS confirmed:** AWS is a Belron cloud provider (confirmed May 12, 2026), which makes Amazon Connect the front-runner CCaaS candidate — it runs natively on AWS infrastructure, integrates with Amazon Bedrock for AI, and now has full MCP support and an agentic rebrand (Amazon Connect Customer). This does not preclude Genesys or Salesforce if Belron has existing contracts, but the AWS fit is now a confirmed advantage rather than a hypothesis.

**The remaining unknown:** Which CCaaS platform does Belron *currently* use? Even if Amazon Connect is the target state, understanding the current platform determines the migration path and transition complexity.

**Agentforce Contact Center — fit analysis (May 2026):**
AGCC is the strongest option *if and only if* Belron opcos run Salesforce Service Cloud. The AGCC value proposition is eliminating the integration tax between CRM and CCaaS. Without Salesforce, that advantage is moot. Key constraints for a Belron-wide play: (1) Geography — UK, US, Canada only today; continental Carglass markets (France, Germany, Belgium, Italy) not available; (2) WFM gap — no native workforce management, Verint/NICE still required; (3) Belron CCOTF architecture principle ("explicit rules, not LLM inference") needs reconciling with AGCC's agentic-default routing. De-risked entry: AGCC can be deployed alongside an existing platform as a single-opco pilot — Autoglass UK is the candidate if they run Salesforce. **First action: audit which Belron opcos run Salesforce Service Cloud.**

**Evidence:**
- [[braindump-2026-05-07-0934-ccotf-technology-component-model]] — "The CCaaS platform choice is the most consequential single technology decision. Everything else in this reference model either sits on top of, integrates with, or is constrained by the CCaaS platform"
- [[daily-brief-2026-05-12]] — Salesforce Agentforce Contact Center GA confirms Service Cloud Voice as a live agentic option
- [[daily-brief-2026-05-12]] — Microsoft Dynamics 365 Contact Center deployed three AI agents (April 2026) — worth assessing if Belron is Dynamics-stack
- [[braindump-2026-05-30-0958-agentforce-contact-center-belron-fit]] — Full fit analysis: AGCC architecture, pricing, geographic gaps, WFM gap, Salesforce dependency, Belron-specific evaluation criteria

**Confidence:** High

---

### Principle 3: The Belron-Specific Layer Is Where the Complexity Lives

**Statement:** Generic CCOTF frameworks do not account for Belron's operating context. Six components are unique to Belron's domain — they are not available from standard CCaaS vendors, they require bespoke integration, and they are the difference between a generic contact centre and a Belron CCOTF.

**The Belron-specific components:**

| Component | Why It's Belron-Specific | Architecture Implication |
|---|---|---|
| **VRM Lookup** | Customer identified by vehicle registration plate, not account number | Must be the first routing step; VRM → customer/vehicle data is the identity layer for all subsequent AI |
| **Glass Type / Damage Assessment** | AI must classify damage type and repair-vs-replace before the contact progresses | Direct integration point with AI Damage Assessment PoC; Domain 4 component |
| **Insurer Claim Pre-Authorisation** | Many jobs are insurance-funded; real-time pre-approval required during contact | Domain 10 Insurer API Integration; the most complex and strategically important component |
| **ADAS Calibration Routing** | ADAS-equipped vehicles require specialist technician and equipment | Skills-based routing extension; not standard ACD capability |
| **Multi-OpCo Routing** | Autoglass UK, Carglass France/Germany, Safelite US — multi-brand, multi-language | CCaaS platform must support multi-brand, multi-language; opco-level routing rules |
| **Mobile vs. Depot Routing** | Some jobs require mobile technician; others need depot visit | Job type determines the fulfilment path in Domain 12 (Field Service Management) |

**The Corgi signal (May 2026):** Corgi, an AI-native full-stack insurer, raised $160M at $1.3B valuation and is expanding into commercial vehicles. If Belron's insurer partners shift toward AI-native platforms, the Insurer Claim Pre-Authorisation component must be API-first, machine-readable, and real-time — not human-to-human liaison. The integration architecture for this component needs to anticipate the AI-native insurer model, not just current insurer APIs.

**Evidence:**
- [[braindump-2026-05-07-0934-ccotf-technology-component-model]] — Belron-specific layer table
- [[daily-brief-2026-05-07]] — Corgi raises $160M at $1.3B; "the insurance ecosystem is where Belron's revenue flows"

**Confidence:** High on component identification; Medium on Corgi's specific impact (depends on which Belron insurer partners move to AI-native)

---

### Principle 4: AI Model Governance (Domain 11) Connects Directly to MCP Governance

**Statement:** Any AI decision made during a customer contact — routing decision, damage assessment result, claim eligibility recommendation, next-best-action guidance — requires governance. The MCP Governance framework is the upstream governance architecture for CCOTF's AI components. These two projects must be explicitly connected; treating them as independent programmes creates a governance gap.

**The connection:**
- Domain 4 (AI & Automation): LLM integration, agentic orchestration, damage assessment AI — all generate AI decisions that need auditability
- Domain 11 (Security & Compliance): AI Model Governance is explicitly listed as a component — "bias, explainability, fairness for AI decisions — a new domain for CCOTF that connects to MCP Governance"
- The MCP Connector in Claude Platform on AWS (May 2026 GA) is a governance-relevant tool: IAM-authenticated, CloudTrail-audited MCP connections directly in the AWS ecosystem that may host the CCaaS platform

**Practical implication:** The CCOTF architecture team must include the MCP Governance project scope within Domain 11 design. Conversely, the MCP Governance framework should identify CCOTF as a primary use case and design the governance register to cover agentic contact centre AI explicitly.

**Evidence:**
- [[braindump-2026-05-07-0934-ccotf-technology-component-model]] — "Domain 11 (AI Model Governance) and Domain 4's agentic AI components need to sit within the MCP Governance framework"
- [[daily-brief-2026-05-12]] — Claude Platform on AWS MCP Connector as a governed integration point

**Confidence:** High — the connection is structural and explicitly identified in source braindump

---

### Principle 5: The Capability-Technology Mapping Is the Missing EA Deliverable

**Statement:** The business capability model says what the business does. The technology component reference model says which systems enable it. The artefact that connects them — the explicit capability-to-technology mapping — is the missing link. Without it, investment decisions remain disconnected from capability strategy, and technology changes cannot be evaluated against business impact.

**The next EA deliverable:** Map each CCOTF business capability to the technology components that enable it. This is the TOGAF Application Architecture layer connecting the Business Architecture (capability model) to the Technology Architecture (this reference model). The result is a heat map: which capabilities have strong technology support, which have gaps, which have redundant overlapping systems.

**LeanIX application:** Load the 12 domains as Application Building Block (ABB) groups in LeanIX. Each technology component becomes a building block. The capability-to-technology mapping becomes the relationship layer in LeanIX — visible, queryable, and updatable as the programme evolves.

**Evidence:**
- [[braindump-2026-05-07-0934-ccotf-technology-component-model]] — "The capability model and the technology component model need an explicit mapping layer. The missing artefact is the mapping between them — which technology components support which capabilities."
- [[braindump-2026-05-05-1549-togaf-ba-application]] — "LeanIX's Business Architecture features (value streams, capability maps) are likely underused — BA course knowledge maps directly to LeanIX practice"

**Confidence:** High

---

### Principle 6: Salesforce/Informatica Convergence Changes the CCaaS Platform Evaluation

**Statement:** The Salesforce acquisition of Informatica (closed November 2025, $8B) has materially changed the weight of the Salesforce Service Cloud Voice / Agentforce CC option. Belron likely uses Informatica for MDM today. If that is true, Salesforce Agentforce CC is not just a CCaaS platform — it is a data-integrated, AI-native contact centre that already has access to Belron's master customer and vehicle data through the Informatica layer. This changes the cost-benefit equation compared to building equivalent data integrations for any other CCaaS platform.

**What the Salesforce stack now looks like:**
- **CCaaS:** Salesforce Agentforce Contact Center (launched Enterprise Connect 2026; generally available)
- **AI agent platform:** Agentforce (multi-step agentic task completion, native in Service Cloud)
- **Master data:** Informatica Customer 360 + MDM feeding Agentforce agents directly — trusted, governed customer data without additional integration effort
- **Data integration:** Informatica Cloud Data Integration (CDI) — the leading ETL platform, now part of the same vendor
- **Data quality:** Informatica CLAIRE DQ Agent — AI-native data quality that directly improves Agentforce output
- **CRM:** Salesforce CRM (Sales Cloud / Service Cloud) — if Belron uses this, the integration is native

**The pivotal unknown:** Does Belron use Salesforce CRM (Sales Cloud, Service Cloud)? If yes, the Salesforce stack has a structural advantage that Microsoft and Amazon cannot easily match at the data layer. If no, the Informatica layer is the decision point — worth activating regardless of CCaaS choice.

**Architecture implication:** The CCaaS platform evaluation should now be explicitly three-way: Microsoft-stack (Teams Phone + Dynamics 365 CC + Azure AI) vs. Salesforce-stack (Agentforce CC + Informatica + MuleSoft) vs. Amazon-stack (Amazon Connect + Bedrock). The Informatica asset is a swing factor in the Microsoft vs. Salesforce comparison.

**Evidence:**
- [[braindump-2026-05-14-1444-informatica-idmc-beyond-mdm]] — "Salesforce acquired Informatica. Informatica is now the data foundation for Agentforce. If Belron evaluates Agentforce CC, they get the data quality, governance, and catalog layer as part of the stack — and if they already have Informatica MDM, Customer 360 feeds the Agentforce agents directly"
- [[braindump-2026-05-16-0041-contact-centre-uc-architecture-ebc]] — Zoom EBC visit; still-unsolved contact centre problems that EBC polish doesn't resolve

**Confidence:** High on the Salesforce/Informatica convergence fact; Medium on Belron-specific impact (depends on whether Belron uses Salesforce CRM — currently unknown)

---

### Principle 8: The CCOTF Reference Architecture Is Now a Formal TOGAF ADD — Govern From It

**Statement:** The CCOTF programme now has a formal TOGAF Architecture Definition Document (v0.1, May 2026), structured across ADM Phases A–D with ArchiMate 3.2 notation. This is the architecture governance artefact for the programme — all subsequent technology decisions, vendor selections, and integration designs should be evaluated against it. The RA is not a static document; it defines the review cadence (quarterly; immediately on CCaaS platform decision) and explicitly flags nine open issues that need resolution.

**What the RA adds beyond this framework:**
- 9 Architecture Principles (AP-01 to AP-09) established and owned by EA
- 19 Architecture Building Blocks (ABB-C01 to ABB-C19) defined at the component level
- A Belron Intelligence Layer formally named and bounded as a separate architectural tier
- AP-02: "Evaluate with explicit rules, not LLM inference" — the semantic governance principle (Darlene Newman, May 2026) — now an architecture standard for the CCOTF programme
- A 5-phase programme roadmap (Foundation → AI-First CC → Intelligent Human CC → Belron Intelligence → Agentic Back-Office)
- 9 Open Issues with owners — the most critical are: OI-02 (CCaaS platform selection), OI-05 (AI Damage Assessment PoC dependency), OI-07 (OneNote content migration due 30 May 2026)

**AP-02 — Semantic Governance Principle:** Evaluation of customer eligibility, job type, damage classification, insurer pre-authorisation, and escalation criteria must use governed rules and explicit ontology, not LLM inference. This ensures determinism, auditability, and EU AI Act compliance. Source: [[braindump-2026-05-21-1700-semantic-layer-governance-newman]].

**Evidence:**
- [[2026-05-23-ccotf-reference-architecture]] — TOGAF ADD v0.1 covering all four ADM phases
- [[braindump-2026-05-21-1700-semantic-layer-governance-newman]] — Newman principle: semantic layer = governance infrastructure, not technology

**Confidence:** High — the RA exists and is the authoritative governance document for the programme

---

### Principle 7: Vendor EBC Content Requires Reference Customer Validation Before Acting On It

**Statement:** Executive Briefing Centre visits are effective at demonstrating vendor capability against a client's stated pain points. They are not evidence that those pain points are solved. Vendors brief against the same structural pain points across every client, every year — because those pain points are structurally persistent, not because the vendor has genuinely resolved them. Belron should treat EBC content as a hypothesis to test against reference customer evidence, not as a proof point.

**The diagnostic test:** For every EBC commitment or capability demonstration, ask: "Which reference customer can I speak to who has deployed this in production at our scale?" If the answer is a case study or a demo environment, the problem is probably still a problem.

**The Zoom EBC signal (May 2026):** A Zoom CCaaS EBC session showed AI add-ons layered on top of underlying CCaaS problems that were recognised from prior (HSBC) experience. The observation: same problems, better presentation. The key institutional memory from HSBC-scale contact centre deployments is that the hardest problems in contact centre technology — routing accuracy at scale, knowledge base quality, agent adoption of AI tools — are not solved by a vendor briefing; they are solved by programme management, change management, and sustained investment in data quality.

**The vendor lock-in representation challenge:** Any honest architecture diagram for UC/CCaaS should explicitly show: which vendor owns which component, data proximity (where does customer data actually live), and the lock-in/buy-in spectrum. This forces the vendor conversation into the open and gives stakeholders a clear view of dependency risk before a platform decision is made.

**Evidence:**
- [[braindump-2026-05-16-0041-contact-centre-uc-architecture-ebc]] — "They are solving the problems that we were solving at HSBC but they're still problems." EBC content as marketing until validated by reference customers.
- [[braindump-2026-05-16-0041-contact-centre-uc-architecture-ebc]] — Architecture representation challenge: showing vendor ownership, data proximity, lock-in vs. buy-in

**Confidence:** High — this is a generalisable principle validated repeatedly across enterprise technology selection; the HSBC pattern gives it specific institutional grounding

---

### Principle 9: The Community Is the Change Management Plan

**Statement:** A pan-Belron programme affecting every contact centre across 35 countries cannot be governed by a small EA team producing architecture documents. The CCOTF community of contact centre practitioners — managers, ops leads, IT, BPO partners — is not a communications channel; it is the architecture's primary change management vehicle. Building the community before the platform decision means practitioners shape the direction rather than receive it.

**The intelligence problem:**
The CCOTF Reference Architecture has 9 open issues. Several (OI-01 capability boundary, OI-03 current platform knowledge, OI-06 insurer API complexity) are open because the EA team lacks line-of-sight into each opco. A community of practitioners with structured Signals capability is faster and broader than formal workshops and bilateral stakeholder loops.

**The Hive Signals model (June 2026):**
Belron's internal Hive innovation platform includes a Signals feature for structured idea and observation submission. Using this for a CCOTF community would:
- Surface current-state platform information across opcos (resolving OI-03)
- Identify pain points that the architecture must address (informing OI-01 scope)
- Create a pipeline of early adopters for Phase 1 deployment (people who contributed are more likely to adopt)
- Provide demonstrable cross-opco engagement for IPO governance narrative — evidence of programme maturity, not just architectural artefacts

**Architecture principle connection:**
AP-09 (multi-opco by default) is the technical statement. The Hive community is the human counterpart: the programme must work for Autoglass, Carglass, and Safelite simultaneously — so must the community.

**The three roles that make this work:**
- Founding members (5–10 respected practitioners per major opco — Autoglass UK, Carglass DE/FR, Safelite US) provide credibility
- Signal contributors provide ground-level intelligence
- Programme liaisons visibly act on community input to close the feedback loop — the pattern fails if signals are submitted but never visibly acted upon

**Evidence:**
- [[braindump-2026-06-19-1652-hive-ccotf-community]] — "The community IS the change management plan. People who contribute to a programme are more likely to adopt its outputs"
- [[braindump-2026-06-05-1739-btops-collaboration-ccotf-viva-engage]] — BT&Ops gap: CCOTF needs a community home before it needs a communications plan; conversation will happen anyway in informal channels
- [[braindump-2026-06-03-1009-ccotf-qualtrics-genesys-ops]] — Stakeholder loops (Jamie/Joakim/Heidi) as the current workaround for a community intelligence problem

**How to apply:**
1. Check whether a CCOTF or contact centre community already exists on Hive (avoid duplicate)
2. Draft the community purpose statement and scope before inviting anyone — what is it for, who should join, what will they contribute?
3. Define the Signals taxonomy: pain points, platform observations, vendor intelligence, ideas, external market signals
4. Consider linking Signals to specific open issues in the RA — members submit against a named OI, making the community-to-architecture connection explicit

**See also:** [[pattern-community-as-change-management]] — the generalisable pattern behind this principle

**Confidence:** High on the principle; Medium on Hive Signals as the right specific implementation (needs product confirmation)

---

## The 12-Domain Reference Model

A complete contact centre technology stack organised into 12 functional domains. Each domain contains the standard components a modern CCOTF would include, plus notes on how they evolve in an AI-native architecture.

| Domain | Purpose | CCOTF Evolution Priority |
|---|---|---|
| **1. Customer Interaction Channels** | How customers reach the contact centre | Medium — channels retained; interaction model changes |
| **2. Routing & Orchestration** | Getting contacts to the right place | High — AI intent-based routing replaces ACD |
| **3. Agent Desktop & Workspace** | What agents see and use | High — AI-embedded desktop; auto-logging |
| **4. AI & Automation** | The intelligence layer — CCOTF differentiator | Critical — this is where CCOTF is built |
| **5. Workforce Management & Engagement** | Managing the human workforce | Medium — AI-enhanced, not replaced |
| **6. CCaaS Platform / Core Infrastructure** | The foundational platform | Critical — the CCaaS decision unlocks everything |
| **7. CRM & Customer Data** | The customer record and data foundation | High — unified Customer 360 required for AI |
| **8. Knowledge & Content Management** | What agents and AI need to know | Medium — AI-indexed KB replaces search |
| **9. Analytics & Reporting** | Insight from contact centre data | Medium — AI-enriched, 100% contact coverage |
| **10. Integration & API Layer** | How the contact centre connects externally | Critical (Belron-specific) — VRM, insurer API, ADAS |
| **11. Security & Compliance** | Data protection and regulatory obligations | High — AI Model Governance is a new component |
| **12. Back-Office Integration** | Systems the contact centre triggers | High (Belron-specific) — claims, job management, inventory |

### Domain 4 Detail: AI & Automation (the differentiating layer)

| Component | CCOTF Role |
|---|---|
| Conversational AI Platform | NLU/NLP engine; LLM-powered, not rules-based |
| Virtual Agent / Chatbot | AI-native self-service; GenAI reasoning, not decision trees |
| LLM Integration | Foundation model API (Claude, GPT-4o, Gemini) — central to all AI capabilities |
| Real-Time Transcription | Feeds agent assist and QA simultaneously |
| Sentiment & Emotion Detection | Agent alert + supervisor routing trigger |
| Real-Time Agent Assist Engine | Live guidance, KB surfacing, response suggestion |
| Next-Best-Action / Recommendation | Predictive guidance on what to do/say |
| Agentic AI Orchestration | Multi-step autonomous task completion — the CCOTF differentiator |
| AI Quality Assurance | 100% contact coverage automated |
| Predictive Contact Prevention | Identify at-risk customers before they contact |
| **AI Damage Assessment Integration** | **Photo/video analysis → repair/replace decision — direct link to AI Damage Assessment PoC** |

### Domain 10 Detail: Integration & API Layer (the Belron-critical layer)

| Component | Belron Specificity |
|---|---|
| **Insurer API Integration** | Real-time claim authorisation — most complex and strategically important |
| **VRM / Vehicle Lookup** | Vehicle registration → customer/vehicle data; identity layer for all AI routing |
| **Field Service / Technician Dispatch** | AI-optimised scheduling; job-type-aware |
| **ADAS Calibration Booking** | Specialist calibration appointment management |
| Event Streaming Platform | Real-time data backbone (Kafka / event bus) |

---

## Applications & Use Cases

### Use Case 1: Technology Estate Gap Analysis (RAG Assessment)
**When to Apply:** Once the CCaaS platform is confirmed and the existing technology estate is known
**How to Apply:**
1. Map Belron's current contact centre technology against each of the 12 domains
2. Assign RAG status per component: Red = gap (no current coverage), Amber = partial coverage, Green = covered
3. Identify overlap (multiple systems serving the same component) and gaps (no system)
4. Prioritise: Domain 6 (CCaaS) and Domain 4 (AI) are the first two to assess

**Expected Outcomes:** A visual heat map of the current estate vs. the reference model — the foundation for the target state architecture

---

### Use Case 2: Loading into LeanIX
**When to Apply:** Once the reference model is validated against Belron's estate
**How to Apply:**
1. Create 12 Application Building Block (ABB) groups in LeanIX — one per domain
2. Create individual ABB records for each component within each domain
3. Assign current system mappings (if known) as Technology Building Blocks (TBBs)
4. Build the capability-to-technology relationship layer

**Expected Outcomes:** CCOTF technology landscape visible and queryable in LeanIX; supports budget cycle roadmap submissions

---

### Use Case 3: Investment Case for the CCOTF Programme
**When to Apply:** Before Belron budget cycle (July 2026 window — roadmaps needed by mid-June)
**How to Apply:**
1. Use the gap analysis (Use Case 1) to identify the highest-priority investments
2. Frame each investment in capability language: "This investment enables [capability], which [business outcome]"
3. Use the Gartner 80%/30% projection (80% autonomous resolution by 2029, 30% cost reduction) as a directional anchor
4. Connect Domain 4 investments to the AI Damage Assessment PoC — they are the same investment viewed from two programmes

---

## Boundaries & Limitations

**This framework works when:**
- There is organisational clarity about which CCOTF components are in-scope vs. already covered by the broader IT estate
- The CCaaS platform decision is made or can be discovered
- There is appetite to load the model into LeanIX rather than treating it as a document artefact

**This framework does NOT work when:**
- CCOTF scope is still being negotiated and the boundary with other programmes is unclear
- Belron's current technology estate cannot be mapped (data unavailable or stakeholder access blocked)
- Budget decisions have already been made — this model is most valuable as an input to investment decisions, not a retrospective justification

**Important caveat:** The reference model is built from industry standards plus Belron-specific domain knowledge. It has not yet been validated against Belron's actual current technology estate. Any strategic decisions based on it should be tested against internal confirmation of current systems.

---

## Evolution & History

### May 7, 2026: Framework Created
Built as a primary EA deliverable for the CCOTF project. Trigger: the recognition that the business capability model existed but had no technology architecture counterpart — the gap between "what the business does" and "what systems enable it" was unaddressed.

**Source:** [[braindump-2026-05-07-0934-ccotf-technology-component-model]]

**Key design decisions:**
- 12 domains modelled on industry-standard CCaaS reference architectures (Gartner, Genesys, NICE reference models)
- Belron-specific layer added as an explicit separate table — not folded into generic domains
- Domain 4 (AI & Automation) intentionally elevated as the differentiating layer rather than just another domain
- AI Damage Assessment PoC explicitly called out as a Domain 4 component and a Belron-specific layer component

### May 2026 — ongoing
- Corgi AI-native insurance signal added: insurer API integration (Domain 10) must anticipate API-first insurer architecture
- Microsoft Dynamics 365 Contact Center and Salesforce Agentforce Contact Center both shipped (April–May 2026) — CCaaS vendor AI competition is accelerating
- Claude Platform on AWS MCP Connector: governance implication for Domain 11

### May 22–23, 2026: CCOTF Reference Architecture TOGAF ADD Completed
The technology component model and framework principles have been elevated into a formal TOGAF Architecture Definition Document — [[2026-05-23-ccotf-reference-architecture]]. This is the primary governance artefact for the CCOTF programme going forward. Key additions over the framework alone: formal architecture principles (AP-01 to AP-09), 19 ABBs, Belron Intelligence Layer formally scoped, 5-phase programme roadmap, and 9 open issues for resolution. The executive stakeholder diagram is at [[2026-05-23-ccotf-exec-diagram]].

---

## Related Frameworks

- [[agentic-ai-governance-framework]] — Domain 11 (AI Model Governance) and Domain 4 agentic components are governed by the MCP Governance framework; these two frameworks must align
- [[ai-damage-assessment-strategy-framework]] — CCOTF is the delivery channel for AI damage assessment; the PoC AI capability integrates into Domain 4 and the Belron-specific layer
- [[ea-effectiveness-framework]] — Principle 6 (BA-EA fluency): the capability-to-technology mapping is the next EA deliverable; requires working with BA colleagues' existing capability model

---

### June 2026 — Community Layer + Cost Model Gap + CCOTF Platform Landscape Mapped

**What Changed:** Three additions:

1. **Community as Change Management (Principle 9):** The Hive Signals community model added as the human counterpart to the AP-09 multi-opco architecture principle. Source: [[braindump-2026-06-19-1652-hive-ccotf-community]].

2. **Consumption cost model gap:** Licensing-only evaluation of CCaaS platforms is insufficient — AI-native consumption pricing (per-interaction, per-AI-action) must be modelled alongside per-seat costs. Source: [[braindump-2026-06-09-2215-genesys-consumption-numbers]].

3. **Belron contact centre platform landscape mapped:** LeanIX queried to extract full current-state contact centre platform inventory. 12 platforms identified across 11 countries. Genesys Cloud confirmed as strategic/target platform (tagged "Strategic" in LeanIX) across AU, BE, CH, DE, ES, FR (phaseIn), IT, NL, NZ, PT, US. Clear succession paths: Odigo → Genesys FR; Mitel AT → Effex; Avaya US/Amazon Connect → Genesys US; LivePerson → Salesforce Service Cloud EU. Confirms OI-03 (current platform knowledge) is substantially resolved for key opcos. Lucid diagram of this landscape was requested (user confirmed "yes please") but not yet completed — pending follow-up session.

---

*Consolidated from 19 sources | Confidence: Working | Status: Reference model built; platform landscape mapped via LeanIX; Hive community pending confirmation*
