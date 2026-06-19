---
type: vendor-overlay
domain: enterprise-architecture
base_ra: ccotf-ra-vendor-agnostic.md
vendor: "NICE CXone"
vendor_stack: "NICE CXone + Enlighten AI + CXone WFM + Enlighten Autopilot + EvaluAgent"
date: 2026-06-19
status: "v0.1 — Working Draft"
owner: "Armo — Enterprise Architecture, Belron"
tags:
  - ccotf
  - vendor-overlay
  - nice
  - cxone
  - ea
---

# CCOTF Vendor Implementation Overlay
## NICE CXone

*Read `ccotf-ra-vendor-agnostic.md` first. This document maps vendor products to each Architecture Building Block (ABB) and assesses fit against Belron's requirements. Where this overlay conflicts with the base RA, the base RA governs.*

---

## 1. Vendor Overview

**NICE CXone** is one of the leading enterprise contact centre platforms, with particular strength in Workforce Engagement Management (WFM + QM) and AI-driven quality assurance. The NICE AI suite is branded **Enlighten** — covering automated QA, agent coaching, sentiment analysis, predictive routing (Enlighten XO), and virtual agents (Enlighten Autopilot). NICE has invested heavily in AI since 2021 and the Enlighten suite is now a significant differentiator, particularly for organisations where quality management and compliance are primary drivers.

**Strategic context for Belron:** NICE CXone is the strongest choice if workforce management and automated quality assurance are the primary CCOTF drivers, rather than AI-native virtual agents or CRM integration. NICE WFM is widely regarded as the most capable multi-site forecasting and scheduling platform in the market. The Enlighten AI QA suite provides best-in-class automated scoring and coaching. However, NICE's AI innovation velocity on the virtual agent and agentic AI fronts is slower than Amazon, Salesforce, or even Genesys.

**Headline fit:** Medium–High — if WFM and AI QA are primary drivers, or if Belron has an existing NICE investment. Less competitive if LLM-native virtual agents and agentic back-office automation are the primary CCOTF differentiators.

---

## 2. ABB Implementation Mapping

