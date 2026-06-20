---
type: reference-architecture
artefact_class: "TOGAF Architecture Definition Document — Vendor-Agnostic Base"
domain: enterprise-architecture
version: "0.3"
date: 2026-06-20
created: 2026-05-23
updated: 2026-06-20
title: "Contact Centre of the Future — Vendor-Agnostic Reference Architecture"
owner: "Armo — Enterprise Architecture, Belron"
status: "v0.2 — Working Draft"
notation: "TOGAF 10 / ArchiMate 3.2"
related_projects:
  - contact-centre-future
  - ai-damage-assessment-poc
  - mcp-governance
companion_documents:
  - overlay-amazon-connect.md
  - overlay-genesys-cloud-cx.md
  - overlay-salesforce-agcc.md
  - overlay-nice-cxone.md
supersedes: "2026-05-23-ccotf-reference-architecture.md"
tags:
  - reference-architecture
  - contact-centre
  - ccotf
  - agentic-ai
  - togaf
  - archimate
  - ea
  - vendor-agnostic
---

# Contact Centre of the Future
## Reference Architecture — Vendor-Agnostic Base
*TOGAF Architecture Definition Document · v0.2 · Enterprise Architecture, Belron*

---

## Document Control

| Field | Value |
|---|---|
| Version | 0.3 (Working Draft) |
| Date | 2026-06-20 |
| Owner | Armo, Enterprise Architecture |
| Notation | TOGAF 10 ADM phases A–D; ArchiMate 3.2 vocabulary |
| Review cadence | Quarterly; immediately on CCaaS platform decision |
| Supersedes | `2026-05-23-ccotf-reference-architecture.md` (v0.1) |
| ⚠ Key gap | CCaaS platform not yet selected — resolve OI-02 before detailed Phase D design |

---

## How to Use This Document

This document defines the **normative, vendor-agnostic reference architecture** for the CCOTF programme. It describes *what* the architecture must do and *how* it must behave — without specifying which vendor products implement each capability.

Four companion **Implementation Overlay** documents map vendor products to this architecture for the four principal CCaaS platform candidates:

| Overlay | File |
|---|---|
| Amazon Connect + Bedrock | `overlay-amazon-connect.md` |
| Genesys Cloud CX | `overlay-genesys-cloud-cx.md` |
| Salesforce Agentforce Contact Center | `overlay-salesforce-agcc.md` |
| NICE CXone | `overlay-nice-cxone.md` |

**Reading order:**
1. Read this document first to understand the target architecture.
2. Select the overlay matching the platform under evaluation.
3. Where an overlay diverges from this document's requirements, this document governs — the overlay must explain how the gap is addressed.

**What the overlays add:**
- Mapping of each Architecture Building Block (ABB) to a named vendor product
- Native vs. custom build classification per capability
- Geographic coverage against Belron's opco footprint
- Architecture Principle compliance RAG assessment
- Pricing model summary
- Honest gap analysis

---

## Executive Architecture Diagram

*Simplified view for stakeholder communication. Full detail in sections below.*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ①  CUSTOMER CHANNELS                                                        │
│  Voice / Phone  ·  Chat / WhatsApp  ·  Email / SMS  ·  Video  ·  App / Web │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────────┐
│  ②  AI-FIRST CONTACT LAYER                                                   │
│  LLM-Powered Virtual Agent  ·  Intelligent Routing  ·  Proactive Outreach   │
│  ~60% of contacts resolved without human involvement                        │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │ Escalate with full context
┌──────────────────────────────▼──────────────────────────────────────────────┐
│  ③  HUMAN AGENT WORKSPACE                                                    │
│  Unified Agent Desktop + Real-Time AI Assist  ·  Supervisor + AI QA         │
└──────────────┬──────────────────────────────────────────────┬───────────────┘
               │ Real-time data & guidance                     │ Contact resolved
┌──────────────▼──────────────────────────────────────────────▼───────────────┐
│  ④  BELRON INTELLIGENCE LAYER  (unique — not available from CCaaS vendors)   │
│  VRM / Vehicle Lookup  ·  Insurer Claims API  ·  ADAS Calibration Router    │
│  AI Damage Assessment Engine  ·  Multi-OpCo Routing Logic                   │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │ Governed API calls — audited, identity-bound
┌──────────────────────────────▼──────────────────────────────────────────────┐
│  ⑤  CCAAS CORE PLATFORM  (vendor TBD — see OI-02)                           │
│  ACD · Omnichannel · SIP/WebRTC · Recording · WFM · Analytics · Platform API│
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────────────────┐
│  ⑥  ENTERPRISE INTEGRATION — GOVERNED API GATEWAY                            │
│  Customer Data  ·  Scheduling & Dispatch  ·  Vehicle & Glass                │
│  Claims & Insurer  ·  Knowledge & Policy  ·  Workforce                      │
└─────────────────────────────────────────────────────────────────────────────┘
                    ⇕  Transversal (all layers)
    Semantic Layer (L2)  ·  Contact Audit Store (L4)
    Identity & Access Management  ·  Distributed Observability
