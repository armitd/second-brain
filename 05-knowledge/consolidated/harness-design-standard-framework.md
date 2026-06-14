---
type: "consolidated-knowledge"
domain: "professional"
framework: "harness-design-standard"
created: "2026-06-14"
last_updated: "2026-06-14"
consolidation_id: "consolidation-2026-06-14"
source_documents: 6
status: "emerging"
tags: ["#framework", "#consolidated", "#agentic-ai", "#harness", "#governance", "#mcp", "#enterprise-architecture"]
---

# Harness Design Standard Framework

## Framework Overview

A harness is the configured execution context that wraps an AI model and defines what it can see, what it can do, when it can act, and who can change those constraints. This framework establishes the harness — not the model, not individual MCP servers, not the agent use case — as the right unit of enterprise AI governance.

**Status:** Emerging (concept is well-evidenced; enterprise standard not yet drafted or socialised)
**Last Updated:** 2026-06-14
**Source Insights:** 6 documents — [[braindump-2026-06-11-0938-harnesses-agentic-ai]], [[braindump-2026-06-04-1710-mcp-ref-architecture-simplified-diagram]], [[braindump-2026-05-11-1200-getting-belron-onto-anthropic]], [[05-knowledge/consolidated/agentic-ai-governance-framework]], [[05-knowledge/consolidated/architecture-operating-model-framework]], [[daily-brief-2026-06-09]]

---

## Why the Harness Is the Right Unit of Governance

**Governing "AI"** is too abstract — you can't write a policy for "AI."

**Governing a specific model** (Claude, GPT-5.5, Gemini) is vendor-specific and unstable — models change, get replaced, and are rarely the actual risk.

**Governing individual MCP servers** is too granular — you end up with a catalogue of approved tools but no coherent view of what an agent can actually do when it combines them.

**The harness** is the right level: it is the complete, bounded execution context — the configured package of model + permissions + tools + memory + triggers + audit trail. This is what teams actually build and deploy. This is what governance can usefully constrain.

---

## Core Principles

### Principle 1: Every Agentic AI Product Is a Harness with a Model Inside

**Statement:** The right mental model for any AI agent or agentic product is: harness + model. The model provides reasoning; the harness defines what it can act on and what it cannot. The business decision is not "which AI model?" but "which harness pattern fits this use case, and do we build or buy it?"

**Examples in the wild:**
- **Claude Code** = developer harness (CLAUDE.md + hooks + skills + permissions) + Claude
- **Firemind** = IT operations harness (default-deny model + credential vaults + audit trail) + Claude
- **Claude Managed Agents** = platform harness (cron scheduling + credential vaults) + Claude
- **Kiro** = spec-driven development harness (requirements.md + design.md + tasks.md workflow) + Claude via Bedrock
- **Copilot Studio** = Microsoft Teams/M365 harness + Azure OpenAI
- **Noma / Linx Security** = harness monitoring/enforcement layers (not harnesses themselves)

**Evidence:**
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]] — "Every agentic AI product is a harness with a model inside. The business decision is not 'which AI model?' but 'which harness pattern fits this use case?'"
- [[braindump-2026-05-26-1018-aws-kiro-workshop]] — Kiro confirmed as Claude via Bedrock; Kiro = harness; the model is secondary to the harness design

**How to apply:** When evaluating any agentic AI vendor, lead with harness evaluation: what does it expose, what does it restrict, who can change it, is it auditable? The model choice is secondary.

**Confidence:** High

---

### Principle 2: Harness Design Encodes Governance Decisions

**Statement:** A harness is not a governance afterthought. Every element of a harness — permitted tools, data scope, escalation paths, audit logging, allowed actions — is a governance decision made concrete in configuration. If EA doesn't define harness design standards, teams will build harnesses with their own implicit governance decisions. That is how shadow AI proliferates at the harness layer.

**Components of a governed harness:**

| Component | What it governs | EA standard required |
|---|---|---|
| **Permitted tools** | Which MCP servers / APIs the agent can call | Approved tool catalogue per use case risk tier |
| **Data scope** | Which data sources the agent can read / write | Data classification alignment |
| **Allowed actions** | What the agent can do (read-only vs. write vs. execute) | Authorised intent definition |
| **Escalation paths** | What happens when agent is uncertain or blocked | Human-in-the-loop thresholds |
| **Memory** | What the agent retains between sessions | Data retention and privacy policy |
| **Audit trail** | What gets logged and for how long | Compliance and EU AI Act auditability |
| **Identity** | How the agent authenticates to tools and data | Entra ID managed identity or equivalent |
| **Who can modify** | Which roles can change harness configuration | Change management and approval process |

**Evidence:**
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]] — "Permissions, allowed tools, data scope, escalation paths, audit logging — these are not afterthoughts to harness design, they *are* harness design."
- [[05-knowledge/consolidated/agentic-ai-governance-framework]] — Governance as intent-setting (Principle 5): "define what goals agents are authorised to pursue, with what tools, under what constraints"

