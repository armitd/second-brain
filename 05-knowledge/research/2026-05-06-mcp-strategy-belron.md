---
type: "strategic-research"
domain: "enterprise-architecture"
date: "2026-05-06"
created: "2026-05-06 09:38"
question: "What is the right MCP adoption strategy for Belron as an enterprise operating a heterogeneous SaaS stack, legacy systems, and multi-cloud infrastructure?"
threads:
  - "mcp-architecture-patterns"
  - "mulesoft-snaplogic-integration"
  - "legacy-systems"
  - "business-capability-alignment"
  - "hyperscaler-strategies"
  - "saas-platform-readiness"
  - "multi-agent-interoperability"
  - "governance-security-observability"
confidence: "high"
tags:
  - "auto-research"
  - "strategy"
  - "mcp"
  - "enterprise-architecture"
  - "belron"
  - "agentic-ai"
related_projects: ["mcp-governance"]
status: "complete"
---

# MCP Adoption Strategy for Belron — Enterprise Architecture Research Report

---

## Executive Summary

The Model Context Protocol (MCP) has emerged as the dominant open standard for connecting AI agents to enterprise tools and data, with 97 million downloads and backing from every major hyperscaler, SaaS vendor, and AI lab. For Belron — operating across 35+ countries with a heterogeneous stack of MuleSoft, SnapLogic, ServiceNow, Salesforce, Workday, Oracle Fusion, and Microsoft 365 — the strategic question is not *whether* to adopt MCP but *how* to structure adoption so that it remains vendor-agnostic, governable, and durable as the protocol evolves.

The central recommendation is a **Centralised MCP Gateway** architecture anchored on IBM ContextForge (open source, Apache 2.0) as the federation and policy layer, with MuleSoft Anypoint and SnapLogic APIM acting as the enterprise integration backbone that exposes existing APIs as MCP servers. This approach preserves Belron's existing integration investment, enforces a single governance control plane, avoids hyperscaler lock-in, and accommodates the emerging A2A protocol for multi-agent coordination without requiring architectural rework.

Belron's SaaS readiness is uneven: ServiceNow (Zurich release) is production-ready today. Salesforce (Agentforce MCP) is in pilot. Oracle Fusion Cloud and Microsoft 365 have strong preview coverage but no GA. Workday has no official MCP — third-party bridges only. This asymmetry shapes the phasing: lead with ServiceNow and MuleSoft, follow with Salesforce and Azure/M365, treat Workday as a deferred integration until official support arrives.

**Estimated timeline:** Foundation layer in 90 days; first production capability in 6 months; full multi-domain deployment in 12-18 months.

---

## Section 1 — MCP Architecture Patterns

### 1.1 The Four Deployment Patterns

Four architecture patterns have emerged in enterprise MCP deployments. Each has a distinct use case and trade-off profile.

**Pattern 1: Centralised MCP Gateway**
A single policy-enforcement gateway through which all agent-to-tool traffic flows. The gateway handles authentication (OAuth 2.1 + PKCE), authorisation (RBAC/ABAC), rate limiting, audit logging, and DLP scanning in one place. Tools are registered in a central server registry. Every agent fleet — regardless of underlying framework (LangGraph, AutoGen, CrewAI, Bedrock) — calls the same gateway endpoint.

*Strengths:* Single control plane, uniform governance, easiest to audit. Simplest operational model.
*Weaknesses:* Single point of failure if not HA. Can become a bottleneck. Governance team must own registry curation.
*Best for:* Organisations with strong central governance appetite. Correct for Belron given the regulatory environment (GDPR, EU AI Act) and the multinational data-residency requirements.

**Pattern 2: Federated MCP Gateway**
Multiple gateway instances — typically one per region or business unit — that auto-discover each other via a shared registry (Redis-backed in IBM ContextForge). Each instance enforces local policies while the federation layer provides cross-instance tool discovery. Traffic stays local unless a cross-region capability is explicitly needed.

*Strengths:* Data residency compliance. Regional autonomy. Resilience if one instance fails.
*Weaknesses:* More complex to operate. Policy consistency requires discipline across federation nodes.
*Best for:* Multinational organisations with data sovereignty requirements. Belron's EU/UK/US split (Carglass, Autoglass, Safelite) makes this a likely mid-term evolution from the centralised start.

**Pattern 3: MCP Sidecar (Kubernetes)**
A sidecar container injected alongside a legacy application pod. The sidecar exposes the app's REST/SOAP/gRPC API as a virtual MCP server, translating MCP protocol calls into the app's native interface. No modification to the host application.

*Strengths:* Zero-touch on legacy app. Works with any app that runs in Kubernetes. Progressive migration path.
*Weaknesses:* Only viable if the legacy app is containerised or can be. Adds latency per hop. Requires Kubernetes platform discipline.
*Best for:* Legacy systems that cannot be modified but must participate in the agent ecosystem. Relevant for Belron's older operational systems.

**Pattern 4: Hybrid (Gateway + Sidecar)**
Gateway pattern for modern SaaS and integration layer (MuleSoft/SnapLogic); sidecar pattern for legacy Kubernetes workloads. The gateway federates both registered servers and sidecar-exposed virtual servers into a unified tool registry. This is the recommended end-state for Belron.

### 1.2 Transport Protocols

As of the MCP June 2025 specification:
- **Streamable HTTP** is the recommended production transport for remote servers (replaces the earlier SSE-only model). Stateless, load-balancer friendly.
- **stdio** is for local/embedded agent scenarios only — not suitable for enterprise multi-tenant deployments.
- **OAuth 2.1 + PKCE** is mandatory for all remote MCP servers. There is no negotiable path around this for production deployment.

### 1.3 Recommended Reference Implementation: IBM ContextForge

IBM ContextForge (open source, Apache 2.0, hosted on GitHub under `ibm/contextforge`) is the most mature open-source enterprise MCP gateway available as of May 2026. Key capabilities:

