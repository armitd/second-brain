---
type: "braindump"
domain: "professional"
date: "2026-05-31"
created: "2026-05-31 15:01"
themes: ["claude-setup", "claude-code", "productivity", "cog-architecture", "second-brain"]
tags: ["#braindump", "#claude", "#claude-code", "#setup", "#cog", "#productivity"]
status: "consolidated"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
source_readwise: "Readwise/Full Document Contents/Tweets/Boris Cherny, the creator of Claude Code at Anthropic, just....md"
consolidated_in: "[[consolidation-2026-07-18]]"
consolidated_date: "2026-07-18"
---

# Braindump: Boris Cherny — 40 Claude Features Most Users Never Configure

## Raw Thoughts
Boris Cherny (creator of Claude Code at Anthropic) — "40 features most users have never touched." Make this a braindump rather than a tweet booklet. The core argument: it's about setup, not prompting skill. Most users leave 30+ features unconfigured.

---

## The Core Argument

**"The difference between power users and casual users is setup, not intelligence, experience, or secret prompting hacks."**

Cherny's observation: Claude ships with dozens of features buried in menus, disabled by default, or simply never announced. Most intermediate users discover half of them by accident. The people producing output that looks like it came from a team of five are not better prompters — they have set up their environment properly.

This is directly relevant to COG: the vault + CLAUDE.md + skills architecture is exactly the "setup" layer Cherny is describing. The question is whether COG's configuration is complete, or whether there are gaps in the 40-feature map that COG doesn't cover.

---

## The 40 Features — Part 1: Claude Chat Settings (1–12)

