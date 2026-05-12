---
type: "braindump"
domain: "project-specific"
project: "contact-centre-future"
date: "2026-05-07"
created: "2026-05-07 09:34"
themes: ["technology-reference-model", "contact-centre", "CCOTF", "architecture", "component-model"]
tags: ["#braindump", "#CCOTF", "#contact-centre", "#technology-model", "#enterprise-architecture", "#reference-model"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-05-12]]"
consolidated_date: "2026-05-12"
energy_level: "high"
emotional_tone: "analytical"
confidence: "high"
---

# Braindump: CCOTF Technology Component Reference Model

## Raw Thoughts
Build out a model of the Contact Centre of the Future from a technology component perspective. I need a standard model that I can use to model the contact centre technology in use at Belron against. We have a business capability model — but I need a technology component view.

---

## Content Analysis

### Main Themes
1. **The gap between business capability model and technology architecture:** Belron has a BC model for CCOTF but no technology component reference model to map current and target technology against.
2. **A standard reference model as a comparison baseline:** The value is in using an industry-standard model as the neutral reference — then overlaying Belron's current technology to identify gaps, overlaps, and evolution targets.
3. **Technology component view as an EA artefact:** This is a TOGAF-style Application/Technology Architecture deliverable — the technology layer that sits beneath the capability model.

### Questions Raised
- What is Belron's current contact centre platform? (CCaaS provider? IVR? CRM?)
- Which of the technology domains are already covered by Belron's existing tech stack, and which are gaps?
- Which components are owned by the CCOTF programme vs. the broader IT estate?
- How does the AI Damage Assessment PoC integrate into the CCOTF technology stack?
- What does the insurer API integration layer currently look like at Belron?

---

## The Reference Model

### Contact Centre Technology Component Model (Standard Reference)

The model is organised into **12 technology domains**, from customer-facing interaction through to back-office integration. Each domain contains the standard component categories that a modern contact centre (and an AI-native CCOTF) would include.

---

### Domain 1: Customer Interaction Channels
*How customers reach the contact centre*

| Component | Description | CCOTF Evolution |
|---|---|---|
| Voice / Telephony (inbound) | PSTN / SIP-based inbound calls | Retained but AI-routed |
| Voice / Telephony (outbound) | Outbound dialler, callback | AI-triggered outbound |
| IVR (Interactive Voice Response) | DTMF/speech-driven self-service tree | Replaced by Conversational AI |
| Web Chat (live agent) | Browser-based chat to human agent | Hybrid AI/human |
| Chatbot / Virtual Agent | Automated chat self-service | AI-native, LLM-powered |
| Email | Inbound email handling | AI triage and auto-response |
| SMS / Messaging | Text-based interaction | WhatsApp Business API, RCS |
| WhatsApp / Messaging Apps | WhatsApp Business, Apple Messages | AI-first channel |
| Video | Video-assisted service | Damage assessment use case |
| Social Media | DM handling (Facebook, Twitter/X) | Social listening + AI routing |
| In-App / Mobile | Native app contact within mobile apps | Deep-link to booking/assessment |
| Web Self-Service | Online account, booking, tracking | AI-augmented |

---

### Domain 2: Routing & Orchestration
*Getting contacts to the right place*

| Component | Description | CCOTF Evolution |
|---|---|---|
| ACD (Automatic Call Distributor) | Inbound call routing engine | Replaced/supplemented by AI router |
| Omnichannel Routing Engine | Cross-channel contact routing | AI intent-based routing |
| Skills-Based Routing | Route to agent by skill/language/specialism | AI-enriched skills matching |
| Priority & Queue Management | Queue position, SLA management | Predictive queue management |
| Intelligent / AI Routing | Intent detection → routing decision | Core CCOTF capability |
| Callback Management | Scheduled and virtual callback | AI-predicted demand scheduling |
| Overflow / Partner Routing | Routing to 3rd party / outsource | Automated handoff |
| Proactive Outreach Orchestration | AI-triggered outbound contact | Claim status, appointment reminders |

---

### Domain 3: Agent Desktop & Workspace
*What the agent sees and uses during a contact*

