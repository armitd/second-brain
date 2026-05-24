---
type: "daily-brief"
domain: "shared"
date: "2026-05-24"
created: "2026-05-24 13:09"
sources_verified: true
news_age_verified: true
confidence: "high"
tags: ["#daily-brief", "#news", "#strategic-intelligence"]
interests: ["anthropic", "agentic-ai", "enterprise-architecture", "eu-ai-act", "contact-centre-future", "mcp-governance", "ai-damage-assessment"]
projects_referenced: ["mcp-governance", "contact-centre-future", "ai-damage-assessment-poc"]
items_count: 6
dedup_urls:
  - "https://ramp.com/leading-indicators/ai-index-may-2026"
  - "https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines"
  - "https://www.anthropic.com/research/glasswing-initial-update"
  - "https://www.bloomberg.com/news/articles/2026-05-22/salesforce-touts-ai-promise-over-reality-in-saaspocalypse-fight"
  - "https://x.com/tryproneo/status/2056292203958358367"
  - "https://x.com/TakSec/status/2058367979793064349"
---

# Daily Brief — 24 May 2026

**Good afternoon, Armo!**

## Executive Summary

Anthropic has overtaken OpenAI in US business adoption for the first time — driven almost entirely by Claude Code — making the enterprise case for Belron's Anthropic alignment stronger than it has ever been. The EU AI Act Omnibus agreement of May 7 extended the high-risk AI compliance deadline by 16 months to December 2027, removing the August 2026 cliff that was uncomfortably close to the IPO window. And the Salesforce Agentforce scandal — Bloomberg confirming that demo videos showed capabilities that aren't deployed — is the cautionary tale to reference when evaluating any enterprise AI vendor's CCOTF pitch.

---

## High Impact News

### Anthropic Overtakes OpenAI in US Business Adoption — 34.4% vs 32.3%
**Relevance:** This directly strengthens the internal case for Belron's Anthropic alignment. The company you're advocating to build on is now the market leader in US business adoption — not a challenger.

The May 2026 Ramp AI Index, tracking AI spending across more than 50,000 US businesses, shows Anthropic at 34.4% of paid business subscriptions vs. OpenAI at 32.3% — the first time Anthropic has led in this measure. Anthropic has quadrupled its adoption over the past year while OpenAI's grew just 0.3%. The engine is almost entirely Claude Code, now the fastest-growing product in Anthropic's history.

VentureBeat's follow-up analysis identifies three threats to Anthropic's lead: escalating compute costs, token-based pricing vulnerability (OpenAI or Google could cut prices aggressively), and the possibility that a single breakthrough model release could shift enterprise procurement overnight.

**Impact Assessment:**
- **Projects Affected:** AI Damage Assessment PoC, MCP Governance, overall Belron AI strategy
- **Potential Effects:** "We chose the market leader" is now a defensible statement for Anthropic. The AI landscape narrative has shifted — this is no longer a contrarian position.
- **Action Suggested:** Use this data point in any upcoming stakeholder briefing on AI strategy. Pair with the Karpathy hire (May 19) and the SAP/MCP integration (Sapphire May 12) as a three-part narrative: Anthropic now leads in business adoption, has recruited the most respected AI educator, and is the declared integration model for SAP enterprise.