*(Note: full thread captured 12 of 40 features — the rest were in Parts 2–4 which weren't captured in Readwise. Summary covers what was captured.)*

| # | Feature | What It Does | COG Equivalent |
|---|---|---|---|
| 01 | **Custom Instructions** | Persistent system prompt injected into every conversation. Write role, industry, output format, communication style. | ✅ **CLAUDE.md** — COG's primary system prompt. Already configured. |
| 02 | **Memory** | Claude remembers things across conversations when told explicitly ("remember that I use X"). | ✅ **COG Memory system** — auto-saves to `.claude/projects/.../memory/`. Already implemented. |
| 03 | **Projects** | Dedicated workspace with its own system prompt + uploaded files. One project per workflow. | ✅ **COG Skills + CLAUDE.md** — partially equivalent. Skills = workflow specialisation. Knowledge files in CLAUDE.md projects = vault documents. |
| 04 | **Artifacts** | Renders code/docs/visualisations in a live preview panel. Interactive, downloadable. | ⚠️ **Not COG's concern** — Artifacts are a claude.ai web/desktop UI feature, not a Claude Code CLI feature. Worth enabling if using claude.ai alongside COG. |
| 05 | **Knowledge Files in Projects** | Upload documents into a Project as permanent context. Never paste the same doc again. | ✅ **CLAUDE.md + Readwise** — vault files as context. COG reads from vault. |
| 06 | **Extended Thinking** | Makes Claude reason step-by-step before answering. Dramatically better on complex analysis. | ✅ **CLAUDE.md session hygiene** — "Use Opus for complex synthesis." Extended thinking is the Opus-class behaviour. Plan Mode (Shift+Tab) is the COG equivalent for pre-task deliberation. |
| 07 | **LaTeX Rendering** | Renders equations natively. | ❌ **Not applicable** — low relevance for Armo's use cases. |
| 08 | **Web Search** | Real-time web search in claude.ai. | ✅ **COG daily-brief skill** uses WebSearch tool. Already integrated. |
| 09 | **Conversation Styles** | Set preferred tone/verbosity once, applies everywhere. | ✅ **CLAUDE.md tone instructions** — COG's "terse, no summaries" preference is captured in memory and CLAUDE.md. |
| 10 | **Keyboard Shortcuts** | Full shortcut set — new conversation, copy response, navigate chats. | ⚠️ **Partially configured** — COG has keybindings.json. Worth auditing against the full Claude shortcut set. |
| 11 | **Multiple Parallel Conversations** | Run several conversations simultaneously in different tabs/sessions. Separate research from writing from coding. | ✅ **COG + Claude Code** — Boris Cherny himself runs 10–15 parallel Claude Code sessions daily. COG's skill architecture supports this — different sessions, different skills. |
| 12 | **Download and Share Artifacts** | Export any artifact as a file or shareable link. | ⚠️ **claude.ai web only** — less relevant for Claude Code CLI use. |

---

## The Boris Cherny Workflow (from Suryansh Tiwari)

Boris Cherny runs **10–15 Claude Code sessions in parallel daily**. While one is running, he has 5 in his terminal + 5–10 on the web simultaneously. The "real weapon" is his setup — not his prompting style.

This is the operational model to aspire to:
- Multiple parallel workstreams, each in its own focused session
- No re-explaining context — CLAUDE.md + Projects + Memory do the setup work
- Sessions isolated by purpose: research session, writing session, code session, brainstorm session

The COG architecture supports this but the practice isn't deliberate. Worth making it deliberate.

---

## The `claude-code-setup` Plugin

Anthropic released an official `claude-code-setup` plugin that scans a project and recommends:
- Hooks
- Skills
- MCP servers
- Subagents
- Automations

Then sets them up step-by-step.

**Install:** `/plugin install claude-code-setup@claude-plugins-official`

**Relevance to COG:** COG already has a substantial skill/hook/MCP architecture. Running `claude-code-setup` on the Second Brain project would either (a) confirm COG is already well-configured, or (b) surface gaps. Low-cost to check.

---

## Strategic Intelligence

### Key Insights

1. **COG already covers most of the 12 captured features.** Custom Instructions (CLAUDE.md), Memory (auto-save system), Projects (skill workspaces), Extended Thinking (Opus + Plan Mode), Web Search (WebSearch tool), Conversation Styles (CLAUDE.md tone settings). The setup investment in COG is real and well-targeted.

2. **The Artifacts gap is a claude.ai UI concern, not a COG concern.** Artifacts are a visual rendering feature of claude.ai web/desktop. Claude Code (COG's runtime) uses file writes instead of visual artifacts. These are different delivery mechanisms for the same output. Not a COG gap.

3. **Parallel session discipline is the underexploited opportunity.** The 12 features don't make you 12× more productive individually — the multiplier comes from running parallel sessions for parallel workflows. COG's skill architecture was designed for this but the practice of actually running 5+ concurrent sessions with distinct purposes isn't habitual yet.

4. **`claude-code-setup` is worth running as a COG audit.** The plugin was built by Anthropic specifically to surface configuration gaps. Running it on the Second Brain project is a 5-minute investment that could validate (or improve) the COG architecture.

### Pattern Recognition
- Connects to: [[05-knowledge/booklets/tweets/claude-code-ecosystem-setup-2026-05-30]] — the tweet booklet that covers this same theme
- Connects to: [[braindump-2026-05-26-1018-aws-kiro-workshop]] — "bounded independence" frame; Kiro's spec-first approach is analogous to COG's CLAUDE.md-first approach
- Connects to: [[05-knowledge/consolidated/ea-effectiveness-framework]] — Principle 9 (Working Backwards / PRFAQ) has the same "set the spec first" logic

### Strategic Implications
- The comparison table above shows COG is well-configured for 8 of 12 captured features. The gaps (Artifacts, LaTeX) are low priority for Armo's use cases.
- The `claude-code-setup` audit could surface Part 2–4 features (features 13–40) that COG doesn't yet address — particularly Claude Code-specific features, API features, and Cowork features that weren't captured in the Readwise thread.
- Parallel session discipline (5–10 concurrent) is the most immediately actionable upgrade.

---

## Action Items

### Immediate (24–48 hours)
- [ ] Run `/plugin install claude-code-setup@claude-plugins-official` in the Second Brain project and review recommendations against current COG setup. 📅 2026-06-01

### Short-term (1–2 weeks)
- [ ] Find and read the full Boris Cherny content covering features 13–40 (Parts 2–4 not captured in Readwise). Search: "Boris Cherny 40 Claude features Part 2" or check the original podcast/post he references. The API features, Claude Code-specific features, and Cowork features are likely the most valuable uncaptured content. 📅 2026-06-07
- [ ] Audit COG's keybindings.json against the full Claude keyboard shortcuts list — quick wins likely. 📅 2026-06-07
- [ ] Deliberately practise the parallel sessions model for one week: run research, braindump, and project sessions simultaneously rather than sequentially. 📅 2026-06-07

### Strategic Considerations
- Parts 2–4 of the 40-feature list are the unknown: Claude Desktop/Cowork features, API features, Claude Code-specific features. These are likely where the biggest COG gaps exist. The current COG architecture is strong on web/chat features but the API and Claude Code-specific configuration may have uncaptured depth.
- The core thesis ("setup > prompting") is already COG's architecture philosophy. This validates the investment made in CLAUDE.md, memory, and skills — and suggests doubling down on that direction rather than changing course.

---

## Connections
- **Related Braindumps:** [[braindump-2026-05-26-1018-aws-kiro-workshop]] (spec-driven development, bounded independence)
- **Knowledge Base:** [[05-knowledge/booklets/tweets/claude-code-ecosystem-setup-2026-05-30]] (tweet booklet covering same theme)
- **Source:** [[Readwise/Full Document Contents/Tweets/Boris Cherny, the creator of Claude Code at Anthropic, just....md|Full thread →]]

---

## Domain Classification
- **Primary Domain:** Professional (85%)
- **Reasoning:** Directly about optimising the EA work tool (COG/Claude Code). Cross-domain relevance to personal productivity.
- **Cross-Domain Elements:** Parallel session model applies to personal projects too.
- **Privacy Level:** Private

## Processing Notes

### Confidence Assessment
- **Overall Analysis:** 88% — strong on what was captured (features 1–12); lower confidence on features 13–40 (not in Readwise capture)
- **COG mapping accuracy:** 90% — the equivalences identified are well-grounded in COG's architecture
- **Areas Requiring Clarification:** Full 40-feature list (Parts 2–4 not captured) — this is the main gap in the analysis

---

*Processed by COG Brain Dump Analyst | Source: Readwise thread capture (partial — 12 of 40 features) + Khairallah AL-Awady / Suryansh Tiwari supplementary tweets*
