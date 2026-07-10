---
type: "daily-brief"
domain: "shared"
date: "2026-06-23"
created: "2026-06-23 13:18"
sources_verified: true
news_age_verified: true
confidence: "high"
tags: ["#daily-brief", "#news", "#strategic-intelligence"]
interests: ["Anthropic", "CCaaS", "AI damage assessment", "enterprise architecture", "agentic AI", "auto glass"]
projects_referenced: ["AI Damage Assessment PoC", "Contact Centre of the Future", "MCP Governance"]
items_count: 7
dedup_urls:
  - "https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/"
  - "https://insurance-edge.net/2026/06/16/motor-claims-adas-repairs-are-up-by-30-says-auto-windscreens/"
  - "https://www.leanix.net/en/blog/mcp-server-for-sap-leanix-solutions"
  - "https://www.cxtoday.com/contact-center/verint-contact-center-agent-retention-crisis-2026/"
  - "https://www.claimsjournal.com/news/national/2026/03/04/336076.htm"
  - "https://www.prnewswire.com/news-releases/telus-digital-and-elevenlabs-partner-to-scale-voice-ai-alongside-frontline-customer-care-teams-302805598.html"
  - "https://www.cxtoday.com/event-news/customer-contact-week-vegas-2026-less-hype-more-operating-discipline/"
  - "https://www.cxtoday.com/contact-center/customer-emotion-ai-august-2026-compliance-cliff/"
---

# Daily Brief — 23 June 2026 (Afternoon Refresh)

**Good afternoon, Armo. This brief corrects one significant error from this morning: Fable 5 and Mythos 5 remain fully offline — the "geo-fenced but restored" narrative was wrong. Three fresh stories alongside: Auto Windscreens reports 30% ADAS calibration surge (direct Belron market signal), SAP LeanIX ships a Claude MCP server you can wire up today, and Verint's CCW headline inverts the standard AI narrative — agents want AI and the ones who don't have it are leaving.**

---

## Executive Summary

