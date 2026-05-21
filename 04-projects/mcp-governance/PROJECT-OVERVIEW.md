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
- [ ] Draft Belron MCP adoption policy v0.1
- [ ] Map existing Belron systems as candidate MCP server candidates
- [ ] Review Linux Foundation MCP governance docs

## Open Questions
- **Semantic governance:** MCP tools return data to agents — but what does that data *mean*? Each agent may interpret the same field differently without a shared semantic layer. Semantic governance (controlled vocabulary, ontology-driven evaluation) is a dependency for meaningful MCP tool output. Needs scoping: is this in MCP Governance or a separate EA initiative? See [[03-professional/braindumps/braindump-2026-05-21-1700-semantic-layer-governance-newman|Semantic Layer Governance braindump]].

---

*Part of Belron EA portfolio. Owner: Armo.*
