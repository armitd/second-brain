---
type: "daily-brief"
domain: "shared"
date: "2026-07-23"
created: "2026-07-23 07:00"
sources_verified: true
news_age_verified: true
confidence: "high"
tags: ["#daily-brief", "#news", "#strategic-intelligence"]
interests: ["Foundation models", "Agentic AI platforms and protocols (MCP, A2A)", "AI damage assessment technology", "Enterprise architecture", "Automotive industry", "Contact Centre Technology"]
projects_referenced: ["AI Damage Assessment PoC", "MCP Governance", "Contact Centre of the Future"]
items_count: 2
dedup_urls: ["https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/", "https://ground.news/article/gemini-35-pro-is-testing-with-partners-have-begun-pre-training-run-for-gemini-4-pro-google", "https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/"]
---

# Daily Brief - 2026-07-23

**Good morning, Armo!**

## Executive Summary
Google shipped three new Gemini "Flash" models this week but again withheld Gemini 3.5 Pro — the piece still missing from the AI Damage Assessment PoC's three-model benchmark set — while quietly confirming pre-training has already begun on Gemini 4. Separately, MCP's Enterprise-Managed Authorization extension has reached stable status, giving MCP Governance a concrete answer for how enterprises centralise access control across MCP servers. Beyond those two, it's another quiet week: Belron/IPO, Anthropic, LeanIX, AI damage assessment vendors, and Contact Centre CCaaS all show no material new developments — several candidate stories were checked and discarded as stale or already covered (see Verification Report).

---

## High Impact News

### Update: Gemini 3.5 Pro still delayed — Google ships three Flash models instead, confirms Gemini 4 pre-training underway
**Relevance:** *First covered 2026-07-22.* Directly affects the AI Damage Assessment PoC's three-model benchmark set (Claude Fable 5, GPT-5.6, Gemini 3.5 Pro) — Gemini remains the missing piece, and Google is now visibly moving its attention to the next model generation rather than confirming a near-term Pro date.

TechCrunch reported (21 July) that Google DeepMind released three new efficiency-focused models — Gemini 3.6 Flash (its new "workhorse" model, up to 17% fewer output tokens and up to 65% cost savings on long-horizon engineering tasks per corroborating reporting, priced at $1.50/$7.50 per million input/output tokens), Gemini 3.5 Flash-Lite, and a government/partner-only Gemini 3.5 Flash Cyber — while Gemini 3.5 Pro remains in partner testing with no release date. Google DeepMind product lead Logan Kilpatrick said the team is "currently testing Gemini 3.5 Pro with partners" and hopes to "land soon," but also disclosed that Google has begun its "most ambitious pre-training run yet" for Gemini 4 — a signal that Pro's delay may be less about an imminent fix and more about resource reallocation toward the next generation.

**Impact Assessment:**
- **Projects Affected:** AI Damage Assessment PoC (three-model benchmark set), Belron AI advocacy narrative
- **Potential Effects:** The benchmark comparison remains effectively two-model (Claude Fable 5 vs. GPT-5.6) with no near-term resolution in sight. The Gemini 4 pre-training disclosure raises a real possibility that Google may leapfrog 3.5 Pro entirely rather than ship it — worth factoring into any PoC timeline that assumes Gemini 3.5 Pro will eventually arrive.
- **Action Suggested:** Consider formally deciding to proceed with the two-model comparison (Fable 5 vs. GPT-5.6) for the next PoC readout, with Gemini flagged as "pending, timeline uncertain" rather than "imminent."

