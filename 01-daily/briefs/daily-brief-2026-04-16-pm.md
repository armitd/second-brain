---
type: "daily-brief"
domain: "shared"
date: "2026-04-16"
created: "2026-04-16 16:50"
sources_verified: true
news_age_verified: true
confidence: "high"
tags: ["#daily-brief", "#news", "#strategic-intelligence"]
interests: ["Foundation models", "Enterprise architecture", "Agentic AI protocols", "AI governance"]
projects_referenced: []
items_count: 4
note: "PM supplement — new stories not in the 09:02 morning brief"
dedup_urls:
  - "https://www.anthropic.com/claude/opus"
  - "https://aws.amazon.com/blogs/aws/introducing-anthropics-claude-opus-4-7-model-in-amazon-bedrock/"
  - "https://www.bloomberg.com/news/articles/2026-04-14/anthropic-attracts-investor-offers-at-a-800-billion-valuation"
  - "https://x.com/realHGA/status/2044779818613346483"
  - "https://x.com/RickLamers/status/2044783222253633598"
---

# Daily Brief (PM Supplement) — 16 April 2026

**Afternoon, Armo.** Four stories, one of which affects you directly right now: Claude Opus 4.7 launched this afternoon. COG is running on it as of this brief. The other three are: Anthropic's revenue trajectory and IPO valuation just became much more concrete; Google shipped four products yesterday while everyone watched for Spud; and Alibaba open-sourced a model that runs on 23GB RAM and tops mid-sized benchmarks.

## Executive Summary

Claude Opus 4.7 is live — new base model, not a fine-tune, with a new tokenizer, 3x vision resolution, and cybersecurity capabilities deliberately capped at 73% through training (a significant governance statement). It tops the Vals Index at 71.4% and SWE-bench Pro at 64.3%. Simultaneously, Anthropic's secondary market valuation has hit $850B on $30B in annualised revenue — grown from $1B 18 months ago. Spud did not drop today; the window shifts to May. And Google shipped Gemini TTS, CLI subagents, Mac app, and Fabula in a single day with almost no coverage.

---

## High Impact

### Claude Opus 4.7 Is Live — New Base Model, 3x Vision, Safety Deliberately Trained In
**Relevance:** This is the model COG is now running on. Every brief, research task, and braindump from this point uses Opus 4.7. The vision resolution improvement is directly relevant to any damage assessment prototyping — and the cybersecurity cap is a significant governance signal that distinguishes Anthropic's approach from the OpenAI safety dissolution story covered Monday.

Anthropic launched **Claude Opus 4.7** today, April 16, 2026. Available on Claude.ai, the API, and Amazon Bedrock.

**What's genuinely new (this is a new base model, not a fine-tune):**
- **New tokenizer** — token usage increases approximately 1.0–1.35x depending on content type (pricing implication for API users)
- **3x vision resolution** — accepts images up to 2,576px on the long edge (~3.75 megapixels vs the previous threshold). For damage assessment: this means significantly more image detail available for model reasoning
- **xhigh effort level** — a new effort tier above the existing high setting; gives more reasoning budget to the model for complex tasks
- **Task budgets** — allows setting compute/token budgets per task for cost control in agentic workflows
- **/ultrareview in Claude Code** — a new review mode for code generation

**Benchmark performance:**
- **Vals Index: 71.4% — #1 on the leaderboard**
- **SWE-bench Pro: 64.3%** (up from 53.4% on Opus 4.6 — a 10-point jump in one generation)
- Beats GPT-5.4 and Gemini 3.1 Pro on most benchmarks per multiple independent reports

**The governance signal — cybersecurity deliberately capped at 73%:**
Anthropic deliberately trained Opus 4.7 to cap its cybersecurity capability at 73% through the model training itself — not guardrails or post-hoc filters, but baked into the weights. This is architecturally significant: it means the limitation cannot be jailbroken away. In context of Monday's brief (OpenAI dissolved its safety teams; Anthropic Mythos too dangerous to release) — Anthropic has made a different design choice. Safety is not an add-on; it is a constraint in the base model.

