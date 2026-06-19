---
type: vendor-overlay
domain: enterprise-architecture
base_ra: ccotf-ra-vendor-agnostic.md
vendor: "Salesforce Agentforce Contact Center"
vendor_stack: "Salesforce AGCC + Service Cloud Voice + Agentforce + Einstein + MuleSoft + Informatica"
date: 2026-06-19
status: "v0.1 — Working Draft"
owner: "Armo — Enterprise Architecture, Belron"
tags:
  - ccotf
  - vendor-overlay
  - salesforce
  - agentforce
  - ea
---

# CCOTF Vendor Implementation Overlay
## Salesforce Agentforce Contact Center (AGCC)

*Read `ccotf-ra-vendor-agnostic.md` first. This document maps vendor products to each Architecture Building Block (ABB) and assesses fit against Belron's requirements. Where this overlay conflicts with the base RA, the base RA governs.*

---

## 1. Vendor Overview

**Salesforce Agentforce Contact Center (AGCC)** — formerly Service Cloud Voice — reached General Availability in February 2026, with UK availability confirmed. AGCC integrates voice, digital channels, AI agents (Agentforce), and CRM (Service Cloud) in a single platform. The voice layer runs on Amazon Chime (AWS-hosted), managed by Salesforce. The AI layer is Agentforce — Salesforce's agentic AI platform — with Einstein for real-time assist and Einstein Bots for conversational AI.

**The Salesforce data equation:** In November 2025, Salesforce completed the acquisition of Informatica ($8B). Informatica is now the data foundation for Agentforce — providing MDM (Customer 360), data integration (CDI), and AI-driven data quality (CLAIRE DQ Agent). If Belron currently uses Informatica for master data management, the AGCC value proposition extends beyond CCaaS: Agentforce agents get direct access to Belron's governed master customer and vehicle data through the Informatica layer, without additional integration effort.

**The pivotal question:** Does Belron use Salesforce Service Cloud as its CRM of record? AGCC's core value proposition — eliminating the integration tax between CRM and CCaaS — only applies if Belron's contact centre agents are already working in Service Cloud. Without Salesforce CRM, the value reduces significantly.

**Geographic constraint:** AGCC is currently available in UK, US, and Canada. Continental Carglass markets (France, Germany, Belgium, Italy) are **not yet supported**. This is a critical constraint for a Belron-wide deployment.

**Headline fit:** High for Autoglass UK/Safelite US if Belron runs Salesforce Service Cloud. Conditional on geography resolving. **Not viable for continental Carglass markets today.**

---

## 2. ABB Implementation Mapping

