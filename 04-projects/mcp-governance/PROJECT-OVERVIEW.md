---
type: project-overview
project: MCP Governance
slug: mcp-governance
created: 2026-04-25
status: active
tags: ["#project", "#overview", "#mcp", "#enterprise-architecture", "#governance", "#agentic-ai"]
---

# MCP Governance

## What is this project?
Enterprise Architecture ownership of the Model Context Protocol (MCP) standard at Belron. MCP was donated by Anthropic to the Linux Foundation and is becoming the de facto integration protocol for agentic AI systems. This project covers policy, vendor integration standards, internal adoption governance, and Belron's strategic positioning on the standard.

## Strategic Framing — The Harness Model

*Added 2026-06-11. Source: [[03-professional/braindumps/braindump-2026-06-11-0938-harnesses-agentic-ai|Harnesses in Agentic AI braindump]]*

The governance problem is a **harness design problem**. The right unit of governance is not the model, not the individual MCP tool, and not "AI" in the abstract — it is the **harness**: the configured execution context that wraps a model and defines its permissions, tools, triggers, memory, and audit trail.

This reframes the project scope:

> *Instead of "how do we govern MCP servers?", the question is: "how do we establish enterprise harness design standards, with MCP as the primary harness interface protocol?"*

**What a harness is:**
- The scaffolding/execution layer between user intent and model action
- Encodes which tools the agent can access, what data it can see, when it can act, and how it is audited
- MCP servers are harness *components*; MCP tools are *permitted actions* within the harness; the server manifest is the harness *configuration*

**Why EA owns this:**
If EA doesn't define harness design standards, teams will build their own harnesses with their own implicit governance decisions. Shadow AI proliferates at the harness layer, not just the prompt layer.

**Vendor lens:**
Every agentic AI product is a harness with a model inside — Firemind, Noma, Linx Security, Claude Managed Agents, Azure AI Foundry. When evaluating vendors, evaluate the harness first: what does it expose, restrict, and audit? Model choice is secondary.

---

## Background
- MCP is the emerging standard for connecting AI agents to tools, data sources, and services
- Anthropic donated it to the Linux Foundation — now vendor-neutral
- All major AI vendors (OpenAI, Google, Microsoft) have adopted or are adopting it
- Armo has EA governance ownership at Belron

## Scope
- Define Belron's MCP adoption policy
- Govern which internal systems expose MCP servers
- Evaluate vendor MCP implementations (Snowflake, SAP, Salesforce, etc.)
- Establish security and accountability standards for agentic AI interactions over MCP
- Connect to broader agentic AI governance framework

## Key Risks
- Agentic AI accountability — who is responsible when an autonomous agent takes a commercial action via MCP?
- Security — MCP servers as attack surface (see CrabTrap, Brex open-source proxy pattern)
- Vendor lock-in risk if MCP implementations diverge

## Current Status
*Governance framework definition phase.*

## Project Resources
- [[braindumps/|Project Braindumps]]
- [[competitive/|Competitive Intelligence]]
- [[planning/|Planning Documents]]
- [[resources/|Resources]]

## Next Steps
- [ ] Draft a one-page "Harness Design Standard" — define what a harness is, what components it must have (permissions, tools, triggers, memory scope, audit trail), and who owns each component in a Belron context 📅 2026-06-18
- [ ] Draft Belron MCP adoption policy v0.1
- [ ] Map existing Belron systems as candidate MCP server candidates
- [ ] Review Linux Foundation MCP governance docs
- [ ] Put together a reference architecture for MCP / Agentic AI
- [ ] Assess Firemind's default-deny harness model as a governance reference — see [[05-knowledge/booklets/tools/firemind-ai-it-operations-2026-06-11]]

## Open Questions
- **Semantic governance:** MCP tools return data to agents — but what does that data *mean*? Each agent may interpret the same field differently without a shared semantic layer. Semantic governance (controlled vocabulary, ontology-driven evaluation) is a dependency for meaningful MCP tool output. Needs scoping: is this in MCP Governance or a separate EA initiative? See [[03-professional/braindumps/braindump-2026-05-21-1700-semantic-layer-governance-newman|Semantic Layer Governance braindump]].

---

*Part of Belron EA portfolio. Owner: Armo.*
