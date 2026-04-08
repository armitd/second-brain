# GitHub Copilot X: The AI-powered developer experience

![rw-book-cover](https://github.blog/wp-content/uploads/2023/03/GitHub-Copilot-X-Announcement.jpg?fit=3840%2C2160)

## Metadata
- Author: [[Thomas Dohmke]]
- Full Title: GitHub Copilot X: The AI-powered developer experience
- Category: #articles
- Summary: GitHub has launched Copilot X, an advanced AI tool that enhances the software development experience by integrating AI support throughout the entire coding process. This new version includes features like chat and voice interactions, AI-generated pull request descriptions, and documentation assistance. By using OpenAI's GPT-4 model, Copilot X aims to make coding faster and more efficient for developers.
- URL: https://github.blog/news-insights/product-news/github-copilot-x-the-ai-powered-developer-experience/

## Full Document
![GitHub Copilot X announcement](https://github.blog/wp-content/uploads/2023/03/GitHub-Copilot-X-Announcement.jpg?zoom=2&resize=1600%2C850)GitHub Copilot X announcement
At GitHub, our mission has always been to innovate ahead of the curve and give developers everything they need to be happier and more productive in a world powered by software. When we began experimenting with large language models several years ago, it quickly became clear that generative AI represents the future of software development. We partnered with OpenAI to create [GitHub Copilot](https://github.com/features/copilot/), the world’s first at-scale generative AI development tool made with OpenAI’s Codex model, a descendent of GPT-3.

GitHub Copilot started a new age of software development as an AI pair programmer that keeps developers in the flow by auto-completing comments and code. And less than two years since its launch, GitHub Copilot is already [writing 46% of code](https://github.blog/2023-02-14-github-copilot-for-business-is-now-available/) and helps [developers code up to 55% faster](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/).

[![](https://github.blog/wp-content/uploads/2023/08/1200x300-Blog_Ad-Master-1-1.png?w=1200)](https://github.com/features/copilot?utm_source=blog&utm_medium=blogB&utm_campaign=cta&utm_content=copilot)
**But AI-powered auto-completion is just the starting point.** Our R&D team at [GitHub Next](https://githubnext.com/) has been working to move past the editor and evolve GitHub Copilot into a readily accessible AI assistant throughout the entire development lifecycle. This is [GitHub Copilot X](https://github.com/features/preview/copilot-x)—our vision for the future of AI-powered software development. We are not only adopting OpenAI’s new GPT-4 model, but are introducing chat and voice for Copilot, and bringing Copilot to pull requests, the command line, and docs to answer questions on your projects.

With AI available at every step, we can fundamentally redefine developer productivity. We are reducing boilerplate and manual tasks and making complex work easier across the developer lifecycle. By doing so, we’re enabling every developer to focus all their creativity on the big picture: building the innovation of tomorrow and accelerating human progress, today.

Let’s jump in.

>  ****Want to see what’s new?**** Discover GitHub Copilot X—our vision for the future of AI-powered software development. [Learn more >](https://github.com/features/preview/copilot-x) 
> 
> 

![A graphic showing how many developers and companies have already used GitHub Copilot and how it's helping improve productivity and happiness.](https://github.blog/wp-content/uploads/2023/03/Blog-Bento-Box-Metrics.png?w=4800)Many developers and companies have already used GitHub Copilot, and it’s helping improve productivity and happiness.
#### A new AI-powered developer experience 🧑‍💻

* **A ChatGPT-like experience in your editor with GitHub Copilot Chat:** We are bringing a chat interface to the editor that’s focused on developer scenarios and natively integrates with VS Code and Visual Studio. This does far more than suggest code. GitHub Copilot Chat is not just a chat window. It recognizes what code a developer has typed, what error messages are shown, and it’s deeply embedded into the IDE. A developer can get in-depth analysis and explanations of what code blocks are intended to do, generate unit tests, and even get proposed fixes to bugs.

GitHub Copilot Chat builds upon the work that OpenAI and Microsoft have done with ChatGPT and the new Bing. It will also join our voice-to-code AI [technology extension we previously demoed](https://githubnext.com/projects/copilot-voice/), which we’re now calling GitHub Copilot Voice, where developers can verbally give natural language prompts.

[Sign up for the technical preview >](https://github.com/github-copilot/chat_waitlist_signup)

<https://github.blog/wp-content/uploads/2023/03/01-Copilot-Chat-Debug-Blog.mp4#t=0.001>
* **Copilot for Pull Requests:** You can now sign up for a technical preview of [the first AI-generated descriptions for pull requests on GitHub](https://githubnext.com/projects/copilot-for-pull-requests). This new functionality is powered by OpenAI’s new GPT-4 model and adds support for AI-powered tags in pull request descriptions through a GitHub app that organization admins and individual repository owners can install. These tags are automatically filled out by GitHub Copilot based on the changed code. Developers can then review or modify the suggested description.

[Enroll your repository in the technical preview >](https://copilot4prs.githubnext.com/login)

<https://github.blog/wp-content/uploads/2023/03/02-Copilot-for-PRs-Ghost-Text-Blog.mp4#t=0.001>
**This is just the first step we’re taking to rethink how pull requests work on GitHub.** We’re testing new capabilities internally where [GitHub Copilot will automatically suggest sentences and paragraphs as developers create pull requests](https://githubnext.com/projects/copilot-for-pull-requests/#ghost-text) by dynamically pulling in information about code changes.

We are also preparing a new feature where **[GitHub Copilot will automatically warn developers if they’re missing sufficient testing for a pull request and then suggest potential tests](https://githubnext.com/projects/copilot-for-pull-requests/#gentest)** that can be edited, accepted, or rejected based on a project’s needs.

<https://github.blog/wp-content/uploads/2023/03/03-Copilot-for-PRs-Test-Generation-Blog.mp4#t=0.001>
This complements our efforts with GitHub Copilot Chat where developers can ask GitHub Copilot to generate tests right from their editor—so, in the event a developer may not have sufficient test coverage, GitHub Copilot will alert them once they submit a pull request. It will also help project owners to set policies around testing, while supporting developers to meet these policies.

* **Get AI-generated answers about documentation:** We are launching GitHub Copilot for Docs, an experimental tool that uses a chat interface to provide users with AI-generated responses to questions about documentation—including questions developers have about the languages, frameworks, and technologies they’re using. We’re starting with documentation for [React](https://react.dev), [Azure Docs](https://learn.microsoft.com/en-us/azure/?product=popular), and [MDN](https://developer.mozilla.org/), so we can learn and iterate quickly with the developers and users of these projects.

<https://github.blog/wp-content/uploads/2023/03/04-Copilot-for-Docs-Blog-1.mp4#t=0.001>
[Join the waitlist >](https://githubnext.com/projects/copilot-for-docs)

**We’re also working to bring this functionality to any organization’s repositories and internal documentation**—so any developer can ask questions via a ChatGPT-like interface about documentation, idiomatic code, or in-house software in their organization and get instant answers.

We know that the benefits of a conversational interface are immense, and we are working to enable semantic understanding of the entirety of GitHub across public and private knowledge bases to better personalize GitHub Copilot’s answers for organizations, teams, companies, and individual developers alike based on their codebase and documentation.

Moving forward, we are exploring the best ways to index resources beyond documentation such as issues, pull requests, discussions, and wikis to give developers everything they need to answer technical questions.

Powered by OpenAI’s new GPT-4 model

**Our work to rethink pull requests and documentation is powered by OpenAI’s newly released GPT-4 AI model.** 

 Even though this model was just released, we’re already seeing significant gains in logical reasoning and code generation. [With GPT-4](https://openai.com/product/gpt-4), the state of AI is beginning to catch up with our ambition to create an AI pair programmer that assists with every development task at every point in the developer experience.

 Moreover, it’s helping GitHub Copilot understand more of a developer’s codebase to offer more tailored suggestions in PRs and better summations of documentation.

 
* **Copilot for the command line interface (CLI):** Next to the editor and pull request, the terminal is the place where developers spend the most time. But even the most proficient developers need to scroll through many pages to remember the precise syntax of many commands. This is why we are launching [GitHub Copilot CLI](https://githubnext.com/projects/copilot-cli/). It can compose commands and loops, and throw around obscure find flags to satisfy your query.

[Join the waitlist >](https://githubnext.com/projects/copilot-cli/)

![A demo of GitHub Copilot for CLI.](https://github.blog/wp-content/uploads/2023/03/Copilot-CLI-1.png?w=3024)A demo of GitHub Copilot for CLI.
#### Let’s build from here 🚀

From reading docs to writing code to submitting pull requests and beyond, we’re working to personalize GitHub Copilot for every team, project, and repository it’s used in, creating a radically improved software development lifecycle. Together with [Microsoft’s knowledge model](https://blogs.microsoft.com/blog/2023/03/16/introducing-microsoft-365-copilot-your-copilot-for-work/), we will harness the reservoir of data and insights that exist in every organization, to strengthen the connection between all workers and developers, so every idea can go from code to reality without friction. At the same time, we will continue to innovate and update the heart of GitHub Copilot—the AI pair programmer that started it all.
