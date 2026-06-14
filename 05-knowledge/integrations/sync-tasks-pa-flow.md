---
type: "integration-guide"
created: "2026-06-14"
integration: "COG → Microsoft Planner via Power Automate"
skill: "sync-tasks"
tags: ["#integration", "#power-automate", "#planner", "#tasks"]
---

# COG → Planner Sync: Power Automate Setup Guide

One-time setup. Takes ~15 minutes. Once done, `/sync-tasks` just works.

---

## Before You Start

You need:
- [ ] Your personal Planner plan already created
- [ ] The five buckets created in that plan: **Inbox**, **AI Damage Assessment**, **MCP Governance**, **Contact Centre**, **Personal**
- [ ] Power Automate access (you already have this)
- [ ] Your Planner Plan ID — get this from the Planner URL when viewing your plan: `https://tasks.office.com/.../#/taskboard/planid/**[THIS PART]**`

---

## Step 1: Create the Flow

1. Go to **make.powerautomate.com**
2. Click **+ Create** → **Instant cloud flow**
3. Name it: `COG Task Sync`
4. Choose trigger: **When an HTTP request is received**
5. Click **Create**

---

## Step 2: Configure the HTTP Trigger

Click the trigger step and paste this into the **Request Body JSON Schema** field:

```json
{
  "type": "object",
  "properties": {
    "tasks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "due_date": {
            "type": "string"
          },
          "bucket": {
            "type": "string"
          },
          "notes": {
            "type": "string"
          }
        }
      }
    }
  }
}
```

**Save the flow** — the HTTP POST URL will appear. Copy it — you'll need it in Step 5.

---

## Step 3: Add "List buckets" Action

Click **+ New step** → search for **Planner** → select **List buckets (V3)**.

Configure:
- **Plan ID**: paste your Planner Plan ID

This retrieves the bucket list so the flow can match bucket names to IDs dynamically. You won't need to hardcode bucket IDs.

---

## Step 4: Add "Apply to each" Loop

Click **+ New step** → search for **Control** → select **Apply to each**.

In the **Select an output from previous steps** field, use the dynamic content picker to select:
- `tasks` (from the HTTP trigger body)

Inside the loop, add the following steps:

---

### Step 4a: Filter Bucket by Name

Inside the Apply to each, click **+ Add an action** → **Data Operation** → **Filter array**.

Configure:
- **From**: select `value` from the **List buckets** output
- **Filter**: `name` **is equal to** → then select `bucket` from dynamic content (from the HTTP trigger's current item)

Rename this step: `Filter bucket by name`

---

### Step 4b: Create the Planner Task

Add another action inside the loop: **Planner** → **Create a task (V3)**.

Configure:
- **Plan ID**: your Planner Plan ID
- **Title**: select `title` from the HTTP trigger dynamic content (current item)
- **Bucket ID**: `first(body('Filter_bucket_by_name'))?['id']`
  *(Type this expression manually using the Expression tab)*
- **Due date/time**: Use this expression:
  `if(empty(items('Apply_to_each')?['due_date']), null, concat(items('Apply_to_each')?['due_date'], 'T12:00:00Z'))`
  *(This sets noon UTC on the due date, or leaves it blank if no date was provided)*

Rename this step: `Create Planner task`

---

### Step 4c: Add Notes to the Task

Add another action inside the loop: **Planner** → **Update task details (V3)**.

Configure:
- **Task ID**: select `id` from the **Create Planner task** output
- **Description**: select `notes` from the HTTP trigger dynamic content (current item)

Rename this step: `Add task notes`

---

## Step 5: Save and Get the Webhook URL

1. Click **Save** (top right)
2. Click back on the **HTTP trigger** step
3. Copy the **HTTP POST URL** — it looks like:
   `https://prod-xx.westeurope.logic.azure.com:443/workflows/abc123.../triggers/manual/paths/invoke?api-version=...`

---

## Step 6: Add the Webhook URL to COG

Open `00-inbox/MY-INTEGRATIONS.md` and add to the Active section:

```markdown
**Microsoft 365 — Planner Task Sync**
- planner-webhook-url: https://prod-xx.westeurope.logic.azure.com/...
- plan-name: [your plan name]
- buckets: Inbox, AI Damage Assessment, MCP Governance, Contact Centre, Personal
```

---

## Step 7: Test It

Run this in terminal to verify the flow works end-to-end:

```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "tasks": [
      {
        "title": "COG sync test task",
        "due_date": "2026-06-21",
        "bucket": "Inbox",
        "notes": "Test from COG sync-tasks skill"
      }
    ]
  }' \
  'YOUR_WEBHOOK_URL_HERE'
```

Check Planner — a task called "COG sync test task" should appear in the Inbox bucket. Delete it once confirmed.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| 400 Bad Request | JSON schema mismatch | Check the payload matches the schema exactly |
| Task created but wrong bucket | Bucket name mismatch | Check bucket names in Planner exactly match: Inbox, AI Damage Assessment, MCP Governance, Contact Centre, Personal |
| Due date missing in Planner | Date format issue | Ensure skill sends `YYYY-MM-DD` format |
| Flow not triggering | Webhook URL expired | Re-save the PA flow, copy the new URL |
| No task notes appearing | Update task details step failing | Check the Task ID expression in Step 4c |

---

## Flow Summary (Quick Reference)

```
Trigger: HTTP POST (JSON)
  └── List Planner buckets
  └── Apply to each task:
        └── Filter bucket array by name
        └── Create Planner task (title, bucket ID, due date)
        └── Update task details (add notes/source)
```

---

*Set up: 2026-06-14 | Skill: /sync-tasks | See .claude/skills/sync-tasks/SKILL.md*