| Component | Description | CCOTF Evolution |
|---|---|---|
| Unified Agent Desktop | Single screen across channels | AI-embedded desktop |
| CTI (Computer Telephony Integration) | Screen-pop on call arrival | Retained, integrated with AI |
| CRM Integration / Customer View | Customer data surfaced in desktop | Real-time AI-enriched customer view |
| Case / Ticket Management | Logging, tracking interactions | AI auto-logging and summary |
| Guided Scripts / Workflows | Step-by-step agent guidance | AI-generated next-best-action |
| Knowledge Base Access | In-desktop KB search | AI-surfaced knowledge (no search needed) |
| Co-browse / Screen Share | Agent sees customer's browser | Retained for complex self-service |
| After-Call Work (ACW) Tools | Wrap-up, disposition coding | AI auto-wrap, disposition suggestion |
| Real-Time Agent Assist | Live AI prompts during contact | Core CCOTF AI agent support layer |
| Supervisor Tools | Listen, barge, whisper, monitoring | AI-augmented supervisory view |

---

### Domain 4: AI & Automation
*The intelligence and automation layer — the defining domain for CCOTF*

| Component | Description | CCOTF Evolution |
|---|---|---|
| Conversational AI Platform | NLU/NLP engine (intent, entity extraction) | Core platform — LLM-powered |
| Virtual Agent / Chatbot Platform | Self-service conversation management | AI-native (GenAI, not rules-based) |
| Large Language Model (LLM) Integration | Foundation model API (Claude, GPT, Gemini) | Central to CCOTF AI capabilities |
| Real-Time Transcription | Live speech-to-text during voice contact | Feeds agent assist and QA |
| Sentiment & Emotion Detection | Real-time tone/emotion analysis | Agent alert + supervisor routing |
| Real-Time Agent Assist Engine | Surfacing guidance, KB articles, responses live | Key productivity tool |
| Next-Best-Action / Recommendation | Predictive guidance on what to do/say | Powered by ML + journey data |
| Robotic Process Automation (RPA) | Automating repetitive back-office steps | Reduced via agentic AI |
| Agentic AI Orchestration | Multi-step autonomous task completion | CCOTF differentiator — long-running workflows |
| AI Quality Assurance | Automated contact scoring and QA | 100% contact coverage (vs. sample) |
| Speech Analytics | Post-contact analysis of voice recordings | VoC, compliance, QA |
| Text Analytics | Analysis of chat, email, social content | VoC and trend detection |
| Predictive Contact Prevention | Identify at-risk customers before they contact | Proactive outreach, deflection |
| **AI Damage Assessment Integration** | Photo/video analysis → repair/replace decision | Direct link to AI Damage Assessment PoC |

---

### Domain 5: Workforce Management & Engagement
*Managing and developing the human workforce*

| Component | Description | CCOTF Evolution |
|---|---|---|
| Workforce Management (WFM) | Forecasting, scheduling, adherence | AI-enhanced demand forecasting |
| Quality Management (QM) | Manual/automated quality scoring | AI QA replaces/supplements manual |
| Agent Coaching Platform | Structured feedback and coaching tools | AI-identified coaching moments |
| Learning Management System (LMS) | Training delivery and tracking | AI-personalised learning paths |
| Performance Management | KPI tracking, scorecards | AI-generated performance insight |
| Gamification | Engagement and motivation tools | Real-time AI-personalised incentives |
| Agent Wellbeing Tools | Fatigue, stress, sentiment monitoring | AI early-warning for burnout |
| Scheduling Self-Service | Agents managing their own schedules | Retained, AI-optimised |

---

### Domain 6: Contact Centre Platform / Core Infrastructure
*The foundational platform layer*

| Component | Description | CCOTF Evolution |
|---|---|---|
| CCaaS Platform | Cloud contact centre as a service (Genesys, Amazon Connect, Salesforce Service Cloud Voice, NICE, Avaya) | Single modern CCaaS platform — key architectural decision for CCOTF |
| SIP Trunking / Telephony | Carrier and SIP infrastructure | Retained, abstracted by CCaaS |
| WebRTC | Browser-based voice/video (no plugin) | Enables in-app voice for Belron mobile/web |
| Recording & Archiving | Call and screen recording, storage | AI-indexed, compliance-grade |
| Compliance Recording Controls | Pause/resume for PCI, consent management | Integrated with compliance layer |
| Platform APIs | CCaaS developer API for customisation | Key integration surface for AI layer |