| ABB ID | ABB Name | Vendor Product | Native / Custom | Notes |
|---|---|---|---|---|
| ABB-C01 | Channel Adapter | AGCC native: voice (Service Cloud Voice on Amazon Chime), digital (Messaging for In-App & Web), email (Email-to-Case), SMS (Messaging), WhatsApp (Messaging channel) | Native | WhatsApp supported natively via Salesforce Messaging. Video not native — third-party integration. **Geographic limit: UK, US, Canada only (Feb 2026 GA).** |
| ABB-C02 | Virtual Agent Platform | Agentforce AI agents (LLM-native, multi-step reasoning) + Einstein Bots (structured) | Native | Agentforce is a genuine LLM-native agentic platform — not a rules-based chatbot extended with AI. Einstein Bots for simpler deterministic flows. Salesforce AI (xAI-based) or Bring-Your-Own LLM option. |
| ABB-C03 | Intelligent Routing Engine | Salesforce Omni-Channel routing + Einstein Classification (intent-based) + Salesforce Flow routing rules | Native | Omni-Channel routes across all channels. Einstein Classification resolves intent. Routing decision point: rule-based via Salesforce Flow (AP-02 compatible) or Einstein-recommended. |
| ABB-C04 | Proactive Outreach Orchestrator | Salesforce Marketing Cloud (outbound campaigns) + Agentforce Proactive Outreach | Native (with Marketing Cloud licence) | Requires Salesforce Marketing Cloud for full outbound campaign management. Agentforce supports proactive contact triggers. |
| ABB-C05 | Real-Time Transcription | Amazon Transcribe (AGCC runs on AWS Chime — transcription via AWS stack) | Native via AWS | Transcription quality and language support follows Amazon Transcribe. Multi-language coverage: EN, FR, DE, NL supported by Amazon Transcribe. |
| ABB-C06 | Unified Agent Desktop | Salesforce Service Console — native CRM integration is the key differentiator | Native | Agents work in Service Console. Contact, case, account, vehicle object, and AI suggestions in one interface. No CRM integration effort — it is the CRM. |
| ABB-C07 | Real-Time Agent Assist Engine | Einstein AI Copilot for Service — real-time suggested replies, KB articles, next-best-action | Native | Einstein Copilot surfaces contextual suggestions without auto-applying. Integrates natively with Salesforce Knowledge. Agent confirms all suggestions. |
| ABB-C08 | AI Quality Assurance | Einstein Conversation Insights — automated call analysis, topic detection, sentiment | Native | Einstein Conversation Insights scores calls and digital contacts. Less mature than Genesys WEM QM or NICE Enlighten for fully automated rubric scoring — check roadmap for 100% QA coverage. |
| ABB-C09 | VRM / Vehicle Lookup | Salesforce External Objects (Vehicle) or Custom Object; Platform Events for real-time lookup; Informatica Customer 360 if Belron uses Informatica | Native (Salesforce data model) | VRM can be modelled as a Salesforce custom object or External Object linking to an external VRM system. If Informatica MDM holds vehicle data, Agentforce agents access it directly via Informatica CDI. |
| ABB-C10 | AI Damage Assessment Engine | Salesforce Flow → External Service → AIDA PoC API; Einstein Vision for image classification (native option) | Custom integration | Salesforce External Services wrap a REST API as a Salesforce action. Salesforce Flow triggers AIDA PoC API during contact. Einstein Vision provides native image analysis if AIDA PoC is not yet available. |
| ABB-C11 | Insurer Claims API Connector | Salesforce External Services (REST) + Salesforce Flow; MuleSoft for API management; Informatica CDI for data integration | Custom / MuleSoft | MuleSoft (Salesforce-owned) is the enterprise integration layer. Insurer APIs modelled as External Services in Salesforce. `claims-mcp` surface via Agentforce MCP (see below). |
| ABB-C12 | ADAS Calibration Router | Salesforce Omni-Channel with custom routing attributes; Salesforce Flow decision step triggered by VRM object data | Custom configuration | ADAS flag on Vehicle object triggers routing attribute via Flow. Omni-Channel routes to ADAS-certified agent skill. |
| ABB-C13 | Multi-OpCo Routing Logic | Salesforce Record Types + Profiles per opco; Omni-Channel configuration per brand; multiple Salesforce Orgs for full data isolation | Native (configuration) | Multiple Orgs per major brand for full data isolation, or Record Types within a shared Org. **Geographic constraint limits continental Carglass.** |
| ABB-C14 | CCaaS Core Platform | Salesforce AGCC — voice on Amazon Chime; digital native in Service Cloud; **no native WFM** — requires Verint or NICE WFM integration | Native (with WFM gap) | Critical gap: AGCC has no native workforce management capability. Verint or NICE WFM must be integrated as a third-party component. Adds cost and integration complexity. |
| ABB-C15 | MCP Gateway | Agentforce MCP actions (announced 2026 — Agentforce agents expose and consume MCP); IBM ContextForge optional | Native (Agentforce) | Salesforce has announced Agentforce will support MCP natively. This is strategically significant: Agentforce-to-system tool calls can be governed as MCP tool calls. Validate GA date and conformance with MCP RA requirements. |
| ABB-C16 | Semantic Layer | Salesforce Data Cloud (unified data layer) + Informatica MDM/Customer 360 (master data governed vocabulary) | Native (Salesforce stack) | Data Cloud provides a unified customer data model. If Belron uses Informatica, CLAIRE DQ Agent provides AI-native data quality. This is the strongest native semantic governance story of any CCaaS vendor. |
| ABB-C17 | Contact Audit Store | Salesforce Platform (Shield — event monitoring + audit trail) + Amazon S3 for voice recordings (Chime-hosted) | Native + AWS | Salesforce Shield provides field-level encryption and event monitoring. Voice recordings stored in S3 (Salesforce-managed AWS). GDPR compliance: Salesforce EU data residency available. |
| ABB-C18 | Observability Plane | Salesforce Event Monitoring (Shield) + OpenTelemetry → Dynatrace | Native + integration | Salesforce Event Monitoring logs all user and API activity. OpenTelemetry integration to Dynatrace for cross-stack observability. |
| ABB-C19 | PCI Compliance Controls | Salesforce PCI DSS compliance; partner integration (e.g. Sycurio, PCI Pal) for payment capture in voice | Native + partner | Salesforce is PCI DSS compliant. For voice payment capture (card data in IVR), Sycurio or PCI Pal integrate with AGCC to ensure card numbers never enter Salesforce or agent context. |

