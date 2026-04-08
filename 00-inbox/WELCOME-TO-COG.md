---
type: guide
created: 2026-04-06
tags: ["#welcome", "#getting-started", "#cog"]
---

# Welcome to Your COG Second Brain, Armo!

Your COG is now personalised and ready to use. Here's how to get started:

## Your Profile Documents

- **[[MY-PROFILE]]** — Your info, role pack, and workflow preferences
- **[[MY-INTERESTS]]** — Topics for your daily briefs (AI, productivity, staff knowledge)
- **[[MY-INTEGRATIONS]]** — GitHub is active; others are disabled until you need them

Edit any of these files anytime — COG reads them when you use skills.

## Your Skills (Ordered by Relevance for Enterprise Architects)

1. **knowledge-consolidation** — Turn your scattered architecture and AI initiative notes into living reference frameworks. *This is your most powerful tool.*
2. **braindump** — Capture ideas, observations, and decisions on the fly. Auto-files into personal/professional/project buckets.
3. **daily-brief** — Personalised briefing on AI tools, productivity tech, field service automation, and staff knowledge systems.
4. **comprehensive-analysis** — Deep 7-day analysis for architecture reviews, technology evaluations, and strategic planning.
5. **meeting-transcript** — Drop in a transcript and get structured decisions, action items, and owners extracted.
6. **weekly-checkin** — Spot patterns across your week — recurring problems, emerging ideas, momentum on initiatives.
7. **auto-research** — Multi-agent parallel research for technology evaluations and vendor comparisons.
8. **url-dump** — Save a URL and get auto-extracted insights filed into your vault.
9. **team-brief** — Cross-reference GitHub and other active tools for a unified picture of what's happening.
10. **update-cog** — Keep your COG framework current with the latest skills and improvements.   test


## Quick Start — Your First 3 Actions

### 1. Try a braindump
Just open Claude Code in this folder and say *"braindump"* — then write whatever's on your mind. Could be thoughts about AI tools you're evaluating, a problem you're seeing with technician knowledge, or anything else. COG will catch and file it.

### 2. Get your daily brief
Say *"daily brief"* to get a curated intelligence briefing across your interest areas:
- AI tools and model developments
- AI for workplace productivity
- Staff knowledge and training technology
- Field service and trade industry applications

### 3. Capture a URL
Found an interesting article about AI for field workers? Say *"url-dump"* and paste the link. COG extracts the key insights and files them in your vault.

## How to Use COG with Claude Code

Open your terminal, navigate to this folder, and launch Claude Code:

```bash
cd ~/Documents/Second\ Brain\ -\ iCloud
claude
```

Then just talk to it naturally. Say things like:
- *"braindump"* → capture thoughts
- *"daily brief"* → morning intelligence
- *"knowledge consolidation"* → synthesise your notes into frameworks
- *"meeting transcript"* → paste a transcript and get structured output
- *"update cog"* → check for framework updates

## Your Vault Structure

```
00-inbox/          ← Your config files (profile, interests, integrations)
01-daily/          ← Daily briefs and weekly check-ins
02-personal/       ← Personal braindumps and development notes
03-professional/   ← Work braindumps, strategy, architecture, AI initiatives
04-projects/       ← Per-project tracking (add when you're ready)
05-knowledge/      ← Consolidated frameworks and patterns (grows over time)
06-templates/      ← Reusable templates
```

## Keeping COG Updated

When new skills are released, run `/update-cog` or:

```bash
./cog-update.sh --check
```

Your notes and profiles are **never touched** by updates — only the framework files change.

---

*Archive or delete this file once you're comfortable with COG. Your second brain is ready.*
