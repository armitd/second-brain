---
type: "braindump"
domain: "professional"
date: "2026-05-26"
created: "2026-05-26 10:18"
themes: ["aws-kiro", "working-backwards", "prfaq", "spec-driven-development", "vaps-wiper-market", "ai-coding-tools"]
tags: ["#braindump", "#raw-thoughts", "#aws", "#kiro", "#workshop", "#live-capture", "#working-backwards", "#vaps"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-05-30]]"
consolidated_date: "2026-05-30"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
capture_mode: "live"
event: "AWS Kiro Workshop"
event_date: "2026-05-26"
merged_from: "[[daybook-2026-05-26]]"
---

# Braindump: AWS Kiro Workshop — Live Capture

> **Live capture mode** — workshop still ongoing. Daybook notes merged in. Full analysis pass to be completed after the session ends.

## Context
- **Event:** AWS Workshop on Kiro
- **Date:** 2026-05-26
- **Format:** Hands-on workshop combining (a) Amazon's Working Backwards / PRFAQ process and (b) a Kiro tooling demo, with VAPS wiper sales used as the worked example.
- **Why I'm here:** [add reason — invited? self-booked? specific Belron angle?]
- **Expected outcomes:** [what do I want to walk away with?]

---

## Raw Notes (chronological)

### Pre-workshop expectations / questions going in
-

### Session notes

**10:29 — Amazon "Working Backwards" process introduced**
- AWS framing the workshop around their internal product development method.
- Core idea: start from the customer outcome and work back to the build — not the other way round.
- Canonical artefacts: **PR/FAQ** (press release + FAQ written *before* the product exists) → forces clarity on customer, problem, and "what would the press release say on launch day?"
- Sequence (as Amazon teaches it): **Customer → Press Release → FAQ → Visuals/UX → Build**.
- Workshop relevance: showing how Kiro embeds this — spec-first, intent-first coding rather than prompt-first.

**~10:35 — Worked example: VAPS / wiper blade replacement opportunity**

The Working Backwards exercise is being run on a Belron-relevant scenario: increasing VAPS (value-added product) sales — specifically wiper blade replacement — via the customer journey at the time of glass service.

- **Core insight:** 70% of the market is unrealised. Customers are not replacing VAPS products (wipers) as often as they should be.
- **Market sizing:**
  - Wiper market addressable share: **0.5% to 2.5%** = **€200m vs €1bn**
  - Total wiper market: **€34bn**
- **Open data questions raised during the exercise:**
  - Do customers have a login? (i.e. is there a customer identity layer to recognise returning customers?)
  - Where are VAPS product IDs stored? How is a VAPS product linked to a specific vehicle?
- **Prior pilot — France:**
  - Already tested in France.
  - They raised min/max stock levels to make sure branches had enough blades.
  - France **did not** track website traffic or contact centre traffic — so attribution / funnel data is missing.
- **Roll-out candidates (future tests):** Sweden, Switzerland, Canada.
- **MVP framing emphasised throughout.**
- **Assumptions surfaced for the PRFAQ:**
  - Wipers will always be available in-store within 2 days.
  - Customers will tolerate a 2-day lead time.
  - Branches stock a large range of wipers.
- **Operational economics:** ~5 mins to fit + 5 mins to raise invoice (= ~10 min total branch overhead per wiper sale).

**~10:55 — Kiro Demo: spec-driven development**

- **Headline framing:** "Spec-driven development" — Kiro is positioned as building *from a spec*, not from prompts.
- **Memorable phrase:** **"bounded independence"** — describes the working mode between developer and Kiro's coding agent. Developer sets the boundary; agent operates independently within it.
- **Collaboration model:** explicit collaboration between developer and coding agent (not prompt-and-pray).
- **Vibe coding vs SDLC framing:**
  > "Vibe coding ships the prototype — traditional SDLC practices ship the actual product."
  - Subtext: Kiro is being positioned as the *SDLC-grade* AI coding tool (vs Cursor/Copilot framed as "vibe coding"). This is a positioning shot at the rest of the market.