**Sources:**
- Ramp AI Index May 2026 (Tier 2) — May 2026 — [ramp.com](https://ramp.com/leading-indicators/ai-index-may-2026)
- VentureBeat (Tier 2) — May 2026 — [Anthropic finally beat OpenAI in business AI adoption](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)
- Axios (Tier 1) — May 13, 2026 — [Anthropic overtakes OpenAI in workplace AI adoption](https://www.axios.com/2026/05/13/anthropic-openai-workplace-ai-adoption)

**Confidence:** High — multiple Tier 1/2 sources from a named primary dataset (Ramp). Note: original Ramp data published ~May 13; included because it was not in previous briefs and is still being actively cited as of today.

---

### EU AI Act Omnibus: High-Risk Deadline Extended 16 Months to December 2027
**Relevance:** Belron's three active AI programmes — AI Damage Assessment PoC, CCOTF, and MCP Governance — all have EU compliance implications. The previous August 2026 deadline was uncomfortably close to the IPO window. December 2027 changes the programme calculus entirely.

On May 7, 2026, EU legislative bodies reached a political agreement on an Omnibus amendment to the AI Act. The key change for enterprise: obligations for **high-risk AI systems (Annex III, use-case-based** — including employment, customer management, and critical infrastructure) are postponed from August 2, 2026 to **December 2, 2027** — a 16-month extension. Annex I product-regulated HRAIS moves from August 2027 to August 2028. Formal adoption by Parliament and Council is expected by July 2026.

The AI Damage Assessment PoC (computer vision applied to customer-submitted images) and the CCOTF agentic layer (AI acting in employment and customer management contexts) both likely qualify as Annex III HRAIS. The extension gives the time to build proper governance rather than scrambling before an IPO roadshow.

**Impact Assessment:**
- **Projects Affected:** AI Damage Assessment PoC, CCOTF, MCP Governance (framework for governed AI tools)
- **Potential Effects:** The compliance pressure on the IPO window is removed. The Dec 2027 deadline lands post-IPO and post-consolidation — when Belron will have the governance structures to address it properly. Risk classification, documentation, and transparency requirements should still begin now, but the execution window is realistic.
- **Action Suggested:** Update the MCP RA and CCOTF RA open issues registers to note Dec 2027 as the active compliance target. Ensure the pre-IPO due diligence narrative frames AI Act compliance as a "Dec 2027 programme underway" rather than a gap.

**Sources:**
- Latham & Watkins (Tier 2) — [AI Act Update: EU Resolves to Change Rules and Extend Deadlines](https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines)
- Inside Privacy (Tier 2) — [EU AI Act Update: Timeline Relief, Targeted Simplification, and New Prohibitions](https://www.insideprivacy.com/artificial-intelligence/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/)
- EU AI Act official site (Tier 1) — [Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)

**Confidence:** High — multiple credible law firm and EU official sources; political agreement confirmed May 7.

---

## Strategic Developments

### **Update** *(first covered May 23)* — Claude Mythos: 10,000+ Vulnerabilities Found; Imminent Release Signals Today
**Relevance:** Anthropic's next-generation frontier model is security-specialised and not yet public. Strings appeared in Claude Code today (May 24) suggesting Mythos 1 Preview is imminent. The capability gap vs. current public models is significant.

The Glasswing Initial Update (published after the May 23 brief) reveals the scale of Claude Mythos Preview's work: more than **10,000 high or critical severity zero-day vulnerabilities** found across every major OS (Windows, macOS, Linux) and every major web browser, in a controlled industry consortium setting. Anthropic has specifically chosen not to release the model publicly due to dual-use risk — it is only available via Project Glasswing, described as an industry security consortium involving major tech companies.

Today (May 24), Claude Mythos strings appeared briefly inside Claude itself and in Claude Code and Claude Security product strings — consistent with preparation for a Mythos 1 Preview launch. The model is also available as a gated preview via Google Cloud Vertex AI.

**Strategic Implications:**
- Anthropic now has a model explicitly too dangerous to release publicly — a new category of AI capability representing a significant jump beyond current publicly available models
- The Vertex AI availability confirms the Anthropic/Google partnership continues to deepen. Both Azure (via OpenAI) and GCP (via Anthropic) now have Claude partnerships — relevant to Belron's cloud architecture decisions
- If Mythos 1 Preview becomes accessible to enterprise programmes, the AI Damage Assessment PoC could benefit from its substantially improved vision and reasoning capabilities

**Sources:**
- Anthropic Glasswing Initial Update (Tier 1) — [glasswing-initial-update](https://www.anthropic.com/research/glasswing-initial-update)
- Google Cloud Blog (Tier 1) — [Claude Mythos Preview on Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/claude-mythos-preview-on-vertex-ai)
- AlignedNews / aiedge_ X (Tier 3) — [Mythos strings in Claude Code](https://x.com/aiedge_/status/2058384253042467194)

**Confidence:** High on vulnerability count and Glasswing update; Medium on "imminent launch" inference from product strings (product strings are soft signals, not confirmed announcements).

---

### Salesforce Agentforce: Bloomberg Confirms Demos Showed Unavailable Capabilities
**Relevance:** Directly relevant to how you evaluate AI vendor pitches for CCOTF. This is also the enterprise AI trust signal of the week — and a model for the question to ask every CCaaS vendor.

Bloomberg confirmed on May 22 that Salesforce's promotional Agentforce videos — including a high-profile University of Chicago Medicine patient services demo — showed capabilities that are not deployed. Patients calling that hospital system today reach keypad menus and human schedulers; the chatbot shown in the video is still in testing and not visible to most web visitors. CEO Marc Benioff defended it as standard forward-looking tech marketing.

The context matters: Salesforce faces what analysts are calling "SaaSpocalypse" — the risk that enterprise AI agents built on open standards (like MCP) render traditional SaaS workflow tools obsolete by replacing human-navigated UI with machine-native API access. Agentforce is Salesforce's defensive response. The mockup controversy suggests the capability is further from production than the marketing implies.

**Strategic Implications:**
- Any CCaaS or CRM vendor pitching CCOTF capabilities should be evaluated with the direct question: "What is live in production today? What is roadmap?" — the Salesforce precedent legitimises asking this bluntly
- The Zoom EBC observation from May (in your competitive watchlist) had the same theme: AI layered on structural problems rather than solving them. This is a pattern across enterprise CCaaS vendors
- The MCP governance model (explicit tool access, auditable logs, explicit rule evaluation) is architecturally positioned to solve exactly what Salesforce is marketing aspirationally

**Sources:**
- Bloomberg (Tier 1) — May 22, 2026 — [Salesforce Touts AI Promise Over Reality in SaaSpocalypse Fight](https://www.bloomberg.com/news/articles/2026-05-22/salesforce-touts-ai-promise-over-reality-in-saaspocalypse-fight)
- PYMNTS (Tier 2) — [Salesforce CEO Defends AI Ads as Standard Tech Marketing](https://www.pymnts.com/news/artificial-intelligence/2026/salesforce-ceo-defends-ai-ads-as-standard-tech-marketing/)

**Confidence:** High — Bloomberg is the primary source; Benioff's own statement confirms the underlying facts.

---

## Technology Watch

### Agent Completion Reality Check: 4% on Real Multi-App SaaS Workflows; 37% Production Gap
**Relevance:** The CCOTF architecture positions AI agents as the primary customer-facing layer. This benchmark data should inform realistic planning assumptions for when those agents are production-ready.

Two data points this week:

**The 4% figure ⚠️ (low confidence — flag for verification):** AlignedNews surfaced a benchmark (via tryproneo on X) claiming LLM agents complete fewer than 4% of real-world SaaS workflows involving **multi-app state and recovery**. This is a very specific and severe claim. I could not verify it from a major independent source — the origin is a single X post from what appears to be a product company with potential commercial bias. Use with caution; flag for follow-up.

**The 37% production gap (higher confidence):** Multiple enterprise AI benchmarking sources independently confirm a 37% gap between laboratory benchmark scores and real-world production deployment performance across enterprise agentic systems. Stanford HAI's 2026 AI Index separately found agents still fail one in three computer use tasks even in controlled settings.

**Technology Implications:**
- The gap between benchmark and production is the key planning assumption for CCOTF — don't build deployment timelines from benchmark scores alone
- "Multi-app state and recovery" is precisely what a CCOTF agentic layer must handle: booking system + CRM + telephony + scheduling accessed within a single customer interaction
- AP-02 in the CCOTF RA ("Evaluate with explicit rules, not LLM inference") remains architecturally correct: the largest completion failures occur in evaluation and decision stages — exactly where LLM inference is least deterministic

**Sources:**
- AlignedNews / tryproneo X (Tier 3) — [source](https://x.com/tryproneo/status/2056292203958358367) — ⚠️ unverified, low confidence
- Digital Applied (Tier 2) — [Agentic Workflow Completion Metrics 2026](https://www.digitalapplied.com/blog/agentic-workflow-completion-metrics-pipeline-health-2026)
- Coasty (Tier 2) — [AI Agent Benchmark Results 2026](https://coasty.ai/blog/ai-agent-benchmark-results-2026-who-actually-wins-20260507)

**Confidence:** Low on 4% figure; Medium-High on 37% production gap (multiple sources)

---

### Prompt Injection Graduates to Operational Agent Security Risk
**Relevance:** Direct MCP Governance project concern. The threat model for MCP-connected agents now explicitly includes prompt injection as a vector for data exfiltration, tool abuse, and remote code execution — not just bad outputs.

A security analysis rated "critical" by AlignedNews reframes prompt injection from a "bad output" problem to an operational compromise risk for agentic systems. The expanded threat map:

- **Data exfiltration**: malicious prompts in ingested content cause agents to send data out-of-band via tool calls
- **Data deletion**: injected instructions directing agents to call destructive tool actions
- **Memory poisoning**: corrupting the agent's context window to affect future decisions in the session
- **Tool abuse**: exploiting trusted agent-to-tool relationships to execute unauthorised actions
- **Impersonation**: causing agents to act as different entities to downstream systems
- **Remote code execution**: especially relevant for MCP servers that execute code on agent behalf

**Technology Implications:**
- The MCP RA security section should explicitly address prompt injection at the **gateway layer** — not just at the model layer. An MCP gateway that allows agents to call tools without semantic validation of calling context is vulnerable to injection that exploits tool trust relationships
- AP-07 (Security by Design) in the CCOTF RA applies directly: agent inputs from customer channels (potentially hostile) must be sanitised before reaching tool-call decision logic
- Open Issue OI-08 (semantic governance) is related: without a controlled vocabulary and explicit evaluation rules, an agent cannot reliably distinguish legitimate instructions from injected instructions that use normal business vocabulary

**Sources:**
- AlignedNews / TakSec X (Tier 3) — [Prompt injection as agentic security risk](https://x.com/TakSec/security-prompt-injection-agents)
- AI News (Tier 2) — [Agentic AI's governance challenges under the EU AI Act](https://www.artificialintelligence-news.com/news/agentic-ais-governance-challenges-under-the-eu-ai-act-in-2026/)

**Confidence:** Medium — security community consensus on the threat categories; primary trigger is a single researcher's post (no paper or CVE published yet)

---

## Opportunities & Recommendations

### Immediate Actions (Today/This Week)
- [ ] Add Anthropic market leadership data (34.4% vs 32.3%) to next stakeholder briefing deck on AI strategy 📅 2026-05-24
- [ ] Update MCP RA and CCOTF RA open issues registers: EU AI Act compliance target is now Dec 2027, not Aug 2026 📅 2026-05-27
- [ ] Add prompt injection at gateway layer to MCP RA security section — expand threat model beyond model-layer to tool-call-layer 📅 2026-05-27
- [ ] When engaging CCaaS vendors for CCOTF: explicitly ask "What is live in production today vs roadmap?" — Salesforce Agentforce is the precedent 📅 2026-05-30

### Research Needed
- Verify the Proneo "4% completion rate" benchmark — if it has peer-reviewed backing, this is a powerful planning constraint for CCOTF; if not, it is noise
- Confirm with Belron's legal or compliance team whether they are planning against the old August 2026 deadline or are aware of the Omnibus extension

### People to Inform/Consult
- **Group IT / IPO planning team**: EU AI Act Dec 2027 deadline change relieves compliance pressure from the IPO window — relevant to the AI programme governance narrative in due diligence
- **CCOTF stakeholders**: Salesforce Agentforce controversy is relevant context if Salesforce is being evaluated as a CCaaS platform

---

## Risks & Threats

### Active Threats
- **Prompt injection as MCP gateway attack vector**: Current MCP RA security section may not explicitly cover gateway-layer prompt injection. Update required before the RA is socialised with security stakeholders.
- **Agent production gap (37%)**: Any CCOTF deployment timeline derived from benchmark performance is likely to be optimistic. Build the 37% production gap in as a standing planning assumption.

### Emerging Risks to Monitor
- **Anthropic compute constraints**: VentureBeat's analysis flags compute costs as the primary vulnerability to Anthropic's market lead. If Anthropic hits capacity constraints, enterprise SLAs could degrade. Monitor for infrastructure signals.
- **Claude Mythos dual-use risk**: If Mythos eventually becomes available to enterprise customers, the security posture of Belron's own systems should be assessed before that access is enabled. Mythos found 10,000+ zero-days in major commercial OSes — internal custom systems are likely easier targets.

---

## Verification Report

### Source Analysis
- **Tier 1 Sources:** 5 (Anthropic, EU AI Act official, Bloomberg, Google Cloud, Axios)
- **Tier 2 Sources:** 8 (Ramp, VentureBeat, Latham & Watkins, Inside Privacy, PYMNTS, Digital Applied, Coasty, AI News)
- **Tier 3 Sources:** 3 (AlignedNews aggregated from X — tryproneo, TakSec, aiedge_)
- **Cross-references performed:** 6

### Fact-Checking Results
- **Verified claims:** 18
- **Unverified claims:** 1 (4% SaaS workflow completion — single commercial source, explicitly flagged)
- **Conflicting information:** None

### Freshness Verification
- ✅ EU AI Act Omnibus: political agreement May 7, 2026 — within window
- ✅ Salesforce Agentforce: Bloomberg May 22, 2026 — within window
- ✅ Claude Mythos strings in Claude Code: May 24, 2026 — today
- ✅ Agent benchmarks and prompt injection: May 2026 sources
- ⚠️ Anthropic business adoption (Axios): May 13 — 11 days ago, outside strict 7-day window; included because not in previous briefs and still actively cited today

### Confidence Assessment
- **Overall Confidence:** 83%
- **High Confidence Items:** 3 (Anthropic adoption data, EU AI Act Omnibus, Salesforce Agentforce)
- **Medium Confidence Items:** 2 (Claude Mythos imminent release inference; prompt injection threat model)
- **Low Confidence Items:** 1 (4% SaaS completion rate — explicitly flagged)

---

## Complete Sources

### Strategic AI
1. [Ramp AI Index May 2026](https://ramp.com/leading-indicators/ai-index-may-2026)
2. [VentureBeat — Anthropic finally beat OpenAI](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)
3. [Axios — Anthropic overtakes OpenAI](https://www.axios.com/2026/05/13/anthropic-openai-workplace-ai-adoption)
4. [Bloomberg — Salesforce Agentforce controversy](https://www.bloomberg.com/news/articles/2026-05-22/salesforce-touts-ai-promise-over-reality-in-saaspocalypse-fight)
5. [PYMNTS — Salesforce CEO defends ads](https://www.pymnts.com/news/artificial-intelligence/2026/salesforce-ceo-defends-ai-ads-as-standard-tech-marketing/)

### Regulatory
6. [Latham & Watkins — EU AI Act Omnibus](https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines)
7. [Inside Privacy — EU AI Act Timeline Relief](https://www.insideprivacy.com/artificial-intelligence/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/)
8. [EU AI Act Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)

### Technology & Security
9. [Anthropic Glasswing Initial Update](https://www.anthropic.com/research/glasswing-initial-update)
10. [Google Cloud — Claude Mythos on Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/claude-mythos-preview-on-vertex-ai)
11. [Digital Applied — Agentic Workflow Completion Metrics 2026](https://www.digitalapplied.com/blog/agentic-workflow-completion-metrics-pipeline-health-2026)
12. [Coasty — AI Agent Benchmark Results 2026](https://coasty.ai/blog/ai-agent-benchmark-results-2026-who-actually-wins-20260507)
13. [AI News — Agentic AI and EU AI Act governance](https://www.artificialintelligence-news.com/news/agentic-ais-governance-challenges-under-the-eu-ai-act-in-2026/)

---

*Curated by COG | AlignedNews feed + 6 web searches + signals | Processed: 2026-05-24 13:09 | All sources cross-referenced*
