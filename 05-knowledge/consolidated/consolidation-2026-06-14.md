---
type: "knowledge-consolidation"
domain: "integrated"
date: "2026-06-14"
consolidation_period: "2026-05-14 to 2026-06-14"
created: "2026-06-14 21:25"
sources_analyzed: 54
frameworks_updated: ["agentic-ai-governance-framework", "architecture-operating-model-framework"]
frameworks_created: ["harness-design-standard-framework"]
patterns_identified: 3
tags: ["#consolidation", "#knowledge", "#frameworks"]
---

# Knowledge Consolidation — 14 June 2026

## Executive Summary

**Period Analysed:** 2026-05-14 to 2026-06-14

**Documents Processed:**
- 34 professional braindumps
- 10 project braindumps (CCOTF ×5, MCP Governance ×4, Nordics ×1)
- 2 weekly check-ins
- 10 daybooks (selected)
- 1 week plan
- Comprehensive analysis (June 7)

**Major Outcomes:**
- **New Framework Created:** 1 — Harness Design Standard (the month's most significant new concept)
- **Frameworks Updated:** 2 — Agentic AI Governance (+2 new principles), Architecture Operating Model (already current)
- **Major Themes Identified:** 5
- **Patterns Reinforced:** 3 (all previously documented; one elevated in significance)

**Key Insights Synthesised:**
1. The harness — not the model, not the MCP server — is the right unit of enterprise AI governance
2. Semantic governance is the missing layer in Belron's AI governance programme
3. EA is in a structural position to own harness design standards, experiment design, and semantic governance simultaneously — each is an EA function, not an IT function
4. The pre-IPO window is for architectural decisions on paper, not programme execution
5. Kiro (AWS) confirmed as Claude via Bedrock — the Anthropic advocacy strategy is strengthened, not threatened, by Kiro adoption

---

## Processing Statistics

- **Total documents analysed:** ~54
- **Date range:** 2026-05-14 to 2026-06-14
- **Domains covered:** Professional, Project-specific (CCOTF, MCP Governance, AI Damage Assessment, Nordics), Personal (limited)
- **Braindumps already consolidated before this session:** 12 (marked `status: consolidated` — included in pattern analysis but not re-processed)
- **New frameworks created:** 1
- **Frameworks updated:** 2
- **New evolution sections added:** 1 (to agentic AI governance framework)
- **New principles added to existing framework:** 2 (Principles 8 and 9 in agentic AI governance)

---

## Major Themes This Period

### Theme 1: The Harness as Governance Unit
**Frequency:** Appeared implicitly across 8+ documents; explicitly crystallised June 11

**The concept:** A harness is the configured execution context that wraps an AI model — defining what it can see, what it can do, when it can act, and who can change those constraints. Every agentic AI product is a harness with a model inside. The governance decision is not "which model?" but "which harness pattern, and do we build or buy it?"

**Why this matters:** The MCP Governance project has been framing the problem as "how do we govern MCP servers?" The harness reframe — "how do we establish enterprise harness design standards, with MCP as the primary interface protocol?" — is more strategic, more durable, and gives EA the right scope of ownership.

**Evidence trail:**
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]] — full concept capture
- [[braindump-2026-05-26-1018-aws-kiro-workshop]] — Kiro as harness; "bounded independence"
- [[daily-brief-2026-06-09]] — Claude Managed Agents: cron + credentials = Anthropic building platform harness infrastructure

**Framework Implications:** New framework created: [[harness-design-standard-framework]]. Principles 8 added to [[agentic-ai-governance-framework]].

**Status:** Emerging — concept well-evidenced; one-page Harness Design Standard document is the next deliverable

---

### Theme 2: Semantic Governance as the Missing AI Layer
**Frequency:** Appeared across 4 documents; already consolidated May 24 but needs framework integration

**The concept:** Enterprise AI governance addresses toolchain security and access control. It does not govern *meaning*. Without shared business definitions (controlled vocabulary, ontology), multi-agent systems create "parallel realities" — each agent interprets "customer," "case closed," or "SLA" independently. The inconsistency is not a data quality problem; it is a meaning governance problem.

**Belron-specific risk:** 30+ opcos, each with their own definitions of core business objects. Group-level AI agents pulling from opco data will produce outputs that are each internally consistent but mutually contradictory. Hard to detect; structurally dangerous for insurance-grade outputs.

**Architecture principle:** Evaluate stage should use explicit ontology-driven rules, not LLM inference. This is auditable, consistent, and EU AI Act-compatible.

**Evidence trail:**
- [[braindump-2026-05-21-1700-semantic-layer-governance-newman]] — core concept (already consolidated May 24)
- [[braindump-2026-05-20-1352-copilot-365-notebooks-data-placement]] — Copilot semantic inconsistency across surfaces
- [[braindump-2026-05-30-0958-agentforce-contact-center-belron-fit]] — CCOTF semantic definitions ("escalation", "resolution")

