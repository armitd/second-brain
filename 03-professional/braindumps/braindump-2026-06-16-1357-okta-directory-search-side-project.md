---
type: "braindump"
domain: "professional"
date: "2026-06-16"
created: "2026-06-16 13:57"
themes: ["okta", "side-project", "directory-search", "internal-tooling"]
tags: ["#braindump", "#raw-thoughts", "#professional", "#side-project"]
status: "consolidated"
energy_level: "medium"
emotional_tone: "curious"
confidence: "medium"
consolidated_in: "[[consolidation-2026-07-18]]"
consolidated_date: "2026-07-18"
---

# Braindump: Okta Directory Search side-project

## Raw Thoughts
I'm more interested for a side-project I want to do - to create an OKTA directory search. OKTA is the one place Belron directories comes together.

## Content Analysis

### Main Themes
1. **Side-project, not an official initiative:** This is Armo's own build, distinct from the MCP Governance project work on Okta's agent/MCP capability ([[../../04-projects/mcp-governance/braindumps/braindump-2026-06-16-1355-okta-mcp-agent-support|earlier braindump]]).
2. **Okta as the unifying directory source:** The core premise is that Okta is the single place where Belron's fragmented opco directories converge — making it the natural data source for a cross-opco people/directory search tool.
3. **Directory search as the product:** The goal is a search interface over that unified directory data — not identity governance, not agent management, just findability.

### Supporting Ideas
- Belron spans ~35 countries / ~30,000 employees across many opcos — directory fragmentation is a real, lived problem at that scale, and "one place to search anyone at Belron" is a plausible high-value, low-risk tool.
- Okta's own MCP server (from the earlier braindump) exposes management-API actions via natural language — that's a different use case (admin actions) but the same underlying API surface a directory search tool would likely read from.

### Questions Raised
- Does Okta's API expose enough directory attributes (name, opco, role, location, reporting line) to build a useful search experience, or is the data thin/inconsistent across opcos?
- Read-only directory search vs. the existing Okta MCP server's natural-language management actions — are these complementary (search tool calls Okta's API directly) or could the MCP server itself be the integration point?
- Where would this live — a personal tool, a Claude Code skill/MCP server, an internal web app? Scale and audience (just Armo vs. wider Belron use) changes the right approach a lot.
- Data privacy/access: would this need to be scoped to Armo's own visibility into Okta, or would broader use require formal sign-off given it's effectively an HR/people-data tool?

## Strategic Intelligence

### Key Insights
1. **Distinct from MCP Governance:** This is personal tooling/curiosity, not part of the formal MCP Governance deliverable — worth keeping the two threads separate so the side-project doesn't get pulled into governance scope discussions prematurely.
2. **Build approach likely simplest as an MCP server:** Given the existing COG/Claude Code context, the natural shape of this side-project is a small custom MCP server wrapping Okta's directory API, callable from Claude Code or a Claude Desktop chat — directory search becomes a natural-language query.
3. **Worth scoping size before starting:** "Search" could mean a one-off CLI script Armo runs locally, or a proper internal tool — the trigger and audience should be settled before building.

## Organisational Benefit
Not asked for by Armo as a justification — captured because it sharpens whether this stays a personal tool or becomes a pilot candidate.

- **Cross-opco findability at scale:** At ~35 countries / ~30,000 employees with directories fragmented across opcos, a single search surface answers "who is this person, what opco/role/location are they in" without knowing which local system to check first — a real friction point for anyone working across opco boundaries (EA, central functions, M&A integration work).
- **Faster cross-functional collaboration:** Central/group functions (architecture, IT, finance, M&A) regularly need to find the right local contact in an opco they don't work in day-to-day. A directory search tool shortens that from "ask around" to "search."
- **Onboarding/org-navigation aid:** New joiners or people moving between opcos benefit from a single place to understand "who's who" rather than learning each opco's own people-finder (if one even exists).
- **Low marginal cost, since the data already exists:** Okta is already the identity source of truth — this tool doesn't require new data collection, just a search layer over data that's already being maintained for authentication purposes.
- **Demonstrates a pattern, not just a tool:** A working Okta-backed directory search is also a concrete, low-risk example of "read-only MCP server over an existing enterprise system" — incidentally useful as a reference point for the MCP Governance project's own work on what a well-scoped, low-risk MCP server looks like (without formally being part of that project).

**Clarified intent (Armo, 2026-06-16):** This is a personal project in the sense that Armo is building it off his own initiative, not a commissioned deliverable — but the intent is for it to become a corporate tool used across Belron, not a private utility. Armo's view is that it will generate huge benefit at that scale. This changes the calculus on several of the open questions above: data privacy/access scope, formal sign-off, and audience need to be addressed as if for a real rollout, not deferred as "later, if it proves useful."

## Action Items

### Short-term (1-2 weeks)
- [ ] Check what directory attributes are actually available via Okta's API for Belron's tenant (test with own access) 📅 2026-06-23
- [ ] Identify who owns sign-off for a corporate tool built on Okta directory data (likely IT security / data privacy / Okta platform owner) 📅 2026-06-23
- [ ] Sketch what "corporate tool" means concretely — internal web app, Teams/Slack-style bot, MCP server exposed to other Belron users — before building 📅 2026-06-23

### Strategic Considerations
- Since the intent is corporate-wide use, treat data privacy/access scope as a now-question, not a later-question — building first and asking permission after is the wrong order for an HR/people-data tool at this scale.
- Worth a short pitch/one-pager to whoever owns Okta or IT security early, both to get sign-off and to test whether "huge benefit" lands the same way with them as it does with Armo.
- Keep this separate from the MCP Governance project's Okta research thread to avoid scope creep in either direction — though if this is going corporate, MCP Governance stakeholders may need visibility regardless, since it's another agent/tool surface touching enterprise identity data.

## Connections
- **Related Braindumps:** [[braindump-2026-06-16-1355-okta-mcp-agent-support]] (MCP Governance project — Okta's own MCP server and agent identity governance)

## Domain Classification
- **Primary Domain:** Professional (80%) — self-initiated build, but explicitly intended as a corporate tool rather than personal utility
- **Reasoning:** Armo is building this off his own initiative ("a side-project I want to do") and it isn't part of MCP Governance, CCOTF, or AI Damage Assessment scope — but the stated intent is corporate-wide adoption, not personal use. The "personal project, corporate tool" framing is the key nuance: ownership/origin is personal, intended audience and impact are organisational.

## Processing Notes
### Confidence Assessment
- **Overall Analysis:** Medium — the idea and motivation are clear; technical feasibility (what Okta's API actually exposes) and intended scope/audience are still open.

---

*Processed by COG Brain Dump Analyst*