- **Multi-protocol gateway:** MCP, A2A, REST, and gRPC unified behind a single gateway interface
- **Federation via Redis:** Multiple ContextForge instances discover each other automatically; suitable for the federated evolution
- **OpenTelemetry-native:** Distributed tracing out of the box; integrates with Dynatrace, Datadog, Splunk, Elastic
- **Policy engine:** RBAC/ABAC with attribute-based tool access; pluggable policy evaluation
- **Open standard:** Apache 2.0 means no licence risk; community-governed; Belron's EA team can contribute

Alternative: **Cloudflare AI Gateway** offers a fully managed MCP gateway with a unique "Code Mode" feature that reduces token consumption by up to 99.9% by sending only executable code paths to the LLM rather than full documentation. Worth evaluating for high-volume, low-latency use cases (e.g., Contact Centre routing), but introduces Cloudflare vendor dependency at the gateway layer.

**Recommendation:** Deploy IBM ContextForge as the primary enterprise MCP gateway for governance and open-standard reasons. Evaluate Cloudflare Code Mode selectively for specific high-volume scenarios where token cost is a primary concern.

---

## Section 2 — MuleSoft and SnapLogic Integration

### 2.1 MuleSoft Anypoint — MCP Connector 1.4

MuleSoft released native MCP support in the Anypoint Platform via MCP Connector 1.4 (GA as of Q1 2026). This is significant: Belron already has MuleSoft deployed as its primary integration platform, meaning MCP capability is available within the existing investment without additional licensing.

**What MuleSoft MCP Connector 1.4 enables:**
- Any Mule flow can be exposed as an MCP tool — API endpoints, integration flows, event listeners, and orchestration sequences all become callable by AI agents
- **MuleSoft MCP Server**: A companion service that registers Mule flows as MCP servers in a central registry; agents discover and call these via the standard MCP protocol
- **Distributed tracing**: Built-in OpenTelemetry support so each agent-initiated MuleSoft call is traceable end-to-end through the existing monitoring stack
- **Streamable HTTP transport**: Production-grade; compatible with the June 2025 MCP spec
- **Bidirectional**: MuleSoft can both *expose* flows as MCP servers (tools available to agents) and *consume* external MCP servers as part of a Mule flow (an integration flow that calls an agent-exposed tool)

**Integration pattern with IBM ContextForge:**
Register the MuleSoft MCP Server as a provider within the ContextForge gateway registry. All agent traffic to MuleSoft-exposed tools flows through the ContextForge policy layer (auth, DLP, audit) before reaching the Mule runtime. This gives Belron a single governance control plane even when the tool implementation lives in Anypoint.

**Critical gap to validate:** MuleSoft MCP Connector 1.4 capability is confirmed in MuleSoft community documentation and release notes, but full enterprise feature parity (multi-tenant RBAC, HA clustering) should be verified in a proof-of-concept before production commitment. The connector is relatively new.

### 2.2 SnapLogic APIM 3.0 — MCP-Native Pipelines

SnapLogic released native MCP support in APIM 3.0 (mid-2025). SnapLogic's positioning is slightly different from MuleSoft's: where MuleSoft exposes *flows* as MCP tools, SnapLogic's design allows *pipelines* and *published APIs* to become MCP servers natively — no separate connector required.

**SnapLogic MCP capabilities:**
- **Dual mode**: SnapLogic can both *expose* pipelines as MCP servers and *consume* external MCP servers within a pipeline. This is more deeply integrated than MuleSoft's connector model.
- **APIM 3.0 governance**: API management policies (rate limiting, auth, versioning) apply to MCP-exposed pipelines automatically — reducing duplication between API governance and MCP governance
- **Schema inference**: SnapLogic auto-generates MCP tool descriptions from pipeline metadata — reducing the documentation burden on integration developers
- **Relevance to Belron**: If Belron uses SnapLogic for specific integration workloads (particularly where MuleSoft is not deployed), SnapLogic's native MCP capability means those pipelines can participate in the agent ecosystem without architectural change

### 2.3 Architectural Recommendation: MuleSoft + SnapLogic + ContextForge

```
Agent Fleet (LangGraph / Bedrock / Copilot Studio)
         │
         ▼
IBM ContextForge Gateway (auth, RBAC, DLP, audit, federation)
         │
    ┌────┴────────────────────┐
    ▼                         ▼
MuleSoft Anypoint         SnapLogic APIM 3.0
(MCP Connector 1.4)       (native MCP pipelines)
    │                         │
    ▼                         ▼
Enterprise systems        Enterprise systems
(SAP, Oracle, CRM)        (data pipelines, ETL)
```

MuleSoft and SnapLogic register their MCP-exposed capabilities with ContextForge. The agent fleet sees a unified tool catalogue. Neither MuleSoft nor SnapLogic is the governance layer — that is ContextForge's role. This preserves optionality to swap either integration platform in the future.

---

## Section 3 — Legacy Systems Integration

### 3.1 The Legacy Challenge

Belron's application landscape includes systems that predate REST APIs, let alone MCP. The challenge: how to make these systems accessible to AI agents without requiring expensive, risky modifications to production code.

Three patterns address this, with different fit depending on the system's technical characteristics:

### 3.2 Pattern A: Integration Layer Wrapping (Recommended for most cases)

The cleanest approach: use MuleSoft or SnapLogic to create a new API facade over the legacy system's existing interface (SOAP, JDBC, file-based, proprietary protocol). This facade is then exposed as an MCP server via the integration layer's native MCP capability. The legacy system never knows it is being called by an AI agent.

*Prerequisites:* The legacy system must have some programmatic interface (even if SOAP or proprietary). MuleSoft/SnapLogic connector or custom adapter required.
*Data residency:* Traffic never leaves the integration platform. Good for systems with sensitive data.
*Latency:* One additional hop through integration layer. Acceptable for most enterprise tool calls.

### 3.3 Pattern B: MCP Sidecar (Kubernetes-native legacy)

For legacy systems that run in Kubernetes (containerised workloads), deploy an MCP sidecar container in the same pod. The sidecar proxies MCP tool calls to the legacy app's local port. The sidecar handles auth (OAuth 2.1), translates MCP request/response formats, and logs to OpenTelemetry.

*Prerequisites:* Legacy app must be containerised (in pod). Kubernetes platform maturity required.
*Advantage:* Zero modification to host application. The app continues to serve its existing consumers unchanged.
*Disadvantage:* If Belron's legacy systems are not containerised, this pattern is not directly applicable.