---

## 3. Layer Architecture — Salesforce AGCC Implementation

### Layer ①: Customer Channels
Voice via AGCC (Amazon Chime-hosted, Salesforce-managed). Chat and web via Salesforce Messaging for In-App & Web. Email via Email-to-Case (creates Service Cloud case automatically). SMS via Salesforce Messaging. WhatsApp via Salesforce Messaging channel (native). Video requires third-party.

**Geographic constraint:** AGCC channel capabilities available in UK, US, and Canada only as of Feb 2026 GA. Continental Carglass (FR, DE, BE, IT) not yet supported.

### Layer ②: AI-First Contact Layer
- **Virtual Agent:** Agentforce — LLM-native multi-step reasoning agent. Can autonomously handle complex, multi-turn contact scenarios (booking, claim status, damage triage). Not a chatbot — a genuine agentic platform.
- **Routing:** Salesforce Omni-Channel with Einstein Classification for intent resolution. Routing decision in Salesforce Flow (rule-based, AP-02 compliant) based on Einstein intent output.
- **Proactive Outreach:** Agentforce proactive outreach + Marketing Cloud for campaign management.

### Layer ③: Human Agent Workspace
Service Console is the agent workspace — not a separate CCaaS desktop but the CRM itself. This is the core AGCC value proposition: the agent sees the full Salesforce record (contact, case, vehicle, insurer, history) alongside the live interaction. No integration tax. Einstein Copilot provides real-time guidance. After-call work: Einstein auto-generates case summary and disposition; agent confirms.

### Layer ④: Belron Intelligence Layer
Implemented in the Salesforce data model and Flow automation:
- **VRM / Vehicle Lookup:** Vehicle as Salesforce custom object or External Object. Lookup triggered on contact creation. VRM-to-vehicle data populates the agent's Service Console automatically if Informatica MDM holds vehicle master data.
- **Damage Assessment:** Salesforce External Service calls AIDA PoC API via Flow.
- **Insurer Claims API:** MuleSoft manages per-insurer API integration. Claims data returned to Salesforce as a custom object/record.
- **ADAS Routing:** ADAS flag on Vehicle record → Flow → Omni-Channel routing attribute.

### Layer ⑤: CCaaS Core — Salesforce AGCC
AGCC provides ACD (Omni-Channel), voice (Amazon Chime), digital channels, recording (S3). **No native WFM.** Verint or NICE WFM required for workforce management — integrate via API.

### Layer ⑥: Enterprise Integration — MCP Gateway
Agentforce's announced native MCP support makes this potentially the most governed agent-to-system integration story. Agentforce Actions (wrapping Salesforce External Services, Flows, and Apex) are exposed as MCP tools. IBM ContextForge can serve as the enterprise MCP gateway if Agentforce's native MCP falls short of ContextForge's governance requirements — validate before deciding.

---

## 4. Belron Intelligence Layer — Integration Notes

The key architectural advantage for Salesforce is the data model convergence:
- Salesforce CRM holds the customer record
- Informatica Customer 360 (if in use) holds the master vehicle and customer data
- AGCC agents read directly from this model without an integration layer

