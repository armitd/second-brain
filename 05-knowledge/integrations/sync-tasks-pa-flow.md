---
type: "integration-guide"
created: "2026-06-14"
integration: "COG → Project for the web via OneDrive file drop"
skill: "sync-tasks"
tags: ["#integration", "#power-automate", "#planner", "#project", "#tasks", "#onedrive"]
---

# COG → Planner Sync: Power Automate Setup Guide

**Approach:** COG writes a JSON file to OneDrive. PA watches the folder, reads the file, creates tasks in Project for the web, deletes the file.
**PA licence required:** Standard (free connectors — OneDrive + Project for the web)
**Project licence required:** Project Plan 1 or higher (you have this — confirmed by Gantt/timeline view)
**Setup time:** ~15 minutes

> **Note:** Your plan is at `planner.cloud.microsoft` with a timeline/Gantt view — this is a **Project for the web** premium plan. The PA flow uses the **"Project for the web"** connector, not the classic "Planner" connector. The JSON format COG writes is unchanged.

---

## Before You Start

- [ ] Five buckets created in your project: **Inbox**, **AI Damage Assessment**, **MCP Governance**, **Contact Centre**, **Personal**
- [ ] OneDrive for Business (BelronGlobal) installed and syncing on your Mac
- [ ] The `COG-Tasks` folder already created in your OneDrive (done automatically when the skill was set up)
- [ ] Your Project ID — in PA, the "Project for the web" connector lets you pick your project from a dropdown, so you may not need to copy the ID manually. If you do need it, it appears in the URL at `planner.cloud.microsoft` as a GUID parameter.

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

## Step 5: List Project Buckets

Click **+ New step** → search **Project for the web** → **List buckets**.

Configure:
- **Project**: select your project from the dropdown (PA discovers your projects automatically)

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

### Step 6b: Create Project Task

Inside the loop → **+ Add an action** → **Project for the web** → **Create a task**.

Configure:
- **Project**: select your project from the dropdown
- **Task name**: select `title` from **Parse task JSON** (current item)
- **Bucket**: click the Expression tab and enter:
  ```
  first(body('Filter_bucket_by_name'))?['id']
  ```
- **Due date**: click Expression tab and enter:
  ```
  if(empty(items('For_each_task')?['due_date']), null, concat(items('For_each_task')?['due_date'], 'T12:00:00Z'))
  ```
- **Description**: select `notes` from **Parse task JSON** (current item)

> Notes go directly into the **Create a task** Description field — no separate update step needed (unlike classic Planner).

Rename: `Create project task`

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
  └── Get file content (OneDrive)
  └── Parse task JSON (Data Operation)
  └── List buckets (Project for the web)
  └── For each task:
        └── Filter bucket by name → get bucket ID (Data Operation)
        └── Create a task (Project for the web — title, bucket, due date, description)
  └── Delete processed file (OneDrive)
```

> Six steps total. Notes/description go directly into Create a task — no separate update step needed.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| File sits in COG-Tasks unprocessed | PA flow not triggered | Check flow is turned on; OneDrive trigger can take 1–3 min |
| "Project for the web" connector not visible | Connector not available in your tenant | Search for "Project" — it may appear as "Project for the Web (Preview)" |
| Task created but wrong bucket | Bucket name mismatch | Confirm bucket names in your project exactly match: `Inbox`, `AI Damage Assessment`, `MCP Governance`, `Contact Centre`, `Personal` |
| Task created with no due date | `due_date` field empty | Expected — task created without a due date |
| File not deleted after processing | Delete step failed | Check Delete file step is outside (after) the Apply to each loop |
| Flow run shows connection error | Project licence not activated | Confirm Project Plan 1+ licence is assigned in M365 admin |
| Flow run history shows expression error | Expression syntax | Check the bucket ID expression in Step 6b — ensure step names in expressions match your renamed steps exactly |

---

*Set up: 2026-06-14 | Skill: /sync-tasks | Drop folder: ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/*
