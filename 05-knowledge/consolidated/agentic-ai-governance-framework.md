---
type: "consolidated-knowledge"
domain: "professional"
framework: "agentic-ai-governance"
created: "2026-04-10"
last_updated: "2026-04-20"
consolidation_id: "consolidation-2026-04-20"
source_documents: 16
status: "working"
tags: ["#framework", "#consolidated", "#agentic-AI", "#MCP", "#A2A", "#EA-governance", "#protocols"]
---

# Agentic AI Governance Framework

## Framework Overview
A working model for how an Enterprise Architect takes ownership of agentic AI infrastructure — specifically the MCP and A2A protocol layer — and turns it into governed, enterprise-grade capability before the business builds ad hoc.

**Status:** Working (solid research base; application to Belron context is the next phase)
**Last Updated:** 2026-04-10
**Source Insights:** 6 documents — MCP/A2A research braindump (Apr 8), emerging tech topic braindump (Apr 9), daily briefs Apr 8–10, competitive watchlist

---

## Why This Matters Now

In April 2026, agentic AI crossed from research into production:
- **MCP:** 97 million installs, Linux Foundation governance, enterprise auth (SAML/OIDC) shipping Q2 2026
- **A2A:** 150+ organisations, Microsoft Agent Framework 1.0 live, active production deployments
- **Gartner signal:** 40% of enterprise applications will embed AI agents by end of 2026, up from <5% in 2025

The critical window is **now to Q4 2026.** Business units and IT teams will start building agent integrations without a governance framework — as happened with SaaS adoption in the 2010s. EA's job is to own this space before it becomes ungovernable.

---

## The Architecture (What These Protocols Are)

| | MCP | A2A |
|---|---|---|
| **Governs** | Agent ↔ Tool/Data | Agent ↔ Agent |
| **Created by** | Anthropic (now Linux Foundation / AAIF) | Google (now Linux Foundation / AAIF) |
| **Analogy** | How an agent accesses the world | How agents coordinate with each other |
| **Layer** | Foundation (data + tools) | Orchestration (workflows + delegation) |
| **Enterprise status** | 97M installs, industry standard (Q1 2026) | 150+ orgs, production-ready (April 2026) |
| **Build order** | First — establish which systems get wrapped | Second — design which agents coordinate |

Together they form a complete governance architecture for multi-agent systems: MCP controls what each agent can access; A2A controls how agents hand work to each other. Without both layers, you get capable but ungovernable agents.

---

## Core Principles

### Principle 1: MCP Is Now Infrastructure — The Decision Is How, Not Whether

**Statement:** At 97M installs and Linux Foundation governance, MCP is not a vendor bet — it is industry infrastructure comparable to Kubernetes or HTTP. The decision is not whether to adopt MCP; it is which systems to wrap first, in what order, with what governance.

**Evidence:**
- [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]] — "MCP is not a vendor product — it's an industry standard. CIOs and EAs can now build long-term integration roadmaps around it without vendor lock-in risk"
- [[daily-brief-2026-04-10]] — A2A 1-year milestone: 150+ orgs, Microsoft Agent Framework 1.0 ships with full MCP support — "the MCP-plus-A2A architecture is becoming the production-ready default for enterprise agentic systems"
- [[daily-brief-2026-04-09]] — MCP enterprise auth (SAML/OIDC) shipping Q2 2026 — the enterprise deployment unlock
- [[daily-brief-2026-04-17]] — **Zapier MCP goes GA with 9,000+ apps, 30,000+ actions, all plans, no extra cost.** This is the moment MCP stopped being a developer experiment and became a default expectation. The barrier to MCP adoption just dropped to near-zero for anyone who already uses Zapier. The same dynamic as when Zapier made webhooks accessible to non-developers in the early 2010s — a complex integration pattern pulled into the mainstream overnight.

**How to apply:** Frame MCP decisions as integration architecture decisions — which business systems get an MCP server, in what priority order, with what data classification. This is standard EA remit. **Zapier MCP GA is the trigger to start governing MCP-connected actions, not just allowing them** — an AI agent that can send emails, create calendar events, update CRM records, and file documents across 9,000 apps is a privilege escalation requiring access review.

**Confidence:** High

---

### Principle 2: A2A Is Where Competitive Advantage Will Be Built