The integration flow:

```
Customer contacts → AGCC receives contact
→ Customer identified (phone number → Contact lookup)
→ Vehicle identified (VRM input → Vehicle object lookup, or Informatica CDI)
→ Agentforce agent: intent resolution + Belron Intelligence context
→ Omni-Channel routing: Einstein Classification + Flow rule (AP-02)
→ Agent receives contact in Service Console with full Salesforce record
→ Einstein Copilot: real-time guidance from Salesforce Knowledge
→ Flow: Insurer Pre-Auth API call (MuleSoft) during contact
→ Case auto-updated; claim record created; job record triggered
```

---

## 5. Native vs. Custom Build Analysis

| Capability | Status | Effort |
|---|---|---|
| Voice + digital omnichannel (UK/US) | Native | None — within geographic availability |
| Continental Europe channels | Not available | Blocked — see geographic gap |
| LLM virtual agent (Agentforce) | Native | Low–Medium — agent definition and training |
| Real-time agent assist (Einstein Copilot) | Native | Low — Salesforce Knowledge integration |
| AI QA (Einstein Conversation Insights) | Native | Low–Medium — validate 100% coverage capability |
| WFM | Gap — third-party required | High — Verint/NICE WFM integration |
| VRM lookup | Custom (Salesforce data model) | Medium — Vehicle object + lookup flow |
| AI Damage Assessment integration | Custom | Low — External Service + Flow |
| Insurer API connectors | MuleSoft | High — per-insurer via MuleSoft (licence cost) |
| ADAS calibration routing | Custom configuration | Medium |
| Multi-opco routing | Native configuration | Medium — per-opco Org or Record Type design |
| MCP Gateway | Agentforce native (validate) | Low–Medium — depends on Agentforce MCP GA scope |
| Semantic Layer | Salesforce Data Cloud + Informatica | Low if Informatica in use; Medium otherwise |

---

## 6. Geographic Coverage

| Belron Opco | Region | Salesforce AGCC Availability |
|---|---|---|
| Autoglass UK | UK | ✅ Available — Feb 2026 GA |
| Carglass France | EU | ❌ Not yet available |
| Carglass Germany | EU | ❌ Not yet available |
| Carglass Belgium | EU | ❌ Not yet available |
| Carglass Italy | EU | ❌ Not yet available |
| Safelite US | US | ✅ Available |

**This is a critical constraint.** AGCC cannot be the single global CCaaS platform for Belron today. A phased approach is required: AGCC for Autoglass UK and Safelite as a pilot/early deployment; continental Carglass on a different platform or delayed.

**Mitigation option:** Deploy Genesys Cloud CX for continental Carglass in parallel with AGCC for UK/US. This creates a dual-platform estate — increases architecture complexity and integration overhead. Only viable if Belron's opcos are sufficiently independent.

---

## 7. Architecture Principle Compliance

| Principle | Compliance | Notes |
|---|---|---|
| AP-01 AI-first | ✅ Green | Agentforce is the strongest LLM-native agentic contact platform in the market — genuine autonomous resolution |
| AP-02 Rule-evaluated outputs | ✅ Green | Salesforce Flow enables deterministic rule evaluation at all AI output points; fully AP-02 compatible |
| AP-03 Belron Intelligence is the moat | ✅ Green | Layer ④ in Salesforce data model + MuleSoft — but Salesforce dependency is higher than Genesys or Amazon (data model lock-in) |
| AP-04 CCaaS unlocks other decisions | ✅ Green | AGCC chosen → Agentforce, Einstein, Data Cloud decisions follow |
| AP-05 MCP Governance | ⚠ Amber | Agentforce MCP announced but GA scope needs validation against MCP RA requirements |
| AP-06 Honest representation | ⚠ Amber | Strongest platform lock-in of any option — value proposition depends entirely on Salesforce CRM. If Belron moves away from Salesforce CRM, AGCC value collapses. |
| AP-07 Semantic consistency | ✅ Green | Salesforce Data Cloud + Informatica MDM provides the strongest native semantic governance story — vocabulary governed at the data platform level |
| AP-08 EU AI Act transparency | ✅ Green | Disclosure configurable in Agentforce conversation opening |
| AP-09 Multi-opco | ❌ Red | Geographic constraint means continental Carglass cannot deploy AGCC today. Multi-opco requires a secondary platform for EU. |

