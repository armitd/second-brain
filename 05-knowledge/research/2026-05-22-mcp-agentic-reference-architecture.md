---
type: "reference-architecture"
artefact_class: "TOGAF Architecture Definition Document (extract)"
domain: "enterprise-architecture"
date: "2026-05-22"
created: "2026-05-22"
title: "MCP-Led Agentic AI Reference Architecture"
owner: "Armo — Enterprise Architecture, Belron"
status: "v0.1 — Working Draft"
related_projects: ["mcp-governance", "ai-damage-assessment-poc", "contact-centre-future"]
related_research: ["2026-05-06-mcp-strategy-belron.md"]
notation: "TOGAF 10 / ArchiMate 3.2"
tags:
  - "reference-architecture"
  - "mcp"
  - "agentic-ai"
  - "togaf"
  - "archimate"
  - "ea"
confidence: "high"
---

# MCP-Led Agentic AI Reference Architecture
*A working reference architecture for governing agent-led automation across Belron's heterogeneous estate.*

> **Companion document:** [[2026-05-06-mcp-strategy-belron]] provides the *adoption strategy* (what to deploy, in what order, with which vendors). This document provides the *reference model* (layers, components, interfaces, patterns) used to govern individual projects against a consistent architecture.

---

## Document Control

| Field | Value |
|---|---|
| Version | 0.1 (Working Draft) |
| Date | 2026-05-22 |
| Owner | Armo, Enterprise Architecture |
| Notation | TOGAF 10 ADM phases A–D; ArchiMate 3.2 vocabulary |
| Review cadence | Quarterly; immediately on MCP spec or Anthropic governance change |
| Companion strategy | [[2026-05-06-mcp-strategy-belron]] |
| Related project | [[04-projects/mcp-governance/PROJECT-OVERVIEW]] |

---

# Phase A — Architecture Vision

## A.1 Purpose

Provide a Belron-wide reference model that any project introducing agentic AI behaviour must conform to, so that:

1. Agents are introduced through a single, governed surface rather than per-project point solutions
2. Tool exposure is consistent (MCP-compliant, identity-bound, audited) regardless of source system
3. Multi-agent coordination is anticipated, not retrofitted
4. Semantic meaning of tool data is governed, not left to each agent to infer
5. IPO-readiness obligations (audit, accountability, EU AI Act, GDPR) are satisfied by construction

## A.2 Scope

**In scope:** any AI system that (a) calls external tools or data sources, or (b) coordinates with other AI systems, within Belron's enterprise estate — covering the AI Damage Assessment PoC, Contact Centre of the Future, MCP Governance, and successor projects.

**Out of scope:** model selection criteria, prompt engineering practice, end-user UX patterns, individual SaaS configuration. These are project-level concerns.

## A.3 Drivers

| Driver | Source |
|---|---|
| **D1.** MCP has become an industry standard (97M+ installs; Linux Foundation / Agentic AI Foundation governance) | Anthropic donation announcement; LF AAIF charter |
| **D2.** Heterogeneous agent fleet is inevitable (Copilot Studio + Bedrock + Vertex + LangGraph all in play) | Vendor strategy across Microsoft, AWS, Google, Anthropic |
| **D3.** EU AI Act Articles 9/12/14 require risk management, immutable audit, and human oversight for high-risk AI | EUR-Lex EU AI Act |
| **D4.** Belron IPO (H2 2026) raises the bar on auditability, control evidence, and vendor concentration risk | Belron exec |
| **D5.** Without a semantic layer, ~60% of agentic projects relying solely on the protocol are forecast to fail by 2028 | Industry analyst (Garcia-Rodeja); Atlan, Fluree reporting |

## A.4 Stakeholders & Concerns

| Stakeholder | Primary concern | View(s) addressed |
|---|---|---|
| CIO / Exec | Vendor-agnostic, governable, IPO-defensible | Architecture Vision, Governance |
| EA Council | Conformance, reuse, building-block re-use | Application, Data, ABB catalogue |
| CISO | Identity, audit, prompt injection, data egress | Security view, Triple-Gate pattern |
| DPO / Legal | EU AI Act, GDPR, data residency, retention | Data view, Audit view |
| Integration Platform Team | MuleSoft/SnapLogic role; reuse of existing connectors | Application, Technology view |
| Project teams (AIDA, Contact Centre) | Conformance cost; speed of delivery | Reference patterns; SBB catalogue |
| BA team | Capability alignment; business glossary | Business view |

## A.5 Architecture Principles

Numbered for cross-reference from project Architecture Compliance Reviews.