**Statement:** MCP will be table stakes within 12–18 months. The organisations that design thoughtful multi-agent architectures using A2A now will have a structural head start on workflow automation. The EA who designs these architectures becomes strategically irreplaceable.

**Evidence:**
- [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]] — "The organisations that design thoughtful multi-agent architectures using A2A *now* will have a structural head start"
- [[braindump-2026-04-09-1322-emerging-technology-topic]] — Option A assessed as the strongest emerging tech topic: "positions EA as the function that owns the governance of the next major technology wave"
- [[daily-brief-2026-04-10]] — A2A surpasses 150 orgs including AWS, Cisco, Google, IBM, Microsoft, Salesforce, SAP, ServiceNow — the ecosystem is now too large to ignore

**How to apply:** Identify Belron's first multi-agent workflow candidate. The booking → dispatch → calibration → claims chain is a natural sequence. Design the A2A handoffs before the business builds them without governance.

**Confidence:** High

---

### Principle 3: EA Is the Natural Owner of Both Protocols

**Statement:** MCP and A2A decisions (which systems are wrapped, which agents are authorised to delegate to which other agents, what data flows between agents) are quintessential EA decisions — capability, integration, governance, and security all in one. No other function has the mandate or the vantage point.

**Evidence:**
- [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]] — "The EA role is the natural owner of both. MCP decisions... and A2A decisions... are quintessential enterprise architecture decisions"
- [[daily-brief-2026-04-10]] — "Integration is the new enterprise architecture... agentic AI governance falling to EA teams"
- [[braindump-2026-04-09-1322-emerging-technology-topic]] — The MCP/A2A paper-presentation-briefing set positions EA as "the function that owns the governance of the next major technology wave"

**How to apply:** Propose an "Agentic AI Architecture Review" as a standing EA agenda item — this creates formal ownership of the space before business units start building ad hoc.

**Confidence:** High

---

### Principle 4: Governance Must Precede Proliferation

**Statement:** AI agents will proliferate inside enterprise systems in 2026 regardless of whether governance exists. The EA function's job is to establish the governance framework before proliferation makes it retrospective. Two confirmed enterprise incidents in April 2026 are the concrete evidence: neither required a malicious actor — both resulted from ungoverned agent access alone.

**Evidence:**
- [[daily-brief-2026-04-09-pm]] — OpenAI, NVIDIA, Okta all launched agent platforms in the same week — supply-side pressure is building fast
- [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]] — "40% of enterprise applications will feature task-specific AI agents by 2026, up from <5% in 2025" (Gartner)
- [[daily-brief-2026-04-10]] — EU AI Act auditability requirements mean "AI Act compliance requires end-to-end lineage and explainability baked into the integration layer — this is an EA design concern, not a data team bolt-on"
- [[daily-brief-2026-04-14-post]] — OutSystems research: 94% of enterprises report concern about AI agent sprawl (uncontrolled proliferation of autonomous agents outside central governance)
- [[daily-brief-2026-04-15]] — Qlik research (QlikConnect): only **12% of enterprises have a centralised platform to maintain control over AI sprawl.** 97% have committed budget to agentic AI; 18% fully deployed. Governance is the #1 blocker.
- [[daily-brief-2026-04-15]] — **Incident: AI agent publishes security firm's threat intel to the open web.** No malicious actor. The agent had access to an internal knowledge base and an external publishing tool with no classification boundaries — it simply connected the two. This is the ungoverned MCP access failure mode made real.
- [[daily-brief-2026-04-15]] — **Incident: CodeWall claims breach of Bain & Company's internal AI tool via exposed API credentials.** No sophisticated attack — misconfigured secrets. Confirms that enterprise AI tools are being deployed faster than security controls can keep up.

**How to apply:** 
- Use the A2A 1-year milestone as the trigger to bring a governance brief to EA leadership
- Use the confirmed incidents as the opening examples: "This happened at a security firm, at Bain, and at Vercel. Here is how we prevent it at Belron."
- The Qlik "12%" stat is the strongest governance gap number available: "We want to be in the 12%, not the 88%."
- Frame the Gateway+Registry architecture pattern (MCP access control + MCP server registry) as the structural answer to the data leakage and credential breach incidents
- **EY deployment (130K auditors on multi-agent Microsoft Azure+Foundry+Fabric platform embedded in EY Canvas)** is the enterprise reference architecture for large-scale agentic AI deployment. Use it to demonstrate scale and provide a credibility anchor in governance briefs.

