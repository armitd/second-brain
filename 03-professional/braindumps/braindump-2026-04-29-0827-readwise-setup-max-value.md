---
type: "braindump"
domain: "professional"
date: "2026-04-29"
created: "2026-04-29 08:27"
themes: ["readwise-setup", "knowledge-management", "signal-curation", "cog-infrastructure"]
tags: ["#braindump", "#readwise", "#knowledge-management", "#cog", "#second-brain"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-04-30]]"
consolidated_date: "2026-04-30"
energy_level: "medium"
emotional_tone: "intentional"
confidence: "high"
---

# Braindump: Readwise Setup — Getting Max Value from Newsletters and Sources

## Raw Thoughts
To put more effort into setting up Readwise to get max value from newsletters, sources etc.

*Context: triggered after running /process-readwise and finding no new content since 2026-04-28 — and after comparing COG to Karpathy's LLM Wiki pattern. The raw source layer is only as good as what flows into it.*

## Content Analysis

### Main Themes
1. **Readwise as the foundation of COG's raw layer** — if the inputs are weak, everything downstream (booklets, patterns, daily briefs) is weaker. The Karpathy comparison makes this vivid: his pattern only works because he's deliberately curating what goes in.
2. **Current state underutilises Readwise Reader** — 1,500 full-text articles and 287 tweet author files exist, but only 18 article booklets and a batch of threads have been processed. The volume suggests passive accumulation rather than active curation.
3. **Newsletter and RSS setup is unclear** — no evidence of deliberate source selection in Readwise. The content that has landed reflects organic saving (articles read elsewhere, tweets saved) rather than a proactive feed strategy.

### Questions Raised
- What newsletters are currently flowing into Readwise Reader vs being read elsewhere (email, browser)?
- Which sources align directly with active interests: AI, enterprise architecture, automotive, foundation models, agentic AI, MCP/A2A?
- What's the reading cadence? Are highlights being generated, or is content accumulating unread?
- Is Readwise Reader being used as the reading surface, or just as a save target?

### Decisions Contemplated
- Which newsletters to route into Readwise Reader (vs keep in email)
- Whether to set up RSS feeds for key sources (Anthropic blog, OpenAI, DeepMind, LeanIX, etc.)
- Whether to use Readwise's "Ghostreader" AI features for auto-highlighting and summarisation
- How to tag/label content in Readwise so COG processing is more targeted

## Strategic Intelligence

### Key Insights

1. **The Karpathy gap is at the source layer.** His pattern works because he deliberately feeds quality raw material. COG's processing pipeline is solid — the gap is upstream. Better Readwise setup = better COG output with no other changes needed.

2. **Newsletters are the highest-ROI source type.** Newsletters from practitioners (not just news aggregators) distil signal from noise. For Armo's domains, a handful of high-quality newsletters would outperform hundreds of saved articles.

3. **Readwise Reader as reading surface is the unlock.** The difference between "saving things to Readwise" and "reading in Readwise" is highlights. Highlights are what /process-readwise turns into booklets. If there are no highlights, the processed output is thin. Reading *in* Readwise Reader makes highlighting natural.

### Pattern Recognition
- **Connection to Karpathy conversation (2026-04-29):** This braindump is a direct output of the COG vs Karpathy comparison — recognising that raw source curation is the gap.
- **Connection to [[braindump-2026-04-27-0854-karpathy-llm-wiki]]:** The earlier braindump focused on the architecture; this one focuses on the input layer.

### Strategic Implications
- Improving Readwise setup is low-effort, high-leverage infrastructure work — worth a dedicated session
- The payoff compounds: better inputs → better booklets → better patterns → better daily briefs
- Aligns with active projects: AI Damage Assessment PoC, MCP Governance, and Contact Centre of the Future all benefit from richer knowledge inflow on AI, agentic protocols, and enterprise architecture

## Suggested Source Setup

### Newsletters — High Priority (route into Readwise Reader)