| # | Principle | Rationale | Implication |
|---|---|---|---|
| **AP-01** | **MCP is the only sanctioned tool-exposure protocol** | Industry standard; Linux Foundation governed; vendor-neutral | No bespoke agent-tool integrations. Existing APIs are wrapped, not displaced |
| **AP-02** | **A2A is the only sanctioned agent-coordination protocol** | Google-originated, 50+ partner ecosystem; open standard | Multi-agent workflows use A2A endpoints, not ad-hoc messaging |
| **AP-03** | **All agent-to-tool traffic transits a Belron-controlled gateway** | Single point of policy enforcement, audit, DLP | No agent connects directly to an MCP server, even SaaS-native ones |
| **AP-04** | **MCP servers are organised by business capability, not source system** | DDD bounded contexts; resilient to source-system change | Tool catalogue mirrors business glossary, not the org chart |
| **AP-05** | **Semantic meaning of tool data is governed centrally** | Without shared meaning, agents misinterpret identical fields | Ontology + semantic layer is a peer concern to MCP itself |
| **AP-06** | **Identity flows end-to-end via enterprise IdP** | Human + agent identity must be traceable to a person | OAuth 2.1 + PKCE; no shared service accounts for agent fleets |
| **AP-07** | **Irreversible actions require a Human-in-the-Loop checkpoint** | EU AI Act Article 14; commercial accountability | Tool calls marked `irreversible: true` block until human confirmation |
| **AP-08** | **Every tool call is logged immutably** | EU AI Act Article 12; IPO audit evidence | Append-only storage with WORM properties; 7-year retention |
| **AP-09** | **Hyperscaler MCP runtimes are used for hyperscaler-native workloads only** | Avoid lock-in at the governance layer | Hyperscaler-native MCP servers register with the central gateway; gateway is never hyperscaler-native |
| **AP-10** | **The reference architecture is provider-portable** | The protocol is the standard; products are replaceable | Every ABB names an interface; SBBs are interchangeable |

---

# Phase B — Business Architecture

## B.1 Business Capability Alignment

Agent-led automation does not introduce new capabilities — it provides a new *execution mechanism* for existing capabilities. Each MCP server family is bound to one or more business capabilities owned by an accountable Belron BU.

| Business Capability (BA-owned) | MCP Server Family | Source-of-Record | Owning BU |
|---|---|---|---|
| Customer Management | `customer-mcp` | Salesforce CRM | Customer Experience |
| Vehicle & Glass | `vehicle-mcp` | Internal product master | Technical Operations |
| Job Scheduling & Dispatch | `scheduling-mcp` | ServiceNow Field Service | Operations |
| Claims & Insurance | `claims-mcp` | Salesforce + insurer APIs | Claims |
| Workforce | `workforce-mcp` | Workday | People |
| Finance | `finance-mcp` | Oracle Fusion ERP | Finance |
| IT Service Management | `itsm-mcp` | ServiceNow ITSM | IT |
| Knowledge & Policy | `knowledge-mcp` | SharePoint / M365 | Various (owner-tagged) |

