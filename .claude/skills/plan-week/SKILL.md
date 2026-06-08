---
name: plan-week
description: Build a structured weekly plan by pulling priorities from the latest check-in, open actions from briefs and projects, and distributing them realistically across the week
roles: [all]
integrations: []
---

# COG Plan Week Skill

## Purpose
Transform the week's known priorities, open actions, and anchored events into a realistic day-by-day plan. The plan is built from vault data — not invented — so it reflects what's actually on your plate.

## When to Invoke
- User types `/plan-week`
- User says "plan my week", "build my week", "what should I focus on this week"
- Monday morning planning session
- After completing a `/weekly-checkin`

## Process Flow

### 1. Get Current Date and Week Boundaries

Run `date '+%Y-%m-%d %A'` using Bash to get today's date and day name.

Calculate:
- **Monday** of the current week (or next Monday if run on a weekend)
- **Friday** of that week
- Use these as the plan boundaries

Label each day with its full date: `Monday 8 June`, `Tuesday 9 June`, etc.

### 2. Gather Inputs

Read all sources in parallel:

#### A. Most Recent Weekly Check-in
Find the latest file in `01-daily/checkins/` (sort by filename, take the most recent).
Extract:
- **Top priorities for next week** (the "Top 3 Must-Do" or equivalent section)
- **Carry forward items** (unresolved from last week)
- **Success criteria** (what a good week looks like)

#### B. Recent Daily Briefs — Open Actions
Read the 3 most recent files in `01-daily/briefs/`.
From each brief, extract all unchecked action items (`- [ ]`) that have a due date falling within this week (or are overdue).
Note the date each action was first flagged.

#### C. Active Project Next Steps
Read `PROJECT-OVERVIEW.md` for each project listed in `00-inbox/MY-PROFILE.md`.
Extract all unchecked `- [ ]` items with due dates this week or earlier.

#### D. Recent Braindumps — Open Actions
Scan `03-professional/braindumps/` and `02-personal/braindumps/` for files from the past 14 days.
Extract any unchecked action items marked as `Immediate` or with due dates this week.

#### E. Anchored Events
Scan all extracted content for mentions of:
- Named events with dates (e.g. "AI Summit London — 10–11 June")
- Named meetings or calls
- Hard deadlines (regulatory dates, submission dates)
These are fixed points the plan must accommodate.

### 3. Build the Week Plan

#### Prioritisation logic

**Tier 1 — Must land this week:**
- Items explicitly flagged as overdue
- Items with hard deadlines this week
- Anchored events (fixed in time)
- Weekly check-in Top 3 priorities

**Tier 2 — Should happen this week:**
- Carry-forward items from last week's check-in
- Project next steps due this week
- Brief action items due this week

**Tier 3 — Nice to do:**
- Items due next week but advanceable
- Research and exploratory tasks

#### Day structure

Distribute Tier 1 and Tier 2 items across Monday–Friday using these principles:
- **Monday:** Highest-priority carry-forward items + stakeholder conversations (people-dependent tasks early in the week)
- **Tuesday–Thursday:** Deep work — documents, frameworks, analysis
- **Friday:** Close loops, review open items, prep for the weekend
- **Never fill every slot** — leave at least one morning or afternoon unscheduled per day as buffer
- **Anchored events block their day** — don't assign heavy work to event days

Each day gets:
- **Focus** — one sentence: what this day is for
- **Tasks** — specific checkable items (max 4–5 per day; fewer is better)

Tier 3 items go into an **Overflow** section, not on specific days.

Items that clearly cannot happen this week go into **Not this week** — be explicit rather than silently dropping them.

### 4. Generate the Plan File

Save to `01-daily/plans/week-plan-YYYY-MM-DD.md` using the Monday date.