- **Working Backwards questions are built into the Kiro process** — i.e. it prompts the developer through customer / press-release / FAQ-style framing before generating code. This is the connection between part 1 and part 2 of the workshop.

**HH:MM —**

---

## Things to look up later
- What exactly is in Kiro's "spec" artefact? Format, schema, persistence model.
- Pricing model for Kiro (per-seat? token-metered? bundled with AWS account?).
- IDE integration scope (VS Code only? JetBrains? terminal?).
- Whether Kiro can call MCP servers — relevance to MCP Governance project.
- Data residency / where prompts and code context get sent for inference (AWS Bedrock region? Anthropic-hosted?).
- France VAPS pilot — who ran it? Is there a written write-up? What was the result?

## Quotes / specific phrasings worth keeping
- **"Bounded independence"** — describes developer/agent collaboration in Kiro.
- **"Vibe coding ships the prototype, traditional SDLC practices ship the actual product."** — AWS positioning of Kiro vs Cursor/Copilot/Claude Code.
- **"Spec-driven development"** — Kiro's headline category claim.

## Demo observations
- **What was shown:** Spec-driven development workflow; Working Backwards questions woven into the coding flow; developer/agent collaboration model ("bounded independence").
- **What worked well:** Framing of Kiro as SDLC-grade (rather than prototype-grade) is a sharp positioning move; the explicit Working Backwards integration is genuinely differentiated vs Claude Code / Cursor / Copilot.
- **What looked rough / unconvincing:** [add as session progresses — particularly: does it actually produce production-grade code, or is "SDLC-grade" marketing?]
- **What was conspicuously absent:** [watch for: which foundation model powers it (Anthropic? Amazon Nova? mix?); MCP support; team/multi-developer flows; security / code review story]

---

## Comparisons that came to mind
- **vs Claude Code:** Claude Code is conversational and tool-rich; Kiro is being positioned as spec-driven and SDLC-grade. Different mental model — Kiro front-loads the spec; Claude Code lets you converge iteratively.
- **vs Cursor:** Cursor is "vibe coding" territory in AWS's framing. Kiro is the deliberate counter-positioning.
- **vs GitHub Copilot:** Copilot is autocomplete-first; Kiro is spec-first.
- **Strategic question:** Does the spec-first claim hold up in practice, or does it just front-load the prompt with extra structure?

## Belron relevance

### AI Damage Assessment PoC
- The PRFAQ / Working Backwards method is **directly applicable** to how the PoC should be pitched and scoped. Writing the press release first for "Belron customer gets damage assessed in 30 seconds via app" forces clarity on customer experience before solutioning.
- Action: produce a PRFAQ for the AI Damage Assessment PoC.

