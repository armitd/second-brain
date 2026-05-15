---
type: "braindump"
domain: "professional"
date: "2026-05-16"
created: "2026-05-16 00:37"
themes: ["glass-part-identification", "vin-lookup", "auto-glass-operations", "adas-calibration"]
tags: ["#braindump", "#research", "#auto-glass", "#belron", "#adas"]
status: "captured"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: AutoBolt — Glass Part Identification by VIN

## Raw Thoughts
I need to find out about the company and product AutoBolt — which is related to identifying the right glass for a vehicle. It may possibly be only for the US market but I need to find out.

## Research Findings

**What AutoBolt is:**
AutoBolt is a glass part identification service — essentially a search engine for auto glass. You enter a VIN (or licence plate) and it returns the correct glass part numbers, vehicle features, and calibration requirements for that specific vehicle.

**How it works:**
- Input: VIN or licence plate
- Output: NAGs (National Auto Glass Specifications) and OEM part numbers, plus interchangeable options
- Also returns windshield features: solar glass, acoustic glass, lane departure warning, heads-up display, rain-sensing, etc.
- Flags ADAS calibration requirements for the specific vehicle

**Headquarters:** Toronto, Canada (not a pure US company)

**Market currently served:** Primarily US auto glass shops

**Pricing:** ~$86/month for 200 lookups (SaaS subscription model). Extra charge per lookup beyond the allowance.

**Accuracy:** Very high. Users report ~99.8% accuracy ("wrong twice out of 1,000 lookups"). Particularly strong on Mazda and Land Rover.

**Vehicle brand coverage:** Ford, GM, Stellantis, Toyota/Lexus, Hyundai/Kia, Nissan/Infiniti, Mazda, Subaru, BMW, Mercedes-Benz, VW/Audi, Volvo — essentially all major global brands.

**Key partnerships:**
- **eDirectGlass** — glass parts ordering platform integrated AutoBolt lookup directly
- **BidClips** — quoting software added AutoBolt VIN lookup for glass shops

**ADAS report (2023):**
AutoBolt published a landmark industry report showing:
- 89% of MY2023+ vehicles require ADAS calibration after windshield replacement
- Up from 25% of MY2016 vehicles — a 64% increase
- The calibration market is now a $1B industry

**Is it US-only?**
Not definitively — HQ is Toronto, vehicle brand coverage is global, and the licence plate lookup feature (not just VIN) suggests broader ambition. But current confirmed customer base is US auto glass shops. UK/Europe availability is unconfirmed.

## Content Analysis

### Main Themes
1. **Part identification at VIN level** — AutoBolt solves a real and costly operational problem: getting the wrong glass to a job. It does this by reading OEM as-built data rather than relying on catalogues.
2. **ADAS complexity driving lookup value** — The more ADAS-equipped vehicles are, the higher the cost of getting the part wrong. AutoBolt's value increases with vehicle complexity.
3. **SaaS integration play** — AutoBolt isn't a standalone tool; it's embedding itself inside ordering platforms (eDirectGlass) and quoting tools (BidClips). API-first business model.

### Questions Raised
- Does AutoBolt cover UK/European vehicle registrations (DVLA/local plate data vs. US VIN)?
- Does any Belron opco (US or otherwise) already use AutoBolt or a direct equivalent?
- What data source does AutoBolt use for OEM as-built data — and is that data available for European vehicles?
- Is AutoBolt's ADAS calibration data (89% of MY2023+) consistent with what Belron sees in its own jobs?
- Could AutoBolt be a vendor, integration partner, or acquisition target for Belron?

### Decisions Contemplated
- Whether this is relevant only to Belron's US opcos or applicable to UK/Europe as well
- Whether Belron currently has a glass part identification capability equivalent to AutoBolt — and if not, whether it's a gap worth closing

## Strategic Intelligence

