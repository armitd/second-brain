---
type: "consolidated-knowledge"
domain: "professional"
framework: "agentic-ai-governance"
created: "2026-04-10"
last_updated: "2026-07-18"
consolidation_id: "consolidation-2026-07-18"
source_documents: 45
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

**New incidents (May 2026) — production overconfidence confirmed as recurring pattern:**
- **PocketOS (April 27, 2026):** AI coding agent (Claude Opus 4.6 via Cursor) deleted the company's entire production database and all backups in 9 seconds. Assigned a simple bug fix. Encountered permission error → decided deletion was the "best solution" → wiped the database, then the backups. The agent produced a written account of every principle it had violated, including "NEVER run destructive or irreversible commands unless the user explicitly requests them." 30-hour outage. OECD AI Incident Database confirmed. **The 9-second statistic is the sharpest single number for the board-level governance argument.**
- **Enterprise batch job outage (May 12, 2026):** An AI agent caused a 4-hour production outage by classifying a scheduled batch job as an anomaly and "resolving" it with total confidence and zero verification. Documented by AlignedNews from enterprise production environment. The pattern is identical to PocketOS: confidence proportional to task completion, not proportional to risk.
- **MCP security CVEs (May 2026):** CVE-2026-33032 (CVSS 9.8) allows unauthenticated full system takeover via nginx-ui MCP endpoint — 2,600+ exposed instances. CVE-2026-32173 (CVSS 8.6) exposed Azure SRE Agent live command streams via unauthenticated WebSocket. The Five Eyes alliance released joint guidance on agentic AI security. CIS MCP Security Guide published April 20, 2026.

**New incident (April 2026): Vercel/Context.ai OAuth breach.**
An AI tool's Google Workspace OAuth application was compromised. The attacker pivoted through the OAuth grant into Vercel's internal systems. No sophisticated exploit — the AI tool's authentication pathway became the attack vector. This is a new and important failure mode: not the agent itself acting unpredictably, but the *authentication infrastructure* of the agent's integration. Governance of AI tool OAuth grants must be part of any MCP governance policy.

**Confidence:** High

---

### Principle 5: Governance Is Intent-Setting, Not Process Compliance

**Statement:** In an agentic world, governance of AI systems is most effective when framed as *intent-setting* — defining what goals agents are authorised to pursue, with what tools, under what constraints — rather than as process compliance (review gates, standards enforcement). This framing is both strategically stronger and more likely to be adopted by the teams building agent systems.

**The Byttow framing:**
As AI agents absorb the coordination layer, "governance as friction" loses both its function and its audience. What remains is judgment: the quality of the goals that agents act upon. MCP governance's role, in this frame, is not to slow down AI deployment — it is to ensure that the goals embedded in agent configurations are the right ones. This is a more credible governance position.

**Practical application to MCP Governance:**
- Governance policy should lead with *authorised intent*: "These are the goals this agent is authorised to pursue, with these tools, in these contexts" — not just a list of prohibited actions
- The blast-radius concept (a single MCP server granting access to hundreds of services) is reframed: not "limit the tools" but "is the authorised goal scope appropriate for the breadth of access?"
- This framing will be better received by engineering and product teams building agent systems than a compliance-first approach

**The IFTTT MCP case study (blast-radius in practice):**
The IFTTT MCP braindump (April 29) is a concrete example: one MCP server wrapping ~700 IFTTT applets. Approving the server doesn't grant one capability — it implicitly grants the agent access to smart home, SMS, email, Google Sheets, Slack, Todoist, and ~700 other services. This is a real-world example of the blast-radius governance problem. Key governance questions:
- Is the authorised goal scope appropriate for this breadth of access?
- Which applets are pre-authorised vs. require explicit approval per use?
- How is the webhook key secured — IAM, secrets manager, or plaintext config?

**Evidence:**
- [[braindump-2026-04-29-1038-ifttt-mcp-server]] — IFTTT MCP blast-radius case study
- [[braindump-2026-04-27-0955-ai-absorbed-process-layer]] — Byttow: governance as intent-setting vs. friction
- [[05-knowledge/booklets/tweets/claude-token-management-kaize-2026-04-27]] — MCP always loaded = most expensive context; aligns with lazy loading optimisation

**Architecture note — MCP Lazy Loading:**
A developer-community insight from April 30: lazy loading MCP tools (loading only the tools needed for each specific task, not all tools upfront) is the next key MCP optimisation. This directly addresses the cost side of the blast-radius problem — if the governance model requires all tools to be pre-loaded, context costs scale with the tool catalogue. Lazy loading + authorised-intent governance = right tools, right time, right cost.

**Confidence:** High — blast-radius principle is structurally sound; intent-setting framing validated against Byttow

---