```

**Reading the layers:**
- **①–②** Automation-first: resolve without a human wherever possible.
- **③** Assisted human: when a human is needed, they are supported by real-time AI — never starting cold.
- **④** Belron's competitive moat: vehicle, glass, insurer, and calibration intelligence that no generic CCaaS platform provides.
- **⑤** Commodity infrastructure: the CCaaS platform is a deployment decision, not an architectural differentiator.
- **⑥** Governance backbone: every agent-to-system call is logged, identity-bound, and auditable via the Enterprise Integration Gateway.

---

# Phase A — Architecture Vision

## A.1 Purpose

Provide a reference model for the CCOTF programme that:

1. Describes the target-state architecture in **vendor-agnostic component terms**
2. Anchors the programme to Belron's existing business capability model (bridging the capability–technology gap)
3. Makes explicit the connection to the AI Damage Assessment PoC (CCOTF is the delivery channel) and the AI Governance programme (the governance layer for CCOTF's agentic components)
4. Provides a baseline for gap analysis against Belron's current contact centre technology estate
5. Serves as an honest representation of capability requirements, data proximity, and lock-in risk — suitable for exec and IPO-context conversations

## A.2 Scope

**In scope:** The technology components, application services, data flows, and governance controls for Belron's contact centre function across all opcos (Autoglass UK, Carglass EU, Safelite US, and other markets). Target state: AI-native, omnichannel, agentic where appropriate, governed.

**Out of scope:** Individual opco CCaaS configuration; telephony carrier selection; specific insurer API contracts; workforce headcount modelling. These are implementation concerns addressed in vendor overlays or programme workstream plans.

## A.3 Architecture Drivers

| ID | Driver | Source |
|---|---|---|
| D1 | Persistent contact centre problems (routing quality, agent productivity, omnichannel consistency) remain unsolved by vendor AI add-ons — structural redesign is needed | Zoom EBC observation, May 2026: "same problems as HSBC, still problems" |
| D2 | AI-first contact — LLM-powered virtual agents can now resolve 50–60% of contacts without human involvement | Industry data, May 2026 |
| D3 | CCOTF is the delivery channel for the AI Damage Assessment PoC — the two programmes must be architecturally coupled | Consolidation May 2026 |
| D4 | The AI Governance programme provides the upstream governance layer — AI & Automation components and AI model decision-making must sit within it | AI Governance programme (Belron EA) |
| D5 | Belron's domain-specific intelligence (VRM, insurer API, ADAS calibration, multi-opco routing) is the differentiator — not the CCaaS platform | CCOTF component model, May 2026 |
| D6 | IPO (H2 2026) requires demonstrable technology architecture governance — the contact centre is a significant customer-facing investment | Belron exec context |
| D7 | EU AI Act Articles 9/12/14 apply to AI agents making customer-facing decisions (routing, damage assessment, claim eligibility) | EUR-Lex |
| D8 | Multi-agent AI systems amplify semantic inconsistency — without shared vocabulary, parallel agents arrive at different answers to the same question | Darlene Newman / semantic layer governance, May 2026 |

## A.4 Stakeholders and Concerns

| Stakeholder | Primary Concern | Views Addressed |
|---|---|---|
| CIO / Exec | Business case, vendor-neutrality, IPO-readiness | Vision, Technology (vendor selection) |
| CCOTF Programme | Deliverable scope, CCaaS platform choice, AI capability roadmap | Application, Technology, Patterns |
| Customer Experience / Operations | Customer outcomes, agent productivity, omnichannel | Business, Application |
| CISO | AI decisions in customer interactions, data egress, PCI/GDPR | Security, Compliance |
| DPO / Legal | EU AI Act, GDPR for customer contact recordings, AI transparency | Compliance |
| AI Governance Programme (EA) | AI & Automation components and AI model decision points within governance scope | Governance |
| AI Damage Assessment PoC team | Integration point in Layer ④ — CCOTF is the delivery channel | Application |
| BA team | Capability boundary: CCOTF vs. front-office | Business Architecture |
| Integration Platform team | Layer ⑥ — governed API integration with CRM, FSM, insurers | Application, Technology |

## A.5 Architecture Principles

| # | Principle | Rationale | Implication |
|---|---|---|---|
| AP-01 | **AI-first, not agent-first** | ~50–60% of contacts can be resolved without a human; humans add value for complexity and empathy, not repetition | Default to virtual agent resolution; human escalation is the exception, not the default path |
| AP-02 | **Evaluate with explicit rules, not LLM inference** | The Evaluate stage (routing decisions, damage assessment outcomes, claim eligibility) must produce auditable, consistent results. LLM inference at this stage produces variance. | Rule-based evaluation engines layered over LLM retrieval; AI retrieves and reasons, rules decide and log |
| AP-03 | **CCaaS platform is infrastructure; the Belron Intelligence Layer is the moat** | The competitive differentiation is VRM lookup, insurer API integration, ADAS routing, and AI damage assessment — not which CCaaS platform is chosen | Invest deeply in Layer ④ (Belron Intelligence); treat Layer ⑤ (CCaaS) as a commodity infrastructure decision |
| AP-04 | **The CCaaS platform decision unlocks all other technology decisions** | Everything in this reference model either sits on, integrates with, or is constrained by the CCaaS platform. Candidate selection must happen before detailed architecture work proceeds | No detailed technology design on Layers ②–③ or WFM until CCaaS platform is chosen |
| AP-05 | **CCOTF's AI components are governed by the AI Governance programme** | AI decisions in a customer contact are subject to the same audit, identity, and accountability requirements as other enterprise agent actions | Layer ② AI components and all AI decision points are registered with and governed by the AI Governance programme |
| AP-06 | **Architecture must honestly represent capability ownership and data proximity** | Vendor EBC content presents polished demos; architecture must show where data lives and which vendor controls it | Vendor overlays explicitly surface lock-in risk, data residency, and portability; these are surfaced before platform decisions |
| AP-07 | **Semantic consistency is governed, not assumed** | AI agents operating across channels will each interpret business terms (customer, case, closed, authorised) independently unless a shared semantic layer governs meaning | Controlled vocabulary is a pre-requisite for multi-agent CCOTF deployments; semantic layer is a pre-Phase 1 dependency |
| AP-08 | **Customer-facing AI must comply with EU AI Act Article 13 transparency** | Customers must be informed when interacting with an AI system | All virtual agent and automated decision touchpoints include disclosure |
| AP-09 | **Multi-opco architecture is the default** | Belron operates in 35+ countries with multiple brands; the architecture must accommodate Autoglass, Carglass, Safelite, and others | CCaaS platform must support multi-brand, multi-language, multi-region; single-opco deployments are pilots, not the target state |

---

# Phase B — Business Architecture

## B.1 Business Capabilities — CCOTF Scope

The six architectural layers map to five core business capability clusters. The boundary between CCOTF and the broader front-office is indicated — this boundary is not yet formally resolved (OI-01).

| Capability Cluster | Core Capabilities | CCOTF / Front-office? |
|---|---|---|
| Customer Contact & Routing | Omnichannel intake, intent recognition, intelligent routing, callback management | CCOTF primary |
| Assisted Resolution | Agent productivity, real-time AI guidance, knowledge surfacing, case management | CCOTF primary |
| Vehicle & Glass Intelligence | VRM lookup, glass type identification, damage assessment, ADAS detection | Shared — CCOTF (channel) + AIDA PoC (AI capability) |
| Claims & Insurer Interaction | FNOL, insurer pre-authorisation, claim status, settlement | Shared — CCOTF (interaction) + Claims domain (process) |
| Workforce & Quality | Agent scheduling, QA, coaching, performance | CCOTF primary |
| Self-Service & Proactive | Online booking, appointment tracking, proactive outreach | Boundary TBD — CCOTF vs. Front-office |

## B.2 Business Actors

| Actor Class | Description | CCOTF Role |
|---|---|---|
| Customer | Belron end customer (vehicle owner, insurer) | Initiates contact via any channel |
| Contact Centre Agent | Belron employee handling customer contacts | Assisted by AI; escalation target |
| Supervisor | Team leader / floor manager | AI-augmented monitoring and coaching |
| Virtual Agent | AI Actor — autonomous first-line resolution | First contact; resolves or escalates with context |
| Agentic Workflow | AI Actor — autonomous multi-step back-office task completion | Post-resolution automation (job creation, claim submission) |
| Insurer / Third Party | External system — automated API interaction | Real-time claim authorisation via API |
| Technician | Field employee — receives job from Field Service Management | Downstream recipient of CCOTF-initiated work |

Virtual Agent and Agentic Workflow are **first-class architecture actors** — they appear in the capability model alongside human roles, with named owners and accountability chains.

## B.3 Value Streams

**Value Stream 1: Customer → Repair/Replace**
```
Customer Contact → Damage Triage → Insurer Authorisation → Job Booking →
Technician Dispatch → Repair/Replace → ADAS Calibration (if required) → Claim Settlement
```
CCOTF owns the first four stages. The AI Damage Assessment PoC (AIDA) is the AI capability in stage two.

**Value Stream 2: Incident → IT Resolution** *(out of CCOTF scope — owned by ITSM programme)*

## B.4 Capability Boundary — Open Issue

The boundary between CCOTF and the broader front-office function is not formally resolved. Key overlap areas: online booking, appointment self-service, and proactive customer communication. Live EA action item — see OI-01.

---

# Phase C — Information Systems Architecture

## C.1 Data Architecture

### C.1.1 Contact Centre Data Model (layered)

```
┌──────────────────────────────────────────────────────────────────┐
│  L0  Source-of-record systems (CRM, FSM, Claims, VRM, ADAS DB)   │
├──────────────────────────────────────────────────────────────────┤
│  L1  Integration layer (real-time feeds via integration platform) │
├──────────────────────────────────────────────────────────────────┤
│  L2  Semantic Layer — controlled vocabulary, governed metrics     │
│      "customer", "job", "case closed", "authorised" defined once  │
├──────────────────────────────────────────────────────────────────┤
│  L3  AI Context Layer — real-time enriched customer/vehicle view  │
│      Contact history + VRM + damage + insurer status + intent     │
├──────────────────────────────────────────────────────────────────┤
│  L4  Recording & Audit Layer — all contacts, AI decisions, HITL   │
│      Immutable storage; GDPR retention; EU AI Act Art. 12         │
└──────────────────────────────────────────────────────────────────┘
```

**The semantic layer obligation (AP-07):** Without L2, a Virtual Agent routing based on "is the customer's case open?" and an Agentic Workflow deciding "is this case closed enough to trigger claim settlement?" will interpret the same state differently. L2 is the prerequisite for safe multi-agent contact centre operation.

### C.1.2 Data Classification

| Class | Examples | Handling |
|---|---|---|
| `public` | Branch locations, pricing, glass spec | No restriction; cacheable |
| `internal` | Agent scripts, routing logic, insurer codes | Authenticated agents only |
| `confidential` | Customer name, contact history, VRM | GDPR-grade; EU data stays in EU |
| `restricted` | Payment card data, call recordings, medical/disability notes | PCI controls; pause/resume recording; explicit consent |

### C.1.3 Canonical Contact Record

All contacts generate an immutable audit record satisfying EU AI Act Article 12:

```
contact_record {
  contact_id, channel, opco, region,
  customer_identity? (if authenticated),
  virtual_agent_session_id?, agent_id?,
  routing_decision { model_version, intent, confidence, rule_applied },
  ai_damage_assessment_result? { model_version, result, confidence },
  insurer_api_call? { insurer_id, authorisation, timestamp },
  hitl_event? { agent_id, decision, duration },
  recording_reference?, transcript_reference?,
  outcome, resolution_time,
  timestamp_utc, retention_expiry
}
```

## C.2 Application Architecture

### C.2.1 Application Layer Stack

```
┌──────────────────────────────────────────────────────────────────────┐
│  ① Customer Channels  (Voice · Chat · Email · Video · App/Web)        │
├──────────────────────────────────────────────────────────────────────┤
│  ② AI-First Contact Layer                                             │
│     Virtual Agent Platform  ·  Intelligent Routing Engine             │
│     Proactive Outreach Orchestrator  ·  Sentiment Detector            │
│     Real-Time Transcription Service                                   │
├──────────────────────────────────────────────────────────────────────┤
│  ③ Human Agent Workspace                                              │
│     Unified Agent Desktop  ·  Real-Time Agent Assist Engine           │
│     Knowledge Surfacing Service  ·  After-Call Work Assistant         │
│     AI Quality Assurance  ·  Supervisor Intelligence View             │
├──────────────────────────────────────────────────────────────────────┤
│  ④ Belron Intelligence Layer  ← competitive differentiator            │
│     VRM / Vehicle Lookup Service  ·  Glass Type Identifier            │
│     AI Damage Assessment Engine  ·  Insurer Claims API Connector      │
│     ADAS Calibration Router  ·  Multi-OpCo Routing Logic              │
├──────────────────────────────────────────────────────────────────────┤
│  ⑤ CCaaS Core Platform  (vendor TBD — see OI-02)                      │
│     ACD  ·  Omnichannel Routing  ·  SIP/WebRTC  ·  Recording         │
│     WFM  ·  Analytics  ·  Platform API                               │
├──────────────────────────────────────────────────────────────────────┤
│  ⑥ Enterprise Integration — Governed API Gateway                      │
│     Customer Data  ·  Scheduling & Dispatch  ·  Vehicle & Glass      │
│     Claims & Insurer  ·  Knowledge & Policy  ·  Workforce             │
└──────────────────────────────────────────────────────────────────────┘
                ⇕ (transversal)
    Semantic Layer (L2)  ·  Audit & Recording (L4)
    Identity & Access Management  ·  Distributed Observability
