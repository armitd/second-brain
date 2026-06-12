---
type: "braindump"
domain: "project-specific"
project: "mcp-governance"
date: "2026-06-12"
created: "2026-06-12 12:35"
themes: ["microsoft-agent-365", "agent-governance", "ai-control-plane", "mcp-governance"]
tags: ["#braindump", "#raw-thoughts", "#microsoft", "#agent-governance", "#mcp-governance", "#ai-governance"]
status: "captured"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: Microsoft Agent 365 — Research

## Raw Thoughts
Find out about Microsoft Agent 365. Put into a braindump document.

---

## What Is Microsoft Agent 365?

**Microsoft Agent 365** (GA: 1 May 2026) is Microsoft's enterprise **control plane for AI agents** — a dedicated product for observing, governing, and securing an organisation's entire AI agent fleet. It sits above individual agent products (Copilot, custom agents, third-party agents) as the management and security layer.

Think of it as: *if agents are the new apps, Agent 365 is the new MDM/endpoint manager — but for AI agents.*

---

## The Three Pillars

### 1. Observe
- **Centralised agent registry** — every agent (Microsoft-built, custom, third-party) visible in one place via M365 Admin Center
- **Agent Map** — visual topology showing agent relationships, device locations, associated identities, cloud resource access
- **Registry sync** — connect external platforms (Salesforce Agentforce, Databricks Genie confirmed May 2026; AWS Bedrock and Google Cloud in public preview) to bring non-Microsoft agents into the same registry
- **Shadow AI discovery** — finds unsanctioned agents running on local devices and cloud platforms
- **Real-time dashboards** — total agents, active users, growth trends, connected platforms, runtime hours, risk signals

### 2. Govern
- Lifecycle management (deploy, update, retire) via M365 Admin Center
- **Microsoft Entra** — consistent risk-based access control for users and agents acting on their behalf
- **Microsoft Purview** — information protection, DLP, compliance policies applied to agent data access
- Policy-based guardrails for agent behaviour
- Audit-ready posture built in

### 3. Secure
- **Microsoft Defender** — continuous threat detection, real-time runtime blocking of unsafe/malicious agent behaviour
- **Microsoft Intune** — policy deployment across managed devices for agent workloads
- Detection of **prompt injection**, data exfiltration, scope violations
- Protection against unsanctioned AI usage and risky file movement
- *Context mapping + runtime blocking via Intune/Defender* — public preview June 2026

---

## Licensing

| Option | Price |
|--------|-------|
| Standalone | **$15 per user per month** |
| Bundled | Included in **Microsoft 365 E7** |

- Works best with **Microsoft E5** as prerequisite
- At least one user needs a qualifying Agent 365 licence to enable the product
- Covers users who manage/sponsor agents or use delegated agent services

---

## Ecosystem Integrations

**Third-party agent platforms (registry sync):**
- Salesforce Agentforce ✅ (GA, May 2026)
- Databricks Genie ✅ (GA, May 2026)
- AWS Bedrock agent discovery (public preview)
- Google Cloud (public preview)
- Microsoft Foundry agents

**Agent launch partners (pre-integrated):**
Genspark, Zensai, Egnyte, Zendesk, Kore.ai, Kasisto, n8n, and others — fully configured, no IT integration work needed

**Notable discovery targets:**
- OpenClaw, GitHub Copilot CLI, **Claude Code** ← Agent 365 can discover and inventory Claude Code sessions

**Services partners:** Accenture, Capgemini, KPMG, Deloitte, EY, PwC (governance enablement workshops, managed services)

**Windows 365 for Agents:** Secured, managed compute environment specifically designed for agentic workloads (US public preview)

---

## Content Analysis

### Main Themes
1. **Microsoft is productising the agent governance problem** — the exact problem the MCP Governance project is architecting, now available as a commercial product within the Microsoft stack
2. **Control plane framing** — Microsoft is positioning Agent 365 as infrastructure, not a feature. "Control plane" language matches EA/platform thinking
3. **Ecosystem reach is the differentiator** — registry sync means Agent 365 doesn't just govern Microsoft agents; it aims to be the governance layer for *all* enterprise agents (Salesforce, Databricks, AWS, Google)
4. **Claude Code is in scope** — Agent 365 can discover Claude Code sessions, making it directly relevant to Belron's own AI tooling decisions
5. **E7 bundle signals pricing direction** — M365 E7 is a new tier above E5; Agent 365 being included there suggests Microsoft expects this to become a standard enterprise capability, not a niche add-on