**Key decision for Belron:** Which CCaaS platform is the strategic choice? This is the single most consequential technology decision in the CCOTF programme. Likely candidates:
- **Amazon Connect** — if AWS is Belron's cloud, strong AI/ML ecosystem (Lex, Bedrock)
- **Genesys Cloud CX** — market leader, strong AI partner ecosystem
- **Salesforce Service Cloud Voice** — if Salesforce is already in the CRM estate
- **NICE CXone** — strong WFM and AI portfolio

---

### Domain 7: CRM & Customer Data
*The customer record and data foundation*

| Component | Description | CCOTF Evolution |
|---|---|---|
| CRM System | Core customer relationship management (Salesforce, Microsoft Dynamics, SAP) | Likely Salesforce at Belron (EBS/Salesforce braindump Apr 8) |
| Customer Data Platform (CDP) | Unified real-time customer profile | Real-time context for AI routing |
| Customer 360 / Unified View | Single view of customer across all channels and touchpoints | CCOTF requirement — currently fragmented? |
| Case / Ticket System | Service case logging and tracking | Integrated with AI auto-logging |
| Identity Verification | Vehicle registration, account, policy verification | AI-assisted (VRM lookup) |
| Preference & Consent Management | Communication preferences, GDPR consent | Required for CCOTF outbound channels |

---

### Domain 8: Knowledge & Content Management
*What agents and AI need to know*

| Component | Description | CCOTF Evolution |
|---|---|---|
| Knowledge Base (KB) | Structured knowledge for agents and self-service | AI-indexed, conversational KB |
| FAQ / Content Library | Customer-facing help content | AI-generated, continuously updated |
| Decision Trees / Guided Flows | Structured guidance for complex processes | Largely replaced by AI reasoning |
| Internal Process Documentation | SOPs, policies for agent reference | AI-surfaced contextually |
| Product / Service Catalogue | Offerings, pricing, eligibility rules | Machine-readable for AI agent use |
| Regulatory / Compliance Content | Legal, regulatory, insurer-specific requirements | Embedded in AI guardrails |

---

### Domain 9: Analytics & Reporting
*Insight from contact centre data*

| Component | Description | CCOTF Evolution |
|---|---|---|
| Real-Time Dashboards / Wallboards | Live operational KPIs | AI-anomaly-highlighted dashboards |
| Historical Reporting | Period reporting on contact volumes, SLAs | BI tool integration |
| CSAT / NPS / CES Measurement | Customer satisfaction survey tooling | AI-inferred sentiment supplements surveys |
| Voice of the Customer (VoC) Platform | Structured VoC programme | AI-powered continuous VoC |
| Speech & Text Analytics Platform | Automated analysis of contact content | 100% contact analysis |
| Predictive Analytics / BI | Forward-looking demand and trend modelling | AI-powered forecasting |
| Agent Performance Analytics | Individual and team performance data | AI coaching trigger |
| Contact Reason Analytics | Why are customers contacting? | AI-categorised, real-time |

---

### Domain 10: Integration & API Layer
*How the contact centre connects to other systems*

| Component | Description | CCOTF Evolution |
|---|---|---|
| API Gateway / Middleware | Central integration hub | Event-driven, API-first |
| CTI Adapters | Telephony ↔ desktop integration | CCaaS-native |
| CRM Connectors | Contact centre ↔ CRM integration | Real-time bidirectional |
| **Insurer API Integration** | Claim authorisation, booking, status | Key Belron-specific component — real-time AI-assisted |
| **VRM / Vehicle Lookup** | Vehicle registration → customer/vehicle data | Integrated into AI routing and agent desktop |
| **Field Service / Technician Dispatch** | Appointment booking, technician availability | AI-optimised scheduling |
| **ADAS Calibration Booking** | Specialist calibration appointment management | Requires specialist technician routing |
| Event Streaming Platform | Kafka / event bus for real-time data flow | Underpins real-time AI |
| Identity & Auth Integration | SSO, identity provider | Platform-level |
| Payment Processing | PCI-compliant payment capture | Retained, may be AI-guided |

---

### Domain 11: Security & Compliance
*Protecting data and meeting regulatory obligations*

