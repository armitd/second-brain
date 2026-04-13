---
type: strategic-research
domain: enterprise-architecture
date: 2026-04-13
question: "What does a Belron EA need to know to become an expert in the Salesforce ecosystem — Sales Cloud, Marketing Cloud, Field Service, and Agentforce?"
threads:
  - platform-architecture
  - sales-cloud
  - marketing-cloud
  - field-service
  - agentforce-data-cloud-mulesoft
confidence: HIGH
tags:
  - auto-research
  - strategy
  - salesforce
  - enterprise-architecture
  - agentforce
  - field-service
  - marketing-cloud
status: complete
---

# Salesforce Ecosystem: Enterprise Architect's Deep Dive

## Executive Summary

Salesforce is no longer a CRM — it is an enterprise platform undergoing its most significant transformation since its founding. In 2025–2026, Salesforce rebranded all its products under the "Agentforce" umbrella and placed autonomous AI agents at the centre of every business process. The underlying architecture has four layers — Data (Data Cloud/360), Applications (the individual clouds), AI Models (Einstein/Atlas), and Agents (Agentforce) — and every architectural decision must now account for all four.

For a Belron EA, three things matter immediately: (1) the Marketing Cloud landscape is split between a legacy platform (ExactTarget-based) and a new native platform — this is the highest-risk area architecturally; (2) Field Service is the most operationally critical system and has hard performance limits and governance requirements that need EA ownership; (3) Data Cloud is no longer optional — it is the foundation that makes Agentforce work, and without it, any AI deployment on Salesforce is operating blind.

---

## Part 1 — The Salesforce Platform Architecture

### The Four-Layer Stack

Every Salesforce product sits within a coherent four-layer architecture:

```
┌─────────────────────────────────────────────────────┐
│  LAYER 4 — AGENTS                                   │
│  Agentforce (autonomous AI agents per domain)       │
├─────────────────────────────────────────────────────┤
│  LAYER 3 — AI MODELS                                │
│  Atlas Reasoning Engine + Einstein Trust Layer      │
├─────────────────────────────────────────────────────┤
│  LAYER 2 — APPLICATIONS                             │
│  Sales Cloud / Marketing Cloud / Field Service /    │
│  Service Cloud / Commerce Cloud / Industry Clouds   │
├─────────────────────────────────────────────────────┤
│  LAYER 1 — DATA & PLATFORM FOUNDATION               │
│  Data Cloud (Data 360) + Salesforce Core Platform  │
│  Metadata Framework + APIs + Einstein Trust Layer   │
└─────────────────────────────────────────────────────┘
```

The key architectural insight: **all application clouds share the same underlying metadata framework and object model.** This means that when a service case is resolved in Service Cloud, a sales rep can see that history in Sales Cloud — if your data model and sharing rules are configured correctly. The platform is inherently unified; it takes poor configuration to make it siloed.

### The Metadata Framework

Everything in Salesforce is metadata: objects, fields, workflows, page layouts, security settings, code (Apex). This is the source of both its power and its governance complexity.

- Metadata describes schema, processes, security, and behaviour
- The Metadata API retrieves and deploys metadata between environments (dev → staging → prod)
- **Source-control driven development** (Salesforce DX + unlocked packages) is the enterprise standard
- **Change sets** are legacy — if Belron's Salesforce team still uses them, this is the single highest-priority technical improvement to recommend

### The 2025 Rebrand: What Changed in Name, What Changed in Substance

| Old Name | New Name | Changed in substance? |
|---|---|---|
| Sales Cloud | Agentforce Sales | No — CRM core unchanged; Agentforce layer added on top |
| Service Cloud | Agentforce Service | No — same architecture |
| Marketing Cloud Engagement | Marketing Cloud Engagement | No — legacy platform unchanged |
| Marketing Cloud Growth | Agentforce Marketing | Yes — new native platform, different architecture |
| Field Service Lightning | Agentforce Field Service | No — FSL core unchanged; Agentforce layer added |
| Data Cloud | Data 360 | No — same product, new name |
| Einstein Copilot | Agentforce | Yes — fully repositioned as autonomous agent platform |

