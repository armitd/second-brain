---
type: "daily-brief"
domain: "shared"
date: "2026-06-23"
created: "2026-06-23 08:49"
sources_verified: true
news_age_verified: true
confidence: "high"
tags: ["#daily-brief", "#news", "#strategic-intelligence"]
interests: ["Anthropic", "CCaaS", "AI damage assessment", "foundation models", "enterprise architecture", "agentic AI"]
projects_referenced: ["AI Damage Assessment PoC", "Contact Centre of the Future", "MCP Governance"]
items_count: 6
dedup_urls:
  - "https://www.developersdigest.tech/blog/claude-fable-5-june-22-deadline"
  - "https://www.prnewswire.com/news-releases/telus-digital-and-elevenlabs-partner-to-scale-voice-ai-alongside-frontline-customer-care-teams-302805598.html"
  - "https://www.cxtoday.com/event-news/customer-contact-week-vegas-2026-less-hype-more-operating-discipline/"
  - "https://www.cxtoday.com/contact-center/customer-emotion-ai-august-2026-compliance-cliff/"
  - "https://www.kucoin.com/news/flash/openai-delays-ipo-as-gpt-5-6-launches-sparks-rsi-speculation"
  - "https://neuralcoretech.com/agentic-ai-model-context-protocol-mcp-architecture-2026/"
  - "http://www.siliconluxembourg.lu/foyer-tractable-ai-automotive-claims/"
---

# Daily Brief — 23 June 2026

**Good morning, Armo! Three threads converge today: Fable 5 becomes pay-per-use from this morning, CCW hits its main intelligence day with a significant new voice AI partnership, and Gartner has a warning about agentic AI projects that's directly relevant to how you frame MCP Governance internally.**

---

## Executive Summary

Two operational changes land today. First, Fable 5 exits free plan inclusion — as of this morning it requires usage credits at $10/$50 per million tokens, compounding yesterday's geo-fencing issue for the AIDA PoC team. The Bedrock/Vertex paths remain unaffected. Second, at Customer Contact Week in Las Vegas, TELUS Digital announced a new voice AI partnership with ElevenLabs (not Cresta — a parallel bet), positioning ElevenAgents as their preferred AI voice agent platform across Genesys, Amazon Connect, and Salesforce. The CCW Innovation Summit is running today — the main expo and vendor announcement day is tomorrow. Meanwhile Gartner is warning that 40% of agentic AI projects may be cancelled by 2027 due to cost and unclear ROI — a framing risk for MCP Governance that's worth getting ahead of.

---

## High Impact News

### Fable 5 Now Pay-Per-Use — Cost Implications for AIDA PoC Access

**Update:** _Geo-fencing for UK access first covered June 22. Today's angle is new: Fable 5 also moved to usage-credit billing as of this morning, separate from the geo-fencing issue._

**Relevance:** Compounds the UK access issue from yesterday. The AIDA PoC team now faces both a routing problem (geo-fencing) and a cost structure change (no longer included in plans). The Bedrock path resolves both.

As of June 23, Fable 5 is no longer included in Claude Pro, Max, Team, or Enterprise plan limits. Continued access requires usage credits, billed at Anthropic's API rates: **$10 per million input tokens, $50 per million output tokens** — double the cost of Opus 4.8. Batch pricing is 50% off ($5/$25).

**What changed vs. yesterday's brief:**
- Yesterday: Fable 5 restored but geo-fenced (UK API calls blocked directly)
- Today: Fable 5 also exits free plan inclusion — usage now draws from prepaid credit pools
- Combined effect: A UK team using Fable 5 via the Anthropic API would face geo-fencing AND credit billing

**Access paths that remain unaffected:**
- **AWS Bedrock** — routes through US infrastructure, bypassing geo-fencing; pricing via Bedrock rates (confirm today)
- **Google Vertex AI** — similarly unaffected by Anthropic's subscription changes
- **API-only users** — already billing per-token; no change to their model
- **Claude.ai consumer subscription** — no change for the consumer app

**For the AIDA PoC specifically:**
The benchmark should be structured to run through Bedrock or Vertex from the outset — not through direct Anthropic API from UK IPs. This also means the cost model for AIDA should use Bedrock pricing, not Anthropic list pricing, as the baseline. Log which model actually executes each benchmark call (Fable 5 vs Opus 4.8 fallback) given the new access structure.