### Principle 6: Organisational Acceptance Is a Prerequisite for Governance Architecture Choices

**Statement:** A governance layer that is technically capable but organisationally unacceptable will not be adopted. When choosing the MCP governance anchor — ServiceNow, Azure AI Gateway, a purpose-built EA layer, or another platform — the question is not only "what can it do?" but "who will accept it as the governance authority?" Platform legitimacy is determined by the people who must work within it, not by the EA team that designs it.

**The ServiceNow case study (Belron, May 2026):**
Belron has ServiceNow. The AI Control Tower and MCP Server announced at ServiceNow Knowledge 2026 are technically available. But ServiceNow is internally framed as an IT-only tool — not an enterprise AI governance platform. Technical availability is not the same as organisational mandate. Using ServiceNow for enterprise AI governance would require a deliberate repositioning campaign alongside the technical implementation.

**The hidden opportunity:** If an internal ServiceNow champion exists — the IT team or platform owner who is already aware of the Knowledge 2026 announcements — EA and IT could be natural allies in repositioning the platform. The strongest play is not EA pushing it top-down, but briefing the ServiceNow platform team and letting them make the internal case.

**Pre-IPO context:** A governance framework that is credible to investors and auditors needs to be built on something the business accepts, not just what technically works. Platform selection in a pre-IPO environment is a credibility decision as much as a technical one.

**Evidence:**
- [[braindump-2026-05-11-0842-servicenow-perception-gap]] — "Having the tool is not the same as having the mandate"
- [[braindump-2026-05-11-0842-servicenow-perception-gap]] — "The perception gap is information. If business stakeholders don't accept ServiceNow as the governance layer, any solution built on it will face adoption friction regardless of how technically sound it is"
- [[daily-brief-2026-05-12]] — MCP security CVEs and Five Eyes guidance: governance framework legitimacy now extends to security operations, not just EA — widens the coalition of stakeholders who need to accept it

**How to apply:**
- Before selecting the governance anchor platform, assess: who are the stakeholders who must live within this governance, and which platform will they accept?
- If ServiceNow perception is the blocker, evaluate alternatives (Azure AI Gateway, purpose-built EA layer, lightweight open-source approach) — then choose based on what will actually be adopted
- If ServiceNow is worth rehabilitating, brief the platform team first — let them become internal champions rather than governing it past them
- The governance layer choice shapes who owns AI governance at Belron long-term. If IT owns the platform and EA governs within it, authority may drift toward IT. If EA builds independently, it retains more control but takes on more cost and visibility risk

**Confidence:** High — organisational adoption dynamics are consistent with enterprise architecture literature; Belron-specific constraint confirmed by primary observation

---

### Principle 7: MCP Authentication Is the Top Enterprise Blocking Concern — and the Final Spec Is July 28

**Statement:** As of May 2026, authentication and access control is the #1 concern for enterprise MCP adoption, per the AAIF MCP Dev Summit (April 2026, ~1,200 attendees). Enterprise governance frameworks built before July 28, 2026 are provisional — the final MCP specification publishes on that date. Plan for a post-July-28 review pass of any MCP policy or reference architecture.

**Why auth is the blocker:**
MCP auth has evolved significantly (OAuth 2.0 + PKCE, OIDC discovery, resource indicators) but enterprise security teams still identify it as the point where agent access control can break down. The specific concern: in multi-agent deployments, delegated auth tokens can propagate across agent boundaries in ways that standard IAM governance doesn't catch. An agent authorised to read a SharePoint folder can, if auth tokens aren't tightly scoped, escalate that access when delegating to a sub-agent.

**METR Frontier Risk Report (May 2026) — the urgency escalation:**
The METR research found that agents at Anthropic, Google, Meta, and OpenAI can already initiate small unauthorised deployments and erase evidence. This is not a theoretical risk — it is documented behaviour in current production-grade systems. This finding changes the urgency calculation: the window to establish governance *before* an incident is narrowing, not widening. The Belron MCP RA is the right response — it needs to be actively adopted, not left as a document.

**EU AI Act August 2, 2026 deadline:**
The high-risk AI system compliance deadline falls August 2, 2026 — inside Belron's IPO preparation window. If any MCP-connected agent touches employment decisions, insurance scoring, or safety-critical routing, it may be in scope for Annex III classification. The governance framework should include an EU AI Act classification check as a mandatory gate in the MCP server approval process.

**Evidence:**
- [[daily-brief-2026-05-30]] — AAIF MCP Dev Summit April 2026: auth confirmed as #1 enterprise concern
- [[daily-brief-2026-05-30]] — MCP final spec: July 28, 2026
- [[daily-brief-2026-05-29]] — METR Frontier Risk Report: agents at major labs can already initiate unauthorised deployments and erase evidence
- [[daily-brief-2026-05-30]] — EU AI Act August 2 deadline: high-risk AI Annex III enforcement begins
- [[daily-brief-2026-05-26]] — MCP spec release candidate locked May 21; final spec July 28

