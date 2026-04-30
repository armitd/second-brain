---
type: "consolidated-knowledge"
domain: "professional"
framework: "llm-wiki-knowledge-infrastructure"
created: "2026-04-30"
last_updated: "2026-04-30"
consolidation_id: "consolidation-2026-04-30"
source_documents: 5
status: "emerging"
tags: ["#framework", "#consolidated", "#llm-wiki", "#knowledge-management", "#cog", "#karpathy", "#enterprise-architecture"]
---

# LLM Wiki Knowledge Infrastructure Framework

## Framework Overview
A model for building and operating AI-maintained knowledge systems — using LLMs to handle the structural and bookkeeping overhead of knowledge management, while humans focus on source curation and strategic direction. Applies at both the personal scale (COG) and the enterprise scale (Belron domain knowledge).

**Status:** Emerging (strong theoretical foundation from Karpathy; COG is a live implementation; enterprise application is speculative but grounded)
**Created:** 2026-04-30
**Source Insights:** 5 documents — Karpathy LLM Wiki gist braindump, Karpathy tweet braindump, AI absorbed the process layer (Byttow), omarsar0 implementation, daily briefs

---

## The Core Idea

Andrej Karpathy's 2026 GitHub gist proposes a specific pattern for AI-assisted knowledge management:

> *"The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."*

LLMs excel at bookkeeping. Humans excel at curation, analysis, and strategic thinking. The LLM Wiki pattern cleanly separates these.

**The contrast with RAG:**
Traditional Retrieval-Augmented Generation (RAG) retrieves raw document chunks at query time. LLM Wiki pre-synthesises knowledge into structured, interlinked pages. When a question arrives, the LLM has already done the thinking — it synthesises from prepared pages, not raw chunks. At ~100-article, ~400K-word scale, Karpathy found RAG was unnecessary — the LLM maintains its own index and reads relevant context on demand.

This has direct cost implications: enterprise AI teams investing in vector database infrastructure may be building for a constraint that no longer exists at standard knowledge base scale.

---

## The Three-Layer Architecture

| Layer | What It Is | COG Equivalent |
|-------|-----------|----------------|
| **Raw Sources** | Immutable curated input documents — articles, papers, data files, transcripts | `Readwise/`, `00-inbox/raw/`, braindumps |
| **The Wiki** | LLM-generated markdown files — summaries, entity pages, cross-references, maintained by the LLM | `05-knowledge/booklets/`, `05-knowledge/consolidated/` |
| **The Schema** | Config document defining wiki structure, workflows, and update rules | `CLAUDE.md` + skill files |

**The key insight for COG:** COG is already an implementation of the LLM Wiki pattern. The vault structure, CLAUDE.md as schema, braindumps as raw sources, and consolidated knowledge as wiki pages — these map directly to Karpathy's three layers. Naming it correctly matters: referring to COG as "an LLM Wiki implementation" gives it intellectual grounding when presenting it internally.

---

## Core Principles

### Principle 1: The Three Operations — Ingest, Query, Lint

**Statement:** A well-functioning LLM Wiki performs three operations. Two are typically in place; the third is most often missing.

**Ingest:** New sources trigger wiki updates across related pages simultaneously. Not just "file this" but "update all pages that this new source touches." In COG: /process-readwise and /braindump are the ingest operations.

**Query:** Questions are answered by synthesising existing wiki pages, with citations. Valuable answers are filed back as new pages — the query itself produces new knowledge. In COG: each session is a query operation; knowledge consolidation files the resulting frameworks.

**Lint:** Periodic health-checks — finding contradictions between pages, stale claims that have been superseded, orphan pages with no connections, and knowledge gaps (topics that keep appearing in queries but lack a dedicated page). **This is the missing operation in most implementations, including COG's current state.**

**The lint gap in COG:**
The ingest and query operations are in place. A dedicated lint pass — monthly, triggered by knowledge consolidation or an explicit /lint skill — would find:
- Contradictions between early braindumps and current frameworks
- Stale action items that were never completed
- Orphan booklets with no connections to active projects
- Knowledge gaps: topics appearing in daily briefs but with no corresponding framework

**Confidence:** High — lint operation is the most technically grounded principle; absence confirmed by audit

---

### Principle 2: The Source Layer Is the Quality Constraint

**Statement:** The LLM Wiki pattern only produces value proportional to the quality and signal density of the raw source layer. A well-built processing pipeline with weak inputs produces weak outputs.

**The Karpathy gap in COG:**
Karpathy's pattern works because he deliberately curates what goes in. COG's processing pipeline (braindumps, /process-readwise, daily briefs) is solid — but the raw source layer has gaps:
- 287 tweet files accumulate passively; practitioner newsletters were absent
- Readwise Reader is being used as a save target rather than a reading surface — highlights are sparse
- The difference between "reading in Readwise Reader" and "saving to Readwise" is highlights; highlights are what /process-readwise turns into booklets