| Source | Why |
|--------|-----|
| **The Batch** (Andrew Ng / DeepLearning.AI) | Weekly AI digest, practitioner-level signal |
| **Import AI** (Jack Clark) | Deep AI research news, foundation model updates |
| **Ben Evans' Newsletter** | Tech strategy, enterprise, AI implications |
| **Ethan Mollick / One Useful Thing** | AI-in-work practical insights — directly relevant to EA role |
| **Stratechery** (Ben Thompson) | Tech business strategy, AI platform dynamics |
| **The Pragmatic Engineer** (Gergely Orosz) | Engineering leadership, AI tooling in enterprise |
| **Lenny's Newsletter** | Product, AI in product — contact centre / customer experience relevance |
| **Architecture Notes** (Gregor Hohpe) | Enterprise architecture thinking |
| **Simon Willison's Blog** | MCP, agentic AI, LLM tooling — directly relevant to MCP Governance project |

### RSS Feeds — High Priority

| Source | Why |
|--------|-----|
| Anthropic Blog | Claude, MCP, agentic AI announcements |
| OpenAI Blog | Foundation model updates, platform strategy |
| Google DeepMind Blog | Gemini, computer vision, research |
| LeanIX Blog | EA tooling updates |
| a16z AI | Venture/strategic takes on AI market |

### Readwise Reader Config to Review
- Enable **Ghostreader** for auto-highlights on queued articles
- Set up **reading lists by topic** (tag: `#ai`, `#ea`, `#automotive`, `#cog`)
- Review **email newsletter routing** — forward key newsletters to Readwise Reader email address
- Set a **daily reading target** (even 15 minutes in Readwise Reader generates highlights for COG)

## Action Items

### Immediate (this week)
- [ ] Audit what newsletters are currently received by email — identify which should be re-routed to Readwise Reader 📅 2026-05-02
- [ ] Set up the 5 highest-priority newsletters in Readwise Reader 📅 2026-05-02
- [ ] Enable Ghostreader auto-highlighting if not already on 📅 2026-05-02

### Short-term (2 weeks)
- [ ] Add RSS feeds for Anthropic, OpenAI, DeepMind, LeanIX blogs 📅 2026-05-09
- [ ] Establish a reading cadence — 15 min/day in Readwise Reader minimum 📅 2026-05-09
- [ ] Review tagging strategy in Readwise to align with COG interest topics 📅 2026-05-09

### Strategic Considerations
- Consider scheduling /process-readwise weekly (Sunday) via cron once source setup is improved — the skill already supports this
- Revisit the 287 per-author tweet files once newsletter quality improves — many may become redundant if practitioner newsletters are covering the same ground

## Connections
- **Related Braindumps:** [[braindump-2026-04-27-0854-karpathy-llm-wiki]], [[braindump-2026-04-27-0955-karpathy-llm-wiki-tweet]]
- **Relevant Skills:** [[process-readwise]], [[daily-brief]]
- **Knowledge Base:** [[karpathy-llm-wiki-original-post-2026-04-27]]

## Domain Classification
- **Primary Domain:** Professional (95%)
- **Reasoning:** Knowledge infrastructure for work-relevant intelligence — directly supports active projects and EA role
- **Cross-Domain Elements:** Personal reading habits intersect — the setup benefits both work and personal interests
- **Privacy Level:** private

## Processing Notes

### Emotional Context
- **Energy Level:** Medium — practical, deliberate intent rather than excitement
- **Emotional Tone:** Intentional — this is infrastructure thinking, not ideation
- **Implications:** High follow-through likelihood when framed as setup work rather than ongoing commitment

### Confidence Assessment
- **Overall Analysis:** 90% — clear intent, strong context from session
- **Source Recommendations:** 80% — based on known interests; actual newsletter quality should be validated before committing
- **Action Timelines:** 85% — realistic given the setup nature of the work

---

*Processed by COG Braindump Skill — 2026-04-29 08:27*
