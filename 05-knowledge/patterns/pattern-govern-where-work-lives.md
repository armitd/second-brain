---
type: "pattern-analysis"
pattern: "govern-where-work-lives"
created: "2026-07-18"
domains: ["professional", "enterprise-architecture", "ai-governance"]
frequency: "high"
tags: ["#pattern", "#analysis", "#enterprise-architecture", "#governance", "#belron"]
---

# Pattern: Govern Where the Work Already Lives

## Pattern Description
The most durable governance is built into the platform where the work already happens, not bolted on as a separate control layer. A parallel governance register that duplicates the system of record drifts out of sync within weeks: two sources of truth that disagree, and nobody sure which to trust. The recurring EA move is to extend the existing system of record to carry its own governance, rather than standing up a new one beside it.

**Frequency:** High — recurs across LeanIX (EA estate), MCP Governance (agent access), and agent-identity management (June–July 2026), and is the structural principle behind the harness-as-unit-of-governance argument.

**Domains:** Professional — Enterprise Architecture, AI Governance

**Significance:** Governance that lives outside the work is governance that decays. This pattern is the antidote to shelfware governance frameworks and duplicate registries — and it is the through-line that lets Belron's separate governance conversations (EA tooling, MCP, AI assets) reinforce rather than compete.

---

## Occurrences

### July 2026 — LeanIX as the estate governance platform
**Context:** LeanIX discovery and the Front Office Meeting AI-governance thread.

**Manifestation:** Rather than build a new register to govern the technology estate (and later a second one to govern AI assets), the play is to govern inside LeanIX — where the applications, integrations, and initiatives already live — and extend the same fact-sheet model to AI use cases, models, and agents.

**Outcome:** Coined as the tagline "If you are working in LeanIX, then it makes sense to govern in LeanIX." Became Principle 6 of the LeanIX framework and the basis of the AI-group pitch.

**Source:** [[braindump-2026-07-15-1426-leanix-discovery-enquiry-access]]

---

### June 2026 — MCP Governance as harness-level control
**Context:** MCP Governance reframed around the harness as the unit of governance.

**Manifestation:** Governance is embedded in the harness (the configured execution context the agent actually runs in) rather than applied as an external review gate. EA owns the template; teams govern their own instances within it — the same "govern where the work happens" shape, applied to agent execution.

**Outcome:** The harness-as-unit-of-governance principle ([[harness-design-standard-framework]], and Principle 8 of [[agentic-ai-governance-framework]]).

**Source:** [[braindump-2026-06-11-0938-harnesses-agentic-ai]]

---

### June 2026 — Agent identity governed in the identity file
**Context:** Persistent-agent identity documents (CLAUDE.md / SOUL.md).

**Manifestation:** An agent's constraints and safety rules are governed in the identity file that travels with the agent and defines its behaviour, not in an external policy document the agent never reads. The governance lives where the agent actually operates.

**Outcome:** The agent-identity document established as a governance artefact (Principle 11 of [[agentic-ai-governance-framework]]).

**Source:** [[braindump-2026-06-21-1209-hermes-agent-persistent-agentic-platform]]

---

## Analysis

**What Triggers This Pattern:**
- A governance need arises for an asset class that already has a system of record
- The instinct (often from outside EA) is to stand up a new, dedicated governance tool or register
- The asset owners already work in the system of record daily; asking them to maintain a second register guarantees non-adoption

**What Follows This Pattern (when applied well):**
- One source of truth; governance data stays current because it is a by-product of the work, not extra work
- Governance conversations across domains reinforce each other (same model, applied consistently)
- Adoption is higher because governance meets people where they already are

**What Follows When Violated:**
- Parallel registers drift; the governance copy goes stale and loses trust
- Owners maintain the working system and neglect the governance shadow
- EA credibility drops when the governance artefact is visibly out of date

**Cross-Domain Implications:**
- Applies to any system of record: EA repository (LeanIX), agent execution (harness), agent identity (identity file), and by extension data governance (govern in the catalogue, not a spreadsheet) and process governance (govern in Signavio, not a separate map).

**Recommended Actions:**
1. Before proposing a new governance register or tool, ask: "Where does this work already live, and can that system govern it?"
2. Extend the existing system of record's native governance features before buying or building a parallel layer.
3. Make governance a by-product of the work (ownership, lifecycle, re-certification inside the working tool), not a separate maintenance task.
4. Watch the framing: "govern where you work" must read as guardrails that enable speed, not a control layer that slows delivery.

---

## Related Patterns & Frameworks
- [[pattern-platform-activation-gap]] — the capability to govern in-place is often already licensed but unactivated
- [[pattern-artefact-as-instrument]] — the governed system of record doubles as a stakeholder-visibility instrument
- [[leanix-ea-repository-framework]] — Principle 6 (govern where the work lives), applied to EA tooling
- [[agentic-ai-governance-framework]] — harness-as-unit (Principle 8) and agent-identity documents (Principle 11) are the agentic instances

---

## Evolution Over Time

Identified July 2026 as the common shape behind three previously separate observations (LeanIX governance, harness governance, agent-identity governance). Expected to recur wherever a governance need meets an existing system of record — a candidate lens for any future "should we build a new register?" decision.

---

*Pattern identified through consolidation 2026-07-18 — [[braindump-2026-07-15-1426-leanix-discovery-enquiry-access]], [[braindump-2026-06-11-0938-harnesses-agentic-ai]], [[braindump-2026-06-21-1209-hermes-agent-persistent-agentic-platform]]*