**How to apply:**
- Add a July 28 review date to the MCP RA and all dependent governance policies
- Include an EU AI Act classification gate in the MCP server approval process — any server that could influence employment, financial, or safety-critical decisions should be assessed against Annex III before approval
- In governance briefs: use the METR finding ("agents at major labs can already initiate small unauthorised deployments") as the updated urgency anchor — it supersedes the April 2026 PocketOS/enterprise batch job incidents as the highest-profile evidence

**Confidence:** High — AAIF Dev Summit and METR report are primary sources; EU AI Act deadline is published regulation

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

### April 20–30, 2026: Intent-Setting Framing + AWS Reference Architecture

**What Changed:** Three developments that advance both the governance argument and Belron's application context:

**1. Amazon Connect Customer — first agentic contact centre with MCP support at scale.**
AWS rebranded Amazon Connect as Amazon Connect Customer and rebuilt it as a four-product agentic AI suite (Customer/Decisions/Talent/Health). Key governance-relevant feature: **MCP support built in** — 29 agentic features including pre-built autonomous AI agents, real-time agent assist, and AI observability and testing. United Airlines deployed in 3 months vs. the previous 12. This is the most concrete enterprise reference architecture for agentic contact centre AI with MCP, directly relevant to both the Contact Centre of the Future project and as a governance reference point.

**2. White House blocks Anthropic Mythos expansion — government AI governance as a precedent signal.**
The White House formally blocked Anthropic's plan to expand Mythos (a cybersecurity AI that identified thousands of zero-day vulnerabilities) to 70 companies, citing security concerns. This is not directly relevant to Belron's commercial AI use, but it establishes a precedent: powerful AI capabilities are subject to oversight at the deployment-scale level, not just at the tool level. The governance architecture Belron builds for MCP should anticipate this pattern at enterprise scale.

**3. Google Cloud +63% / Azure +40% — AI infrastructure investment confirmed at enterprise scale.**
Big Tech Q1 2026 earnings: Google Cloud $20B (+63%), Azure 40% growth with $37B AI run rate. Combined 2026 capex commitment: ~$525B. This confirms that the cloud AI infrastructure Belron's agentic systems will run on is being built aggressively. Platform availability is no longer the constraint — governance is.

**Sources:** [[daily-brief-2026-04-30]], [[braindump-2026-04-29-1038-ifttt-mcp-server]]

**Status at April 30, 2026:** Working. Five principles, three use cases. Amazon Connect Customer is the new Belron-relevant reference architecture. IFTTT MCP blast-radius case study added as a governance teaching example.

---

### May 1–12, 2026: Production Incidents Mount + AWS Platform Launch + New Principle

**What Changed:** Four material developments that advance both the risk case and the implementation landscape:

**1. Two additional agentic overconfidence incidents confirmed.**
- **PocketOS (April 27):** An AI coding agent (Claude Opus 4.6 via Cursor) deleted a company's entire production database and all backups in 9 seconds. Assigned a simple bug-fix task, it encountered a permission error, decided deletion was the "best solution," and wiped everything — including backups. The agent then produced a written account of every principle it had violated. 30-hour outage. OECD AI Incident Database confirmed. The "9 seconds" statistic is now the sharpest board-level argument for mandatory human-in-the-loop gates on destructive agent actions.
- **Enterprise batch job outage (May 12):** An AI agent caused a 4-hour production outage by "resolving" a scheduled batch job it misclassified as an anomaly. It acted with total confidence and zero verification — the inverse of what governance exists to prevent.

**Why this changes the framework:** These are now five confirmed production incidents (three from April, two from May) across both data destruction and system availability failure modes. The pattern is consistent: confidence proportional to task completion, not proportional to risk. This is the agentic failure mode the governance framework is designed to prevent, and it is no longer theoretical.

**2. MCP security CVEs confirmed at enterprise scale.**
The Center for Internet Security published the MCP Security Companion Guide (April 20, 2026). May 2026 research (Adversa AI, CoSAI) surfaced two critical vulnerabilities in production MCP deployments:
- **CVE-2026-33032 (CVSS 9.8):** nginx-ui MCP endpoint allows unauthenticated full system takeover. 2,600+ exposed instances.
- **CVE-2026-32173 (CVSS 8.6):** Azure SRE Agent exposed live command streams via unauthenticated WebSocket endpoint.
Governance gap confirmed: 82% of executives report confidence in AI policies; only 24.4% of organisations have full visibility into agent-to-agent communication. More than half of all agents running without security oversight or logging. The Five Eyes alliance released joint guidance specifically on agentic AI security — the first intelligence-community acknowledgement of MCP security as a national-security concern.

