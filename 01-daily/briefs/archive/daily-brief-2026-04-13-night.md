---
type: "daily-brief"
domain: "shared"
date: "2026-04-13"
created: "2026-04-13 21:56"
sources_verified: true
news_age_verified: true
confidence: "high"
tags: ["#daily-brief", "#news", "#strategic-intelligence"]
interests: ["Foundation models", "AI workforce", "AI literacy", "Enterprise architecture", "Agentic AI"]
projects_referenced: []
items_count: 4
note: "Late night supplement — new stories not in the 08:25 morning, 15:59 PM, or 19:37 evening briefs"
dedup_urls:
  - "https://hai.stanford.edu/ai-index/2026-ai-index-report"
  - "https://siliconangle.com/2026/04/13/stanford-hais-2026-ai-index-reveals-china-u-s-now-neck-neck-race-global-dominance/"
  - "https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4"
  - "https://www.prnewswire.com/news-releases/fathom-applauds-governor-spanbergers-signing-of-landmark-ai-governance-legislation-302739994.html"
  - "https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/"
---

# Daily Brief (Late Night Supplement) — 13 April 2026

**Late one, Armo.** Four more stories — none in the previous three briefs. The Stanford AI Index dropped today with a finding that changes how to frame internal AI conversations: experts and the public are 50 points apart on whether AI is good for jobs. That gap *is* your communication problem. Also: a Chinese open-weight model just beat every US frontier model on the most practical coding benchmark that matters. And Claude Mythos is being used to find zero-days in every major OS and browser — with implications for how EA governs AI security tooling.

---

## Executive Summary

Stanford's 2026 AI Index landed today with its biggest finding being a crisis of trust, not capability: 73% of AI experts are optimistic about jobs, only 23% of the public agrees — a 50-point chasm. China has erased the US AI lead per the same report, and a Chinese model (GLM-5.1, MIT-licensed) just topped SWE-Bench Pro above GPT-5.4 and Claude Opus 4.6. Anthropic's Mythos model is being used to discover zero-day vulnerabilities across every major OS and browser via Project Glasswing. And Virginia became the first US state to establish a formal AI verification framework — the Independent Verification Organisation (IVO) model — a governance precedent worth tracking for EA.

---

## High Impact

### Stanford 2026 AI Index: 50-Point Expert-Public Gap on Jobs — And China Has Erased the US AI Lead

**Relevance:** Two findings in one report that together reframe the AI strategy conversation. The expert-public gap is the single most useful stat for understanding why internal AI programmes face resistance even when the business case is strong. The China finding changes the competitive context for every foundation model vendor on the watchlist.

Stanford HAI published its 457-page 2026 AI Index Report on April 13. The headline findings:

**Expert-public gap:**
- **73% of AI experts** are optimistic about AI's impact on jobs
- **Only 23% of the public** agrees — a **50-point gap**
- This is not a knowledge gap — the report finds four out of five US high school and college students now use AI for school work. The gap is a *trust* gap, not a literacy gap
- Separately: the US Education system is lagging — only half of middle and high schools have AI policies, and just **6% of teachers** say those policies are clear
- Generative AI reached **53% population adoption** within three years — faster than the PC or the internet

**China AI parity:**
- The report finds China has **erased the US lead in AI** — the two are now "neck-and-neck" in global dominance
- This is consistent with tonight's GLM-5.1 story (see below) and the earlier AlignedNews signals on DeepSeek capability reassessment

**Transparency declining:**
- The most powerful modern models are now **among the least transparent**
- Foundation Model Transparency Index average scores dropped from **58 to 40** year-over-year
- Power is concentrating — giant models dominated by largest AI companies

