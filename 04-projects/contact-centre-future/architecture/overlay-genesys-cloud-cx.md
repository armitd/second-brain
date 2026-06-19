---
type: vendor-overlay
domain: enterprise-architecture
base_ra: ccotf-ra-vendor-agnostic.md
vendor: "Genesys Cloud CX"
vendor_stack: "Genesys Cloud CX + Genesys AI + Genesys WEM + Genesys DX + AppFoundry"
date: 2026-06-19
status: "v0.1 — Working Draft"
owner: "Armo — Enterprise Architecture, Belron"
tags:
  - ccotf
  - vendor-overlay
  - genesys
  - ea
---

# CCOTF Vendor Implementation Overlay
## Genesys Cloud CX

*Read `ccotf-ra-vendor-agnostic.md` first. This document maps vendor products to each Architecture Building Block (ABB) and assesses fit against Belron's requirements. Where this overlay conflicts with the base RA, the base RA governs.*

---

## 1. Vendor Overview

**Genesys Cloud CX** is the market-leading cloud contact centre platform (Gartner Magic Quadrant Leader, consistently). It is cloud-neutral — deployable on AWS, Azure, or GCP — making it the natural choice for organisations that want to avoid cloud-provider lock-in at the CCaaS layer. The AI stack is branded **Genesys AI** and covers predictive routing, virtual agents, agent assist, automated QA, and workforce management. Genesys also maintains the **AppFoundry** marketplace for pre-built integrations with third-party AI, CRM, WFM, and analytics vendors.

**Strategic context for Belron:** Genesys is the strongest option for organisations that want a cloud-neutral, best-of-breed CCaaS platform with deep WFM capabilities and a broad partner ecosystem. If Belron has not committed to a primary cloud provider, or has multi-cloud requirements across Autoglass, Carglass, and Safelite, Genesys does not create a cloud dependency. The trade-off is that Genesys is typically the highest per-seat cost option and relies on third-party or manual integration for LLM providers.

**Headline fit:** High — if cloud neutrality, best-in-class WFM, or existing Genesys contracts are Belron priorities.

---

## 2. ABB Implementation Mapping