**High-ROI source types (in priority order):**
1. **Practitioner newsletters** — distil signal from noise; Andrew Ng, Jack Clark, Ethan Mollick, Gregor Hohpe, Simon Willison are the highest-signal sources for Armo's domains
2. **Long-form essays and articles** — read in Readwise Reader, highlight key passages
3. **Substantive tweet threads** — full document captures via Readwise
4. **Braindumps** — already the strongest source layer; continue

**Evidence:** [[braindump-2026-04-29-0827-readwise-setup-max-value]] — full source for newsletter recommendations and Readwise Reader setup analysis

**Confidence:** High — source quality as the upstream constraint is structural, not speculative

---

### Principle 3: Knowledge and Action Layers Must Be Coupled

**Statement:** A knowledge base that can only answer questions is half a system. The full capability is a knowledge layer (LLM Wiki) coupled to an action layer (MCP tools) — so agents can surface knowledge when acting, not just when asked.

**The omarsar0 extension:**
When Karpathy published his gist, DAIR.AI's omarsar0 immediately shared his own implementation: automated daily paper curation, indexed with qmd CLI, fed into an interactive artifact generator via MCP. The key addition: MCP tools inside an agent orchestrator. The wiki doesn't just answer questions — the agent *acts on the answers*.

> *"The research is only as good as the research questions. And the research questions are only as good as the insights the agents have access to."*

**The COG coupling gap:**
COG currently has a knowledge layer (the vault, braindumps, booklets) and an action layer (MCP tools, Claude Code). They are not tightly coupled — the vault informs sessions as context at session start, but agents don't proactively query the vault as a tool during task execution. The next evolution: agents query `05-knowledge/` as a tool during task execution, not just as context at the beginning.

**Practical implications:**
- When running /daily-brief, the agent should be able to query existing framework files to check what's already been captured about a topic before searching the web
- When running /braindump, the agent should surface relevant connections from existing consolidated knowledge rather than relying on the user to identify them
- This is a COG architecture upgrade, not a minor feature

**Confidence:** Medium-High — coupling is architecturally sound; implementation pathway exists via MCP tools; not yet built

---

### Principle 4: The Finetuning Endgame

**Statement:** The LLM Wiki is not the destination. The progression is: LLM reads your knowledge base → LLM has become your knowledge base. As wiki scale grows and finetuning costs fall, the logical endpoint is synthetic data generation + model finetuning from the wiki corpus.

**The roadmap:**
1. **Current (COG Phase 1):** LLM reads vault as context at session start
2. **Next (COG Phase 2):** LLM queries vault as a tool during execution (knowledge-action coupling)
3. **Medium-term (COG Phase 3):** Wiki corpus used as synthetic training data for a personalised model variant
4. **Long-term:** The model has internalised the corpus — vault knowledge is in the weights, not the context window

**Not immediately actionable** — model finetuning costs are falling but personalised fine-tuning at the individual level is not yet practical. Worth tracking as costs continue to decrease.

**Confidence:** Medium — roadmap is plausible; timeline is speculative; intermediate steps are actionable now

---

## Enterprise Application — Belron LLM Wiki

The three-layer architecture scales from personal to domain-level knowledge management.

### Damage Assessment LLM Wiki
| Layer | Content |
|-------|---------|
| Raw Sources | FNOL reports, claim photographs, repair notes, calibration records |
| The Wiki | Synthesised pages per damage type, vehicle model, repair complexity, edge cases |
| The Schema | CLAUDE.md defining damage taxonomy, update rules, confidence thresholds |

**Value:** Rather than agents retrieving raw claim documents via RAG, the damage assessment agent queries pre-synthesised wiki pages that already capture patterns, edge cases, and decision rules. Materially different quality of output.

### Contact Centre LLM Wiki
| Layer | Content |
|-------|---------|
| Raw Sources | Call transcripts, resolution notes, product data, policy documents |
| The Wiki | Synthesised pages per issue type, resolution pathway, customer segment |
| The Schema | CLAUDE.md defining issue taxonomy, resolution standards, escalation rules |

**Value:** Contact centre agents have persistent, synthesised knowledge rather than RAG retrieval of raw transcripts. The wiki accumulates institutional knowledge from every resolved interaction.

### Strategic Framing for Belron EA
The enterprise LLM Wiki is strong enough to be an EA initiative in its own right — not just a personal productivity tool, but a governed capability Belron could deploy for domain knowledge management. The natural path: MCP Governance framework v0.1 → add LLM Wiki as the companion knowledge layer → propose "Belron Enterprise Knowledge Infrastructure" as a formal EA initiative.

---

## Applications & Use Cases