---

## 8. Strengths and Gaps

### Strengths
- **Strongest AI agent platform** — Agentforce provides genuine LLM-native, multi-step autonomous resolution that others cannot yet match
- **Eliminates CRM integration tax** — if Belron runs Service Cloud, the agent desktop is the CRM. No separate CCaaS integration.
- **Salesforce Data Cloud + Informatica** — strongest native semantic governance and master data story of any platform
- **$2/conversation pricing** — can be significantly cheaper than per-seat at high self-service rates
- **MuleSoft** — enterprise integration capability already owned if Belron uses MuleSoft today
- Agentforce MCP (native) could become the strongest MCP governance implementation of any CCaaS vendor

### Gaps
- **Geographic blocker** — continental Carglass (EU) not available in Feb 2026 GA. No firm availability date for EU. This alone may eliminate AGCC as a single global platform.
- **No native WFM** — Verint or NICE integration required; adds cost and complexity
- **Hard Salesforce dependency** — value is contingent on Salesforce CRM of record. Without Service Cloud, AGCC loses most of its differentiation.
- **Highest vendor lock-in** — Agentforce, Data Cloud, MuleSoft, and Informatica create a deeply integrated proprietary stack. Switching away becomes increasingly expensive.

---

## 9. Pricing Model

| Component | Model | Notes |
|---|---|---|
| Salesforce AGCC | $2/conversation (digital) | Voice pricing separate — confirm with Salesforce account team |
| Agentforce | $2/conversation OR named user | AI agent conversations at $2 each; human agent seat licence separate |
| Service Cloud (agent seats) | Per named user/month | Enterprise or Unlimited tier required for full AGCC feature access |
| Salesforce Data Cloud | Credits-based consumption | Data unification and real-time data platform |
| MuleSoft | Per connection/month | Required for insurer API integration at scale |
| Verint/NICE WFM | Per agent/month | External WFM — additional licence and integration cost |
| Einstein Copilot | Included or add-on | Confirm bundling with AGCC licence tier |

**Budget modelling note:** The $2/conversation model can be very cost-effective if AI self-service resolution rates are high (60%+ deflection). Cost depends heavily on contact volume and resolution mix. Model both scenarios: high deflection (AI-resolved at $2) and low deflection (human agent falls back to per-seat cost).

---

## 10. When Salesforce AGCC Is the Right Choice

**Select Salesforce AGCC if:**
- Belron opcos use Salesforce Service Cloud as the CRM of record — the integration-free agent experience is the primary value
- Belron uses Informatica MDM — the Agentforce-Informatica data layer provides the strongest native customer/vehicle data foundation for AI agents
- The deployment scope is Autoglass UK + Safelite US (within geographic availability)
- Agentic AI capability (genuine multi-step autonomous resolution) is the #1 priority
- $2/conversation pricing creates a favourable business case at high deflection rates

**Caution if:**
- Continental Carglass (FR, DE, BE, IT) is in scope for the first deployment phase — geographic availability blocks it today
- Belron does not use Salesforce CRM — the core value proposition (CRM-CCaaS integration) does not apply
- WFM is a first-phase priority — the WFM gap adds cost and complexity
- Long-term platform independence is a strategic requirement — Salesforce creates the highest lock-in of any option

**Recommended approach (if interested):** Pilot AGCC for Autoglass UK (if Salesforce CRM confirmed) as a single-opco deployment. Validate the Agentforce-Belron Intelligence Layer integration and the $2/conversation economics before committing globally. Continental Carglass runs on Genesys or Amazon Connect in the interim.

---

*v0.1 — 2026-06-19. Pair with `ccotf-ra-vendor-agnostic.md` (base RA). EA Owner: Armo · Belron Enterprise Architecture.*
