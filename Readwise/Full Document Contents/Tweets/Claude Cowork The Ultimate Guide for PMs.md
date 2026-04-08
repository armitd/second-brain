# Claude Cowork: The Ultimate Guide for PMs

![rw-book-cover](https://pbs.twimg.com/profile_images/2006064264495206400/UtSOHwhm.jpg)

## Metadata
- Author: [[Paweł Huryn]]
- Full Title: Claude Cowork: The Ultimate Guide for PMs
- Category: #tweets
- Summary: Claude Cowork is a powerful desktop agent that helps manage complex tasks by breaking them into smaller parts and working on them in parallel. It supports many plugins and connects to tools like Gmail and Slack to improve productivity for everyday work. Unlike Claude Chat, Cowork focuses on workflows and delivering files directly, making it ideal for product managers and business users.
- URL: https://x.com/pawelhuryn/status/2025939744316682724/?s=12&t=iGBahVZb08SpJ-immXsWdQ&rw_tt_thread=True

## Full Document
![Claude Cowork: The Ultimate Guide for PMs](https://pbs.twimg.com/media/HBvqNj-W4AAytvD.jpg)

Anthropic just shipped **Claude Cowork for Windows and Intel-based macOS** with full feature parity to the version released in January. It’s now **available on all platforms** for Pro, Max, Team, and Enterprise plans.

Everyone’s hyping Claude Code. But if you’re not a developer, Cowork might be a better default option for everyday tasks — and almost nobody’s talking about it enough. 

I'm a former engineer. I can use the terminal just fine. But prototyping aside, I choose Cowork for day-to-day work: analyzing and drafting emails, reorganizing files, preparing contracts, managing invoices, and even configuring my OS. 

Same model as Claude Code. Same skill format, same connector types. 

Technically, Code can do everything Cowork does. The difference is how you get there. Code needs git worktrees, tmux, and CLI flags. Cowork gives you a simple visual interface. 

This guide covers everything you need to know: 

1. What Cowork Actually Is
2. Cowork vs. Chat: Why it’s a Different Beast
3. Plugins and Skills in Claude Cowork
4. MCPs: Connecting Cowork to Your World
5. Scheduled Tasks
6. A 1-Minute Hack That Makes Claude Desktop 2x More Powerful
7. How to Give Claude Cowork Cross-Session Memory

---

#### 1. What Cowork Actually Is

Cowork is not a chat interface with a new skin. It’s an autonomous desktop agent built into the Claude Desktop app. 

When you open the Cowork tab, you’re giving Claude access to a sandboxed Linux VM running on your machine. Inside that sandbox, Claude can write code, execute scripts, create files (Word docs, slide decks, spreadsheets, PDFs), and connect to services like Gmail, GitHub, and Slack (you don't set this up — Anthropic manages it). 

You describe what you need. Cowork plans the work, breaks it into sub-agents that run in parallel, and delivers output as clickable files you can open directly.

![Image](https://pbs.twimg.com/media/HBvmUKAWoAA4oKL.jpg) 

![Image](https://pbs.twimg.com/media/HBvmZU1XsAAmzr5.jpg) 

A few things that set it apart from Chat: 

* **It plans and tracks work.** Give Cowork a complex task and it decomposes it into subtasks, shows you the plan, and works through it step by step. You can watch progress in real time and steer mid-task. Chat doesn’t do this.
* **It coordinates parallel work.** Cowork can spawn sub-agents — independent Claude instances that each get their own context — to work on different parts of a task simultaneously.
* **It creates real files.** Not an artifact. Actual .docx, .pptx, .xlsx, and .pdf files delivered to the folder you granted access to.
* **It’s sandboxed — but not entirely.** Cowork runs in a VM, so it can’t touch your OS or files outside the folder you shared. But inside that folder, it has full read/write/delete access.
* **It connects to your tools.** Gmail, GitHub, Slack, Google Drive, and more via built-in connectors. Plus any custom tool via MCP servers.

---

#### 2. Cowork vs. Chat: Why it’s a Different Beast

Many of you already use Claude Chat in the Desktop app. You might be wondering: what does Cowork add? Here’s my comparison:

![Image](https://pbs.twimg.com/media/HBvmp8AWwAA93n1.jpg) 

In short, Cowork adds what matters for getting real work done: sub-agent coordination that handles parallel work, task decomposition, and files delivered directly to your folder instead of chat artifacts. 

**Chat is for conversations. Cowork is for workflows.** 

---

#### 3. Plugins and Skills in Claude Cowork

When Anthropic unveiled AI tools automating legal and financial research in early 2026, legacy [software stocks dropped $285 billion](https://finance.yahoo.com/news/anthropic-slams-wall-street-285-195732491.html) in a single day. Investors saw AI agents moving into the application layer — legal, sales, marketing, finance — and repriced the entire software sector. 

The plugins sitting in your Cowork sidebar are part of what triggered that reaction. Here’s how they work. 

**What Are Skills?** 

Let’s start with skills. They are reusable instruction manuals that teach Claude how to approach specific, repeatable tasks. Say “create a Word doc” and the docx skill loads. You can also trigger skills explicitly — type / in Cowork for autocomplete. 

The format works across Claude ecosystem and third-party tools like Cursor, Windsurf, and Codex CLI. 

Built-in skills include pdf, docx, pptx, xlsx, canvas-design, algorithmic-art, and skill-creator. 

Skills don’t all load at once. Claude reads only a short description of each skill (~100 tokens) to decide which ones are relevant, then loads full instructions only when needed. This keeps your context window clean. 

**The Cowork Plugin Panel** 

Cowork has a dedicated Plugins panel that Chat doesn’t. You can browse, install, upload, and create plugins from a visual UI:

 

Each plugin bundles skills with slash commands, for example “Product Management:”

![Image](https://pbs.twimg.com/media/HBvnTv3XoAIjyPQ.jpg) 

**Skill and Plugin Access Across Tools** 

Here’s the high-level picture. In this article we focus on Cowork:

![Image](https://pbs.twimg.com/media/HBvnljAXIAIhUSa.jpg) 

**Default plugins:** 

* Cowork ships with 11 plugins from anthropics/knowledge-work-plugins (productivity, product-management, legal, finance, marketing, data, etc.)
* Code’s marketplace defaults to anthropics/claude-code (developer workflows: agent-sdk-dev, frontend-desing, feature-dev, code-review, etc.).But you can add **any marketplace repo to either too**l — load Code’s developer plugins into Cowork, or Cowork’s business plugins into Code. Same skill format, fully cross-compatible.

**Note:** Cowork and Code Tab have separate, isolated plugin panels. Installing a plugin in one doesn't make it available in the other. Skills uploaded via Claude Desktop settings are shared across Chat, Cowork, and Code Tab. 

**Where to Find More Skills and Plugins** 

Beyond built-in skills and Anthropic’s plugins, there’s a growing ecosystem worth exploring. All essential sources: 

* github[.]com/anthropics/skills — Anthropic's official repo. Document skills (docx, xlsx, pptx, pdf) plus creative, technical, and enterprise examples
* github[.]com/anthropics/knowledge-work-plugins — Cowork's default plugin registry. The 11 business-role plugins
* github[.]com/anthropics/claude-code — Developer-focused workflows. Code's marketplace, open "Plugins"
* claudemarketplaces[.]com — A marketplace of marketplaces you can add to Cowork or Code
* github[.]com/travisvn/awesome-claude-skills — Community-curated. Battle-tested skills for TDD, debugging, collaboration
* github[.]com/sickn33/antigravity-awesome-skills — 868+ universal agentic skills. Role-based bundles: Startup Founder, Marketing & Growth, and more
* skills[.]sh — Product strategy frameworks, pricing strategy, launch playbooks, discovery interview guides, PRD generator, analytics, resume optimizer

---

#### 4. MCPs: Connecting Cowork to Your World

MCP stands for Model Context Protocol — the open standard by Anthropic. Each MCP server exposes tools Claude can call. 

A [custom Gmail MCP](https://github.com/GongRzhe/Gmail-MCP-Server) gives Claude search\_emails, send\_email, read\_email. The official [official GitHub MCP](https://github.com/github/github-mcp-server) gives it create\_pull\_request, list\_issues. You get the idea. 

There are three ways to connect MCP servers to Claude, and understanding the difference matters. When I say “Claude Desktop” below, I mean all three tabs in the Desktop app: Chat, Cowork, and Code. 

Three types of MCP connections

![Image](https://pbs.twimg.com/media/HBvns0zXcAEZRbz.jpg) 

**Remote and custom connectors** work everywhere — including [claude.ai](http://claude.ai) in your browser. You add them in *“Connectors > Manage connectors”*:

![Image](https://pbs.twimg.com/media/HBvnyi-WwAA8TaG.jpg) 

**Extensions** are how Anthropic packages local MCP servers for one-click install — they show up in both the Extensions panel (to install/remove) and the Connectors panel (to toggle on/off). You manage them in *“Settings > Extensions”*:

![Image](https://pbs.twimg.com/media/HBvn3dnWEAE4Qe-.jpg) 

**Custom MCP servers** are managed by editing a JSON config. Click *“Menu > Developer > App Config File…”* An example content with a custom Gmail and Outlook MCPs that allow my Cowork to Draft and edit emails:

{

 "mcpServers": {

 "gmail": {

 "command": "npx",

 "args": [

 "@gongrzhe/server-gmail-autoauth-mcp"

 ]

 },

 "outlook-assistant": {

 "command": "C:\nvm4w\nodejs\node.exe",

 "args": [

 "C:\Users\Dell\outlook-mcp\index.js"

 ],

 "env": {

 "USE\_TEST\_MODE": "false",

 "OUTLOOK\_CLIENT\_ID": "6c***\*-******\*******\*",***

 "OUTLOOK\_CLIENT\_SECRET": "53***\*******\*\_******\****\*\*\*\*"

 }

 }

 }

} 

What might be a bit confusing is that Claude Desktop presents them all in a single “Connectors” interface with on/off toggles:

![Image](https://pbs.twimg.com/media/HBvoDuAXcAAYiXA.jpg) 

**Per-Tool Permissions** 

For every connector, you can set individual tools to Allow (runs automatically), Ask (confirms before running), or Block (never runs). You could allow Claude to search your emails but block it from sending them. Click: *“Settings → Connectors”*:

![Image](https://pbs.twimg.com/media/HBvoJ8YXMAA0BiV.jpg) 

**MCP Config Is Not Shared Across All Tools** 

Different tools use different config methods. For example, adding an MCP server to Chat makes it available in Cowork, and Code Tab, but not Code CLI:

![Image](https://pbs.twimg.com/media/HBvoSiYXsAEUXvJ.jpg) 

**Windows gotcha:** If you installed Claude Desktop via the Microsoft Store (MSIX), the "Edit Config" button may open the wrong file. The app reads from the MSIX virtualized path, not %APPDATA%\Claude. Check GitHub issue #26073 if MCP servers silently fail to load. 

**Where to Find MCP Servers** 

* github[.]com/modelcontextprotocol/servers: Official MCP server repo — filesystem, GitHub, Google Drive, Slack, and more
* modelcontextprotocol[.]io/examples: Official MCP directory — reference implementations for many services
* github[.]com/punkpeye/awesome-mcp-servers: Community-curated list — hundreds of MCP servers by category
* mcp[.]so: MCP server registry with search and install instructions

---

#### 5. Scheduled Tasks

You'll see this feature mentioned often alongside Cowork — it gets bundled into broader Claude Desktop coverage. Worth knowing it exists, but in my tests it's unreliable.

![Image](https://pbs.twimg.com/media/HBvog4kXYAAMKFh.jpg) 

For scheduled automation, [n8n](https://www.productcompass.pm/p/the-ultimate-guide-to-n8n-for-pms) or an MCP-based approach will serve you better. 

---

#### 6. A 1-Minute Hack That Makes Claude Desktop 2x More Powerful

I can’t believe some people working with AI don’t know about Desktop Commander. That’s one of the highest-ROI moves. And it takes < 1 minute: 

1. Open Claude Desktop
2. In a chat window click: *“+ > Connectors > Manage connectors”*
3. Click: *“Browse connectors > All > Desktop Commander”*
4. Select tools that do not require your approval**The result:** Chat, Cowork, and Code Tab can do **virtually anything on your laptop** including installing MCP servers or accessing any file.

**Example 1: Claude Desktop installed and configured an MCP server based on the URL** 

This works in Claude Chat/Cowork/Code Tab:

![Image](https://pbs.twimg.com/media/HBvonw-XMAAaQk6.jpg) 

**Example 2: Claude Desktop reorganized files on my desktop.** 

This works in Claude Chat/Cowork/Code Tab:

![Image](https://pbs.twimg.com/media/HBvorxFWwAAO3MB.jpg) 

**Tips**: 

* Disable the Claude in Chrome extension when not needed, so Claude doesn’t default to web-based actions (sometimes, it prefers it, even when it has a dedicated MCP).
* Consider which actions require your approval. That said, unlike OpenClaw, none of those tools can take actions on their own. You can also observe what they are doing or disable the connector when not in use. Over time, I learned to trust them.

---

#### 7. How to Give Claude Cowork Cross-Session Memory

Two simple steps: 

1. Enable Desktop Commander extensions in *“Settings → Connectors”*
2. Copy this to *“Settings → Cowork → Global instructions”*\*## Memory Management

When you discover something valuable for future sessions — architectural decisions,

bug fixes, gotchas, environment quirks — immediately append it to {your\_folder}/[memory.md](http://memory.md)

Don't wait to be asked. Don't wait for session end.

Keep entries short: date, what, why. Read this file at the start of every session.\* 

This costs almost zero tokens and survives crashes, compaction, and new sessions. 

**Advanced: Structured Memory** 

Split into multiple files so Claude loads only what’s relevant:

\*## Memory Management 

Maintain a structured memory system rooted at .claude/memory/ 

##### Structure

* [memory.md](http://memory.md) — index of all memory files, updated whenever you create or modify one
* [general.md](http://general.md) — cross-project facts, preferences, environment setup
* domain/{topic}.md — domain-specific knowledge (one file per topic)
* tools/{tool}.md — tool configs, CLI patterns, workarounds

##### Rules

1. When you learn something worth remembering, write it to the right file immediately
2. Keep [memory.md](http://memory.md) as a current index with one-line descriptions
3. Entries: date, what, why — nothing more
4. Read [memory.md](http://memory.md) at session start. Load other files only when relevant
5. If a file doesn't exist yet, create it

##### Maintenance

When I say "reorganize memory": 

1. Read all memory files 

2. Remove duplicates and outdated entries 

3. Merge entries that belong together 

4. Split files that cover too many topics 

5. Re-sort entries by date within each file

6. Update [memory.md](http://memory.md) index 

7. Show me a summary of what changed\* 

Example of what my Claude Code writes to /memory/tools/[docker.md](http://docker.md)

\*## Docker

* 2026-02-12: Must use `host.docker.internal` not `localhost` for DB connections from containers — spent 30 min debugging this
* 2026-02-13: Project Dockerfile needs `--platform=linux/amd64` on M1 Macs or builds silently produce broken images
* 2026-02-13: docker compose v2 uses `docker compose` (no hyphen) — old scripts with `docker-compose` fail on CI\*

**Bonus: How to Give Claude Code (Tab/CLI) Memory** 

For short term memory “Claude forgot what we discussed yesterday”: 

* In the Code Tab sessions are visible in the left menu
* In Claude Code CLI use --continue to continue the previous session

Paste the same prompt into your Claude Code instructions but replace your custom path with “.claude/[memory.md](http://memory.md)” 

An alternative only for Claude Code (.md format is often more than you need): https://github[.]com/thedotmack/claude-mem

*/plugin marketplace add thedotmack/claude-mem*

/plugin install claude-mem 

#### **------**

#### [Bonus] A Visual Summary: Claude Chat vs. Cowork vs. Code

![Image](https://pbs.twimg.com/media/HBvqWLoWMAALPmP.jpg) 

#### **------**

#### Thanks for Reading The Product Compass

It’s amazing to learn and grow together. 

I’ll demonstrate working with Cowork and answer your questions on Tuesday, during Office Hours. Register and add to your calendar: <https://go.productcompass.pm/premium>. 

Next week, I’ll publish more about Claude Code, creating skills, and **dozens of PM plugins and skills I created for paid subscribers**. 

Consider subscribing, if you haven't already. Accorting to 130K+ readers it's the #1 most hands-on AI PM newsletter: productcompass[.]pm 

---

[@kelhendros](https://twitter.com/kelhendros) Yes, it doesn't understand its own configuration. 

Perhaps you can just quickly export this to PDF. It's free for everyone: [productcompass.pm/p/claude-cowor…](https://www.productcompass.pm/p/claude-cowork-guide)
