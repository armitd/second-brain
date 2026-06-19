---
type: vendor-overlay
domain: enterprise-architecture
base_ra: ccotf-ra-vendor-agnostic.md
vendor: "Amazon Connect"
vendor_stack: "Amazon Connect + Amazon Lex + Amazon Bedrock + Amazon Q in Connect + Contact Lens"
date: 2026-06-19
status: "v0.1 — Working Draft"
owner: "Armo — Enterprise Architecture, Belron"
tags:
  - ccotf
  - vendor-overlay
  - amazon-connect
  - aws
  - ea
---

# CCOTF Vendor Implementation Overlay
## Amazon Connect + AWS AI Stack

*Read `ccotf-ra-vendor-agnostic.md` first. This document maps vendor products to each Architecture Building Block (ABB) and assesses fit against Belron's requirements. Where this overlay conflicts with the base RA, the base RA governs.*

---

## 1. Vendor Overview

**Amazon Connect** is AWS's cloud-native omnichannel contact centre platform, launched in 2017 and rebranded in May 2026 as **Amazon Connect Customer** to reflect its full agentic AI positioning. It runs natively on AWS infrastructure with deep integration to the AWS AI/ML ecosystem: Amazon Lex for conversational AI, Amazon Bedrock for LLM access (including Claude), Amazon Q in Connect for real-time agent assist, and Contact Lens for analytics and quality assurance.

**Strategic context for Belron:** AWS is a confirmed Belron cloud provider (confirmed May 2026). This is a structural advantage: Amazon Connect runs natively in the same infrastructure Belron already operates, eliminating cross-cloud data transfer costs and simplifying data residency compliance. The MCP Connector for Claude Platform on AWS (GA May 2026) is CloudTrail-audited and IAM-authenticated — directly satisfying the MCP Governance framework's audit and identity requirements.

**Headline fit:** High — provided AWS is confirmed as the primary or co-primary cloud platform for the CCOTF workload.

---

## 2. ABB Implementation Mapping