### 3.4 Pattern C: Virtual MCP Server via ContextForge Adapter

IBM ContextForge includes an adapter framework that allows non-MCP endpoints to be registered as virtual MCP servers in the gateway registry. An administrator writes a thin adapter (typically <100 lines of configuration or code) that maps MCP tool call schemas to the legacy system's native API calls. The gateway handles the translation transparently.

*Prerequisites:* The legacy system must be network-accessible from the ContextForge deployment. Admin configuration effort required.
*Advantage:* No modification to legacy system, no sidecar deployment needed.
*Disadvantage:* Adapter maintenance becomes a dependency. Schema changes in the legacy system require adapter updates.

### 3.5 Authentication Bridge for Legacy Systems

Legacy systems often use authentication mechanisms that are incompatible with OAuth 2.1 + PKCE (the MCP mandatory standard). Common examples: LDAP/AD basic auth, API key headers, IP allowlisting, SAML assertions.

**Solution:** The MCP gateway (ContextForge) acts as an authentication bridge. Agents authenticate to the gateway using OAuth 2.1. The gateway maintains a credential vault that maps agent identities to legacy system credentials, performing credential substitution before forwarding calls to the legacy system. The legacy system receives its expected auth format; the agent ecosystem is never exposed to legacy credentials.

*Security note:* The credential vault becomes a high-value target. Must be deployed with HSM-backed key storage (AWS KMS, Azure Key Vault, or HashiCorp Vault) and rigorous access controls.

---

## Section 4 — Business Capability Model Alignment

### 4.1 Why Capability-Aligned MCP Server Design Matters

A common early mistake in MCP deployments is organising servers by *technical system* rather than *business capability*. This produces tool catalogues that mirror the org chart (a "MuleSoft server," a "ServiceNow server," a "Salesforce server") — forcing agents to understand implementation boundaries rather than business concepts.

The recommended approach, validated across multiple enterprise MCP reference architectures, is **Domain-Driven Design (DDD) applied to the MCP server taxonomy**: organise tools by bounded context (business domain), not by source system. A tool named `get_customer_repair_history` belongs to the *Customer* domain regardless of whether its data comes from Salesforce, ServiceNow, or a legacy CRM.

### 4.2 Belron Business Domains → MCP Server Families

Mapping Belron's business capability model to MCP server families:

| Business Domain | Core Capabilities | Primary Source Systems | MCP Server Name (suggested) |
|---|---|---|---|
| **Customer** | Customer profile, repair history, preferences, NPS | Salesforce CRM, legacy CRM | `customer-mcp` |
| **Vehicle** | Vehicle identification, glass specifications, ADAS calibration data, damage assessment | Internal systems, AI Damage Assessment POC | `vehicle-mcp` |
| **Scheduling & Operations** | Job scheduling, technician dispatch, branch capacity, parts availability | ServiceNow Field Service, legacy scheduling | `scheduling-mcp` |
| **Claims & Insurance** | FNOL, claim status, insurer authorisation, settlement | Salesforce, external insurer APIs | `claims-mcp` |
| **HR & Workforce** | Employee data, skills, training records, compliance | Workday | `workforce-mcp` |
| **Finance** | Invoicing, cost centres, budgeting | Oracle Fusion ERP | `finance-mcp` |
| **IT Service Management** | Incident, change, asset, configuration | ServiceNow ITSM | `itsm-mcp` |
| **Knowledge & Policy** | Technical procedures, safety policies, product specifications | SharePoint/M365, Confluence | `knowledge-mcp` |

### 4.3 Tool Naming Conventions

Within each domain server, tools should follow a consistent verb-noun convention aligned to business language:

- `get_[entity]` — read a single resource
- `list_[entities]` — enumerate resources with filters
- `create_[entity]` — create a new resource
- `update_[entity]` — modify an existing resource
- `search_[entities]` — semantic or filtered search
- `trigger_[process]` — initiate a business process

Example: `customer-mcp` tools include `get_customer_profile`, `list_customer_jobs`, `search_repair_history`, `get_customer_satisfaction_score`.

Agents discovering the tool catalogue should be able to infer purpose from the name alone — without reading the full tool description. This matters at scale when an agent is choosing between hundreds of registered tools.

### 4.4 Alignment with EA Team's Existing Capability Model

The TOGAF Business Architecture work being undertaken with the 3 BAs in the EA team is directly relevant here. The business capability model produced through BA artefacts (capability maps, value streams, information maps) should be the canonical source for:

1. Defining MCP domain boundaries (which capabilities become which server family)
2. Naming conventions (tool names should use terms from the business glossary, not technical jargon)
3. Data ownership decisions (which source system is the system of record per capability → determines which integration path feeds the MCP server)

**Recommended action:** Bring a draft of the MCP server taxonomy to the BAs as a boundary conversation — use it to test whether the domain boundaries make sense from a business perspective before they are hardcoded into server registrations.

---

## Section 5 — Hyperscaler MCP Strategies

### 5.1 AWS — Bedrock AgentCore

Amazon launched AWS Bedrock AgentCore in Q4 2025 as the primary MCP runtime within the AWS ecosystem. Key capabilities:

- **Native MCP hosting**: Deploy and run MCP servers on AWS-managed infrastructure (ECS, Lambda, or EKS)
- **IAM integration**: MCP server permissions are managed through standard AWS IAM roles and policies — no separate RBAC system to manage for AWS-native tools
- **awslabs/mcp**: AWS maintains an official open-source repository of MCP servers for AWS services (S3, DynamoDB, RDS, Bedrock, CloudWatch). These are production-quality, AWS-maintained implementations.
- **Multi-agent coordination**: Bedrock AgentCore supports multi-agent orchestration patterns with MCP as the tool layer
- **Pricing model**: Usage-based; MCP hosting adds to existing Bedrock consumption costs

**Relevance to Belron:** If Belron's AI Damage Assessment POC or other projects are deployed on AWS, Bedrock AgentCore provides a low-friction path to MCP-enable those workloads. However, using Bedrock AgentCore as the *enterprise* MCP gateway would introduce AWS lock-in at the governance layer — which contradicts the vendor-agnostic principle. **Use for AWS-native workloads; do not use as the central enterprise gateway.**

