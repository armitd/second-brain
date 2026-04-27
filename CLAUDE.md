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