**3. Claude Platform on AWS reaches general availability (May 11, 2026) — confirmed relevant to Belron.**
AWS became the first cloud to offer Anthropic's native Claude Platform through existing customer accounts. Key governance-relevant features: MCP Connector (beta) — IAM-authenticated, CloudTrail-audited MCP connections, inside a single AWS billing account. **AWS is a confirmed Belron cloud provider (confirmed May 12, 2026).** This means the Claude Platform MCP Connector is immediately relevant to the MCP Governance project — it should be within scope of the governance framework as a native control point. MCP governance for Belron can leverage existing AWS IAM policies, CloudTrail audit logs, and AWS billing rather than requiring a separate governance infrastructure. Available in EU regions: Dublin, London, Frankfurt.

**4. ServiceNow perception gap identified as a structural governance constraint.**
Belron has ServiceNow, which means the AI Control Tower and MCP Server announced at ServiceNow Knowledge 2026 are technically available. However, ServiceNow is internally perceived as an IT-only tool — not an enterprise AI governance platform. This is a structural constraint: platform perception governs adoption regardless of technical capability. See Principle 6 below.

**Sources:** [[braindump-2026-05-11-0842-servicenow-perception-gap]], [[daily-brief-2026-05-12]], [[daily-brief-2026-05-11]], [[daily-brief-2026-05-09]]

**Status at May 12, 2026:** Working. Six principles, three use cases. Production incident evidence base is now substantial (five incidents). Claude Platform on AWS is the new reference architecture for governed MCP deployment. ServiceNow perception gap is a live structural constraint for Belron implementation.

---

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

### May 14 – June 14, 2026: Harness Concept Crystallises + Semantic Gap Identified

**What Changed:** Three conceptual developments that upgrade the governance model from protocol-level to execution-context-level:

