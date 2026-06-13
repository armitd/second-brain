---
name: process-daybook
description: Read today's daybook and run it through the braindump pipeline — no copy-pasting required
roles: [all]
integrations: []
---

# COG Process Daybook Skill

## Purpose
Read today's daybook file (or a specified date), extract the raw content, and run it through the full braindump analysis pipeline — producing a structured braindump file without the user needing to copy-paste anything. Marks the daybook as processed when done.

## When to Invoke
- User types `/process-daybook`
- User says "process my daybook", "turn my daybook into a braindump", "process today's notes"
- User provides a date: `/process-daybook 2026-06-12`

## Process Flow

### 1. Get Date

- If the user provided a date argument (e.g. `/process-daybook 2026-06-12`), use that date.
- Otherwise, run `date '+%Y-%m-%d'` using Bash to get today's date. NEVER guess the date.

### 2. Find the Daybook

Look for `01-daily/daybooks/daybook-YYYY-MM-DD.md`.

**If it doesn't exist:**
```
No daybook found for [date]. You can create one with /daybook.
```
Stop.

**If it exists but has no content** (only the template comment, nothing below it):
```
Your daybook for [date] is empty — nothing to process yet.
```
Stop.

**If it already has `status: "processed"` in frontmatter:**
```
The daybook for [date] has already been processed.
Want me to process it again? (This would create a second braindump from the same notes.)
```
Wait for confirmation before proceeding.

### 3. Extract Raw Content

Read the daybook file. Extract everything below the `<!-- Append thoughts here... -->` comment line — that is the user's raw captured content. Ignore the frontmatter and the comment itself.

### 4. Read Context Files

Read the following to personalise the braindump analysis (same as the braindump skill):
- `00-inbox/MY-PROFILE.md` — user's name, role, active projects
- `03-professional/COMPETITIVE-WATCHLIST.md` — for competitive intelligence detection

Also run `date '+%Y-%m-%d %H:%M'` to get the current timestamp for the output file.

### 5. Auto-Classify Domain

Scan the raw content and auto-classify without asking the user (they're not at their desk to answer questions):

- **Personal:** Health, family, hobbies, personal goals, non-work topics
- **Professional:** Work themes not tied to a specific project (strategy, leadership, EA practice)
- **Project-specific:** Mentions of a named active project → use that project's slug
- **Mixed:** Spans multiple domains → save to `00-inbox/`

If the content clearly maps to one of the user's active projects, assign it to that project. If ambiguous, default to `professional`.

### 6. Run Braindump Analysis

Apply the full braindump processing pipeline to the extracted content:

#### Phase 1: Content Analysis
- **Main Themes:** 3–5 primary topics
- **Supporting Ideas:** Related concepts and detail
- **Questions Raised:** Explicit and implicit questions
- **Decisions Contemplated:** Choices being considered
- **Action Items:** Tasks and commitments

#### Phase 2: Strategic Insight Extraction
- **Key Insights:** 3–5 most important realisations
- **Pattern Recognition:** Connections to previous thinking
- **Strategic Implications:** What this means for goals and active projects

#### Phase 3: Competitive Intelligence Detection
Scan content for mentions of companies or people from `COMPETITIVE-WATCHLIST.md`. If found, note them for extraction (Step 8).

### 7. Generate Braindump File

Create the braindump file using the same format as the `/braindump` skill:

```markdown
---
type: "braindump"
domain: "[personal|professional|project-specific|mixed]"
project: "[project-name]"  # only if project-specific
date: "YYYY-MM-DD"
created: "YYYY-MM-DD HH:MM"
source: "daybook"
source_file: "01-daily/daybooks/daybook-YYYY-MM-DD.md"
themes: ["theme1", "theme2", "theme3"]
tags: ["#braindump", "#from-daybook", "#domain-tag"]
status: "captured"
energy_level: "[high|medium|low]"
emotional_tone: "[primary-emotion]"
confidence: "[high|medium|low]"
---

# Braindump: [Auto-generated descriptive title]

## Raw Thoughts
[Original daybook content preserved exactly as captured]

## Content Analysis

### Main Themes
1. **Theme 1:** [description and significance]
2. **Theme 2:** [description and significance]
3. **Theme 3:** [description and significance]

### Supporting Ideas
- [Supporting concept 1]
- [Supporting concept 2]

### Questions Raised
- [Question 1]
- [Question 2]

### Decisions Contemplated
- [Decision being considered]

## Strategic Intelligence

### Key Insights
1. **Insight 1:** [description and implications]
2. **Insight 2:** [description and implications]
3. **Insight 3:** [description and implications]

### Pattern Recognition
- **Connection to Previous Thinking:** [links to earlier braindumps or frameworks if evident]
- **Recurring Patterns:** [themes that keep appearing]

### Strategic Implications
- [How this affects goals or active projects]

## Action Items

**Note:** Calculate actual due dates from today's date.

### Immediate (24–48 hours)
- [ ] [specific action] 📅 [YYYY-MM-DD]

### Short-term (1–2 weeks)
- [ ] [specific action] 📅 [YYYY-MM-DD]

### Strategic Considerations
- [Longer-term implications]

## Connections
- **Source:** [[daybook-YYYY-MM-DD]]
- **Related Projects:** [[project1]], [[project2]]

## Domain Classification
- **Primary Domain:** [domain] ([confidence]%)
- **Reasoning:** [why this classification]
- **Privacy Level:** [public|private|confidential]

---
*Processed by COG from daybook — [YYYY-MM-DD HH:MM]*
```

Save to the same location rules as `/braindump`:
- **Personal:** `02-personal/braindumps/braindump-YYYY-MM-DD-HHMM-<slug>.md`
- **Professional:** `03-professional/braindumps/braindump-YYYY-MM-DD-HHMM-<slug>.md`
- **Project:** `04-projects/[project-slug]/braindumps/braindump-YYYY-MM-DD-HHMM-<slug>.md`
- **Mixed:** `00-inbox/braindump-YYYY-MM-DD-HHMM-<slug>.md`

### 8. Extract Competitive Intelligence (if detected)

If any content references companies or people from the competitive watchlist, follow the same competitive intelligence extraction process as `/braindump` — create or update the relevant file in `03-professional/` and cross-reference from the braindump.

### 9. Mark Daybook as Processed

Update the daybook file's frontmatter: change `status: "open"` to `status: "processed"`.
Also append a one-line note at the bottom of the daybook file:

```
---
*Processed → [[braindump-YYYY-MM-DD-HHMM-slug]]*
```

### 10. Confirm Completion

Report back:
```
Daybook for [date] processed.

Braindump saved to: [file path]
Main themes: [theme1], [theme2], [theme3]
Action items: [count] captured
[If competitive intel extracted]: Also extracted competitive intelligence for [company/person].

Daybook marked as processed.
```

If the content was thin (fewer than ~50 words), note:
```
Note: The daybook was fairly sparse — you may want to add more context via /braindump.
```

## Notes
- This skill is intentionally non-interactive. It reads and processes without asking questions, because the user is likely back at their desk wanting a quick turnaround, not a Q&A session.
- If domain classification is genuinely ambiguous, default to `professional` rather than asking.
- The `source: "daybook"` and `source_file:` frontmatter fields distinguish these braindumps from direct `/braindump` captures, which is useful for pattern analysis later.
- Never delete or overwrite the daybook file — only append the processed note and update the status field.