| ABB ID | ABB Name | Vendor Product | Native / Custom | Notes |
|---|---|---|---|---|
| ABB-C01 | Channel Adapter | Amazon Connect (voice/chat/email); Amazon Pinpoint (SMS/WhatsApp outbound); Amazon Chime SDK (video) | Native for voice/chat; Partner for WhatsApp inbound | WhatsApp inbound requires Amazon Pinpoint + partner Business API integration |
| ABB-C02 | Virtual Agent Platform | Amazon Lex v2 (NLU/ASR) + Amazon Bedrock (LLM — Claude/Titan) | Native | Lex handles session management; Bedrock provides LLM reasoning. Amazon Connect generative AI features (Bedrock-powered) available in Connect flows |
| ABB-C03 | Intelligent Routing Engine | Amazon Connect routing profiles + Amazon Q in Connect routing; Contact Lens real-time intent detection | Native + configuration | Rules-based routing decision per AP-02 can be implemented in Connect Contact Flows with Lambda for rule evaluation |
| ABB-C04 | Proactive Outreach Orchestrator | Amazon Connect outbound campaigns + Amazon Pinpoint (SMS/email) | Native | Outbound campaigns for voice dialler; Pinpoint for digital outbound. Predictive signal from `customer-mcp` triggers via Lambda |
| ABB-C05 | Real-Time Transcription | Amazon Transcribe Real-Time + Contact Lens (built on Transcribe) | Native | Contact Lens provides real-time transcription with PII redaction. Multi-language: EN, FR, DE, NL (Belron opco languages supported) |
| ABB-C06 | Unified Agent Desktop | Amazon Connect Agent Workspace (browser-based CCP) + Amazon AppIntegrations for CRM embed | Native | CRM embed via AppIntegrations SDK. Fully customisable. Screen-pop via Contact Flows |
| ABB-C07 | Real-Time Agent Assist Engine | Amazon Q in Connect | Native | Surfaces KB articles, suggested responses, next-best-action in real-time during contact. Powered by Bedrock. No auto-send — agent decides. |
| ABB-C08 | AI Quality Assurance | Amazon Connect Contact Lens | Native | Contact Lens: 100% contact analysis, sentiment, category detection, automated QA scoring, supervisor alerts. Available for voice and chat. |
| ABB-C09 | VRM / Vehicle Lookup | AWS Lambda (custom) invoked from Connect Contact Flows | Custom | VRM lookup is a bespoke Belron capability. Lambda function calls internal/external VRM API during IVR flow. Result injected into contact attributes for routing and agent desktop. |
| ABB-C10 | AI Damage Assessment Engine | AWS Lambda → AIDA PoC API; Amazon Rekognition (optional image pre-processing) | Custom integration | AIDA PoC is the authoritative engine. Lambda bridges Connect flow to AIDA API. Rekognition available for image validation pre-AIDA if needed. |
| ABB-C11 | Insurer Claims API Connector | AWS Lambda + Amazon API Gateway → per-insurer adapters | Custom | Lambda functions called from Connect flows for real-time authorisation. API Gateway manages per-insurer endpoints. `claims-mcp` surface via MCP Gateway. |
| ABB-C12 | ADAS Calibration Router | Amazon Connect routing profiles + custom routing logic in Connect Contact Flows + Lambda | Custom configuration | Skills-based routing: ADAS-certified agents tagged in routing profiles. VRM result triggers routing rule via Lambda. |
| ABB-C13 | Multi-OpCo Routing Logic | Amazon Connect: multiple queues, routing profiles, phone numbers, and Contact Flows per opco | Native | Single Connect instance with opco-partitioned configuration. Or separate Connect instances per major region (UK, EU, US) for data residency isolation. |
| ABB-C14 | CCaaS Core Platform | Amazon Connect | Native | ACD, omnichannel, SIP (Connect native + Chime SDK), recording (S3), WFM (Connect Workforce Management — launched 2024), analytics (Contact Lens). |
| ABB-C15 | MCP Gateway | IBM ContextForge on AWS; OR Amazon Bedrock Agents with native MCP support (GA May 2026) | Native on AWS | Amazon Bedrock Agents natively supports MCP (confirmed May 2026) — IAM-authenticated, CloudTrail-audited. IBM ContextForge remains the enterprise MCP gateway per MCP RA. |
| ABB-C16 | Semantic Layer | Amazon DataZone (data governance) + custom semantic layer (Cube.js on Amazon RDS) | Custom | Amazon DataZone provides data cataloguing and governance. Semantic Layer (L2) is a bespoke initiative — see OI-08. Cube.js on RDS/Redshift is the current candidate. |
| ABB-C17 | Contact Audit Store | Amazon S3 (WORM via Object Lock) + AWS CloudTrail | Native | S3 Object Lock provides immutable WORM storage. CloudTrail audits all API calls. Contact Lens logs persist in S3. GDPR: EU-region S3 buckets for EU opcos. |
| ABB-C18 | Observability Plane | Amazon CloudWatch + AWS X-Ray + OpenTelemetry → Dynatrace + Elastic | Native + integration | CloudWatch for AWS-layer metrics. X-Ray for distributed tracing. OpenTelemetry Collector exports to existing Dynatrace/Elastic estate. |
| ABB-C19 | PCI Compliance Controls | Amazon Connect PCI DSS compliance; pause/resume recording API; Amazon Connect IVR for secure card capture | Native | Amazon Connect is PCI DSS Level 1 certified. Pause/resume via API in Contact Flows. Secure IVR (DTMF) for card capture — card data never enters agent or LLM context. |

---

## 3. Layer Architecture — Amazon Connect Implementation

### Layer ①: Customer Channels
Voice via PSTN (Amazon Connect phone numbers or bring-your-own carrier via SIP), Amazon Connect Chat (SDK for web/app), email via Amazon Connect Email (launched 2024), SMS via Amazon Pinpoint, WhatsApp inbound via Business API partner + Pinpoint.

### Layer ②: AI-First Contact Layer
- **Virtual Agent:** Amazon Lex v2 bot embedded in Contact Flow handles intent recognition and dialogue. For complex LLM-based reasoning, Lambda invokes Amazon Bedrock (Claude recommended for AIDA PoC alignment). Amazon Connect generative AI features provide Bedrock-native conversational flows.
- **Routing:** Intent resolved in Lex → Contact Flow applies rule-based routing logic (Lambda) → queued to agent or deflected. Predictive routing via Amazon Q in Connect.
- **Proactive Outreach:** Amazon Connect outbound campaigns for scheduled voice outbound. Pinpoint for programmatic SMS/email outreach triggered by `customer-mcp` events.

