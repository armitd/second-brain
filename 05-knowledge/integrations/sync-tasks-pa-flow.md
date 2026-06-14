---
type: "integration-guide"
created: "2026-06-14"
integration: "COG → Microsoft Planner via OneDrive file drop"
skill: "sync-tasks"
tags: ["#integration", "#power-automate", "#planner", "#tasks", "#onedrive"]
---

# COG → Planner Sync: Power Automate Setup Guide

**Approach:** COG writes a JSON file to OneDrive. PA watches the folder, reads the file, creates Planner tasks, deletes the file.
**PA licence required:** Standard (free connectors only — OneDrive + Planner)
**Setup time:** ~15 minutes

---

## Before You Start

- [ ] Five buckets created in your personal Planner plan: **Inbox**, **AI Damage Assessment**, **MCP Governance**, **Contact Centre**, **Personal**
- [ ] OneDrive for Business (BelronGlobal) installed and syncing on your Mac
- [ ] The `COG-Tasks` folder already created in your OneDrive (done automatically when the skill was set up)
- [ ] Your Planner Plan ID — get this from the URL when viewing your plan in Planner: `https://tasks.office.com/.../#/taskboard/planid/[COPY THIS PART]`

---

## Step 1: Create the Flow

1. Go to **make.powerautomate.com** (sign in with your Belron account)
2. Click **+ Create** → **Automated cloud flow**
3. Name it: `COG Task Sync`
4. Search for trigger: **"When a file is created"** (OneDrive for Business)
5. Click **Create**

---

## Step 2: Configure the Trigger

In the **"When a file is created"** trigger:

- **Folder**: Browse to and select `/COG-Tasks`

---

## Step 3: Get File Content

Click **+ New step** → search **OneDrive for Business** → **Get file content**.

Configure:
- **File**: select `Id` from the trigger dynamic content

Rename this step: `Get file content`

---

## Step 4: Parse the JSON

Click **+ New step** → search **Data Operation** → **Parse JSON**.

Configure:
- **Content**: select `File content` from the **Get file content** step
- **Schema**: paste this:

```json
{
  "type": "object",
  "properties": {
    "sent_at": {
      "type": "string"
    },
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

Rename this step: `Parse task JSON`

---

## Step 5: List Planner Buckets

Click **+ New step** → search **Planner** → **List buckets (V3)**.

Configure:
- **Plan ID**: paste your Planner Plan ID

This runs once per file and fetches all bucket IDs so the loop can match by name.

Rename this step: `List buckets`

---

## Step 6: Add "Apply to each" Loop

Click **+ New step** → **Control** → **Apply to each**.

- **Select output from previous steps**: select `tasks` from the **Parse task JSON** dynamic content

Rename this step: `For each task`

Inside the loop, add these three steps:

---

### Step 6a: Filter Bucket by Name

Inside the loop → **+ Add an action** → **Data Operation** → **Filter array**.

Configure:
- **From**: select `value` from the **List buckets** step
- **Filter row**: click into the left field → select `name` from **List buckets** dynamic content
- **is equal to**
- Right field: select `bucket` from **Parse task JSON** (current item)

Rename: `Filter bucket by name`

---

### Step 6b: Create Planner Task

Inside the loop → **+ Add an action** → **Planner** → **Create a task (V3)**.

Configure:
- **Plan ID**: your Planner Plan ID
- **Title**: select `title` from **Parse task JSON** (current item)
- **Bucket ID**: click the Expression tab and enter:
  ```
  first(body('Filter_bucket_by_name'))?['id']
  ```
- **Due date/time**: click Expression tab and enter:
  ```
  if(empty(items('For_each_task')?['due_date']), null, concat(items('For_each_task')?['due_date'], 'T12:00:00Z'))
  ```

Rename: `Create Planner task`

---

### Step 6c: Add Notes

Inside the loop → **+ Add an action** → **Planner** → **Update task details (V3)**.

Configure:
- **Task ID**: select `id` from **Create Planner task**
- **Description**: select `notes` from **Parse task JSON** (current item)

Rename: `Add task notes`

---

## Step 7: Delete the Processed File

After the loop (outside it) → **+ New step** → **OneDrive for Business** → **Delete file**.

Configure:
- **File**: select `Id` from the trigger dynamic content

Rename: `Delete processed file`

---

## Step 8: Save the Flow

Click **Save**. The flow is now active and watching the COG-Tasks folder.

---

## Step 9: Test It

1. Copy this JSON and save it as `test.json` anywhere on your Mac
2. Move or copy it into `~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/`
3. Wait ~1–2 minutes
4. Check Planner — a task "COG sync test" should appear in the Inbox bucket
5. The file should disappear from COG-Tasks (PA deleted it)

```json
{
  "sent_at": "2026-06-14T12:00:00",
  "tasks": [
    {
      "title": "COG sync test",
      "due_date": "2026-06-21",
      "bucket": "Inbox",
      "notes": "Test task — delete me"
    }
  ]
}
```

---

## Flow Summary

```
Trigger: File created in OneDrive /COG-Tasks
  └── Get file content
  └── Parse task JSON
  └── List Planner buckets
  └── For each task:
        └── Filter bucket by name → get bucket ID
        └── Create Planner task (title, bucket, due date)
        └── Update task details (add source notes)
  └── Delete processed file
```

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| File sits in COG-Tasks unprocessed | PA flow not triggered | Check flow is turned on; OneDrive trigger can take 1–3 min |
| Task created but wrong bucket | Bucket name mismatch | Confirm bucket names in Planner exactly match: `Inbox`, `AI Damage Assessment`, `MCP Governance`, `Contact Centre`, `Personal` |
| Task created with no due date | `due_date` field empty | Expected — task created without a due date |
| File not deleted after processing | Delete step failed | Check Delete file step is outside (after) the Apply to each loop |
| Flow run history shows error | Expression syntax | Check the bucket ID and due date expressions in Steps 6b |

---

*Set up: 2026-06-14 | Skill: /sync-tasks | Drop folder: ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/*