**Framework Implications:** Principle 9 added to [[agentic-ai-governance-framework]]. Semantic governance should be scoped into the MCP Governance project as a parallel workstream.

**Status:** Understood; not yet actioned at Belron. Entry point: lightweight ontology covering 20–30 core business objects

---

### Theme 3: EA Elevation — Four Simultaneous Authority Opportunities
**Frequency:** Appeared across 10+ documents; a structural pattern not a single event

**The pattern:** In the past month, four separate EA authority opportunities appeared simultaneously, each positioning EA as the strategic governance layer rather than a technical support function:

1. **Harness design standards** — EA owns the template that all agentic AI deployments must comply with
2. **Experiment design framework** — EA owns the innovation accounting framework for AI PoCs (not just architecture review, but the hypothesis/metric/pivot-threshold framework)
3. **Semantic governance** — EA proposes the enterprise ontology programme (owns it or co-owns with CDO/Data Governance)
4. **Architecture operating model** — EA produces the EA/SA/TA proposal that defines accountability for all technical architecture work

**Why the elevation matters:** Each of these shifts EA from "reviewer of decisions already made" to "owner of the framework within which decisions are made." That is the structural difference between a support function and a governance function.

**Key risk:** Taking on all four simultaneously when stakeholder bandwidth is limited and CCOTF scope is still undefined. The operating model proposal may need to come first — it establishes EA's internal authority before EA claims external governance scope.

**Evidence trail:**
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]] — harness standards as EA deliverable
- [[braindump-2026-05-06-0952-lean-startup-cycle]] — EA as owner of experiment design framework
- [[braindump-2026-05-21-1700-semantic-layer-governance-newman]] — semantic governance as EA initiative
- [[braindump-2026-06-04-1516-architecture-split-ea-sa-ta]] — architecture operating model proposal

**Status:** Pattern identified; sequencing is the strategic question. No framework update required — this is an operational positioning insight.

---

### Theme 4: Pre-IPO Decide-Not-Execute
**Frequency:** Appeared in 5+ documents across different topics

**The pattern (reinforced this period):** The H2 2026 IPO creates a narrow window where Belron should be making architectural decisions on paper and getting them approved — not starting major programmes. The same principle applied this month to:
- **Microsoft single tenant:** Decide the architecture direction now; programme starts post-IPO (Q1 2027)
- **BCM programme:** Get the business case and methodology approved now; full programme post-IPO
- **Architecture operating model:** Socialise and approve the proposal now; headcount decisions post-IPO
- **MCP Governance framework:** Get the governance framework approved now; harness registry and tooling post-IPO

**Why this is a pattern not just a constraint:** Pre-IPO decisions that get board/Group IT alignment become part of the post-IPO technology roadmap. Decisions not made pre-IPO risk being superseded by new leadership priorities after listing. The EA function's output in H2 2026 should be a set of approved architecture decisions and governance frameworks, not delivered programmes.

**IPO compressed timeline (all in H2 2026):**
- EU AI Act Annex III enforcement: August 2, 2026
- MCP final spec: July 28, 2026
- Anthropic IPO: H2 2026
- Belron IPO: H2 2026

**Status:** Stable pattern, well understood. No new framework needed — existing patterns documentation covers this.

---

### Theme 5: Anthropic Advocacy — Multiple Doors, Same Model
**Frequency:** Appeared across 4+ documents; key strategic clarification from AWS Kiro

**The clarification:** The Anthropic advocacy strategy (getting Belron onto Anthropic/Claude) was initially threatened by the emergence of AWS Kiro as a potential competing AI coding tool. The post-workshop analysis resolved this: Kiro runs on Claude via Amazon Bedrock. Kiro adoption at Belron = Claude adoption at Belron, routed through AWS infrastructure.

**The enriched picture:**
- **Claude Code** = direct Anthropic API path to Claude
- **AWS Kiro** = AWS Bedrock path to Claude
- **Salesforce Agentforce CC** = potentially Salesforce Einstein AI (not Claude — this is the divergence to watch)
- **Microsoft 365 Copilot** = Azure OpenAI (mix of models, not primarily Claude)

**Strategic implication:** The EA function can advocate for Claude at Belron through multiple routes simultaneously — a direct PoC (AI Damage Assessment), a developer tooling adoption (Kiro pilot via AWS), and any SAP Joule integration if Belron uses SAP (Joule now runs on Claude). The H&F/Anthropic relationship is not a lever; the PoC and developer tooling are the levers.

**Evidence trail:**
- [[braindump-2026-05-11-1200-getting-belron-onto-anthropic]] — H&F arm's-length constraint
- [[braindump-2026-05-26-1018-aws-kiro-workshop]] — Kiro runs on Claude via Bedrock (resolved)
- [[weekly-checkin-2026-06-07]] — SAP Joule + Anthropic partnership noted