### Key Insights
1. **The "right glass first time" problem is real and monetisable.** AutoBolt has built a SaaS business on it. The problem exists equally in the UK/Europe — Autoglass and Carglass technicians face the same part selection challenge.
2. **ADAS is creating urgent need for accurate part ID.** If 89% of recent vehicles need calibration after windshield replacement, knowing which glass a vehicle has (and what sensors are embedded) before ordering becomes critical to job economics.
3. **AutoBolt is Canadian, not American.** Toronto HQ with global brand coverage suggests this isn't locked to the US market by design — it may simply not have invested in UK/EU data yet.
4. **The licence plate lookup feature is the UK unlock.** UK shops don't use VIN in the same way US shops do — DVLA registration plate lookup is the equivalent. AutoBolt already supports plate lookup as well as VIN, which is a positive signal.

### Pattern Recognition
- **Connection to ADAS calibration work:** Directly connects to the May 10 brief's story on ADAS calibration costs ($20k+ for complex vehicles) and the May 11/12 brief's Ravin.ai / damage assessment context.
- **Connection to Competitive Watchlist:** AutoBolt sits in the same ecosystem as Safelite (US glass operator) and Audatex/Solera (claims workflow) — it's the part ID layer that feeds the ordering and claims process.

### Strategic Implications
- If Belron doesn't have an equivalent capability, there's a gap worth investigating
- If AutoBolt is looking to expand to UK/Europe, there could be a partnership angle — Belron's scale and data would be valuable to them; their part ID accuracy would be valuable to Belron
- The ADAS calibration data AutoBolt is publishing is competitor intelligence — Safelite is using this data to lobby for calibration billing rights (Illinois HB 4373)

## Action Items

### Immediate (24-48 hours)
- [ ] Ask someone on the Autoglass operations/technical side: do we have a VIN-level glass part identification tool? If so, what is it? 📅 2026-05-17
- [ ] Check whether AutoBolt has a UK/Europe offering or is in discussions to expand 📅 2026-05-17

### Short-term (1-2 weeks)
- [ ] Review AutoBolt's knowledge centre / coverage page to confirm UK vehicle support 📅 2026-05-23
- [ ] Check whether any Belron US opcos already have an AutoBolt subscription 📅 2026-05-23
- [ ] Cross-reference AutoBolt's ADAS calibration data against Belron's own job data — do the 89% figures hold in UK/EU markets? 📅 2026-05-23

### Strategic Considerations
- AutoBolt's integration partnerships (eDirectGlass, BidClips) suggest they grow through embedding in existing workflow tools — Belron would need to understand how this maps to its own ordering and booking systems
- If AutoBolt is genuinely accurate and API-based, it could be a fast integration win for UK/EU opcos — no custom model training required

## Connections
- **Related Braindumps:** [[braindump-2026-04-09-1136-market-scan-machine-vision-frontend]]
- **Relevant Projects:** [[04-projects/ai-damage-assessment-poc/PROJECT-OVERVIEW]]
- **Competitive Watchlist:** [[03-professional/COMPETITIVE-WATCHLIST]]
- **Relevant Brief:** [[daily-brief-2026-05-10]] (ADAS calibration costs), [[daily-brief-2026-05-11]] (damage assessment PoC context)

## Domain Classification
- **Primary Domain:** Professional (95%)
- **Reasoning:** Direct relevance to Belron's core business — auto glass operations and the ADAS calibration challenge. Not specific to one project but touches AI Damage Assessment PoC and MCP Governance.
- **Privacy Level:** internal

## Processing Notes
### Emotional Context
- **Energy Level:** Medium — captured on the move, prompted by external information rather than internal reflection
- **Emotional Tone:** Curious — "I need to find out" suggests this is early-stage discovery, not a formed view

### Confidence Assessment
- **Research findings:** 85% — based on multiple sources; gap is no direct AutoBolt confirmation of UK/EU availability
- **Strategic implications:** 80% — relevance to Belron is clear; exact applicability depends on whether Belron already has an equivalent tool

---

*Processed by COG Brain Dump Analyst*
