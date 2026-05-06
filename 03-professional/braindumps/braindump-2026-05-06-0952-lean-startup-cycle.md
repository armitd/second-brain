---
type: "braindump"
domain: "professional"
date: "2026-05-06"
created: "2026-05-06 09:52"
themes: ["lean-startup", "innovation", "product-development", "enterprise-ai", "validated-learning"]
tags: ["#braindump", "#lean-startup", "#innovation", "#product-management", "#enterprise-architecture"]
status: "captured"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: Lean Startup Cycle — Research Notes

## Raw Thoughts
lean startup cycle - do some research

---

## Research Summary

### The Core Framework: Build–Measure–Learn

Introduced by Eric Ries in *The Lean Startup* (2011), the **Build–Measure–Learn (B–M–L) loop** is the foundational cycle of lean startup methodology. It is a disciplined feedback system for turning assumptions into validated knowledge under conditions of extreme uncertainty.

**The three stages:**

1. **Build** — Start with a hypothesis. Build the *minimum* thing needed to test it: the **Minimum Viable Product (MVP)**. The MVP is not a rough product — it is the *fastest path to evidence*. It might be a landing page, a manual process with a professional veneer, a prototype, or a single working feature.

2. **Measure** — Define actionable metrics *before* building. Measure customer behaviour against the hypothesis. Vanity metrics (page views, downloads) are traps. The right metric shows cause and effect — it changes *because* of what you did.

3. **Learn** — Evaluate the data. The fundamental question: does the data support the hypothesis or falsify it? This drives the **Pivot or Persevere** decision:
   - **Persevere:** Data supports the hypothesis. Continue and build on it.
   - **Pivot:** Data does not support the hypothesis. Structurally change direction — new customer segment, new product feature, new channel, new business model — and begin the loop again.
   - **Kill:** The experiment reveals the whole idea is not viable.

The loop repeats indefinitely. The goal is not to execute a plan — it is to learn faster than competitors whether you are building the right thing.

---

### Innovation Accounting

A critical concept that is often overlooked: **innovation accounting** is the discipline of evaluating progress when traditional business metrics (revenue, profit, market share) are effectively zero.

Eric Ries defined it as: *"evaluating progress when all metrics typically used in established companies are effectively zero."*

In practice, innovation accounting defines:
- What does "learning" look like as a measurable outcome?
- What are the leading indicators that tell you *before* revenue arrives whether the product is working?
- How do you compare the "productivity" of different experiments?

**2025 benchmarks in enterprise lean startup:**
- Experiment velocity: minimum 2–3 experiments per sprint cycle during early phases
- MVP-to-launch target: within 90 days of initial concept
- Startups with functional MVP + early user data are 3× more likely to secure pre-seed funding

Innovation accounting is the answer to the question: *"How do we justify AI investment to the business when it isn't generating revenue yet?"* — directly applicable to Belron's AI PoC portfolio.

---

### How the MVP Concept Has Evolved

The MVP concept (coined by Frank Robinson in 2001, popularised by Ries and Steve Blank) has drifted significantly from its original intent in common practice.

**Original intent:** The MVP is a *learning* instrument, not a *product*. It is the minimum experiment that generates the maximum validated learning. It might be embarrassingly unfinished by product standards.

**Common misapplication:** Teams treat MVP as shorthand for "first version of the product" — a scope-reduced but still fully-built product. This misses the point: the goal is to be wrong *cheaply and quickly*, not to build a minimal version of a full product.

**Four types of MVP (modern practice):**
1. **Concierge MVP** — manually deliver the product experience to early customers to validate value before automating anything
2. **Wizard of Oz MVP** — product appears automated/AI-driven to the customer; humans do the work behind the scenes
3. **Landing page MVP** — test demand and willingness-to-pay before building anything
4. **Feature-limited prototype** — a working subset of the intended product; closest to the "first version" interpretation

For Belron's AI projects, the **Wizard of Oz** and **Concierge** approaches are most relevant — they allow validation of AI-driven outcomes before committing to full model development.

---

## Content Analysis

### Main Themes

1. **Validated learning as the unit of progress** — Not features shipped, not stories completed. The fundamental currency of lean startup is knowledge gained through structured experiments. This reframes how you justify work to stakeholders.

2. **The pivot/persevere decision as a governance mechanism** — Regular, data-driven reviews of whether a hypothesis holds. In an enterprise context this maps well onto PoC stage gates and investment review meetings.

3. **Speed as a strategic advantage** — The faster you can complete a B–M–L loop, the faster you accumulate knowledge relative to competitors. AI tools (automated measurement, no-code build, LLM-assisted analysis) are dramatically compressing loop times in 2025–2026.