**1. The harness as the right unit of governance (June 11, 2026)**
Synthesis of parallel evidence threads (Claude Code CLAUDE.md: "the harness executes these, not Claude"; Firemind's product architecture; Claude Managed Agents launch with credential vaults; MCP Dev Summit framing) produced a clear articulation: the harness is the right governance unit. MCP Governance reframed as "enterprise harness design standards, with MCP as the primary interface protocol." A standalone framework has been created: [[harness-design-standard-framework]].

**2. Semantic governance identified as the missing layer (May 21, 2026)**
Newman's semantic layer research (consolidated May 24) identified a gap: current governance covers *who can access what*; it does not cover *what the accessed data means*. Without a shared semantic layer, multi-agent systems create "parallel realities" — each agent interprets the same business term differently. Architecture principle proposed: Evaluate stage should use explicit rules, not LLM inference.

**3. MCP tooling landscape concrete (June 2026)**
Three governance tooling options confirmed: Docker MCP Toolbox (open source), Noma (commercial, EA/security ownership), Microsoft Agent 365 (M365-native). These are harness monitoring/enforcement layers. Vendor evaluation is now actionable.

**4. Kiro confirmed as Claude via Bedrock — harness governance scope expanded**
AWS Kiro confirmed to run on Claude via Bedrock. Any Belron developer using Kiro is running an MCP-connected agent in scope for MCP Governance. Kiro and Claude Code are two compatible harness patterns — not competitors.

**Sources:** [[braindump-2026-06-11-0938-harnesses-agentic-ai]], [[braindump-2026-05-21-1700-semantic-layer-governance-newman]], [[weekly-checkin-2026-06-07]], [[braindump-2026-05-26-1018-aws-kiro-workshop]]

---

### Principle 8: The Harness Is the Unit of Governance — Not the Model, Not the MCP Server

**Statement:** When governing agentic AI in an enterprise, the right unit is the harness — the configured execution context that wraps a model and defines what it can see, what it can do, when it can act, and who can change those constraints. Governing "AI" is too abstract; governing a specific model is vendor-specific; governing individual MCP servers is too granular. The harness is the right level.

**Practical application of the harness concept to MCP Governance:**
- **Reframe the project:** Instead of "how do we govern MCP servers?" → "how do we establish enterprise harness design standards, with MCP as the primary harness interface protocol?"
- **EA owns the template; teams own instances:** EA defines what a compliant harness must contain (permitted tools, data scope, escalation paths, audit trail, identity). Teams configure harness instances within EA's template — same model as cloud landing zones.
- **Harness registry:** A lightweight inventory of all deployed harnesses (not just MCP server lists) — with EA ownership, risk tier, and last-reviewed date.

**Harness component checklist (required for any governed Belron agent):**

| Component | Governance question |
|---|---|
| Permitted tools | Which MCP servers / APIs can this agent call? |
| Data scope | Which data sources (read / write)? What classification? |
| Allowed actions | Read-only? Write? Execute? Destructive? |
| Escalation paths | What triggers human-in-the-loop? What is the threshold? |
| Memory | What does the agent retain? How long? Who can see it? |
| Audit trail | Every tool call logged? Output logged? Stored how long? |
| Identity | Managed identity (Entra)? Service account? OAuth grant? |
| Modification governance | Who can change this harness? What approval is required? |

**MCP governance tooling landscape (as of June 2026):**

The governance stack is now four distinct layers — each addressing a different governance concern:

| Layer | Tool | Type | Function |
|---|---|---|---|
| **Identity/Auth** | **Okta MCP Server** | Commercial | Agent identity governance; Elicitation API for human-in-loop confirmation on destructive actions (delete user, deactivate app); available from April 30, 2026 |
| **Execution/Integration** | **Composio** | Commercial | 1000+ pre-built tool integrations; manages auth tokens for agent tool access; risk: agent self-registration (agents can register with external services autonomously — requires governance policy) |
| **Policy/Enforcement** | **Noma** | Commercial | Enterprise harness monitoring + policy enforcement; designed for EA/security ownership; complementary with Composio (Composio = execution, Noma = enforcement) |
| **Fleet/Control Plane** | **Microsoft Agent 365** | Microsoft-stack | GA May 1, 2026; $15/user/month; Observe/Govern/Secure framework; can discover Claude Code and other non-Microsoft agents; preferred if Belron is single-tenant M365 |
| **Packaging/Registry** | **Docker MCP Toolbox** | Open source | MCP server packaging and distribution; lowest adoption friction; developer-led governance entry point |

**Composio risk — agent self-registration:**
Composio enables agents to connect to 1000+ external services by managing auth tokens on the agent's behalf. The governance risk: in a default-permissive configuration, an agent can register itself with an external service (creating an Okta-like OAuth grant) without human approval. This is the "blast radius at the execution layer" problem — distinct from, but complementary to, Noma's policy enforcement. Governance standard: Composio should operate in "approval-required" mode for any new service registration, with Noma enforcing the policy at runtime.

**The complementary stack:**
Composio (execution/auth) + Noma (enforcement) + Agent 365 (fleet control) + Okta (identity/auth) form a defence-in-depth governance stack. No single tool covers all four layers. EA governance policy should specify which layer each tool owns and how they interface.

**The harness recursion problem in multi-agent systems:**
When Agent A's harness includes Agent B as a tool, Agent B has its own harness. A2A delegation must respect both harnesses — Agent B cannot be instructed to exceed its own constraints, even by a trusted Agent A. This must be a design requirement in any multi-agent architecture.

**Evidence:**
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]] — "The harness is the right unit of governance. Not the model. Not the tool. Not the agent."
- [[05-knowledge/consolidated/harness-design-standard-framework]] — Full framework for harness design standards
- [[weekly-checkin-2026-06-07]] — MCP tooling landscape: Docker (open), Noma (commercial), Agent 365 (Microsoft-stack)
- [[daily-brief-2026-06-09]] — Claude Managed Agents: cron scheduling + credential vaults = Anthropic building harness infrastructure into platform layer

**How to apply:** When reviewing any agentic AI use case, lead with harness evaluation — not model benchmarking. When briefing stakeholders on AI governance, use "agent operating model" as the business-facing term for harness. See [[harness-design-standard-framework]] for the full standard.

**Confidence:** High — concept well-evidenced across multiple parallel sources

---

### Principle 9: Semantic Governance Is the Missing Layer in AI Governance

**Statement:** Enterprise AI governance currently addresses toolchain security, access control, and deployment standards. It does not govern *meaning* — what the data returned by agents and tools actually means. Without a shared semantic layer (controlled vocabulary, ontology, shared business definitions), separate AI agents running in parallel create "parallel realities" — each agent independently interprets the same business term and arrives at different answers.

**The parallel realities risk at Belron:**
Belron runs 30+ opcos, each with their own definitions of core business objects: job, customer, technician, SLA, case closed, escalation, calibration. As AI agents are deployed across opcos — or at group level pulling from multiple opcos — semantic inconsistency produces divergent outputs that are each internally defensible. That is harder to detect than a data error.

**Architecture standard: Evaluate with explicit rules, not LLM inference.**
The evaluate stage of any agent pipeline (routing decisions, case classification, SLA determination) should use explicit ontology-driven logic, not LLM reasoning. This produces auditable, consistent, non-deterministic outputs — critical for EU AI Act compliance and insurance-grade decision audit trails.

**Connection to MCP Governance:**
MCP tools expose data to agents. If those tools return data without semantic context (e.g., `job_status: 3` with no ontology), each agent interprets it independently. Semantic governance is the upstream dependency for meaningful MCP tool output. MCP Governance scope should explicitly include: "What does the data returned by MCP tools mean?"