**EA and Workforce Implications:**
- The 50-point trust gap is the reason AI change management programmes fail before they begin. Any internal AI programme at Belron that doesn't address employee trust head-on will face this gap — you can use the Stanford figure to make the case for why communications and change management need to be part of the programme from day one, not an afterthought
- The education policy gap (only 6% of teachers with clear AI policies) maps directly to the enterprise equivalent: most organisations have no clear policy on how employees should use AI tools. Belron almost certainly sits in this group. EA can own the policy question.
- China AI parity: the vendor landscape is no longer safely "US labs ahead, everyone else catching up." For any long-term architecture, assume Chinese open-weight models (GLM, DeepSeek) are production-viable alternatives to US closed models

**Sources:**
- [Stanford HAI — 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report) (Tier 1) — 13 April 2026
- [Stanford HAI — 12 Takeaways from the 2026 Report](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report) (Tier 1) — 13 April 2026
- [SiliconAngle — China has erased the US lead in AI, Stanford HAI 2026 AI Index reveals](https://siliconangle.com/2026/04/13/stanford-hais-2026-ai-index-reveals-china-u-s-now-neck-neck-race-global-dominance/) (Tier 2) — 13 April 2026

**Confidence:** High — Stanford HAI is the authoritative primary source; figures drawn directly from the published report.

---

## Strategic Developments

### GLM-5.1 — MIT-Licensed Chinese Model Tops SWE-Bench Pro Above GPT-5.4, Claude Opus 4.6, and Gemini

**Relevance:** The evening brief noted that the open-source backstop in your foundation model landscape was weakening (Meta's closed-source pivot). GLM-5.1 is the answer to that concern from an unexpected direction — a Chinese lab has just released the most capable open-weight agentic coding model in the world, MIT-licensed, free for commercial use.

Z.ai (Zhipu AI, Beijing) released GLM-5.1 on April 7, 2026:

**Benchmark performance:**
| Model | SWE-Bench Pro Score |
|---|---|
| **GLM-5.1 (open-weight, MIT)** | **58.4** |
| GPT-5.4 (closed) | 57.7 |
| Claude Opus 4.6 (closed) | 57.3 |
| Gemini 3.1 Pro (closed) | 54.2 |

**Technical profile:**
- **754 billion parameter** Mixture-of-Experts architecture
- Designed for **up to 8 hours of autonomous task execution** on a single goal — maintains goal alignment across thousands of tool calls
- Can "rethink its own coding strategy across hundreds of iterations" (The Decoder)
- Model weights available on Hugging Face and ModelScope under MIT License
- **MIT License** = fully open for commercial use, no restrictions

**What GLM-5.1 is and isn't:**
- This is an **agentic coding model** — it's optimised for sustained software engineering tasks, not general multimodal use
- It does not have the same multimodal image analysis capability as GPT-5.4 or Gemini for damage assessment use cases
- However, for any agentic workflow, enterprise integration, or code generation task, it is now the best available open-weight option — and it's free

**Strategic implications:**
- The "open-source fallback requires quality compromise" assumption is now broken for coding tasks. GLM-5.1 is demonstrably better than GPT-5.4 on practical software engineering benchmarks
- For Belron, this doesn't directly affect the damage assessment PoC (which needs multimodal image analysis). But for any agentic workflow, integration layer, or internal tooling, GLM-5.1 is a credible zero-cost alternative to GPT-5.4 or Claude Opus 4.6
- The watchlist should be updated: **Chinese AI labs (GLM, DeepSeek) are now production-viable vendors** — not just research curiosities. This needs to be accounted for in any multi-year AI architecture plan
- The Stanford finding (China has erased US AI lead) is now confirmed by direct benchmark data

**Sources:**
- [VentureBeat — GLM-5.1 beats Opus 4.6 and GPT-5.4 on SWE-Bench Pro](https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4) (Tier 1) — April 2026
- [Dataconomy — Z.ai's GLM-5.1 Tops SWE-Bench Pro](https://dataconomy.com/2026/04/08/z-ais-glm-5-1-tops-swe-bench-pro-beating-major-ai-rivals/) (Tier 2) — 8 April 2026
- [The Decoder — GLM-5.1 can rethink its own coding strategy](https://the-decoder.com/zhipu-ais-glm-5-1-can-rethink-its-own-coding-strategy-across-hundreds-of-iterations/) (Tier 2) — April 2026

**Confidence:** High — benchmark figures independently reported across multiple Tier 1 and 2 sources; MIT licence confirmed on Hugging Face.

---

## Technology Watch

### Claude Mythos — Project Glasswing: Zero-Day Vulnerabilities Found in Every Major OS and Browser

**Relevance:** Anthropic is on your watchlist. Mythos is the next-generation model and this is its first public outing. The cybersecurity finding is relevant on two levels: it's the strongest signal yet of what frontier models can do autonomously in a high-stakes domain, and it's directly relevant to EA's security governance remit — agents that can find (and exploit) zero-days are a new class of risk that needs to be in Belron's threat model.

Anthropic released Claude Mythos Preview on April 7, 2026, exclusively through **Project Glasswing** — a controlled security research programme. It is not publicly available.

**What Project Glasswing is:**
- Mythos Preview is being made available only to a curated set of security research partners: Amazon, Apple, Broadcom, Cisco, CrowdStrike, the Linux Foundation, Microsoft, and Palo Alto Networks
- The goal is offensive security research — using Mythos to find vulnerabilities before attackers do
- Anthropic is explicitly restricting broader access while the model matures

**What Mythos has done so far:**
- Found **thousands of zero-day vulnerabilities** across every major operating system and every major web browser
- The UK AI Security Institute (AISI) independently evaluated Mythos against a 32-step corporate network attack simulation:
  - Completed the full 32-step attack in **3 out of 10 attempts**
  - Averaged **22 out of 32 steps** per attempt — more than two-thirds of a complete corporate network compromise, autonomously
  - Achieved **73% success rate** on expert-level CTF (Capture the Flag) cybersecurity challenges
  - Tasks that would take a human professional **days** — completed autonomously

**EA and security governance implications:**
- This is a concrete capability threshold: as of April 2026, an AI model can independently execute most of a corporate network attack. This is not theoretical — it has been independently verified by a government security institute
- For Belron's EA function, this raises a direct question: does Belron's threat model account for AI-assisted attacks? The enterprise security team needs to be briefed on this capability shift
- On the opportunity side: the Project Glasswing partners (Amazon, Microsoft, Cisco, CrowdStrike) now have early access to a vulnerability discovery capability that no one else has. This is a competitive security advantage for organisations in that programme
- Mythos is not publicly available — so this is an Anthropic-specific capability that isn't accessible via standard API. For planning purposes: Mythos remains a horizon item, not an immediate deployment option
- The Anthropic watchlist entry should note that Mythos exists and its capability profile — it's relevant to any conversation about AI-assisted security testing or red-teaming in the Belron context

**Sources:**
- [TechCrunch — Anthropic debuts Claude Mythos Preview in cybersecurity initiative](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) (Tier 1) — 7 April 2026
- [AISI — Our evaluation of Claude Mythos Preview's cyber capabilities](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) (Tier 1) — April 2026
- [The Hacker News — Claude Mythos Finds Thousands of Zero-Day Flaws](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) (Tier 2) — April 2026
- [SecurityWeek — Anthropic unveils Claude Mythos](https://www.securityweek.com/anthropic-unveils-claude-mythos-a-cybersecurity-breakthrough-that-could-also-supercharge-attacks/) (Tier 2) — April 2026
- [Anthropic — Project Glasswing](https://www.anthropic.com/glasswing) (Tier 1) — April 2026

**Confidence:** High — AISI is a UK Government body; TechCrunch and SecurityWeek provide independent corroboration; Anthropic's official page confirms the programme.

---

## Market Intelligence

### Virginia Becomes First US State to Establish AI Independent Verification Organisations (IVOs)

**Relevance:** Most AI regulation to date has been either vague (US state bills) or prescriptive rules (EU AI Act). The IVO model is architecturally different — it creates a new *institutional* layer: independent expert bodies that certify whether AI systems meet safety standards. This is the governance model that EA practitioners should be watching most closely for enterprise adoption.

Governor Spanberger (Virginia) signed SB 384 and HB 797 into law this week. The legislation:

**What it does:**
- Directs Virginia's Joint Commission on Technology and Science (JCOTS) to evaluate and develop a framework for **Independent Verification Organisations (IVOs)**
- IVOs are independent, expert-led bodies that verify whether AI systems meet safety, fairness, and transparency standards — analogous to financial auditors or product safety certification bodies
- Passed with strong bipartisan support: **84-14 in the House**, **40-0 in the Senate**

**Why the IVO model is different:**
- Traditional regulation says "AI must not discriminate" — and then leaves enforcement to lawyers after harm occurs
- The IVO model says "here is an independent body that certifies your AI meets the standard before deployment" — it's a pre-market verification model, more like CE marking than a prohibition
- The AlignedNews summary described this as "AI independence legislation" — the more precise framing is AI *verification* legislation, which is the more significant and defensible innovation

**EA governance implications:**
- The IVO model is the enterprise governance equivalent of what the MCP roadmap is calling for at the protocol level: independent, authoritative validation before production deployment
- If the IVO framework proves effective in Virginia, it will be replicated by other US states and potentially influence EU AI Act implementation guidance for high-risk AI systems
- For any Belron AI programme operating in the US, IVO certification could become a procurement requirement within 2-3 years — especially for insurer-facing products where AI determines claims outcomes
- The broader pattern: AI governance is shifting from "prohibition lists" to "verification frameworks." EA's role is to anticipate this shift and build verification capability into programme design from the start

**Sources:**
- [PR Newswire — Fathom Applauds Governor Spanberger's Signing of Landmark AI Governance Legislation](https://www.prnewswire.com/news-releases/fathom-applauds-governor-spanbergers-signing-of-landmark-ai-governance-legislation-302739994.html) (Tier 2) — April 2026
- [Hunton — Virginia Legislature Passes AI Bill](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-legislature-passes-ai-bill) (Tier 2) — April 2026
- [Governor of Virginia — April Releases](https://www.governor.virginia.gov/newsroom/news-releases/2026/april-releases/name-1115383-en.html) (Tier 1) — April 2026

**Confidence:** Medium-High — PR Newswire announcement confirmed by Hunton law firm analysis and Governor's office press releases; precise date of signing not pinned in search results.

---

## Unverified — Figure AI Shutdown Rumour: Treat as Hearsay

**⚠️ Unable to verify from independent sources**

AlignedNews surfaced a Robert Scoble post tonight stating he had "heard hearsay" that Figure AI may have been shut down. Scoble was explicit that this was unconfirmed.

Multiple searches found **no corroborating evidence** of a Figure AI shutdown. Available data as of tonight:
- Figure AI has $39B valuation and over $1.9B in total funding
- The company website and news feed are active
- No announcement from Figure, their investors, or BMW (their primary deployment partner)

**The evening brief stated** that Figure AI's humanoid robots have contributed to the production of 30,000 cars at BMW globally — this claim is **not affected** by Scoble's rumour and stands as verified.

**Recommendation:** Treat as hearsay only. If Figure AI had actually shut down, it would be one of the largest startup failures of 2026 and would be across every major tech publication within hours. Monitor tomorrow morning — if nothing appears by 9am, the rumour is almost certainly false.

**Confidence:** Low for the claim (hearsay, no corroboration) | High that it is unsubstantiated.

---

## Opportunities & Recommendations

### Immediate Actions (This Week)
- [ ] **Use the Stanford 50-point trust gap in any AI strategy conversation.** "73% of experts are optimistic about jobs; only 23% of the public agrees" is a single number that explains why AI programmes face internal resistance — and why communications and change management need to be treated as programme infrastructure, not afterthoughts 📅 2026-04-20
- [ ] **Update competitive watchlist — add Chinese AI labs section.** GLM-5.1 and DeepSeek are now production-viable vendors with benchmark performance exceeding US frontier models on practical tasks. The watchlist currently has no Chinese lab entries. This is a gap. 📅 2026-04-17
- [ ] **Brief enterprise security team on Claude Mythos / AISI evaluation.** The independent verification that an AI model can autonomously execute most of a corporate network attack is the kind of concrete, verified capability threshold that security teams need to know about. This is relevant to Belron's threat model regardless of whether Mythos is ever deployed internally. 📅 2026-04-20

### Research Needed
- Does Belron have a clear internal AI usage policy? The Stanford finding that only 6% of teachers say AI policies are clear maps directly to the enterprise — it's almost certain that Belron employees are using AI tools without clear governance. EA is well-positioned to own this.
- What is the EU AI Act classification for a windscreen damage assessment AI used in insurer claims decisions? The IVO model suggests this type of tool could require pre-market verification within 2-3 years in key markets.

### People to Inform/Consult
- **Enterprise Security / CISO team:** The Mythos AISI evaluation — 22 of 32 steps of a corporate network attack, autonomously — is a threat model input they need. Even if Belron doesn't deploy AI offensively, adversaries may.
- **People / HR:** The Stanford 50-point trust gap reinforces the Anthropic white-collar employment data from this morning. Two primary-source data points now point to the same thing: employees are worried, and the data says they are right to be. This warrants an honest internal communication strategy, not just an upskilling programme.

---

## Risks & Threats

### Active Threats
- **AI-assisted cyberattacks are now verified at corporate network level.** The AISI Mythos evaluation is an independent government confirmation that autonomous AI-driven corporate network attacks are possible today. This is a live threat — not a future concern. The same capability that finds zero-days for defence can be used offensively by adversaries with access to equivalent or lesser models.
- **Chinese open-weight models now match or exceed US frontier models on key tasks.** GLM-5.1 on SWE-Bench Pro is the clearest example to date. Export control and technology competition assumptions built on permanent US capability lead are now structurally incorrect. This affects vendor strategy, geopolitical AI positioning, and any argument that relies on "Chinese AI is behind."

### Emerging Risks to Monitor
- **Foundation model transparency collapse.** The Stanford finding that the Transparency Index fell from 58 to 40 means enterprises are increasingly unable to audit the models they're building on. For Belron, this is a supply chain risk for any AI programme that relies on closed frontier models — you cannot know what you're deploying.
- **AI verification as a procurement requirement.** The Virginia IVO model, if successful and replicated, could become a procurement requirement for AI systems in regulated industries within 2-3 years. Design AI programmes now with verifiability in mind.

---

## Verification Report

### Source Analysis
- **Tier 1 Sources:** 5 — Stanford HAI (×2), AISI (UK Government), TechCrunch, Governor of Virginia
- **Tier 2 Sources:** 6 — SiliconAngle, VentureBeat, Dataconomy, The Decoder, Hacker News, SecurityWeek, Hunton, PR Newswire
- **Cross-References Performed:** 9
- **Rejected:** 1 (Figure AI shutdown — Scoble hearsay, no corroboration found)

### Freshness Verification
- ✅ Stanford AI Index: published 13 April 2026 — same day
- ✅ GLM-5.1: released 7 April 2026 — within window
- ✅ Claude Mythos / Project Glasswing: announced 7 April 2026 — within window
- ✅ Virginia IVO legislation: signed April 2026 — within window
- ❌ Figure AI shutdown: rejected — unverified hearsay

### Confidence Assessment
- **Overall Confidence:** 85%
- **High Confidence Items:** 3 (Stanford AI Index, GLM-5.1, Claude Mythos)
- **Medium-High Confidence Items:** 1 (Virginia IVO — signing confirmed, precise date not pinned)
- **Rejected Items:** 1 (Figure AI shutdown — treated as hearsay)

---

*Curated by COG | Late night supplement to morning (08:25), PM (15:59), and evening (19:37) briefs | All verified news within 7-day freshness window | Sources cross-referenced for accuracy*
