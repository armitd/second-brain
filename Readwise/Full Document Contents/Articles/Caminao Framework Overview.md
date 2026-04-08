# Caminao Framework Overview

![rw-book-cover](https://caminao.blog/wp-content/uploads/2022/11/Prism-Cake-1.png)

## Metadata
- Author: [[Caminao's Ways]]
- Full Title: Caminao Framework Overview
- Category: #articles
- Summary: Enterprise architectures are dynamic structures that evolve throughout the life cycle of a business, focusing on key capabilities and layers to align with environments. Symbolic representations play a crucial role in enterprise architecture, managing knowledge and fostering interoperability through layered yet interconnected models. Decision-making processes are paired with data, information, and knowledge to support operational, tactical, strategic, and support actions within enterprises.
- URL: https://caminao.blog/about/caminao-framework-overview/

## Full Document
[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MCi-Pagoda.png?w=455&ssl=1)](https://caminao.blog/about/caminao-framework-overview/#blueprint)Pagoda Blueprint
EA Ontologies
Knowledge Galaxies
![](https://i0.wp.com/caminao.blog/wp-content/uploads/2021/09/Pagoda-Icon.png?w=1680&ssl=1)
[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/10/Prism-BBFi.png?w=445&ssl=1)](https://caminao.blog/about/caminao-framework-overview/#digitwin)The Brain of the Firm
Projects & Workshops (MBSE)
Processes & Workflows
Decision-making
***Click on Cards***

#### The Pagoda Blueprint

Compared to brick-and-mortar architectures, which are tangible and perennial, enterprise architectures are works in progress to be carried out all along the life cycle of enterprises. Hence the need of maps to monitor changes in business and technical environments, ensuring the continuity and consistency of representations and the traceability and accountability of decisions-making processes.

To that effect, enterprise architectures are described in terms of key capabilities (Who, What, How, Where, When) at levels (or tiers or layers) defined with regard to environments:

* At the enterprise (or organizational) level, blueprints consider business environments, concepts, objectives, organization and processes.
* At the technical (or operational) level, blueprints consider physical and digital environments, systems interfaces, and platforms.
* In-between, logical/functional blueprints deal with the symbolic representation of business models, organization, and systems.

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MC-Pagoda.png?w=712&ssl=1)](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MC-Pagoda.png?ssl=1)Enterprise Architecture Capabilities
While terminologies may vary, the Pagoda levels can be neatly aligned with:

* [Established conceptual, logical, and physical modeling levels](https://caminao.blog/book-pick-the-shift-to-the-stanford-paradigm/)
* [MDA (Model Driven Architecture)](https://caminao.blog/2016/11/09/focus-mda-uml/) CIM (Computation Independent), PIM (Platform Independent), and PSM (Platform Specific) models
* [Zachman architecture framework](https://caminao.blog/enterprise-architecture-fundamentals-the-book/book-pick-zachmann-framework-revisited/)

More limited alignments can also be achieved with engineering frameworks like [Archimate](https://caminao.blog/overview/archimate-the-pagoda-blueprint/) or Capella/Arcadia.

#### Knowledge

Symbolic representations are the bread and butter of architecture, especially for enterprise architecture which is by itself a mix of physical and symbolic artifacts; not to mention their immersion in digital environments.

##### EA Ontologies

From a functional perspective the role of ontologies is to manage [knowledge representations](https://caminao.blog/knowledge-management-booklet/) (KR); as defined by Davis, Shrobe, and Szolovits, that can be summarised with five basic functions:

1. Surrogates: manage the symbolic counterparts of objects, events and relationships identified in context and pertaining to concerns.
2. Ontological commitments: maintain a set of consistent statements about the categories of things that may exist in the domain under consideration.
3. Fragmentary theory of intelligent reasoning: support actionable an representation of what the things can do or can be done with.
4. Medium for efficient computation: make knowledge understandable by computers and support smooth learning curves.
5. Medium for human expression: improve the communication between specific domain experts and generic knowledge managers.

Traditional models can support points 1, 4 and 5, but often fall short of points 2 and 3. Ontologies are meant to generalize the representation of and the reasoning about any kind of realm, actual or virtual:

* Terms, for elementary meanings (lexicon)
* Facts, for actual or symbolic elements identifiable in environments (directories)
* Categories, for the symbolic representation of facts
* Concepts, for semantic constructs defined independently of instances or categories
* Documents, for structured symbolic contents

To that effect, EA ontologies must bring together different kinds of resources:

* Thesauruses, deal with the meaning of terms, categories, and concepts.
* Models, add syntax to build representations of contexts and concerns.
* Ontologies, add pragmatics in order to ensure the functional integration of models and thesauruses in physical and symbolic environments.

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MC-Onto-3.png?w=759&ssl=1)](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MC-Onto-3.png?ssl=1)Ontologies
Mirroring the representation of contents, linguistic tiers can be mapped to communication interfaces: digital (things), symbolic (systems), natural (people).

##### Data, Information, Knowledge

The **r**aison d’etre of enterprise architecture is to bring under a common roof business, organizational, and technological perspectives. As there is no reason to assume a comprehensive, ecumenical and fixed language, ontologies must provide constructs ensuring the interoperability of the various thesauruses and modeling languages in use.

To begin with, a key distinction is necessary between data, information, and knowledge:

* Data (or facts as defined by ORM) encompass whatever can be observed in environments
* Information (aka models) deals with the symbolic representations managed by enterprises
* Knowledge is for enterprises’ objectives and value chains, in other words data or information put to use

To ensure the sharing of resources as well as a full traceability of outcomes, layered yet interoperable representations are required:

* Networks, for the semantics of the terms employed
* Resource Description Framework (RDF), for the syntax used by modeling languages to describe the structure of categories
* Graphs, for the concepts and pragmatics of domain specific languages

A [galactic metaphor](https://caminao.blog/knowledge-management-booklet/a-hitchhikers-guide-to-knowledge-galaxies/) can be used to describe their integration:

* Stars, planets, and satellites, respectively for concepts, categories, and facts
* Gravity forces, for positive or negative semantic bonds between terms
* Star systems and orbits, for the abstraction levels within (subtypes) and between (realization) perspectives

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/09/MC-Galax.png?w=758&ssl=1)](https://caminao.blog/knowledge-management-booklet/a-hitchhikers-guide-to-knowledge-galaxies/)Knowledge Galaxies
For instance:

* ‘Wheels’ is a familiar equivalent for ‘Car’, ‘Bike’ is opposed to ‘Car’ (definition) and ‘Wheels’ (usage)
* Stat system for concept Vehicle encompasses Car, Boat, and Plane categories, as well as Time Capsule concept
* Motorbike and Bicycle are actual subtypes of bike, as instances can be mapped to identified elements in environments
* Compact, Van, and SUV are functional (aka symbolic) subtypes of rental categories, as instances can be mapped to sets of identified elements in environments
* Retired and Employed commuters are actual realization of Commuter (as opposed to subtypes) because while there are instances identified in environment there is no managed categories representing them
* Ford Mustang and Fiat500 are functional realization of Car Model (as opposed to subtypes) because there is no identified instances or managed categories

It must be stressed that ensuring the interoperability of representations makes no assumption with regard to their validity.

##### Ontological Prisms

[Ontologies are meant to ensure the integration of thesauruses, models, and knowledge graphs](https://caminao.blog/knowledge-management-booklet/), as well as the [interoperability of representations](https://caminao.blog/knowledge-management-booklet/a-hitchhikers-guide-to-knowledge-galaxies/): facts (data view), categories or types (information view), and ideas or concepts (knowledge view). That can be achieved with [ontological prisms](https://caminao.blog/knowledgeable-organizations/the-pagoda-playbook/ea-digital-twins/) treating contents as light, enabling some kind of reversible diffraction between ontologies’ contents and data, information, and knowledge constituents.

To be of any use the diffraction mechanisms must ensure a consistent composition and decomposition of contents at different levels of abstraction, within and across views:

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/Pyram01g-7.png?w=571&ssl=1)](https://caminao.blog/knowledgeable-organizations/the-pagoda-playbook/ea-digital-twins/)Subsets (data view): between identified facts (physical or symbolic) and named sets (symbolic)
* Types and subtypes (information view): between identified facts and categories or types (symbolic)
* Kind-of (knowledge view): between ideas, or concepts
* Realizations: across views

Ontological prisms could thus be used to ensure a continuous and sustainable alignment of architecture designs with emerging changes brought about from shifting environments. And that alignment is not limited to symbolic representations: with enterprises immersed in digital environments ontological prisms can be turned into ” …virtual representation of an object or system that spans its lifecycle, is updated from real-time data, and uses simulation, machine learning and reasoning to help decision-making.” (What is a digital twin? IBM)

On that basis ontological prisms can serve as matrices for EA digital twins:

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MC-Digitwin-2.png?w=671&ssl=1)](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MC-Digitwin-2.png?ssl=1)EA Digital Twin
* Processes design reflect the crossing of business models (knowledge) and business intelligence (data mining)
* Operations reflect the crossing of application (information) and environment (process mining)
* Organization reflects the crossing of business models (knowledge) and enterprise architecture capabilities (information)

##### The Brain of the Firm

Ontological prisms can go further, turning digital twins into enterprises’ nervous and cognitive systems combining osmosis and homeostasis:

* Ontologies ensure the [comprehensive and consistent symbolic representation](https://caminao.blog/knowledge-management-booklet/) of the different components of an enterprise architecture
* Machine learning technologies enable updates from real-time data, if with some latency for information and knowledge (Osmosis)
* Knowledge graphs enable the [pairing of decision-making processes and symbolic resources](https://caminao.blog/knowledge-management-booklet/knowledge-driven-decision-making-1/) and the explainability of actual and simulated processes (homeostasis)

That combination of sensory-motor systems immersed in digital environments on the one hand, a collective intelligence with reasoning, judgment, and learning capabilities on the other hand, gives a new relevance to Stafford Beer’s vision of a [“Brain of the Firm”](https://www.amazon.com/gp/product/047194839X/ref=dbs_a_def_rwt_bibl_vppi_i0) supporting the three fundamental cognitive functions:

* Understanding of contexts and opportunities (business intelligence)
* Symbolic representation of relevant aspects of contexts and opportunities (system modeling)
* Symbolic representation of virtual aspects of contexts and opportunities (planning)

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/10/Prism-BBF.png?w=750&ssl=1)](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/10/Prism-BBF.png?ssl=1)The Brain of the Firm
##### Decision-Making

Decision-making is often confused with problem-solving, namely how to pick a solution given a set of resources, typically people, information, financing, materials. That paradigm ignores the temporal dimension of enterprises’ decision-making which are made of interdependent commitments meant to be carried out across shifting backgrounds and overlapping timescales.

Assuming a [knowledge management framework](https://caminao.blog/knowledge-management-booklet/), the objective is to [pair (as in DNA strands) the Observation/Orientation/Decision/Action (OODA) steps of decision-making processes with their Data/Information/Knowledge counterparts for content](https://caminao.blog/knowledge-management-booklet/knowledge-driven-decision-making-1/).

* Observation: data can be obtained from digital or business environments. It can be analysed and turned into knowledge (business intelligence) or matched with models of managed information.
* Orientation: reasoning (information) is applied to observations (data) and judgment (knowledge).
* Decision: judgment (knowledge) is supported by observations (data) and causal chains (information).
* Action: decisions are carried out through a mix of operations (data) and organization (knowledge).

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/09/MC-OODAb-2.png?w=734&ssl=1)](https://caminao.blog/knowledge-management-booklet/knowledge-driven-decision-making-1/)Decision-making
Each step can thus put its focus on key issues, namely:

* Uncertainty (observations): facts are not gold nuggets ready to be picked from river beds; their meanings are mined from data and applications as determined by segmentation (models). Confidence, and more generally the quality of data, can thus be enhanced during decision-making processes.
* Causalities (orientation): competing in digital environments means that root causes and rationales, usually set upfront for problem-solving, can now be reassessed on a continuous basis, with causal chains improved through the integration of data analytics and information models.
* Risks (decisions): since business competition is by nature a time-dependent, nonzero-sum game, risks can be reassessed until the “last responsible moment,” when delaying a commitment would reduce the range of options or the expected returns. Such reassessment (knowledge) can take into account reduced uncertainties (data) and improved causal chains (information).
* Experience (action): decisions taken at the enterprise level usually involve sets of intertwined commitments and deeds whose efficiency is determined by the alignment of operations (data) with organization (knowledge). Set in digital environment, experience can benefit from direct feedback combining knowledge and observations.

More generally, the pairing of decision-making processes with the nature of symbolic resources can help to define horizons:

* Operational: when observed data can be directly mapped to information and put to use as knowledge, thus allowing for routine decision-making (a)
* Tactical: when the execution of decisions can be improved by additional data and better traceability (b)
* Strategic: when commitments must be made without reliable causal chains for the time frame considered; regular costs/benefits assessments must thus be replaced by risk-management schemes covering for ill-fated turns of events (c)
* Support: for actions meant to improve the capabilities of enterprises’ organization and systems.

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/OODA-OperTactStra-4.png?w=387&ssl=1)](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/OODA-OperTactStra-4.png?ssl=1)Horizon Knowl’Edges: Operational (a), Tactical (b), Strategic (c)
#### EA Engineering

Enterprise architectures are a combination of culture, organization, and systems with a life of their own. It ensues that EA changes cannot be carried out through autonomous projects as they must ensure the continuity, integrity, and consistency of supported activities. On that account phased processes with neatly defined inception and completion are of limited use for large, diversified, and structured organizations. Hence the benefits of setting apart changes pertaining to EA engineering from projects carried out at the system level.

##### Requirements

[Requirements](https://caminao.blog/how-to-implement-symbolic-representations/requirements/requirements-taxonomy/) expressed at the enterprise architecture level can be of any kind and nothing can be assumed upfront about their footprint. Hence the benefit of [ontological prisms](https://caminao.blog/knowledgeable-organizations/the-pagoda-playbook/ea-digital-twins/) for their elicitation:

* Business domain requirements describe activities independently of the part played by supporting systems
* Functional requirements describe the part of activities supported by systems
* Capability requirements describe functions shared across business processes
* Non functional requirements (Quality of service and technical) refer to to the implementation of supporting systems independently of specific functional contents.

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/11/PrismReks-1.png?w=389&ssl=1)](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/11/PrismReks-1.png?ssl=1)Requirements Capture
##### Projects & Workshops

[EA engineering](https://caminao.blog/enterprise-architecture-fundamentals-the-book/book-pick-agile-ea-engineering/) should first be defined by scope:

* System level, focused on the consistency and continuity of the representations managed by supporting systems
* Enterprise level, focused on the role of systems in support of business models

and purpose:

* Business value, for requirements rooted in the specifics of business processes as defined directly or through use cases
* Architecture assets, for requirements set across business processes, through models or system cases

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/04/Wf-Scopurpo-7.png?w=545&ssl=1)](https://caminao.blog/knowledgeable-organizations/the-pagoda-playbook/the-pagoda-workflows-governance/)Scope & Purpose
Engineering interfaces are then defined accordingly:

* Business cases (BC), between enterprises and environments
* Use cases (UC), between enterprises and systems, with Agile cases (AC) for stand-alone projects without organizational or technical dependencies (ensuring shared ownership continuous deliveries)
* Function cases (FC), between systems
* Technical cases (TC), within systems

Indicative remits can be added but the specifics are best left to enterprises’ organization.

Given scope and purpose, activities can then be assigned to workshops:

* Enterprise, for business objectives and organization (descriptive models)
* Domains, for the symbolic representation of business objects and processes (prescriptive models)
* Applications, for the implementation of processes by supporting systems (technical models)
* Systems, for operational resources deployments (configurations)

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MC-Workshops-6.png?w=722&ssl=1)](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MC-Workshops-6.png?ssl=1)Projects & Workshops
Projects, built bottom-up from work units attached to targeted artifacts, are managed as dynamic trees explored and developed according to the status of nodes and leaves:

* Roots are used to set contexts, business processes, and anchors in descriptive (or CIM) models (downward arrow). They can also be associated with functions and anchors in prescriptive (or PIM) models.
* Use cases are first seen as black boxes anchored to descriptive (or PIM) models (downward arrow).
* System cases are further detailed and anchored to technical (or PSM) models, and applications are developed and tested.
* Applications are integrated with functions, tested through use cases, and then used as white boxes; i.e., with their counterpart in systems (upward arrow).
* Use cases are finally integrated, tested, and accepted in operational (processes’) environments (upward arrow).

##### Processes & Workflows

***Enterprise architects “…are like sailors who have to rebuild their ship on the open sea, without ever being able to dismantle it in dry dock and reconstruct it from the best components.”*** (**Otto Neurath)**

That can only be done through workflows that combine phased and iterative schemes:

1. Agile development, for business-specific applications free of cross dependencies
2. Model-based developments, for architecture- based functions subject to cross dependencies
3. Workflows combining Agile and Model-based developments, for requirements with enterprise-level dependencies

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2021/06/fig-12-10.png?w=372&ssl=1)](https://i0.wp.com/caminao.blog/wp-content/uploads/2021/06/fig-12-10.png?ssl=1)EA & Development Models
Agile developments are carried out iteratively through a direct collaboration across enterprise, application, and systems workshops, without impacting shared use cases or models. Phased developments are organized across limited to the sharing of use cases or also to shared models.

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/08/MC-Workflows-2.png?w=752&ssl=1)](https://caminao.blog/knowledgeable-organizations/the-pagoda-playbook/)Processes & Workflows
The aim of the [Pagoda playbook](https://caminao.blog/knowledgeable-organizations/the-pagoda-playbook/) is set a path toward a comprehensive enterprise architecture supporting an incremental integration of engineering and business processes along revisited CMMI (Capacity maturity model integration) levels:

1. Initialization: existing assets, resources, and practices (systems, tools, organizational units, …) are progressively inventoried and matched with core Pagoda blueprint elements (components, models, use cases, …).
2. Management: inventoried elements are organized with regard to commonly accepted engineering categories, e.g., Zachman’s or ArchiMate’s
3. Normalization: projects are progressively defined (or refactored) in terms of core Pagoda blueprint categories for use cases and models, and development models, Agile or phased
4. Assessment: phased projects are refactored and assessed in terms of Model-based engineering processes.
5. Optimization: engineering processes, Agile or phased, are mapped to business ones, paving the way to EA maturity assessment.

##### EA Governance

Applying the ontological prism to Pagoda architectures can be used to align EA governance with symbolic resources:

[![](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/11/Prism-Cake-1.png?w=750&ssl=1)](https://i0.wp.com/caminao.blog/wp-content/uploads/2022/11/Prism-Cake-1.png?ssl=1)
* Requirements (facts)
* Business intelligence (facts/concepts)
* Strategic planning (concepts)
* Modernization (concepts/categories)
* Systems engineering (categories)
* Systems modeling (facts/categories)

Combined with enterprises immersion in digital environment that will provide a systemic, intelligible, and actionable framework for EA governance.

###### FURTHER READING

* [Knowledgeable Organizations](https://caminao.blog/edges-of-knowledge/)
* [Knowledge Management Booklet](https://caminao.blog/knowledge-management-booklet/)
* [Edges of Knowledge](https://caminao.blog/edges-of-knowledge/)
* [The Pagoda Playbook](https://caminao.blog/knowledgeable-organizations/the-pagoda-playbook/)
* [ABC of EA: Agile, Brainy, Competitive](https://caminao.blog/enterprise-architecture-fundamentals-the-book/)
* [EA in bOwls (Overview)](https://caminao.blog/ea-in-bowls/)
* [Knowledge-driven Decision-making (1)](https://caminao.blog/knowledge-management-booklet/knowledge-driven-decision-making-1/)
* [Models & Meta-models](https://caminao.blog/open-concepts/models-meta/)
* [Ontologies & Enterprise Architecture](https://caminao.blog/knowledge-architecture/ontologies-ea/)
* [Abstraction Based Systems Engineering](https://caminao.blog/system-engineering/models-perspectives/abse/)
* [EA & MDA](https://caminao.blog/2013/12/17/mda-ea/)