| Component | Description | CCOTF Evolution |
|---|---|---|
| Authentication / SSO / MFA | Agent and customer identity | Zero-trust architecture |
| PCI-DSS Compliance Controls | Payment card data handling | Pause/resume recording, secure IVR payment |
| GDPR / Data Privacy Controls | EU/UK data protection compliance | AI-assisted consent and data handling |
| Call Recording Compliance | Consent capture, recording governance | Automated consent management |
| AI Model Governance | Bias, explainability, fairness for AI decisions | New domain for CCOTF — connects to MCP Governance |
| Fraud Detection | Real-time fraud signals during contact | AI-powered |
| Data Retention & Archiving | Regulatory retention of contact records | Automated policy enforcement |

---

### Domain 12: Back-Office Integration
*The systems the contact centre hands off to or triggers*

| Component | Description | CCOTF Evolution |
|---|---|---|
| **Claims Management System** | Insurer claim submission and tracking | AI-native claim initiation and tracking |
| **Appointment / Job Management** | Technician job creation and management | AI-optimised, real-time |
| **Glass/Parts Inventory** | Stock availability for repair/replace | Real-time availability in agent view |
| Order Management | Parts orders, supply chain | Automated via AI workflow |
| Billing & Finance Systems | Invoice generation, payment | Automated for standard transactions |
| Field Service Management | Technician dispatch and routing | AI-optimised dispatch |
| **ADAS Calibration System** | Specialist calibration job management | Belron-specific back-office integration |

---

## The Belron-Specific Layer

### Unique Technology Components for Belron's CCOTF

These components are specific to Belron's domain and do not appear in a generic contact centre reference model:

| Component | Belron Specificity | Connection |
|---|---|---|
| VRM (Vehicle Registration) Lookup | Customer identified by vehicle plate, not account number | Routing, customer 360, job creation |
| Glass Type / Damage Assessment | Visual/AI assessment of glass damage → repair or replace decision | AI Damage Assessment PoC |
| Insurer Claim Authorisation | Pre-approval from insurer before job can proceed | Real-time insurer API, affects contact duration |
| ADAS Calibration Routing | ADAS-equipped vehicles require specialist technician and equipment | Skills-based routing extension |
| Multi-OpCo Routing | Autoglass UK, Carglass France/Germany, Safelite — language, geography, brand | CCaaS platform must support multi-brand, multi-language |
| Mobile vs. Depot Routing | Some jobs require mobile technician; others need depot visit | Job type determines fulfilment path |

---

## Strategic Intelligence

### Key Insights

1. **The CCaaS platform choice is the most consequential single technology decision.** Everything else in this reference model either sits on top of, integrates with, or is constrained by the CCaaS platform. Belron needs a CCaaS decision before designing anything else in depth. The three realistic candidates are Amazon Connect (if AWS-first), Genesys Cloud CX (best-of-breed, vendor-neutral), or Salesforce Service Cloud Voice (if Salesforce CRM is already core).

2. **Domain 4 (AI & Automation) is the differentiating layer — everything else is table stakes.** A modern contact centre can buy Domains 1–3 and 5–12 from any competent CCaaS vendor. The competitive differentiation and the CCOTF vision lives in Domain 4, specifically: LLM-powered virtual agents, real-time agent assist, agentic orchestration for multi-step workflows, and AI damage assessment integration.

3. **The Belron-specific layer (VRM lookup, insurer API, ADAS routing) is where the complexity lives.** Generic CCOTF frameworks don't account for these. The insurer API integration in particular is both the most complex and the most strategically important — it determines whether Belron can pre-approve claims in real-time during a contact (reducing duration and increasing conversion) or continues to treat insurer authorisation as a manual step.

4. **AI model governance (Domain 11) connects directly to MCP Governance.** Any AI decision made during a customer contact — routing, damage assessment, claim eligibility, agent guidance — needs governance. The MCP Governance framework that Armo is building is the upstream governance layer for CCOTF's AI components. These two projects need to be explicitly connected.

5. **The capability model and the technology component model need an explicit mapping layer.** The BC model says what the business does; the technology model says what systems enable it. The missing artefact is the mapping between them — which technology components support which capabilities. That's the next EA deliverable after this reference model is validated.