**EA implication:** The naming change is marketing. The architectural change is real for Marketing Cloud (legacy vs native split) and Agentforce (from copilot to autonomous agent). Don't let the rebrand obscure which products have actually changed.

### The Product Portfolio at a Glance

**Core CRM Applications:**
- **Sales Cloud** — pipeline, opportunities, accounts, contacts, forecasting
- **Service Cloud** — case management, omni-channel support, knowledge base, entitlements
- **Field Service** — workforce management, scheduling, dispatch, mobile technicians *(built on top of Service Cloud)*
- **Marketing Cloud** — campaign orchestration, email/SMS/push, journey automation *(two distinct platforms — see Part 3)*
- **Commerce Cloud** — B2B and B2C e-commerce
- **Experience Cloud** — customer/partner portals and self-service sites

**Platform & Integration:**
- **Salesforce Platform** — custom app development (Lightning, Apex, Flow, Heroku)
- **MuleSoft** — enterprise integration platform and API management
- **Slack** — the primary human-agent collaboration interface in Agentforce architecture

**Data & AI:**
- **Data Cloud (Data 360)** — unified customer data platform; the foundation for Agentforce
- **CRM Analytics** — native BI and dashboards
- **Tableau** — enterprise data visualisation (acquired 2019)
- **Agentforce** — autonomous AI agent platform

**Industry Clouds (vertical extensions):**
Financial Services Cloud, Health Cloud, Manufacturing Cloud, Government Cloud, and others — all built on top of the core CRM stack with industry-specific objects, flows, and compliance features.

---

## Part 2 — Sales Cloud: The CRM Foundation

### What Sales Cloud Does

Sales Cloud is Salesforce's original product and the foundation of the entire ecosystem. It manages the full sales lifecycle:

**Core objects and what they hold:**
| Object | Purpose |
|---|---|
| **Lead** | Unqualified prospect — name, company, source. Converted to Account/Contact/Opportunity when qualified |
| **Account** | A company or organisation. The anchor object — almost everything relates to an Account |
| **Contact** | A person at an Account |
| **Opportunity** | A potential deal. Has a Stage (pipeline position), Amount, and Close Date |
| **Activity** (Task/Event) | Interactions with contacts and leads — calls, emails, meetings |
| **Quote** | A formal pricing proposal linked to an Opportunity |
| **Contract** | A signed agreement, typically post-sale |

**The pipeline mechanics:** Opportunities move through configurable Stages. Sales forecasting aggregates Opportunities by Stage, owner, and time period. This is where a sales manager gets their "number."

### Key Capabilities

- **Einstein Lead Scoring** — AI-ranks leads by likelihood to convert
- **Agentforce Inbound Lead Gen (2026)** — autonomous agent captures web leads, answers questions, schedules meetings without human intervention
- **Conversation Intelligence** — AI joins sales calls, generates recaps, identifies action items, auto-updates Opportunity stages
- **Sales Performance Management** — quota setting, territory assignment, compensation tracking (requires additional licences)
- **Collaborative Forecasting** — hierarchical forecast roll-up from rep → manager → VP

### What Sales Cloud Does NOT Do Well Natively

- Complex CPQ (Configure Price Quote) — requires **Salesforce CPQ** (now called Revenue Cloud) as a separate product
- E-commerce transactions — that's Commerce Cloud
- Marketing campaign execution — that's Marketing Cloud
- Field technician dispatch — that's Field Service

### EA Governance Considerations for Sales Cloud

1. **Account ownership model** — Who owns an Account record when multiple teams or regions use the same org? This governance decision (account hierarchies, sharing rules, ownership rules) is foundational and hard to change later.
2. **Lead routing** — How do Leads get assigned to reps? Manual, round-robin, or territory-based? Each has different configuration implications.
3. **Opportunity stages** — A poorly defined stage process creates garbage forecast data. EA should influence this definition, not just the IT team.
4. **Master of record** — For customer data, is Salesforce the master or is the ERP (e.g., Oracle EBS) the master? The answer determines the direction and rules of data sync (see MuleSoft section).
5. **Agentforce governance** — When Conversation Intelligence agents auto-update Opportunity stages, who audits that? This is a data quality and audit trail question that EA must address before enablement.