Full mapping rationale and tool-naming conventions are in [[2026-05-06-mcp-strategy-belron#Section 4]].

## B.2 Business Actors

Three actor classes are recognised:

- **Human Actor** — a Belron employee or contractor, identified via Entra ID
- **Agent Actor** — an autonomous or semi-autonomous AI system, registered with the gateway, with a named owner and capability description
- **External Actor** — a customer-facing agent (e.g., Contact Centre voice agent); must satisfy Transparency requirements (AP-07 + EU AI Act Art. 13)

Agent Actors are *first-class* in the business architecture — they appear on capability maps with accountability owners, just like teams do.

## B.3 Business Services Exposed via MCP

A business service is a unit of value the business chooses to offer; an MCP tool is the machine-callable surface of that service. Not every service should be exposed.

Decision filter: a business service may be exposed as an MCP tool only if it has (a) a clear owner, (b) a defined risk classification, and (c) a documented business glossary entry for every parameter and return field.

## B.4 Value Streams Touched

Agents are most relevant in these Belron value streams (initial scoping):

1. **Customer → Repair** (booking, dispatch, calibration, claims)
2. **Incident → Resolution** (IT ITSM)
3. **Hire-to-Retire** (recruitment, onboarding, skills) — *deferred pending Workday MCP*
4. **Plan-to-Report** (finance, FP&A) — *Phase 2*

---

# Phase C — Information Systems Architecture

## C.1 Data Architecture

### C.1.1 Layered Data Model

```
┌───────────────────────────────────────────────────────────────┐
│  L0  Source-of-record systems (Salesforce, ServiceNow, etc.) │
├───────────────────────────────────────────────────────────────┤
│  L1  Integration / canonical data (MuleSoft, SnapLogic)      │
├───────────────────────────────────────────────────────────────┤
│  L2  Semantic Layer (governed metrics + business glossary)   │
│      — Open Semantic Interchange (OSI) v1.0 compliant        │
├───────────────────────────────────────────────────────────────┤
│  L3  Enterprise Ontology (OWL/RDF)                           │
│      — "what things ARE" — typed entities, relationships      │
├───────────────────────────────────────────────────────────────┤
│  L4  Knowledge / Context Graph (instance data)               │
│      — provenance via named graphs; ArchiMate 3.2 → RDF      │
├───────────────────────────────────────────────────────────────┤
│  L5  MCP Tool Response Surface (the protocol "pipe")         │
└───────────────────────────────────────────────────────────────┘
```

**The key insight (AP-05):** MCP is the pipe, not the water. Without L2/L3 the same field name returned by two MCP servers can mean different things to two agents, with no error raised.

### C.1.2 Data Classification (ArchiMate `business object` attribute)

Every data object surfaced through MCP carries a classification label that the gateway uses for policy decisions:

| Class | Examples | Gateway treatment |
|---|---|---|
| `public` | Glass spec sheets, FAQ content | No restriction |
| `internal` | Branch capacity, technician rosters | Belron-authenticated agents only |
| `confidential` | Customer contact, repair history | Tool-level RBAC + tenant region check |
| `restricted` | Payment data, employee PII, claims financials | DLP redaction by default; explicit policy to unredact |

### C.1.3 Data Residency

EU-classified data objects may only transit gateway instances physically hosted in EU regions. The gateway enforces this via a routing policy keyed on the `data-residency` tag of the calling tool and the geography of the origin agent.

### C.1.4 Audit Data

Every gateway transaction generates an immutable audit record with the following minimum fields. This is the EU AI Act Article 12 obligation.

```
audit_record {
  request_id, parent_trace_id (W3C TraceContext),
  caller_identity { user_id, agent_id, tenant },
  tool { server, name, version },
  arguments_hash, response_hash, response_classification,
  decision { policy_id, decision, reason },
  timestamp_utc, gateway_instance, region,
  hitl_event? { reviewer_id, decision, justification }
}
```

Storage: append-only WORM (AWS S3 Object Lock or Azure Immutable Blob). Retention: 7 years (IPO + regulator default).

## C.2 Application Architecture

### C.2.1 Application Layer Stack (ArchiMate view)

```
┌─────────────────────────────────────────────────────────────────┐
│  Experience Layer  — Channels (Voice, Chat, Web, Mobile, Email) │
├─────────────────────────────────────────────────────────────────┤
│  Agent Layer       — Agent Actors (LangGraph, Copilot Studio,   │
│                       Bedrock, Vertex ADK, Custom)               │
│                       + A2A Coordination Plane                  │
├─────────────────────────────────────────────────────────────────┤
│  Control Plane     — MCP Gateway (Identity · Access · Audit ·   │
│                       Data) + Tool Registry + Agent Registry    │
├─────────────────────────────────────────────────────────────────┤
│  MCP Server Layer  — Domain MCP Server Families                 │
│                       (customer-mcp, vehicle-mcp, ...)          │
├─────────────────────────────────────────────────────────────────┤
│  Integration Layer — MuleSoft Anypoint · SnapLogic APIM         │
├─────────────────────────────────────────────────────────────────┤
│  Source Systems    — Salesforce · ServiceNow · Workday ·        │
│                       Oracle Fusion · M365 · Legacy             │
└─────────────────────────────────────────────────────────────────┘
                  ⇕ (transversal)
       Semantic & Knowledge Plane (L2–L4)
       Observability & Telemetry Plane (OpenTelemetry)
       Security & Identity Plane (Entra ID, OAuth 2.1+PKCE)
```

### C.2.2 Canonical Application Components

ArchiMate notation: `[A]` = Application Component, `[AS]` = Application Service, `[AI]` = Application Interface.

#### Agent Layer

- **[A] Agent Runtime** — hosts one Agent Actor. Implementations: LangGraph runtime, Copilot Studio Agent, Bedrock AgentCore Agent, Vertex ADK Agent. All conform to `[AI] AgentRegistrationInterface` and `[AI] A2AEndpoint`.
- **[A] Agent Memory Store** — short-term (working context) + long-term (vector DB or graph) memory. Per the agentic taxonomy: retrieval, structure, retention policies are mandatory subcomponents.
- **[AS] Reasoning Service** — planning + reflection. Abstracted from model provider via the Provider Adapter (see C.2.4).
- **[AS] Agent Coordination Service** — A2A delegation, task handoff, registry lookup. Owns the Agent Card (well-known URL).

#### Control Plane (MCP Gateway)

The four-layer governance model is canonical:

| Sub-component | Responsibility |
|---|---|
| **[A] Identity Broker** | OAuth 2.1 + PKCE; Dynamic Client Registration; token brokering between agents and downstream systems; binds enterprise IdP identity to agent identity |
| **[A] Tool Registry** | Authoritative catalogue of MCP servers and their tools; cryptographic signing of tool descriptions (CIS MCP Security Guide); curation workflow |
| **[A] Agent Registry** | Authoritative catalogue of registered agents; capability descriptions; A2A endpoint addresses |
| **[A] Policy Engine** | ABAC; consumes (agent identity ⊕ human identity ⊕ tool sensitivity ⊕ data classification ⊕ region) → allow/deny/HITL |
| **[A] DLP & Injection Scanner** | Scans tool *call parameters* (outbound) and tool *responses* (inbound); detects prompt-injection patterns (MCPTox baseline) and PII patterns |
| **[A] Audit Logger** | Writes immutable audit records; integrates with [AS] Telemetry Service |
| **[A] HITL Service** | Pauses tool execution where policy flags HITL required; routes approval request to a named human via Teams/Slack/email; records decision in audit |
| **[A] Code Mode Optimiser** *(optional)* | Compresses tool descriptions into executable code paths to reduce token cost on high-volume tool calls |
| **[AS] Federation Service** | Cross-instance tool/agent discovery between regional gateway instances; only personal-data-free metadata leaves region |

#### MCP Server Layer

- **[A] Domain MCP Server** — exposes a coherent bundle of tools, resources, and prompts for one business capability. Naming, taxonomy, and conventions per [[2026-05-06-mcp-strategy-belron#Section 4]].
- **[A] Virtual MCP Server (Adapter)** — gateway-resident adapter that exposes a non-MCP endpoint as a virtual MCP server. Used for legacy systems where modification is not possible.
- **[A] Sidecar MCP Server** — Kubernetes sidecar pattern; proxies MCP calls to a co-located legacy application. Used for containerised legacy.

Each Domain MCP Server exposes three MCP primitives:

| Primitive | Purpose | Belron design rule |
|---|---|---|
| **Tools** | Imperative, model-callable actions | One tool per user-intent; smallest schema; explicit `irreversible` flag |
| **Resources** | Read-only contextual data the agent can retrieve | Always classified; never returns `restricted` without explicit policy |
| **Prompts** | Server-curated prompt templates for common operations | Versioned; reviewed by capability owner |

### C.2.3 MCP Server / Tool Design Patterns (mandatory)

Compiled from arcade.dev's 54-pattern catalogue and Anthropic guidance. These are conformance requirements for any new MCP server built for Belron.

| Pattern | Statement |
|---|---|
| **P1. Context Injection** | User identity, permissions, and credentials are passed server-side via the gateway, never as tool parameters the LLM can see or modify |
| **P2. Idempotent Operation** | Every write tool accepts a client-supplied `idempotency_key`; duplicate calls return the original result |
| **P3. Async Job** | Operations >5s return a job ID; agents poll via `get_job_status`; never block the agent loop |
| **P4. Error-Guided Recovery** | Errors return a structured `recovery_hint` (e.g., "rate-limited; retry after 30s with batch ≤50") |
| **P5. Parameter Coercion** | Tools accept multiple input forms (ISO dates, natural-language dates) and normalise internally |
| **P6. Smallest-Schema** | Tool inputs and outputs are minimised to the necessary fields; no "kitchen-sink" payloads |
| **P7. Capability-Bound Naming** | Tool names use the business glossary (`get_customer_repair_history`), not technical jargon (`sf_account_query`) |
| **P8. Classification on Response** | Every response field carries a classification (or inherits the tool's default) |
| **P9. Irreversibility Flag** | Tools whose effects cannot be undone declare `irreversible: true` in tool metadata; gateway policy forces HITL |
| **P10. Composition-Friendly Shapes** | Tool outputs are shaped so the natural next-tool input is the previous tool's output |

### C.2.4 Provider Abstraction

Because the model market is volatile and Belron's primary AI advocacy goal is Anthropic/Claude alignment, an explicit **Provider Adapter** ABB is mandated:

- **[A] Provider Adapter** — translates a model-agnostic Reasoning request into provider-specific calls (Anthropic Messages API, Bedrock Converse, Azure OpenAI, Vertex Gemini). All agent runtimes call this adapter, not the provider SDK directly.
- *Rationale:* preserves optionality to swap providers without rewriting agents; isolates the Anthropic-preferred path without enforcing it everywhere.

---

# Phase D — Technology Architecture

## D.1 Technology Layer Stack (ArchiMate view)

ArchiMate notation: `[N]` = Node, `[TS]` = Technology Service, `[SS]` = System Software.

```
┌──────────────────────────────────────────────────────────────────┐
│  [N] Multi-Region Compute  (AWS · Azure · GCP · on-prem K8s)    │
├──────────────────────────────────────────────────────────────────┤
│  [SS] Container Platform   (Kubernetes / EKS / AKS / GKE)        │
├──────────────────────────────────────────────────────────────────┤
│  [SS] Service Mesh        (Istio or equivalent — mTLS)           │
├──────────────────────────────────────────────────────────────────┤
│  [SS] Gateway Runtime     (IBM ContextForge — Apache 2.0)        │
├──────────────────────────────────────────────────────────────────┤
│  [TS] Identity            (Entra ID + OAuth 2.1 + PKCE)          │
│  [TS] Secrets             (Azure Key Vault / AWS KMS / HashiCorp)│
│  [TS] Telemetry           (OpenTelemetry → Dynatrace + Elastic)  │
│  [TS] Audit Storage       (S3 Object Lock / Azure Immutable Blob)│
│  [TS] Vector Store        (per-agent memory; product TBD)        │
│  [TS] Knowledge Graph     (Stardog or Neo4j; OWL/RDF)            │
│  [TS] Semantic Layer      (Cube or dbt Semantic Layer + OSI 1.0) │
└──────────────────────────────────────────────────────────────────┘
```

## D.2 Technology Component Selection

| Layer | Primary | Alternative / Notes |
|---|---|---|
| Gateway Runtime | **IBM ContextForge** (Apache 2.0, self-hosted) | Cloudflare AI Gateway (selective; Code Mode benefit, vendor risk) |
| Integration Backbone | **MuleSoft Anypoint** (MCP Connector 1.4) + **SnapLogic APIM 3.0** | Existing investment; native MCP support |
| Identity | **Entra ID** (Belron house IdP) | OAuth 2.1 + PKCE mandatory per MCP June 2025 spec |
| Secrets | **Azure Key Vault** (Belron-standard) | AWS KMS for AWS-native MCP servers |
| Observability | **OpenTelemetry → Dynatrace + Elastic** (existing stack) | OTel is the protocol; backends are commodity |
| Audit Storage | **Azure Immutable Blob** (EU regions) + **S3 Object Lock** (US) | Region-aligned with data residency |
| Knowledge Graph | **Stardog** (commercial, OWL+SHACL) or **Neo4j** | TBD via PoC |
| Semantic Layer | **Cube** or **dbt Semantic Layer**; OSI v1.0 compliant | OSI portability is the principle, not the product |
| Vector Memory | **TBD per PoC** (Pinecone, pgvector, OpenSearch) | Per-agent; no single corporate store |
| Agent Frameworks (allowed) | **LangGraph**, **Copilot Studio**, **Bedrock AgentCore**, **Vertex ADK**, **Semantic Kernel** | All must register via [AI] AgentRegistrationInterface |

## D.3 Deployment Topology

Four reference deployment patterns (full pattern logic in [[2026-05-06-mcp-strategy-belron#Section 1]]):

| Pattern | When to use |
|---|---|
| **DT-1. Centralised Gateway** | Default for all new agentic projects in 2026 |
| **DT-2. Federated Gateway** | Cross-region in 2027+; one instance per EU / US / APAC; cross-discovery for non-personal-data tools |
| **DT-3. K8s Sidecar** | Legacy containerised systems where API modification is forbidden |
| **DT-4. Hybrid** | The target end-state — Centralised gateway + Sidecars for legacy; federated when residency triggers |

---

# Reference Patterns Catalogue

Patterns are reusable, named architectural responses to recurring problems. Project Architecture Compliance Reviews check that the chosen pattern is named explicitly.

### RP-01 Triple-Gate Security
Three enforcement points: (1) Client→LLM (identity + prompt filtering); (2) LLM→Gateway (auth + tool authorisation + outbound DLP); (3) Gateway→External (downstream credential substitution + inbound DLP + circuit breakers). Missing any gate is a control gap.

### RP-02 Capability-Aligned Server Family
MCP servers organised by business capability bounded context, not by source system. Server families are named to the business glossary.

### RP-03 Integration-Layer Wrap (Legacy)
A legacy system is exposed as MCP via a MuleSoft/SnapLogic flow that becomes the MCP tool implementation. Legacy code is untouched. Authentication is bridged in the gateway's credential vault.

### RP-04 A2A + MCP Orthogonal Composition
A2A coordinates *between* agents (Agent Card discovery, task delegation). MCP connects an agent *to tools*. Both layers are present in every multi-agent workflow; neither replaces the other.

### RP-05 Heterogeneous Agent Fleet
The architecture assumes no single agent framework wins. All agents — Copilot Studio, Bedrock, Vertex, LangGraph, custom — register through the same Agent Registry, call tools through the same Gateway, and coordinate via A2A.

### RP-06 Provider-Abstracted Reasoning
Agent runtimes call a Provider Adapter, not a model SDK directly. Provider selection is a configuration concern, not a code concern.

### RP-07 Semantic-Backed Tool
A tool response is generated by composing data from L0 (source) with definitions from L2 (semantic) and types from L3 (ontology). The agent receives meaning, not raw rows. The OSI v1.0 metric definition travels with the response.

### RP-08 HITL Gate on Irreversibility
Any tool flagged `irreversible: true` is intercepted by the Gateway HITL Service before execution. Human approver named per tool family. Decision is part of the audit record.

### RP-09 Code Mode for High-Volume Tools
For high-frequency tool families (e.g., Contact Centre routing), the gateway uses Code Mode to compress tool descriptions into executable code paths, reducing LLM token consumption. Selective use; not a default.

### RP-10 Shadow MCP Detection
Gateway scans egress traffic for unauthorised MCP traffic patterns (hostname `mcp.*`, paths `/mcp`, `/sse`, JSON-RPC method signatures) and blocks/alerts. Prevents project teams from bypassing the gateway.

---

# Architecture Building Blocks (ABBs)

ABBs are notation-defined, vendor-neutral. Every ABB has at least one implementing SBB; ABBs are the conformance unit.

| ID | ABB | Responsibility | Conforming Interface(s) |
|---|---|---|---|
| ABB-01 | Agent Runtime | Hosts an Agent Actor | `AgentRegistrationInterface`, `A2AEndpoint` |
| ABB-02 | Provider Adapter | Model-agnostic reasoning | `ReasoningRequest` |
| ABB-03 | Agent Memory Store | Short + long-term memory | `MemoryReadWrite` |
| ABB-04 | Agent Registry | Catalogue of registered agents | `AgentRegistrationInterface` |
| ABB-05 | Tool Registry | Catalogue of MCP servers + tools | `MCPServerRegistrationInterface` |
| ABB-06 | Identity Broker | OAuth, DCR, token brokering | `OAuth2.1+PKCE` |
| ABB-07 | Policy Engine | ABAC decisions | `PolicyDecisionInterface` |
| ABB-08 | DLP & Injection Scanner | Outbound / inbound scanning | `ScanRequest` |
| ABB-09 | HITL Service | Human approval orchestration | `ApprovalRequest` |
| ABB-10 | Audit Logger | Immutable audit emission | `AuditRecord` (W3C-traced) |
| ABB-11 | Federation Service | Cross-region discovery | `FederationDiscovery` |
| ABB-12 | Code Mode Optimiser | Token-cost optimisation | `CompiledToolPath` |
| ABB-13 | Domain MCP Server | Business-capability tool bundle | MCP spec primitives (tools/resources/prompts) |
| ABB-14 | Virtual MCP Server (Adapter) | Wraps non-MCP endpoint | MCP spec + adapter config |
| ABB-15 | Sidecar MCP Server | Co-located legacy proxy | MCP spec + K8s sidecar |
| ABB-16 | Semantic Layer Service | Governed metrics + glossary | OSI v1.0 |
| ABB-17 | Enterprise Ontology Service | OWL/RDF typed entities | SPARQL |
| ABB-18 | Knowledge Graph Store | Instance data + provenance | SPARQL / Cypher |
| ABB-19 | Observability Plane | OTel collector + backends | OpenTelemetry |
| ABB-20 | Audit Storage | Immutable retention | WORM (S3 Object Lock / Azure Immutable Blob) |

---

# Solution Building Blocks — Belron Instantiation

SBBs are concrete products selected for Belron. They satisfy ABBs and are interchangeable.

| ABB | SBB (Belron) | Status |
|---|---|---|
| ABB-01 Agent Runtime | LangGraph (custom) · Copilot Studio · Bedrock AgentCore · Vertex ADK | Multi-vendor by design |
| ABB-02 Provider Adapter | Custom (Belron-built) wrapping Anthropic, Azure OpenAI, Bedrock, Vertex | To be built |
| ABB-04+05+06+07+08+09+10+11+12 (Gateway) | **IBM ContextForge** | To deploy (Action 1) |
| ABB-13 Domain MCP Server | ServiceNow native MCP · Salesforce Agentforce · MuleSoft MCP Connector · SnapLogic APIM 3.0 | Mixed maturity (see strategy doc §6) |
| ABB-14 Virtual MCP Server | ContextForge adapter framework | Available |
| ABB-15 Sidecar MCP Server | Custom K8s sidecar | Build per legacy |
| ABB-16 Semantic Layer | Cube **or** dbt Semantic Layer — PoC | Decision pending |
| ABB-17 Ontology Service | Stardog **or** Neo4j — PoC | Decision pending |
| ABB-19 Observability | Dynatrace + Elastic (existing) | In place |
| ABB-20 Audit Storage | Azure Immutable Blob (EU) + S3 Object Lock (US) | To configure |

---

# Standards Information Base

External standards and specifications that are conformance obligations under this RA.

| Standard | Version | Source | Conformance |
|---|---|---|---|
| Model Context Protocol | June 2025 spec | modelcontextprotocol.io | Mandatory |
| Agent2Agent (A2A) | v0.3+ | a2aproject GitHub | Mandatory for multi-agent |
| OAuth 2.1 + PKCE | RFC | IETF | Mandatory |
| W3C TraceContext | W3C Rec | w3.org | Mandatory for audit correlation |
| OpenTelemetry | 1.x | opentelemetry.io | Mandatory for traces/metrics/logs |
| Open Semantic Interchange | v1.0 (Jan 2026) | OSI Initiative | Required for L2 |
| OWL 2 / RDF 1.1 / SPARQL 1.1 | W3C Rec | w3.org | Required for L3/L4 |
| ArchiMate | 3.2 | The Open Group | EA notation; convertible to RDF for L3 population |
| CIS MCP Security Guide | April 2026 | cisecurity.org | Required security baseline |
| EU AI Act | as enacted | eur-lex.europa.eu | Mandatory in EU operations |
| GDPR | as enacted | EUR-Lex | Mandatory in EU operations |

---

# Security Architecture (transversal view)

## SA.1 Identity Plane

- Single enterprise IdP (Entra ID) is authoritative
- Every human and every agent has a distinct identity
- No shared service accounts for agent fleets
- Agent identity is created at registration; bound to a named human owner
- Token lifetime: short (≤1h); refresh via Identity Broker

## SA.2 Threat Model (resident in gateway design)

| Threat | Control |
|---|---|
| Prompt injection via tool response content | RP-01 Triple-Gate (Gate 3 inbound scan); MCPTox-pattern detection |
| Tool registration tampering | Cryptographically signed tool descriptions (CIS) |
| Shadow MCP (project bypass) | RP-10 Shadow MCP Detection at egress |
| Agent identity spoofing | Mutual TLS in service mesh; signed registration |
| Excessive data egress | Outbound DLP at Gate 2; classification-driven policy |
| Runaway agent loop | Per-agent rate limits at Gateway; anomaly alerts |
| Credential leakage to LLM | Context Injection (P1) — credentials never enter LLM context |
| Audit log tampering | WORM storage; cryptographic chain of records |

## SA.3 EU AI Act Mapping

| Article | Obligation | Architectural element |
|---|---|---|
| Art. 9 — Risk Management | Documented risk register per high-risk system | Agent registration includes risk classification |
| Art. 12 — Logging | Lifetime automatic logging | ABB-10 + ABB-20 |
| Art. 13 — Transparency | User informed of AI interaction | RP-04 + UX obligation on customer-facing channels |
| Art. 14 — Human Oversight | Effective human oversight | RP-08 HITL Gate + Irreversibility flag (P9) |

---

# Governance Framework

## G.1 Decision Rights

| Decision | Owner | Consulted |
|---|---|---|
| New ABB introduced | EA Council | CISO, DPO, Integration Lead |
| New SBB selected for an existing ABB | EA + relevant Platform team | EA Council (notification) |
| New MCP server family created | EA + Capability owner BA | DPO, CISO |
| New tool added to an existing server | Capability owner | EA (notification if classification ≥ confidential) |
| Tool flagged `irreversible` | Capability owner | CISO, named HITL approver |
| Cross-region federation enabled | EA + DPO | CISO |

## G.2 Architecture Compliance Review (ACR)

A new agentic project completes an ACR before production. The ACR template checks conformance against:

1. Architecture Principles AP-01 through AP-10
2. Pattern selection (named, not invented)
3. ABB conformance (which ABBs are touched; which are new)
4. Security architecture (SA.1–SA.3)
5. EU AI Act risk class declared
6. Audit and observability wiring confirmed
7. Capability owner named

## G.3 Standards Currency

Owner: EA. The Standards Information Base is reviewed at every quarterly EA Council and on any of:
- MCP spec version change
- A2A version change
- EU AI Act enforcement-related guidance
- Anthropic / Linux Foundation governance change

---

# Views & Viewpoints

This document presents the following viewpoints (TOGAF/ArchiMate terminology):

| Viewpoint | Stakeholder primarily addressed | Section |
|---|---|---|
| Architecture Vision | CIO, Exec | Phase A |
| Stakeholder | All | A.4 |
| Principles | EA Council | A.5 |
| Business Capability Map | BA team, CIO | B.1 |
| Business Service | Capability owners | B.3 |
| Data Layered | DPO, Data team | C.1 |
| Application Co-operation | Integration, Platform | C.2.1 |
| Application Component | Project teams | C.2.2 |
| Technology Stack | Platform, Ops | D.1 |
| Deployment | Platform | D.3 |
| Pattern | Project Architects | Patterns catalogue |
| Implementation & Migration | Programme | (deferred to companion strategy doc Section 9) |
| Security | CISO | SA.* |
| Compliance (EU AI Act) | DPO, Legal | SA.3 |
| Governance | EA Council | G.* |

---

# Open Issues / Architecturally Significant Decisions Pending

| ID | Issue | Decision needed by | Owner |
|---|---|---|---|
| OI-01 | Knowledge Graph product (Stardog vs Neo4j) | Q3 2026 | EA + Data |
| OI-02 | Semantic Layer product (Cube vs dbt) | Q3 2026 | EA + Data |
| OI-03 | Vector Memory standardisation — per-agent vs shared | Q3 2026 | EA |
| OI-04 | Workday MCP path — MuleSoft bridge confirmed; official path pending Workday roadmap | Watch | EA |
| OI-05 | Code Mode adoption criteria — which workloads warrant the Cloudflare dependency | Q4 2026 | EA + CISO |
| OI-06 | Provider Adapter — build vs adopt (e.g., LiteLLM as SBB) | Q3 2026 | EA |
| OI-07 | A2A version stability — GA timing on Microsoft side affects Copilot Studio agent participation | Watch | EA |
| OI-08 | ContextForge production support model — open-source self-support vs SI engagement | Q3 2026 | EA + Procurement |
| OI-09 | Boundary between MCP Governance project and Semantic Governance — separate initiative or one body of work | Q2 2026 | EA |
| OI-10 | ArchiMate-to-RDF conversion — adopt the published pattern, or model ontology natively | Q4 2026 | EA + BA |

---

# Sources

Synthesised from the following web sources (May 2026 research pass) plus the companion strategy document [[2026-05-06-mcp-strategy-belron]].

1. [Cloudflare — Scaling MCP adoption: reference architecture](https://blog.cloudflare.com/enterprise-mcp/)
2. [InfoQ — Cloudflare Outlines MCP Architecture as Enterprises Confront Security and Governance Risks](https://www.infoq.com/news/2026/04/cloudflare-mcp/)
3. [Obot.ai — MCP Enterprise Architecture Reference Guide](https://obot.ai/blog/mcp-enterprise-architecture-reference-guide/)
4. [Arcade.dev — 54 Patterns for Building Better MCP Tools](https://www.arcade.dev/blog/mcp-tool-patterns/)
5. [arXiv — Agentic AI Architectures, Taxonomies, and Evaluation (2601.12560)](https://arxiv.org/html/2601.12560v1)
6. [arXiv — Simplified and Secure MCP Gateways for Enterprise AI Integration (2504.19997)](https://arxiv.org/pdf/2504.19997) *(fetched as PDF; reference only)*
7. [Atlan — Ontology vs Semantic Layer](https://atlan.com/know/ontology-vs-semantic-layer/)
8. [Fluree — How to Build a Semantic Layer for Enterprise AI](https://flur.ee/fluree-blog/how-to-build-a-semantic-layer-for-enterprise-ai/)
9. [Linked Data Orchestration — Context Graph Architecture](https://linkeddataorchestration.com/2026/05/08/context-graph-architecture-knowledge/)
10. [Anthropic — Donating MCP and establishing the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
11. [IBM — Powering autonomous IT operations: agentic AI-ready IBM infrastructure](https://www.ibm.com/new/product-blog/powering-the-future-of-autonomous-it-operations-agentic-ai-ready-ibm-infrastructure)
12. [Prateek Sharma — MCP Is the New API: What MCP Means for Enterprise Architecture](https://www.prateek-sharma.com/blog/mcp-model-context-protocol-enterprise-architecture/)
13. [ByteBridge — MCP and the MCP Gateway: Concepts, Architecture, Case Studies](https://bytebridge.medium.com/model-context-protocol-mcp-and-the-mcp-gateway-concepts-architecture-and-case-studies-3470b6d549a1)
14. [Tedt.org — MCP's 2026 Roadmap](https://tedt.org/MCPs-2026-Roadmap/)
15. [Knowlee — AI Agent Platform Architecture 2026: Reference Patterns + Layer Decomposition](https://www.knowlee.ai/blog/ai-agent-platform-architecture-2026)

---

*v0.1 working draft — 2026-05-22. Pair with [[2026-05-06-mcp-strategy-belron]] for the adoption plan.*