### MCP Governance
- Need to check whether Kiro speaks MCP. If yes, Kiro is in scope for the MCP Governance project (it's another agent that needs governing). If no, it's a gap in their story.
- Note: Anthropic donated MCP to the Linux Foundation as the industry standard — AWS not adopting it in Kiro would be a competitive signal.

### Contact Centre of the Future
- Loosely related — same Working Backwards method could be applied to the contact centre customer journey redesign.

### General EA / developer tooling strategy
- Kiro is a **direct alternative to Claude Code** for Belron developers — needs to go on the developer tooling watchlist and be evaluated.
- **Risk to primary AI advocacy goal:** Armo's stated goal is getting Belron onto Anthropic/Claude. If AWS pushes Kiro into Belron via the AWS account team, it could dilute the Anthropic-first narrative. Need to understand what foundation model Kiro uses under the hood (it may actually run on Claude via Bedrock — in which case Kiro adoption *helps* the Anthropic narrative).
- The Working Backwards / PRFAQ method is **independently valuable** to the EA practice regardless of Kiro adoption — it can be lifted into the EA toolkit.

### VAPS / wiper business case (cross-cutting)
- This is the worked example, not the workshop's purpose — but the content itself is a Belron strategic data point worth preserving:
  - 70% of the addressable VAPS market is unrealised at Belron.
  - A €200m–€1bn revenue opportunity inside a €34bn total market.
  - France pilot exists but lacked traffic/funnel attribution — instrumentation gap.
  - Next pilots: Sweden, Switzerland, Canada.
- Worth flagging to whoever owns VAPS strategy: is this case being actively pursued, or is it a workshop hypothetical that's based on real Belron numbers?

---

## People met / worth following up
-

## Questions I asked / wanted to ask
- What foundation model powers Kiro? (Claude via Bedrock? Amazon Nova? Both?)
- Does Kiro support MCP servers / tools?
- What is the spec artefact format — is it portable, version-controllable, reviewable?
- How does Kiro handle code review / approval flows in an SDLC?
- Pricing model — and is it tied to an AWS account or standalone?

---

## Initial reactions (gut feel — refine later)
- The Working Backwards / PRFAQ framing is the **most valuable takeaway** regardless of Kiro itself — it's a method, not a tool, and it's lift-and-use into EA practice immediately.
- Kiro's positioning ("vibe coding vs SDLC") is sharp marketing but I want to see whether the spec-first claim survives contact with messy real-world tasks.
- "Bounded independence" is a useful phrase — captures the collaboration model better than "AI coding assistant".
- The fact that AWS chose a VAPS wiper case study suggests Belron may be the implicit target customer for this workshop (or they're using publicly relatable retail/service examples). Worth asking the AWS team why they picked this scenario.

## Action items captured during the session

### Immediate (24–48 hours)
- [ ] Write up a one-paragraph summary of Working Backwards / PRFAQ for the EA team 📅 2026-05-27
- [ ] Capture a Kiro vs Claude Code vs Cursor comparison note for the developer-tooling watchlist 📅 2026-05-27

### Short-term (1–2 weeks)
- [ ] Draft a PRFAQ for the AI Damage Assessment PoC using the method demonstrated today 📅 2026-06-02
- [ ] Find out whether the VAPS / wiper numbers shown (70% unrealised, €200m–€1bn) are live Belron data or workshop illustration — and if live, who owns the initiative 📅 2026-06-02
- [ ] Confirm what foundation model Kiro uses under the hood (Claude / Bedrock / Nova) 📅 2026-06-02
- [ ] Confirm whether Kiro supports MCP — feeds into MCP Governance scope 📅 2026-06-02

### Strategic considerations
- Should Belron's EA practice formally adopt PRFAQ as a method? (Lightweight, doesn't require AWS commitment.)
- If Kiro runs on Claude via Bedrock, Kiro adoption may *accelerate* Belron's Anthropic relationship rather than threaten it — need to verify before forming a position.

---

## Content Analysis *(post-workshop pass — partial, will be completed when session ends)*

### Main Themes (so far)
1. **Working Backwards / PRFAQ method** — Amazon's customer-first product development process being taught as the prerequisite to using Kiro.
2. **Spec-driven development** — Kiro's category claim. Differentiates it from prompt-driven tools (Cursor, Copilot, Claude Code).
3. **VAPS / wiper market opportunity** — the worked example, but containing real Belron-relevant numbers worth preserving on their own merit.
4. **AWS positioning vs the AI coding tools market** — "vibe coding vs SDLC" is deliberate competitive framing.

### Strategic Insights (so far)
1. **Method > tool.** The Working Backwards method is independently valuable to Armo's EA practice — adopt it whether or not Belron adopts Kiro.
2. **Kiro's competitive moat (claimed) is process, not model.** They're competing on workflow opinionation, not raw model quality. If Belron developers don't want a prescriptive workflow, Kiro is a bad fit.
3. **The Anthropic question is the unlock.** If Kiro runs on Claude via Bedrock, the strategic story changes from "Kiro vs Claude Code" to "two doors into the same Anthropic relationship." Need to confirm.
4. **Belron VAPS data point.** The 70%-unrealised / €200m–€1bn figure is a real strategic insight that should be captured separately from the workshop notes — it has value independent of the Kiro context.

### Pattern Recognition
- Connects to: [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]] (MCP governance scope; Kiro's MCP support is the open question).
- Connects to: AI Damage Assessment PoC project — PRFAQ is the right vehicle for stakeholder pitch.
- Connects to: developer tooling positioning across Cursor / Copilot / Claude Code / Kiro — Belron will need a stated position.

---

## Domain Classification
- **Primary Domain:** professional (~90%)
- **Secondary Domains:** project-specific — bleeds into AI Damage Assessment PoC and MCP Governance.
- **Cross-Domain Elements:** the Working Backwards method itself is a transferable EA / personal productivity method.
- **Privacy Level:** confidential — contains internal Belron VAPS numbers and strategic positioning.

## Processing Notes

### Emotional Context
- **Energy Level:** medium (workshop ongoing; observations forming).
- **Emotional Tone:** curious, mildly sceptical of marketing framing, genuinely interested in the method.
- **Implications:** good state for strategic note-taking; less so for snap decisions on tooling adoption.

### Confidence Assessment
- **Overall Analysis:** 70% — workshop is still in progress; final view will firm up post-session.
- **Domain Classification:** 90% — clearly professional with project crossover.
- **Strategic Insights:** 70% — directional reads, to be confirmed post-workshop.
- **Areas requiring clarification:**
  - Foundation model behind Kiro.
  - Whether VAPS numbers shown are live Belron data or illustrative.
  - MCP support in Kiro.

---

---

## Post-Workshop Analysis *(completed 2026-05-30)*

### Outstanding Questions — Answered

**Q: What foundation model powers Kiro?**
**A: Claude Sonnet + Amazon Nova via Amazon Bedrock.** As of May 2026, Kiro supports Claude Opus 4.8 (released May 28) via Bedrock. This resolves the strategic question entirely: Kiro adoption at Belron is **not** a threat to the Anthropic narrative — it is a second door into the same Anthropic relationship. Kiro + Claude Code = two delivery paths for Claude at Belron, both running through Bedrock or the Anthropic API.

**Q: Does Kiro support MCP servers?**
**A: Yes — native MCP support.** Kiro includes native Model Context Protocol support, enabling connection to any MCP-compatible tool server. It also supports the AWS MCP Server (GA May 2026), which wraps the full AWS service catalogue with proper authentication. **Governance implication:** Kiro is in scope for the MCP Governance project. Any Belron team using Kiro is running an MCP-connected agent. This must be addressed in the MCP governance framework.

**Q: Pricing model?**
**A:** Free tier: 50 interactions/month. Pro: **$19/month**. Competitive with Cursor ($20/month). Important caveat: spec-mode requests cost $0.20/credit vs $0.04 for vibe-mode — a 5× premium for the signature feature. Pro gives ~350 mixed requests (225 vibe-mode, 125 spec-mode). For heavy spec-driven use, costs escalate.

**Q: IDE scope — VS Code only?**
**A: Standalone IDE** (not a plugin). Built on VS Code foundations but ships as its own application. Kiro replaced Amazon Q Developer — if any Belron developers use Q Developer, Kiro is the natural upgrade path.

**Q: Data residency / GovCloud?**
**A:** Kiro is available in GovCloud regions (confirmed February 2026). Inference runs through Amazon Bedrock with regional data residency options — compatible with GDPR requirements for EU opcos.

**Q: Are the VAPS wiper numbers live Belron data or workshop illustration?**
**A: Unknown** — not resolved by post-workshop research. The specificity of the numbers (70% unrealised, €200m vs €1bn opportunity, France pilot, next pilots Sweden/Switzerland/Canada) strongly suggests live Belron data rather than a generic retail example. The fact AWS chose a VAPS scenario for a workshop with Belron attendees supports this. **Action still needed:** Confirm with the AWS account team or internal VAPS owner whether these numbers are current.

---

### Spec Artefact Format — What Kiro Actually Produces

Before writing any code, Kiro generates three structured documents:
1. **requirements.md** — functional requirements in EARS (Easy Approach to Requirements Syntax) notation
2. **design.md** — system design, architecture decisions, component breakdown
3. **tasks.md** — structured implementation task list, sequenced and reviewable

The developer reviews and approves all three before code generation begins. This is the "spec-first" claim made concrete. The documents are plain Markdown — version-controllable, reviewable in PRs, portable outside Kiro.

**EA relevance:** requirements.md + design.md are lightweight equivalents of an Architecture Vision + Solution Design. For a small initiative, generating these via Kiro and reviewing them as EA governance artefacts is a plausible lightweight alternative to a full TOGAF review.

---

### Revised Strategic Assessment (post-workshop)

**The Anthropic question is resolved — in the best possible way.**
Kiro runs on Claude via Bedrock. AWS Kiro adoption at Belron = Claude adoption at Belron, routed through AWS infrastructure. The initial risk ("Kiro could dilute the Anthropic narrative") is inverted: Kiro and Claude Code are two compatible delivery paths for Claude at Belron, not competitors.

**Kiro vs Claude Code — they're not the same tool.**
| | Kiro | Claude Code |
|---|---|---|
| **Starting point** | Spec (requirements.md → design.md → tasks.md → code) | Conversation (iterative, context-driven) |
| **Best for** | Greenfield features, structured delivery, regulated environments where artefacts matter | Exploratory work, debugging, refactoring, fast iteration |
| **Governance angle** | Spec artefacts are reviewable EA inputs | Less structured; harder to govern without explicit conventions |
| **Developer profile** | Disciplined SDLC teams; those who want a plan before executing | Fast-moving teams; those comfortable with iterative convergence |
| **Foundation model** | Claude via Bedrock | Anthropic API (Claude) |
| **MCP support** | Native | Native |

**The real competitive framing:** Kiro is not a Cursor replacement for everyone. It's the right tool for developers who need their AI-generated work to be auditable, approvable, and connected to a design artefact trail. For a pre-IPO Belron building technology stories for investors, that distinction matters.

**Working Backwards method — lift immediately, regardless of Kiro.**
The PRFAQ method is platform-independent. The most valuable takeaway from the workshop requires zero AWS commitment. Already incorporated into [[ea-effectiveness-framework]] as Principle 9.

**MCP Governance scope update:**
Kiro must be listed as a governed MCP client in the Belron MCP Governance framework. Any Belron developer running Kiro on internal data sources is operating an MCP-connected agent under EA's governance scope.

---

### Revised Action Items (post-workshop)

**Immediate:**
- [ ] Add Kiro to developer tooling watchlist alongside Claude Code, Cursor, GitHub Copilot 📅 2026-06-05
- [ ] Update MCP Governance framework scope to include Kiro as a governed MCP client 📅 2026-06-05
- [ ] Draft AI Damage Assessment PRFAQ using the Working Backwards method (independent of Kiro) 📅 2026-06-05

**Short-term:**
- [ ] Confirm VAPS/wiper numbers (70% unrealised, €200m–€1bn) with AWS account team or internal VAPS owner — are these live Belron figures? 📅 2026-06-13
- [ ] Assess Kiro pilot feasibility: is there a Belron development team (AWS-native, disciplined SDLC) where a Kiro pilot would fit naturally? Free tier = zero cost to evaluate. 📅 2026-06-13

**Strategic consideration:**
If Belron already uses Amazon Q Developer for any development team, Kiro is the natural upgrade path — and that team is already an Anthropic (via Bedrock) customer without necessarily knowing it. Map the Q Developer footprint.

---

*Post-workshop analysis completed 2026-05-30. Outstanding: VAPS data provenance unconfirmed.*