| ABB ID | ABB Name | Vendor Product | Native / Custom | Notes |
|---|---|---|---|---|
| ABB-C01 | Channel Adapter | Genesys Cloud CX native: voice, chat, email, SMS, social media. WhatsApp via Genesys Messenger + WhatsApp Business API (direct partner). | Native | WhatsApp natively supported in Genesys via Messenger channel — no additional partner integration required |
| ABB-C02 | Virtual Agent Platform | Genesys Dialog Engine Bot Flows (native NLU) + Genesys AI Agents; OR third-party LLM integration via Genesys Architect (Google CCAI, Amazon Lex, Azure Bot Framework) | Native + optional third-party | Genesys native bot is rule-extended; for full LLM-native agent, integrate Bedrock/Azure OpenAI via Genesys Architect data actions. GenAI Capabilities (Genesys AI) launched 2025 provide native LLM reasoning. |
| ABB-C03 | Intelligent Routing Engine | Genesys Intelligent Routing — ML-based predictive routing; skills-based; attribute-based; queue prioritisation | Native | Genesys predictive routing uses ML to match customer to best available agent. Rule-based override per AP-02 configurable in routing policies. |
| ABB-C04 | Proactive Outreach Orchestrator | Genesys Outbound Dialler (voice campaigns) + Genesys Proactive Web Engagement (digital) + Campaign Manager | Native | Voice outbound campaigns and digital proactive engagement. SMS/email outbound via Genesys Agentless Messaging. |
| ABB-C05 | Real-Time Transcription | Genesys Transcription (native voice-to-text) + partner integrations (Google STTI, Amazon Transcribe) | Native + optional | Genesys native transcription available; language coverage via partner where native falls short. Multi-language: EN, FR, DE, NL supported. |
| ABB-C06 | Unified Agent Desktop | Genesys Workspace (fully customisable agent UI) + CRM integrations (Salesforce, ServiceNow, MS Dynamics pre-built via AppFoundry) | Native | Agent sees all channels in one workspace. Screen-pop via CTI. CRM embed pre-built for major CRM vendors. |
| ABB-C07 | Real-Time Agent Assist Engine | Genesys Agent Assist (native) — real-time guidance, suggested responses, KB surfacing powered by Genesys AI | Native | Genesys Agent Assist surfaces contextual suggestions without auto-sending. KB integration configurable. Agent decides on all AI suggestions. |
| ABB-C08 | AI Quality Assurance | Genesys Cloud QM + Genesys AI Scoring + Genesys Speech and Text Analytics | Native | Automated 100% contact scoring across voice and digital. AI-generated evaluation forms. Coaching integration. |
| ABB-C09 | VRM / Vehicle Lookup | Genesys Data Actions (REST call from Architect flow to VRM API) | Custom | Data Actions allow real-time REST API calls during routing and IVR. VRM lookup triggered in Architect flow; result injected as contact attributes. |
| ABB-C10 | AI Damage Assessment Engine | Genesys Data Actions → AIDA PoC API; Architect flow triggers Lambda or direct REST call | Custom integration | Same pattern as VRM lookup — Data Actions bridge to AIDA PoC API. Image upload flow for digital channels. |
| ABB-C11 | Insurer Claims API Connector | Genesys Data Actions → per-insurer REST endpoints; `claims-mcp` surface via MCP Gateway | Custom | One Data Action per insurer API. Real-time call during routing or agent handling. Result returned as contact attribute. |
| ABB-C12 | ADAS Calibration Router | Genesys Intelligent Routing with custom skill/attribute for ADAS-certified agents; triggered by VRM Data Action result | Custom configuration | Routing policy: if VRM result includes ADAS flag → route to queue with ADAS skill requirement. Configurable in Genesys routing policies. |
| ABB-C13 | Multi-OpCo Routing Logic | Genesys Cloud Divisions — single org with opco-partitioned administration; multiple queues/flows per brand/language/region | Native | Genesys Divisions allow multi-brand management in one org with data segregation. Alternatively, multiple Genesys orgs per major region. |
| ABB-C14 | CCaaS Core Platform | Genesys Cloud CX (Tier 1/2/3 licences) — ACD, omnichannel, SIP, recording, WFM (Genesys WEM), analytics | Native | Best-in-class WFM (Genesys WEM): multi-site, multi-skill, AI forecasting, scheduling, adherence — most mature in market. |
| ABB-C15 | MCP Gateway | IBM ContextForge (deployed on customer cloud); Genesys open APIs allow ContextForge integration | IBM product on Belron cloud | Genesys itself does not provide an MCP gateway. ContextForge deployed on Belron's chosen cloud connects to Genesys via Platform API. |
| ABB-C16 | Semantic Layer | Genesys Analytics data export → Cube.js or dbt Semantic Layer (custom); Genesys does not provide a semantic layer | Custom | Genesys Analytics provides KPI reporting. Semantic Layer (L2) is a bespoke initiative per OI-08, built outside of Genesys. |
| ABB-C17 | Contact Audit Store | Genesys Cloud recording + compliance export to customer-managed storage (S3 / Azure Blob) | Native export | GDPR-compliant; Genesys supports EU data residency. WORM compliance via S3 Object Lock or Azure Blob immutable storage in customer-managed bucket. |
| ABB-C18 | Observability Plane | Genesys Analytics platform (native) + Genesys API data export + OpenTelemetry → Dynatrace + Elastic | Native + integration | Genesys exposes comprehensive API for data export. OpenTelemetry Collector to Dynatrace for cross-stack observability. |
| ABB-C19 | PCI Compliance Controls | Genesys Cloud PCI DSS compliance — pause/resume recording API; DTMF masking; PCI vault partner integration (e.g. Sycurio) | Native | Genesys is PCI DSS Level 1 certified. Pause/resume exposed as an API call in Architect. Sycurio or equivalent for full card capture isolation. |

---

## 3. Layer Architecture — Genesys Cloud CX Implementation

### Layer ①: Customer Channels
Voice via PSTN (Genesys managed SBC or bring-your-own carrier), Genesys Messenger for chat and web, email, SMS, WhatsApp (Business API via Genesys Messenger — native partner), social media (Facebook, Twitter, Instagram).

### Layer ②: AI-First Contact Layer
- **Virtual Agent:** Genesys Bot Flows for structured dialogue; Genesys GenAI Capabilities for LLM-native conversational AI. For maximum LLM capability, integrate with Amazon Bedrock (Claude) or Azure OpenAI via Genesys Architect Data Actions.
- **Routing:** Genesys Intelligent Routing with ML-based predictive routing as the default. Rule-based evaluation applied at decision points per AP-02 via routing policies and Architect decision steps.
- **Proactive Outreach:** Genesys Campaign Manager for voice. Agentless Messaging for digital outbound. Predictive contact prevention signal from `customer-mcp` consumed via Genesys Data Actions or external trigger.

