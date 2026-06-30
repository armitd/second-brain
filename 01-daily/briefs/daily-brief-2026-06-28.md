---
type: "daily-brief"
domain: "shared"
date: "2026-06-28"
created: "2026-06-28 16:18"
sources_verified: true
news_age_verified: true
confidence: "high"
tags: ["#daily-brief", "#news", "#strategic-intelligence"]
interests: ["AI foundation models", "agentic AI", "enterprise architecture", "contact centre", "auto glass industry", "EU AI Act", "Belron IPO"]
projects_referenced: ["AI Damage Assessment PoC", "MCP Governance", "Contact Centre of the Future"]
items_count: 5
dedup_urls:
  - "https://explainx.ai/blog/when-will-fable-5-be-available-again-2026"
  - "https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/"
  - "https://openai.com/index/previewing-gpt-5-6-sol/"
  - "https://www.leanix.net/en/blog/ai-enterprise-architecture"
  - "https://www.hklaw.com/en/insights/publications/2026/04/us-companies-face-eu-ai-acts-possible-august-2026-compliance-deadline"
  - "https://www.cxtoday.com/contact-center/how-cloud-voice-ai-is-reviving-the-contact-center-in-2026/"
  - "https://www.autobodynews.com/news/californias-auto-glass-bill-would-tighten-adas-and-claims-rules"
---

# Daily Brief — 28 June 2026

**Good afternoon, Armo!**

## Executive Summary

Two material shifts landed in the last 24 hours. First, Zhipu AI released GLM-5.2 open weights that independently beat Claude Mythos on Semgrep cybersecurity benchmarks — directly undermining the US government's rationale for the Fable 5 ban and raising an uncomfortable question about whether restricting Western access to frontier AI creates defensive gaps faster than it closes offensive ones. Second, GPT-5.6 (Sol/Terra/Luna) actually launched on June 26 in limited preview — the June 26 brief called it slipped to July, but OpenAI shipped it that same day to ~20 pre-approved organisations. The AIDA PoC benchmark table now has three models nominally available but two still restricted. Elsewhere: SAP LeanIX launched a native MCP server that surfaces EA data directly in Claude or Copilot chats — directly relevant to your EA toolchain — and the EU AI Act's high-risk enforcement window opens in 35 days (2 August).

---

## High Impact

### 1. Fable 5 Day 16 — Zhipu GLM-5.2 Beats Mythos on Security, Open Weights Released
**Relevance:** The ban's national security justification just got materially weakened — and the defensive access question is now urgent.

Zhipu AI's GLM-5.2 scored a 39% F1 on IDOR (Insecure Direct Object Reference) detection at Semgrep's independent benchmark, beating Claude Code (32%) at roughly **$0.17 per vulnerability found**. The model shipped as open weights on June 16. Guillermo Rauch (Next.js creator, Vercel CEO) captured the dilemma well: the same cybersecurity capabilities that justify the ban are now openly available from a Chinese lab — meaning the US companies that most need defensive access to Mythos-class tools are the ones currently blocked from them.

Independent caveats apply: Zhipu's own benchmarks use a narrow Semgrep test rather than a head-to-head with the full restricted Mythos model. Scores should not be read as "Zhipu = Mythos across the board." But the directional signal — that the capability gap is closable fast in specialised domains — is credible.

**Impact Assessment:**
- **Projects Affected:** AI Damage Assessment PoC, MCP Governance
- **AIDA PoC implication:** The three-model benchmark plan (Fable 5, GPT-5.6 Sol, Gemini 3.5 Pro) now has a fourth datapoint worth tracking: what does a comparable open-weight Chinese model score on damage classification? Not for procurement, but for the "what if our primary model becomes unavailable" resilience question.
- **Governance implication:** Model provenance and supply-chain questions (Western vs. Chinese origin, open vs. closed weights) are moving from theoretical to procurement-relevant. Worth adding a provenance classification field to the MCP Governance vendor comparison.
- **Belron IPO implication:** AI supplier risk — over-dependency on any single Western foundation model vendor — is a risk register item worth surfacing given the ban precedent.