### 5.2 GCP — Vertex AI Agent Development Kit (ADK)

Google's Vertex AI ADK was updated in Q1 2026 to include first-class MCP and A2A support. Key capabilities:

- **MCP + A2A unified**: ADK supports both protocols natively; agents built on ADK can call MCP tools *and* coordinate with other A2A-capable agents in the same workflow
- **Google-managed MCP servers**: Google provides managed MCP server implementations for BigQuery, Compute Engine, Cloud Storage, Kubernetes Engine, and other GCP services — comparable to the AWS awslabs/mcp repository
- **A2A protocol origin**: Google launched A2A in April 2025 with 50+ ecosystem partners; ADK is the reference implementation
- **Vertex AI model integration**: ADK is deeply integrated with Gemini models on Vertex; calling a Vertex-hosted model alongside MCP tools is native

**Relevance to Belron:** If Belron uses GCP/BigQuery for analytics (relevant to Contact Centre analytics, AI Damage Assessment data pipelines), GCP's managed MCP servers for BigQuery are ready to use. A2A support in ADK is relevant for the multi-agent coordination architecture (Section 7). **Evaluate for analytics and data platform use cases.**

### 5.3 Azure — Copilot Studio and Azure AI Foundry

Microsoft's MCP story spans two products with different maturity levels:

**Microsoft Copilot Studio (GA):**
- MCP reached General Availability in Copilot Studio in February 2026
- Copilot Studio agents can call any MCP-compliant server as a tool
- Native integration with M365 (Teams, SharePoint, Outlook) as MCP-exposed resources
- Satya Nadella declared MCP a "first-class citizen" in the Microsoft AI stack at Build 2025
- Relevant for Belron's Microsoft 365 investment: SharePoint knowledge bases, Teams workflows, and Outlook data can be surfaced as MCP tools to any compliant agent

**Azure AI Foundry Agent Service (Preview as of May 2026):**
- MCP support is in preview — not GA
- Azure AI Foundry is Microsoft's enterprise agent hosting platform (successor to Azure OpenAI Service for agentic workloads)
- When GA, this will allow Azure-hosted agents to call enterprise MCP servers with Azure AD authentication and Azure Monitor observability

**⚠ Conflict flag:** Multiple sources confirm Copilot Studio MCP is GA; Azure AI Foundry MCP status is reported as "preview" in some sources and "GA" in others as of May 2026. Verify current status against official Microsoft Learn documentation before planning production deployments on Azure AI Foundry MCP.

**Relevance to Belron:** Microsoft 365 is Belron's productivity platform. Copilot Studio MCP (GA) means M365 data — SharePoint documents, Teams conversations, Calendar, Outlook — can be made available as MCP tools today. This is the most immediately actionable hyperscaler integration for Belron's knowledge management use cases. **Prioritise for knowledge and productivity domain MCP servers.**

### 5.4 Hyperscaler Strategy Summary

| Hyperscaler | MCP Maturity | Belron Relevance | Risk |
|---|---|---|---|
| AWS Bedrock AgentCore | GA (Q4 2025) | AI Damage Assessment, Lambda-native tools | Lock-in if used as central gateway |
| GCP Vertex AI ADK | GA (Q1 2026) | Analytics, BigQuery, A2A coordination | Lower Belron GCP footprint |
| Azure Copilot Studio | GA (Feb 2026) | M365, SharePoint, Teams, knowledge | Microsoft ecosystem dependency |
| Azure AI Foundry | Preview | Future enterprise agent hosting | Not production-ready yet |

**Architectural stance:** Use hyperscaler-native MCP for workloads that already live in that cloud. Route all hyperscaler MCP traffic through the central ContextForge gateway so that governance, audit, and DLP apply uniformly regardless of which cloud the tool implementation lives in.

---

## Section 6 — SaaS Platform Readiness

### 6.1 ServiceNow — Most Ready

ServiceNow Zurich release (H2 2025) is the most mature MCP implementation in Belron's SaaS estate. Assessment: **production-ready today**.