### Layer ③: Human Agent Workspace
Amazon Connect Agent Workspace provides the unified desktop. Amazon Q in Connect surfaces real-time guidance. Contact Lens provides supervisor view with sentiment alerts and real-time transcription. After-call work: Amazon Q in Connect generates AI-summarised contact notes for agent confirmation before CRM logging.

### Layer ④: Belron Intelligence Layer
All Layer ④ components are custom builds on AWS:
- Lambda functions invoked at specific points in Contact Flows
- VRM lookup: Lambda → VRM API → result injected into Contact Attributes
- Damage Assessment: Lambda → AIDA PoC API (once available)
- Insurer API: Lambda → API Gateway → per-insurer endpoints
- Results available to routing engine and Agent Workspace via Contact Attributes

### Layer ⑤: CCaaS Core — Amazon Connect
Amazon Connect native features: ACD, omnichannel, SIP, recording to S3, Connect Workforce Management, Contact Lens analytics, Platform API (full REST API). All data in AWS; EU data stays in EU-region.

### Layer ⑥: Enterprise Integration — MCP Gateway
IBM ContextForge deployed on AWS (EC2/ECS). Alternatively, Amazon Bedrock Agents' native MCP support (May 2026 GA) can serve CCOTF MCP tool calls directly within the AWS ecosystem, with IAM identity and CloudTrail audit natively.

---

## 4. Belron Intelligence Layer — Integration Notes

The Layer ④ components are implemented as AWS Lambda functions invoked from Amazon Connect Contact Flows. Key integration points:

```
Customer calls → Connect Contact Flow
→ VRM entered/spoken
→ Lambda: VRM Lookup (< 1s target)
→ Contact Attributes populated: vehicle make/model, glass spec, ADAS flag, opco
→ Lambda: Lex + Bedrock intent resolution (damage type, job intent)
→ Lambda: Rule-Evaluated Routing Decision (AP-02)
→ Queue routing + screen-pop to agent
→ (Parallel) Lambda: Insurer Pre-Auth API call
→ Pre-auth result available in Contact Attributes before agent handles call
```

Amazon Connect Contact Attributes are the data carrier across the flow — available to the agent desktop via CCP screen-pop and to all Lambda invocations within the same contact.

---

## 5. Native vs. Custom Build Analysis

| Capability | Status | Effort |
|---|---|---|
| Voice/chat omnichannel | Native | None |
| LLM virtual agent (Lex + Bedrock) | Native | Low — configuration + prompt engineering |
| Real-time agent assist (Q in Connect) | Native | Low — KB indexing required |
| 100% AI QA (Contact Lens) | Native | Low — rubric configuration |
| WFM | Native | Medium — migration from current WFM |
| Proactive outreach | Native | Low |
| VRM lookup | Custom | Medium — Lambda + VRM API contract |
| AI Damage Assessment integration | Custom | Low — Lambda bridge once AIDA PoC available |
| Insurer API connectors | Custom | High — per-insurer adapter per carrier |
| ADAS calibration routing logic | Custom | Medium — routing profile configuration + Lambda |
| Multi-opco routing | Native (configuration) | Medium — opco config design and rollout |
| MCP Gateway | Native/IBM | Low — ContextForge on AWS or Bedrock native MCP |
| Semantic Layer | Custom | High — shared with MCP Governance initiative |

---

## 6. Geographic Coverage

| Belron Opco | Region | Amazon Connect Availability |
|---|---|---|
| Autoglass UK | EU (UK) | ✅ Available — London region (eu-west-2) |
| Carglass France | EU | ✅ Available — Paris (eu-west-3) or Frankfurt (eu-central-1) |
| Carglass Germany | EU | ✅ Available — Frankfurt (eu-central-1) |
| Carglass Belgium | EU | ✅ Available — EU regions |
| Carglass Italy | EU | ✅ Available — EU regions |
| Safelite US | US | ✅ Available — US East (us-east-1), US West (us-west-2) |
| Other markets | Various | Generally available; check specific country PSTN number availability |

**Assessment:** Amazon Connect has strong geographic coverage for Belron's key opcos. No geographic blockers.

---

## 7. Architecture Principle Compliance