| ABB ID | ABB Name | Vendor Product | Native / Custom | Notes |
|---|---|---|---|---|
| ABB-C01 | Channel Adapter | CXone native: voice, chat, email, SMS, social media, WhatsApp, video (CXone Video) | Native | Strong omnichannel breadth. WhatsApp via CXone Digital First Omnichannel. Video supported natively. |
| ABB-C02 | Virtual Agent Platform | Enlighten Autopilot (CXone native conversational AI) + partner integrations (Google CCAI, Amazon Lex, Microsoft Azure Bot) | Native + partner | Enlighten Autopilot handles structured conversational flows. For LLM-native reasoning (AP-01), integration with a third-party LLM (Bedrock, Azure OpenAI) via CXone Studio is required. Less mature than Agentforce or Connect for full LLM-native agents. |
| ABB-C03 | Intelligent Routing Engine | CXone ACD with Enlighten XO (AI-powered routing) + skills-based routing | Native | Enlighten XO provides AI-predicted routing based on customer and agent attributes. Rule-based override via CXone Studio (AP-02 compatible). |
| ABB-C04 | Proactive Outreach Orchestrator | CXone Proactive Outbound (voice dialler) + CXone Digital (SMS/email outbound) | Native | Outbound dialler and digital campaign capabilities. Predictive signal from `customer-mcp` triggers via Studio script. |
| ABB-C05 | Real-Time Transcription | CXone Transcription (native voice-to-text) — feeds Enlighten AI and QA | Native | CXone native transcription. Multi-language support: EN, FR, DE, NL (validate language coverage for all Carglass markets). |
| ABB-C06 | Unified Agent Desktop | CXone Agent (browser-based unified workspace) — CRM integration via pre-built connectors or custom | Native | CXone Agent is a standalone agent desktop. CRM integration (Salesforce, ServiceNow, Dynamics) via pre-built adapters — not native CRM; integration effort required. |
| ABB-C07 | Real-Time Agent Assist Engine | Enlighten Copilot — real-time agent guidance, suggested responses, KB surfacing | Native | Enlighten Copilot provides contextual guidance based on live transcription. Agent-confirmed suggestions. Integrated with CXone Expert (KB). |
| ABB-C08 | AI Quality Assurance | Enlighten AI QA — automated 100% contact scoring, sentiment, categorisation, coaching | Native — market-leading | NICE Enlighten AI QA is the strongest out-of-box QA capability of any evaluated platform. 100% contact coverage, automated scoring against customisable rubrics, AI-driven coaching recommendations, and performance trend analysis. |
| ABB-C09 | VRM / Vehicle Lookup | CXone Studio custom script (REST API call to VRM service) | Custom | Studio scripts allow REST API calls during IVR and routing flows. VRM lookup triggered as a Studio action; result stored as contact attribute. |
| ABB-C10 | AI Damage Assessment Engine | CXone Studio → REST API call to AIDA PoC | Custom integration | Same Studio pattern as VRM lookup. REST call to AIDA PoC API during contact; result in contact attribute. |
| ABB-C11 | Insurer Claims API Connector | CXone Studio → REST API per insurer; `claims-mcp` surface via MCP Gateway | Custom | One Studio script per insurer API. `claims-mcp` surface via IBM ContextForge. |
| ABB-C12 | ADAS Calibration Router | CXone ACD skills-based routing + custom Studio logic triggered by VRM attribute | Custom configuration | ADAS flag in contact attribute → Studio condition → routing to ADAS-skilled agent queue. |
| ABB-C13 | Multi-OpCo Routing Logic | CXone Business Units — multi-brand administration; multiple queues/flows/routing per opco | Native | CXone Business Units provide opco-partitioned administration within a shared platform. Or separate CXone instances per major region. |
| ABB-C14 | CCaaS Core Platform | NICE CXone — ACD, omnichannel, SIP, recording, CXone WFM, Enlighten Analytics | Native — strongest WFM | CXone WFM is best-in-class: multi-site, multi-skill, AI-enhanced demand forecasting, intraday management, adherence, gamification, and agent self-scheduling. |
| ABB-C15 | MCP Gateway | IBM ContextForge (deployed on customer cloud); CXone open APIs integrate with ContextForge | IBM product on Belron cloud | NICE does not provide an MCP gateway natively. ContextForge deployed on Belron's cloud; integrates with CXone via Platform API. |
| ABB-C16 | Semantic Layer | CXone Analytics data export → custom Semantic Layer (Cube.js / dbt); NICE does not provide a semantic layer | Custom | NICE Analytics provides KPI reporting and data exports. Semantic Layer is a bespoke initiative per OI-08, built outside of CXone. |
| ABB-C17 | Contact Audit Store | CXone Recording + compliance export to customer-managed storage (S3 / Azure Blob) | Native export | GDPR-compliant; NICE supports EU data residency. WORM compliance via immutable storage in customer-managed bucket. |
| ABB-C18 | Observability Plane | CXone Analytics (native) + API data export + OpenTelemetry → Dynatrace | Native + integration | CXone Analytics provides platform-layer reporting. OpenTelemetry integration to Dynatrace for cross-stack observability. |
| ABB-C19 | PCI Compliance Controls | CXone PCI DSS compliance — pause/resume recording API; DTMF masking; Sycurio/PCI Pal for secure card capture | Native | CXone is PCI DSS Level 1 certified. Pause/resume via Studio or API. Card capture via Sycurio or PCI Pal integration. |

---

## 3. Layer Architecture — NICE CXone Implementation

### Layer ①: Customer Channels
Full native omnichannel: voice (PSTN + SIP), CXone Digital First (chat, email, SMS, social, WhatsApp, in-app messaging), video (CXone Video). NICE has the most complete native channel set of the four evaluated platforms.

### Layer ②: AI-First Contact Layer
- **Virtual Agent:** Enlighten Autopilot for structured conversational flows. For LLM-native reasoning, integrate third-party LLM (Amazon Bedrock/Claude preferred, Azure OpenAI) via CXone Studio REST calls. This requires custom integration work — not native like Amazon Connect or Agentforce.
- **Routing:** CXone ACD with Enlighten XO predictive routing. Rule-based evaluation at routing decision points via Studio conditions (AP-02 compatible).
- **Proactive Outreach:** CXone Proactive Outbound for voice campaigns. Digital outbound via CXone Messaging.

### Layer ③: Human Agent Workspace
CXone Agent is the unified desktop. Enlighten Copilot provides real-time AI guidance. CXone Expert is the knowledge management platform integrated with Copilot. After-call work: Enlighten AI generates contact summary for agent confirmation. Supervisor: Enlighten AI provides real-time floor view with sentiment alerts and performance monitoring.