```markdown
---
type: "week-plan"
week_of: "YYYY-MM-DD"
created: "YYYY-MM-DD HH:MM"
status: "active"
tags: ["#week-plan", "#planning"]
sources:
  checkin: "weekly-checkin-YYYY-MM-DD.md"
  briefs_scanned: 3
  projects_scanned: [count]
---

# Week Plan — [Date Range, e.g. 8–13 June 2026]

## What Makes This Week a Win

[Pull directly from the weekly check-in's success criteria, or derive from the Top 3 priorities. One sentence.]

---

## Monday [DD Month]

**Focus:** [One sentence — what Monday is for]

- [ ] [Task 1] 📅 YYYY-MM-DD
- [ ] [Task 2] 📅 YYYY-MM-DD
- [ ] [Task 3] 📅 YYYY-MM-DD

---

## Tuesday [DD Month]

**Focus:** [One sentence]

- [ ] [Task 1] 📅 YYYY-MM-DD
- [ ] [Task 2] 📅 YYYY-MM-DD
- [ ] [Task 3] 📅 YYYY-MM-DD

---

## Wednesday [DD Month]

**Focus:** [One sentence — or "AI Summit London" if anchored event]

[If anchored event day:]
🗓 *[Event name] — [location/details]*

- [ ] [Any tasks that can happen around the event] 📅 YYYY-MM-DD

---

## Thursday [DD Month]

**Focus:** [One sentence]

- [ ] [Task 1] 📅 YYYY-MM-DD
- [ ] [Task 2] 📅 YYYY-MM-DD

---

## Friday [DD Month]

**Focus:** Close loops + weekly review

- [ ] [Task 1 — wrap-up or review type] 📅 YYYY-MM-DD
- [ ] [Task 2] 📅 YYYY-MM-DD
- [ ] Review open items and update project files 📅 YYYY-MM-DD

---

## Overflow — This Week If Possible

*Items that belong this week but didn't make the daily cut. Pull from here when a slot opens.*

- [ ] [Item 1]
- [ ] [Item 2]
- [ ] [Item 3]

---

## Not This Week

*Explicitly deferred — not forgotten, just not now.*

- [Item 1] — [brief reason, e.g. "waiting on X" or "delayed to next week"]
- [Item 2]

---

## Week Sources

- Check-in reviewed: [[01-daily/checkins/weekly-checkin-YYYY-MM-DD]]
- Briefs scanned: [[daily-brief-YYYY-MM-DD]] × 3
- Projects reviewed: [list]

---

*Generated by COG Plan Week | [date]*
```

### 5. Confirm and Present

After saving the file:
- Confirm: "Week plan saved to `01-daily/plans/week-plan-YYYY-MM-DD.md`"
- Show the user the **What Makes This Week a Win** line and the **Monday** section
- Mention how many total items were found vs. how many made the daily plan (so they know what's in overflow)
- Offer: "Want to adjust any of the day allocations?"

### 6. Handle Edge Cases

**If no weekly check-in exists:**
Skip step 2A. Build the plan from briefs and project files only. Note at the top of the plan: "No recent check-in found — priorities derived from briefs and project files."

**If run mid-week (not Monday):**
Start the plan from today, not Monday. Label days accordingly. Don't backfill completed days — only plan forward.

**If a day has an anchored event that fills most of the day:**
Cap that day at 1–2 lightweight tasks maximum. Don't stack deep work against a full-day event.

**If the task list is very long (20+ items):**
Be more ruthless with Overflow and Not This Week. A plan with 6 items across 5 days is more useful than 20 items spread thin. Quality of focus beats completeness of capture.

## Design Principles

- **Pull from the vault, don't invent** — every task in the plan should trace back to a source (brief, check-in, project file, braindump)
- **Anchor events first, then fill** — fixed commitments shape the week; tasks fill the gaps
- **Fewer tasks per day, done** beats **many tasks, moved** — max 4–5 tasks per day
- **Friday is for closing, not starting** — don't put new deep work on Friday
- **Not this week is a decision, not a failure** — being explicit about deferral is better than silent omission
- **The plan is a proposal, not a contract** — the user should feel free to adjust after seeing it

## Integration with Other Skills

- **Runs best after `/weekly-checkin`** — the check-in produces the priority inputs this skill consumes
- **Feeds into `/daybook`** — each day's focus line is the seed for that day's daybook
- **Revisit mid-week** — run `/plan-week` again on Wednesday to replan Thursday–Friday if the week has shifted
