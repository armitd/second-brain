---
type: "braindump"
domain: "professional"
date: "2026-06-30"
created: "2026-06-30 09:14"
themes: ["subscriptions", "news-intelligence", "tooling-decisions"]
tags: ["#braindump", "#raw-thoughts", "#professional", "#subscriptions"]
status: "resolved"
energy_level: "low"
emotional_tone: "curious"
confidence: "high"
consolidated_in: "[[consolidation-2026-07-18]]"
consolidated_date: "2026-07-18"
---

# Braindump: Subscription Review — AlignedNews vs TBD

## Raw Thoughts

Subscriptions - alignednews vs TBD ?

**Follow-up context (2026-06-30):** Cost is the driver. Actively reviewing all subscriptions. Currently paying:
- **Every.to** — subscribed, like both the tools and content
- **TBD community** — member, like the content (£25 pcm)
- **AlignedNews** — questioning value ($25 pcm). Wondering if WebSearch/WebFetch alone would cover the same ground without the cost.

## Content Analysis

### Main Themes
1. **Cost-driven subscription audit:** Reviewing all paid tools against value delivered — not a single cancellation decision, a broader discipline
2. **AlignedNews on trial:** $25 pcm questioned against what WebSearch/WebFetch already delivers for free in the daily brief
3. **Keepers identified:** Every.to (tools + content) and TBD community (£25 pcm content) are both valued — these are not under review

### Supporting Ideas
- AlignedNews is the current Tier 2 news source in the daily brief (via MCP tool), sitting alongside free WebSearch/WebFetch
- The attribution bug (ERRORS.md, 2026-05-21) means AlignedNews stories already require manual correction — adds friction without unique value
- Every.to offers both content (essays, podcasts) and tools — dual value justifies cost
- TBD community is a peer/learning network — different value type (community vs intelligence feed)

### Questions Raised
- Would the daily brief quality drop meaningfully if AlignedNews was removed and replaced with additional WebSearch calls?
- Is there an alternative curated AI/tech feed at lower cost or free? (e.g. TLDR.tech, Import AI, Ben Thompson's Stratechery, Axios Pro AI)
- Is $25 pcm the actual cost or has it increased?

### Decisions Contemplated
- Cancel AlignedNews and absorb the gap with improved WebSearch prompting in the daily brief skill
- Keep AlignedNews but reduce other subscriptions elsewhere
- Replace AlignedNews with a free-tier alternative (RSS, newsletters) integrated into the brief pipeline

## Strategic Intelligence

### Key Insights
1. **AlignedNews is the weakest link in the subscription stack:** Every.to and TBD both have clear, multi-dimensional value (content + community). AlignedNews is a single-function feed with a known attribution bug and a $25 pcm price tag — easiest candidate to cut.
2. **The daily brief already has free alternatives:** WebSearch and WebFetch cover direct source fetching. The AlignedNews MCP adds curation and aggregation — but that layer could be approximated with better search prompting or free newsletter digests.
3. **Dropping AlignedNews requires a brief skill update:** The daily-brief skill makes explicit calls to the AlignedNews MCP tools. Cancellation means either removing those calls or replacing them with a free equivalent — a 30-minute code change, not a blocker.

### Pattern Recognition
- This is the second tooling evaluation captured recently (cf. LeanIX MCP, Miro MCP) — pattern of auditing the COG tool stack
- The ERRORS.md attribution issue for AlignedNews was first noted 2026-05-21 — this braindump may be the follow-through

### Strategic Implications
- If AlignedNews is replaced, the daily-brief skill will need updating to swap the MCP tool calls
- A self-hosted RSS + summarisation approach would remove vendor dependency but add maintenance overhead
- Worth defining evaluation criteria before researching alternatives

## Action Items

### Completed
- [x] Analysed last 5 daily briefs for AlignedNews contribution — 0 stories in 3 of 5 briefs; X/Twitter signals only when used 📅 2026-06-30
- [x] Moved AlignedNews to Disabled in MY-INTEGRATIONS.md — daily brief will skip it from next run 📅 2026-06-30

### Remaining
- [x] Cancel AlignedNews subscription ($25 pcm saving) 📅 2026-06-30

### Strategic Considerations
- Every.to and TBD are both confirmed keepers — no action needed
- No replacement needed — WebSearch covers the gap

## Connections
- **Related Braindumps:** [[braindump-2026-06-30-0818-cog-launchd-fixes]]
- **Knowledge Base:** [[ERRORS.md]] (AlignedNews attribution bug, 2026-05-21)

## Domain Classification
- **Primary Domain:** Professional (90%)
- **Reasoning:** Directly relates to COG tooling used for professional intelligence gathering
- **Privacy Level:** public

## Processing Notes
### Confidence Assessment
- **Overall Analysis:** 90% — context clarified, decision direction clear
- **Domain Classification:** 90% — professional tooling / personal subscription management overlap
- **Areas Requiring Clarification:** None outstanding — next step is the trial run

---

*Processed by COG Brain Dump Analyst*
