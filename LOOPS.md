# COG Loops

COG skills can run as autonomous, scheduled loops — not just on-demand commands. This document explains the pattern and maps it to the schedulable skills in this vault.

The insight: every time you trigger a skill manually, you are the trigger. Close the session and the work stops. A scheduled cloud agent removes you from the loop — the skill runs whether or not you open Claude Code.

---

## The Loop Pattern

Every autonomous COG loop has four parts:

```
TRIGGER   → a schedule kicks it off, or a new file appears
DO        → Claude runs the skill
VERIFY    → output is checked against a hard rule (not a vibe)
ITERATE   → fix what failed, or stop if it passes
```

**The verify step is the part most people skip.** "The summary covers all key points" is a vibe — Claude grades its own homework and writes itself a 9. "The output has all five sections AND at least 2 [[wiki links]] to existing notes" is a hard rule Claude cannot talk its way past.

Every loop also needs a stop condition. Without one, a loop spins on a bad input all night. The rule: verify passes, stop. It doesn't, skip or log and move on.

---

## Schedulable COG Skills

| Skill | Suggested Cadence | Hard Verify Rule |
|-------|-------------------|-----------------|
| `/vault-review` | Daily 06:00 | Each question names or quotes something specific from the source note — not answerable from general knowledge |
| `/daily-brief` | Weekdays 06:30 | All stories verified within 7-day window; at least 2 tier-1 sources cited |
| `/process-readwise` | Sunday 07:00 | Every processed item has `status: processed` in frontmatter; at least 1 `[[wiki link]]` to an existing note |
| `/weekly-checkin` | Sunday 19:00 | All sections present; at least 3 patterns identified across the week |

Run `/vault-review` before `/daily-brief` so vault questions land in the daybook before the brief is written.

---

## Setting Up Automation

Two approaches. Pick one; they are not mutually exclusive.

### Option A: Local cron (launchd) — Python scripts calling the API directly

The approach from the article. Scripts live in `scripts/`, triggered by macOS launchd. Your Mac needs to be on, but nothing else is required — no browser tab, no Claude Code session.

**First-time setup (one-off):**

```bash
# 1. Create a virtual environment and install the Anthropic SDK
cd ~/Library/Mobile\ Documents/iCloud\~md\~obsidian/Documents/Second\ Brain/scripts
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Make the wrapper executable
chmod +x run_vault_review.sh

# 3. Install the launchd agent
cp com.cog.vault-review.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.cog.vault-review.plist
```

**Test it runs without waiting until 06:00:**

```bash
source scripts/.venv/bin/activate
python3 scripts/vault_review.py
```

**Check the log after a scheduled run:**

```bash
cat /tmp/cog-vault-review.log
```

**To stop/uninstall:**

```bash
launchctl unload ~/Library/LaunchAgents/com.cog.vault-review.plist
```

Scripts available: `scripts/vault_review.py` (the loop), `scripts/run_vault_review.sh` (launchd wrapper), `scripts/com.cog.vault-review.plist` (schedule config).

---

### Option B: Cloud agent scheduling — via `/schedule` skill

Runs on Claude's infrastructure, not locally. Mac does not need to be on.

```
/schedule vault-review — run daily at 06:00, prompt: "Run /vault-review and append to today's daybook"

/schedule daily-brief — run weekdays at 06:30, prompt: "Run /daily-brief for Armo"

/schedule process-readwise — run every Sunday at 07:00, prompt: "Run /process-readwise — process up to 20 unprocessed items"
```

---

## Cost Guidance

Loops accumulate token cost because context grows with each iteration. Keep verify criteria tight so loops stop quickly.

- **Haiku**: tagging, scoring, sanity checks, question generation, simple classification — anything where the task is clear and short
- **Sonnet**: synthesis, research, complex reasoning, weekly check-ins, auto-research
- **Opus**: architecture decisions, deep analysis, anything needing extended reasoning

`/vault-review` and `/process-readwise` should run on Haiku. `/daily-brief` and `/weekly-checkin` warrant Sonnet.

---

## Manual Loop Template

Use this in any Claude session when you want loop-style output without scheduling. Paste it as the first message and fill in the blanks:

```
You will work in a loop until the task meets the bar.

TASK:
[describe exactly what you want produced]

SUCCESS CRITERIA (strict, no soft passes):
- [criterion 1]
- [criterion 2]
- [criterion 3]

LOOP PROTOCOL — repeat every turn:
1. PLAN   — state the single next step.
2. DO     — produce or improve the work.
3. VERIFY — score the result 1-10 on each criterion.
             Be brutally honest. List what is still weak.
4. DECIDE — if every criterion is 8 or above, print FINAL and stop.
             Otherwise print ITERATING and fix the weakest point first.

RULES:
- Never call it done until every criterion is 8 or above.
- Each pass must fix the weakest score from the last VERIFY.
- Do not ask questions. Make a sensible assumption, note it, and keep going.

Begin.
```

This works for anything: drafting a position paper, refining a strategy doc, writing a job spec. If you find yourself reaching for it more than three times on the same type of task, that task is a candidate for a scheduled COG skill.

---

## Adding a New Loop

If you want to automate a skill that isn't in the table above:

1. **Run it manually three times.** If it produces useful output reliably, it's worth automating. If not, fix the skill first.
2. **Define the hard verify rule.** One sentence, measurable, no soft criteria.
3. **Add it to the schedule** via `/schedule`.
4. **Add it to this table** so the pattern is documented.

New skills added to `.claude/skills/` also need to be added to the `custom_skills` list in `.claude/settings.json` to bypass framework file protection.

---

*COG Loop Reference — inspired by the Mac Mini loop pattern (gippp69, June 2026)*
