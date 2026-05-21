---
type: "braindump"
domain: "professional"
date: "2026-05-21"
created: "2026-05-21 17:00"
themes: ["semantic-layer", "ai-governance", "multi-agent-systems", "enterprise-data-architecture", "operational-governance"]
tags: ["#braindump", "#semantic-layer", "#ai-governance", "#enterprise-architecture", "#multi-agent"]
status: "captured"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
source: "linkedin"
source_url: "https://www.linkedin.com/posts/darlenenewman_most-people-think-the-semantic-layer-is-a-share-7463194457618886658-P2ef"
source_author: "Darlene Newman"
---

# Braindump: The Semantic Layer Is Governance Infrastructure, Not Technology

## Raw Thoughts

*(Source: LinkedIn post by Darlene Newman, 21 May 2026)*

> "Most people think the semantic layer is a tool you buy. The tooling? Sure. But the meaning… nope. It isn't one thing, and nobody can sell it to you."

Newman's post argues that the semantic layer cannot be purchased — only the tooling sitting on top of it can. The *meaning* — the shared business definitions, controlled vocabulary, and consistent interpretation of concepts — has to be defined and owned by the organisation itself.

She maps it across five workflow stages:

1. **Ask** — Define competency questions and system requirements
2. **Understand** — Establish controlled vocabulary for shared meaning
3. **Retrieve** — Access documents, operational data, and relationship context
4. **Evaluate** — Apply explicit rules and ontology-driven logic (not LLM inference)
5. **Output** — Deliver consistent decisions across systems

Her key governance challenge: without a shared semantic layer, separate AI agents running in parallel create *"parallel realities"* — each agent independently interprets the same business term (revenue, customer, active account, case closed) and arrives at different answers. The inconsistency isn't a data quality problem; it's a *meaning governance* problem.

Commenter Glenn Hutchinson reinforced this: "The tooling can be bought, but the meaning has to be owned and maintained."

Commenter Joseph B. extended the scope: semantic layers constitute an operational governance problem, not just a data problem — requiring explicit definitions and process-state awareness.