---

## Framework Created

### New Framework: Harness Design Standard
**Location:** [[05-knowledge/consolidated/harness-design-standard-framework]]

**Created:** Based on 6 insights from June 11, 2026 (crystallisation of parallel threads)

**Core Concept:** The harness — configured execution context wrapping an AI model — is the right unit of enterprise AI governance. Every agent product is a harness + model. EA owns harness design standards; teams own harness instances.

**Components of a governed harness:** Permitted tools, data scope, allowed actions, escalation paths, memory, audit trail, identity, modification governance.

**Three vocabulary options:** "Harness" (technical/EA), "Agent Operating Model" (business/CxO), "Agent Policy Container" (security/GRC)

**Primary Use Cases:**
- AI Damage Assessment PoC: design the harness before selecting the model
- MCP Governance: reframe as enterprise harness standards with MCP as interface protocol
- Vendor evaluation: harness-first assessment checklist

**Status:** Emerging — concept solid; one-page enterprise standard document is the next deliverable

---

## Frameworks Updated

### Updated: Agentic AI Governance Framework
**Location:** [[05-knowledge/consolidated/agentic-ai-governance-framework]]

**What Changed:**
- Updated frontmatter: `last_updated: 2026-06-14`, `source_documents: 37`, `consolidation_id: consolidation-2026-06-14`
- **New Principle 8:** The Harness as the Unit of Governance — complete with harness component checklist, MCP tooling landscape (Docker/Noma/Agent 365), harness recursion problem in multi-agent systems
- **New Principle 9:** Semantic Governance as the Missing Layer — parallel realities risk, architecture principle (explicit rules > LLM inference), practical entry point (20–30 core business objects)
- **New Evolution Section:** May 14 – June 14, 2026 — harness concept, semantic gap, tooling landscape, Kiro confirmation
- **Updated Related Frameworks:** Added [[harness-design-standard-framework]]
- **Updated footer**

**New Evidence Added:**
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]] — harness concept
- [[braindump-2026-05-21-1700-semantic-layer-governance-newman]] — semantic governance
- [[weekly-checkin-2026-06-07]] — MCP tooling landscape (Docker/Noma/Agent 365)
- [[braindump-2026-05-26-1018-aws-kiro-workshop]] — Kiro as governed MCP client

---

## Patterns Reinforced (No New Pattern Documents Required)

### Pattern 1: Governance at the Wrong Level
**Previous documentation:** [[pattern-platform-activation-gap]], [[agentic-ai-governance-framework]] Principle 6
**Reinforcement this period:** Same pattern appearing across three domains simultaneously:
- Governing the model (wrong) → govern the harness (right)
- Governing the data (wrong) → govern the meaning / semantic layer (right)
- Governing MCP server catalogues (wrong) → govern harness instances (right)
The pattern is now structural, not situational. It should be named explicitly in the EA effectiveness framework as a diagnostic tool: "When a governance proposal isn't working, ask: is it governing at the wrong level?"

### Pattern 2: Pre-IPO Decide-Not-Execute
**Previous documentation:** [[pattern-ipo-driven-prioritisation]]
**Reinforcement this period:** Applied consistently across tenant strategy, BCM, operating model, and MCP Governance. Pattern is now stable and reliable as a decision filter. No update to pattern document required — it is accurately documented.

### Pattern 3: Internal Champion Pattern
**Previous documentation:** [[braindump-2026-05-11-0842-servicenow-perception-gap]], [[braindump-2026-05-11-1200-getting-belron-onto-anthropic]]
**Reinforcement this period:** The Kiro/Anthropic insight reinforces: technology adoption happens through demonstrated results, not vendor relationships. The PoC is the vehicle. The ServiceNow perception gap is the counter-example. Both point to the same principle: evidence-based internal advocacy beats top-down mandate.

---

## Cross-Cutting Insights

**Connections Across Domains:**
- Semantic governance, harness design, and BCM are all upstream dependencies for the same downstream outcome: AI agents that produce consistent, auditable, trust-worthy outputs. None of these are independent — they form a stack: capability map (BCM) → shared definitions (semantic) → governed execution (harness).
- The EA/SA/TA operating model proposal and the Communities of Practice proposal are connected: a formal EA CoP is the vehicle for spreading EA capability (including BCM, semantic governance, harness standards) across the organisation without top-down mandate.
- The pre-IPO timing makes all of these converge: the architecture decisions made in H2 2026 will define Belron's technology governance narrative for investors and post-IPO leadership.

