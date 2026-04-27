---
type: "braindump"
domain: "professional"
date: "2026-04-27"
created: "2026-04-27 08:54"
themes: ["llm-wiki", "knowledge-architecture", "rag-alternative", "ai-knowledge-management", "cog-pattern"]
tags: ["#braindump", "#raw-thoughts", "#ai-knowledge", "#enterprise-architecture", "#karpathy"]
status: "captured"
energy_level: "high"
emotional_tone: "curious"
confidence: "high"
source_url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
---

# Braindump: Karpathy's LLM Wiki — The Pattern Underneath COG

## Raw Thoughts

Andrej Karpathy's GitHub gist proposing "LLM Wiki" — a pattern for building personal knowledge bases using LLMs. Core idea: instead of traditional RAG (retrieving raw document chunks at query time), LLMs should incrementally build and maintain a persistent wiki — structured, interlinked markdown files.

Three-layer architecture:
1. **Raw Sources** — immutable curated documents (articles, papers, data files)
2. **The Wiki** — LLM-generated markdown files: summaries, entity pages, cross-references, maintained entirely by the LLM
3. **The Schema** — config document (like CLAUDE.md) defining wiki structure and workflows

Key operations:
- **Ingest**: new sources trigger wiki updates across 10–15 related pages simultaneously
- **Query**: questions answered by synthesising existing wiki pages with citations; valuable answers filed back as new pages
- **Lint**: periodic health-checks — contradictions, stale claims, orphan pages, knowledge gaps

The quote: *"The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."* LLMs excel at maintenance burden; humans handle source curation, analysis direction, strategic thinking.

700+ comments, competing implementations: Synthadoc, Beever Atlas, OpenCrab.

---

## Content Analysis

### Main Themes
1. **LLM Wiki as RAG alternative:** Rather than retrieval at query time, knowledge is pre-synthesised into navigable wiki pages. The LLM has already done the thinking when the question arrives.
2. **Bookkeeping as the failure mode of PKM:** Not intelligence or organisation appetite, but the mechanical overhead of keeping cross-references consistent. COG is built on this insight.
3. **Human/LLM division of labour:** Humans own curation and direction; LLMs own structure and maintenance. Clean separation.

### Questions Raised
- How does LLM Wiki handle contradictions between sources — what's the lint workflow in practice?
- At what scale does the wiki need its own index layer (i.e., when does the wiki need a wiki)?
- How does this sit alongside MCP as a protocol — is LLM Wiki a *pattern*, MCP a *transport*, and design.md a *context format*? Are these three orthogonal layers of the same stack?

### Decisions Contemplated
- Whether to formally adopt LLM Wiki as the pattern name for what COG is doing — it's a stronger conceptual frame than "PKM" or "second brain"
- Whether Belron knowledge domains (vehicle glass taxonomy, damage types, brand standards) should be explicitly managed as LLM Wikis with ingest/query/lint operations

---

## Strategic Intelligence

### Key Insights

1. **COG is an implementation of LLM Wiki.** The vault structure, CLAUDE.md as schema, braindumps as raw sources, consolidated knowledge as wiki pages — this is the pattern Karpathy describes. The AI Edge tweet linking here was pointing at the conceptual foundation of the system you're already running. The terminology is useful: referring to COG as "an LLM Wiki implementation" gives it intellectual grounding when presenting it internally.

2. **The lint operation is what's missing from COG's current workflow.** Ingest (braindumps, url-dumps, daily briefs) and query (COG sessions) are both in place. But the periodic lint — finding contradictions, stale claims, orphan pages, knowledge gaps — isn't explicitly scheduled. The weekly check-in partially covers this, but a dedicated lint pass (monthly?) would strengthen the system.

3. **This pattern has direct enterprise applicability beyond personal PKM.** An LLM Wiki for the Belron damage assessment domain would look like: raw sources = FNOL reports, claim photos, repair notes; wiki = synthesised pages per damage type, vehicle model, repair complexity; schema = CLAUDE.md defining taxonomy and update rules. The pattern scales from personal to domain-level knowledge management.