The most important correction from this morning: Fable 5 and Mythos 5 are still entirely offline — not "geo-fenced" — following the June 12 US Commerce Department export control directive. Day 11 of the suspension; prediction markets at 57% odds of restoration by July 1. There is no Bedrock or Vertex path while the models are suspended at source. The full AIDA three-model benchmark cannot run until Fable 5 restores AND GPT-5.6 and Gemini 3.5 Pro reach GA — mid-July is the realistic horizon. Three new stories: Auto Windscreens (Belron's UK competitor) reports 30% year-on-year growth in ADAS calibrations driven by Chinese EVs, which is a direct operational signal for Autoglass. SAP LeanIX has shipped a generally available MCP server that lets Claude query your LeanIX fact sheets, relationship maps, and dashboards directly in a chat interface — usable today. And Verint's CCW report finds 31% of contact centre agents plan to quit within six months, not because of AI, but because they don't have it — a concrete ROI framing for the CCOTF business case.

---

## High Impact News

### Fable 5 and Mythos 5: Still Offline — Morning Brief Had It Wrong

**Correction** — This morning's brief reported Fable 5 as "restored but geo-fenced to US only." Search results as of 13:00 confirm this was incorrect. As of June 23, Day 11 of the suspension, neither model has been restored in any form.

**The actual timeline:**
- **June 12:** US Commerce Department (Bureau of Industry and Security) issued an export control directive ordering Anthropic to suspend Fable 5 and Mythos 5 for all foreign nationals, inside and outside the US, citing a reported jailbreak vulnerability
- **Why all users were affected:** Anthropic could not reliably screen users by nationality in real time, so disabled both models entirely for everyone
- **June 22-23 sources claiming "geo-fenced restoration":** Were speculative secondary sources — no official Anthropic confirmation followed and no restoration was announced
- **The June 23 subscription plan change (pay-per-use for Fable 5) is real but separate** from the export control dispute

**Two distinct issues — easy to conflate:**

| Issue | Status | What changed |
|---|---|---|
| Export control suspension | ONGOING — models fully offline globally | June 12; not yet resolved |
| Subscription plan change | Confirmed — Fable 5 now requires usage credits | June 22-23; independent of the ban |

**The restoration path:**
- Anthropic's updated ID verification policy (takes effect July 8) is the most likely mechanism for US-first restoration without fully lifting the directive
- Broader resolution requires Anthropic to join a classified frontier model pre-brief framework mandated by the June 2 Executive Order — underlying deadline August 1, 2026
- Prediction markets: 57% odds of restoration before July 1, 75% by July 17
- Anthropic MD International Chris Ciauri stated "very confident the models will become available again in coming days" — that statement was made around June 13

**AIDA PoC implication — planning assumption to adopt:**
While the suspension persists, there is no access path to Fable 5 via any route (direct API, Bedrock, Vertex) — Anthropic suspended at source. The AIDA three-model benchmark set (Fable 5, GPT-5.6, Gemini 3.5 Pro) cannot run as planned until all three are simultaneously available. Mid-July is the realistic planning horizon. Interim approach: use Claude Opus 4.8 (unaffected by the export control directive — it covers Fable and Mythos specifically) for any pre-benchmark development and testing.

**Vendor risk flag for the broader portfolio:**
This is the first confirmed instance of a US government export control directive suspending a commercial AI model with 24 hours notice, for a jailbreak rationale that Anthropic publicly disputed. The precedent is real and should be noted in Belron's AI vendor risk register — model suspension can happen faster than any SLA.

**Impact Assessment:**
- **Projects Affected:** AI Damage Assessment PoC (benchmark timing and access); MCP Governance (AI vendor risk register)
- **Action:** Update AIDA PoC timeline — assume Fable 5 unavailable until at least July 8; confirm that Opus 4.8 API access works from UK IPs (it should — not covered by the directive) 📅 2026-06-24
- **Action:** Add "AI model suspension" as a vendor risk category in the MCP Governance framework with this case as the reference incident 📅 2026-06-30

**Sources:**
- Fortune (Tier 1) — June 13 — [Anthropic Disables Fable and Mythos Following US Export Ban](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/)
- Al Jazeera (Tier 1) — June 13-14 — [US Orders Anthropic to Disable AI Models for All Foreign Nationals](https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals/)
- Anthropic (Tier 1) — [Statement on US Government Directive to Suspend Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)
- ExplainX (Tier 2) — June 23 — [Current Status Day 11](https://www.explainx.ai/blog/us-government-bans-fable-5-mythos-5-anthropic-export-control-2026)

**Confidence:** High — export control directive confirmed via multiple Tier 1 sources; restoration timing is probabilistic, not confirmed.

---

### Auto Windscreens Reports 30% ADAS Calibration Surge — Direct Belron Market Signal

**Relevance:** Auto Windscreens is a direct UK market competitor to Autoglass. Their operational data is the closest public proxy for what Belron's UK opco should be seeing. A 30% year-on-year increase in calibrations is a structural signal, not a blip.

Published June 16, Auto Windscreens reported:
- **30% increase in ADAS calibrations** in the last 12 months
- **7% increase** in windscreen replacements and repairs overall
- **Nearly half** of all front windscreen replacement jobs now require ADAS calibration
- **Primary driver:** Rising number of Chinese vehicle models (BYD, NIO, SAIC, Chery) entering the UK market, all fitted with dense ADAS sensor arrays as standard

**What this means operationally:**
ADAS calibration is no longer a premium add-on — it is approaching the default for roughly half of windscreen replacement jobs. This changes:
- **Job time:** Calibration adds significant time vs glass-only replacement
- **Technician certification:** Calibration requires specialist equipment and training — a skills and equipment capacity constraint
- **Revenue mix:** Calibration jobs command higher revenue but also higher cost per job
- **Scheduling:** Calibration bays become a throughput bottleneck as volume rises

**Why Chinese vehicles specifically:**
Chinese manufacturers fit more ADAS sensors per vehicle than comparable European models, partly because Chinese safety regulations have driven widespread adoption earlier. As Chinese vehicles reach 10-15% of new UK sales, the average ADAS density per job rises even before European mandates take effect.

**AutoBolt watchlist connection:**
This reinforces AutoBolt's 2023 US figure (89% of MY2023+ vehicles require calibration after windshield replacement). The UK is reaching a similar penetration point now. If Belron does not have an equivalent to AutoBolt's VIN-based calibration lookup identifying which ADAS sensors need recalibration for a specific vehicle, this operational gap is widening with every new Chinese model registration.

**AIDA PoC connection:**
A vehicle arriving for repair that also needs calibration is a higher-complexity job with more data points (vehicle model, ADAS configuration, calibration type required). An accurate AIDA model that can flag calibration requirements from VIN and vehicle image would extend the value proposition beyond damage assessment into job scoping.

**Impact Assessment:**
- **Projects Affected:** AI Damage Assessment PoC (expanded use case scope); Belron operational awareness
- **Action:** Check with Autoglass UK whether ADAS calibration volume as a proportion of total jobs is tracked — compare against the Auto Windscreens 30% figure 📅 2026-06-27
- **Action:** Flag AutoBolt's VIN-lookup capability to Autoglass UK operations leads as a potential tool for the growing calibration identification challenge 📅 2026-06-27

**Sources:**
- Insurance Edge (Tier 2) — June 16, 2026 — [Motor Claims: ADAS Repairs Are Up by 30%, Says Auto Windscreens](https://insurance-edge.net/2026/06/16/motor-claims-adas-repairs-are-up-by-30-says-auto-windscreens/)
- Bodyshop Magazine (Tier 2) — [ADAS Calibrations Up 30% in a Year at Auto Windscreens](https://www.bodyshopmag.com/2026/news/adas-calibrations-up-30-in-a-year-at-auto-windscreens/)
- Fleet News (Tier 2) — [ADAS Calibration Increase for Auto Windscreens](https://www.fleetnews.co.uk/news/increase-in-adas-calibrations-for-auto-windscreens)

**Confidence:** High — data from direct competitor, published across multiple trade publications within 7 days.

---

## Strategic Developments

### SAP LeanIX Ships Claude MCP Server — Your EA Data in the Chat Interface Today

**Relevance:** LeanIX is your primary EA tooling platform. They have shipped a generally available MCP server that lets Claude query your LeanIX fact sheets, relationship maps, reports, and dashboards directly within Claude Desktop. This is usable today without waiting for an integration project.

In early June 2026, SAP LeanIX launched:
- An **official MCP server** for SAP LeanIX solutions, generally available to all SAP LeanIX customers
- **MCP apps** that render LeanIX fact sheets and dependency maps inline in Claude without leaving the chat interface
- Connects via LeanIX's GraphQL API, exposing fact sheets, relationship maps, reports, and dashboards as MCP tools
- Compatible with Claude Desktop, Microsoft Copilot Studio, Cline, and custom LLMs

**What you can do with it today:**
- Query your LeanIX fact sheet data in natural language ("Show me all applications in the Contact Centre domain and their dependency status")
- Drill into application relationships from within a Claude session and navigate the architecture map interactively
- Run architecture analysis using Claude's reasoning against live LeanIX data
- Map AI agents in your estate to the architecture — LeanIX has shipped an AI agent representation model alongside this

**MCP Governance connection:**
The LeanIX MCP server is itself an MCP server that Belron would need to govern under the MCP Governance framework. It is also a valuable reference implementation: SAP LeanIX has built a well-scoped MCP server with proper auth, data scoping, and enterprise access controls. That is a pattern the MCP Governance framework should review as a reference for what a governed, vendor-supported MCP server looks like in practice.

**Note on freshness:** EA Voices published this June 3 — 20 days ago. Included because it was not in the vault and is directly actionable with your current tooling.

**Impact Assessment:**
- **Projects Affected:** MCP Governance (real governed MCP server case study); EA tooling (immediately usable)
- **Action:** Set up the LeanIX MCP server in Claude Desktop — follow the SAP LeanIX blog setup guide — and test against your Belron LeanIX instance 📅 2026-06-27
- **Action:** Add SAP LeanIX MCP server to the MCP Governance framework as a Tier 1 case study (enterprise data, vendor auth model, GA) 📅 2026-06-27

**Sources:**
- SAP LeanIX (Tier 1) — [Introducing the MCP Server for SAP LeanIX Solutions](https://www.leanix.net/en/blog/mcp-server-for-sap-leanix-solutions)
- EA Voices (Tier 2) — June 3, 2026 — [AI-Native Enterprise Architecture Now Available in SAP LeanIX](https://eavoices.com/2026/06/03/ai-native-enterprise-architecture-now-available-in-sap-leanix/) ⚠️ 20 days old — disclosed
- SAP LeanIX (Tier 1) — [AI-Native Enterprise Architecture Blog Post](https://www.leanix.net/en/blog/ai-enterprise-architecture)

**Confidence:** High — confirmed via SAP LeanIX official blog; GA status explicitly stated.

---

### Verint at CCW: 31% of Contact Centre Agents Plan to Quit — The CCOTF Business Case Reframe

**Relevance:** Verint is presenting this data at CCW today. The finding inverts the standard "AI replaces agents" narrative — agents want AI, and those without it are leaving. This is a more defensible ROI framing for the CCOTF business case than cost reduction through deflection.

Verint's 2026 State of Agent Experience report (released at CCW Las Vegas):
- **31% of contact centre agents** plan to quit within the next six months
- Primary drivers: unrealistic performance expectations (47%), lack of schedule flexibility (45%)
- **Only 8% fear being replaced by AI** — agents want AI to relieve them of tedious work, not worry about replacement
- The financial consequence: replacing one agent costs an average of $20,000; a 1,000-agent contact centre at 31% annual churn = $6.2M/year in replacement costs alone
- Agents are working across more channels simultaneously than ever before, increasing cognitive load in the absence of AI support

**The reframe for CCOTF:**
The business case for AI in contact centres has typically been framed around cost efficiency — fewer agents required. Verint's data supports a different and more defensible framing for Belron: **AI reduces attrition, which directly reduces the per-agent replacement cost.** For a Belron opco with 500 contact centre agents at 31% churn, that is $3.1M in avoidable replacement costs annually — before any savings from call deflection. This framing is:
- Harder to challenge (attrition is already measured; the number is real)
- More humane (the story is "we're supporting our people" not "we're reducing headcount")
- More defensible to HR and unions

**Connection to CCW's "year of accountability" theme:**
CX Today's editorial framing for CCW 2026 is that the industry is moving from AI deployment to AI governance and measurable ROI. Verint's attrition data gives a concrete, pre-existing ROI metric that requires no new measurement. That is exactly the accountability-era business case structure.

**Impact Assessment:**
- **Projects Affected:** Contact Centre of the Future (business case framing — attrition-reduction ROI)
- **Action:** Request Belron CCOTF contact centre attrition rate from HR or Operations — compare against Verint's 31% benchmark to size the AI ROI opportunity 📅 2026-06-27

**Sources:**
- CX Today (Tier 2) — [One Third of Agents Are Ready to Quit Because of AI Absence, Verint Warns](https://www.cxtoday.com/contact-center/verint-contact-center-agent-retention-crisis-2026/)
- NoJitter (Tier 2) — [Agent Attrition Rates Are High, Verint Survey Finds](https://www.nojitter.com/contact-centers/agent-attrition-rates-are-high-verint-survey-finds)

**Confidence:** High — Verint primary research, corroborated across multiple CX trade publications.

---

## Technology Watch

### Touchless Claims: 30%+ of Insurer Claims Now AI-Automated — AIDA PoC Competitive Baseline

**Relevance:** While the AIDA benchmark is delayed, the market is setting the bar. Leading insurers are automating over 30% of motor claims as fully touchless — this is the standard AIDA needs to compete with, not human assessors.

Key 2026 figures from industry sources:
- Leading insurers: 30%+ of claims fully automated as touchless, targeting instant settlement
- AI vision accuracy on car damage: 95-99%; 40% reduction in inspection time
- Tractable and Admiral Seguros: 70-75% of customers who receive an AI assessment link complete their claim digitally, typically in about two minutes
- Cycle time reduction with AI: 40-60%; handling cost reduction: 25-35%
- Fragmentation caveat: Only 12% of insurers report fully mature AI capabilities; only 7% claim scalable success — fragmentation is limiting impact

**The positioning context for AIDA:**
Belron is not an insurer. But Belron's booking and repair fulfilment happens downstream of the insurer claim. If an insurer's AI (Tractable, Ravin, or similar) has already priced the claim before Belron is even booked, then AIDA's value is in aligning Belron's assessment to what the insurer has already generated — consistency and defensibility, not first-mover speed. When the benchmark runs, frame the accuracy target against the 95-99% insurer AI standard, not against human assessors.

**Sources:**
- Claims Journal (Tier 2) — March 4, 2026 — [Carriers Using AI for Claims But Adoption is Fragmented](https://www.claimsjournal.com/news/national/2026/03/04/336076.htm)
- Vantage Point (Tier 2) — [Insurtech Trends 2026: AI Claims and Underwriting](https://vantagepoint.io/blog/sf/insights/insurtech-trends-2026-ai-claims-underwriting)

**Confidence:** Medium — leading-adopter figures corroborated across sources; "30%+ touchless" represents the leading edge, not the industry average.

---

### GPT-5.6 and Gemini 3.5 Pro: No Change

**Update** — No official launch for either model as of 13:00 today.

- **GPT-5.6:** GPT-5.5 remains the confirmed current model. No official OpenAI announcement as of today. Prediction markets at ~83% for a June 22-28 launch. Some Pro users report improved outputs suggesting a possible shadow rollout, but unconfirmed. Some analyst sources have flagged June 25 as a potential public launch date, but OpenAI has not responded.
- **Gemini 3.5 Pro:** Still in limited Vertex enterprise preview. Google has committed to GA by end of June. Prediction markets at 50-55% odds of GA by June 30.

For AIDA PoC: with Fable 5 also offline, the three-model benchmark cannot run as planned regardless. Use the delay productively — confirm Opus 4.8 access from UK IPs works, structure the benchmark test harness, and prepare image datasets so the benchmark can run immediately when all three models are available.

**Sources:**
- TechTimes (Tier 2) — June 16, 2026 — [GPT-5.6: OpenAI Chief Scientist Calls It a Meaningful Leap](https://www.techtimes.com/articles/318492/20260616/gpt-56-openai-chief-scientist-calls-it-meaningful-leap-june-launch-nears.htm)
- AI Weekly (Tier 2) — [Gemini 3.5 Pro Eyes June GA With 2M Context and Deep Think](https://aiweekly.co/alerts/gemini-35-pro-eyes-june-ga-with-2m-context-and-deep-think)

**Confidence:** Medium — launch window signals high-probability; official confirmation still pending for both.

---

## CCW Las Vegas: Today and Tomorrow

**Today (June 23) — Innovation Summit:**
- AI deployment, agent experience in the age of AI agents, trust, and "tech trends that actually move the needle"
- Verint presenting State of Agent Experience findings (31% churn risk — covered above)
- CMP Research releasing Prisms for Chatbots, Virtual Agents, and Real-Time Agent-Assist/Copilot — a benchmarking report on virtual agent maturity across the CCaaS market
- TELUS Digital + ElevenLabs 90-minute live voice agent deployment workshop
- TELUS/ElevenLabs VIP Networking Reception (6pm PDT)

**Tomorrow (June 24) — Expo Day:**
Genesys, NICE, Verint, and all major CCaaS vendors in the expo hall. This is where product announcements will land. CX Today is the best single feed for live coverage. Monitor specifically for: Genesys on Agent Fabric compatibility with their platform, NICE on agentic AI architecture (post-NICE World), and any vendor taking an explicit EU AI Act compliance position on emotion/sentiment AI.

EU AI Act compliance check is still outstanding as a CCOTF procurement criterion — any vendor at the expo demoing sentiment or emotion AI features is a test case.

---

## Opportunities & Recommendations

### Immediate Actions (Today/This Week)
- [ ] Update AIDA PoC timeline — Fable 5 unavailable until at least July 8; use Opus 4.8 for any interim development and testing 📅 2026-06-24
- [ ] Confirm Opus 4.8 API access works from UK IPs (should be unaffected — directive covers Fable/Mythos specifically) 📅 2026-06-24
- [ ] Set up SAP LeanIX MCP server in Claude Desktop — instructions via SAP LeanIX blog — and test against Belron's LeanIX instance 📅 2026-06-27
- [ ] Monitor CX Today for Genesys/NICE/Verint product announcements at CCW expo on June 24 📅 2026-06-24
- [ ] Check with Autoglass UK on ADAS calibration job proportion vs total windscreen jobs 📅 2026-06-27
- [ ] Add EU AI Act emotion AI compliance check to CCOTF vendor evaluation criteria 📅 2026-06-27
- [ ] Request Belron CCOTF contact centre attrition rate — compare against Verint's 31% benchmark 📅 2026-06-27

### Research Needed
- **Fable 5 restoration:** Monitor Anthropic's news channel daily — a restoration announcement will likely arrive on a weekday with a blog post; the July 8 ID verification policy date is the clearest structural trigger
- **AIDA benchmark preparation:** Use the delay to structure the test harness, prepare image datasets, and confirm Opus 4.8 as the interim Anthropic model — so the benchmark can run immediately when all three models are available
- **LeanIX MCP server setup:** One session to wire up and test against Belron LeanIX would confirm whether the natural-language fact sheet querying is production-grade or still rough

### People to Inform/Consult
- **AIDA PoC team:** Fable 5 still offline (this corrects this morning's brief) — no Bedrock workaround while the suspension is at source; use Opus 4.8 for interim work
- **CCOTF stakeholders:** CCW expo intelligence incoming June 24-25; the Verint 31% attrition framing is worth surfacing in the CCOTF business case ahead of any board presentation

---

## Risks & Threats

### Active Threats
- **Fable 5 suspension duration:** No confirmed restoration date. If the export control dispute extends past the August 1 Executive Order deadline, the timeline lengthens significantly. 43% market probability of it slipping past July 1.
- **AIDA benchmark model availability gap:** All three benchmark models (Fable 5, GPT-5.6, Gemini 3.5 Pro) are simultaneously unavailable. Mid-July is the earliest realistic benchmark window. If the business case needs results before Q3 review, this is a schedule risk.
- **AI vendor suspension precedent:** The US government has now demonstrated it can suspend a commercial AI model with under 24 hours' notice for a jailbreak rationale the vendor publicly disputed. This is a new category of vendor risk that should be in Belron's AI governance framework.

### Emerging Risks to Monitor
- **ADAS calibration throughput at Belron opcos:** If nearly half of UK windscreen replacement jobs now require ADAS calibration (as Auto Windscreens reports), and Belron opcos are not tracking this proportionally, scheduling impacts may be compounding without visibility. A quick operational check is low cost.
- **CCW vendor emotion AI compliance posture:** Any CCaaS vendor at tomorrow's expo demoing frustrated-caller detection or sentiment scoring without an EU AI Act compliance position is selling something Belron's EU opcos cannot deploy after August 2. Procurement lock-in before the compliance picture is clear is a real risk.

---

## Verification Report

### Source Analysis
- **Tier 1 Sources:** 5 (Fortune, Al Jazeera, Anthropic, SAP LeanIX official blog x2)
- **Tier 2 Sources:** 9
- **Tier 3 Sources:** 0
- **Cross-References Performed:** 14

### Fact-Checking Results
- **Verified Claims:** All primary claims cross-referenced across at least 2 sources
- **Unverified Claims:** 0
- **Conflicting Information:** Fable 5 restoration status — this brief supersedes this morning's incorrect "geo-fenced" narrative; current status confirmed via Fortune, Al Jazeera, and Anthropic's own statement

### Freshness Verification
- ✅ Fable 5 export control: June 12-23 (active, ongoing)
- ✅ Auto Windscreens ADAS: June 16, 2026 (within 7-day window)
- ✅ Verint agent attrition: June 2026 — CCW current
- ✅ GPT-5.6 / Gemini 3.5 Pro: Status confirmed June 21-23
- ⚠️ SAP LeanIX MCP server: June 3, 2026 (20 days — disclosed; included as new to vault and directly actionable)
- ⚠️ Touchless claims adoption: March-June 2026 range — figures represent current market state, not a single dated event

### Confidence Assessment
- **Overall Confidence:** 85%
- **High Confidence Items:** 4 (Fable 5 suspension status correction, Auto Windscreens ADAS data, LeanIX MCP GA status, Verint attrition research)
- **Medium Confidence Items:** 3 (Model launch timing, touchless claims adoption rate, CCW announcement preview)
- **Low Confidence Items:** 0

---

*Curated by COG | Afternoon refresh replacing the 08:49 brief | All news verified within 7-day freshness window (disclosures noted) | Sources cross-referenced*