**Sources:**
- TechCrunch (Tier 1) - 2026-07-21 - [Google releases three new Gemini models — but no 3.5 Pro](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)
- Ground News aggregation (Tier 2, corroborating) - 2026-07-23 - [Gemini 3.5 Pro is testing with partners; Google begins pre-training run for Gemini 4](https://ground.news/article/gemini-35-pro-is-testing-with-partners-have-begun-pre-training-run-for-gemini-4-pro-google)

**Confidence:** High — primary Tier 1 report corroborated by independent aggregation citing the same Kilpatrick quotes and pricing detail.

---

## Strategic Developments

### ⚠️ Older item, included with disclosure: MCP's Enterprise-Managed Authorization extension reaches stable status
**Publication date:** 6 July 2026 — 11 days outside the 7-day window, but not previously covered in this vault and directly relevant to the MCP Governance project ahead of the 28 July final specification release already being tracked.

**Relevance:** Gives MCP Governance a concrete, adopted answer for centralising authentication across MCP servers — directly relevant scope for the framework being built.

The Enterprise-Managed Authorization (EMA) extension centralises MCP server authentication through an organisation's existing identity provider rather than per-user, per-server consent prompts. It uses an Identity Assertion JWT Authorization Grant (ID-JAG) that an IdP exchanges for access tokens, giving a "single log in" experience where users inherit access to servers their organisation has already approved. Notably, EMA governs *connection* access only — it does not inspect MCP traffic after a token is issued, so organisations still need their own runtime controls for what an agent does once inside a system (the same gap Noma and Microsoft Agent 365 are positioned to fill). Real-world adoption is already reported across Anthropic, Microsoft, Okta, and numerous MCP servers, which is what drove the promotion to stable.

**Strategic Implications:**
- EMA solves the *connection-layer* authorization problem for MCP Governance; it explicitly does not solve runtime/behavioural governance — reinforces that Belron's framework still needs a distinct answer for in-session enforcement (the Noma / Agent 365 layer), not just access provisioning.
- Adoption by Anthropic, Microsoft, and Okta specifically is a useful signal that this is becoming the default enterprise pattern, not a niche proposal — worth citing if the MCP Governance framework needs to justify aligning with a standard extension rather than building bespoke access control.
- Lands five days before the 28 July final MCP specification release already on the MCP Governance team's calendar — worth checking whether EMA is folded into that release or remains a separate extension track.

**Sources:**
- InfoQ (Tier 2) - 2026-07-06 - [AI Model Context Protocol Adds Centralised Auth for Enterprise](https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/)

**Confidence:** Medium-High — single trade-press source, but reporting is specific (named adopters, technical mechanism) and consistent with the broader MCP specification direction already tracked from official sources in prior briefs.

---

## Competitive Landscape

### Belron / D'Ieteren IPO — quiet week
No new reporting since 2026-07-21. Same "early-stage talks, H2 2026 target, Amsterdam-or-New-York, ~€32bn enterprise value" status confirmed across outlets, none newly dated this week.

### Anthropic — quiet week
No Anthropic news dated within the 16–23 July window. Checked and confirmed several candidates are recycled or already-covered older items (see Verification Report) — Claude Enterprise admin analytics/spend alerts (2 July), Cowork expansion (7 July), memory redesign (10 July), monthly recap settings (9 July), and HIPAA self-serve config (14 July) all predate the window and/or were already discarded in the 2026-07-22 brief.

### LeanIX — quiet week
SAP LeanIX Exploration Workshops in San Francisco ran 21–22 July; no new product or strategy news beyond previously tracked AI Agent Hub / Enterprise Architecture Assistant positioning.

### AI Damage Assessment vendors (Tractable, Ravin.ai, Audatex/Solera) — quiet week
No new dated announcements this week; general market-overview content only.

### Contact Centre CCaaS (Genesys, Salesforce Agentforce Contact Center, Zoom) — quiet week
No material update since the Pinkfish acquisition (announced 30 June, rollout through Genesys AppFoundry expected by end of Genesys FY27 Q2, i.e. by 31 July 2026) — worth a calendar note to check for a rollout announcement in the next week or two, but nothing new this week itself.

### Auto glass / ADAS — no new items
A candidate story on rising ADAS-related auto glass claims was checked and confirmed to be a general industry overview dated March 2026, not new reporting; discarded. The "Safelite ending Service Auto Glass wholesale" story resurfaced in search again this week and was re-confirmed (as in the 2026-07-22 brief) to be recycled January 2021 content — discarded again.

---

## Opportunities & Recommendations

### Immediate Actions (Today/This Week)
- [ ] Decide whether to formally proceed with a two-model (Fable 5 vs. GPT-5.6) AI Damage Assessment PoC benchmark readout, flagging Gemini 3.5 Pro as "pending, timeline uncertain" given the Gemini 4 pre-training disclosure 📅 2026-07-25
- [ ] Add MCP Enterprise-Managed Authorization (EMA) to the MCP Governance framework's scope as the connection-layer/access-provisioning answer, distinct from runtime enforcement (Noma/Agent 365) 📅 2026-07-30

### Research Needed
- Whether Google formally abandons Gemini 3.5 Pro in favour of jumping to Gemini 4 — worth a dedicated check next week.
- Whether the 28 July MCP specification final release folds in EMA or keeps it as a separate extension track.

### People to Inform/Consult
- **AI Damage Assessment PoC stakeholders:** Gemini 3.5 Pro's continued absence and the Gemini 4 pre-training signal, ahead of any PoC readout.
- **MCP Governance project team:** EMA extension as a candidate access-control layer, and its explicit non-coverage of runtime enforcement.

---

## Risks & Threats

### Active Threats
- None new this week.

### Emerging Risks to Monitor
- If Google skips Gemini 3.5 Pro entirely in favour of Gemini 4, the PoC's "three foundation models" framing needs a firmer contingency plan rather than continuing to wait indefinitely.

---

## Verification Report

### Source Analysis
- **Tier 1 Sources:** 1 — TechCrunch
- **Tier 2 Sources:** 2 — Ground News (aggregation, corroborating), InfoQ
- **Cross-References Performed:** 3 (Gemini story corroborated across TechCrunch + Ground News aggregation citing consistent Kilpatrick quotes and pricing; EMA extension checked against MCP specification direction already tracked from official sources in prior briefs)

### Fact-Checking Results
- **Verified Claims:** 2 (Gemini Flash releases + Pro delay; MCP EMA stable status)
- **Unverified Claims:** 0
- **Conflicting Information:** 0

### Freshness Verification
- ✅ 1 of 2 items verified within the 7-day window (Gemini update, 21–23 July)
- ⚠️ 1 item (MCP EMA extension) published 6 July 2026 — 11 days outside the window, included with explicit disclosure given direct relevance to MCP Governance and no prior coverage in this vault
- Publication date range: 2026-07-06 to 2026-07-23

### Candidates checked and discarded (duplicate or stale)
- Safelite "Service Auto Glass" wholesale closure — resurfaced in search again this week; re-confirmed as recycled January 2021 content (same finding as 2026-07-22 brief)
- Auto glass ADAS claims rise (autofreak.com) — dated March 2026, general overview with no original data; discarded
- Microsoft Project Perception "622 patches" detail (beri.net, 18 July) — attributes the metric to the underlying MDASH scanner (released 15 July), not to Project Perception itself; no new confirmed Project Perception launch or metrics this week, so folded out rather than treated as a fresh headline
- Claude Enterprise admin analytics/spend alerts (2 July), Cowork expansion (7 July), memory redesign (10 July), monthly recap settings (9 July), HIPAA self-serve config (14 July) — all outside the 7-day window; several already discarded in the 2026-07-22 brief
- Salesforce Agentforce Contact Center GA — already tracked (23 Feb 2026 GA), no new development this week
- Genesys $1.5bn Salesforce/ServiceNow investment — dated July 2025, already flagged stale in the 2026-07-20 brief

### Confidence Assessment
- **Overall Confidence:** 88%
- **High Confidence Items:** 1 (Gemini update)
- **Medium Confidence Items:** 1 (MCP EMA extension — single trade-press source, older item)
- **Low Confidence Items:** 0

---

## Complete Sources

### Technology Watch
1. TechCrunch - [Google releases three new Gemini models — but no 3.5 Pro](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)
2. Ground News - [Gemini 3.5 Pro is testing with partners; Google begins pre-training run for Gemini 4](https://ground.news/article/gemini-35-pro-is-testing-with-partners-have-begun-pre-training-run-for-gemini-4-pro-google)
3. InfoQ - [AI Model Context Protocol Adds Centralised Auth for Enterprise](https://www.infoq.com/news/2026/07/mcp-ema-enterprise-auth/)

### Competitive Intelligence (checked, not included)
1. Beri.net - [622 Patches in One Month. Microsoft Just Open-Sourced the Weapon.](https://www.beri.net/article/microsoft-mdash-project-perception-multi-model-ai-vulnerability-hunting-enterprise-security-2026) — MDASH metric, not Project Perception itself
2. Autofreak.com - Auto Glass Repair Claims Rise with Advanced Sensor Integration in 2026 — dated March 2026, discarded
3. glassBYTEs.com - Safelite to Close Business Unit — dated January 2021, resurfaced again, discarded

---

*Curated by COG News Curator | All news verified within 7-day freshness window unless explicitly disclosed otherwise | Sources cross-referenced for accuracy*