### Questions Raised
- Does Belron already have M365 E5 licensing? If so, what's the incremental cost to Agent 365?
- Does Agent 365 govern **MCP servers** specifically, or only higher-level agents? The docs don't mention MCP natively — this is the critical gap to investigate
- How does Agent 365 relate to **Noma** (already on watchlist as the specialist MCP governance vendor)? Are they complementary or competing?
- Would adopting Agent 365 reduce or replace the need for a bespoke MCP Governance framework at Belron?
- Is Agent 365 available in EU data residency configuration? (Critical given Belron's GDPR constraints across 35 countries)

### Decisions Contemplated
- **Adopt vs. architect** — should the MCP Governance project recommend Agent 365 as the tooling layer, or architect independently and treat Agent 365 as one input?
- **Noma vs. Agent 365** — which fills the MCP-specific governance gap better? Or is it a stack (Agent 365 for broad agent governance + Noma for MCP-specific runtime enforcement)?

## Strategic Intelligence

### Key Insights
1. **Microsoft has validated the market** — A standalone commercial product at $15/user/month from Microsoft confirms that enterprise agent governance is a solved-enough problem to productise. This strengthens the internal case for the MCP Governance project at Belron
2. **The MCP gap** — Agent 365 governs agents; it's less clear it governs the **MCP servers** (tools/connectors) those agents use. Noma explicitly addresses MCP server governance. These may be complementary layers, not alternatives
3. **Claude Code discovery** — Microsoft can see Claude Code usage. If Belron standardises on Agent 365 for agent governance, Claude Code becomes visible/governable. This is a positive for AI advocacy — Claude is not invisible to enterprise governance tooling
4. **Salesforce integration is significant** — Belron runs Salesforce Service Cloud + Marketing Cloud. Salesforce Agentforce + Agent 365 registry sync means Belron could have a unified view of Salesforce agents and Microsoft agents in one place. Important for CCOTF project
5. **E7 tier** — Microsoft is creating a new premium tier above E5. Watch whether Belron's Microsoft licensing strategy will track to E7 and whether Agent 365 becomes "free" in that context

### Pattern Recognition
- **Connection to Noma:** Noma (added to watchlist June 2026) focuses specifically on MCP server governance with runtime enforcement. Agent 365 focuses on agent fleet governance at a higher level. The two products appear to address different layers of the same stack — not competitors, but potential complements
- **Recurring theme:** Every major vendor (Microsoft, Salesforce, Google) is building agent governance as a platform play. The window to establish Belron's own governance framework before vendor lock-in is narrowing
- **Microsoft E5 → E7 pattern:** Similar to the E3 → E5 upsell cycle, Microsoft is using Agent 365 to drive E7 adoption. Belron should model this upgrade path now

### Strategic Implications
- **MCP Governance project:** Agent 365 should be evaluated as a candidate tooling layer. Get a demo. Specifically probe MCP server governance capabilities — if that gap exists, Noma fills it; if it doesn't, Agent 365 may be sufficient
- **Licensing conversation:** If Belron is M365 E5 today, the path to Agent 365 is $15/user/month or an E7 upgrade — needs commercial modelling
- **CCOTF intersection:** Salesforce Agentforce ↔ Agent 365 registry sync means the Contact Centre of the Future project now has a governance dimension to consider when speccing Agentforce deployments
- **AI advocacy:** Agent 365 discovering Claude Code sessions is a useful proof point — Claude operates within Microsoft's enterprise governance framework

## Action Items

### Immediate (24-48 hours)
- [ ] Check whether Belron's current Microsoft licensing is E3 or E5 (governs the Agent 365 cost/path) 📅 2026-06-13
- [ ] Read the [Microsoft Agent 365 licensing FAQ](https://www.microsoft.com/licensing/faqs/122) to understand per-user coverage model in detail 📅 2026-06-13

### Short-term (1-2 weeks)
- [ ] Request an Agent 365 demo from Microsoft (or Belron's Microsoft account team) — specifically probe MCP server governance capabilities 📅 2026-06-19
- [ ] Map Agent 365 capabilities against the MCP Governance framework currently being designed — where does it cover, where are the gaps? 📅 2026-06-19
- [ ] Raise Agent 365 in the next MCP Governance planning discussion as a potential tooling candidate 📅 2026-06-19
- [ ] Cross-reference Agent 365 vs. Noma — present a comparison for the MCP Governance architecture decision 📅 2026-06-26

### Strategic Considerations
- Monitor the Agent 365 public preview in June 2026 (context mapping + runtime blocking via Intune/Defender) — this could close the MCP server gap
- Track whether Microsoft E7 becomes part of Belron's licensing roadmap
- Consider whether a "Microsoft Agent 365 + Noma" stack (broad agent governance + MCP-specific enforcement) is the right architecture for Belron

## Connections
- **Related Braindumps:** [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]]
- **Relevant Projects:** [[04-projects/mcp-governance/PROJECT-OVERVIEW]], [[04-projects/contact-centre-future/PROJECT-OVERVIEW]]
- **Competitive Watchlist:** [[COMPETITIVE-WATCHLIST]] — Microsoft AI entry updated; Noma entry cross-referenced
- **Knowledge Base:** N/A yet

## Domain Classification
- **Primary Domain:** Project-specific — MCP Governance (85%)
- **Secondary Domain:** Professional — AI governance market landscape (15%)
- **Cross-Domain Elements:** CCOTF (Salesforce Agentforce + Agent 365 sync), AI Damage Assessment PoC (Claude Code discoverability), AI advocacy (Claude in Microsoft governance scope)
- **Privacy Level:** professional

## Processing Notes

### Emotional Context
- **Energy Level:** Medium — research task, high relevance
- **Emotional Tone:** Curious — significant product, multiple project implications

### Confidence Assessment
- **Overall Analysis:** 92% — sourced from Microsoft Learn, Microsoft Security Blog, verified GA status
- **Domain Classification:** 90% — clearly MCP Governance primary
- **Strategic Insights:** 85% — MCP gap assessment is inferred (docs don't explicitly address MCP servers); needs confirmation via demo
- **Areas Requiring Clarification:** Whether Agent 365 governs MCP servers natively vs. only higher-level agent constructs

---

**Sources:**
- [Microsoft Agent 365 overview — Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-agent-365/overview)
- [Microsoft Agent 365 GA announcement — Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)
- [What's New in Agent 365: May 2026 — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/agent-365-blog/what%E2%80%99s-new-in-agent-365-may-2026/4516340)
- [Microsoft Agent 365: The Control Plane for Agents](https://www.microsoft.com/en-us/microsoft-agent-365)
- [star-knowledge.com: Microsoft Agent 365 Features & Benefits](https://star-knowledge.com/blog/microsoft-agent-365-explained-features-benefits/)

---

*Processed by COG Brain Dump Analyst*