| Principle | Compliance | Notes |
|---|---|---|
| AP-01 AI-first | ✅ Green | Lex + Bedrock virtual agent; full self-service flows supported |
| AP-02 Rule-evaluated outputs | ✅ Green | Lambda functions can implement deterministic rule evaluation over Lex/Bedrock outputs |
| AP-03 Belron Intelligence is the moat | ✅ Green | Layer ④ is custom Lambda; not locked to any CCaaS vendor |
| AP-04 CCaaS unlocks other decisions | ✅ Green | Connect is the enabling platform; Lex/Bedrock decisions follow |
| AP-05 MCP Governance | ✅ Green | Bedrock Agents native MCP (May 2026) + ContextForge on AWS; IAM identity + CloudTrail audit |
| AP-06 Honest representation | ✅ Green | High AWS dependency acknowledged; switching cost increases over time with adoption — surfaced openly |
| AP-07 Semantic consistency | ⚠ Amber | No native semantic layer in Connect; shared initiative required (OI-08) |
| AP-08 EU AI Act transparency | ✅ Green | Virtual agent disclosure configurable in Contact Flow opening prompt |
| AP-09 Multi-opco | ✅ Green | Multi-instance or partitioned single-instance; strong opco configuration support |

**Lock-in consideration:** Amazon Connect creates progressive AWS lock-in. The deeper the adoption of Lex, Bedrock, Q in Connect, and Contact Lens, the higher the switching cost to a non-AWS CCaaS. This is not inherently bad — Belron already committed to AWS — but it should be surfaced explicitly in the platform decision.

---

## 8. Strengths and Gaps

### Strengths
- Native AWS integration eliminates cross-cloud cost and complexity for a confirmed AWS shop
- Amazon Bedrock provides access to multiple LLMs (Claude, Titan, Llama) via a single API — vendor-agnostic at the LLM layer within an AWS-aligned stack
- MCP native support (May 2026) directly satisfies MCP Governance requirements with IAM + CloudTrail
- Contact Lens: strong out-of-box QA without additional vendor
- Rapid deployment evidence: United Airlines deployed in 3 months vs. previous 12-month migrations
- No separate WFM vendor required: Connect Workforce Management now available
- S3 + CloudTrail natively satisfies EU AI Act Art. 12 audit requirements

### Gaps
- WhatsApp inbound is not native — requires partner integration
- WFM is newer and less mature than NICE or Genesys WEM for complex multi-site forecasting
- Lex is less capable than Genesys AI or Salesforce Einstein for out-of-box NLU without Bedrock augmentation
- Strong AWS dependency — not appropriate if Belron strategy changes to Azure-primary

---

## 9. Pricing Model

| Component | Model | Notes |
|---|---|---|
| Amazon Connect | Per-minute (voice) + per-contact (digital) | ~$0.018/min voice (US); EU pricing similar. No per-seat licence. |
| Amazon Lex | Per-request (text + voice) | $0.004/text request; $0.006/speech request. Volume discounts apply. |
| Amazon Bedrock | Per-token (model-dependent) | Claude pricing applies; cost scales with contact volume and LLM usage. |
| Amazon Q in Connect | Per active agent/month | Approx. $9/agent/month (US pricing). |
| Contact Lens | Per-minute analysed | ~$0.015/min. All contacts if 100% QA required. |
| Connect WFM | Per-agent/month | Included or low add-on; confirm with AWS account team. |

**Budget modelling note:** At Belron's scale (35 countries, multi-thousand agent estate), negotiate an enterprise discount agreement. Per-minute/per-contact can be cost-effective vs. per-seat for high-turnover or seasonal contact centres.

---

## 10. When Amazon Connect Is the Right Choice

**Select Amazon Connect if:**
- AWS is confirmed as Belron's primary or co-primary cloud provider for CCOTF workloads ✅ (confirmed May 2026)
- The AIDA PoC is deployed on AWS — using Bedrock for damage assessment creates native integration with Connect
- Speed of deployment is a priority (3-month deployment precedent)
- You want per-consumption pricing rather than per-seat
- MCP Governance via native Bedrock + CloudTrail is a governance requirement

**Caution if:**
- Belron has a strategic commitment to remain cloud-neutral long-term
- WFM requirements are highly complex multi-site and mature WEM is critical from day one
- Continental Carglass operations have data residency requirements that conflict with AWS EU regions (unlikely but validate)

---

*v0.1 — 2026-06-19. Pair with `ccotf-ra-vendor-agnostic.md` (base RA). EA Owner: Armo · Belron Enterprise Architecture.*
