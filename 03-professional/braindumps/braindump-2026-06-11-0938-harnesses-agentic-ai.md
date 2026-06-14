---
type: "braindump"
domain: "professional"
date: "2026-06-11"
created: "2026-06-11 09:38"
themes: ["agentic-ai", "harnesses", "governance", "mcp", "enterprise-architecture"]
tags: ["#braindump", "#agentic-ai", "#harness", "#governance", "#mcp", "#enterprise-architecture"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-06-14]]"
consolidated_date: "2026-06-14"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: Harnesses in the Context of Agentic AI

## Raw Thoughts

Harnesses in the context of agentic AI.

---

## Content Analysis

### Main Themes

1. **The harness as the governance unit** — When people talk about governing AI agents, they're actually talking about harness design. The model itself (Claude, GPT-5.5, Gemini) is not what gets governed. What gets governed is the harness around it: what it can see, what it can do, when it can act, and who can change those constraints.

2. **Harnesses are not new — they're just newly visible** — Every enterprise system has a harness: the integration layer, the orchestration middleware, the IAM policy. Agentic AI makes the harness conceptually explicit in a way traditional software didn't require, because the agent can reason about and potentially attempt to circumvent its own constraints. The harness has to be intentional.

3. **The MCP Governance problem is a harness design problem** — MCP servers are harness components. The question "how do we govern MCP at Belron?" is really: who controls which harnesses exist, what tools each harness exposes, and what actions agents within those harnesses can take.

### Supporting Ideas

