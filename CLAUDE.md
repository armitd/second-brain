# COG Second Brain — Framework Instructions

## Integration Preferences

Before using any external integration in a skill, check `00-inbox/MY-INTEGRATIONS.md`:

- **Active integrations**: Use normally.
- **Disabled integrations**: Skip silently. Do not attempt to call their tools, do not suggest setting them up, do not mention them in output.
- **Unknown integrations** (not listed in either section): Ask the user if they want to set it up. If they say no, add it to the Disabled section.

## Role Packs

COG uses role packs (`.claude/roles/*.md`) to personalize skill recommendations and integration suggestions per user role.

### How role matching works
1. During onboarding, the user's role text is matched against `role_id` and `aliases` in each role pack's YAML frontmatter.
2. The matched role pack is stored as `role_pack` in `00-inbox/MY-PROFILE.md` frontmatter.
3. When suggesting skills or workflows, check the user's `role_pack` and order recommendations by role relevance.

### Role-aware behavior
- **Skill suggestions**: When a user asks "what can COG do?" or similar, prioritize skills listed in their role pack. Show role-specific explanations from the pack.
- **Integration prompts**: When a skill needs an integration the user hasn't set up, check their role pack to provide role-specific context for why it matters.
- **No role pack match**: If the user's role doesn't match any pack, recommend core skills (`roles: [all]`) and let them discover team skills organically.

### Available role packs
Role packs live in `.claude/roles/`. New roles can be added by dropping a file following the `_template.md` format.

## Vault Structure

### User configuration files (`00-inbox/`)
- `MY-PROFILE.md` — User info, role pack, agent mode, active projects
- `MY-INTERESTS.md` — Topics for daily briefs
- `MY-INTEGRATIONS.md` — Active/disabled external service integrations

### Professional tracking (`03-professional/`)
- `COMPETITIVE-WATCHLIST.md` — Companies/people being tracked

### Framework files (updated via `cog-update.sh` or `/update-cog`)
- `.claude/skills/` — Claude Code skills (18 skills, including custom: process-readwise)
- `.claude/roles/` — Role packs for personalized recommendations
- `.kiro/powers/` — Kiro powers
- `.gemini/commands/` — Gemini CLI commands
- `AGENTS.md` — Universal agent documentation

### Content directories (never touched by updates)
- `00-inbox/` — Profiles, interests, integrations
- `00-inbox/raw/` — Raw source documents (PDFs, Word docs, reports received externally). Immutable originals. Do not process automatically — wait for user to reference them in a session.
- `01-daily/` — Briefs and check-ins
- `02-personal/` — Personal braindumps (private)
- `03-professional/` — Professional braindumps and strategy
- `04-projects/` — Per-project tracking
- `05-knowledge/` — Consolidated insights and patterns

## Raw Sources Convention

**Readwise is the primary raw sources layer** (per Karpathy's LLM Wiki pattern). All external content — articles, PDFs, tweets, books, web pages — should flow through Readwise first, then be processed by COG from there.

### Intended flow
```
External content → Readwise (save via app/extension) → Readwise/ vault → COG processes on demand
```

### `Readwise/` — Primary raw vault
- `Readwise/Tweets/` — saved tweets by author
- `Readwise/Full Document Contents/Tweets/` — full thread captures by topic (75 threads)
- `Readwise/Articles/` — saved articles with highlights
- `Readwise/Books/` — books with highlights
- `Readwise/Full Document Contents/Articles/` — full-text article exports
- `Readwise/Full Document Contents/Books/` — full-text book exports

### `00-inbox/raw/` — Fallback only
For documents that cannot go through Readwise: internal/confidential files, Belron-internal reports, documents with data residency concerns. Not the default path.

### Rules
- **Never auto-process** either location. Wait for the user to reference content in a session.
- **Check `Readwise/` first** before asking the user to re-paste or re-upload anything.
- **When a user drops a PDF or article into a session**, suggest saving it to Readwise so it flows through the standard path in future. Only suggest `00-inbox/raw/` for confidential/internal documents.
- **When processing raw content**, note the source in the output file's frontmatter: `source_readwise: "Readwise/..."` or `source_file: "00-inbox/raw/filename"`.
- **Suggest Readwise** when a user pastes a long article, tweet thread, or shares a public PDF they want to keep.

## Behaviour Rules

Rules governing what COG can do without explicit instruction:

- **Scope lock:** Only modify files explicitly requested. If a related file needs attention, mention it — don't touch it. One task = one scope.
- **Confirm before rewriting:** Never rewrite or substantially restructure an existing braindump, project file, or knowledge document without explicit instruction. Adding a section is fine; restructuring requires confirmation.
- **Hard stop before destructive actions:** Deleting files, overwriting braindumps, removing project content — always confirm first. No exceptions.
- **No autonomous scheduling:** Never create or modify cron jobs, scheduled tasks, or reminders without being asked. The user decides what runs automatically.
- **Summarise changes:** After any session that modifies vault files, state which files were touched, what changed, and what was deliberately left unchanged.

## Permanent Facts

Always-true constraints that apply in every session — do not re-derive or contradict these:

- **Who:** Armo — Enterprise Architect at Belron (global windscreen repair/replace company, ~35 countries, ~30,000 employees)
- **Context:** Belron is pre-IPO (H2 2026 target). Major IT decisions carry IPO risk implications.
- **Active projects:** AI Damage Assessment PoC · MCP Governance · Contact Centre of the Future · 60th Birthday Party · Jurassic Coast Walk
- **Primary AI advocacy goal:** Getting Belron onto Anthropic/Claude — the AI Damage Assessment PoC is the primary vehicle; H&F's Anthropic relationship is background context, not a lever
- **Framework files are immutable:** `.claude/`, `.kiro/`, `.gemini/`, `AGENTS.md`, `CLAUDE.md` — updated only via `cog-update.sh` or `/update-cog`. Never restructure or delete these.
- **Readwise/ is immutable:** Raw source files. Read-only. Never delete, rename, or modify.
- **COG memory lives in:** `.claude/projects/.../memory/` — auto-saved across sessions by the memory system

## Session Hygiene

Guidelines for keeping session quality high as conversations grow:

- **Use /compact when sessions get long:** Context quality drops as a session fills up. If a session has covered multiple distinct topics (e.g. daily brief + braindumps + research + project updates), run `/compact` to compress history before starting the next heavy task. Fresh context produces better output.
- **Start a new session for substantive analytical work:** Don't continue a long operational session (Readwise processing, task filing, brief generation) into complex synthesis work (auto-research, position papers, weekly check-ins). Start fresh so the model has full context budget available.
- **Model selection by task type:**
  - **Opus** — complex synthesis, auto-research, position papers, weekly check-ins, architecture decisions, anything requiring deep reasoning across multiple sources
  - **Sonnet** — routine execution: Readwise processing, filing braindumps, daily briefs, adding tasks, small edits
- **Use Plan Mode (Shift+Tab) before complex skill runs:** For auto-research, weekly check-ins, or any multi-step skill with significant vault writes, switch to Plan Mode first. Let the model think through the approach before acting — prevents wasted work from wrong-direction execution.

## Known Failure Patterns

See `ERRORS.md` in the vault root for a log of approaches that have failed and what worked instead. Check it when retrying a previously-attempted operation.