4. **Incremental vs. breakthrough innovation tension** — The most substantive criticism: lean startup optimises for finding product-market fit in an *existing* problem space. For truly novel products (Tesla, iPod, foundational AI platforms), customers cannot imagine the future well enough for their feedback to be the primary signal. Lean startup is best for *demand validation*, not *vision creation*.

5. **Enterprise applicability is real but requires adaptation** — Fortune 500s, government agencies, and established companies are adopting lean startup principles. But the incentive structure in large organisations is the inverse of a startup (limited upside, high downside of failure) — this makes genuine experimentation culturally difficult without executive cover and safe-to-fail framing.

### Questions Raised

- For Belron's AI PoC portfolio: are we doing *innovation accounting*, or just reporting milestones? Do we have leading indicator metrics defined before we build?
- Is the AI Damage Assessment PoC running as a Wizard of Oz MVP phase first, or are we building the full model from the start?
- How does lean startup interact with EA governance? Stage-gate processes are antithetical to fast B–M–L loops — but *some* governance is necessary. What's the right cadence?
- Contact Centre of the Future has long feedback cycles (cultural change, agent training, system integration) — how do you run lean startup experiments in a slow-feedback environment?

### Decisions Contemplated

- Whether to formally adopt lean startup language and tooling for Belron's AI PoC reporting to stakeholders
- Whether to recommend innovation accounting metrics to the AI Damage Assessment and Contact Centre project teams
- Whether a "Wizard of Oz" phase should be a standard early step in Belron AI projects before model investment

---

## Strategic Intelligence

### Key Insights

1. **Innovation accounting solves the AI PoC justification problem.** The standard complaint from business stakeholders about AI PoCs is "when does it generate value?" Innovation accounting gives a structured answer: here are our learning milestones, here are our leading indicators, here is the evidence threshold for the next investment decision. This is the EA team's contribution to AI governance — not just architecture, but learning frameworks.

2. **Wizard of Oz MVPs are underused in enterprise AI.** Before committing to model training, data pipelines, and MLOps infrastructure, run a human-in-the-loop pilot: a person does what the AI will eventually do, to test whether the *decision* is valuable to the customer. If the decision isn't valuable when a human makes it, the AI version won't be either. The AI Damage Assessment PoC should have (or already have had) a concierge/Wizard of Oz phase.

3. **Lean startup loop speed is about to collapse via AI.** No-code builders, LLM-generated prototypes, and automated A/B testing mean that the "build" phase of B–M–L can now happen in hours, not weeks. This changes the competitive dynamic: companies that have embedded fast-loop culture will accelerate; those still running 6-month PoC projects will fall further behind. Belron needs a *structural* mechanism for fast experiments — not just agile sprints.

4. **The criticism is valid and important for Belron:** Lean startup creates *incremental* innovations by design. For breakthrough bets (e.g., fully autonomous vehicle glass assessment via computer vision and ADAS calibration) the vision must come first and experiments must validate the *path* to the vision, not the vision itself. Don't let lean startup's short-term feedback loops kill long-horizon bets.

5. **Pivot/persevere as an EA governance artefact.** The stage gate between PoC and pilot is a natural pivot/persevere decision point. If EA owns the framework for defining what "validated learning" looks like before the PoC begins, EA is structuring the governance moment — not just reviewing architecture. This is EA as enabler of innovation, not just guardian of standards.

### Pattern Recognition

- **Connection to MCP Governance project:** The centralised MCP gateway approach benefits from a lean startup framing — start with the minimum governance surface (ServiceNow + ContextForge), measure agent behaviour, learn what policies are actually needed before writing 50-page policy documents. Don't build governance for hypothetical risks.
- **Connection to AI Damage Assessment PoC:** This is structurally a lean startup experiment. The question is whether it's being run with a clear hypothesis, leading indicators, and a pre-defined pivot threshold — or as a traditional project with a delivery date and a feature list.
- **Connection to TOGAF BA work:** Value streams and capability models can define the *hypothesis* for lean startup experiments — "we believe automating capability X will reduce cost by Y or improve outcome Z." The BA artefacts become the experiment design brief.

### Strategic Implications

- Belron's AI investment cycle should adopt innovation accounting language for all AI PoCs: define learning milestones, leading indicators, and pivot thresholds before the first sprint begins
- The EA team should position itself as the owner of the *experiment design framework*, not just the architecture framework
- Fast-loop capability (Wizard of Oz, concierge pilots, rapid prototyping) should be a formal Belron capability — consider whether a small internal venture/innovation function is needed to run these loops independently of the delivery pipeline

---

## Action Items