> **Note on images:** LinkedIn post included visual diagrams (likely a 5-stage lifecycle graphic and/or an agent interaction model). These could not be retrieved via web fetch — add manually from the original post if needed. [View original post](https://www.linkedin.com/posts/darlenenewman_most-people-think-the-semantic-layer-is-a-share-7463194457618886658-P2ef)

---

## Content Analysis

### Main Themes

1. **The semantic layer is organisational, not technical** — You can buy dbt, Atlan, Collibra, or a graph database. You cannot buy the shared understanding of what "customer" means across your opcos. That has to be built, governed, and maintained by the business.

2. **Multi-agent systems amplify semantic inconsistency** — A single agent making a mistake is a bug. Ten agents each making different-but-internally-consistent mistakes is a governance failure. As Belron's agent landscape grows (Copilot, MCP-connected agents, bespoke automation), semantic drift becomes structural risk.

3. **Evaluate stage: explicit rules beat LLM inference** — Newman specifically calls out that the Evaluate stage should use explicit ontology-driven logic, not LLM reasoning. This is a significant architectural choice — it argues for rule-based evaluation engines layered *over* LLM retrieval, not instead of it.

4. **Semantic consistency = operational governance infrastructure** — Newman and her commenters are clear: this is an ops problem, not a data problem. The right owner is governance, not the data team.

### Supporting Ideas

- Controlled vocabulary is the output of the Understand stage — this is the canonical definition layer that all agents must resolve against
- Process-state awareness is a component of semantic consistency: "case closed" means something different in a booking system vs. a complaints system vs. a legal system
- The Ask stage (defining competency questions) is often skipped — organisations deploy agents before they've articulated what questions the agents are answering
- The gap between "the tooling" and "the meaning" is exactly where most enterprise AI deployments stall

### Questions Raised

- Does Belron have a controlled vocabulary or enterprise ontology today? (Likely partial — probably exists in some opcos but not unified)
- Who *owns* semantic consistency at Belron? Data team? EA? CIO?
- Which AI agents currently running at Belron are operating with inconsistent semantic definitions?
- How does the semantic layer intersect with MCP governance? If MCP tools expose data, which semantic layer governs what the data means?
- Is the Evaluate stage (explicit rules > inference) compatible with how current Copilot agents are built? Or are they doing pure LLM inference all the way through?

### Decisions Contemplated

- Whether semantic governance should be explicitly scoped into the MCP Governance project — or should sit as a separate EA initiative
- Whether to recommend a controlled vocabulary / enterprise ontology workstream as part of the Belron AI governance programme
- Whether to raise the "Evaluate stage = explicit rules" principle as an architectural standard for Belron agent builds

---

## Strategic Intelligence

### Key Insights

1. **Semantic governance is the missing layer in Belron's AI governance framework.** MCP Governance currently covers toolchain security, access control, and deployment standards. It doesn't cover *meaning* — what the data returned by tools actually means. Newman's framework suggests this is a separate, equally important layer.

2. **The parallel realities risk is real and growing.** Belron runs multiple opcos, each with their own definitions of common business objects (job, customer, technician, SLA). As AI agents are deployed across these opcos — or at group level pulling from multiple opcos — semantic inconsistency will produce divergent outputs that are each internally defensible. That's harder to detect than a data error.

3. **"Evaluate = explicit rules" is an architectural standard worth adopting.** If agents are allowed to infer evaluation criteria from context, the results are non-deterministic. Building a governed rule layer for the Evaluate stage — owned by the business, not the model — produces auditable, consistent outputs.

### Pattern Recognition

- **Connection to MCP Governance:** MCP tools expose data to agents. If those tools return data without semantic context (e.g., `job_status: 3` with no ontology), each agent will interpret it independently. Semantic governance is the upstream dependency for meaningful MCP tool output.
- **Connection to M365 Copilot Notebooks braindump:** Copilot agents across BizChat, Loop, and Teams each operate in different data contexts. Without a shared semantic layer, the same question asked in different Copilot surfaces may return different answers — not because the data is different, but because the interpretation is. See [[braindump-2026-05-20-1352-copilot-365-notebooks-data-placement]].
- **Connection to Contact Centre of the Future:** In a contact centre with AI agent assist, live call transcription, and post-call analytics, "escalation", "resolution", "customer satisfaction" are terms that multiple systems will interpret. Inconsistent definitions produce inconsistent agent coaching, inconsistent SLA reporting, and inconsistent customer experience measurement.
- **Recurring pattern:** Every AI governance challenge Belron faces eventually traces back to *who owns the meaning of data*, not just who owns the data. Data mesh principles handle ownership; semantic governance handles meaning.

### Strategic Implications

- EA should position semantic governance as a first-class programme — parallel to, and upstream of, agent deployment
- The MCP Governance project scope should explicitly include: "What does the data returned by MCP tools mean?" — not just "who can call which tool"
- The architecture principle "Evaluate with explicit rules, not inference" should be proposed as a Belron AI architecture standard
- A lightweight enterprise ontology effort — starting with the top 20 business objects that appear across multiple agent use cases — would be a pragmatic entry point

---

## Action Items

### Immediate (This week)
- [ ] Add semantic governance as an open question in the MCP Governance project 📅 2026-05-23
- [ ] Note the "Evaluate = explicit rules" principle in the Contact Centre of the Future architecture notes 📅 2026-05-23

### Short-term (2 weeks)
- [ ] Draft a one-page framing document: "Semantic Governance as Enterprise Infrastructure" — what it is, why it matters, who owns it 📅 2026-06-04
- [ ] Identify whether Belron has any existing enterprise ontology or controlled vocabulary work (check with data architecture team) 📅 2026-06-04

### Strategic Considerations
- Semantic governance programme could be scoped as a Belron EA initiative in H2 2026 — timing aligns with increased AI agent deployment across opcos
- The right stakeholder is likely the CDO or Data Governance lead, not the IT team — this is a business definitions problem
- Starting with a controlled vocabulary for 20-30 core business objects (job, customer, technician, SLA, case, resolution, escalation, calibration) would demonstrate value before committing to a full ontology programme

---

## Connections
- **Related Braindumps:** [[braindump-2026-05-20-1352-copilot-365-notebooks-data-placement]]
- **Relevant Projects:** [[04-projects/mcp-governance/PROJECT-OVERVIEW|MCP Governance]], [[04-projects/contact-centre-future/PROJECT-OVERVIEW|Contact Centre of the Future]]
- **Knowledge Base:** [[05-knowledge/research/2026-05-21-zero-copy-architecture|Zero Copy Architecture Research]] *(tangential — data-at-rest governance)*

---

## Domain Classification
- **Primary Domain:** Professional (95%)
- **Reasoning:** Enterprise AI governance, EA programme framing, Belron-specific strategic implications
- **Cross-Domain Elements:** None
- **Privacy Level:** Public (source is a public LinkedIn post)

---

## Processing Notes

### Source Context
- Darlene Newman is a knowledge graph and ontology practitioner — her framing comes from a semantic web / ontology background, not a data engineering background. The "Evaluate = explicit rules" recommendation reflects ontology best practice, not necessarily a general enterprise AI standard. Apply with that lens.
- The 5-stage framework (Ask → Understand → Retrieve → Evaluate → Output) is her original framework, not an industry standard. It's useful as a thinking tool; don't treat it as a canonical reference without noting the source.

### Confidence Assessment
- **Overall Analysis:** 90% — post content is clear and well-argued; Belron implications are interpretive but well-grounded
- **Domain Classification:** 95% — clearly professional EA territory
- **Strategic Insights:** 85% — the MCP Governance connection is strong; the Contact Centre connection is directional
- **Areas Requiring Clarification:** Whether Belron already has an enterprise ontology programme underway (would change priority of action items)

---

*Processed by COG Brain Dump Analyst*