### Layer ④: Belron Intelligence Layer
All Layer ④ components are custom-built using CXone Studio scripts (synchronous REST API calls). Studio is CXone's low-code IVR/flow development environment:

```
Customer contacts → CXone ACD receives contact
→ VRM entered/spoken in IVR
→ Studio Action: REST call → VRM Lookup API (< 1s target)
→ Contact attribute populated: vehicle data, ADAS flag, opco
→ Enlighten XO: intent prediction
→ Studio condition: Rule-Evaluated Routing (AP-02)
→ Queue routing + screen-pop to CXone Agent
→ (Parallel) Studio Action: REST call → Insurer Pre-Auth API
→ Pre-auth result in contact attribute before agent handles
```

### Layer ⑤: CCaaS Core — NICE CXone
CXone native: ACD, omnichannel, SIP, recording, **CXone WFM** (best-in-class), Enlighten Analytics. No cloud-provider dependency — NICE manages the infrastructure.

### Layer ⑥: Enterprise Integration — MCP Gateway
IBM ContextForge deployed on Belron's chosen cloud. ContextForge connects to CXone via CXone Platform API. CCOTF agent-to-system tool calls route through ContextForge for identity, audit, and governance per MCP RA requirements. No native MCP capability in CXone.

---

## 4. Belron Intelligence Layer — Integration Notes

CXone Studio is the integration mechanism for Layer ④. Studio actions are synchronous REST calls within the IVR/routing flow. Key consideration: Studio REST calls are well-suited to VRM lookup and insurer pre-auth but require careful timeout management for real-time scenarios. CXone Studio is a proven pattern for this type of integration in production enterprise contact centres.

---

## 5. Native vs. Custom Build Analysis

| Capability | Status | Effort |
|---|---|---|
| Voice/chat/WhatsApp/video omnichannel | Native | None — most complete native channel set |
| LLM virtual agent | Custom (third-party LLM via Studio) | Medium — LLM API integration in Studio |
| Real-time agent assist (Enlighten Copilot) | Native | Low — KB integration and configuration |
| 100% AI QA (Enlighten AI QA) | Native — market-leading | Low — rubric configuration |
| WFM (CXone WFM) | Native — market-leading | Medium — configuration and migration from current WFM |
| Proactive outreach | Native | Low |
| VRM lookup | Custom (Studio) | Medium — Studio script + VRM API contract |
| AI Damage Assessment integration | Custom (Studio) | Low — Studio REST call to AIDA PoC API |
| Insurer API connectors | Custom (Studio) | High — one script per insurer |
| ADAS calibration routing | Custom configuration | Medium — Studio condition + routing |
| Multi-opco routing (Business Units) | Native | Medium — Business Unit design and governance |
| MCP Gateway | IBM product | Medium — ContextForge deployment + CXone API integration |
| Semantic Layer | Custom | High — shared with MCP Governance |

---

## 6. Geographic Coverage

| Belron Opco | Region | NICE CXone Availability |
|---|---|---|
| Autoglass UK | EU (UK) | ✅ Available |
| Carglass France | EU | ✅ Available |
| Carglass Germany | EU | ✅ Available |
| Carglass Belgium | EU | ✅ Available |
| Carglass Italy | EU | ✅ Available |
| Safelite US | US | ✅ Available |
| Other markets | Various | NICE has broad global coverage |

**Assessment:** NICE CXone has full geographic coverage for all Belron opcos. No geographic blockers — an advantage over Salesforce AGCC. EU data residency supported.

---

## 7. Architecture Principle Compliance

| Principle | Compliance | Notes |
|---|---|---|
| AP-01 AI-first | ⚠ Amber | Enlighten Autopilot is capable but not LLM-native out-of-box. Full LLM-native virtual agent requires third-party integration. |
| AP-02 Rule-evaluated outputs | ✅ Green | CXone Studio enables deterministic rule evaluation at all AI output decision points |
| AP-03 Belron Intelligence is the moat | ✅ Green | Layer ④ built as Studio scripts calling Belron-owned APIs — not locked to NICE |
| AP-04 CCaaS unlocks other decisions | ✅ Green | CXone chosen → WFM, LLM, and integration decisions follow |
| AP-05 MCP Governance | ⚠ Amber | No native MCP in CXone; IBM ContextForge required on separate infrastructure |
| AP-06 Honest representation | ✅ Green | Low vendor lock-in — Studio is CXone-specific but underlying APIs are standard REST |
| AP-07 Semantic consistency | ⚠ Amber | No native semantic layer; shared initiative required (OI-08) |
| AP-08 EU AI Act transparency | ✅ Green | Virtual agent disclosure configurable in Studio IVR flow |
| AP-09 Multi-opco | ✅ Green | CXone Business Units support multi-brand, multi-region deployment; full EU coverage |