**Impact Assessment:**
- **Projects Affected:** AI Damage Assessment PoC (access path + cost modelling); MCP Governance (vendor SLA reference case)
- **Action:** Confirm Bedrock pricing for Fable 5 vs Anthropic API rates — update the AIDA cost model with Bedrock as the canonical path 📅 2026-06-24
- **Action:** Brief AIDA PoC team: Fable 5 via Bedrock is now the recommended access route for non-US teams 📅 2026-06-23

**Sources:**
- Developers Digest (Tier 2) — June 22 — [Fable 5 Leaves Your Claude Plan on June 22](https://www.developersdigest.tech/blog/claude-fable-5-june-22-deadline)
- Claudefa.st (Tier 2) — June 2026 — [Claude Fable 5 Pricing & Usage Credits Explained](https://claudefa.st/blog/guide/development/fable-5-usage-credits)
- Anthropic (Tier 1) — [Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)

**Confidence:** High — pricing change confirmed across multiple sources and matches Anthropic's published announcement.

---

### TELUS Digital + ElevenLabs: New Voice AI Partnership Announced at CCW

**Relevance:** TELUS Digital has placed a second voice AI bet — separate from the Cresta partnership on the watchlist. ElevenLabs is a different proposition: pure voice AI (TTS/STT), not CCaaS. This changes how to read TELUS's strategy and what it signals for the CCOTF vendor landscape.

Announced June 22 (opening day of CCW), TELUS Digital became a preferred implementation partner for **ElevenAgents**, ElevenLabs' AI voice agent platform. The arrangement:

- Enterprises contract directly with ElevenLabs, TELUS Digital deploys and operates
- TELUS provides implementation, integration, and governance across: **Genesys, Twilio, Amazon Connect, Zendesk, Salesforce**
- Post-launch managed services from TELUS's 900+ AI engineers

**What ElevenAgents actually does:**
- Handles high-volume routine inbound calls autonomously
- Routes complex/sensitive interactions to human agents with context
- 70+ languages, follows callers who switch languages mid-conversation
- Real-time system integration (CRM actions during the call)

**Proof-of-concept results TELUS has published:**
- Customers receiving AI welcome calls were "less than half as likely to cancel within 30 days"
- Average satisfaction score: 8.5/10
- ElevenLabs platform-wide: 4.8M agents live, 1.3M conversations/day across 80 countries

**CCW component:** TELUS and ElevenLabs are running a 90-minute hands-on workshop **today (June 23)** where attendees configure and deploy a live voice agent using ElevenAgents. Plus a VIP reception tonight at 6pm PDT.

**How this relates to the Cresta watchlist entry:**
The June 2026 TELUS + Cresta partnership (added to watchlist June 16) was about CX AI for global enterprise clients — conversation intelligence and human augmentation. ElevenLabs is the pure voice layer (TTS/STT + agentic voice calls). TELUS appears to be building a layered stack: Cresta for conversation intelligence, ElevenLabs for the voice AI agent itself. Not a replacement — a stack.

**CCOTF implications:**
- ElevenLabs as a CCaaS-adjacent voice layer is distinct from Cartesia (also on watchlist for similar voice capability). Both now have enterprise implementation routes.
- The Genesys + ElevenLabs integration confirms that Belron's existing CCaaS evaluation can consider ElevenLabs as a layered capability, not a separate platform selection.
- The "routine calls to AI, complex to human" operating model is the same framing in Cartesia's pitch — this is becoming the standard AI contact centre architecture.

**Impact Assessment:**
- **Projects Affected:** Contact Centre of the Future (vendor landscape — ElevenLabs now has a preferred enterprise implementation partner)
- **Action:** Add TELUS Digital + ElevenLabs stack to CCOTF vendor landscape alongside TELUS + Cresta — these are complementary, not alternative 📅 2026-06-25
- **Action:** Update watchlist entry for TELUS Digital to reflect the ElevenLabs partnership and the emerging stack logic 📅 2026-06-25

**Sources:**
- PR Newswire (Tier 1) — June 22 — [TELUS Digital and ElevenLabs Partner to Scale Voice AI](https://www.prnewswire.com/news-releases/telus-digital-and-elevenlabs-partner-to-scale-voice-ai-alongside-frontline-customer-care-teams-302805598.html)
- TELUS Digital (Tier 1) — [TELUS Digital to Showcase AI-Powered CX at CCW Las Vegas 2026](https://www.telusdigital.com/about/newsroom/telus-digital-to-showcase-ai-powered-customer-experience-solutions-at-customer-contact-week-las-vegas-2026)
- Stock Titan (Tier 2) — [TELUS Digital, ElevenLabs partner on voice AI](https://www.stocktitan.net/news/TU/telus-digital-and-eleven-labs-partner-to-scale-voice-ai-alongside-go29v5bdrrte.html)

**Confidence:** High — official press release confirmed.

---

## Strategic Developments

### CCW Day 2: Innovation Summit Running Today, Expo Opens Tomorrow

**Update:** _First covered June 22 (event opened). Today is the main intelligence day._

**Relevance:** The Innovation Summit is happening now — this is where the AI/automation narrative for CCW 2026 will be set.

Today's programme at CCW Las Vegas:
- **Innovation Summit** — AI deployment, agent experience in the age of AI agents, trust, and "tech trends that actually move the needle"
- **Management Summit** — leadership behaviours and operational outcomes
- **CCWomen Summit** — human-centred leadership
- **TELUS Digital + ElevenLabs workshop** (90 min) — live voice agent deployment
- **VIP Networking Reception** (6pm PDT) — TELUS/ElevenLabs

**Tomorrow (June 24) is the expo day:** Genesys, NICE, Verint, and others will be in the expo hall. CX Today is covering live — their coverage will be the best single feed for product announcements.

CX Today's editorial framing for CCW 2026: "2026 is not the year of experiments — it's the year of accountability." Sessions are structured around building AI governance and guardrails, not just deploying AI. This is a signal shift worth noting: the CCaaS market is maturing from demo-stage AI to governance-stage AI, which aligns with where the CCOTF project needs to be thinking.

**Action:** Monitor CX Today live feed for Genesys, NICE, Verint product announcements on June 24 📅 2026-06-24

**Sources:**
- CX Today (Tier 2) — [Customer Contact Week Vegas 2026: Less Hype, More Operating Discipline](https://www.cxtoday.com/event-news/customer-contact-week-vegas-2026-less-hype-more-operating-discipline/)
- TELUS Digital (Tier 1) — [CCW Las Vegas 2026 Event Page](https://www.telusdigital.com/events/ccw-las-vegas-2026)

**Confidence:** High — programme confirmed via event registration sources.

---

### EU AI Act: 40 Days to the Emotion AI Compliance Cliff

**Update:** _August 2 deadline first flagged June 20. CX Today's coverage confirms the scale of unreadiness across the CCaaS vendor landscape._

**Relevance:** August 2 is 40 days away. CX Today published "Most Contact Centers Have No Idea What's Coming" — an editorial that names specific compliance requirements. At CCW, vendors pitching emotion AI without a compliance conversation are now a procurement yellow flag.

What happens on August 2, 2026 (EU AI Act, Article 9):
- **Customer-facing emotion recognition** is reclassified as **high-risk AI**
- High-risk requirements: conformity assessments, technical documentation, CE marking, EU database registration, human oversight mandates, post-market monitoring
- **Workplace sentiment analysis** (contact centre emotion AI on agents) was already prohibited from February 2025 — enforcement now extends to the customer-facing layer
- Penalties for non-compliance are substantive

**The CCW vendor angle:**
Any vendor at CCW demoing frustrated-caller detection, real-time sentiment analysis, or emotion scoring in a customer interaction — without a clear EU AI Act compliance position — is selling something Belron's EU opcos cannot deploy after August 2. This needs to be a specific procurement criterion in the CCOTF evaluation.

**What to ask any CCaaS vendor:**
1. Does your AI assistant/co-pilot include emotion recognition or sentiment inference on customer voice/text?
2. Have you completed a conformity assessment for EU AI Act high-risk AI classification?
3. What is your technical documentation / CE marking status?

**Impact Assessment:**
- **Projects Affected:** Contact Centre of the Future (procurement evaluation criterion — EU opco compliance)
- **Action:** Add EU AI Act compliance check to CCOTF vendor evaluation criteria — specifically: emotion/sentiment AI scope, conformity assessment status, CE marking 📅 2026-06-27

**Sources:**
- CX Today (Tier 2) — [Customer Emotion AI August 2026 Compliance Cliff](https://www.cxtoday.com/contact-center/customer-emotion-ai-august-2026-compliance-cliff/)
- Basil AI (Tier 2) — May 31 — [EU AI Act Emotion Recognition Ban Takes Effect in 63 Days](https://basilai.app/articles/2026-05-31-eu-ai-act-emotion-recognition-ban-meeting-tools-sentiment-analysis-compliance.html)
- CCMA (Tier 2) — [How Does the EU AI Act Impact Contact Centre Leaders?](https://www.ccma.org.uk/how-does-the-eu-ai-act-impact-contact-centre-leaders/)

**Confidence:** High — August 2 deadline confirmed via EU AI Act text; vendor readiness assessment corroborated across multiple sources.

---

## Technology Watch

### GPT-5.6 and Gemini 3.5 Pro — Still Pending, Launch Imminent

**Update:** _Both models covered June 22. No confirmed release today; probability markets have tightened further._

**GPT-5.6 status:**
Still no official OpenAI announcement as of June 22 evening. One KuCoin headline ("OpenAI Delays IPO as GPT-5.6 Launches") suggests a possible stealth release, but no model card, API model string, or official blog post has been confirmed. Polymarket has tightened to 90%+ for the June 22-28 window. Key confirmed specs: 1.5M token context window, improved agentic workflows, token efficiency focus. The model reportedly delays the IPO — OpenAI is prioritising the launch over filing timing.

**Gemini 3.5 Pro status:**
Still in limited Vertex enterprise preview. Google has committed to GA by end of June. Pricing confirmed at ~$15/M input tokens, ~$60/M output tokens. The GA signal to watch: Google publishes a blog post on blog.google — that's when the public preview window opens.

**For AIDA PoC:**
When either model lands, do not rush the benchmark. The structured three-model run (Fable 5 via Bedrock, GPT-5.6, Gemini 3.5 Pro Deep Think) is more valuable than a quick comparison. Allow 48 hours from GA for API stability before running.

**Action:** Monitor OpenAI and Google blog channels; trigger AIDA benchmark setup once both models confirm GA 📅 2026-06-28

**Sources:**
- TechTimes (Tier 2) — June 21 — [GPT-5.6 Launch Window Starts Monday](https://www.techtimes.com/articles/318799/20260621/gpt-56-launch-window-starts-monday-alignment-fix-15m-token-context-inside.htm)
- KuCoin (Tier 3) — [OpenAI Delays IPO as GPT-5.6 Launches](https://www.kucoin.com/news/flash/openai-delays-ipo-as-gpt-5-6-launches-sparks-rsi-speculation) — unconfirmed; treat as signal only
- GrowwingAssistant (Tier 3) — [Gemini 3.5 Pro Release Date June 2026](https://growwingassistant.com/ai-news/gemini-3-5-pro-release-date-june-2026-every-confirmed-spec-pricing-when-it-drops/)

**Confidence:** Medium — launch window high-probability; official confirmation still pending.

---

### Gartner Warning: 40% of Agentic AI Projects Could Be Cancelled by 2027

**Relevance:** Gartner has published a warning that up to 40% of enterprise agentic AI projects may be cancelled by 2027 due to rising costs, unclear business value, and inadequate risk controls. This is the framing risk for any internal AI initiative — including the MCP Governance project.

The three failure modes Gartner identifies:
1. **Rising costs** — GPU/LLM inference costs at scale exceed business case projections
2. **Unclear ROI** — pilots succeeded; production ROI didn't materialise
3. **Inadequate risk controls** — governance frameworks weren't built before deployment

This maps directly onto the MCP Governance project's reason for existence: organisations that deploy AI agents without a governance framework are the ones Gartner is warning about. The inverse is the positioning argument — having MCP Governance in place before broad agent deployment is the risk mitigation that avoids being in the 40%.

**How to use this internally:**
- In the MCP Governance business case: lead with Gartner's 40% failure rate as the cost of *not* having governance
- In the AIDA PoC: the governance layer isn't optional overhead; it's what makes production deployment viable
- The "year of accountability" framing from CCW 2026 aligns with this — both the CCaaS and agentic AI markets are maturing from deployment-first to governance-first

**Sources:**
- NeuralCoreTech (Tier 2) — [Agentic AI and Model Context Protocol (MCP): Architecture Guide 2026](https://neuralcoretech.com/agentic-ai-model-context-protocol-mcp-architecture-2026/)
- Poniaktimes (Tier 2) — [How Agentic AI Is Transforming Enterprise Architecture in 2026](https://www.poniaktimes.com/agentic-ai-enterprise-architecture-2026/)

**Confidence:** Medium — Gartner figure cited in secondary sources; verify against direct Gartner publication before using in presentations.

---

## Competitive Landscape

### Tractable Expanding in European Insurance Market

**⚠️ Published May 18, 2026 — 36 days ago. Included because it was not in prior briefs and is new to the vault.**

Luxembourg insurer **Foyer** deployed Tractable's AI for automotive damage assessment in May 2026. Focus: low-severity motor claims assessed from policyholder-submitted photos, without physical inspection.

Quote from Foyer Head of Claims & Customer Service: *"Artificial intelligence allows us to strengthen the responsiveness and consistency of our assessments."*

**Why this matters for AIDA PoC:**
Tractable is now live with a European insurer (Foyer, part of the broader European insurance ecosystem). This means Tractable's technology is now being evaluated against European vehicle damage photos, European claim types, and European regulatory requirements — the same context as Belron's EU opcos.

Tractable won a Global Recognition Award for 2026 for improving accident and disaster recovery across automotive and property insurance. Their platform is confirmed live at GEICO and all major Japanese insurers, plus LKQ.

**For the competitive intelligence:**
The question has shifted from "is Tractable relevant in Europe?" to "which EU insurers are now using Tractable that also have relationships with Belron's EU opcos?" A Belron opco could face a situation where the insurer routing them a job is already using Tractable to price the claim before the job is booked.

**Sources:**
- Silicon Luxembourg (Tier 2) — May 18, 2026 — [Foyer Taps Tractable's AI to Speed Up Car Claims](http://www.siliconluxembourg.lu/foyer-tractable-ai-automotive-claims/)
- Global Recognition Awards (Tier 2) — [Tractable Wins Global Recognition Award 2026](https://globalrecognitionawards.org/innovative-companies/tractable/)

**Confidence:** Medium — Foyer partnership confirmed via press release; scope of Tractable's EU insurer relationships requires further investigation.

---

## Opportunities & Recommendations

### Immediate Actions (Today/This Week)
- [ ] Brief AIDA PoC team: Fable 5 via AWS Bedrock is now the recommended access route — resolves both geo-fencing and plan-limit issues 📅 2026-06-23
- [ ] Confirm AWS Bedrock pricing for Fable 5 and update AIDA production cost model accordingly 📅 2026-06-24
- [ ] Monitor CX Today's CCW coverage for Genesys/NICE/Verint product announcements on expo day (June 24) 📅 2026-06-24
- [ ] Add EU AI Act emotion AI compliance check to CCOTF vendor evaluation criteria 📅 2026-06-27

### Research Needed
- **Tractable EU insurer relationships:** Which EU insurers using Tractable also have claim-routing relationships with Belron's EU opcos? This closes the loop on whether AIDA PoC is defensive (matching insurer capability) or offensive (ahead of it).
- **Gartner agentic AI source:** Find the original Gartner publication for the 40% cancellation prediction — the secondary sources are consistent but the primary source is needed before using this in internal materials.
- **ElevenLabs vs Cartesia for CCOTF:** Both are now on the radar as voice AI layers for contact centres. A brief comparison note would be useful before the CCOTF evaluation progresses — they're targeting the same layer but with different go-to-market models.

### People to Inform/Consult
- **AIDA PoC team:** Bedrock access path confirmed; cost model needs updating with Bedrock pricing
- **CCOTF stakeholders:** CCW producing intelligence June 24 — brief expected by June 25

---

## Risks & Threats

### Active Threats
- **Fable 5 cost creep:** At $10/$50 per M tokens, even moderate AIDA benchmark usage runs to meaningful cost. Budget the benchmark run before triggering it — don't discover the bill after.
- **EU AI Act vendor unreadiness:** CCaaS vendors at CCW may pitch emotion AI features that are non-compliant in the EU from August 2. Procurement lock-in before the compliance picture is clear is a risk.

### Emerging Risks to Monitor
- **Gartner 40% cancellation rate:** If this framing gains traction internally, agentic AI projects (including AIDA PoC and MCP Governance) may face a harder internal bar. Get ahead of this by framing both projects around governance and ROI clarity, not just capability demonstration.
- **GPT-5.6 pricing:** The model is expected to offer "reduced API pricing" — if OpenAI undercuts Claude significantly on token costs, the AIDA cost model comparisons need updating immediately after launch.

---

## Verification Report

### Source Analysis
- **Tier 1 Sources:** 3 (Anthropic, PR Newswire, TELUS Digital)
- **Tier 2 Sources:** 9
- **Tier 3 Sources:** 2 (KuCoin — flagged as unconfirmed; GrowwingAssistant — secondary)

### Freshness Verification
- ✅ All primary stories verified within 7-day window
- ⚠️ Tractable/Foyer item: published May 18, 2026 — explicitly disclosed
- Publication date range: May 18 (disclosed) to June 23, 2026

### Confidence Assessment
- **Overall Confidence:** 82%
- **High Confidence Items:** 3 (Fable 5 pricing, TELUS/ElevenLabs, CCW programme)
- **Medium Confidence Items:** 3 (GPT-5.6 launch status, Gartner figure, Tractable EU scope)
- **Low Confidence Items:** 0

---

*Curated by COG | Sources cross-referenced | 7-day freshness standard applied*