**Contradictions Identified:**
- **CCOTF scope vs. vendor intelligence:** The intelligence gathering on CCOTF (Agentforce CC, Genesys numbers, Qualtrics) is excellent but the project itself has no written scope. Intelligence accumulation without a project container feeds anxiety, not progress. Resolution: write the one-page CCOTF scope before doing more research.
- **Anthropic advocacy via PoC vs. IPO caution:** The PoC is the advocacy vehicle, but pre-IPO Belron is cautious about new vendor commitments. These aren't irreconcilable — position the PoC as "proving model capability" not "committing to a vendor" until the evidence is strong enough to make the case.

**Strategic Observation:**
The month's strongest signal is that the EA function at Belron has a rare convergence of authority opportunities: four separate governance frameworks where EA is the natural owner, all arriving simultaneously, against an IPO deadline that rewards having governance on paper. The risk is trying to do all four at once with insufficient stakeholder bandwidth. The opportunity is to sequence them deliberately: operating model first (internal EA authority), then harness standards (external AI governance authority), then semantic governance (data-level AI governance), then BCM (strategic business alignment). Each one builds the credibility for the next.

---

## Knowledge Base Maintenance

### Updates Made
- ✅ Created new framework: [[harness-design-standard-framework]]
- ✅ Updated: [[agentic-ai-governance-framework]] — Principles 8 and 9, evolution section, related frameworks, footer
- ✅ Consolidation report saved: [[consolidation-2026-06-14]]

### Braindumps to Mark Consolidated
The following braindumps processed in this session that were `status: captured` (not previously consolidated) should have their metadata updated:
- [[braindump-2026-06-11-0938-harnesses-agentic-ai]]
- [[braindump-2026-06-04-1516-architecture-split-ea-sa-ta]]
- [[braindump-2026-06-04-1710-mcp-ref-architecture-simplified-diagram]]
- [[braindump-2026-05-31-communities-of-practice-notebooklm]]
- [[braindump-2026-05-31-business-capability-mapping-notebooklm]]
- [[braindump-2026-06-09-1614-eldm-mulesoft-research]]

Previously consolidated braindumps (already marked): microsoft-single-tenant-strategy, lean-startup-cycle, getting-belron-onto-anthropic, semantic-layer-governance-newman, agentforce-contact-center-belron-fit, aws-kiro-workshop, informatica-idmc-beyond-mdm.

---

## Future Consolidation Needs

### Ready for Framework Creation
- [ ] **BCM + Application Rationalization Framework** — Sufficient evidence (May 31 NotebookLM braindump + earlier April research). TIME matrix, six-step process, heat map overlays well documented. Anchor to a specific business problem (CCOTF rationalisation or AI Damage Assessment investment case). Target: next consolidation session.
- [ ] **Communities of Practice Framework update** — The May 31 CoP braindump adds the full lifecycle model, distributed leadership roles, and failure mode table. The existing framework needs updating with this richer content.

### Needs Deeper Analysis
- [ ] **ELDM + MuleSoft** — [[braindump-2026-06-09-1614-eldm-mulesoft-research]] flagged as needing auto-research. Feeds into the Salesforce ecosystem strategy deliverable. Run `/auto-research` session.
- [ ] **CCOTF architecture decisions** — Genesys consumption numbers, Qualtrics/Genesys ops model, CCOTF written scope — all captured but not synthesised. Cannot build the framework without a written project scope.

### Monitoring Required
- [ ] **MCP final spec July 28** — All MCP governance policies need a post-July-28 review pass. Calendar reminder needed.
- [ ] **EU AI Act August 2** — Annex III enforcement. PoC DPO/Legal classification still unconfirmed. Urgent.
- [ ] **Belron Salesforce footprint** — Critical unknown for CCOTF vendor selection. Needs a direct question to a stakeholder.
- [ ] **VAPS numbers from Kiro workshop** — Are the 70% unrealised / €200m–€1bn figures live Belron data? Confirm with AWS account team or internal VAPS owner.

---

## Next Steps

**Immediate Actions:**
1. Produce one-page Harness Design Standard document for MCP Governance project (converts framework to usable EA deliverable)
2. Write CCOTF project scope — one page, before any more vendor research
3. Confirm EU AI Act classification for AI Damage Assessment PoC (deadline: August 2, 2026)

**Next Consolidation:**
- **Suggested date:** 2026-07-14 (one month)
- **Focus Areas:** BCM framework creation, CoP framework update, ELDM/MuleSoft research outputs, post-July-28 MCP spec review

**Framework Applications:**
- MCP Governance project: use harness framework to reframe scope and deliverables
- AI Damage Assessment PoC: harness design sketch alongside model benchmarking plan
- Architecture community proposal: use operating model framework as the base document
- Vendor evaluations (Firemind, Noma, Linx): apply harness evaluation checklist from new framework

---

*Consolidation completed: 2026-06-14 21:25 | Processed ~54 documents | Created 1 framework, updated 2 frameworks, reinforced 3 patterns*