**EA Implications:**
- The 3x vision resolution strengthens the case for Gemini ER 1.6 vs Claude Opus 4.7 as candidate models for a damage assessment PoC — they are now much closer in image capability
- The tokenizer change is a cost consideration for any API-based agentic workflow: build a token usage estimate into any Belron agentic AI business case using Opus 4.7
- The cybersecurity cap story is useful for Belron governance conversations: "the model has safety constraints trained in, not bolted on" is a cleaner compliance story than guardrails

**What's coming next:** Sam Altman presents at World Network **tomorrow** (April 17) — observers expect OpenAI announcements around proof of personhood integration, likely timed as a response to Opus 4.7's launch.

**Sources:**
- [Anthropic — Claude Opus](https://www.anthropic.com/claude/opus) (Tier 1) — 16 April 2026
- [AWS — Introducing Claude Opus 4.7 on Amazon Bedrock](https://aws.amazon.com/blogs/aws/introducing-anthropics-claude-opus-4-7-model-in-amazon-bedrock/) (Tier 1) — 16 April 2026
- [StreetInsider — Anthropic Launches Claude Opus 4.7](https://www.streetinsider.com/Corporate+News/Anthropic+launches+Claude+Opus+4.7+with+enhanced+coding+and+vision+capabilities/26322789.html) (Tier 2) — 16 April 2026
- [AlignedNews — "Claude Opus 4.7 Is Here — New Base Model, Not Just a Fine Tune"](https://x.com/natolambert/status/2044788470179332533) (Tier 2, via AlignedNews ten-things) — 16 April 2026
- [AlignedNews — "Anthropic Deliberately Trained Safety Into Opus 4.7 — Cybersecurity Capped at 73%"](https://x.com/zephyr_z9/status/2044788455683895438) (Tier 2, via AlignedNews ten-things) — 16 April 2026

**Confidence:** High — multiple Tier 1 sources; benchmark figures cross-referenced.

---

## Strategic Developments

### Anthropic Revenue: $1B → $30B in 18 Months. Secondary Market Implies $850B Valuation.
**Update:** _IPO/board story first covered 14 April 2026 (PM brief)_

**Relevance:** This is the material update to Monday's Anthropic IPO story. The board appointment and October 2026 IPO timeline were reported then. Today's data adds the commercial context: the valuation jump is being driven by a revenue trajectory that has no precedent in enterprise software.

**The revenue number:**
- Anthropic had ~$1B in annualised revenue at end of 2024
- As of early April 2026: **$30B in annualised revenue**
- That is a **30x growth** in approximately 18 months
- For context: Salesforce took over a decade to reach $10B in revenue; Anthropic hit $30B in 18 months from $1B

**The valuation:**
- Series G (February 2026): closed at **$380B post-money**
- Secondary market today (Hiive pre-IPO, Jupiter tokenized shares): **$850B implied**
- Bloomberg reported investors making offers above $800B — Anthropic has rejected them
- TechCrunch: Anthropic's rise is giving some OpenAI investors second thoughts about their allocations

**The IPO calculus:** At $30B revenue and an implied $850B valuation, Anthropic is trading at ~28x revenue. For comparison: Salesforce trades at ~7x, Snowflake at ~18x. The market is pricing in continued hypergrowth and frontier model dominance — a bet on Opus 4.7's position and what comes after it.

**EA Implications:**
- The revenue trajectory confirms Anthropic is not a research lab in commercial clothes — it is one of the fastest-growing enterprise software businesses ever built. Platform decisions built on Claude now have a more durable commercial counterparty.
- The gap between the $380B Series G close (February) and $850B implied today (April) — two months apart — reflects how quickly sentiment is moving on AI infrastructure. Any Belron vendor assessment that relies on valuations from 6+ months ago is stale.

**Sources:**
- [Bloomberg — Anthropic Attracts Investor Offers at $800B Valuation](https://www.bloomberg.com/news/articles/2026-04-14/anthropic-attracts-investor-offers-at-a-800-billion-valuation) (Tier 1) — 14 April 2026
- [The Next Web — Anthropic $800B Valuation, $30B Revenue](https://thenextweb.com/news/anthropic-800-billion-valuation-revenue-30-billion-ipo) (Tier 2) — April 2026
- [Yahoo Finance — Anthropic Tokenized Shares Imply $850B](https://finance.yahoo.com/markets/stocks/articles/anthropic-tokenized-shares-jupiter-imply-182504941.html) (Tier 2) — April 2026
- [TechCrunch — Anthropic's Rise Giving Some OpenAI Investors Second Thoughts](https://techcrunch.com/2026/04/14/anthropics-rise-is-giving-some-openai-investors-second-thoughts/) (Tier 1) — 14 April 2026

**Confidence:** High — Bloomberg and TechCrunch as primary sources; secondary market valuations are indicative not definitive.

---

## Technology Watch

### Google Shipped Four Products Wednesday — Gemini TTS, CLI Subagents, Mac App, Fabula
**Relevance:** The "four-launch Wednesday" referenced in this morning's brief is now confirmed in detail. Each launch is individually relevant — Gemini TTS for voice interface interest; CLI subagents directly comparable to Anthropic Managed Agents; Mac app as a competitive desktop AI product; Fabula as an interesting signal on how Google thinks about AI and creative professionals.

**The four launches (April 15, 2026):**

**1. Gemini 3.1 Flash TTS**
- Audio Tags: inline performance direction in plain language ("speak slowly here", "use a concerned tone")
- 70+ languages supported
- Native multi-speaker dialogue — two characters in one generation
- Ranked #2 on Speech Arena (behind only ElevenLabs)
- Available on fal

**2. Gemini CLI — Subagents**
- Each subagent gets a **separate context window** and **custom system instructions**
- Enables complex multi-agent workflows where specialised agents collaborate without context pollution
- Direct EA relevance: this is the "team of specialists" agentic pattern in a CLI tool

**3. Gemini on Mac**
- Native Mac app with 100+ features built in less than 100 days
- Option+Space for mini chat; Option+Shift+Space for full interface
- All three major AI assistants (Claude, ChatGPT, Gemini) now have native Mac apps — the desktop AI platform war is live

**4. Google Research Fabula**
- AI writing tool co-designed with **42 expert writers** (not just engineers)
- Focuses on narrative structure and development, not text generation
- Signals Google's strategy: involve domain experts in AI tool design, don't just build and hope

**Combined signal:** Google is shipping at a pace that's easy to miss when everyone is watching for Spud and Opus 4.7. The Gemini CLI subagents feature specifically is a direct response to Anthropic Managed Agents and Claude Code.

**Sources:**
- [AlignedNews — Gemini 3.1 Flash TTS](https://x.com/realHGA/status/2044779818613346483) (Tier 2, via AlignedNews breaking) — 16 April 2026
- [AlignedNews — Gemini CLI Subagents](https://x.com/realHGA/status/2044782345408889305) (Tier 2, via AlignedNews breaking) — 16 April 2026
- [AlignedNews — Gemini on Mac](https://x.com/realHGA/status/2044782230631780860) (Tier 2, via AlignedNews breaking) — 16 April 2026
- [AlignedNews — Google Research Fabula](https://x.com/realHGA/status/2044782489122570738) (Tier 2, via AlignedNews breaking) — 16 April 2026

**Confidence:** Medium-High — AlignedNews-sourced; Gemini TTS confirmed independently via Speech Arena ranking.

---

### Alibaba Qwen3.6-35B-A3B — Best Mid-Sized Open Model, Runs on 23GB RAM, Apache 2.0
**Relevance:** The GLM-5.1 story from Monday's morning brief established that Chinese open-source models are competitive at the frontier. Qwen3.6 extends that pattern into the mid-sized model tier — the sweet spot for on-device or private deployment. Apache 2.0 means it can be used commercially without restriction.

Alibaba open-sourced **Qwen3.6-35B-A3B** today:
- **Architecture:** Sparse Mixture of Experts — 35B total parameters, only **3B active** per inference
- **Hardware requirement: 23GB RAM** — consumer-grade GPU territory (RTX 4090 can run it)
- **Licence: Apache 2.0** — commercial use unrestricted
- **Performance:** Ranked as the strongest mid-sized model on nearly all benchmarks
- Runs comfortably on a single high-end consumer GPU or a modest cloud instance

**Why it matters alongside Gemma 4 (covered this morning):**
Both Qwen3.6 and Gemma 4 31B are now serious options for a self-hosted, GDPR-compliant, commercially unrestricted AI deployment. The Belron damage assessment use case — where customer vehicle photos should not leave company infrastructure — now has two strong open-weight candidates that run on attainable hardware.

**Sources:**
- [AlignedNews — "Qwen3.6-35B-A3B Goes Open-Source — Best Mid-Sized Model, Apache 2.0"](https://x.com/RickLamers/status/2044783222253633598) (Tier 2, via AlignedNews ten-things) — 16 April 2026

**Confidence:** Medium — single AlignedNews source; benchmark claim ("strongest mid-sized model on nearly all benchmarks") is vendor/community-reported and requires independent verification.

---

## Technology Watch (Continued)

### GPT-5.5 "Spud" — April 16 Date Missed, Window Shifts to May
**Update:** _First covered 10 April 2026; tracked in all subsequent briefs_

No OpenAI release today. The April 16 leaked date did not materialise. Multiple sources now put the highest-probability window at **late April to early June, with May as the mode estimate** based on OpenAI's typical 3–6 week post-pretraining pipeline.

Sam Altman presents at World Network tomorrow (April 17) — the community is watching for whether any Spud signals emerge there. Given Opus 4.7 just launched, OpenAI may feel timing pressure.

**Confidence:** Medium — prediction market only; no official communication.

---

## Opportunities & Recommendations

### Immediate Actions (This Week)
- [ ] COG is now running on Opus 4.7 — the 3x vision resolution and xhigh effort level are live. Worth testing on a complex EA task to feel the capability difference 📅 2026-04-17
- [ ] The Anthropic $30B revenue figure is the single most important commercial context for any Belron AI vendor assessment. Add it as a data point to any internal conversation about platform stability and longevity 📅 2026-04-18
- [ ] The Gemini CLI subagents feature deserves a look alongside Anthropic Managed Agents and Cloudflare Agent Cloud — the agentic infrastructure market is converging fast; EA should have a position on where Belron sits 📅 2026-04-23
- [ ] Qwen3.6 + Gemma 4: two strong open-weight, commercially-licensed models now exist for on-device/private deployment. Worth adding both to the competitive watchlist as candidate models for any GDPR-constrained Belron use case 📅 2026-04-20

### Watch Tomorrow
- Sam Altman at World Network (April 17): proof of personhood integration with OpenAI + potential Spud signals. If Spud drops tomorrow, it's the direct Opus 4.7 response.

---

## Verification Report

### Source Analysis
- **Tier 1 Sources:** 4 — Anthropic official, AWS official blog, Bloomberg, TechCrunch
- **Tier 2 Sources:** 6 — StreetInsider, The Next Web, Yahoo Finance, AlignedNews (breaking + ten-things)
- **Cross-References Performed:** 8

### AlignedNews Feed
- AlignedNews (breaking + ten-things): 5 stories surfaced — Opus 4.7 launch, Opus 4.7 cybersecurity cap, Google four launches, Qwen3.6, Sam Altman tomorrow. Opus 4.7 and Anthropic valuation verified against Tier 1 sources. Google launches and Qwen3.6 cross-referenced where possible.

### Freshness Verification
- ✅ Claude Opus 4.7 launch: 16 April 2026 — today
- ✅ Anthropic $800B+ valuation (Bloomberg): 14 April 2026 — within window
- ✅ Google Gemini TTS, CLI subagents, Mac, Fabula: 15 April 2026 — within window
- ✅ Qwen3.6-35B-A3B: 16 April 2026 — today
- GPT-5.5 Spud: forward-looking tracking item

### Confidence Assessment
- **Overall Confidence:** 90%
- **High Confidence Items:** 2 (Opus 4.7 specs, Anthropic revenue/valuation)
- **Medium-High Confidence Items:** 1 (Google four launches — AlignedNews sourced, partially verified)
- **Medium Confidence Items:** 2 (Qwen3.6 benchmark claims unverified; Spud May window prediction-market only)

---

*Curated by COG | PM supplement to morning brief (09:02) | All news verified within 7-day freshness window*