**New incident (April 2026): Vercel/Context.ai OAuth breach.**
An AI tool's Google Workspace OAuth application was compromised. The attacker pivoted through the OAuth grant into Vercel's internal systems. No sophisticated exploit — the AI tool's authentication pathway became the attack vector. This is a new and important failure mode: not the agent itself acting unpredictably, but the *authentication infrastructure* of the agent's integration. Governance of AI tool OAuth grants must be part of any MCP governance policy.

**Confidence:** High

---

## The Belron Application Map

For a windscreen repair/replace business, the natural multi-agent workflow is end-to-end job lifecycle:

| Business Area | MCP Server (what the agent accesses) | A2A Handoff (agent → agent) |
|---|---|---|
| Customer booking | CRM / booking system | Booking agent → Dispatch agent |
| Parts & inventory | Parts database | Parts agent → Supplier portal agent |
| Insurance claims | Claims system | Claims agent → Insurer portal agent |
| ADAS calibration | Calibration records | Calibration agent → Documentation agent |
| Technician scheduling | Scheduling system | Dispatch agent → Routing agent |

The booking → dispatch → calibration → claims chain is the most valuable first target: it spans the primary customer value chain and would reduce manual handoffs at each stage.

---

## Applications & Use Cases

### Use Case 1: MCP Governance Register
**When to Apply:** Before any business unit or IT team deploys an MCP-connected tool

**How to Apply:**
1. Define a classification scheme for data types that can be exposed via MCP servers (public, internal, confidential, restricted)
2. Create a registry of all MCP servers deployed in the enterprise — system, owner, data classification, approved AI clients
3. Apply the same process that governs API access to MCP server access
4. Publish the governance policy; make it easy to comply, hard to bypass

**Expected Outcomes:** Prevents data leakage through unmanaged MCP connections; creates visibility into what AI models can access

---

### Use Case 2: A2A Workflow Design — First Multi-Agent Pilot
**When to Apply:** Once MCP servers are in place for 2+ systems that are part of the same business process

**How to Apply:**
1. Map the workflow end-to-end — what is the trigger, what are the steps, what is the output?
2. Identify which steps could be handled by an AI agent vs. require human decision
3. Design the Agent Cards for each agent — what capabilities do they advertise?
4. Define delegation rules — which agents are authorised to hand tasks to which other agents?
5. Build a prototype on the lowest-risk workflow first (e.g., internal scheduling optimisation before customer-facing)

---

### Use Case 3: Agentic AI Briefing for Leadership
**When to Apply:** Now — the A2A 1-year milestone is the hook

**Format:**
- One-page briefing: "What just standardised, what it means for Belron, what decisions we need to make"
- Full paper: MCP + A2A protocol primer, Belron application map, governance recommendation
- Presentation: "The Agent Economy — What It Means for Belron's Architecture"

**Audience:** EA leadership, CTO, opco technology leads

---

## Boundaries & Limitations

**This framework works when:**
- Building multi-agent workflows where steps can be clearly defined and delegated
- Systems have APIs or can be wrapped in MCP servers
- Governance appetite exists for a formal AI integration policy

**This framework does NOT work when:**
- The use case requires fully custom AI interactions not following standard protocol shapes
- Infrastructure does not support MCP-compatible tool interfaces
- Governance maturity is too low for formal agent policy (build awareness first)

---

## Evolution & History

### April 8, 2026: Research Phase
MCP and A2A researched in depth. Key finding: these are not competing standards — they are complementary layers. MCP is foundation; A2A is orchestration. Both now have Linux Foundation governance.

**Source:** [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]]

### April 9, 2026: Strategic Positioning
The emerging tech topic planning explicitly assesses MCP/A2A as the strongest topic for a three-part deliverable set. The external environment validates this: OpenAI, NVIDIA, and Okta all launched agent platforms the same week.

**Source:** [[braindump-2026-04-09-1322-emerging-technology-topic]]

### April 10, 2026: Production Confirmation
A2A 1-year milestone confirms 150+ organisations and Microsoft Agent Framework 1.0 — the protocol has crossed from experimental to enterprise-production. The EA governance window is now.

**Source:** [[daily-brief-2026-04-10]]

### April 16–20, 2026: MCP Becomes Mainstream + New Attack Vector Confirmed