**How to apply:** When a team brings an agent use case to EA review, the review is not about the model — it is about the harness design. Use the component table above as the review checklist.

**Confidence:** High

---

### Principle 3: EA Owns Harness Design Standards; Teams Own Harness Instances

**Statement:** The right ownership split is: EA defines the template (what a compliant harness must contain), teams own their harness instances (configured to their use case within EA's template). This is the same model as cloud landing zones: EA defines the zone architecture; teams deploy into zones.

**The MCP Governance reframe:**
Instead of "how do we govern MCP servers?" → "how do we establish enterprise harness design standards, with MCP as the primary harness interface protocol?"

This reframe is more strategic, more durable, and positions EA as the right owner — not IT Security (who owns specific controls) and not the engineering team (who owns a specific use case).

**Landing zone analogy:**

| Cloud Landing Zone | Agent Harness |
|---|---|
| Zone definition (VNet, NSG, policies) | Harness template (tools, permissions, audit, identity) |
| Team deploys into a zone | Team configures a harness instance from the template |
| Azure Policy enforces compliance | Harness governance enforces policy at runtime |
| Central networking team owns the zone | EA owns the harness design standard |
| Workload team owns their resources | Product/delivery team owns their harness instance |

**Evidence:**
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]] — "EA should own the harness design standards; individual teams own their harness instances within those standards"
- [[04-projects/mcp-governance/PROJECT-OVERVIEW]] — MCP Governance as the vehicle for establishing these standards

**Confidence:** High on the ownership model; Medium on the MCP-as-primary-protocol claim (A2A and other protocols also relevant)

---

### Principle 4: Multi-Agent Systems Create Harness Recursion — Governance Must Address This

**Statement:** In multi-agent architectures, Agent A's harness may include Agent B as a tool. Agent B has its own harness. The governance question is not just "what can Agent A do?" but "can Agent A cause Agent B to do things outside Agent B's authorised scope?" This is the harness recursion problem.

**Recursion failure modes:**
- Agent A calls Agent B to take an action that A is not authorised to take directly
- Agent B's permissions are implicitly inherited by Agent A through delegation
- The audit trail for B's actions doesn't surface in A's audit trail

**Governance principle:** A2A delegation must respect both harnesses — Agent B cannot be instructed to exceed its own harness constraints, even by a trusted Agent A. This must be a design requirement, not an implicit assumption.

**Evidence:**
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]] — "In multi-agent systems it gets recursive: agent A's harness might include agent B as a tool, and agent B has its own harness. This is the governance recursion problem."
- [[05-knowledge/consolidated/agentic-ai-governance-framework]] — A2A as the delegation protocol (Principle 2)

**How to apply:** When reviewing a multi-agent architecture, map the harness boundaries explicitly. Verify that A2A delegation does not create privilege escalation paths across harness boundaries.

**Confidence:** Medium — the problem is clear; the standard solution is not yet settled

---

## Applications & Use Cases

### Use Case 1: AI Damage Assessment PoC — Harness Design Before Model Benchmarking

**Current problem:** PoC thinking is "which model analyses the damage image best?" (Fable 5 vs GPT-5.5). This is a secondary question.

**The right design question:** What does the harness look like?

**Proposed harness sketch:**

```
[Image input] → [Harness entry: format validation + classification]
                          ↓
               [Model inference: damage assessment]
                          ↓
               [Confidence gate: >threshold → structured output]
                          ↓
               [Confidence gate: <threshold → human review queue]
                          ↓
               [Audit log: image, model version, confidence, output]
                          ↓
               [Structured output: damage type, severity, recommended action]
```

**Harness components required:**
- Permitted tools: image classification API only (no external data access)
- Data scope: anonymised images only during PoC (no PII)
- Escalation: all images below 80% confidence threshold routed to human review
- Audit: every inference logged with model version and confidence score (EU AI Act auditability)
- Identity: managed identity — no service account credentials in config

**Action:** Produce this as a one-page harness architecture diagram alongside the model benchmarking plan.

---

### Use Case 2: MCP Governance Project — Reforming as Harness Standards

**Current framing:** "How do we govern MCP servers?"

**Stronger framing:** "How do we establish enterprise harness design standards, with MCP as the primary interface protocol for harness-to-tool connections?"

**Practical outputs to produce under new framing:**
1. Enterprise Harness Design Standard (one-page) — lists the required components of any Belron agent harness
2. MCP Governance Policy — rules for which MCP servers a harness may connect to, and approval process
3. Harness Registry (lightweight) — inventory of all harnesses in production, with EA ownership and last-reviewed date
4. Harness Classification — risk tiers (read-only data harness → low risk; write access to production systems → high risk → mandatory EA review)

---

### Use Case 3: Vendor Evaluation — Harness-First Assessment

**When to apply:** Evaluating Firemind, Noma, Linx Security, Azure AI Foundry, AWS Bedrock, or any agentic AI platform.

