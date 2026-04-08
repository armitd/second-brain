# Power BI’s AI Revolution: What’s Here, What’s Next, and How to Leverage It

![rw-book-cover](https://cdn.prod.website-files.com/645b9abe6a218233e4ac7428/67d9b664c9b30b28fb8ff827_Blue%20Fabric.webp)

## Metadata
- Author: [[thevirtualforge.com]]
- Full Title: Power BI’s AI Revolution: What’s Here, What’s Next, and How to Leverage It
- Category: #articles
- Summary: AI is transforming how organizations use Power BI by enhancing data accessibility and efficiency. Features like CoPilot allow users to ask questions in natural language and automate tasks, making data analysis easier for everyone. The future promises even more advancements, including better predictive analytics and modular AI functionalities.
- URL: https://www.thevirtualforge.com/company/blog/power-bis-ai-revolution-whats-here-whats-next-and-how-to-leverage-it

## Full Document
Artificial intelligence (AI) is not just a key aspect of the discussion of how organizations manage business data and workflows, it is THE discussion. Indeed, AI is rapidly transforming the landscape, redefining the ways people create and consume data. When it comes to Power BI, this revolution promises both increased accessibility and efficiency, though unpacking exactly what this means can be difficult given the seemingly daily release of new features.

Let’s unpack that promise, focusing on:

* what an AI-assisted Power BI experience can do right now for end users and developers
* how AI can be leveraged via both internal and external tools
* implementation considerations
* what the future may hold

#### Augmenting the User Experience

Let’s review a few essential ways AI tools are currently re-shaping the Power BI landscape and maximizing the efficiency of analysis for end users and developers:

##### CoPilot for the End User

By leveraging the Natural Language Processing (NLP) capabilities of Large Language Models (LLMs), end users in the business are no longer beholden to analyst availability in order to ask questions of a particular visualization. CoPilot allows the user to simply pose a question in conversational language and let the AI agent do the work, often in mere seconds.

##### Democratization for the Citizen Developer

For several years now, [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi) has enabled the rise of the “citizen developer” through the introduction of no-code and low-code features, enabling users to quickly ingest and visualize data without in-depth technical knowledge. CoPilot accelerates that trend by allowing users to create KPIs and measures and visualize data with nothing more than a few conversational prompts.

##### Task Automation

For seasoned Power BI developers, CoPilot offers a means to increase efficiency, automating time-consuming tasks like DAX documentation and troubleshooting. CoPilot can also assist in tackling complex calculations via prompts, where the desired outcome is known, but the steps to reach that outcome aren’t readily identifiable, effectively eliminating the time spent pouring over documentation.

##### Prediction, Not Description

In traditional business intelligence, analysis was largely focused on understanding what happened and why: reviewing past performance, identifying anomalies, and uncovering root causes. By leveraging Azure Machine Learning (ML) services, organizations can effectively pivot from “what happened?” to “what will happen?”, from describing the past to predicting and planning for future outcomes.

#### Power BI AI Integrations

With an understanding of how AI tools in Power BI serve to enhance both the user and developer experience, let’s take a look at how AI integrates with the platform: through both native and external toolsets:

##### The Power BI Experience - CoPilot and Fabric

[CoPilot](https://copilot.microsoft.com/chats/yR8CqaMnuj8LAF7aX4eGD), an LLM-based AI assistant, was introduced into the Power BI desktop application with the release of Fabric, which offers a slightly different experience depending on where you are in the app. CoPilot is not the only AI integration however, as [Fabric](https://www.microsoft.com/en-us/microsoft-fabric) provides multiple machine learning (ML) capabilities, and Power BI has offered AI-powered visuals for several years. Notable AI integrations within the Power BI ecosystem include the following:

* In the desktop application Report View, CoPilot Q&A functionality supports the interrogation of the data model and specific visuals, as well as visualization generation via natural language queries (though there’s significant overhead to optimize performance).
* CoPilot in the DAX Query View allows developers to use natural language prompts to create measures and add comments to new and existing code.
* From the desktop application Model View, users can generate measure-level descriptions, automating an otherwise time-consuming task.
* For predictive and text-based analytics, Fabric integrates with Azure AI services to leverage pre-built AI models, as well as the ability to build and train custom models via AutoML or MLFlow.
* At the visual level, users can generate text-based analysis using the Narrative visual, or conduct root cause analysis via the Decomposition Tree and Key Influencers visuals.

##### External Tools: VS Code

While Power BI provides a self-contained development environment, developers often utilize external tools for greater flexibility. To this end, [VS Code](https://code.visualstudio.com/docs/copilot/overview), via platform-specific extensions for DAX and tabular data model development, as well as tenant management, leverages GitHub CoPilot at no additional cost to provide code completion and suggestion functionality.

##### External Tools: API Calls

CoPilot functionality does not extend to Power Query (the data ingestion & transformation component) in the desktop application, so in order to carry out complex text classification or sentiment analysis tasks during transformation (particularly if you opt to forgo a Fabric implementation), you pass a prompt via API to an LLM in a query to carry out the task (using methods similar to that described [here](https://youtu.be/gHuARhCDV4A?si=J1Ctdcd09Vbgak9L)).

#### Implementing AI in BI: Considerations

Of course, even after you’ve invested in a Fabric implementation or external AI integration, it isn’t as easy as flipping a switch to get the organization up and running. Let’s next turn to a few of the chief considerations for a successful implementation:

##### Licensing

As of this writing, Microsoft only offers CoPilot at higher Fabric capacities (starting with the F64 SKU, formerly P1), which for a reserved capacity costs just over $5K USD per month. Depending on how closely your organization intends to manage uptime, a pay-as-you-go option may reduce those costs, though overall the pricing for this option can be much higher.

##### Objectives

Since CoPilot for Power BI is only available within the larger Fabric offering, it’s important that your plan for implementation encompasses a larger data strategy with your organization. Without clear objectives that align to business data and insight needs, you run the risk of solutions that are inefficient and features that are unused, wasting both resources and effort. As with any new tool implementation, it’s best to identify high-value, well-defined use cases to tackle, demonstrating ROI and gaining buy-in from stakeholders.

##### Data Quality and Governance

The saying “garbage in, garbage out” as it applies to standard analytics equally applies to the integration of AI. Just as poor data quality can erode user confidence through incorrect and misleading visualizations, CoPilot agent responses can be likewise affected - the agent can only provide responses based on what it has available. It’s therefore critical to cleanse datasets, follow best practices for data modeling, and incorporate the appropriate governance mechanisms to ensure proper monitoring and maintenance.

##### Upskilling

If your organization is new to Fabric and/or Power BI, developer and end user training is critical. Beyond the tools themselves, there is another skill to develop: prompting.

‍  

Similar to data, we can think of prompting as a new form of “garbage in, garbage out” for the AI age. While you can have an exemplary data model, a poorly constructed or naive prompt often leads to responses that are generalized, unsatisfactory, and in some cases, incorrect. Prompting is an art unto itself, and understanding [prompt optimization techniques](https://medium.com/@manas15072002/mastering-the-art-of-prompt-engineering-unveiling-effective-approaches-for-optimizing-results-from-f676508d3861#:~:text=Naive%20prompting%20involves%20presenting%20a,and%20exercise%20for%20stress%20relief.) for both developers and business users alike is indispensable to the success of any AI implementation.

##### Ethical/Responsible Behavior

Data-level permissions with regards to regulatory concerns like GDPR and CCPA (and more if you’re working with sensitive data from the healthcare industry for example) must be considered. Once CoPilot is enabled, for instance, all end user and developer-facing elements are enabled - you can’t pick and choose. Accordingly, your underlying models should be constructed in such a way that the LLM agent does not expose private or otherwise sensitive information to the wrong audience, and the guardrails in place to prevent divulging this information should be transparent and easily explainable to your users.

##### Performance Monitoring

Performance monitoring requirements are a two-fold consideration. You need to first be sure that the performance isn’t adversely affected by requests submitted via CoPilot. In Power BI. processing for natural language queries consumes capacity bandwidth, and given enough volume, this has the potential to be disruptive to the overall system performance. Second, you need to monitor the agent’s response quality with the aim of ensuring that there is no significant variance in the quality of a response to the same question over time, particularly as new data is introduced into the model.

##### LLM Costs

Even if you’re not considering Fabric/CoPilot for your organization, and plan to leverage LLM API calls as part of your data preparation process, it’s important to to understand costs related to token consumption, as these can build up quickly. For instance, suppose you’re using an LLM for sentiment analysis in your dataset. While it may only cost $0.01 per API call, imagine that the table has 100K rows and refreshes eight times per day.

#### What Does the Future Hold in Store?

Let’s turn to the future with a bit of a caveat: Given that AI advances on an exponential curve, it’s difficult to definitively predict how AI will impact Power BI, Fabric, and related toolsets next year, let alone five years from now. We are already seeing possible changes in language generation via [Large Language Diffusion Models (LLaDA)](https://towardsdatascience.com/llada-the-diffusion-model-that-could-redefine-language-generation/) that could have a significant impact on the next generation of agent-assisted BI.

That caveat notwithstanding, based on current gaps and trends:

1. CoPilot-assisted technologies in Power BI will extend to the Power Query desktop experience, automating data preparation and cleansing, and generating reporting models without the need for human oversight
2. CoPilot will increase contextual awareness, and be able to deliver recommendations that account for business goals, its market conditions, and the general industry.
3. Azure ML toolsets will focus on predictive analytics in real time, generating immediate insights without the need for supervised training or processing in downstream systems.
4. As AI drives more and more business decisions, Power BI will increase transparency for the reasoning behind agent-generated insights (an early form of this is already available in response to visual-level prompts).
5. As demand for CoPilot services increases, it’s possible that Microsoft follows the Power BI Premium-Per-User licensing model and offers at least some AI-backed functionality at a lower price point.
6. CoPilot deployment may become more modular, allowing users to selectively enable only the experiences appropriate to their organization.
7. Likewise, Fabric itself may become more modular, priced based on the features you need rather than offering the full complement of services, some of which may never be used by an organization.

#### Conclusion

The world of AI and its impact on the Power BI ecosystem is evolving rapidly, and it can be difficult to sift through what feels like equally ever-advancing features and opinions (indeed, there’s a non-zero chance that some of the things noted here will change by the time you read this). My hope is that this discussion has shed some light on how an AI-assisted Power BI implementation (with or without Fabric) can benefit your organization, what you need to consider, and where it may be headed. To be sure, there are many unknowns with respect to the AI-assisted experience, though I think we can also see that it holds a great deal of promise for increasing the accessibility and efficiency of unlocking business insights.

#### How The Virtual Forge Can Help

As Artificial Intelligence continues to reshape the data visualization landscape, you can stay up to date on developments with the help of [The Virtual Forge](https://www.thevirtualforge.com/). Our team of experts can help you transition your business into newer ways of working in this rapidly changing environment, including learning how to more effectively and efficiently visualize your data via Power BI.

The sooner you are able to leverage these new capabilities to understand the data at hand, the sooner you can make better-informed decisions on performance KPIs and gauge business-wide progress. Contact us today to learn more about our [data visualization services](https://www.thevirtualforge.com/services/ai-and-data/data-visualisation)!

‍
