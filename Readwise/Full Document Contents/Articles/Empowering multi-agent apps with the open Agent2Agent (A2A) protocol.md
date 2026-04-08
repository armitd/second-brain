# Empowering multi-agent apps with the open Agent2Agent (A2A) protocol

![rw-book-cover](https://www.microsoft.com/en-us/microsoft-cloud/blog/wp-content/uploads/2025/04/Cloud_Blog_Abstract-12.jpg)

## Metadata
- Author: [[Yina Arenas]]
- Full Title: Empowering multi-agent apps with the open Agent2Agent (A2A) protocol
- Category: #articles
- Summary: Microsoft is advancing the Agent2Agent (A2A) protocol to enable AI agents to collaborate across different platforms and clouds. This open approach allows developers to build complex systems that maintain control and trust while using familiar tools. The upcoming A2A features aim to create a future where intelligent agents work together seamlessly, enhancing enterprise software capabilities.
- URL: https://www.microsoft.com/en-us/microsoft-cloud/blog/2025/05/07/empowering-multi-agent-apps-with-the-open-agent2agent-a2a-protocol/

## Full Document
Over the past year, we’ve seen AI agents evolve from experimental tools to essential components of enterprise systems. From simple prompt and response bots to agents that act autonomously on your behalf, this shift marks a new era of software design where intelligence is no longer tied to static interfaces or single applications.

At Microsoft, we’ve seen this transformation firsthand. [**Azure AI Foundry**](https://ai.azure.com/) is now used by developers at more than 70,000 enterprises and digital native companies, including Atomicwork, Epic, Fujitsu, Gainsight, H&R Block, and LG Electronics, to design, customize, and manage AI apps and agents. In just four months, over 10,000 organizations have adopted our new Agent Service to build, deploy, and scale agentic systems. More than 230,000 organizations, including 90% of the Fortune 500, have already used [**Microsoft** **Copilot Studio**](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio).

As agents take on more sophisticated roles, they need access not only to diverse models and tools but also to one another. That is why we are committed to advancing open protocols like [Agent2Agent (A2A)](https://github.com/google/A2A), coming soon to Azure AI Foundry and Copilot Studio, which will enable agents to collaborate across clouds, platforms, and organizational boundaries.

Some content could not be imported from the original document. [View content ↗](https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7325882270177710083?compact=1) 

We’re aligning with the broader industry push for shared agent protocols—doing what we’ve always done: embracing openness, supporting real-world developers, and turning experimentation into enterprise-grade platforms. Our goal is simple: empower both pro and citizen developers to build agents that interoperate across clouds and frameworks.

We believe that Microsoft Copilot will empower every employee and act as the “UI for AI” to connect with agents and agentic systems—networks of agents that reason, act, and adapt across boundaries. As customers scale these systems, **interoperability is no longer optional**. They want their agents to orchestrate tasks that span vendors, clouds, and data silos. They want control, visibility, and trust—without being locked in.

A2A can enable structured agent communication—exchanging goals, managing state, invoking actions, and returning results securely and observably. Developers can use tools they know, like Semantic Kernel or LangChain, and still interoperate. Every call travels through enterprise-grade safeguards: Microsoft Entra, mutual TLS, Azure AI Content Safety, and full audit logs. Azure AI Foundry is built with trust by default, and as agent ecosystems grow more open and distributed, safety, compliance, and accountability remain first-class.

#### What we are delivering

With support for A2A:

* **Azure AI Foundry** customers can build complex, multi-agent workflows that span internal copilots, partner tools, and production infrastructure—while maintaining governance and SLAs.
* **Copilot Studio** agents will be able to securely invoke external agents, including those built with other platforms or hosted outside Microsoft.
* Enterprises gain a path to composable, intelligent systems that scale across organizational and cloud boundaries.
* Microsoft’s contributions will accelerate development and adoption of the open A2A protocol across the industry.

This is just one step on a longer journey. As we’ve done with innovations like Autogen, Semantic Kernel, our contributions to Model Context Protocol (MCP), and our catalog of open models, we will continue to evolve the platform to support **the protocols, models, and frameworks that matter most to developers and enterprises**. We see protocols like A2A and MCP as important steps in the direction of realizing our vision for the agentic future.

#### What’s next

Agentic computing isn’t a trend—it’s a foundational shift. It changes how software is built, how decisions are made, and how value is created.

We have joined the A2A working group on GitHub to contribute to the spec and tooling. The A2A public preview in Foundry and Copilot Studio will arrive soon.

By supporting A2A and building on our open orchestration platform, we’re laying the foundation for the next generation of software—collaborative, observable, and adaptive by design. The best agents won’t live in one app or cloud; they’ll operate in the flow of work, spanning models, domains, and ecosystems. We’re building that future with openness at the center—because agents shouldn’t be islands, and intelligence should work across boundaries, just like the world it serves.

#### Getting started

We’ve introduced a [new sample in Semantic Kernel](https://devblogs.microsoft.com/foundry/semantic-kernel-a2a-integration/) (available in Python) that demonstrates how two local agents can collaborate using the A2A protocol. In this example, the agents work together to plan a travel itinerary and handle currency conversions, showcasing seamless interoperability without the need for custom orchestration code.

#### Resources