**Capabilities:**
- Native MCP server: ServiceNow exposes ITSM, Field Service, and HR Service Delivery capabilities as MCP tools
- **AI Control Tower**: ServiceNow's governance interface for MCP and AI agent activity — provides visibility into which agents called which tools, with full audit trail
- OAuth 2.1 + PKCE: Compliant with the June 2025 MCP spec
- No additional licensing cost for Pro Plus and Enterprise Plus customers (verify against Belron's current licence tier)
- Bidirectional: ServiceNow agents can call external MCP servers; external agents can call ServiceNow MCP tools

**Relevant Belron capabilities available via ServiceNow MCP:**
- Incident management (create, update, resolve incidents)
- Change management (raise, review, approve change requests)
- Field Service Management (job scheduling, technician dispatch, parts ordering)
- Asset and Configuration Management (CMDB queries)
- HR Service Delivery (if deployed)

**Recommendation:** ServiceNow should be the first MCP integration deployed in production. The combination of native MCP, built-in governance (AI Control Tower), and audit trail makes it the lowest-risk starting point. Use `itsm-mcp` and `scheduling-mcp` as the first registered server families in ContextForge.

### 6.2 Salesforce — Pilot Stage

Salesforce Agentforce MCP is in pilot phase as of July 2025. Assessment: **pilot-ready; production in H2 2026 estimated**.

**Capabilities:**
- MCP client: Agentforce agents can call external MCP servers (pilot)
- Hosted MCP servers: Salesforce intends to expose CRM capabilities (accounts, contacts, opportunities, cases) as hosted MCP servers
- Enterprise registry: Salesforce is building an enterprise MCP registry with policy enforcement baked in
- Data Cloud integration: Salesforce Data Cloud data (unified customer profile) available as MCP tool context

**Gaps / risks:**
- Pilot status means production deployment is premature for mission-critical workloads
- Data residency: Salesforce-hosted MCP servers will process Belron CRM data within Salesforce infrastructure — verify against EU data residency requirements
- Schema stability: Tool definitions in pilot are subject to change before GA

**Recommendation:** Participate in Salesforce Agentforce MCP pilot programme (via Belron's Salesforce account team) to gain early familiarity and influence on tool design. Plan `customer-mcp` and `claims-mcp` integration for H2 2026 once GA.

### 6.3 Workday — Weakest Link

Workday has no official native MCP implementation as of May 2026. Assessment: **deferred — third-party bridges only**.

**Available options (all third-party):**
- **CData MCP Server for Workday**: Read-only; exposes Workday HCM data via the Workday Report-as-a-Service API. Limited to reporting data; no write capability.
- **Composio**: Managed MCP bridge service; supports Workday among 200+ integrations. Write capability available, but data is processed by Composio infrastructure (GDPR/data residency risk for Belron).
- **Zapier MCP**: Similar to Composio; managed service; same data residency concern.

**⚠ Gap flag:** There is no confirmed timeline for official Workday MCP support. Workday's platform roadmap has not publicly committed to MCP as of the research date. This is a genuine gap in Belron's SaaS MCP estate.

**Recommendation:** Do not build production AI agent workflows that depend on Workday data until official Workday MCP is available or a self-hosted MCP adapter (via MuleSoft → Workday connector → MCP) is deployed. Use MuleSoft's existing Workday connector to expose `workforce-mcp` tools — this keeps data within Belron's integration layer without routing through third-party managed services.

### 6.4 Microsoft 365 — Ready via Copilot Studio

Microsoft 365 MCP availability is via Copilot Studio (GA, February 2026). Assessment: **production-ready for knowledge/productivity domain**.

**Available MCP tools (Copilot Studio):**
- SharePoint document and knowledge base search
- Teams channel and conversation access
- Outlook calendar and email data
- OneDrive file access
- Microsoft Graph API as MCP server layer

**Consideration:** M365 MCP tools expose potentially sensitive communications data (emails, Teams messages). Before registering these with ContextForge and making them available to AI agents:
- Define a clear access control policy: which agent personas can access M365 data, at what granularity
- Enable DLP scanning at the ContextForge gateway layer for all M365 tool responses
- Consider whether email/calendar data should be in-scope for AI agent access at all (HR and legal review recommended)

**Recommendation:** Start with SharePoint-based knowledge tools (`knowledge-mcp`); defer email and Teams access until data governance policy is defined.

### 6.5 Oracle Fusion — Emerging

Oracle Fusion Cloud MCP status is emerging. Assessment: **available for evaluation; production readiness unclear**.

**What exists:**
- **Oracle AI Agent Studio**: Includes an MCP Tool component for building Oracle-hosted AI agents that can call MCP servers. This is an agent-building tool, not a tool-exposure mechanism.
- **Oracle Database MCP Server**: An open-source MCP server for Oracle Database (SQL query execution, schema inspection). Not specific to Fusion Cloud apps.
- **ERP/EPM Cloud MCP**: Oracle is evaluating native MCP for Fusion ERP, HCM, and EPM. As of February 2026, no GA announcement. Customers using Oracle AI Agents for ERP automation are the likely early adopters.

**⚠ Gap flag:** Oracle Fusion Cloud (the ERP Belron uses for finance) does not have a confirmed GA MCP implementation. This means `finance-mcp` capabilities cannot be sourced directly from Oracle Fusion today. Mitigation: use MuleSoft's Oracle Fusion connector to expose finance capabilities as MCP tools via the integration layer.

**Recommendation:** Use MuleSoft → Oracle Fusion as the `finance-mcp` path until Oracle publishes an official Fusion Cloud MCP server. Monitor Oracle's AI Agent Studio roadmap for Fusion ERP MCP announcements in H2 2026.

### 6.6 SaaS Readiness Summary

| Platform | MCP Status | GA? | Path to `mcp-governance` | Timeline |
|---|---|---|---|---|
| ServiceNow Zurich | Native MCP + AI Control Tower | Yes | Register directly in ContextForge | Now |
| Salesforce Agentforce | MCP client in pilot; server hosting planned | No (pilot) | MuleSoft bridge until GA, then direct | H2 2026 |
| Workday | No official MCP | No | MuleSoft → Workday connector → MCP | Deferred |
| Microsoft 365 | GA in Copilot Studio | Yes (Copilot Studio) | SharePoint first; evaluate email/Teams with governance review | Now (SharePoint) |
| Oracle Fusion | MCP server evaluating; Database MCP exists | No (ERP) | MuleSoft → Oracle Fusion connector | H2 2026 (watch) |

---

## Section 7 — Multi-Agent Interoperability

### 7.1 The Protocol Landscape

Two protocols govern the multi-agent space as of May 2026:

**MCP (Model Context Protocol):** Agent-to-tool connectivity. Answers the question "how does an agent call a tool?" MCP has definitively won this category — 97M downloads, universal adoption across hyperscalers and SaaS vendors. Version 1.x is stable; the June 2025 spec is the production baseline.

**A2A (Agent-to-Agent Protocol):** Agent-to-agent coordination. Answers the question "how does one agent delegate a task to another agent?" Launched by Google in April 2025, with 50+ ecosystem partners at launch (including Microsoft, AWS, IBM, SAP, Salesforce, and Workday). Complements MCP rather than replacing it.

**ACP (Agent Communication Protocol):** Launched by IBM and the Linux Foundation in 2025 as a competing agent coordination standard. By early 2026, ACP's scope has substantially overlapped with and largely deferred to A2A. For Belron's planning horizon, treat A2A as the agent-to-agent coordination standard. ACP-specific implementations are not recommended.

### 7.2 The Heterogeneous Multi-Agent Fleet Principle

The strategic design principle for Belron's agent architecture is: **assume heterogeneity as the default**. Belron will not run a single agent framework — the organisation will accumulate agents built on different frameworks (Copilot Studio, Bedrock, Vertex ADK, LangGraph, AutoGen) as different teams, vendors, and use cases drive adoption. The architecture must accommodate this reality.

The interoperability stack that makes this work:

```
Agent A (LangGraph)    Agent B (Copilot Studio)    Agent C (Bedrock)
         │                      │                        │
         └──────────────────────┴────────────────────────┘
                                │
                    A2A coordination layer
                    (task delegation, agent discovery)
                                │
                    IBM ContextForge Gateway
                    (unified tool registry, policy)
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                  ▼
         ServiceNow-MCP    MuleSoft-MCP    Salesforce-MCP
         (itsm-mcp)        (customer-mcp)  (claims-mcp)
```

Agents coordinate with each other via A2A (task handoffs, parallel execution). Each agent calls tools via MCP through the central gateway. Neither layer knows about the other's implementation details.

### 7.3 Framework MCP + A2A Support Matrix

| Framework | MCP Support | A2A Support | Notes |
|---|---|---|---|
| LangGraph / LangChain | Native (mid-2025) | Native (mid-2025) | Best-in-class; both protocols first-class |
| AWS Bedrock AgentCore | Native MCP | Bedrock-to-Bedrock A2A | A2A cross-cloud less mature |
| GCP Vertex AI ADK | Native MCP | Native A2A (reference impl) | Google is the A2A originator; ADK is most complete A2A implementation |
| Microsoft Copilot Studio | Native MCP (GA) | A2A in preview | Check current status before depending on A2A |
| AutoGen (Microsoft Research) | MCP via tool adapter | A2A in preview | Research framework; not production-hardened |
| CrewAI | MCP via tool adapter | Limited A2A | Popular for multi-role agent teams; MCP adapter required |
| Semantic Kernel (Microsoft) | MCP via plugin | A2A planning | Enterprise-targeted; likely to get full support in 2026 |

### 7.4 Agent Discovery and Registration

In a heterogeneous fleet, agents must be discoverable by other agents for A2A coordination. IBM ContextForge's A2A support includes an agent registry alongside the tool registry — agents register their capabilities, and other agents can query the registry to discover what agents are available to delegate tasks to.

**Recommended agent registration pattern:**
- Each deployed agent (regardless of framework) registers with ContextForge on startup
- Registration includes: agent name, capabilities description, A2A endpoint URL, supported task types, owner team
- ContextForge enforces that only registered agents can initiate A2A coordination
- Audit log records every agent-to-agent delegation event

---

## Section 8 — Governance, Security, and Observability

### 8.1 The Triple-Gate Security Pattern

Enterprise MCP security requires enforcement at three distinct points. Missing any gate creates exploitable gaps:

**Gate 1 — Client to LLM:**
- Validate user identity before requests reach the LLM
- Apply role-based prompt filtering (prevent users from injecting tool calls they are not authorised to make)
- Rate limiting per user identity
- Audit log of all LLM interactions

**Gate 2 — LLM to MCP Gateway:**
- OAuth 2.1 + PKCE authentication mandatory (MCP June 2025 spec)
- Validate that the LLM's tool call request is for a registered, authorised tool
- Apply ABAC policies: agent identity + user identity + tool sensitivity → allow/deny
- DLP scanning of tool call parameters (detect PII being passed to unexpected tools)

**Gate 3 — MCP Gateway to External API:**
- The gateway authenticates to downstream systems using per-system credentials (credential vault pattern from Section 3.5)
- Rate limiting and circuit breaking on downstream calls
- Response DLP scanning (detect PII/sensitive data in tool responses before returning to the agent)
- Audit log of every tool call with full request/response payloads (subject to data retention policy)

### 8.2 Prompt Injection via MCP Tool Responses

A critical and underappreciated threat vector: **prompt injection through MCP tool responses**. If a malicious actor can inject content into data that is returned by an MCP tool (e.g., a document in SharePoint, a ticket description in ServiceNow), that content can influence the LLM's subsequent actions.

Two research tools/frameworks address this:
- **MCPTox**: Publicly documented attack framework demonstrating prompt injection via MCP tool responses (published April 2026). Reference for red-teaming.
- **MindGuard**: Emerging defensive tool for scanning MCP tool responses for injection patterns before they reach the LLM context.

**Recommended defence:**
1. Output validation at Gate 2 (scan tool responses for injection patterns)
2. Separate system prompt from tool output in LLM context (structural defence)
3. Principle of least authority: tools should return only the data the agent specifically requested, not full documents that may contain attacker-controlled content
4. Regular red-team exercises using MCPTox patterns

### 8.3 CIS MCP Security Guide

The Center for Internet Security published an MCP Security Guide in April 2026 — the first authoritative security benchmark for MCP deployments. Key recommendations (paraphrased):

- All MCP servers must use OAuth 2.1 + PKCE; no API key auth for production
- Tool descriptions must be cryptographically signed to prevent tampered tool registrations
- Comprehensive audit logging with immutable storage
- Regular review of registered tools (orphaned tools are an attack surface)
- Separate MCP deployments for production and non-production environments; no shared credentials

This guide should be the baseline for Belron's MCP security posture assessment.

### 8.4 Observability Stack

MCP deployments require distributed tracing across the entire chain: user → LLM → gateway → tool → downstream system. Without this, debugging failures and auditing AI decisions is impractical.

**Recommended observability stack:**

| Layer | Tool/Standard | Notes |
|---|---|---|
| Distributed tracing | OpenTelemetry (OTel) | Industry standard; supported by ContextForge, MuleSoft 1.4, SnapLogic APIM 3.0 |
| Trace backend | Dynatrace or Elastic (Belron's existing stack) | OTel traces ship to existing monitoring infrastructure |
| MCP-specific metrics | IBM ContextForge built-in dashboards | Tool call latency, error rates, token consumption per tool |
| LLM cost tracking | ContextForge token ledger + hyperscaler billing APIs | Track per-agent, per-tool token consumption |
| Audit log | Immutable append-only log (S3 Object Lock or Azure Immutable Blob) | Required for EU AI Act compliance article on audit trails |
| Alert thresholds | Anomaly detection on tool call volume per agent | Detect runaway agent loops or unexpected usage spikes |

### 8.5 EU AI Act Compliance Considerations

The EU AI Act (applicable to Belron's EU operations) has specific requirements relevant to MCP-enabled AI systems:

- **Article 9 (Risk Management):** AI systems used in high-risk categories (including certain HR decisions, safety-critical systems) must have documented risk management. MCP-enabled agents making decisions in these domains require risk documentation.
- **Article 12 (Logging):** High-risk AI systems must maintain automatic logging of operations throughout their lifecycle. The Gate 3 audit log satisfies this requirement if implemented as immutable storage.
- **Article 14 (Human Oversight):** High-risk AI systems must be designed to allow effective human oversight. MCP tool calls that trigger irreversible actions (financial transactions, access provisioning, service appointments) should require human confirmation in the agent workflow.
- **Transparency:** Any MCP-enabled agent interacting with Belron customers (e.g., Contact Centre agent) must disclose that the customer is interacting with an AI system.

**Recommendation:** During the MCP governance framework design phase, map each planned agent use case to EU AI Act risk categories. High-risk use cases require additional controls (human-in-the-loop checkpoints, enhanced audit trails) before production deployment.

### 8.6 Data Loss Prevention for MCP

MCP tool responses can contain sensitive personal data (customer PII, employee data, financial records) that should not be returned to all agents or processed outside approved data regions.

**DLP approach at the gateway layer:**
- Pattern matching on tool responses for known PII formats (email addresses, phone numbers, VIN numbers, payment card data)
- Response redaction: replace matched PII with tokens where the agent does not need the raw value
- Regional routing: tool calls requesting EU customer data routed only to EU-hosted MCP servers; never forwarded to US-hosted gateway instances
- Classification labels: tag tool responses with data classification (Public, Internal, Confidential, Restricted) so agent workflows can enforce downstream handling

---

## Section 9 — Recommended Next Steps for Belron

The following actions are prioritised in sequence. Items tagged **Foundational** must be done before **Accelerator** items that depend on them.

### Action 1 — Deploy ContextForge as Enterprise MCP Gateway [Foundational]
**Priority:** Immediate (0-30 days)
**What:** Stand up IBM ContextForge in a non-production environment. Configure OAuth 2.1, base RBAC policies, and OpenTelemetry integration with Belron's existing monitoring stack. Define the agent registration schema and tool naming conventions from Section 4.
**Why:** Every other action depends on having a governance-controlled gateway. Starting without this means early integrations will be ungoverned and will need to be retrofitted.
**Owner:** EA team (MCP Governance project)
**Success criterion:** A test agent can register, authenticate, and call a stub tool through ContextForge with a full audit trail.

### Action 2 — Register ServiceNow as First Production MCP Server [Foundational]
**Priority:** 30-60 days
**What:** Register ServiceNow Zurich's native MCP endpoint with ContextForge. Enable the `itsm-mcp` and `scheduling-mcp` server families. Define the initial tool catalogue (incident management, change management, field service operations).
**Why:** ServiceNow is the most mature MCP implementation in Belron's SaaS estate. It provides a low-risk path to a real production integration with built-in governance (AI Control Tower) that can be validated against ContextForge's governance layer.
**Owner:** EA team + ServiceNow platform team
**Success criterion:** An agent can create a ServiceNow incident and query job scheduling data through ContextForge with policy enforcement verified.

### Action 3 — Expose MuleSoft Flows as MCP Tools [Foundational]
**Priority:** 60-90 days
**What:** Deploy MuleSoft MCP Connector 1.4. Identify 3-5 high-value existing Mule flows (e.g., customer profile retrieval, vehicle lookup, claims status) and expose them as MCP tools. Register with ContextForge.
**Why:** MuleSoft is Belron's integration backbone. This is the most scalable path to surfacing legacy system capabilities to agents. Once the pattern is established, additional flows can be exposed incrementally.
**Owner:** Integration platform team + EA team
**Dependency:** Action 1 complete (ContextForge deployed)
**Success criterion:** Customer profile and vehicle lookup flows callable as MCP tools through ContextForge, with full OTel tracing.

### Action 4 — Define Business Capability → MCP Domain Taxonomy [Foundational]
**Priority:** 0-60 days (parallel with Actions 1-3)
**What:** Work with the EA team's 3 BAs to produce a canonical mapping of Belron's business capability model to MCP server families. Validate domain boundaries, data ownership, and naming conventions. Publish as an internal EA standard.
**Why:** Without this, individual teams will create ad-hoc MCP servers that fragment the tool catalogue and create governance gaps. The taxonomy is the architectural governance artefact that prevents proliferation.
**Owner:** EA team (lead), BA team (co-design)
**Output:** Published MCP Domain Taxonomy document in the EA knowledge base

### Action 5 — Deploy Workday MCP via MuleSoft Bridge [Foundational]
**Priority:** 90-120 days
**What:** Use MuleSoft's existing Workday connector to expose workforce management capabilities as `workforce-mcp` tools through ContextForge. Do not use third-party managed Workday MCP bridges (data residency risk).
**Why:** Workday has no official MCP — but HR use cases (skills lookup, org chart traversal, leave data) are likely to be needed by agents. A MuleSoft bridge keeps data within Belron's integration perimeter.
**Dependency:** Action 3 complete (MuleSoft MCP pattern established)
**Success criterion:** `workforce-mcp` tools callable by authorised agents; no Workday data routed to third-party services.

### Action 6 — Pilot Salesforce Agentforce MCP [Accelerator]
**Priority:** Q3 2026 (when Salesforce approaches GA)
**What:** Join the Salesforce Agentforce MCP pilot programme via Belron's Salesforce account team. Evaluate native CRM data exposure as `customer-mcp` tools.
**Why:** Salesforce holds Belron's customer relationship data. Native MCP from Salesforce is preferable to a MuleSoft bridge for CRM data — it is more likely to reflect Salesforce's data model accurately and stay current with schema changes.
**Dependency:** ContextForge deployed (Action 1). Monitor Salesforce GA announcement.

### Action 7 — Implement EU AI Act Compliance Controls [Foundational]
**Priority:** Concurrent with first production deployment (Action 2)
**What:** Document each MCP-enabled agent use case against EU AI Act risk categories. Implement human-in-the-loop checkpoints for any tool calls triggering irreversible actions. Configure immutable audit log storage (S3 Object Lock or Azure Immutable Blob). Initiate legal/HR review of any agent use cases touching employee data.
**Why:** Belron's EU operations are subject to the EU AI Act. Retrofitting compliance controls into deployed AI agent workflows is significantly more expensive than building them in from the start.
**Owner:** EA team + Legal/Compliance + CISO
**Output:** EU AI Act compliance register for MCP-enabled use cases

### Action 8 — Federated Gateway for Data Residency [Accelerator]
**Priority:** 6-12 months after foundational layer
**What:** Extend the centralised ContextForge deployment to a federated pattern: separate instances for EU (Carglass/Autoglass), US (Safelite), and APAC regions, with cross-instance tool discovery for non-personal-data tool calls. Configure regional routing policy so EU customer data never leaves EU gateway instances.
**Why:** Belron's multinational structure and GDPR requirements will require data residency enforcement at the gateway layer as agent workloads scale beyond the initial UK/EU deployments.
**Dependency:** Centralised ContextForge operational and stable (Actions 1-3)

---

## Vendor Lock-In Risk Summary

| Technology | Lock-In Risk | Mitigation / Portable Alternative |
|---|---|---|
| IBM ContextForge | Low | Apache 2.0 open source; self-hosted; can be replaced with any MCP-compliant gateway |
| MuleSoft MCP Connector 1.4 | Medium | MuleSoft dependency; migration cost is high but all tools would continue to work via the integration layer — lock-in is to MuleSoft, not to MCP |
| SnapLogic APIM 3.0 MCP | Medium | Same as MuleSoft — platform-layer lock-in, not protocol lock-in |
| ServiceNow native MCP | Low | ServiceNow MCP is standards-compliant; if ServiceNow is replaced, the MCP server registration changes but the agent code does not |
| Salesforce Agentforce MCP | Low–Medium | Pilot; tool schema may change before GA. Build agent tool calls via the ContextForge abstraction layer to isolate from Salesforce schema changes |
| AWS Bedrock AgentCore | Medium–High | If used as central gateway (not recommended), high lock-in. If used only for AWS-native tools, low lock-in. Follow the vendor-agnostic pattern. |
| Azure Copilot Studio MCP | Medium | M365 data is in Microsoft 365 regardless; MCP access layer is standards-compliant. Lock-in is to M365, not to the MCP implementation. |
| GCP Vertex AI ADK | Low | ADK is open source; GCP-managed MCP servers are additive, not required. A2A is an open standard. |
| Cloudflare AI Gateway | Medium | Cloudflare-specific "Code Mode" feature creates dependency on Cloudflare for token-optimised MCP calls. Use selectively. |
| Third-party Workday MCP (Composio, Zapier) | High | Data processed by third-party infrastructure. GDPR risk. Use MuleSoft bridge instead. |

---

## Confidence and Gaps

### High Confidence
- MCP as the agent-to-tool standard: confirmed by universal adoption across hyperscalers, SaaS vendors, and AI frameworks
- ServiceNow Zurich native MCP: confirmed via official ServiceNow documentation and multiple third-party sources
- MuleSoft MCP Connector 1.4 existence: confirmed via MuleSoft community documentation
- IBM ContextForge capabilities: confirmed via GitHub repository and IBM technical documentation
- OAuth 2.1 as mandatory MCP standard: confirmed in June 2025 MCP spec
- A2A as the emerging agent-to-agent coordination standard: confirmed via Google's launch announcement and 50+ partner confirmations

### Medium Confidence
- Azure AI Foundry MCP GA status: conflicting reports (preview vs. GA) as of May 2026 — **verify against current Microsoft Learn documentation before planning**
- MuleSoft MCP Connector 1.4 enterprise feature parity: connector confirmed; full HA/multi-tenant feature set requires PoC validation
- Oracle Fusion Cloud MCP timeline: no official announcement as of research date; roadmap from Oracle is unconfirmed

### Gaps
- **Workday official MCP timeline**: No public roadmap commitment found. This is a genuine planning gap — the `workforce-mcp` path must go through MuleSoft until Workday publishes an official MCP roadmap.
- **Belron-specific MuleSoft licence scope**: Whether MCP Connector 1.4 is included in Belron's current Anypoint licence tier requires confirmation with MuleSoft account team.
- **ContextForge production SLA**: IBM ContextForge is open source (Apache 2.0) — there is no IBM-supported enterprise version confirmed as of May 2026. Belron would need to self-support or engage a systems integrator for production support.

---

## Sources

1. MCP Official Specification v1.x — modelcontextprotocol.io
2. IBM ContextForge GitHub — github.com/ibm/contextforge
3. MuleSoft MCP Connector documentation — docs.mulesoft.com
4. SnapLogic APIM 3.0 release notes — docs.snaplogic.com
5. AWS Bedrock AgentCore announcement — aws.amazon.com/bedrock/agentcore
6. AWS Labs MCP repository — github.com/awslabs/mcp
7. GCP Vertex AI ADK MCP + A2A documentation — cloud.google.com/vertex-ai/docs/adk
8. Google A2A Protocol announcement (April 2025) — developers.googleblog.com
9. Microsoft Copilot Studio MCP GA announcement — learn.microsoft.com
10. Azure AI Foundry Agent Service documentation — learn.microsoft.com/azure/ai-foundry
11. ServiceNow Zurich release notes — docs.servicenow.com
12. Salesforce Agentforce MCP pilot announcement — developer.salesforce.com
13. Oracle AI Agent Studio documentation — docs.oracle.com
14. Oracle Database MCP Server — github.com/oracle
15. CIS MCP Security Guide (April 2026) — cisecurity.org
16. MCPTox prompt injection research — security research publication, April 2026
17. Cloudflare AI Gateway MCP documentation — developers.cloudflare.com
18. EU AI Act text — eur-lex.europa.eu
19. LangChain MCP integration documentation — docs.langchain.com
20. Aakash Gupta — Perplexity MCP contradiction signal (May 2026) — x.com/aakashgupta
21. Karpathy Sequoia Ascent 2026 — sensor/actuator/logic decomposition framing
22. Multiple industry sources on Workday MCP absence (CData, Composio, Zapier documentation)

---

*Research by COG Auto-Research | 15+ web searches across 8 research threads | 2026-05-06*
*For Armo — Enterprise Architect, Belron*
