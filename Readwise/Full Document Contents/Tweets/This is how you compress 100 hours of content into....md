# This is how you compress 100 hours of content into...

![rw-book-cover](https://pbs.twimg.com/profile_images/2022077728359682048/UWClPPZX.jpg)

## Metadata
- Author: [[Mr. Buzzoni]]
- Full Title: This is how you compress 100 hours of content into...
- Category: #tweets
- Summary: This is how you compress 100 hours of content into 10 minutes!

just tried NotebookLM + Obsidian and it's actually insane

> the "YouTube to NotebookLM" extension lets you dump entire channels into NotebookLM and get a structured mega-summary in minutes

> Audio Overviews turns any PDF, report or notes into a podcast-style dialogue - perfect for walking or driving

> Book Filter: upload your Obsidian vault + a new book, ask "is there anything new for me here?" - if no, skip it and save dozens of hours

this combo feels like compression for knowledge

the stack:
📁 NotebookLM
↳ https://t.co/YJYHE2kHL5

📁 YouTube to NotebookLM Chrome Extension
↳ https://t.co/2ZnZzGcysm

this combo + Obsidian vault = unfair advantage
- URL: https://twitter.com/polydao/status/2059873049508532426/?rw_tt_thread=True

## Full Document
**This is how you compress 100 hours of content into 10 minutes!**

*just tried NotebookLM + Obsidian and it's actually insane*

>   
> the "**YouTube to NotebookLM**" extension lets you dump entire channels into NotebookLM and get a structured mega-summary in minutes
> 
> **Audio Overviews** turns any PDF, report or notes into a podcast-style dialogue - perfect for walking or driving
> 
> **Book Filter:** upload your Obsidian vault + a new book, ask "*is there anything new for me here?*" - if no, skip it and save dozens of hours
> 
> 

  
this combo feels like compression for knowledge

**the stack:**

📁 NotebookLM

↳ <https://t.co/YJYHE2kHL5>

📁 YouTube to NotebookLM Chrome Extension

↳ <https://t.co/2ZnZzGcysm>

this combo + Obsidian vault = unfair advantage 

Your browser does not support the video tag.

![](https://pbs.twimg.com/profile_images/2035229727414534145/aWap3Jbq.jpg)

[CyrilXBT](https://twitter.com/cyrilXBT)
[@cyrilXBT](https://twitter.com/cyrilXBT)

![How To Use Obsidian + Vellum To Build A Second Brain That Thinks 24/7](https://pbs.twimg.com/media/HJRxktiXUAAhB4x.jpg)

A chief of staff reads everything you've read, remembers everything you've forgotten, and briefs you every morning on what matters. 

Here's how to build one for $0. 

**What You Need Before You Start** 

Obsidian — download at [obsidian.md](http://obsidian.md). Free for personal use. Your notes are plain markdown files stored locally on your machine. 

Vellum — create your account at [vellum.ai](http://vellum.ai). Credits are prepaid and passed through at cost with zero markup. Light daily usage runs a few dollars a month. 

Readwise — [readwise.io](http://readwise.io). Aggregates every highlight you make across articles, Kindle, Twitter bookmarks, and Pocket into one place. Has a native Obsidian integration that routes everything automatically. 

N8N — [n8n.io](http://n8n.io). Open source automation tool. Runs the workflows that connect your capture sources to your vault. Self-host it or use their cloud version. 

Now you have everything you need, go through these next steps. 

**Step One: Build The Vault Architecture** 

Open Obsidian. Create a new vault. Name it CHIEF. 

Now create this exact folder structure: 

CHIEF/ 

├── 00-INBOX/ 

├── 01-CAPTURES/ 

│ ├── articles/ 

│ ├── ideas/ 

│ ├── patterns/ 

│ ├── questions/ 

│ └── numbers/ 

├── 02-CONNECTIONS/ 

├── 03-PROJECTS/ 

└── 04-VELLUM/ 

├── [VELLUM.md](http://VELLUM.md) 

└── workflows/ 

This structure is not arbitrary. Every folder has exactly one job. 

00-INBOX is where everything lands first. Unprocessed. Raw. The goal at capture time is speed not structure. You never sort things manually at capture time. 

01-CAPTURES is organized by note type not topic. This is the most important architectural decision in the entire system. When you organize by topic a note about a crypto pattern and a note about a psychological principle never meet. When you organize by type they both land in the patterns folder and Vellum finds the connection between them automatically. 

02-CONNECTIONS is where synthesized insights live. These are not raw captures. They are new ideas that emerge from the relationship between two or more notes. This is where your best thinking comes from. 

03-PROJECTS is for active work. One subfolder per project. Everything related to what you are currently researching or building lives here. 

04-VELLUM is the intelligence layer's working directory. This is where Vellum reads its instructions and stores its working files. 

**Step Two: Install The Essential Plugins** 

In Obsidian go to Settings → Community Plugins → turn off Safe Mode → Browse. 

Install these three: 

**Templater** — runs dynamic templates with real logic. You will use this for automated note formatting when captures arrive from N8N. 

**Dataview** — queries your vault like a database. Surfaces notes by tag, date, or any property you define. Essential for the weekly connection sessions. 

**Obsidian Git** — backs up your entire vault to a private GitHub repository automatically every hour. Set it once. Never think about it again. 

**Step Three: Set Up Automated Capture** 

The capture layer has one job. Collect everything without asking anything of you. 

Every friction point in capture is a future gap in your knowledge base. Set this up once. Never touch it again. 

**Articles and highlights:** 

Install Readwise at [readwise.io](http://readwise.io). 

Add the browser extension. Every article you read, highlight the sentences that matter. Readwise stores them automatically. You do nothing else. No tagging. No summarizing. Highlight and move on. 

Enable the native Obsidian sync inside Readwise settings. Every highlight flows into your 01-CAPTURES/articles/ folder automatically as a formatted markdown file. 

**Quick capture from anywhere:** 

Build a Telegram bot that accepts any message you send and routes it directly to your 00-INBOX folder. 

Copy this N8N workflow exactly: 

Node 1: Telegram Trigger → Event: message → Chat ID: your\_bot\_id 

Node 2: Code Node → Filename: 00-INBOX/{{date}}-[capture.md](http://capture.md) → Content: 

#### **Quick Capture**

{{message}} Date: {{date}} Source: Telegram 

Node 3: Write File → Path: /your-vault/00-INBOX/ → Operation: create 

Takes 30 minutes to build. Runs forever after that. 

An idea that hits you at 2am. A wallet you want to track. A pattern you noticed in the market. Send it to the bot. It lands in your vault automatically. 

**Voice notes:** 

Record anything longer than a quick thought as a voice memo. Run it through Whisper for a clean transcript. Paste the transcript into your Telegram bot. It lands in INBOX automatically. 

**Step Four: Write The [VELLUM.md](http://VELLUM.md) File** 

This is the most important file in the entire system. 

Without it Vellum starts every session knowing nothing about who you are, what you are working on, or what you want from it. With it Vellum is a collaborator who has been reading your notes for months. 

Create this file at 04-VELLUM/[VELLUM.md](http://VELLUM.md). Copy this template exactly: 

#### **CHIEF SYSTEM — [VELLUM.md](http://VELLUM.md)**

**Identity** 

My name is [YOUR NAME]. I am [WHAT YOU DO — be specific]. My focus right now: [The one thing you are trying to get better at]. My goals for 2026: [3 specific outcomes you are working toward]. 

**This Vault** 

This is my permanent knowledge base and thinking system. Every note is raw material for decisions, research, and original thinking. Nothing here is decoration. 

**Vault Structure** 

* 00-INBOX: unprocessed captures — always check here first
* 01-CAPTURES/articles: processed highlights and article notes
* 01-CAPTURES/ideas: my own thinking and observations
* 01-CAPTURES/patterns: the same principle appearing in different domains
* 01-CAPTURES/questions: things I genuinely do not know the answer to
* 01-CAPTURES/numbers: real data points with specific numbers attached
* 02-CONNECTIONS: synthesized insights from two or more captured notes
* 03-PROJECTS: active research and work folders
* 04-VELLUM: your working directory

[Posted May 27, 2026 at 2:28AM](https://twitter.com/cyrilXBT/status/2059461814333673705)