---

## Part 3 — Marketing Cloud: The Split Platform

### The Most Architecturally Complex Part of the Salesforce Estate

Marketing Cloud is not one product. It is two fundamentally different technology stacks that share a brand name. Every Salesforce-experienced person you speak to will have a view on this — it is the source of more architectural grief than any other part of the platform.

### Stack A: Marketing Cloud Engagement (Legacy)

**Origin:** ExactTarget, acquired by Salesforce in 2013. Never fully migrated onto the Salesforce Core platform.

**Architecture characteristics:**
- Runs on its own separate infrastructure — a different data centre, different data model
- Data is stored in **Data Extensions** — essentially custom database tables, not Salesforce objects
- Requires **Marketing Cloud Connect** to synchronise data with Sales/Service Cloud — this creates latency and can create data inconsistencies
- Scripting is done via **AMPscript** and **Server-Side JavaScript** — unique languages not found anywhere else in the Salesforce ecosystem
- Journey orchestration is **Journey Builder** — a visual canvas for mapping customer journeys

**When it's appropriate:**
- High-volume email sending at scale (millions of sends)
- Complex transactional email programmes
- Organisations with established Journey Builder journeys and significant AMPscript investment
- When Marketing Cloud Connect sync latency is acceptable for your use case

**Governance risks:**
- Data lives in a separate system — Marketing has its own customer data that may diverge from Sales Cloud
- AMPscript expertise is specialist and not widely available
- Marketing Cloud Connect sync failures can cause campaigns to run with stale data
- PII governance is harder because data resides in a separate platform

### Stack B: Marketing Cloud Next / Growth (Native)

**Origin:** Built natively on Salesforce Core from scratch; generally available 2024–2025.

**Architecture characteristics:**
- Runs on the same infrastructure as Sales/Service Cloud — no Marketing Cloud Connect needed
- Data is stored as Salesforce objects — same model as the rest of the platform
- Powered by **Data Cloud** for segmentation and personalisation
- Campaign orchestration uses **Salesforce Flow** instead of Journey Builder
- Zero-copy architecture — can query Snowflake, Databricks, BigQuery in real time without data movement

**When it's appropriate:**
- New marketing implementations without legacy Journey Builder investment
- Organisations that want unified data across Sales, Service, and Marketing
- Where Data Cloud is already in use or planned
- Smaller or mid-market volumes initially (enterprise scale validation still maturing)

**2026 Agentic Marketing capabilities (native platform only):**
- **Campaign Designer** — natural language input generates complete multi-channel campaign strategies, copy, segments, and flows for human approval
- **Journey Decisioning** — agents autonomously select next steps and channels based on real-time Data Cloud signals rather than rigid flowcharts
- **Conversational Email** — Agentforce interprets customer replies to marketing broadcasts and responds contextually
- **Paid Media Optimisation** — autonomous agents reallocate ad budgets based on ROI thresholds

### The Migration Question

**The single most important Marketing Cloud decision for Belron EA:**

Belron is likely using **Marketing Cloud Engagement** (legacy) given the scale of operations and the tenure of the implementation. The strategic question is: migrate to Marketing Cloud Next, or stay on Engagement?

| Factor | Engagement (legacy) | Next (native) |
|---|---|---|
| Salesforce's investment direction | Maintenance mode | Active development |
| Agentforce / AI capabilities | Limited | Full |
| Data unification with Sales/Service | Via sync (latency risk) | Native (real-time) |
| Journey orchestration | Journey Builder | Salesforce Flow |
| High-volume sending maturity | Proven at scale | Maturing |
| AMPscript / existing journeys | Protected | Requires rebuild |

**EA recommendation:** Do not force migration. Run **greenfield initiatives on Marketing Cloud Next**, maintain established high-volume campaigns on Engagement. Build toward native incrementally, using Data Cloud as the unification layer. The journey rebuild effort is significant and should be costed honestly.

### Key Marketing Cloud Governance Responsibilities