**What Changed:** Three developments that materially advance the governance case:

**1. Zapier MCP GA — MCP is now mainstream infrastructure.**
9,000+ apps, 30,000+ actions, all Zapier plans, no extra cost. MCP crossed from protocol to default expectation overnight. For enterprise architecture: the question is no longer "will business units adopt MCP?" but "which actions do we want to enable and what governance do we need *before* agents start connecting to everything by default?" This is the SaaS-in-the-2010s moment — governance after the fact is painful; governance before proliferation is protective.

**2. Vercel/Context.ai OAuth attack — new attack vector class confirmed.**
An AI tool's Google Workspace OAuth app was compromised, with the attacker pivoting through the OAuth grant into Vercel's internal systems. No sophisticated exploit. The attack vector was the *authentication infrastructure of the AI tool's integration*, not the AI behaviour itself. This extends the governance scope beyond data access (what can the agent read?) to include authentication governance (what OAuth grants have AI tools been given, and are those grants auditable and revocable?).

**3. EY 130K auditors on agentic AI — enterprise reference architecture exists.**
EY has deployed a multi-agent platform (Microsoft Azure + Foundry + Fabric) to 130,000 auditors embedded in EY Canvas, their core audit platform. This is the largest enterprise agentic AI deployment confirmed to date. It provides a credible reference point for enterprise governance discussions: "EY ran a governance programme before deploying this to 130K employees. What is Belron's equivalent?" 

**Sources:** [[daily-brief-2026-04-17]], [[daily-brief-2026-04-20]]

---

### April 14–15, 2026: The Governance Gap Quantified + First Confirmed Incidents

The week produced the sharpest evidence yet that the governance gap is real and underestimated:

**The quantified gap:**
- OutSystems: 94% of enterprises report concern about agentic AI sprawl
- Qlik (QlikConnect): only 12% of enterprises have a centralised platform to control it
- Translation: nearly everyone is worried; almost no one has fixed it. Being in the 12% is a genuine competitive advantage, not just risk mitigation

**Two confirmed real-world incidents (no malicious actors required):**
1. An unnamed security firm's AI agent published internal threat intelligence to the open web. The agent had legitimate access to an internal knowledge base and an external publishing tool. No classification boundaries existed. No one told it not to. This is the exact failure mode the Gateway+Registry governance pattern exists to prevent.
2. CodeWall claimed to have breached Bain's internal AI tool via exposed API credentials. No sophisticated attack — just misconfigured secrets management. Enterprise AI tools deployed faster than security controls.

**Emerging architecture:** The three-layer micro/macro/meta agent model is gaining traction (Bain paper, CIO.com article, MCP/A2A community). Micro agents handle specific tasks; macro agents orchestrate across systems; meta/governance agents own oversight, auditability, and policy. This is the architecture that addresses both the data leakage incident (classification-aware meta layer) and the credential breach (centralised secrets management at the governance layer).

**Sources:** [[daily-brief-2026-04-14-post]], [[daily-brief-2026-04-15]]

---

## Related Frameworks

- [[ea-effectiveness-framework]] — Principle 2: The MCP/A2A briefing is a dual-purpose artefact (governance tool + visibility instrument)
- [[belron-business-understanding-framework]] — Layer 4 (Systems Landscape) identifies which systems are MCP server candidates
- [[ai-damage-assessment-strategy-framework]] — The damage assessment workflow is a candidate A2A multi-agent pipeline

---

## Future Development

**Next Steps:**
- [ ] Scan Belron's current AI tool landscape: which tools already support MCP? 📅 2026-04-17
- [ ] Map the 3–5 highest-value internal systems for MCP server wrapping 📅 2026-04-18
- [ ] Draft the Agentic AI briefing for leadership (use A2A 1-year milestone as hook) 📅 2026-04-10

**Questions to Resolve:**
- Does Belron have a formal AI governance policy that MCP/A2A decisions should connect to?
- Which cloud platform does Belron run on? (Azure/GCP/AWS) — this determines the Microsoft Agent Framework vs. Vertex AI vs. Bedrock path
- Is there an existing agent or automation programme where EA governance ownership would be welcomed vs. seen as overhead?

---

*Consolidated from 16 sources | First version: April 10, 2026 | Last updated: April 20, 2026 | Status: Working*
