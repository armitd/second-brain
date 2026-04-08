# The Ontology issue: From knowledge to graphs and back again. The Year of the Graph Newsletter Vol. 29, Winter 2025 – 2026

![rw-book-cover](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/charlesdeluvio-OWkXt1ikC5g-unsplash.jpg)

## Metadata
- Author: [[ganadiotis]]
- Full Title: The Ontology issue: From knowledge to graphs and back again. The Year of the Graph Newsletter Vol. 29, Winter 2025 – 2026
- Category: #articles
- Summary: Ontologies give AI and people a shared semantic framework that turns raw data into meaningful entities and relationships. Knowledge graphs use those ontologies to improve trust, explainability, and reasoning for AI and enterprise systems. Organizations should learn and adopt ontology-driven knowledge graphs to build reliable, scalable, and grounded AI.
- URL: https://yearofthegraph.xyz/newsletter/2025/12/the-ontology-issue-from-knowledge-to-graphs-and-back-again-the-year-of-the-graph-newsletter-vol-29-winter-2025-2026/

## Full Document
![The Ontology issue: From knowledge to graphs and back again. The Year of the Graph Newsletter Vol. 29, Winter 2025 – 2026](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/charlesdeluvio-OWkXt1ikC5g-unsplash.jpg)
**Enterprise and data architects, data modelers, GenAI adopters, analysts, thought leaders, Graph RAG application builders, Microsoft, Palantir – everyone is talking about ontologies. Why, what is an ontology actually, and how is it related to graphs?**

An ontology is an explicit specification of a conceptualization which is, in turn, the objects, concepts, and other entities that are presumed to exist in some area of interest and the relationships that hold among them.

Ontology introduces the semantic foundation that connects people, processes, systems, actions, rules and data into a unified ontology [sic]. By binding real-world data to these ontologies, raw tables and events are elevated into rich business entities and relationships, giving people and AI a higher-level, structured view of the business to think, reason, and act with confidence.

