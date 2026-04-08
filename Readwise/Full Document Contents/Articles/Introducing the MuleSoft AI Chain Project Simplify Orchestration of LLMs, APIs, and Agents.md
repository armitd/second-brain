# Introducing the MuleSoft AI Chain Project: Simplify Orchestration of LLMs, APIs, and Agents

![rw-book-cover](https://blogs.mulesoft.com/wp-content/uploads/ai-chain-proj.png)

## Metadata
- Author: [[https://blogs.mulesoft.com/author/astonwhiteling/]]
- Full Title: Introducing the MuleSoft AI Chain Project: Simplify Orchestration of LLMs, APIs, and Agents
- Category: #articles
- Summary: The MuleSoft AI Chain project aims to simplify the integration and management of various AI tools, APIs, and agents to prevent AI sprawl. It offers connectors that allow developers to easily build and deploy AI applications using existing MuleSoft APIs, enhancing collaboration across different AI models. This project empowers users to innovate securely and efficiently while maintaining control over costs and data.
- URL: https://blogs.mulesoft.com/news/mulesoft-ai-chain-project/

## Full Document
[![Aston Whiteling profile image](https://blogs.mulesoft.com/wp-content/uploads/aston-150x150.jpeg)](https://blogs.mulesoft.com/author/astonwhiteling/)
Reading Time: 10 minutes

There’s a concept in API Management referred to as [API sprawl](https://blogs.mulesoft.com/learn-apis/api-sprawl/). This term was coined to describe an uncontrolled proliferation of APIs across an organization.

If you onboard and ramp APIs without considering the processes they’re connected to, how you want them to work together, or your intention for them as they grow, you can dig yourself into a technically complex hole – one that isn’t easy to climb out of.

As the number of apps and microservices continues to expand as businesses mature into their journey of digital transformation, being able to centrally discover, design, and govern any API is paramount.

This is a problem that MuleSoft knows well and that is heavily invested in solving. As the functionality of AI tools continuously expands, we’re beginning to see the creeping signs of **AI sprawl**.

Although there are still plenty of monolithic players in the space, the market is shifting towards a more decentralized model; businesses want to adopt multiple, boutique LLMs and Agents that are focused on a specific use case or function.

Jumping from LLM to LLM isn’t an experience anyone is particularly interested in though. Natural language being the input method lends itself to the widespread belief that there should be one I/O to rule them all. So how do you effectively orchestrate these models into a unified experience, while ensuring each one has a common set of functionalities that drive the most desirable output, no matter the prompt?

**Author note:** if you encounter an AI term you’re unfamiliar with in this article, you can refer to [Salesforce’s GenAI glossary of terms](https://help.salesforce.com/s/articleView?id=sf.generative_ai_glossary.htm&type=5).

#### What is the MuleSoft AI Chain project?

Many organizations are seeing signs of AI sprawl; there’s a lot of experimenting happening which makes it hard to secure data and manage the cost of GenAI interactions.

The [MuleSoft AI Chain](https://mac-project.ai/) project aims to address this challenge for MuleSoft users, while simultaneously making it easy to extend your copilots and agents with your existing MuleSoft APIs.

It offers a suite of connectors designed for MuleSoft developers, enabling seamless interaction with LLMs, vector databases, APIs, and token management. With these connectors, customers can implement a wide range of AI use cases, including RAG for both online and offline scenarios, agentic workflows, and knowledge bases. The project supports the entire agent lifecycle – from building and configuring to deploying agents – allowing users to route and orchestrate across LLMs for optimized capability, cost efficiency, and privacy controls, while also integrating their own data context.

![MuleSoft AI Chain Project](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfCGTkAt9lYib_WNR2JO5-BAP26Tmj0sJvpKYEXqV7EbKY8UvUq-jlsPKik-1qpjvrr6563W6fk2CUwduDNacQdf5T973MQ25wYijPUkzgbSO8S0w0i3qdNz0p-n_tfKa4ILiMnWJnkAWCV0PW3CIBu2-g?key=KvUKrGMRrTrpx5IgPz4EHQ)
The project is based on an open-source framework called [LangChain4j](https://docs.langchain4j.dev/), which aims to simplify the process of building LLM-driven applications, such as chatbots, virtual agents, and summarization services. While LangChain4j has been incredibly important in driving the adoption of LLMs and creating new innovative AI-application architectures, it does require users to take a code-heavy approach to development. This inhibits many organizations from taking advantage of its capabilities and slows the adoption of AI-based applications and services.

The initial concept of MuleSoft AI Chain is to further simplify the approach LangChain4j has taken by bringing the power of this framework into MuleSoft’s low code integration tools. By building directly within MuleSoft, developers can easily expose their existing MuleSoft APIs to any agent or copilot created using MuleSoft AI Chain.

This approach allows users to fully leverage the power of the Anypoint Platform – from design to deployment – while ensuring robust security for agents and workflows. These copilots and agents can seamlessly operate across LLMs or vector stores, offering advanced capabilities such as dynamic prompt templates, image generation, complex model chain linking, input classification, and more.

Our goal is to provide users with a unified and trusted environment to experiment with LLMs and APIs while enforcing a lifecycle framework that helps prevent AI sprawl from the start. With comprehensive security, governance, and monitoring features, MuleSoft AI Chain empowers developers to innovate confidently and securely.

#### MuleSoft AI Chain project structure

The MuleSoft AI Chain project consists of several different connectors:

* **MuleSoft AI Chain Connector:** Connector that can be used to build agents (in a similar experience as LangChain4j) and provide a unification layer for LLM and Vector Store (in-memory) AI services.
* **Einstein AI:** Connector that leverages the [Einstein Trust Layer](https://www.salesforce.com/artificial-intelligence/trusted-ai/) to interact with the models that are available on the Salesforce platform.
* **Amazon Bedrock:** Connector for [Amazon Bedrock](https://aws.amazon.com/bedrock/?gclid=CjwKCAjw59q2BhBOEiwAKc0ijSU3hJPWddvGCO7mR-qz9rYFRsu9mvY6lsp75QSNuW3XEWBxrDJpaRoChSAQAvD_BwE&trk=0eaabb80-ee46-4e73-94ae-368ffb759b62&sc_channel=ps&ef_id=CjwKCAjw59q2BhBOEiwAKc0ijSU3hJPWddvGCO7mR-qz9rYFRsu9mvY6lsp75QSNuW3XEWBxrDJpaRoChSAQAvD_BwE:G:s&s_kwcid=AL!4422!3!692006004682!e!!g!!aws%20bedrock!21048268554!159639952735) to design, build, and manage Amazon Bedrock agent workflows, LLM interactions, knowledge bases, and RAG.
* **Vectors:** Connector for external embedding models and vector databases, i.e. Milvus, Chroma, Pinecone, Elastic, Nomic, OpenAI, etc.
* **Whisperer:** Connector to support Speech-to-Text and Text-to-Speech use cases in combination with the other MuleSoft AI Chain Connectors

Combining a unified API plane with this set of tools makes it simple for MuleSoft users to quickly build complex copilots that can extend across a range of LLMs, while taking advantage of any existing APIs available within MuleSoft.

##### What’s next?

MuleSoft AI Chain empowers our customers to accelerate the time-to-value of their AI investments with low-code MuleSoft development, seamless omnichannel connections to any LLM in use today, and a comprehensive suite of management tools. These tools help control costs, maintain system health, and ensure security, effectively preventing AI sprawl before it starts.

To make the open source project more accessible to MuleSoft customers, we plan to offer certified versions of the connectors on Anypoint Exchange, with the first release expected by the end of 2024. To stay up to date with the latest updates on MuleSoft AI Chain or contribute to its growth, join our [community on LinkedIn](https://www.linkedin.com/showcase/mulesoftcommunity/posts/?feedView=all) and learn more about the project on the [website](https://mac-project.ai/) or our [YouTube channel](https://www.youtube.com/@MuleSoft-MAC-Project).

**Editor’s note:** *This article was written in collaboration between Aston Whiteling and Rohan Vettiankal.*