---

## 8. Strengths and Gaps

### Strengths
- **Best-in-class WFM** — CXone WFM (tied with Genesys WEM for top position) — multi-site, multi-skill, AI-enhanced forecasting, intraday management
- **Best-in-class AI QA** — Enlighten AI QA is the most mature automated quality assurance platform in the market; 100% coverage, sophisticated rubric scoring, AI coaching
- **Full geographic coverage** — no Belron opco excluded; strongest global reach
- **Native video** — CXone Video is native; Genesys, Amazon Connect, and Salesforce require third-party
- **Compliance strength** — NICE has deep heritage in compliance recording and regulatory-grade QA
- **Lowest integration risk for WFM + QA** — if these are primary drivers, NICE requires the least custom build

### Gaps
- **Weakest LLM-native virtual agent** — Enlighten Autopilot requires significant custom integration to achieve LLM-native reasoning capability. If AI-first deflection is the primary CCOTF goal, NICE requires more build than Agentforce or Amazon Connect.
- **AI innovation velocity** — NICE's AI roadmap is slower than Amazon, Salesforce, or Google. Agentforce and Amazon Connect are shipping agentic features faster.
- **No native MCP** — ContextForge integration required (same position as Genesys)
- **No CRM integration parity with Salesforce** — CXone Agent requires separate CRM integration; no native CRM like Service Console

---

## 9. Pricing Model

| Component | Model | Notes |
|---|---|---|
| CXone Platform | Per named user/month (tiered) | Indicative: CXone Complete ~$100–$150/agent/month including WFM and QM |
| Enlighten AI QA | Included or add-on | Confirm bundling with CXone licence tier |
| Enlighten Copilot | Add-on | Real-time agent assist add-on |
| Enlighten Autopilot | Consumption-based | Per self-service interaction |
| CXone WFM | Included in Complete | Best-in-class WFM included at higher tier |

**Budget modelling note:** NICE CXone's all-in pricing (including WFM and QM) is competitive when the full suite is needed. If WFM and QM are primary drivers, the total cost of ownership vs. a lower-licence platform plus best-of-breed WFM (Verint + Genesys/Connect) is often favourable.

---

## 10. When NICE CXone Is the Right Choice

**Select NICE CXone if:**
- **Workforce management is a primary programme driver** — multi-site, complex scheduling requirements where CXone WFM's maturity is the key requirement
- **AI quality assurance at 100% contact coverage** is the immediate priority — Enlighten AI QA is the market leader here
- **Compliance and regulatory-grade recording** are paramount — NICE's heritage in regulated industries is a genuine differentiator
- Belron has an existing NICE on-premises deployment (IEX WFM, NICE Engage) that provides a migration path
- Full geographic coverage is required from day one and Salesforce AGCC's EU gap is a blocker for a single-vendor strategy

**Caution if:**
- LLM-native virtual agents and agentic back-office automation are the primary CCOTF differentiators — NICE requires more build for this than Amazon Connect or Salesforce AGCC
- AI innovation velocity is a strategic requirement — Amazon and Salesforce are shipping agentic capabilities faster
- The CCOTF vision is primarily about AI-first self-service deflection rather than agent productivity and quality management

**Recommended use case for Belron:** NICE CXone is the strongest fit if the CCOTF programme is sequenced quality-first: stabilise and automate quality assurance and workforce management before investing in LLM-native virtual agents. If the Belron CCOTF programme is sequenced AI-first (virtual agent deflection as Phase 1), Amazon Connect or Salesforce AGCC are stronger candidates.

---

*v0.1 — 2026-06-19. Pair with `ccotf-ra-vendor-agnostic.md` (base RA). EA Owner: Armo · Belron Enterprise Architecture.*