The first paragraph is taken from the [entry for Ontology in the Encyclopedia of Database Systems](https://tomgruber.org/writing/definition-of-ontology.pdf), written by Tom Gruber in 2009. Gruber is credited with the most widely cited definition of ontology in the context of computer and information sciences, introduced circa 1993.

The second paragraph is taken from the [blog post introducing Fabric IQ, a new semantic foundation within Microsoft Fabric](https://blog.fabric.microsoft.com/en-us/blog/introducing-fabric-iq-the-semantic-foundation-for-enterprise-ai?ft=All). It was written by Chafia Aouissi in November 2025. Aouissi is Sr. Director Product Management Fabric IQ at Microsoft.

As usually happens when terms become part of the mainstream discourse, there is a certain tension between rigor and adoption. Case in point – not just Microsoft Fabric IQ, but also Palantir.

Palantir has been floating the term “ontology” as the cornerstone of its architecture for a while. While this has [helped popularize the term, as Juan Sequeda notes](https://www.linkedin.com/feed/update/urn:li:activity:7389287692645253120/), at the same time it has also ignited confusion as to what ontology really is.

When Palantir’s CEO, Alex Karp, lashed out at Michael Burry – “Big Short” investor who bet against Palantir and Nvidia – he wasn’t just defending his balance sheet, but also an idea. In Karp’s words, ontology now sits beside chips as the engine of AI. But if we take ontology seriously, Burry’s short might not be wrong, [J Bittner notes](https://www.linkedin.com/pulse/shorting-ontology-why-michael-burry-might-wrong-j-bittner-cvfte/).

In this issue of the Year of the Graph, we identify ontology and knowledge graph definitions, applications, tools, and educational resources.

**This issue of the Year of the Graph is brought to you by [metaphacts](https://blog.metaphacts.com/neuro-symbolic-ai-the-key-to-truly-intelligent-systems?mtm_campaign=Year%20of%20the%20graph%20newsletter&mtm_kwd=Dec-2025-Neurosymbolic-AI-blog), [Process Tempo](https://calendly.com/processtempo/yotg), [Linkurious](https://eu1.hubs.ly/H0qhxmM0), [RDFox](https://www.oxfordsemantic.tech/free-trial?YOTG25), [Tentris](https://linkly.link/2Tc9K), [Connected Data London,](https://2025.connected-data.london) [State of the Graph](https://www.stateofthegraph.com) and [Pragmatic AI Training](http://pragmaticai.training).**

If you want to be featured in an upcoming issue and support this work, [reach out](https://yearofthegraph.xyz/contact/)!

**Neuro-symbolic AI: The key to truly intelligent systems**

[![](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/YoG-neurosymbolic-ai.png)](https://blog.metaphacts.com/neuro-symbolic-ai-the-key-to-truly-intelligent-systems?mtm_campaign=Year%20of%20the%20graph%20newsletter&mtm_kwd=Dec-2025-Neurosymbolic-AI-blog)
Just as you wouldn’t bring half your brain to work, enterprises shouldn’t bring half of artificial intelligence’s capabilities to their architectures. Neuro-symbolic AI combines neural-network technology like LLMs with symbolic technology like knowledge graphs. This integration, also known as ‘knowledge-driven AI’, delivers significant advantages:  

 ● Trustworthy & explainable insights grounded in explicit facts  

 ● Reliable & transparent AI agents  

 ● Grounded LLMs that can assist in complex modeling

If you’re not exploring how knowledge graphs and symbolic AI can augment your  

 organization’s intelligence—both artificial and actual—now is a good time to start.

[Read the full article.](https://blog.metaphacts.com/neuro-symbolic-ai-the-key-to-truly-intelligent-systems?mtm_campaign=Year%20of%20the%20graph%20newsletter&mtm_kwd=Dec-2025-Neurosymbolic-AI-blog)

#### **The “O” word**

If you talk to people working with data, AI, or enterprise architecture and ask, “what is an ontology?”, you’ll get different answers. For some, ontology is a kind of clever data schema. For others, it’s a business glossary. For others still, the heart of a knowledge graph. They’re all right, and that’s the problem as per Juha-Pekka Joutsenlahti.

In “[Demystifying ontologies](https://www.linkedin.com/pulse/demystifying-ontologies-what-really-do-knowledge-joutsenlahti-wyraf/)“, Joutsenlahti gives a brief history of the concept of ontologies in IT and knowledge representation. He explains that different communities adopted “ontology” and bent it slightly towards their own needs, resulting in confusion.

The key to reducing the confusion is to always ask: What is this ontology for? Is it meant to clarify meaning or to define data structure (or both)? Once we make that distinction explicit, much of the mystery starts to disappear.

“[The O word: do you really need an ontology?](https://yearofthegraph.xyz/newsletter/2019/11/the-o-word-do-you-really-need-an-ontology-the-year-of-the-graph-newsletter-november-october-2019/)” was published in 2019. Before GenAI was a thing, Mark Hall made a compelling case for ontologies and offered an explanation as to why isn’t everyone doing this.

Today, as Ole Olesen-Bagneux [notes](https://www.linkedin.com/posts/ole-olesen-bagneux_ontology-knowledgeengineering-ai-activity-7401910226066591744-_Vg7/), ontologies are once again hot because they are key to succeeding with AI: ontologies provide context for AI to perform better. Thus, we are seeing the re-introduction of knowledge engineering as if it were new.

![](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/DataModelsOntologiesConnectBuildSemanticFoundations.webp)How Data Models and Ontologies Connect to Build Semantic Foundations
Knowledge Management and the Library Sciences, from which taxonomies, ontologies, and knowledge graphs were born, are well-established disciplines, as Juha Korpela notes in “[How Data Models and Ontologies Connect to Build Your Semantic Foundations](https://moderndata101.substack.com/p/semantic-foundations-with-data-models-or-ontology)“.

Korpela points out that people who have traditionally worked with ontologies and knowledge graphs have not been communicating much with domains such as data modeling, but the exchange would be meaningful.

Data modelers focus on the technical implementation of data solutions, thus following a path from Conceptual to Logical to Physical modeling. Even if concept models and ontologies are different, as Jessica Talisman [notes](https://jessicatalisman.substack.com/p/concept-models-and-ontologies), there is overlap. Conceptual modeling may be used to build an ontological foundation that acts as the context provider for agents and chatbots as well as humans.

**Bring your graph ideas to life!**

Building a knowledge graph? You’re going to want people to use it. We can help!

[![](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/ProcessTempoYearOfTheGraph.png)](https://calendly.com/processtempo/yotg)
Process Tempo Jupiter makes it easy to build beautiful, production-ready applications on top of your graph without writing code. Now you can bring your graph ideas to life using skills you already have.

Jupiter supports multi-modal, read and write, between graph databases, relational databases and Rest-based APIs. No ETL required!

✅Neo4j, ✅Memgraph, ✅PuppyGraph, ✅OpenCypher

✅Databricks, ✅Snowflake, ✅Big Query, ✅MySQL, ✅Postgres, ✅ Dremio

Ready to get started? Get on our calendar to learn more: [calendly.com/processtempo](https://calendly.com/processtempo/yotg)

#### **From knowledge to graphs and back again**

Another term that is overloaded, being used in different contexts to mean different things, is “knowledge graph”. For an elaboration of the definition of a knowledge graph, the connection to ontology, and how they become [the essential truth layer for Pragmatic AI](https://linkeddataorchestration.com/2025/03/11/knowledge-graphs-as-the-essential-truth-layer-for-pragmatic-ai/), check this conversation between Tony Seale and George Anadiotis.

Taewoon Kim has a go at [defining knowledge graphs and offering a practical guide of the different options for implementing them](https://www.linkedin.com/feed/update/urn:li:activity:7381637511820939264). Nicolas Figay summarizes the [insights from different viewpoints on what a knowledge graph really is](https://www.linkedin.com/pulse/what-knowledge-graph-really-insights-from-great-debate-nicolas-figay-o17te).

Like ontologies, what has largely contributed both to popularizing and creating confusion around knowledge graphs is their use for GenAI, specifically to support LLMs in Graph RAG. As Fanghua (Joshua) Yu notes, even when talking about [knowledge graphs in Graph RAG use cases](https://www.linkedin.com/feed/update/urn:li:activity:7402600988752216064), there are different KG types to consider.

[![](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/KnowledgeGraphsGenAIComplexity.jpg)](https://www.linkedin.com/feed/update/urn:li:activity:7379463421693411329)Knowledge Graphs and GenAI: When the Complexity Is Worth It
But is using knowledge graphs with GenAI always a good idea? The [complexity may not always be worth it](https://www.linkedin.com/feed/update/urn:li:activity:7379463421693411329), Dave Bechberger argues. You [may not always need Graph RAG](https://www.linkedin.com/feed/update/urn:li:activity:7383388152591372290). While graph-based enhancements improve information organization & reasoning, they also come with a heavy token cost.

[Graph RAG is a data engineering challenge, not just an LLM trick](https://www.linkedin.com/feed/update/urn:li:activity:7396085260981022720), Fanghua (Joshua) Yu notes. Plus, [Graph RAG does not always outperform “vanilla” RAG](https://www.linkedin.com/feed/update/urn:li:activity:7385918160924987393). If you are going to be using Graph RAG, however, there are some useful frameworks, applications and analyses to consider.

[Flexible GraphRAG](https://www.linkedin.com/feed/update/urn:li:activity:7379767403146035202) and [ApeRAG](https://github.com/apecloud/ApeRAG) are configurable open source frameworks for Graph RAG. Niklas Emegård built an [open source semantic Graph RAG application that can be used as a template for projects](https://www.linkedin.com/feed/update/urn:li:activity:7390898141820092416/). Sergey Vasiliev explores [how graph data science and analytics can help power Graph RAG applications](https://substack.com/home/post/p-175002266). And Benito Martin shares how he built [a Biomedical GraphRAG system, combining knowledge graphs with vector search](https://www.linkedin.com/feed/update/urn:li:activity:7401157719262629888).

**The shortest path between you and graph insights**

Graph visualization and analytics just got a lot easier!  

 Introducing [Linkurious Enterprise Cloud](https://eu1.hubs.ly/H0qhyQV0): An online solution that brings powerful graph exploration to anyone, right from a browser.

[![](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/LinkuriousEnterpriseCloud.jpg)](https://eu1.hubs.ly/H0qhxmM0)Create an account, connect your graph database, start the exploration of your data, collaborate with your teammates and share your results, all before lunch.
What else?  

 • Compatibility with leading graph databases  

 • Zero IT bottlenecks or infrastructure tasks  

 • Flexible plans that adapt to your needs

The fastest way to start a graph project today — and the easiest way to scale it tomorrow.

[Sign up now](https://eu1.hubs.ly/H0qhxmM0) for a 30-day free trial.

#### **Knowledge graph applications at scale**

Today, knowledge graph applications in production are scaling up. [Walmart uses its People.AI knowledge graph to power recommendation tools](https://www.linkedin.com/feed/update/urn:li:activity:7384165584726298624). This knowledge graph includes 1.6 million nodes and 83 million edges, representing entities such as job titles, openings, associates, applicants, and skills.

[Barclays is scaling knowledge graphs and knowledge-based AI in the financial crime and KYC domain](https://2025.connected-data.london/talks/scaling-knowledge-graphs-kyc/). They are using semantic reasoning to automatically enrich knowledge graphs with new facts based on expert knowledge to deliver improved operational efficiency, reduce compliance risk and improve customer experience.

GitLab is building what they call the [GitLab Knowledge Graph](https://www.linkedin.com/feed/update/urn:li:activity:7372211125221953536). It’s a framework written in Rust to turn your codebase into a live, embeddable graph database that can be used for code retrieval and navigation, impact analysis and architecture visualization.

[![RTVE-Grafo: The knowledge graph of the Spanish audiovisual archive](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/RTVE-Grafo.webp)](https://fiatifta.org/awards/)RTVE-Grafo: The knowledge graph of the Spanish audiovisual archive
RTVE, the Spanish national radio and television public broadcaster, has created [a knowledge graph that structures information by understanding the relationships among various audiovisual content as well as any potentially linked objects](https://www.rtve.es/grafo/en#knowledge-graph). It unifies data, making it accessible and comprehensible for both machines and people.

Wiz, the cybersecurity phenomenon recently acquired by Google for $32 billion, has redefined cloud security by providing comprehensive visibility across multi-cloud environments. Their success is based on a [massive, a constantly evolving security graph that spans customers’ entire cloud footprints](https://2025.connected-data.london/talks/how-wiz-became-the-most-valuable-security-startup-with-amazon-neptune).

[Microsoft introduced the Sentinel graph](https://www.linkedin.com/feed/update/urn:li:activity:7379100781322514433/) to bring relationship-aware context to Microsoft Security across Defender and Purview. This way defenders and AI can see connections, understand the impact of a potential compromise, and act faster across pre-breach and post-breach scenarios.

[Graph-Wide scanning is a technique for solving advanced cyber threats](https://www.linkedin.com/feed/update/urn:li:activity:7378736629894524928). In one example, a query on a 150 billion-edge graph scanned a mind-boggling 123 trillion edges. It took time, but it found fewer than 4,000 answers, highlighting the power of finding the critical few from the overwhelming many.

#### **Ontology and knowledge graph insights, tools and education**

A key finding of the [State of the Graph survey for 2025](https://www.linkedin.com/feed/update/urn:li:activity:7402384429488345089) is that knowledge graphs and graph databases are driving adoption, but guidance and training are still critical. Here are some pointers to knowledge graph and ontology educational resources.

[Connected Data London 2025](https://2025.connected-data.london/) was a gathering of top minds and practitioners in this space, featuring use cases, innovation and educational content from the likes of Airbus, AstraZeneca, AWS, Barclays, Bloomberg, Netflix, Nvidia, SAP, ServiceNow, S&P, Vodafone and more. You can [follow CDL](https://uk.linkedin.com/company/connecteddataworld) for [trip reports](https://www.linkedin.com/feed/update/urn:li:activity:7402247397042536448) and [teasers](https://www.youtube.com/shorts/wS7ASgBpEBo), or [dive into the content with a Remote Access Ticket and a special 15% discount](https://2025.connected-data.london/checkout/select-tickets/?coupon=YOTGCDL2515).

metaphacts recently published their [Semantic Modeling Guidelines for Knowledge Engineers](http://bit.ly/47uVMIC). These semantic modeling guidelines are designed for beginners as well as advanced modelers, offering a step-by-step introduction to semantic modeling concepts, key elements and practical techniques.

Kurt Cagle shares [tips for building knowledge graphs](https://www.linkedin.com/feed/update/urn:li:activity:7396787051158732800), noting that the hard part of building a knowledge graph is not the technical aspects, but identifying the types of things that are connected, acquiring good sources for them, and figuring out how they relate to one another.

It is better to create your own knowledge graph ontology, possibly building on existing upper ontologies, than it is to try to shoehorn your knowledge graph into an ontology that wasn’t designed with your needs in mind.

[![Becoming an Ontologist](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/BecomingAnOntologist.jpeg)](https://www.linkedin.com/feed/update/urn:li:activity:7380912735003422721)Becoming an Ontologist
In “[Becoming an Ontologist](https://www.linkedin.com/feed/update/urn:li:activity:7380912735003422721)“, Cagle notes there is a surge in interest in the profession of ontologist. Some of it can be attributed to the fact that people are beginning to realize the value of knowledge graphs, but there is also the opportunistic element here. Like many other fields in the past, ontology work is seen as a ticket to big money. But perceptions and reality are not necessarily aligned.

Dean Allemang shares his [insights on a day in the life of a working ontologist](https://medium.com/@dallemang/a-day-in-the-life-of-a-working-ontologist-5ecc72b22421). Building ontologies is actually the last thing on the list, as there isn’t much spent on that compared to other tasks. Allemang notes that “ontologist” is going to be a much more sought after skill in the near future.

Check also these [tools for visualizing, editing and creating ontologies](https://www.linkedin.com/feed/update/urn:li:activity:7403759799978438657) and [conceptual modeling and Linked Data](https://www.linkedin.com/feed/update/urn:li:activity:7406236067789508608). Robert Sanderson shared his [10 design principles for knowledge graphs and ontology](https://www.linkedin.com/feed/update/urn:li:activity:7396344543891177472/), and Giancarlo Guizzardi shared [a tutorial on the Unified Foundational Ontology](https://www.linkedin.com/feed/update/urn:li:activity:7383449448099758081). And the AIOTI published a [report on the different Data to Ontology mapping tools available](https://www.linkedin.com/feed/update/urn:li:activity:7388898601726377984).

For more in-depth education:

* [Pragmatic AI Training](http://pragmaticai.training): A holistic AI education program, including modules on knowledge graphs, Graph RAG and ontology design
* The [Knowledge Graph Academy](https://www.knowledge-graph-guys.com/academy): learn how to build and scale knowledge graphs through a unique program led by global experts

**Do you need a graph technology that scales without sacrificing performance?**

[![](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/RDFoxCDL2025Advert-1.png)](https://www.oxfordsemantic.tech/free-trial?YOTG25)
RDFox® is one of the most advanced RDF triple stores on the market. Built on world-leading research from the University of Oxford, RDFox® stands out through:

● Highly performant, scalable in-memory architecture  

 ● Advanced rule-based reasoning for dynamic graph enrichment  

 ● An optimised memory footprint for on device, server, or cloud

RDFox® is trusted by a growing list of the world’s largest brands across financial services, manufacturing, automotive, retail, and big tech.

[Powering what is possibly the world’s largest graph deployment across tens of millions of Samsung smartphones – see what all the fuss is about here](https://www.oxfordsemantic.tech/free-trial?YOTG25).

#### **Two meanings of “Semantic Layer” and why both matter for AI**

Another concept [everyone is talking about, but not necessarily meaning the same thing, is semantic layers](https://www.linkedin.com/feed/update/urn:li:activity:7389262743293427712). On the analytics side, [semantic layer usually refers to something we’ve seen before](https://www.linkedin.com/pulse/why-semantic-layers-suddenly-sexy-cindi-howson-z1pie/). It’s the business-friendly model that sits between raw data and BI tools. A governed way to define joins, metrics, and consistent logic.

This version of semantics is about trust. It makes sure when someone (or something) asks, “What’s our total revenue last month?” the answer is accurate, governed, and consistent.

Case in point: the [Open Semantic Interchange (OSI)](https://venturebeat.com/ai/the-usd1-trillion-ai-problem-why-snowflake-tableau-and-blackrock-are-giving). Snowflake, Salesforce, dbt Labs and other vendors announced they are working on what they claim will be a universal standard for how business data is defined and shared across platforms.

[![Semantic Layers and GraphRAG are essential for Trustworthy AI](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/SemanticLayersGraphRAGEssentialTrustworthyAI.jpeg)](https://www.linkedin.com/feed/update/urn:li:activity:7388537977053810688)Semantic Layers and GraphRAG are essential for Trustworthy AI
But there’s another camp using the same phrase and they’ve been doing it far longer. For ontologists, RDF, OWL and JSON-LD are open standards for exchanging semantic data. To them, a semantic layer isn’t a metrics model, it’s a knowledge model. It’s about representing meaning, relationships, and context across systems.

This version of semantics is about understanding. It connects definitions and relationships, providing the context AI uses to make sense of information.

Case in point: [Semantic Layers and GraphRAG are essential for Trustworthy AI](https://www.linkedin.com/feed/update/urn:li:activity:7388537977053810688), Andreas Blumauer points out. [Agents need a semantic layer](https://www.linkedin.com/posts/anthony-alcaraz-b80763155_your-agents-need-a-semantic-layer-traditional-activity-7383530747850170368-nRA7/), Anthony Alcaraz chimes in.

**Query more, wait less. Try Tentris today**

[![](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/Tentris%20Logo%20mit%20Name%20Square.png)](https://linkly.link/2Tc9K)
Tentris is a new disk-based RDF graph database that delivers blazing fast querying performance with highly efficient memory usage, turning analytics that once took days into results within minutes or seconds. Built for real time workloads and complex data, it solves tasks others cannot.

#### Subscribe to the Year of the Graph Newsletter

Keeping track of all things Graph Year over Year

Subscribe

#### **Graph databases: growing market, competition & options**

Moving to graph database updates, let’s open with another piece of news from Microsoft. In Microsoft’s Q1 2026 earnings call, it was reported that [Cosmos DB business grew over 50% YoY](https://www.linkedin.com/posts/kirillgavrylyuk_from-msft-earnings-call-yesterday-cosmos-activity-7389713806656139264-vMsp). Cosmos DB is a multi-model database, and we don’t know the extent to which graph contributed to its growth.

However, this signal is one of many pointing towards growth for graph databases. [According to Fortune Business Insights](https://www.fortunebusinessinsights.com/graph-database-market-105916), the global graph database market size is projected to grow from $2.85 billion in 2025 to $15.32 billion by 2032, exhibiting a CAGR of 27.1%.

Microsoft, AWS, Google, and Oracle were named as leaders in the [2025 Gartner® Magic Quadrant for Cloud Database Management Systems](https://cloud.google.com/blog/products/data-analytics/a-leader-in-2025-gartner-magic-quadrant-for-cdbms). All superscalers have a graph database offering with Cosmos DB, Amazon Neptune, Google Spanner Graph, and Oracle Graph, respectively.

[![Gartner Magic Quadrant for Cloud Database Systems 2025](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/2025_Gartner_Magic_Quadrant_for_Cloud_Data.png)](https://cloud.google.com/blog/products/data-analytics/a-leader-in-2025-gartner-magic-quadrant-for-cdbms)Gartner Magic Quadrant for Cloud Database Systems 2025
[Neo4j was the only pure-play graph database to be listed in the same Magic Quadrant](https://neo4j.com/blog/news/gartner-magic-quadrant/) as a niche player. Neo4j also announced [Fleet Manager, a single control plane for all Neo4j deployments](https://neo4j.com/blog/news/neo4j-fleet-manager/), as well as the release of [Neo4j Graph Analytics for Snowflake in the Snowflake Marketplace](https://neo4j.com/blog/developer/unleash-neo4j-on-your-snowflake-data/).

But there has also been [churn in the graph database market](https://www.linkedin.com/posts/szarnyasg_graph-database-system-licenses-activity-7383889513019899906-FzMQ). [Dgraph was acquired by Istari Digital](https://www.linkedin.com/feed/update/urn:li:activity:7390997231539040256) to strengthen data foundation for AI and engineering. And the [KuzuDB embedded open source graph database has been abandoned by its creator and sponsor Kùzu Inc](https://www.linkedin.com/feed/update/urn:li:activity:7384825332786270208).

[LadybugDB](https://www.linkedin.com/pulse/ladybug-next-chapter-embedded-graph-databases-arun-sharma-29xuc) and [RyuGraph](https://www.linkedin.com/feed/update/urn:li:activity:7389177893593116673) are new forks of the KuzuDB codebase aiming to pick up where KuzuDB left off. Furthermore, [GraphLite emerged as a new open source graph database for embedded processes](https://www.linkedin.com/feed/update/urn:li:activity:7398636380894982144), and [FalkorDB introduced FalkorDBLite](https://www.falkordb.com/blog/falkordblite-embedded-python-graph-database/) – both aiming to fill in the embedded graph database void left by KuzuDB’s departure.

Challengers such as [QLever](https://www.linkedin.com/feed/update/urn:li:activity:7387073579378446336), [RushDB](https://www.rushdb.com/blog/labeled-meta-property-graphs-rushdb-s-revolutionary-approach-to-graph-database-architecture), [TuringDB](https://docs.turingdb.ai/concepts/columnar_storage), [TypeDB](https://www.linkedin.com/feed/update/urn:li:activity:7392441603581353984), and [DuckDB](https://www.linkedin.com/feed/update/urn:li:activity:7387100945270136832) with its [DuckPGQ](https://duckpgq.org/) extension are emerging. It seems like the graph database market pie is growing, and the competition for a piece of it is intensifying.

Finally, another signal pointing in the direction of [growth for the graph market](https://yearofthegraph.xyz/newsletter/2025/05/the-evolution-of-the-graph-technology-and-business-landscape-in-2025-the-year-of-the-graph-newsletter-vol-27-spring-summer-2025/): Linkurious, who just published the [2026 update of their Graph technology landscape](https://www.linkedin.com/feed/update/urn:li:activity:7395001871431536640), are [getting acquired by Nuix in a €20M deal](https://www.proactiveinvestors.co.uk/companies/news/1083740/nuix-to-acquire-graph-intelligence-platform-linkurious-in-20m-deal-1083740.html).

#### **New tools and research**

Wrapping up with a roundup of new tools and research. Focusing on graph research and innovation in NeurIPS, one of the leading AI conferences, shows that [graph is a significant part of NeurIPS 2025, supporting its growing importance and market share](https://www.linkedin.com/feed/update/urn:li:activity:7401893973113470976).

[GraphFrames represents the natural evolution of GraphX](https://www.linkedin.com/feed/update/urn:li:activity:7389926925911302144), the native library for cluster-based graph processing on Apache Spark – one of the most powerful engines for large-scale data processing in distributed computing. GraphFrames has been revived after being dormant for a while, with version 0.10.0 recently released.

[Brahmand is an open source Graph Engine built on top of ClickHouse](https://www.linkedin.com/feed/update/urn:li:activity:7376506972617162752). It extends ClickHouse with graph modeling and OpenCypher, merging OLAP speed with graph analysis.

[Gephi Lite v1.0](https://gephi.wordpress.com/2025/10/08/gephi-lite-v1/) was recently released. Gephi Lite is a lighter, web-based version of Gephi, used for visual network analysis. Cosmograph, a single-node web-based tool used to visualize graphs, [released v.2.0](https://cosmograph.app/docs-general/).

[![Ontology-Guided open-domain knowledge extraction with LLMs](https://filedn.com/lAGFqCrfCf9p4SPhvQtCjAf/YotG_Images/Posts/YotGV.29/OntologyGuidedOpenDomainKnowledgeExtractionLLMs.jpeg)](https://www.linkedin.com/feed/update/urn:li:activity:7378376007600300032)Ontology-Guided open-domain knowledge extraction with LLMs
ODKE+ supports [Ontology-Guided open-domain knowledge extraction with LLMs](https://www.linkedin.com/feed/update/urn:li:activity:7378376007600300032), and [GraphQA introduces an open source agent for asking graphs questions](https://www.linkedin.com/feed/update/urn:li:activity:7384896235507216384). Tree-KG is [an expandable knowledge graph construction framework for knowledge-intensive domains](https://www.linkedin.com/feed/update/urn:li:activity:7386651233593405441).

[Text2KGBench-LettrIA is a refined benchmark for Text2Graph systems](https://www.linkedin.com/feed/update/urn:li:activity:7391731600243273728), attempting to address the question of whether LLMs are good at populating knowledge graphs based on a set of text documents. [RAGE-KG explores the state of the art and beyond in integrating Retrieval-Augmented Generation with Knowledge Graphs](https://www.linkedin.com/feed/update/urn:li:activity:7399350737803161600) as well as the synergies between Large Language Models and the Linked Open Data ecosystem.

[KGGen](https://www.linkedin.com/feed/update/urn:li:activity:7384174260149272577) extracts knowledge graphs from plain text with language models. [Exploring Network-Knowledge graph duality](https://www.linkedin.com/feed/update/urn:li:activity:7382359516987961344) is a case study in agentic supply chain risk analysis. And GraphPFN is an [attempt to create general-purpose graph foundation models from tabular foundation models](https://www.linkedin.com/feed/update/urn:li:activity:7381553667025330176).