1. **Consent management** — who owns opt-in/opt-out data and how does it synchronise between Marketing Cloud, Sales Cloud, and any consent management platform?
2. **Data Extension governance (legacy)** — which Data Extensions contain PII? Who can access them? How are they provisioned and decommissioned?
3. **Marketing Cloud Connect sync rules** — what syncs, how frequently, in which direction? This is a performance and data quality governance question.
4. **Journey governance** — who can create and activate Journeys? Uncontrolled Journey creation is a significant risk (duplicated sends, conflicting customer communications).
5. **Agentic guardrails (native)** — as autonomous agents begin to make campaign decisions, circuit breakers (max send frequency, max spend thresholds) must be defined before enablement, not after.

---

## Part 4 — Field Service: The Technician Platform

### Architecture: Built on Service Cloud

Field Service (FSL — Field Service Lightning is the legacy name) is **not a standalone product**. It is a managed package that extends Service Cloud. This means:

- You must have Service Cloud licences before Field Service can run
- Field Service inherits all of Service Cloud's case management, omni-channel, and knowledge capabilities
- Work Orders connect to Cases — a customer complaint (Case) generates a dispatch job (Work Order)

### The Core Data Model

Understanding these objects is essential for governing FSL:

```
Account / Contact
     │
     └── Case (customer complaint or request)
              │
              └── Work Order (what work needs to be done)
                       │
                       └── Work Order Line Items (individual tasks/parts within a job)
                                │
                                └── Service Appointment (when/where the tech goes)
                                         │
                                         ├── Service Resource (the technician)
                                         └── Service Territory (geographic/functional zone)
```

**Supporting governance objects:**
- **Operating Hours** — when services are available (weekdays only, 8am-6pm, etc.)
- **Scheduling Policies** — rules governing how the optimizer assigns jobs (shortest travel, highest skill match, etc.)
- **Work Types** — templates standardising task definitions (e.g., "Windscreen Repair" vs "Windscreen Replace" as distinct Work Types with different duration and skill requirements)
- **Skills** — competencies assigned to technicians; jobs can require specific skills
- **Entitlements** — service level agreements (e.g., "insurer X requires 4-hour response")

### The Dispatcher Console

The operational heart of Field Service. A split-panel interface with:
- **Gantt chart** — visual timeline of technician schedules for the day/week
- **Map view** — geographic view of jobs and technician locations
- **Appointment List** — queue of unscheduled or at-risk appointments

Dispatchers can manually drag-and-drop appointments or invoke the **AI Scheduling Optimizer** to automatically assign all unscheduled jobs against the active Scheduling Policy.

### The Technician Mobile App

Field technicians use the **Field Service Mobile App** (iOS/Android):
- Access Work Orders and Service Appointments
- Receive turn-by-turn navigation to jobs
- Work offline (sync when reconnected) — critical for remote locations
- Capture photos, customer signatures, and service reports
- Access knowledge articles and troubleshooting guides
- **Agentforce (2026):** Pre-work briefs with customer and asset history; step-by-step guided troubleshooting; knowledge retrieval via natural language

### Hard Performance Limits (Govern Against These)

These are architectural constraints that must inform data design:

| Limit | Value | Governance Implication |
|---|---|---|
| Service Resources per Work Order | < 10,000 recommended | Don't create global Work Orders at this scale |
| Service Appointments per Territory per Day | Max 1,000 | Territory design must account for appointment volume |
| Service Resources per Territory | Max 50 | Territory granularity must match technician density |

**EA implication for Belron:** If Belron has hundreds of technicians per region, territory design must be granular enough to stay within the 50-resource-per-territory limit. This is an architectural decision that determines how the entire dispatch operation scales.

### Licensing Model

Field Service has its own licence types on top of Service Cloud:

| Licence | Who it's for |
|---|---|
| Dispatcher | Office-based schedulers who use the Dispatcher Console |
| Technician | Field workers who use the mobile app only |
| Field Service Plus | Full access — dispatchers with mobile capability |

**EA implication:** Licensing decisions at the product/user level are an EA governance responsibility. Overpaying for Field Service Plus licences for workers who only need the mobile app is a common and expensive mistake.

### Deployment Complexity Warning

Field Service is a managed package with **complex relational data** that is difficult to move between environments. This creates deployment challenges:

- Sandbox → Production migrations for scheduling policy changes can take days
- Work Type and Operating Hours configuration changes must be carefully tested
- Scheduling Policy changes can have ripple effects on in-flight Service Appointments

**EA recommendation:** Field Service configuration changes should go through a formal change control process — not the informal "quick update in production" that other Salesforce configuration sometimes gets treated as.

---

## Part 5 — Agentforce, Data Cloud, and MuleSoft

### Data Cloud (Data 360): The Non-Negotiable Foundation

**What it is:** A real-time hyperscale data engine built natively into the Salesforce platform. Processes 30 trillion transactions per month. As of 2026, it is the foundation that makes Agentforce effective.

**The core capability — Unified Customer Profile:**
Data Cloud ingests data from multiple sources, resolves identity (matching records across systems), and creates a single "golden record" for each customer. This uses configurable match and reconciliation rules.

**Zero-copy architecture:** Data Cloud can federate data from external platforms (Snowflake, Databricks, BigQuery, Azure Data Lake) **without physically moving the data**. Using Apache Iceberg as the open table format, it queries data where it lives, in real time. For a GDPR-sensitive company like Belron, this is significant: customer data doesn't need to be copied into Salesforce — it can be read in place, with access controls applied at the source.

**Why it matters for Agentforce:** An Agentforce agent is only as good as the data it can access. Without Data Cloud, an agent sees only the data within a single Salesforce org. With Data Cloud, it sees a unified view of the customer across all systems. Pre-work briefs for technicians, next-best-action recommendations for sales reps, and personalised marketing journeys all require Data Cloud to function at their full potential.

**EA implication:** If Belron doesn't have Data Cloud yet, this should be on the architecture roadmap before significant Agentforce investment. The sequence matters: Data Cloud → Unified Profile → Agentforce capabilities.

### Agentforce: The AI Layer

**What it is:** An autonomous AI agent platform built on top of the Salesforce stack. Not a chatbot. Not a copilot. Agents can execute multi-step workflows, make decisions, and take actions without human intervention.

**The five-component anatomy of an Agentforce agent:**

| Component | What it does |
|---|---|
| **Role** | Defines what the agent is responsible for (e.g., "Handle inbound service requests") |
| **Topics** | Categories of tasks the agent handles (e.g., "Appointment Booking", "Damage Assessment Query") |
| **Instructions** | Natural language rules guiding behaviour within each Topic |
| **Actions** | What the agent can DO — invoke Flows, query Data Cloud, call APIs, delegate to other agents |
| **Guardrails** | What the agent must NEVER do — escalate when uncertain, never share PII, etc. |

**The Atlas Reasoning Engine** is the brain. It receives a user input, determines the appropriate Topic, builds an execution plan using available Actions, executes it, and returns a result. All of this happens within the **Einstein Trust Layer** — which:
- Masks PII before it reaches any external LLM
- Guarantees zero data retention by the LLM provider
- Logs every agent action for audit
- Applies toxicity and bias filters

**Multi-agent architecture patterns:**

Salesforce defines three enterprise deployment patterns:

| Pattern | When to use |
|---|---|
| **SOMA** (Single Org, Multiple Agents) | Most enterprises start here. All agents within one Salesforce org. Shared governance, simpler to operate. |
| **MOMA** (Multi-Org, Multiple Agents) | When different business units have separate orgs. Agents coordinate via the A2A protocol across org boundaries. |
| **Multi-Vendor A2A** | When Salesforce agents need to coordinate with non-Salesforce agents (e.g., an agent built in Azure AI or Google Vertex AI). Uses the A2A standard protocol. |

**The MCP-A2A boundary within Agentforce:**
- Salesforce explicitly supports **MCP** as the protocol for connecting agents to tools, data sources, and external systems
- Salesforce explicitly supports **A2A** as the protocol for agent-to-agent coordination
- This means Belron's Salesforce Agentforce agents can, in principle, participate in the broader enterprise agentic ecosystem governed by these open standards

**Agentforce use cases most relevant to Belron:**