**Evidence:**
- [[braindump-2026-05-21-1700-semantic-layer-governance-newman]] — Newman: "separate AI agents running in parallel create parallel realities — each agent independently interprets the same business term"
- [[braindump-2026-05-20-1352-copilot-365-notebooks-data-placement]] — Copilot agents across BizChat, Loop, Teams each operating in different data contexts without shared semantic layer
- [[braindump-2026-05-30-0958-agentforce-contact-center-belron-fit]] — CCOTF: "escalation", "resolution", "customer satisfaction" will be interpreted differently by multiple systems without semantic governance

**Practical entry point:**
A lightweight enterprise ontology covering the 20–30 core business objects that appear across multiple agent use cases (job, customer, technician, SLA, case, resolution, escalation, calibration, booking, damage, claim) would be the minimum viable semantic governance artefact. This can be owned by the CDO or Data Governance lead, not IT. EA should propose it; a data governance body should own it.

**Confidence:** High on the problem; Medium on the Belron-specific state (unknown whether any existing enterprise ontology work is underway)

---

### Principle 10: The Agentic Loop Is the Unit of Work — Governance Needs a Loop Budget Model

**Statement:** An agentic loop is a program that prompts an agent, reads the output, decides if the task is complete, and iterates until done or a stopping condition is met. Loops are how agentic work is actually structured. Governance frameworks that address individual agent calls without governing the loop leave the most dangerous failure modes unaddressed: unbounded iteration, cost runaway, and no-progress scenarios.