```

### C.2.2 Canonical Application Components

*ArchiMate notation: `[A]` = Application Component, `[AS]` = Application Service, `[AI]` = Application Interface.*

#### Layer ②: AI-First Contact Layer

| Component | Type | Vendor-Agnostic Requirement |
|---|---|---|
| Virtual Agent Platform | [A] | LLM-powered conversational AI; handles intent recognition, dialogue management, and self-service resolution across all text and voice channels. Must be a GenAI agent, not a rules-based chatbot. Multi-language, multi-brand. |
| Intelligent Routing Engine | [A] | Translates resolved intent + customer context + real-time queue state → routing decision. Per AP-02: routing decision uses rule-based evaluation over LLM-extracted intent. Must support skills-based, attribute-based, and predictive routing. |
| Proactive Outreach Orchestrator | [A] | AI-triggered outbound: appointment reminders, claim status updates, proactive contact prevention. Consumes predictive contact prevention signals. |
| Sentiment and Emotion Detector | [AS] | Real-time tone/emotion signal during voice contacts; feeds routing escalation (distressed customer → priority queue) and supervisor alerts. |
| Real-Time Transcription | [AS] | Real-time speech-to-text for voice contacts; feeds Agent Assist Engine, QA, and contact audit record. Must support English (UK), French, German, Dutch, and other Belron opco languages. |

#### Layer ③: Human Agent Workspace

| Component | Type | Vendor-Agnostic Requirement |
|---|---|---|
| Unified Agent Desktop | [A] | Single interface across all channels; screen-pop on contact arrival with pre-loaded customer context. Must not require agents to switch between multiple tools. |
| Real-Time Agent Assist Engine | [A] | Surfaces next-best-action, KB articles, and suggested responses live during contact. Does not auto-send — agent decides. Must reduce after-call work, not add to it. |
| Knowledge Surfacing Service | [AS] | Semantic search over knowledge base; AI-ranked results matched to current contact context, not keyword search. Must support multi-language KB. |
| After-Call Work Assistant | [AS] | AI-generated contact summary, disposition suggestion, auto-logging to CRM. Agent confirms rather than manually enters. |
| AI Quality Assurance | [A] | 100% contact scoring against a configurable QA rubric; replaces or supplements manual sampling. Results feed coaching agenda. |
| Supervisor Intelligence View | [A] | Real-time floor view with AI anomaly highlighting; listen/barge/whisper; sentiment alerts. |

#### Layer ④: Belron Intelligence Layer

This layer has no equivalent in any generic CCaaS reference architecture. It must be built or integrated regardless of CCaaS platform choice.

| Component | Type | Vendor-Agnostic Requirement | Integration |
|---|---|---|---|
| VRM / Vehicle Lookup Service | [A] | Receives vehicle registration mark → returns vehicle make/model/year, glass specifications, ADAS sensor presence, and calibration requirements. Must support UK, EU, and US plate formats. | Feeds routing engine, agent desktop, damage assessment |
| Glass Type Identifier | [AS] | Identifies OEM vs. aftermarket glass, acoustic/solar variants, part numbers for the confirmed vehicle | Feeds repair/replace decision, insurer authorisation |
| AI Damage Assessment Engine | [A] | Photo/video → AI analysis → repair or replace recommendation with confidence score. Per AP-02 and RP-03: results below confidence threshold route to human review. | **AIDA PoC integration point** |
| Insurer Claims API Connector | [A] | Real-time pre-authorisation request to insurer → approved/declined/referred within contact duration. Per-insurer adapters required. | Enterprise Integration Gateway (Claims & Insurer service domain) |
| ADAS Calibration Router | [AS] | Identifies calibration requirement from VRM data → applies skills-based routing to ADAS-certified technician and appropriate depot | Feeds routing engine; affects field service job type |
| Multi-OpCo Routing Logic | [AS] | Brand, language, geography, and regulatory routing across Autoglass, Carglass, Safelite, and others. Brand-of-contact determines context from the moment of inbound identification. | CCaaS Platform API |

#### Layer ⑤: CCaaS Core Platform

**The platform choice is open — OI-02.** This layer is represented as a single [A] with sub-components. The specific vendor is a parameter resolved in the vendor overlays.

| Sub-component | Vendor-Agnostic Requirement |
|---|---|
| ACD / Omnichannel Router | Automatic call distribution + cross-channel routing. Must integrate with the Intelligent Routing Engine (Layer ②) via API. |
| SIP / WebRTC | Carrier and browser-based voice. Must support number portability across Belron opcos. |
| Call Recording and Archiving | Full contact recording with compliance controls. AI-indexed; feeds QA and audit store. GDPR-compliant EU data residency. |
| Workforce Management | Forecasting, scheduling, and adherence. Must support multi-site, multi-skill, and AI-enhanced demand forecasting. |
| CCaaS Analytics | Contact centre KPI and reporting. Must expose data to external analytics platform. |
| Platform API | Developer APIs for customisation and integration. Must support Layer ④ components; open standards preferred. |

**Platform selection requirement (OI-02):** The CCaaS platform must satisfy the following non-negotiable criteria before selection:
- Multi-brand, multi-language, multi-region support without separate deployments
- Open API surface sufficient for Layer ④ integration (VRM, insurer, ADAS)
- LLM integration capability for Layer ② (either native or via open model API)
- GDPR-compliant EU data residency for Carglass markets
- Geographic availability covering UK, EU (France, Germany, Belgium, Italy minimum), and US

See individual vendor overlays for assessment against these criteria.

#### Layer ⑥: Enterprise Integration — Governed API Gateway

This layer connects CCOTF's AI and human agents to Belron's enterprise systems of record through a governed, audited integration fabric. Every agent-to-system call must be authenticated, authorised, and logged — governance is built in at the integration layer, not bolted on.

The integration technology (API gateway, event streaming, integration platform, AI tool protocol) is a vendor decision addressed in the overlays and the AI Governance programme. The capability domains required are:

| Integration Domain | Capability | Priority |
|---|---|---|
| Customer Data | Customer profile, contact history, preferences, authentication | Immediate |
| Scheduling & Dispatch | Job scheduling, technician dispatch, depot capacity, SLA management | Immediate |
| Vehicle & Glass | Vehicle master data, glass specifications, ADAS configuration | Immediate |
| Claims & Insurer | FNOL, insurer pre-authorisation, claim status, settlement triggers | Phase 2 |
| Knowledge & Policy | Technical procedures, insurer requirements, SOPs, product catalogue | Immediate |
| Workforce | Agent skills, availability, language capability, shift data | Phase 2 |

**Integration governance requirements (all domains):**
- All calls authenticated to a named agent or system identity
- All calls audit-logged with timestamp, caller identity, parameters, and result
- Data residency enforced per contact's opco (EU data stays in EU)
- Sensitive data (PCI, GDPR-restricted) never passed in clear text through the integration layer

---

# Phase D — Technology Architecture

## D.1 Technology Layer (Abstract)

```
┌──────────────────────────────────────────────────────────────────┐
│  [N] Multi-Region Compute  (cloud + on-prem where required)       │
│      EU Zone (GDPR) · US Zone (Safelite) · Shared Services        │
├──────────────────────────────────────────────────────────────────┤
│  [SS] CCaaS Platform  (vendor TBD — OI-02)                        │
│  [SS] Enterprise Integration Gateway  (vendor TBD)                │
│  [SS] Service Mesh  (mutual TLS for inter-service communication)  │
├──────────────────────────────────────────────────────────────────┤
│  [TS] LLM Provider  (vendor TBD — see vendor overlays)            │
│  [TS] Real-Time Transcription  (vendor TBD)                       │
│  [TS] Identity & Access Management  (enterprise IdP — vendor TBD) │
│  [TS] Recording Storage  (GDPR-compliant; EU-region anchored)     │
│  [TS] Audit Storage  (Immutable WORM — EU AI Act Art. 12)         │
│  [TS] Distributed Observability  (vendor TBD)                     │
│  [TS] Semantic Layer  (governed vocabulary — TBD via PoC)         │
│  [TS] PCI Compliance Controls  (pause/resume, secure IVR)         │
└──────────────────────────────────────────────────────────────────┘
```

## D.2 Key Technology Decisions

| Decision | Requirement | Status | Resolved In |
|---|---|---|---|
| CCaaS Platform | Must meet Layer ⑤ requirements above | **Open — OI-02** | Vendor overlay + CIO decision |
| LLM Provider | Vendor TBD via vendor overlays; Anthropic preferred for AIDA alignment | Dependency on CCaaS and cloud choice | Vendor overlay |
| Real-Time Transcription | Multi-language; feeds QA and audit; GDPR-compliant | Dependency on CCaaS choice | Vendor overlay |
| AI Damage Assessment Engine | AIDA PoC output; integration via Layer ④ | **Dependency on AIDA PoC — OI-05** | AIDA programme |
| Semantic Layer | Governed vocabulary for cross-agent consistency; shared with AI Governance programme | **Open — OI-08** | EA-led initiative |
| Recording Storage | GDPR EU-region primary; immutable WORM for compliance | Architecture defined | Vendor overlay specifies platform |
| VRM Lookup | UK/EU/US plate formats; real-time; feeds routing | **Open — OI-04** | CCOTF Technical Ops |
| Insurer API Integration | Per-insurer adapters; real-time response within contact duration | Architecture defined; adapters TBD | Integration Platform |

## D.3 Deployment Topology

| Zone | Scope | Key Constraint |
|---|---|---|
| EU Zone (primary) | Autoglass UK, Carglass EU opcos | GDPR; EU AI Act; EU data stays in EU |
| US Zone | Safelite | US data sovereignty; may use separate CCaaS instance |
| Shared Services | Cross-opco: semantic layer, audit aggregation, integration gateway federation | Non-personal-data only crosses zones |

---

# Reference Patterns Catalogue

### RP-01 AI-First, Human-in-Reserve
Virtual Agent is the first-contact handler on all channels. Human agents receive escalations with full AI-generated context packet (customer summary, intent, prior turns, VRM data). No human starts a contact cold.

### RP-02 Rule-Evaluated AI Outputs
AI models (LLM, damage assessment) produce structured output. A rule-based evaluation engine — not the LLM — makes the decision: route, repair/replace, authorise. The AI retrieves and reasons; the rule decides and logs. Satisfies EU AI Act Art. 14 (human oversight by design) and produces auditable decisions.

### RP-03 Confidence-Gated HITL
AI decisions below a configured confidence threshold are intercepted before action is taken. Example: damage assessment confidence < 80% → routes to specialist agent for human review. Threshold is configurable per decision type.

### RP-04 Belron Intelligence Enrichment
On every contact, VRM lookup triggers automatically on authentication. The returned vehicle profile (glass specs, ADAS presence, calibration requirements) pre-populates the routing engine, agent desktop, and damage assessment context. No agent manually looks up vehicle data.

### RP-05 Real-Time Insurer Authorisation
Insurer API calls are made during the contact, not post-contact. The routing engine requests insurer pre-authorisation for the likely job type as soon as intent and VRM are resolved. Result is available to the agent before they take the call. Reduces contact duration and improves first-call resolution.

### RP-06 Multi-OpCo Context Switching
A contact arriving on an Autoglass UK number is processed under UK brand context, UK language model, UK insurer rules, and UK data residency. Carglass DE contacts use German context. The architecture routes by opco brand from the moment of inbound contact identification.

### RP-07 100% AI Quality Assurance
Every contact (all channels, all agents, all virtual agent sessions) is scored by the AI QA component against a configurable rubric. No sampling. Results feed coaching agendas, not automated performance management (AP-02: rules decide outcomes, not AI scores alone).

### RP-08 Proactive Contact Prevention
AI predicts which customers are likely to contact (appointment concerns, claim delays, post-repair queries) and triggers proactive outreach before they call. Requires real-time customer data from the Customer Data integration domain (Layer ⑥).

---

# Architecture Building Blocks (ABBs)

| ID | ABB Name | Layer | Capability Description | Implementation Requirement |
|---|---|---|---|---|
| ABB-C01 | Channel Adapter | ① | Normalises inbound contacts from all channel types into a common interaction object | Must support: voice (PSTN + VoIP), chat, email, SMS, WhatsApp Business, video, web/app. See vendor overlay for native vs. partner channels. |
| ABB-C02 | Virtual Agent Platform | ② | LLM-powered conversational AI for first-line resolution | Must use LLM-native reasoning (not rules trees); multi-language; capable of multi-turn dialogue; integrates with Layer ④ for VRM and damage context |
| ABB-C03 | Intelligent Routing Engine | ② | Intent + context + queue → routing decision | Must support skills-based, attribute-based, and predictive routing; AP-02: routing decisions are rule-evaluated, not LLM-decided |
| ABB-C04 | Proactive Outreach Orchestrator | ② | AI-triggered outbound contact initiation | Must consume predictive signals from the Customer Data integration domain (Layer ⑥); support voice, SMS, and email outbound |
| ABB-C05 | Real-Time Transcription | ② | Speech-to-text during live voice contacts | Must support Belron opco languages; output feeds ABB-C07 and ABB-C08 simultaneously; latency < 2s |
| ABB-C06 | Unified Agent Desktop | ③ | Single-pane agent interface across all channels | Must surface VRM data, contact history, AI Assist, and case management in one view; no manual application switching |
| ABB-C07 | Real-Time Agent Assist Engine | ③ | Live next-best-action and knowledge surfacing | Suggestions not auto-applied; agent confirms; must integrate with ABB-C16 (knowledge) |
| ABB-C08 | AI Quality Assurance | ③ | 100% automated contact scoring | Must score all channels (not voice only); output is coaching input, not automated HR action |
| ABB-C09 | VRM / Vehicle Lookup Service | ④ | VRM → vehicle profile lookup | Real-time; < 1s latency during routing; must support UK, EU, US plate formats; triggers on every authenticated contact |
| ABB-C10 | AI Damage Assessment Engine | ④ | Photo/video → repair/replace recommendation | AIDA PoC integration point; confidence-gated per RP-03; result logged in contact record |
| ABB-C11 | Insurer Claims API Connector | ④ | Real-time insurer pre-authorisation | Must respond within contact duration (~30s); per-insurer adapters; routed via the Claims & Insurer integration domain (Layer ⑥); high-value jobs require HITL override |
| ABB-C12 | ADAS Calibration Router | ④ | Identifies calibration requirement → specialist routing | Triggered by VRM data; must integrate with skills-based routing in CCaaS platform |
| ABB-C13 | Multi-OpCo Routing Logic | ④ | Brand/language/geo routing | Routes by opco brand from inbound identification; GDPR-aware data residency per contact |
| ABB-C14 | CCaaS Core Platform | ⑤ | ACD, omnichannel, recording, WFM, analytics | Vendor TBD — OI-02; must satisfy Layer ⑤ non-negotiable criteria above |
| ABB-C15 | Enterprise Integration Gateway | ⑥ | Governed, audited, identity-bound API access to enterprise systems | Vendor TBD; must enforce: authentication of all callers, authorisation per caller identity, immutable audit log of all calls, data residency per opco zone. Integration technology (API gateway, event streaming, AI tool protocol) is an implementation choice resolved in vendor overlays. |
| ABB-C16 | Semantic Layer | Transversal | Controlled vocabulary for cross-agent consistency | Pre-requisite for multi-agent deployment; shared initiative with AI Governance programme — OI-08; technology TBD |
| ABB-C17 | Contact Audit Store | Transversal | Immutable record of all contacts and AI decisions | WORM-compliant immutable storage; GDPR-compliant retention; satisfies EU AI Act Art. 12; EU-region anchored; vendor TBD via overlay |
| ABB-C18 | Observability Plane | Transversal | End-to-end telemetry across all layers | Distributed tracing and metrics across all layers; must feed existing enterprise observability estate; vendor TBD |
| ABB-C19 | PCI Compliance Controls | Transversal | Payment card data isolation during contacts | Pause/resume recording API; card numbers never enter LLM context; CCaaS platform PCI-DSS scope |

---

# Regulatory and Compliance Standards

The following are non-negotiable mandatory requirements — they apply regardless of vendor or technology choices. Technology standards (API protocols, integration standards, observability frameworks) are implementation decisions resolved in the vendor overlays.

| Standard / Regulation | Scope | Conformance |
|---|---|---|
| GDPR | All contact data for EU opco customers | Mandatory — EU data stays in EU; retention, consent, subject access rights |
| EU AI Act | All AI systems making customer-facing decisions (routing, damage assessment, claim eligibility) | Mandatory — Art. 9 risk management, Art. 12 logging, Art. 13 transparency, Art. 14 human oversight |
| PCI-DSS v4.0 | Payment card data in IVR and agent-handled contacts | Mandatory — pause/resume recording; card numbers never in LLM context or unencrypted storage |
| Ofcom / national telecoms regulation | Voice services per country | Per-opco compliance — number porting, emergency services, CLI rules |
| GDPR-equivalent data protection laws | Non-EU opcos (UK GDPR, US state laws for Safelite) | Per-jurisdiction; mapped in deployment topology |

**Technology standards note:** The choice of integration protocol, identity standard, API specification, and observability framework are vendor and implementation decisions. These will be specified in the CCaaS selection decision (OI-02) and the AI Governance programme framework. They do not belong in this vendor-agnostic RA.

---

# Security Architecture

## SA.1 Contact Centre Threat Model

| Threat | Control |
|---|---|
| Customer identity fraud (caller impersonation) | VRM-based verification as secondary factor; voice biometrics evaluated |
| AI routing manipulation (customer gaming the virtual agent) | Intent confidence thresholds; rule-evaluated outcomes per AP-02; agent review for ambiguous intents |
| Prompt injection via customer inputs | Input sanitisation before LLM context; Virtual Agent system prompt isolated from user turn |
| Insurer API abuse (fraudulent authorisation requests) | Insurer API call authenticated to agent identity via Enterprise Integration Gateway; HITL for above-threshold job values |
| Call recording exfiltration | Immutable storage; access logs; DLP on recording retrieval |
| PCI data in LLM context | Pause/resume controls; payment card numbers never enter LLM context |
| AI Quality score manipulation | QA model outputs version-pinned and logged; scores are coaching inputs, not automated actions |

## SA.2 EU AI Act Compliance Mapping

| Article | Obligation | Architectural Control |
|---|---|---|
| Art. 9 — Risk Management | Document risk for each AI decision in a customer interaction | AI Actor registration includes risk classification; damage assessment and routing flagged as high-risk |
| Art. 12 — Logging | Lifetime automatic logging of AI operations | ABB-C17 Contact Audit Store; all AI decisions logged with model version and confidence |
| Art. 13 — Transparency | Customer informed when interacting with AI | AP-08 — disclosure in virtual agent opening turn |
| Art. 14 — Human Oversight | Effective human oversight | RP-02 Rule-Evaluated AI Outputs; RP-03 Confidence-Gated HITL |

---

# Governance Framework

## G.1 Relationship to the AI Governance Programme

The CCOTF reference architecture is **subordinate** to the Belron AI Governance programme. Specifically:
- Layer ② AI components (Virtual Agent, Intelligent Routing, AI Damage Assessment Engine) are registered as governed AI actors in the enterprise AI registry
- AI Model Governance is not a separate CCOTF concern — it is the AI Governance programme's domain, applied to CCOTF use cases
- All AI-to-system calls from CCOTF components pass through the Enterprise Integration Gateway; CCOTF does not maintain its own integration gateway

## G.2 Architecture Compliance Review Checklist

A CCOTF project or sub-project completes an Architecture Compliance Review (ACR) that checks:

1. Architecture Principles AP-01 through AP-09 (above)
2. AI Governance programme principles (as published)
3. CCaaS platform alignment (no shadow CCaaS deployments)
4. Belron Intelligence Layer components used — not reimplemented per-project
5. EU AI Act risk classification declared for all AI decision components
6. Semantic layer vocabulary coverage for all new business terms
7. Multi-opco routing behaviour documented
8. PCI and GDPR data flows confirmed

## G.3 Decision Rights

| Decision | Owner | Consulted |
|---|---|---|
| CCaaS platform selection | CIO + CCOTF Programme | EA, CISO, Legal, Procurement |
| New AI Actor registration | EA | CISO, DPO, CCOTF Programme |
| New integration service domain | EA + Capability Owner | DPO, CISO |
| Insurer API onboarding | Integration Platform + Claims | Legal, CISO |
| Confidence threshold adjustment | CCOTF Programme | EA, CISO (for HITL-affecting changes) |
| Semantic layer term addition | EA + BA team | Capability owners |

---

# Programme Phasing

| Phase | Scope | Dependencies |
|---|---|---|
| **Phase 0 — Foundation** | CCaaS platform decision; current-state gap analysis; Enterprise Integration Gateway selection; semantic layer scoping | OI-02 (CCaaS) and OI-03 (current estate) must be resolved first |
| **Phase 1 — Core AI Contact** | Virtual Agent on primary channels; Intelligent Routing; VRM lookup; agent desktop with Real-Time Assist | CCaaS platform selected |
| **Phase 2 — Belron Intelligence** | AI Damage Assessment integration (AIDA PoC → CCOTF); Insurer API real-time authorisation; ADAS calibration routing | AIDA PoC Phase 1 complete |
| **Phase 3 — Full Omnichannel** | All channels live; 100% AI QA; proactive outreach; full multi-opco deployment | Phases 1 and 2 stable |
| **Phase 4 — Agentic Back-Office** | Post-contact agentic workflows (auto job creation, auto claim submission, auto scheduling) via Enterprise Integration Gateway | Integration Gateway Phases 2–3 complete |

---

# Open Issues

| ID | Issue | Decision Needed By | Owner |
|---|---|---|---|
| OI-01 | CCOTF vs. front-office capability boundary — not formally resolved | Q3 2026 | EA + BA team |
| OI-02 | CCaaS platform selection — most consequential single technology decision | Q3 2026 | CIO + CCOTF Programme |
| OI-03 | Current Belron contact centre platform — not confirmed in architecture record | Immediately | EA — desk research |
| OI-04 | VRM / Vehicle Lookup solution — no confirmed Belron VRM solution | Q3 2026 | CCOTF Programme + Technical Ops |
| OI-05 | AI Damage Assessment Engine — dependent on AIDA PoC outcomes | Q4 2026 | AIDA PoC team |
| OI-06 | Insurer API integration — per-insurer adapters needed; no current map of insurer connectivity | Q3 2026 | Integration Platform |
| OI-07 | OneNote migration — UC/CCaaS architecture notes not yet in COG | Overdue | Armo |
| OI-08 | Semantic layer scope — one initiative covering CCOTF and AI Governance programme, or two? | Q2 2026 | EA |
| OI-09 | Multi-opco CCaaS topology — single global instance vs. regional instances | Q3 2026 | CIO + CCOTF Programme |

---

*v0.3 working draft — 2026-06-20. Vendor-agnostic base: technology assumptions removed; all implementation choices deferred to vendor overlays.*
*Supersedes: v0.2 (2026-06-19) and `05-knowledge/research/2026-05-23-ccotf-reference-architecture.md` (v0.1)*
*EA Owner: Armo · Belron Enterprise Architecture*