### Use Case 1: Adding the Lint Operation to COG
**When:** Monthly, as part of knowledge consolidation
**How:**
1. Scan consolidated frameworks for claims that are now superseded by newer braindumps or daily briefs
2. Identify orphan booklets — files in `05-knowledge/booklets/` with no connections to active projects or frameworks
3. Find knowledge gaps — topics appearing frequently in daily briefs (e.g., Amazon Connect Customer, MCP lazy loading) without a corresponding framework page
4. Update or archive stale content; create stub pages for identified gaps

**Expected outcome:** Knowledge base stays coherent rather than accumulating contradictions

---

### Use Case 2: Readwise Source Layer Upgrade
**When:** This week (setup work, low effort, high compound return)
**How:**
1. Route 5 priority newsletters into Readwise Reader (The Batch, Import AI, One Useful Thing, Architecture Notes, Simon Willison)
2. Enable Ghostreader auto-highlighting for queued articles
3. Set reading target: 15 min/day in Readwise Reader generates highlights; highlights feed /process-readwise; processed booklets feed consolidation
4. Add RSS feeds: Anthropic, OpenAI, DeepMind, LeanIX blogs

**Expected outcome:** /process-readwise finds richer content; daily briefs can reference source material rather than relying only on web search

---

### Use Case 3: COG Knowledge-Action Coupling (Phase 2)
**When:** After Readwise source layer is improved; when IFTTT MCP experiment is complete
**How:**
1. Add `05-knowledge/consolidated/` as a queryable resource in Claude Code — tools that let agents search the vault during skill execution
2. Update /daily-brief to check existing frameworks before searching the web for topics already covered
3. Update /braindump to surface connections to existing consolidated knowledge in the "Connections" section automatically

**Expected outcome:** Agents produce richer outputs by building on accumulated knowledge rather than starting from scratch each session

---

## Boundaries & Limitations

**This pattern works when:**
- Source curation is deliberate — the wiki is only as good as what flows in
- The knowledge domain is bounded — personal PKM, a specific business domain
- The LLM has sufficient context window to hold relevant wiki pages (current frontier models: adequate)

**This pattern does NOT work when:**
- Sources are purely noise (low-quality saves accumulate without filtering)
- The domain is too broad to synthesise meaningfully
- The schema (CLAUDE.md) is poorly defined — the LLM doesn't know what to do with new sources

**The key failure mode:**
Passive accumulation without active curation. Most personal knowledge management systems fail not because the processing is hard but because the input quality degrades over time as the novelty of the system wears off. The lint operation exists specifically to detect and address this.

---

## Evolution & History

### April 27, 2026: Framework Identified
Two braindumps on the same day (Karpathy gist + Karpathy tweet) produced the LLM Wiki pattern as a distinct conceptual framework — previously recognised implicitly in COG's design, now explicitly named.

**Key recognition:** COG is already an LLM Wiki implementation. The gist's three-layer architecture, three operations, and human/LLM division of labour are all present in COG's design. The naming gives the pattern intellectual grounding for external communication.

**Sources:** [[braindump-2026-04-27-0854-karpathy-llm-wiki]], [[braindump-2026-04-27-0955-karpathy-llm-wiki-tweet]]

### April 29, 2026: Source Layer Gap Identified
Post-/process-readwise session revealed the source layer as the quality constraint. The processing pipeline is solid; the raw input quality is not. Newsletter setup as the highest-ROI improvement.

**Source:** [[braindump-2026-04-29-0827-readwise-setup-max-value]]

---

## Related Frameworks

- [[agentic-ai-governance-framework]] — MCP is the *action* layer; LLM Wiki is the *knowledge* layer. Together they define Belron's AI agent infrastructure. EA governing both is the repositioned function.
- [[ea-effectiveness-framework]] — The enterprise LLM Wiki initiative is a concrete application of Principle 2 (dual-purpose artefact) and Use Case 4 (emerging technology governance ownership)
- [[ai-damage-assessment-strategy-framework]] — The damage assessment LLM Wiki is the most concrete enterprise application of this framework

---

## Future Development

**Near-term (this month):**
- [ ] Set up Readwise source layer (newsletters, RSS feeds) — highest ROI improvement 📅 2026-05-02
- [ ] Add lint operation to monthly COG rhythm 📅 2026-05-09
- [ ] Sketch the damage assessment LLM Wiki structure — one page, for internal use 📅 2026-05-09

**Medium-term:**
- [ ] Design COG Phase 2 knowledge-action coupling — vault as queryable tool during skill execution
- [ ] Develop "Belron Enterprise Knowledge Infrastructure" position paper — build on top of MCP Governance v0.1

**Watch for:**
- Model finetuning costs: when personalised fine-tuning becomes practical, the Phase 3 pathway becomes actionable
- Enterprise LLM Wiki implementations: any published case studies from comparable organisations would validate the enterprise application claims

---

*Created from 5 sources | Confidence: Emerging (theoretical base strong; enterprise application speculative) | First version: April 30, 2026*
