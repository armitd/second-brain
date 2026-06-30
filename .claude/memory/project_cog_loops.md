---
name: project-cog-loops
description: Vault-review skill and LOOPS.md added to COG — autonomous loop pattern with verify gates
metadata:
  type: project
---

Added the loop pattern (from gippp69 Mac Mini article, June 2026) to COG:

- `/vault-review` skill at `.claude/skills/vault-review/SKILL.md` — spaced repetition from the vault, finds notes at 7/30/90-day intervals, generates verified review questions, appends to today's daybook. Hard verify rule: questions must reference specific note content, not be answerable from general knowledge.
- `LOOPS.md` in vault root — reference doc covering the TRIGGER/DO/VERIFY/ITERATE pattern, schedulable skills table, cost guidance, and the manual loop template.
- `vault-review` added to `custom_skills` allowlist in `.claude/settings.json` to bypass framework file protection.

**Why:** User interested in autonomous scheduling — COG skills triggering without user opening a chat tab. Cloud agents via `/schedule` are the mechanism.

**How to apply:** When the user asks about automating COG skills or scheduling things, refer them to `LOOPS.md` and the `/schedule` skill. The `/vault-review` skill is the primary new autonomous loop.