### Layer ③: Human Agent Workspace
Genesys Workspace is the unified agent desktop — fully customisable. AppFoundry provides pre-built CRM integrations (Salesforce, ServiceNow, Dynamics). Genesys Agent Assist provides real-time guidance. After-call work: Genesys AI Wrap-Up — AI-generated summary for agent confirmation.

### Layer ④: Belron Intelligence Layer
All Layer ④ components use Genesys Data Actions (REST calls from Architect flows) to invoke Belron-built or third-party APIs:

```
Customer contacts → Genesys Architect Flow
→ VRM input (IVR or digital form)
→ Data Action: VRM Lookup (< 1s target)
→ Flow variable populated: vehicle data, ADAS flag, opco
→ Genesys Bot Flow: intent resolution (damage type, job intent)
→ Architect Decision Step: Rule-Evaluated Routing (AP-02)
→ Queue routing + screen-pop to agent
→ (Parallel) Data Action: Insurer Pre-Auth API call
→ Pre-auth result available in contact attributes before agent handles
```

### Layer ⑤: CCaaS Core — Genesys Cloud CX
Genesys Cloud CX Tier 3 (or 2+) provides full feature set: ACD, omnichannel, SIP (managed SBC), recording, Genesys WEM (best-in-class WFM: forecasting, scheduling, adherence, gamification), Genesys Analytics, Platform API. Deployable on AWS, Azure, or GCP per Belron cloud strategy.

### Layer ⑥: Enterprise Integration — MCP Gateway
IBM ContextForge deployed on Belron's chosen cloud. ContextForge connects to Genesys via Genesys Platform API. All CCOTF agent-to-system calls route through ContextForge for identity, audit, and governance per MCP RA requirements.

---

## 4. Belron Intelligence Layer — Integration Notes

Genesys Data Actions are the primary integration mechanism for Layer ④. A Data Action is a real-time REST call made from within an Architect flow, with result available as a flow variable. This is well-suited to VRM lookup, insurer pre-auth, and damage assessment triggers.

Key consideration: Data Action latency requirements (< 1s for VRM, ~30s for insurer pre-auth) must be validated in performance testing. Genesys Data Actions have configurable timeouts and retry logic.

---

## 5. Native vs. Custom Build Analysis

| Capability | Status | Effort |
|---|---|---|
| Voice/chat/WhatsApp omnichannel | Native | None |
| LLM virtual agent (GenAI + Architect) | Native/config | Low–Medium — LLM integration via Data Actions or native |
| Real-time agent assist | Native | Low — KB integration and configuration |
| 100% AI QA | Native | Low — rubric configuration |
| WFM (Genesys WEM) | Native | Medium — configuration and agent training |
| Proactive outreach | Native | Low |
| VRM lookup | Custom | Medium — Data Action + VRM API contract |
| AI Damage Assessment integration | Custom | Low — Data Action bridge to AIDA PoC API |
| Insurer API connectors | Custom | High — one Data Action per insurer |
| ADAS calibration routing | Custom config | Medium — routing policy + Data Action |
| Multi-opco routing (Divisions) | Native | Medium — Divisions setup and governance |
| MCP Gateway | IBM product | Medium — ContextForge deployment and Genesys API integration |
| Semantic Layer | Custom | High — shared with MCP Governance |

---

## 6. Geographic Coverage

| Belron Opco | Region | Genesys Cloud CX Availability |
|---|---|---|
| Autoglass UK | EU (UK) | ✅ Available — EU (Ireland/UK regions) |
| Carglass France | EU | ✅ Available — EU (Ireland / Frankfurt regions) |
| Carglass Germany | EU | ✅ Available — EU (Frankfurt preferred) |
| Carglass Belgium | EU | ✅ Available — EU regions |
| Carglass Italy | EU | ✅ Available — EU regions |
| Safelite US | US | ✅ Available — US regions (multiple) |
| Other markets | Various | Genesys has broadest global PoP coverage of any CCaaS vendor |

**Assessment:** Genesys has the widest global footprint of any CCaaS vendor — no geographic blockers for any Belron opco. EU data residency fully supported.

---

## 7. Architecture Principle Compliance