- Claude Code (what I'm using right now) has a harness: `CLAUDE.md`, hooks, skills, permissions settings, allowed/blocked tool lists. The harness file says "the harness executes these, not Claude" — that's the clearest articulation of the concept I've seen.
- Firemind is a harness product. They've built a production harness for Claude that runs IT operations. Their "default-deny security model" is a harness constraint. Their credential vaults are a harness capability.
- Claude Managed Agents (released June 9) adds cron scheduling and credential vaults to the Claude platform harness. Anthropic is building harness infrastructure into the platform layer.
- Noma and Linx Security (both in MCP Governance watchlist) are harness governance tools — they don't change what agents can do, they monitor and enforce harness constraints at runtime.
- MCP is effectively a harness *standard* — a protocol for defining what a harness can expose to an agent. The Linux Foundation AAIF is standardising harness interoperability.

### Questions Raised

- Is "harness" the right word to use in Belron governance conversations? It's a developer term. The business equivalent might be "agent operating model" or "agent policy layer." What's the right vocabulary for a non-technical stakeholder?
- Who owns the harness in an enterprise? EA? IT Security? The product team that built the use case? Platform/Cloud ops? This ownership question is the crux of the MCP Governance project.
- Can a harness be governed independently of the model it wraps? I.e., is Belron's MCP Governance framework model-agnostic? It should be — the harness is what matters, not which LLM sits inside it.
- At what layer does the harness live in a reference architecture? It sits between the orchestration layer and the model API. But in multi-agent systems it gets recursive: agent A's harness might include agent B as a tool, and agent B has its own harness. This is the governance recursion problem.

### Decisions Contemplated

- Whether to use "harness" as the central organising concept in MCP Governance documentation — or to translate it into EA/TOGAF language.
- Whether Belron needs to build or buy harness infrastructure, or whether platform capabilities (Claude Managed Agents, Azure AI Foundry, AWS Bedrock) are now sufficient.

---

## Strategic Intelligence

### Key Insights

1. **The harness is the right unit of governance — not the model, not the tool, not the agent.** Governing "AI" in enterprise is too abstract. Governing "Claude" is vendor-specific. Governing individual MCP servers is too granular. The harness — the configured execution context that wraps a model and defines its permissions, tools, triggers, memory, and audit trail — is the right level of abstraction. EA should own the harness design standards; individual teams own their harness instances within those standards.

2. **Every agentic AI product is a harness with a model inside.** Firemind = harness for IT ops + Claude. Noma = harness monitoring layer. Claude Code = developer harness + Claude. Claude Managed Agents = platform harness + Claude. The business decision is not "which AI model?" but "which harness pattern fits this use case, and do we build or buy it?" The model is relatively commoditised; the harness is the differentiation.

3. **Harness design encodes your governance decisions.** Permissions, allowed tools, data scope, escalation paths, audit logging — these are not afterthoughts to harness design, they *are* harness design. If EA doesn't define harness standards, teams will build their own harnesses with their own implicit governance decisions. That's how shadow AI proliferates at the harness layer, not just the prompt layer.

4. **The AI Damage Assessment PoC needs a harness design, not just a model choice.** The current PoC thinking is "which model analyses the image best?" The real design question is "what does the harness look like?" — what receives the image, routes it to the model, handles confidence thresholds, routes low-confidence results to human review, returns structured output, and maintains an audit trail for insurance compliance. Choosing Claude Fable 5 vs GPT-5.5 is secondary to defining the harness architecture.

### Pattern Recognition

- **Connection to MCP Governance:** The entire MCP Governance framework maps onto harness design. MCP server = harness component. MCP tool = permitted action. Server manifest = harness configuration. The governance gap is the absence of an enterprise standard for harness design and ownership.
- **Connection to Firemind:** Firemind's value proposition is "we built a production harness so you don't have to." Their "Claude Enablement" service is essentially "let us run the harness in your cloud." The question for Belron is whether to buy Firemind's harness or build one — a classic build/buy decision framed in EA terms.
- **Recurring pattern:** Every agentic AI conversation eventually surfaces the same unspoken question: "but who controls what the agent can actually do?" That's the harness question. It keeps appearing because no one has named it clearly.

### Strategic Implications

- **MCP Governance framing shift:** Instead of framing the project as "how do we govern MCP servers?", reframe as "how do we establish enterprise harness design standards, with MCP as the primary harness interface protocol?" This is more strategic, more durable, and positions EA as the right owner.
- **PoC next step:** The benchmark tests (Fable 5 vs GPT-5.5) should be accompanied by a harness design sketch — even a one-page diagram showing the execution flow around the model. This makes the PoC architecture-grade, not just a proof of model capability.
- **Vendor evaluation lens:** When evaluating any agentic AI vendor (Firemind, Noma, Linx, AWS Bedrock), evaluate the harness first: what does it expose, what does it restrict, who can change it, and is it auditable? The model choice is secondary.

---

## Action Items

### Immediate (24-48 hours)
- [ ] Sketch a one-page harness architecture diagram for the AI Damage Assessment PoC — show the execution flow from image receipt → model → confidence gate → human review → output. 📅 2026-06-12

### Short-term (1-2 weeks)
- [ ] Draft a one-page "Harness Design Standard" framing note for the MCP Governance project — define what a harness is, what components it must have, and who owns each component in a Belron context. 📅 2026-06-18
- [ ] Revisit Firemind's architecture documentation through the harness lens — how have they structured their harness, and does their default-deny model translate into a governance pattern Belron could adopt? 📅 2026-06-18

### Strategic Considerations
- Consider whether "harness" needs to be translated into TOGAF/ArchiMate terms for EA documentation — possibly maps to an Application Service or Technology Component in the architecture model.
- The harness concept may be the right framing for the AI Summit London debrief, if governance conversations came up there — "we're not governing models, we're governing harnesses."

---

## Connections

- **Related Braindumps:** [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]], [[braindump-2026-04-09-1136-market-scan-machine-vision-frontend]]
- **Relevant Projects:** [[04-projects/mcp-governance/PROJECT-OVERVIEW]], [[04-projects/ai-damage-assessment-poc/PROJECT-OVERVIEW]]
- **Knowledge Base:** [[COMPETITIVE-WATCHLIST]] (Firemind, Noma, Linx Security)
- **Tools:** [[firemind-ai-it-operations-2026-06-11]]

---

## Domain Classification

- **Primary Domain:** Professional (95%)
- **Reasoning:** Core EA and governance concept with direct implications for two active Belron projects.
- **Cross-Domain Elements:** None — purely professional/strategic.
- **Privacy Level:** Professional (internal framing, no confidential data)

---

## Processing Notes

### Emotional Context

- **Energy Level:** Medium — calm, analytical. Post-Summit context.
- **Emotional Tone:** Curious — the harness concept is crystallising from several parallel threads (Firemind, Claude Managed Agents, MCP Governance, COG's own architecture).
- **Implications:** This is the kind of quiet conceptual consolidation that often precedes a stronger articulation. Worth developing further.

### Confidence Assessment

- **Overall Analysis:** 90% — the harness framing is well-evidenced across multiple parallel contexts.
- **Domain Classification:** 95% — clearly professional/strategic.
- **Strategic Insights:** 85% — the "harness as governance unit" insight is strong; the PoC harness design implication is high confidence. The TOGAF translation is speculative.
- **Areas Requiring Clarification:** How does "harness" map precisely to TOGAF/ArchiMate constructs? Is there existing industry terminology that's equivalent (orchestration layer, agent runtime, agent policy container)?

---

*Processed by COG Brain Dump Analyst*