### Pattern Recognition
- **Connection to CCOTF capability overlap braindump (Apr 8):** [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]] — the overlap was unresolved at that point. The technology model now gives a concrete basis for drawing the boundary: which technology components sit in CCOTF vs. front-office?
- **Connection to AI Damage Assessment PoC:** The Damage Assessment component in Domain 4 and the Belron-specific layer is a direct integration point between the two projects. CCOTF is the *delivery channel* for AI damage assessment; the PoC is the *AI capability* it will call.
- **Connection to MCP Governance:** Domain 11 (AI Model Governance) and Domain 4's agentic AI components need to sit within the MCP Governance framework.
- **Connection to today's daily brief:** Corgi (AI-native insurer) signals that Domain 10's Insurer API Integration is being rebuilt. Belron's integration architecture needs to anticipate API-first, automated insurer interaction rather than human-mediated claims.

### Strategic Implications
- This reference model is a **working artefact, not a final deliverable** — it needs to be validated against Belron's current technology estate before it becomes an architecture document
- The model should be loaded into LeanIX as a set of Application Building Blocks (ABBs) — each domain becomes a capability group; each component becomes a technology building block
- **Priority for gap analysis:** Start with Domain 6 (CCaaS platform) and Domain 4 (AI & Automation) — these are the most strategically significant and most likely to have gaps

---

## Action Items

### Immediate (This Week)
- [ ] Share this reference model with the CCOTF team / BA colleagues — validate against what they know of current Belron technology 📅 2026-05-09
- [ ] Identify which CCaaS platform Belron currently uses (or if there is a platform decision pending) — this unlocks most other technology decisions 📅 2026-05-09

### Short-term (2 Weeks)
- [ ] Map Belron's current contact centre technology against this reference model — RAG status per component (Red = gap, Amber = partial, Green = covered) 📅 2026-05-21
- [ ] Load the 12 domains into LeanIX as Application Building Blocks for the CCOTF programme 📅 2026-05-21
- [ ] Create the explicit mapping between CCOTF business capabilities (existing BC model) and these technology components 📅 2026-05-21
- [ ] Connect with MCP Governance project team — flag Domain 11 (AI Model Governance) and Domain 4 agentic components as shared governance scope 📅 2026-05-14

### Strategic Considerations
- The reference model is also useful as a **stakeholder communication tool** — showing leadership what a full CCOTF technology stack looks like, and where Belron currently sits on that map, makes the investment case concrete
- Consider publishing this as a CCOTF Architecture Vision artefact (connects to the TOGAF ADM template braindump from yesterday) — it is the technology equivalent of the business vision

---

## Connections
- **Related Braindumps:** [[braindump-2026-04-08-1207-ccotf-front-office-capability-overlap]], [[braindump-2026-05-06-1627-togaf-adm-templates-belron-adaptation]] (ADM templates — this model is a candidate Architecture Definition Document input)
- **Relevant Projects:** [[04-projects/contact-centre-future/PROJECT-OVERVIEW|Contact Centre of the Future]], [[04-projects/ai-damage-assessment-poc/PROJECT-OVERVIEW|AI Damage Assessment PoC]], [[04-projects/mcp-governance/PROJECT-OVERVIEW|MCP Governance]]
- **Daily Brief Connection:** [[01-daily/briefs/daily-brief-2026-05-07]] — Corgi AI-native insurance signal affects Domain 10 (Insurer API Integration)

## Domain Classification
- **Primary Domain:** Project-Specific — Contact Centre of the Future (99%)
- **Reasoning:** This is a primary EA deliverable for the CCOTF project, directly scoped to that project
- **Cross-Domain Elements:** Connects to MCP Governance (AI governance layer) and AI Damage Assessment PoC (Domain 4 integration)
- **Privacy Level:** confidential

## Processing Notes

### Emotional Context
- **Energy Level:** High — this is substantive EA work with immediate practical application
- **Emotional Tone:** Analytical — structured problem-solving, not exploratory

### Confidence Assessment
- **Overall Analysis:** 88% — standard contact centre technology domains are well-established; Belron-specific components are inferred from domain knowledge of the business
- **Domain Classification:** 99% — clearly CCOTF project work
- **Strategic Insights:** 85% — CCaaS platform recommendation and Belron-specific layer are well-grounded; actual current Belron technology estate is inferred, not confirmed
- **Areas Requiring Clarification:** Current Belron CCaaS platform; whether Salesforce is the CRM of record; status of insurer API integration; which AI tools are already in the contact centre today

---

*Processed by COG Brain Dump Analyst*