*Customer-facing:*
- **Booking Agent** — customer calls or messages; agent checks technician availability, books appointment, sends confirmation
- **Claims Triage Agent** — customer submits windscreen damage claim via digital channel; agent assesses, qualifies, routes to appropriate insurer workflow
- **Status Update Agent** — customer queries job status; agent retrieves Field Service data and responds

*Technician-facing (via Field Service mobile app):*
- **Pre-Work Brief Agent** — technician opens job; agent surfaces customer history, vehicle details, prior repair notes, and insurer requirements before arrival
- **Troubleshooting Agent** — technician encounters unexpected damage type; agent walks through diagnostic steps using knowledge base
- **Parts Lookup Agent** — technician needs a part; agent queries inventory and ERP data (via MuleSoft/Data Cloud) for availability and alternatives

*Internal/Back-office:*
- **Scheduling Optimisation Agent** — monitors appointment queue and automatically proposes schedule adjustments based on cancellations, traffic, or technician capacity changes
- **Escalation Triage Agent** — monitors high-risk cases (SLA breach risk, insurer-flagged jobs) and proactively alerts dispatchers

### MuleSoft: The Integration Fabric

**What it is:** Salesforce's enterprise integration platform, acquired 2018. Now the integration layer for the entire Agentforce ecosystem, not just Salesforce-to-Salesforce.

**The three-layer API architecture:**

```
┌────────────────────────────────────────────┐
│  EXPERIENCE APIs                           │
│  Tailored for specific consumers:          │
│  mobile app, LLM/agent, partner portal     │
├────────────────────────────────────────────┤
│  PROCESS APIs                              │
│  Business logic + data composition:        │
│  "Create a booking" = check calendar +     │
│  update CRM + notify technician            │
├────────────────────────────────────────────┤
│  SYSTEM APIs                               │
│  Direct connections to source systems:     │
│  Oracle EBS, SAP, legacy databases,        │
│  third-party SaaS                          │
└────────────────────────────────────────────┘
```

**Pre-built connectors include:** Oracle E-Business Suite (EBS), SAP, ServiceNow, Workday, Snowflake, and hundreds of others — directly relevant given the EBS braindump context.

**2026 role — MuleSoft Agent Fabric:** MuleSoft now provides a **central management plane for AI agents** — discovering, governing, orchestrating, and observing all agents regardless of which platform built them. This positions MuleSoft as the enterprise "agent integration layer" alongside its traditional data integration role.

**When to use MuleSoft vs Salesforce Flow:**

| Use case | Tool |
|---|---|
| Data sync between Salesforce and ERP | MuleSoft |
| Automation within Salesforce (e.g., update a field when an Opportunity closes) | Salesforce Flow |
| Complex multi-system orchestration (e.g., booking that touches Salesforce + ERP + technician app) | MuleSoft |
| Simple Salesforce-to-Salesforce integration between two orgs | Salesforce Flow or Platform Events |
| AI agent connecting to an external data source | MCP Server (can be built on MuleSoft) |

---

## Part 6 — EA Governance Framework for the Full Salesforce Estate

### Governance Domain 1: Data Ownership and Master of Record

The most important architectural decision across the entire estate.

| Data Domain | Likely master | Implications |
|---|---|---|
| Customer/Account | Salesforce (Sales Cloud) | ERP customer data should sync FROM Salesforce, not override it |
| Order/Invoice/Financial | ERP (Oracle EBS or equivalent) | Surface in Salesforce for visibility, but ERP owns the record |
| Vehicle/Asset data | Likely operational system | MuleSoft integration to surface in Field Service |
| Technician skills/availability | Field Service | HR system may also hold — needs governance decision |
| Marketing consent/opt-out | Needs a decision | Marketing Cloud, CRM, or dedicated consent platform? |

### Governance Domain 2: Org Strategy

Single org or multiple orgs? This is the highest-leverage architectural decision.

| Consideration | Single Org | Multi-Org |
|---|---|---|
| Data sharing | Easy — same platform | Requires A2A or integration |
| Governance complexity | Higher (one team governs everything) | Lower per-org but harder across orgs |
| Regional autonomy | Difficult — shared metadata | Easier — separate orgs |
| Agentforce | SOMA pattern — simpler | MOMA pattern — more complex |
| Cost | Generally lower | Generally higher |

