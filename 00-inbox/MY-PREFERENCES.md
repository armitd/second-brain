---
type: preferences
created: 2026-07-18
tags: ["#preferences", "#config", "#cog"]
---

# My COG Working Preferences

How I want COG (Claude) to work with me. This file lives in the synced vault, so
these preferences follow me across all my Macs — unlike COG's per-machine auto-memory.

Canonical source of truth for working preferences. When a durable preference emerges
in a session, it belongs here (synced), not only in local auto-memory (per-machine).

## Explain the concept before executing

When a new mechanism, skill, or system concept comes up for the first time, explain
what it is and how it works before acting on it. Not a wall of theory: a clear, short
grounding, then act on my confirmation. For routine, already-understood operations,
just proceed.

**Origin:** In the 2026-07-18 session I paused a `memory-hygiene` run mid-flight to ask
how the vault memory store actually worked before authorising it. I learn the model
first, then approve the action.

## Propose, don't auto-apply, anything out of scope

Keep changes surgical and in-scope. Auto-apply only low-risk, in-scope corrections
(e.g. stamping a date, fixing a verified-wrong count in the file being worked on).
For anything else — file moves, archives, deletes, or edits to files outside the
requested task — present a proposal with evidence and wait for confirmation. Flag
adjacent issues rather than silently fixing them. Prefer scoped git commits over
`git add -A`.

**Origin:** Reinforced repeatedly on 2026-07-18 (flagging `MY-INTEGRATIONS.md` as out of
a sweep's scope; flagging a garden-file title mismatch instead of restructuring;
propose-only archives). Aligns with the vault `CLAUDE.md` scope-lock and hard-stop rules.

## Personal capture lists — check when relevant

I keep four personal capture lists in `02-personal/`: `READING-LIST.md`, `PLACES-TO-VISIT.md`,
`LISTEN.md` (music), and `WATCH.md` (films/TV). These are **mobile capture** — I dump rough
one-liners (e.g. just a name or a place) while out and about, then review and flesh them out
when I'm back online. When I mention one of these lists, or drop a rough item into one, offer to
expand it into the structured format (author/ISBN, location/type, director/year, plus a short
"why"/notes), verifying details with web search rather than guessing. No automated schedule and
no consumption tracking — I review them manually.

**Origin:** 2026-07-22 session. Considered a monthly cloud routine to resurface the lists, but the
vault's frequent Obsidian-Git auto-backup and unverified GitHub App access made cloud write-back
fragile; chose manual review instead, matching the "review when online" workflow.

## Wellbeing: regular journalling practice

I'm building a regular personal journalling habit for wellbeing, using **Day One** on mobile for
the rich stuff (photos, audio, longer reflections). This is distinct from the vault journal
(`07-journal/` via `/create-journal`), which stays for quick, typed, nebulous thoughts at the desk.

- **Prod:** a recurring **Microsoft To Do** reminder, a few times a week (Mon/Wed/Fri) until it
  becomes a habit. Seeded via the COG→To Do drop; recurrence set natively in To Do (the sync can't
  set repeat/reminders). Dial the frequency down once it sticks.
- **Export is ad-hoc and manual:** I run `/process-dayone` myself when I want something to move
  from Day One into the vault. COG should NOT auto-run it or nag me to export.
- **Audio caveat:** the Day One JSON export maps photos/tags/location/weather, not audio — voice
  memos likely stay in Day One only.
- **Privacy:** exported entries enter the git-backed, synced, AI-readable vault; I keep the most
  private entries in Day One and never export them.

**Origin:** 2026-07-23 session. Chose To Do (native notifications, already integrated) over a
cloud routine, given the vault-sync fragility noted above.

## Related
- [[MY-PROFILE|My COG Profile]]
- [[MY-INTERESTS|My Interests & News Sources]]