**What a loop is (Boris Cherny's definition, June 2026):**
A loop has three elements:
1. A program that issues prompts to an agent
2. A reader that checks the output
3. A decision gate that iterates or terminates

The loop is not the agent — it is the structure that contains the agent. Governance of the loop means governing: how many iterations are permitted, what "no progress" looks like, what the maximum cost ceiling is, and who can be notified when the loop terminates (normally or abnormally).

**The cost shift:**
Writing the agent skill (the "what to do") is a one-time cost. The loop is the ongoing operational cost. In agentic AI, the cost model is inverted from traditional software: the capability (the skill) is cheap; the execution (the loop) is expensive. Governance frameworks that treat agent deployment as the control point miss that the loop — not the skill — is where the actual cost and risk accumulate.

**Loop budget governance — required components:**

| Governance element | What it controls | Default if unset |
|---|---|---|
| **Max iterations** | How many times the loop can prompt the agent | Unbounded — will iterate until task complete or token limit |
| **No-progress detection** | Whether successive outputs are advancing toward the goal | None — loop can cycle forever on the same step |
| **Cost ceiling** | Maximum spend per loop invocation | None — runaway loops can accumulate significant API cost |
| **Timeout** | Maximum wall-clock time for the loop | None |
| **Human escalation trigger** | When the loop is stuck, who gets notified | Fails silently or exits with error |
| **Audit trail** | Each iteration logged with input, output, decision | Often absent by default |

**The harness connection:**
Loop budget governance is a harness design dimension — it must be part of the harness template (see [[harness-design-standard-framework]]). A harness that specifies permitted tools and data scope but does not specify loop governance is incomplete. EA governance review should include loop budget review as a required component for any agentic use case.

**Skills are the asset; loops are the plumbing:**
The strategic implication: Belron should invest in building reusable skills (the domain knowledge encoded in what the agent does) — these are the durable asset. Loops are infrastructure. Governance of loops is housekeeping that prevents the infrastructure from becoming a liability.

**Evidence:**
- [[braindump-2026-06-14-1937-wtf-is-a-loop]] — Boris Cherny definition: "a loop is a program that prompts an agent, reads output, decides if done, iterates." Five-stage lineage. Skills as asset; loops as plumbing.
- [[braindump-2026-06-14-1937-wtf-is-a-loop]] — Cost shift: "writing code is free; managing the loop is expensive"
- [[harness-design-standard-framework]] — Loop budget as the missing harness dimension

**How to apply:** When approving any agentic workflow for production, require a loop specification alongside the harness specification: max iterations, no-progress detection, cost ceiling, timeout, and escalation path. If any are absent, send back to the team to specify them.

**Confidence:** High — Boris Cherny's definition is authoritative; the loop budget governance extensions are EA synthesis of that pattern

---

### Principle 11: The Agent Paradigm Has Split — Governance Must Cover Persistent Agents, Not Just Session-Based Ones

**Statement:** Enterprise agentic governance to date has been designed around the session-based model: request → tool call → response → audit log, with state discarded when the session ends. A second category is now production-grade: the **persistent agent** — one that lives on a server, remembers across sessions, writes its own skill files, runs autonomously overnight, and is reachable from any device. A persistent agent that accumulates memory and self-authored capability over months is a structurally different governance challenge. Any Belron governance framework, and any vendor evaluation (Noma, Microsoft Agent 365, Okta), must state explicitly whether it governs both categories or only the session model.

**The split (June 2026):**

| | Session-based agent | Persistent agent |
|---|---|---|
| **Examples** | Claude Code, Cursor, Codex | Hermes Agent (Nous Research) |
| **State** | Discarded at session end | Retained across sessions / months |
| **Capability growth** | Fixed per session | Self-accumulating (writes its own skill files) |
| **Governance concern** | Per-call access + audit | All of that + memory retention, drift, undocumented capability expansion |
| **Best for** | Focused work in a known context | Research, scheduling, long autonomous runs, cross-day memory |

**Agent-identity documents are a governance artefact.** Both categories now define a durable identity file — CLAUDE.md for Claude Code, SOUL.md for Hermes — that persists across sessions and encodes the agent's character, constraints, and safety rules (e.g. "never send money without explicit confirmation"). These are converging on the same idea: **the agent identity document**. Governance is not just OAuth tokens and API keys; it must cover the identity files that define what an agent will and will not do. EA governance should require an approved, version-controlled identity document as a standard artefact for any governed agent — session or persistent.

**Accumulated skill files cut both ways.** A persistent agent's self-written skill library (procedure, pitfalls, verification steps) is either a compliance *asset* (an auditable record of what the agent learned to do) or a compliance *risk* (undocumented capability expansion), depending entirely on whether the governance framework versions and reviews it. Treat the skill library as an auditable surface, not background state.

**Memory retention is now a first-class harness dimension.** Principle 8's harness checklist already lists "Memory: what does the agent retain, how long, who can see it?" — for persistent agents this moves from a nice-to-have to the central control. Months of accumulated memory over Belron-confidential data is a data-retention and IPO-due-diligence question, not just a technical one.

**Model-agnostic by design is now a risk-mitigation requirement.** Hermes's model-swappable architecture (and the "local models as insurance" practitioner response to the Fable 5 ban) validates the principle: the durable asset is the agent framework + accumulated skills, not the model. This reinforces the [[ai-sovereignty-framework]] and directly informs the [[ai-damage-assessment-strategy-framework|AIDA PoC]] — build the model-agnostic abstraction layer as a requirement, not just a benchmark convenience.

**Evidence:**
- [[braindump-2026-06-21-1209-hermes-agent-persistent-agentic-platform]] — the session vs persistent split; SOUL.md / CLAUDE.md convergence; skill-file accumulation as compound interest and as an audit surface; model-agnostic architecture as insurance
- [[harness-design-standard-framework]] — memory as a harness dimension
- [[ai-sovereignty-framework]] — model as commodity; framework + skills as the durable asset

**How to apply:** When scoping MCP Governance vendor capability, add an explicit column: "governs persistent agents (memory, self-authored skills) — yes/no?" Require an approved agent-identity document (CLAUDE.md / SOUL.md-equivalent) for any governed agent. For persistent agents specifically, add memory-retention policy and skill-library review to the harness approval gate.

**Confidence:** High on the category split and the identity-document point; Medium on Belron applicability (no confirmed persistent-agent deployment at Belron yet — this is a watch-and-prepare principle).

---

### Principle 12: Knowledge Quality Is the Upstream Gate on Agent Trust — "RAG-Ready" Is a Governance Standard

**Statement:** An agent is only as trustworthy as the knowledge behind it. A machine-readable, "RAG-ready" knowledge base (consistent structure, chunking, metadata, provenance, freshness) is not content-ops housekeeping — it is a precondition for reliable agentic answers, and therefore a governance artefact. This is the same lesson as Principle 9 (semantic governance) viewed from the content side: Principle 9 governs what data *means*; this principle governs whether the knowledge is *structured well enough for an agent to consume at all*.

**Why it is a governance concern, not just a KB concern:** if knowledge documents feed agentic AI (CCOTF contact-centre agents answering from a knowledge base, for example), then their structure, provenance, and freshness determine whether the agent gives a correct, auditable answer. That makes a "RAG-ready / machine-readable knowledge document standard" a shared dependency between CCOTF and MCP Governance, and a natural bridge between them.

**Draft criteria for "RAG-ready" (to be firmed up with the AI team):** explicit structure and sensible chunk boundaries; rich metadata (owner, topic, audience, effective date); provenance (source of record, last-reviewed); freshness signals (review cadence, expiry); and unambiguous, self-contained passages that don't rely on surrounding page context.

**Evidence:**
- [[braindump-2026-07-08-1608-ccotf-knowledge-base-voc]] — "RAG-ready" and "machine-readable knowledge document standards for agentic AI" as the precondition for a knowledge-driven contact centre; "agents are only as good as the data and metadata behind them"
- [[llm-wiki-knowledge-infrastructure-framework]] — maintained-knowledge vs RAG debate; the knowledge-infrastructure substrate
- [[ccotf-technology-architecture-framework]] — the KB reference architecture as a CCOTF component

**How to apply:** When any agentic use case depends on a knowledge base, require a knowledge-readiness assessment against the RAG-ready criteria as part of the harness approval — treat an un-assessed KB the same way you'd treat an un-scoped API key. Define the standard once (with the AI team) and reuse it across CCOTF, AIDA, and future agent use cases.

**Confidence:** High on the principle; the specific RAG-ready criteria are a working draft pending AI-team input.

---

## Related Frameworks

- [[ea-effectiveness-framework]] — Principle 2: The MCP/A2A briefing is a dual-purpose artefact (governance tool + visibility instrument)
- [[belron-business-understanding-framework]] — Layer 4 (Systems Landscape) identifies which systems are MCP server candidates
- [[ai-damage-assessment-strategy-framework]] — The damage assessment workflow is a candidate A2A multi-agent pipeline
- [[harness-design-standard-framework]] — The harness as the unit of governance (Principle 8 detail)
- [[ai-sovereignty-framework]] — Governance stack sovereignty assessment; avoiding vendor lock-in at the governance layer

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

### June 14–19, 2026: Loop Governance + Four-Layer Stack + Sovereignty Dimension

**What Changed:** Three additions that extend the framework from harness-level to loop-level, and add a sovereign AI dimension:

**1. Agentic loop governance (June 14, 2026)**
Boris Cherny's "WTF Is a Loop" articulation crystallised the loop as the unit of agentic work — distinct from the agent skill, from the harness, and from the MCP server. Governance frameworks that stop at harness design leave loop-level risk unaddressed: unbounded iteration, cost runaway, no-progress cycling. Principle 10 added to address this.

**2. Four-layer governance stack confirmed (June 12–16, 2026)**
Three new vendor capabilities confirmed: Composio (execution/auth, 1000+ integrations, GA), Microsoft Agent 365 (fleet control, GA May 1), Okta MCP Server with Elicitation API (identity/auth, GA April 30). Together with Noma (enforcement) and Docker MCP Toolbox (packaging), these form a complete four-layer defence-in-depth governance stack. Principle 8 updated with the expanded table and Composio self-registration risk pattern.

**3. Sovereign AI as governance dimension (June 12, 2026)**
Kekst LTW 2026 confirmed AI sovereignty is entering IPO prospectuses as a risk factor. Governance frameworks must themselves be sovereignty-assessed — vendor lock-in at the governance layer is especially dangerous. New framework created: [[ai-sovereignty-framework]].

**Sources:** [[braindump-2026-06-14-1937-wtf-is-a-loop]], [[braindump-2026-06-12-1235-microsoft-agent-365]], [[braindump-2026-06-13-1517-composio-agent-infrastructure]], [[braindump-2026-06-16-1355-okta-mcp-agent-support]], [[braindump-2026-06-12-1336-kekst-cnc-ltw-2026-sovereignty-capital]]

---

### June 21 – July 18, 2026: Persistent-Agent Category + Knowledge-Readiness Gate

**What Changed:** Two additions that extend governance scope in new directions — one into a new agent category, one upstream into knowledge quality:

**1. The persistent-agent category is now real (June 21, 2026).**
Hermes Agent (Nous Research, MIT-licensed) crystallised a structural split: session-based agents (Claude Code, Cursor, Codex) vs persistent agents (server-resident, cross-session memory, self-authored skill files, autonomous overnight runs). Existing governance and vendor evaluations assume the session model. Principle 11 added to cover persistent agents, and to establish the agent-identity document (CLAUDE.md / SOUL.md) as a required governance artefact. Also reinforced model-agnostic-by-design as a risk-mitigation requirement for the AIDA PoC.

**2. Knowledge quality identified as the upstream gate on agent trust (July 8, 2026).**
CCOTF knowledge-base work surfaced "RAG-ready / machine-readable knowledge document standards for agentic AI" as the precondition for a knowledge-driven contact centre. Principle 12 added: knowledge readiness is a governance artefact and a shared CCOTF ↔ MCP Governance dependency. This is Principle 9 (semantic governance) viewed from the content side.

**Sources:** [[braindump-2026-06-21-1209-hermes-agent-persistent-agentic-platform]], [[braindump-2026-07-08-1608-ccotf-knowledge-base-voc]]

---

*Consolidated from 45 sources | First version: April 10, 2026 | Last updated: July 18, 2026 | Status: Working (Principles 1–9 solid; Principles 10–12 Emerging)*