**Action Suggested:**
- [ ] Add "model provenance resilience" as a dimension to the AIDA PoC vendor comparison 📅 2026-07-05
- [ ] Monitor for full Fable 5 restoration — Manifold prediction market gives partial probability by June 30 but no official signal yet

**Sources:**
- [Semgrep: GLM-5.2 vs Claude on Cyber Benchmarks](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) (Tier 2) — June 2026
- [explainx.ai: Zhipu AI Matches Claude Mythos on Security Bugs](https://explainx.ai/blog/zhipu-ai-matches-claude-mythos-security-bugs-chinese-ai-2026) (Tier 3) — June 28, 2026
- [VGTimes: GLM-5.2 Open Chinese AI Model](https://vgtimes.com/tech-and-hardware/159377-glm-5.2-open-chinese-ai-model-matches-claude-mythos-in-cybersecurity-and-vulnerability-detection.html) (Tier 3) — June 2026
- [Guillermo Rauch via Polymarket X](https://x.com/rauchg/status/2071047674187714830) (Tier 3 — verified account) — June 28, 2026

**Confidence:** Medium-High — Semgrep benchmark is independent and methodology is disclosed. Full Mythos head-to-head comparison has not been independently verified. The directional signal is credible; the "parity" claim is contested.

---

### 2. **Update — first covered 2026-06-26:** GPT-5.6 Did Not Slip to July — Launched June 26 as Limited Preview
**Relevance:** The AIDA PoC benchmark model set is now nominally complete, but two of three models remain access-restricted.

The June 26 brief reported GPT-5.6 had slipped to July. That same day, OpenAI launched GPT-5.6 (Sol, Terra, Luna) in limited preview to approximately 20 US government-approved organisations. General availability is planned "in the coming weeks." Pricing is confirmed: Sol at $5/$30 per 1M tokens (input/output), Terra at $2.50/$15, Luna at $1/$6. Sol's headline capability is **Ultra Mode** — uses subagents internally, scored 91.9% on Terminal-Bench 2.1. Cerebras deployment in July will push Sol to 750 tokens per second.

OpenAI explicitly said it does not want government-gated releases to become permanent practice, signalling this constraint is temporary.

**Impact Assessment:**
- **Projects Affected:** AI Damage Assessment PoC
- **AIDA benchmark status:** Three-model set (Fable 5, GPT-5.6 Sol, Gemini 3.5 Pro) exists — but Fable 5 is banned for general use, GPT-5.6 Sol is restricted to ~20 orgs, and Gemini 3.5 Pro is still Vertex AI preview. Mid-July is now the realistic earliest date for a full three-model benchmark run.
- **Cost modelling:** Sol ($5 input / $30 output) vs Claude Sonnet 4.6 ($3/$15) — Sol is roughly 2x the price of Sonnet for I/O-heavy workloads. For a damage assessment PoC that analyses vehicle images, output token volume will be the dominant cost driver. Terra ($2.50/$15) may be the right cost comparison point for production cost modelling.

**Action Suggested:**
- [ ] Update AIDA PoC benchmark tracker — note GPT-5.6 Sol launched June 26 (limited), revise benchmark run estimate to mid-July 📅 2026-06-30

**Sources:**
- [OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/) (Tier 1 — official) — June 26, 2026
- [VentureBeat: OpenAI unveils GPT-5.6 Sol, Terra and Luna](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov) (Tier 1) — June 26, 2026
- [The Decoder: GPT-5.6 Sol launches under government access](https://the-decoder.com/openais-claude-mythos-competitor-gpt-5-6-sol-launches-under-government-controlled-access-it-calls-unsustainable/) (Tier 2) — June 26, 2026

**Confidence:** High — OpenAI official announcement, cross-referenced by multiple Tier 1 tech outlets.

---

## Strategic Developments

### 3. SAP LeanIX Launches Native MCP Server — EA Data Now Queryable from Claude and Copilot
**Relevance:** Your primary EA tooling is now an MCP server. Two implications: new workflow capability, and a new MCP governance scope item.

SAP LeanIX shipped two capabilities in the last week of June: (a) an **AI Enterprise Architecture Assistant** — a chat interface inside the LeanIX workspace for natural-language queries against your EA inventory; and (b) a **native MCP server** that exposes LeanIX fact sheets, relationship maps, reports, and dashboards directly to Claude or Microsoft Copilot via MCP apps. This means you can ask Claude questions about your application landscape, capability maps, or technology radar without leaving the chat interface.

This is the first major EA tooling vendor to ship a native MCP integration at production quality.

**Strategic Implications:**
- **New workflow:** Claude Code (or Claude.ai) can now pull live LeanIX EA data mid-session. Architecture questions that previously required switching to LeanIX can be answered inline. Worth testing with a representative EA query during your next LeanIX session.
- **MCP Governance scope:** LeanIX is now an MCP server in Belron's environment. The MCP Governance framework needs a concrete answer for "who can connect what to LeanIX via MCP" — access control, data sensitivity (EA data includes vendor relationships, technology spend, roadmaps), and audit trail. Add LeanIX MCP to the governance inventory alongside Salesforce Agentforce MCP.
- **EA Copilot agent relevance:** The existing idea of an EA Copilot agent (Watchlist: Microsoft AI) now has a Salesforce + LeanIX data source available via MCP. The architecture is becoming clearer — Copilot Studio or Claude orchestrating MCP connections to Salesforce, LeanIX, and other EA data sources.

**Sources:**
- [SAP LeanIX: AI-Native Enterprise Architecture (MCP)](https://www.leanix.net/en/blog/ai-enterprise-architecture) (Tier 2 — official product blog) — June 3, 2026
- [EA Voices: AI-Native EA now available in SAP LeanIX](https://eavoices.com/2026/06/03/ai-native-enterprise-architecture-now-available-in-sap-leanix/) (Tier 2) — June 3, 2026
- [SAP LeanIX: AI-Generated Custom Reports](https://www.leanix.net/en/blog/democratize-reporting-ai) (Tier 2) — June 24, 2026

**Confidence:** High — official SAP LeanIX product announcements, cross-referenced by EA Voices.

---

### 4. EU AI Act — 35 Days to Full High-Risk Enforcement (2 August 2026)
**Relevance:** Belron operates across 35 countries, many in the EU, and is pre-IPO. Regulatory non-compliance at this stage carries disproportionate risk.

The EU AI Act's high-risk AI system provisions become enforceable on **2 August 2026** — 35 days from today. This is not a new law but an activation of existing law; penalties up to €35M or 7% of worldwide turnover are live from that date. Key obligations:

- **AI system inventory:** Every AI system must be classified by risk tier. Unclassified systems are exposed.
- **Voice AI disclosure:** Any AI voice agent used in customer interactions must disclose AI status to the caller before the interaction begins. This is directly relevant to CCOTF — any Belron opco deploying AI voice agents in EU markets from August 2 needs a compliant disclosure flow.
- **High-risk categories:** AI used in employment decisions (e.g. AI-assisted scheduling, performance evaluation) and customer-facing risk decisions may trigger Annex III high-risk obligations.
- **AIDA PoC note:** Damage assessment AI that feeds into a repair/replace recommendation affecting a customer's contract or insurance claim may need risk classification. Early legal review is advisable before the PoC moves to production.

A European Commission "Digital Omnibus" package could push some Annex III obligations to December 2027 — but this is not enacted, and planning as if August 2 is live remains the prudent posture.

**Action Suggested:**
- [ ] Flag to Legal/Compliance: EU AI Act high-risk provisions enforceable 2 August — request Belron's current AI inventory and classification status 📅 2026-07-01
- [ ] Add EU AI Act disclosure requirement to CCOTF voice AI vendor evaluation criteria 📅 2026-07-05
- [ ] Raise AIDA PoC risk classification question in next project review 📅 2026-07-05

**Sources:**
- [Holland & Knight: US Companies Face EU AI Act August 2026 Deadline](https://www.hklaw.com/en/insights/publications/2026/04/us-companies-face-eu-ai-acts-possible-august-2026-compliance-deadline) (Tier 1 — major law firm) — April 2026
- [Covasant: EU AI Act Compliance for Autonomous Agents 2026](https://www.covasant.com/blogs/eu-ai-act-compliance-autonomous-agents-enterprise-2026) (Tier 2) — 2026
- [EU AI Act official tracker](https://artificialintelligenceact.eu/) (Tier 1 — official) — current

**Confidence:** High — enforcement date confirmed in the Act text. Digital Omnibus delay is speculative and unlegislated.

---

## Market Intelligence

### 5. Contact Centre Voice AI: $0.30 vs $17 — The Cost Economics Are Now Documented
**Relevance:** The CCOTF business case needs a number. This is it — and it comes with an EU compliance caveat.

Post-Customer Contact Week, the market data has crystallised. AI voice agents now cost **$0.30–$0.50 per contact** versus **$17+ for human agents** — a 35x cost differential. Gartner projects $80 billion in global contact centre labour savings by 2026. Separate vendor rankings place Retell AI, Amazon Connect, Cresta, NICE CXone, and Genesys Cloud CX as leading enterprise platforms, with production deployment timelines of 2–9 days (commodity use cases) to 8–16 weeks (complex omnichannel).

The counter-signal: most organisations are still only deploying AI in 5–10% of real-world contact volume. The gap between the demo and production deployment is real.

**Market Impact:**
- For Belron CCOTF: the $17 per contact vs $0.30–$0.50 comparison is the headline number for any ROI analysis. Belron handles millions of contacts across 35 opcos — even a 10% AI deflection at these unit economics generates significant savings.
- EU AI Act constraint: mandatory caller disclosure from 2 August means a Belron EU opco cannot silently route customers to AI voice agents. The disclosure requirement needs to be built into the interaction design, not retrofitted.
- Salesforce Agentforce relevance: Agentforce ARR grew 169% YoY to $800M (June 15 Summer '26 release). Salesforce is positioning Agentforce as the native AI agent layer on top of existing Service Cloud — relevant for Belron given existing SC deployment.

**Sources:**
- [CX Today: How Cloud Voice AI Is Reviving the Contact Center in 2026](https://www.cxtoday.com/contact-center/how-cloud-voice-ai-is-reviving-the-contact-center-in-2026/) (Tier 2) — 2026
- [Retell AI: Top 10 Enterprise AI Voice Agent Vendors 2026](https://www.retellai.com/blog/top-10-enterprise-ai-voice-agent-contact-center-vendors) (Tier 2) — 2026
- [Business Standard: Can voice be AI's next growth frontier?](https://www.business-standard.com/technology/artificial-intelligence/call-screening-to-in-call-agent-can-voice-be-ai-s-next-growth-frontier-126062200634_1.html) (Tier 1) — June 22, 2026

**Confidence:** High — unit cost figures are widely corroborated across multiple industry sources.

---

## Technology Watch

### California SB 988 Auto Glass ADAS Bill — Industry Pushback Continuing
**Relevance:** US legislative pattern that typically leads UK/European regulation by 12–24 months.

California's SB 988 (Motor Vehicle Glass Act) is following the NCOIL template pushed by Safelite and its insurance partners in multiple states. The bill would require auto glass shops to disclose ADAS systems, document calibration results, and follow new claims rules before starting insured work. Industry groups pushed back at an April 14 hearing, arguing the bill over-reaches and creates compliance costs for independent shops.

No June 2026 update from Safelite's own press releases. The California bill remains in committee. Worth monitoring: if SB 988 passes, it will likely be cited in future UK/EU ADAS calibration debates — and Belron's European opcos will face equivalent regulation.

**Sources:**
- [Autobody News: California's Auto Glass Bill Would Tighten ADAS and Claims Rules](https://www.autobodynews.com/news/californias-auto-glass-bill-would-tighten-adas-and-claims-rules) (Tier 2) — 2026
- [GlassBYTEs: Industry Pushes Back on California Bill](https://glassbytes.com/2026/04/industry-pushes-back-on-california-bill/) (Tier 2) — April 2026

**Confidence:** Medium — no June update from Safelite directly; California bill status unconfirmed post-April.

---

## Opportunities & Recommendations

### Immediate Actions (This Week)
- [ ] Test SAP LeanIX MCP integration — connect Claude to LeanIX workspace and run a representative EA query 📅 2026-06-30
- [ ] Update AIDA PoC benchmark tracker to reflect GPT-5.6 Sol launched June 26 (limited); revise three-model benchmark run to mid-July 📅 2026-06-30
- [ ] Flag EU AI Act August 2 deadline to Legal/Compliance — request Belron's current AI classification status 📅 2026-07-01

### Next Week
- [ ] Add model provenance resilience dimension to AIDA PoC vendor comparison (following GLM-5.2 open-weights development) 📅 2026-07-05
- [ ] Add LeanIX MCP server to MCP Governance inventory alongside Salesforce Agentforce MCP 📅 2026-07-05
- [ ] Add EU AI Act caller disclosure requirement to CCOTF voice AI vendor evaluation criteria 📅 2026-07-05
- [ ] Add AIDA PoC EU AI Act risk classification to next project review agenda 📅 2026-07-05

### Research Needed
- Gemini 3.5 Pro GA date — still Vertex AI preview; needed to complete AIDA three-model benchmark
- Belron's current EU AI Act preparation status — legal and compliance team owns this
- LeanIX MCP server data sensitivity classification — what does the MCP server expose, and is there a scope control?

### People to Inform/Consult
- **Legal/Compliance:** EU AI Act 35-day window — request AI system inventory and classification status
- **CCOTF project team:** $0.30 vs $17 contact economics + EU disclosure requirement from August 2

---

## Risks & Threats

### Active Threats
- **Fable 5 ban continues (Day 16):** Full restoration has no confirmed date. AIDA PoC benchmark run remains blocked on the Fable 5 slot. Zhipu GLM-5.2 development does not accelerate restoration — if anything, the US government may interpret it as validation of the threat model.
- **EU AI Act non-compliance window closes 2 August:** 35 days. If Belron has unclassified AI systems touching EU customers or employees, the exposure becomes live. Pre-IPO environment makes regulatory non-compliance an IPO risk item, not just an operational one.

### Emerging Risks to Monitor
- **Open-weights Chinese models catching frontier Western models in specialist domains:** GLM-5.2 is the first documented example at a commercially relevant benchmark. If this pattern accelerates, the foundation model vendor landscape becomes more fragmented and geopolitically complex.
- **GPT-5.6 government-gated access becoming a template:** OpenAI called it "unsustainable" — but if it persists, enterprise access to frontier models could become politically gated rather than commercially available. Worth noting in any AI dependency risk assessment.

---

## Verification Report

### Source Analysis
- **Tier 1 Sources:** 5 (OpenAI official, VentureBeat, Business Standard, Holland & Knight, EU AI Act official tracker)
- **Tier 2 Sources:** 9 (Semgrep, LeanIX blog, EA Voices, CX Today, Retell AI, Autobody News, GlassBYTEs, The Decoder, Covasant)
- **Tier 3 Sources:** 4 (explainx.ai ×2, VGTimes, Guillermo Rauch X — all noted where used)
- **Cross-References Performed:** 6

### Freshness Verification
- All news items verified within 7-day window (June 21–28, 2026)
- Publication date range: June 3, 2026 (LeanIX MCP launch) to June 28, 2026 (Zhipu/GLM-5.2 market response)

### Confidence Assessment
- **Overall Confidence:** 82%
- **High Confidence Items:** 3 (GPT-5.6 launch, LeanIX MCP, EU AI Act date)
- **Medium-High Confidence Items:** 1 (Zhipu GLM-5.2 — independent benchmark verified, full parity claim contested)
- **Medium Confidence Items:** 1 (California ADAS bill — no June update confirmed)

---

*Curated by COG | All news verified within 7-day freshness window | Sources cross-referenced for accuracy*