For a global operator like Belron with multiple national opcos, a **federated model** is common: a central "hub" org for shared capability (Data Cloud, MuleSoft, global processes) with regional or opco-specific orgs for local operations.

### Governance Domain 3: Package Architecture

Based on the braindump context — the EA recommendation stands:
- **Managed packages** = what you buy from AppExchange (configure only, can't modify)
- **Unlocked packages** = what your team builds internally (source-controlled, independently deployable)
- If deploying via change sets: migrate to unlocked packages + Git + CI/CD pipeline. This is the enterprise standard.
- **Governance role:** Own the package architecture diagram — what packages exist, what they contain, their dependencies, and who owns each one.

### Governance Domain 4: Einstein Trust Layer Configuration

Before enabling any Agentforce capability:
- Define PII fields that must be masked before reaching an LLM
- Review the zero-data-retention policy with legal/privacy
- Configure audit logging — where do agent action logs go? Who reviews them?
- Define escalation thresholds — when must an agent hand off to a human?
- Establish circuit breakers for Marketing agents — max send frequency, max budget spend per agent action

### Governance Domain 5: Licensing Oversight

Salesforce licensing is complex and expensive. EA should own a licensing register:

| Cloud | Licence types to track |
|---|---|
| Sales Cloud | Sales rep vs read-only vs partner community |
| Marketing Cloud Engagement | Email/SMS volume, Contacts database size |
| Field Service | Dispatcher vs Technician vs Plus |
| Agentforce | Charged per conversation (not per user) in 2026 |
| Data Cloud | Charged per profile and by data volume |
| MuleSoft | Charged by API call volume and connector count |

**Agentforce pricing shift (2026):** Agentforce is priced per conversation (~$2/conversation), not per user seat. This is a fundamentally different cost model — volume scales linearly, and a single customer-facing bot with 100,000 monthly conversations costs $200,000/year at list price. EA must model usage before enabling.

---

## Scenarios

### Scenario A (Most Likely): Incremental Agentforce Adoption on Existing Stack
Belron extends existing Sales Cloud, Marketing Cloud Engagement, and Field Service with targeted Agentforce use cases. Field Service technician pre-work briefs and internal scheduling optimisation are first (low risk, high value). Customer-facing booking agents and marketing agentic capabilities follow once Data Cloud is established. Migration from Marketing Cloud Engagement to Next is deferred 2–3 years.

### Scenario B (Accelerated): Data Cloud as Transformation Enabler
Belron invests in Data Cloud as the first move, creating a unified customer profile across all opcos and channels. This then unlocks Agentforce at full capability across all three clouds simultaneously. Higher upfront investment but faster realisation of cross-cloud AI benefits (e.g., a technician agent that knows the customer's full insurer claim history before arrival).

### Scenario C (Disruption Risk): Vendor Lock-In Overreach
Belron allows individual opcos to adopt Agentforce point solutions without central EA governance. Agents proliferate across orgs with no shared governance, contradictory guardrails, and disconnected data. Marketing Cloud Engagement and Next both run simultaneously with no migration plan. MuleSoft is not standardised, creating parallel integration paths. This is the "agent sprawl" risk from the daily brief — Kai Waehner's April 6 analysis applies directly.

---

## Recommended Actions

### Immediate (This Month)
- [ ] **Confirm the deployment model** — are Belron's Salesforce orgs still using change sets, or have they moved to unlocked packages + source control? This determines the maturity baseline. 📅 2026-04-20
- [ ] **Identify which Marketing Cloud** is in use — Engagement (legacy/ExactTarget) or Growth/Next (native)? This determines the migration strategy and Agentforce readiness. 📅 2026-04-20
- [ ] **Map the Field Service territory structure** — how many territories, how many resources per territory? Validate against the 50-resource limit. 📅 2026-04-20
- [ ] **Find out if Data Cloud (Data 360) is licensed and in use** — without it, Agentforce capability is severely limited. If not licensed, assess the cost. 📅 2026-04-20

### Short-Term (Next 4 Weeks)
- [ ] **Build a licensing register** — a simple spreadsheet of what Salesforce products are licensed, at what tier, and who uses them. This is the EA baseline for governance. 📅 2026-04-30
- [ ] **Document the master of record decision** for each key data domain (customer, vehicle, order, consent) across Salesforce and the ERP. Where decisions haven't been made, flag them. 📅 2026-04-30
- [ ] **Assess MuleSoft usage** — is it in use? Who manages it? What integrations does it own? Is there a three-layer API architecture or ad-hoc connector sprawl? 📅 2026-04-30
- [ ] **Read the Salesforce Architects site** (architect.salesforce.com) — specifically the Fundamentals and Well-Architected sections. This is Salesforce's own EA guidance and it's excellent. 📅 2026-04-30

### Strategic (Next Quarter)
- [ ] **Define the Agentforce governance framework** before any production agent is enabled — Einstein Trust Layer config, escalation thresholds, audit logging, and the conversation cost model. 📅 2026-05-31
- [ ] **Identify two high-value, low-risk Agentforce pilots** — technician pre-work briefs (Field Service) and internal scheduling optimisation assistant are the natural candidates given Belron's operational context. 📅 2026-05-31
- [ ] **Propose a Data Cloud roadmap** — unified customer profile as the foundation for all downstream Agentforce use cases. Sequence: data sources → identity resolution → segmentation → agent grounding. 📅 2026-05-31

---

## Key Resources

### Official Salesforce (Primary Sources)
- [Salesforce Architects site](https://architect.salesforce.com) — EA-specific guidance, Well-Architected framework, design patterns
- [Trailhead](https://trailhead.salesforce.com) — free learning paths for every product; Architect certifications are EA-relevant
- [Salesforce Developer Docs](https://developer.salesforce.com/docs) — Metadata API, REST API, Field Service developer guide
- [Spring '26 Release Notes](https://ascendix.com/blog/salesforce-notes-spring-26-release/) — quarterly releases are significant; understanding the release calendar is essential

### Analyst / Community
- [Salesforce Ben](https://www.salesforceben.com) — best independent Salesforce resource; covers every product in depth
- [Salesforce Ben — Field Service complete guide](https://www.salesforceben.com/salesforce-field-service/)
- [MartechNotes — Journey Builder architecture](https://www.martechnotes.com/what-is-journey-builder-in-salesforce-marketing-cloud-engagement/)
- [Digital Marketing on Cloud — SFMC 2026 state](https://digitalmarketingoncloud.com/salesforce-marketing-cloud/the-state-of-sfmc-in-2026-navigating-the-shift-from-engagement-to-agentic-marketing/)

### Certifications Worth Pursuing
In priority order for a Belron EA:
1. **Salesforce Certified Platform App Builder** — platform fundamentals, the foundation
2. **Salesforce Certified Administrator** — org governance, security model, data management
3. **Salesforce Certified Application Architect** — the EA-level credential; covers data model, integration, identity, mobility
4. **Salesforce Certified Field Service Consultant** — FSL-specific; relevant given operational criticality
5. **Salesforce Certified Marketing Cloud Email Specialist** — Marketing Cloud Engagement foundation

---

## Confidence & Gaps

### High Confidence
- Platform architecture, four-layer model, and cloud relationships
- Field Service object model, limits, and governance requirements
- Marketing Cloud split (legacy vs native) — this is well-documented and widely acknowledged
- Agentforce components and multi-agent patterns
- Data Cloud architecture and zero-copy fundamentals

### Medium Confidence (Belron-specific, needs verification)
- Which Marketing Cloud platform Belron is on (Engagement vs Next)
- Whether Data Cloud is currently licensed
- The ERP system in use (Oracle EBS confirmed as a possibility from braindump, not confirmed)
- Number of Service Territories and territory structure

### Gaps to Fill
- Belron's org strategy — single org or multi-org across opcos?
- Current deployment model (change sets vs unlocked packages)
- MuleSoft licensing status and current integration landscape
- Salesforce contract structure and renewal dates (relevant to licensing governance)

---

*Research by COG Auto-Research | 3 sequential passes | Sources: Salesforce Architects documentation, Salesforce Ben, Digital Marketing on Cloud, Vantagepoint.io, architect.salesforce.com | 13 April 2026*
