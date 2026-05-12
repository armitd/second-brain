---
type: "consolidated-knowledge"
domain: "professional"
framework: "ccotf-technology-architecture"
created: "2026-05-12"
last_updated: "2026-05-12"
consolidation_id: "consolidation-2026-05-12"
source_documents: 5
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
| **Amazon Connect** | Belron is AWS-first | Native AI/ML ecosystem (Lex, Bedrock, Connect Wisdom); MCP support confirmed (May 2026); full agentic rebrand | Deeply AWS-tied; switching cost increases over time |
| **Genesys Cloud CX** | Cloud-neutral; best-of-breed preferred | Market leader; broad AI partner ecosystem; strongest WFM integration | Higher per-seat cost; independent of cloud infrastructure |
| **Salesforce Service Cloud Voice** | Salesforce is the CRM of record at Belron | Native CRM integration; Agentforce (May 2026 GA) is the agentic layer | Requires Salesforce CRM; licensing complexity |
| **NICE CXone** | WFM and QM are the primary priorities | Strong WFM and AI QA portfolio | Less AI innovation velocity than Amazon/Salesforce |

**The unknown:** Which CCaaS platform does Belron currently use? This is the highest-priority fact to confirm before any CCOTF architecture work proceeds.

**Evidence:**
- [[braindump-2026-05-07-0934-ccotf-technology-component-model]] — "The CCaaS platform choice is the most consequential single technology decision. Everything else in this reference model either sits on top of, integrates with, or is constrained by the CCaaS platform"
- [[daily-brief-2026-05-12]] — Salesforce Agentforce Contact Center GA confirms Service Cloud Voice as a live agentic option
- [[daily-brief-2026-05-12]] — Microsoft Dynamics 365 Contact Center deployed three AI agents (April 2026) — worth assessing if Belron is Dynamics-stack

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

---

## Related Frameworks

- [[agentic-ai-governance-framework]] — Domain 11 (AI Model Governance) and Domain 4 agentic components are governed by the MCP Governance framework; these two frameworks must align
- [[ai-damage-assessment-strategy-framework]] — CCOTF is the delivery channel for AI damage assessment; the PoC AI capability integrates into Domain 4 and the Belron-specific layer
- [[ea-effectiveness-framework]] — Principle 6 (BA-EA fluency): the capability-to-technology mapping is the next EA deliverable; requires working with BA colleagues' existing capability model

---

*Consolidated from 5 sources | Confidence: Working | Status: Reference model built; estate validation pending*