### Immediate (24-48 hours)
- [ ] Read the Reforge critique of lean startup methodology (reforge.com/blog) — strongest current-day critique 📅 2026-05-07
- [ ] Check AI Damage Assessment PoC: is there a defined hypothesis + pivot/persevere threshold? If not, suggest adding one 📅 2026-05-07

### Short-term (1-2 weeks)
- [ ] Prepare a 1-page "Innovation Accounting Lite" template for Belron AI PoCs — hypothesis, leading indicators, experiment design, pivot threshold 📅 2026-05-13
- [ ] Discuss with the 3 BAs: can BA capability maps serve as the hypothesis-definition layer for lean startup experiments? 📅 2026-05-13

### Strategic Considerations
- Consider whether to recommend a formal innovation accounting review cadence for all AI projects (monthly or per-sprint) as part of the MCP Governance and AI governance frameworks
- Explore whether Belron's internal innovation processes already use lean startup language — or if this would be introducing a new framework that needs buy-in

---

## Connections
- **Related Braindumps:** [[braindump-2026-05-05-1549-togaf-ba-application]] — BA artefacts as hypothesis design layer
- **Relevant Projects:** [[04-projects/ai-damage-assessment-poc/PROJECT-OVERVIEW]], [[04-projects/mcp-governance/PROJECT-OVERVIEW]]
- **Knowledge Base:** [[05-knowledge/research/2026-05-06-mcp-strategy-belron]] — MCP governance approach benefits from lean experiment design

---

## Criticism Summary (What Lean Startup Gets Wrong)

Worth holding in tension with the positives:

| Criticism | Source | Validity for Belron |
|---|---|---|
| Produces incremental, not breakthrough, innovations | Felin, Gambardella, Stern, Zenger (strategy scholars) | High — AI Damage Assessment is a breakthrough bet; don't let lean loops kill the vision |
| Customer feedback limits imagination | Ben Silbermann (Pinterest), HBR | Medium — customers can validate *pain*, but not always imagine the *solution* |
| Doesn't work for hardware/capital-intensive products | Entrepreneur.com, HBR | Medium — ADAS calibration and physical glass replacement have real-world constraints that can't be cheaply prototyped |
| Large company incentives are inverted (big downside, limited upside) | RevelX, multiple sources | High — this is structurally true at Belron; innovation requires executive cover to feel safe to fail |
| Overemphasises speed, underemphasises strategy | Reforge | Medium — the risk of running too many fast experiments without a coherent strategic narrative |

---

## Domain Classification
- **Primary Domain:** Professional (95%)
- **Reasoning:** Strategy and methodology research directly relevant to EA role and active AI projects at Belron
- **Cross-Domain Elements:** The Wizard of Oz MVP concept has personal application (test ideas cheaply before committing)
- **Privacy Level:** Internal

## Processing Notes
### Emotional Context
- **Energy Level:** Medium — exploratory research session, not urgent
- **Emotional Tone:** Curious — seeking to understand a methodology and identify where it applies
- **Implications:** This is background-building work; the immediate value is the innovation accounting template and the AI PoC hypothesis framing

### Confidence Assessment
- **Overall Analysis:** 90% — well-sourced, multiple independent research threads
- **Domain Classification:** 95% — clearly professional
- **Strategic Insights:** 85% — the Wizard of Oz and innovation accounting points are strong; the "EA as experiment design owner" framing is speculative but grounded

---

## Key Sources
- [Eric Ries — Lean Startup Methodology](https://theleanstartup.com/principles)
- [Lean Startup — Wikipedia](https://en.wikipedia.org/wiki/Lean_startup)
- [The Limits of the Lean Startup Method — HBR](https://hbr.org/2016/03/the-limits-of-the-lean-startup-method)
- [What the Lean Startup Method Gets Right and Wrong — HBR](https://hbr.org/2019/10/what-the-lean-startup-method-gets-right-and-wrong)
- [Challenges With The Lean Startup Methodology — Reforge](https://www.reforge.com/blog/lean-startup-methodology-problems)
- [Lean Startup Methodology and Techniques: a re-interpretation for 2025](https://www.june.so/blog/lean-startup-method-2024)
- [Innovation Accounting for Lean Startup: 15 KPIs for 2025](https://www.growthjockey.com/blogs/innovation-accounting-lean-startup)
- [What Is an MVP? Eric Ries Explains](https://leanstartup.co/resources/articles/what-is-an-mvp/)
- [Avoiding 4 Misapplications of The Lean Startup](https://leanstartup.co/resources/articles/4-misapplications-of-the-lean-startup-and-how-you-can-avoid-them/)
- [Why lean startup doesn't always work in corporates — RevelX](https://www.revelx.co/blog/why-lean-startup-doesnt-always-work-in-corporates/)

---

*Processed by COG Brain Dump Analyst | Research-backed braindump*