| Principle | Compliance | Notes |
|---|---|---|
| AP-01 AI-first | ✅ Green | Genesys GenAI Capabilities support LLM-native virtual agents; Intelligent Routing for deflection |
| AP-02 Rule-evaluated outputs | ✅ Green | Architect Decision Steps allow rule-based evaluation at every AI output point; Data Actions carry structured outputs |
| AP-03 Belron Intelligence is the moat | ✅ Green | Layer ④ built as Data Actions calling Belron-owned APIs — not locked to Genesys |
| AP-04 CCaaS unlocks other decisions | ✅ Green | Genesys chosen → Genesys-compatible LLM and WFM decisions follow |
| AP-05 MCP Governance | ⚠ Amber | No native MCP support in Genesys; IBM ContextForge on separate infrastructure required. Workable but adds deployment overhead vs. Amazon Connect native MCP. |
| AP-06 Honest representation | ✅ Green | Genesys is the lowest lock-in of the four platforms — cloud neutral, open APIs, broad ecosystem |
| AP-07 Semantic consistency | ⚠ Amber | No native semantic layer; shared initiative required (OI-08) |
| AP-08 EU AI Act transparency | ✅ Green | Virtual agent disclosure configurable in Architect flow opening prompt |
| AP-09 Multi-opco | ✅ Green | Genesys Divisions are purpose-built for multi-brand, multi-region deployment |

---

## 8. Strengths and Gaps

### Strengths
- **Lowest vendor lock-in** of any evaluated platform — cloud neutral, open APIs, broad AppFoundry ecosystem
- **Best-in-class WFM** (Genesys WEM) — most mature multi-site workforce management in the market
- WhatsApp natively supported (no partner integration required)
- Broadest global coverage — no opco left out
- Predictive routing is a Genesys native strength — ML-based matching without additional build
- AppFoundry marketplace offers 350+ pre-built integrations — reduces custom build for some Layer ④ integrations
- If Belron runs a multi-cloud estate, Genesys is compatible with all major cloud providers

### Gaps
- Higher per-seat licence cost vs. Amazon Connect (per-consumption) or Salesforce (per-conversation)
- LLM integration for virtual agent requires additional work (Data Actions to external LLM API) vs. Amazon Connect native Bedrock
- MCP Governance integration requires ContextForge on separate infrastructure (vs. Amazon's native MCP on Bedrock)
- Genesys's own AI innovation velocity is slower than Amazon/Salesforce/Microsoft — relies more on ecosystem integrations

---

## 9. Pricing Model

| Component | Model | Notes |
|---|---|---|
| Genesys Cloud CX Tier 1 | Per named user/month | Voice only; ~$75–$95/agent/month (indicative, enterprise negotiated) |
| Genesys Cloud CX Tier 2 | Per named user/month | Voice + digital; ~$95–$115/agent/month |
| Genesys Cloud CX Tier 3 | Per named user/month | Full feature set including WFM; ~$140–$160/agent/month |
| Genesys AI Scoring | Add-on | QA scoring and analytics add-on |
| Genesys Agent Assist | Add-on | Real-time agent guidance add-on |
| Genesys WEM | Included in Tier 3 | Best-in-class WFM included at higher tier |

**Budget modelling note:** Genesys per-seat pricing is predictable but higher than consumption-based models. At Belron scale, enterprise licence negotiation is essential. Genesys often provides significant volume discounts for large, multi-opco commitments.

---

## 10. When Genesys Cloud CX Is the Right Choice

**Select Genesys if:**
- Cloud neutrality is a strategic Belron requirement — no cloud provider commitment at the CCaaS layer
- WFM is a primary programme driver and best-in-class forecasting/scheduling is required from day one
- Belron has complex multi-opco requirements and wants the most mature Divisions/multi-brand architecture
- An existing Genesys on-premises deployment (e.g. PureConnect or PureEngage) is in scope for migration — Genesys provides a clear migration path
- The AIDA PoC is deployed on a different cloud provider than AWS — Genesys is cloud-agnostic

**Caution if:**
- AWS is confirmed as Belron's primary cloud — Amazon Connect's native AWS integration is a structural advantage Genesys cannot match
- Per-seat cost vs. consumption pricing is materially important for Belron's budget model
- Speed of LLM integration is critical — Genesys requires additional integration effort for LLM-native virtual agents

---

*v0.1 — 2026-06-19. Pair with `ccotf-ra-vendor-agnostic.md` (base RA). EA Owner: Armo · Belron Enterprise Architecture.*