4. **The three-layer architecture maps cleanly onto EA governance concerns.** Raw Sources = operational data and documents. Wiki = synthesised enterprise knowledge (architecture decisions, principles, patterns). Schema = EA governance framework defining what gets captured and how. An enterprise LLM Wiki governed by EA would be a significant capability — and a natural evolution from the current MCP governance work.

### Pattern Recognition
- **Connection to COG origin article:** The Huy Tieu article (bookmarked April 25) makes the same fundamental argument — remove the organisational overhead. Karpathy's framing is more precise: the overhead is *bookkeeping*, and bookkeeping is exactly what LLMs do well at any scale.
- **Connection to design.md:** design.md is a schema-layer document — it defines structure for a specific domain (visual identity) so AI agents can maintain it consistently. Karpathy's Schema layer is the generalisation of which design.md is one instance.
- **Connection to MCP Governance:** MCP governs how AI agents access tools and data. LLM Wiki governs how AI agents maintain and synthesise knowledge. These are complementary — one for action, one for memory.

### Strategic Implications
- **For the MCP Governance project:** Add LLM Wiki pattern as a companion framework. MCP = agentic *action* layer. LLM Wiki = agentic *knowledge* layer. Together they define Belron's AI agent infrastructure.
- **For the Contact Centre of the Future:** A CCOTF knowledge base built as an LLM Wiki (ingesting call transcripts, resolution notes, product data) would give contact centre agents persistent, synthesised knowledge rather than RAG retrieval of raw documents. Materially different capability.
- **For EA positioning:** Presenting "Belron Enterprise LLM Wiki" as an EA-governed knowledge infrastructure initiative is the kind of strategic framing that differentiates EA from "just enough architecture." It's concrete, bounded, and demonstrably useful.

---

## Action Items

### Immediate (This Week)
- [ ] Add LLM Wiki pattern reference to MCP Governance project — position as knowledge layer alongside MCP's action layer 📅 2026-04-28
- [ ] Capture CCOTF vision braindump and include LLM Wiki as the knowledge architecture model 📅 2026-04-28

### Short-term (2 Weeks)
- [ ] Sketch what a Belron damage assessment LLM Wiki would look like: raw sources, wiki structure, schema rules — one page, for internal use 📅 2026-05-09
- [ ] Add lint operation to COG rhythm — monthly pass to find contradictions, stale claims, orphan pages 📅 2026-05-09

### Strategic Considerations
- The enterprise LLM Wiki framing is strong enough to be an EA initiative in its own right — not just a tool Armo uses personally, but a governed capability Belron could deploy for domain knowledge management. Worth developing into a position paper once MCP governance framework has a v0.1.

---

## Connections
- **Related Braindumps:** —
- **Relevant Projects:** [[04-projects/mcp-governance/PROJECT-OVERVIEW|MCP Governance]], [[04-projects/contact-centre-future/PROJECT-OVERVIEW|Contact Centre of the Future]], [[04-projects/ai-damage-assessment-poc/PROJECT-OVERVIEW|AI Damage Assessment PoC]]
- **Knowledge Base:** [[05-knowledge/booklets/articles/cog-second-brain-huy-tieu-2025-10-15|COG origin article]], [[05-knowledge/booklets/articles/design-md-google-labs-2026-04-25|design.md]]
- **Source:** [LLM Wiki — Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

---

## Domain Classification
- **Primary Domain:** Professional (95%)
- **Reasoning:** Direct relevance to EA role, active projects, and enterprise knowledge strategy
- **Cross-Domain Elements:** Personal — COG itself is an implementation of this pattern, so improvements to the pattern improve the daily tool
- **Privacy Level:** Professional/shareable

## Processing Notes

### Emotional Context
- **Energy Level:** High — this is the kind of foundational framing that recontextualises existing work
- **Emotional Tone:** Curious and motivated — seeing COG as an LLM Wiki implementation gives it more weight as something to develop further

### Confidence Assessment
- **Overall Analysis:** 92% — source is clean and well-structured; gist content is clear
- **Domain Classification:** 95% — professional with minor personal cross-domain element
- **Strategic Insights:** 88% — LLM Wiki / CCOTF connection is strong; enterprise LLM Wiki initiative is speculative but grounded

---

*Processed by COG Brain Dump Analyst*