**Harness evaluation questions:**
1. What does the harness expose by default? (Opt-in vs. opt-out tool access)
2. Can the harness be configured to a default-deny security model?
3. Who can modify the harness configuration, and is there an approval workflow?
4. Is the audit trail complete — every tool call, every output, every modification?
5. Does the harness support managed identity / Entra ID authentication (not service account keys)?
6. Can the harness be version-controlled and reviewed as code?
7. Does the harness support the EU AI Act auditability requirements for automated decision-making?

**Example — Firemind through harness lens:**
- Firemind = harness product for IT operations
- Default-deny security model = Principle 2 in practice
- Credential vault = managed identity component
- "Let us run the harness in your cloud" = build vs. buy harness decision
- Evaluation question: Does Firemind's harness template satisfy Belron's enterprise design standard, or does it require modification?

---

## Boundaries & Limitations

**This framework works when:**
- The use case involves an AI agent taking autonomous or semi-autonomous actions in enterprise systems
- The governance question is about what an agent is allowed to do (not what a human user is allowed to do — that is IAM)
- The organisation wants model-agnostic governance (governs the harness regardless of whether the model is Claude, GPT, or Gemini)

**This framework does NOT apply when:**
- The AI interaction is purely conversational with no tool access or system actions (chat assistant without tools)
- The risk is in the model's response quality rather than its actions (RAG accuracy, hallucination risk — different governance domain)
- The governance concern is user access to AI tools (that is user access management, not harness governance)

**Common pitfalls:**
- Conflating harness design with model selection: model choice is secondary to harness design
- Governing MCP server catalogues without a harness-level ownership model: you get an approved list but no clear accountability
- Assuming harness design is a one-time activity: harnesses evolve as use cases change; a review cadence is required

---

## Vocabulary Note: "Harness" vs. Enterprise Equivalents

**"Harness"** is a developer term (from testing: a test harness wraps a component under test). It may not land well with non-technical stakeholders.

**Alternative framings for different audiences:**

| Audience | Preferred term | Definition |
|---|---|---|
| Technical / EA | Harness | Configured execution context wrapping a model |
| Business / CxO | Agent Operating Model | The rules, permissions, and accountability structure for an AI agent |
| Security / GRC | Agent Policy Container | The bounded environment defining what an agent can access and do |
| TOGAF / ArchiMate | Application Component + Technology Service (composite) | Formal notation for the execution context |

Use "harness" in architecture documentation and EA-to-EA conversations. Use "agent operating model" in board-level or business stakeholder conversations.

---

## Evolution & History

### June 2026 — Concept Crystallises

**What Emerged:** The harness concept crystallised from three parallel threads arriving simultaneously:
1. Claude Code's own CLAUDE.md notes: "the harness executes these, not Claude" — the clearest external articulation of the concept
2. Firemind's product architecture review — explicitly a harness product
3. MCP Governance project struggling with "what level to govern at" — harness is the answer

**Catalysts:**
- [[daily-brief-2026-06-09]] — Claude Managed Agents launch (cron scheduling + credential vaults in platform layer = Anthropic building harness infrastructure)
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]] — concept capture and analysis
- AWS Kiro workshop (May 26) — surfaced "bounded independence" as the agent/harness relationship concept

**Current confidence:** 85% — the harness framing is well-evidenced; the enterprise standard (what a compliant harness must contain) is the next work product.

---

## Related Frameworks

- [[agentic-ai-governance-framework]] — The harness concept is the structural upgrade to this framework's Principle 4 (governance must precede proliferation)
- [[architecture-operating-model-framework]] — EA owns harness design standards; this is an EA function deliverable
- [[microsoft-single-tenant-strategy-framework]] — Single tenant is the identity foundation that makes harness identity management coherent (one Entra ID = one managed identity plane)

---

## Future Development

**Questions for Deeper Exploration:**
- How does "harness" map precisely to TOGAF/ArchiMate constructs? Likely: Application Component (model) + Application Collaboration + Technology Service (MCP layer)
- What is the minimum viable Harness Design Standard for Belron? One page, listing required components
- Is there existing industry terminology that's equivalent? (Orchestration layer, agent runtime, agent policy container, execution environment)

**Next Work Products:**
- [ ] One-page Harness Design Standard for MCP Governance project
- [ ] Harness architecture diagram for AI Damage Assessment PoC
- [ ] Harness evaluation checklist for vendor assessments

**Watch For:**
- How Microsoft Azure AI Foundry, AWS Bedrock, and Anthropic Claude Managed Agents develop their harness infrastructure — these platform choices will shape Belron's build vs. buy decision
- Whether the Linux Foundation AAIF (AI Agent Interoperability Framework) standardises harness interfaces — if so, the Belron standard can align to an industry spec

---

*Consolidated from 6 sources | Confidence: High | Status: Emerging — concept is solid, enterprise standard document is the next deliverable*
