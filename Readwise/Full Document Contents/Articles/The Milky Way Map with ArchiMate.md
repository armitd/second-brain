# The Milky Way Map with ArchiMate

![rw-book-cover](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Milky-Way-Map-1-colors.png)

## Metadata
- Author: [[Eero Hosiaisluoma]]
- Full Title: The Milky Way Map with ArchiMate
- Category: #articles
- Summary: Intro. This blog post is written inspired by the Milky Way book by Cecilia Nordén. The book gives you the best understanding & overall big picture and detailed description of The Milky Way Map.
- URL: https://www.hosiaisluoma.fi/blog/milky-way-map/

## Full Document
**Intro**. This blog post is written inspired by the Milky Way book by Cecilia Nordén. The book gives you the best understanding & overall big picture and detailed description of The Milky Way Map. This blog post just gives you some tips on how to utilize the idea of Milky Way Map with ArchiMate modeling notation. If you like some other ways of visualization, please don’t waste your time with this. But if you like modelling with ArchiMate, and you have an appropriate EA-modelling tool, why not take a look at this. I’m inspired and impressed by the idea behind the Milky Way Map as introduced in the book. So I want to share these modelling *recipes* here with those who also like to cook with ArchiMate, and get some inspiration for capability-based development…

***Disclaimer*** – This content represents my interpretations of some parts of the Milky Way Map, and this article should not be taken as an exact nor complete description of the Milky Way Map.

— Eero Hosiaisaluoma

### Maps for enterprises

***The Milky Way*** is an approach to analyzing and visualizing the whole organization on one page. Too good to be true…

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Milky-Way-book.jpg)Figure 1: The book: The Milky Way – map, navigate and accelerate change, Cecilia Nordén.
…But it can be done! The Milky Way concept is based on the fact that most of us can understand and interpret visualized maps better than other kinds of information (such as plain text or tables). There can be many kinds of maps: maps of countries, cities, roads, undergrounds etc. But there can be a map of the organization too. The Milky Wap Map can be *THE* one-pager that everybody (!) in an organization understands: the C-level, managers, business developers, service designers, product owners, developers, architects, IT staff etc. A Milky Way map is based on common concepts such as value streams, capabilities etc.

***The Milky Way Map can be understood by executives within seconds. Brilliant graphical layout!***

A comprehensive overview of an organization can’t be easier to create or easier to use than the Milky Way Map. But the most important and valuable thing is that the Milky Way Map is really useful for all (!) the stakeholders in an organization. Everybody can share the same insight of the organization with this nice way of visualization: how the organization creates value, with which value streams, what are the capabilities, and how the capabilities are realized. The Milky Way Map is easy and quite fast to create, and it is easy to understand. Enterprise Architecture cannot be made easier than this.

The Milky Way is introduced in the book named “*The Milky Way – map, navigate and accelerate change*” by Cecilia Nordén (Amazon [link](https://www.amazon.in/Milky-Way-navigate-accelerate-change-ebook/dp/B09H61612Y/ref=sr_1_1?qid=1660472471&refinements=p_27%3ANORDEN&s=books&sr=1-1)). The Milky Way is a model, a method and a philosophy. Annika Klyver has introduced the idea in many webinars (here is one of those: [link](https://www.youtube.com/watch?v=DbcdM-UNtes)).

##### Enterprise Architecture on a page

A Milky Way Map can be created with seven steps as follows (according to the Milky Way book):

1. Identify the main steps in the value flow
2. Make rough division within the sectors
3. Capture capabilities, IT systems and information flows
4. Integrate and gain acceptance
5. Follow the value flow
6. Review the map
7. Add explanatory information.

The Milky Way method encourages open communication and discussion, sharing the map with other roles for gaining wider acceptance.

The Milky Way Map provides an overall insight into an organization. It can be used as a communication model & method from managers to developers, for everybody who is interested in what is happening in the organization and how it really works. The Milky Way Map provides a chance for the Enterprise Architecture to be important.

The Milky Way Map is at its best in communication and knowledge sharing between then decision-makers, development teams etc. But the very core of a Milky Way Map is built on elements, the building blocks, of the Enterprise Architecture.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/MilkyWay-picture.png)Figure 2: The real Milky Way galaxy.
The idea is simple – as in most of the best concepts. The overview of an enterprise is provided within a map. The map is visualized according to an analogy to a galaxy: entities surrounding the center. This image makes it easier for us to construct a common, shared mental model and associate entities with organizational entities. The target enterprise can be e.g. the whole organization, a business unit, or a value stream that overlaps organizational units.

In the middle of the map is the organization logo as shown in the figure below. The center is surrounded by the value stream, which is divided into sectors that consist of capabilities. So simple as that. Easy to start with. The complexity comes with the details. However, it is a matter of choice how detailed maps are to be created. The simpler the better, so that all the stakeholders can share the same understanding: what is the organization all about. The Milky Way Map can be modelled on diverse abstraction levels depending on the case and what is appropriate in the organization. For example, a high-level (level-1) view can be created for executives and more detailed views (levels 2-n) can be created for business developers and designers. Some tools provide a drill-down feature to switch from one level to another.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Milky-Wap-Model.png)Figure 3: The Milky Way Map – the Enterprise Map.
In any case, it is always valuable to get a quick overview of the context – the easier, the faster, the better. The Milky Way method nicely leads us to start with the big picture first. Just like the analogy to the real *Milky Way* galaxy in the sky – the first sight is the galaxy itself with the center and surrounding entities (figure 2 above). Then we can sharpen the picture and zoom into details. Then we can see smaller entities from which the bigger entities are composed of.

In the business, it is good practice to start with the high-level context with coarse-grained elements, and then iterate into more detailed views. We can first capture a wider landscape map with large objects. Then continue by adding sub-objects and their interactions. Like zooming with Google Map from the sky to the ground: first, we see countries, then cities and roads, then buildings and streets etc. The Milky Way method and model enable this same idea of having an overall overview map visible all the time, and going deeper and deeper – depending on what is appropriate in the case. The Milky Way Map is *the map of the enterprise*.

**Change activities** can be pointed out by visualizing them by specific coloring on the Milky Way Map. It is quite typical to use heat mapping within capability maps. With the Milky Way Map, we can use the idea of a heat map to the overall overview of the organization: by coloring, we can highlight those capabilities (and their inner elements) that are affected by a certain – major or minor – change in the organization. E.g. the most affected capabilities (or projects or products) and related IT systems can be shown with some heat map color etc.

**Information Management** is one of the main drivers behind the Milky Way Map, which is focused on the information flows between the capabilities. When capturing how information is flowing through the systems, we can achieve e.g. following things: a) the overview of information flows between main business-critical systems, b) specific integration points and c) data security aspects, d) *what* is the data and *who* manages it (within the organization). As we know what has been said to emphasize the importance of information exchange: “integrations are the reasons for success or failure in an organization”. The better we can manage flows of information, and those valuable assets, the better we can run the business.

**Customer perspective** is another aspect of the Milky Way Map. As the value stream-based capability mapping focuses on the organizational view, the *inside-out* view, and the customer perspective focus on the customer view, and the *outside-in* view. Both viewpoints can be defined and visualized with the Milky Way Map. Customer journeys can be added to the outer circle of the Milky Way Map. Customer touchpoints can be connected to certain elements in the capabilities. The Milky Way Map can be used for analyzing the entire organization at the same time. From the customer point of view, we can visualize the customer journeys, and we can visualize how they interact with the organization’s capabilities and resources.

##### The Milky Way Map + ArchiMate = perfect match

A nice way to use the Milky Way Map is to utilize it together with the most comprehensive Enterprise Architecture modeling language, the [ArchiMate](https://pubs.opengroup.org/architecture/archimate3-doc/) standard. As the ArchiMate defines all the necessary concepts and relationships between them, the ArchiMate is a good choice for creating Milky Way Maps. ArchiMate provides all the required building blocks of the Milky Way Map:

* Value Stream
* Capability
* Application (IT system)
* Business Actor
* Business Service, -process and -function
* etc. (ArchiMate provides all the meaningful elements to model organizational concepts)

A quick way to create an MVP of the Milky Way Map goes as follows:

1. Create a diagram with the value stream in the center, the value stream stages as “sectors” (divided by radial lines)
2. Place the capabilities into the sectors of the value stream
3. Capture resources of the capabilities (e.g. processes, actors, IT systems)
4. Capture information flows between the resources.
5. Add customer journeys into the outer circle when analyzing the customer experiences (the *outside-in* view)

The figures below illustrate how the Milky Way Map can be modelled with the ArchiMate.

The first version of the Milky Way Map can be based on the value stream sectors and core capabilities as shown below.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Milky-Way-Map-1-colors-1.png)Figure 4: Milky Way Map (level-1).
The second version of the Milky Way Map can be extended with more detailed capabilities as shown below.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Milky-Way-Map-2-2.png)Figure 5: Milky Way Map (level-2). (Note! This coloring scheme uses the default colors of ArchiMate. Any other colors can be used according to what is appropriate.)
The Milky Way Map consists of capabilities mapped to value streams. Each capability consists of elements such as actors and applications that switch information. Information flows between the elements *connecting the dots* – the capabilities – with each other.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Milky-Way-Map-2-part-1.png)Figure 6: Milky Way Map (level-2) – part.
Note! The Milky Way Map focuses on the ***value flow***, which can be a) a value stream or b) a value network. In both cases, the enterprise is placed in the middle and the value stages with its entities in the surrounding sectors. In addition, the Milky Way Map can be used for visualizing the entire ecosystem that spans several organizations. Such an ecosystem is a cooperation of organizations, in which each organization takes the responsibility for specific actions in a high-level customer journey.

##### What are the organizations made of?

**Capabilities** – they represent the DNA of a business. A capability is a high-level abstraction of the things that an organization needs for executing its strategy and business model. A capability defines **WHAT** an organization shall have. A capability encapsulates the details of **HOW** it is realized. These details can be modelled with elements such as applications, actors, processes, functions etc. Each of these defines specific behavioral or structural aspects of an organization, encapsulated in capabilities. By discussing the capabilities, we make things easier to communicate and decide: we discuss the big boxes – no matter if they are built up of services, processes, functions, actors or applications, or all of them.

Capability definintion [[ArchiMate](https://pubs.opengroup.org/architecture/archimate3-doc/chap07.html#_Toc10045359)]:

* A capability represents an ability that an active structure element, such as an organization, person, or system, possesses.
* Capabilities provide a high-level view of the current and desired abilities of an organization, in relation to its strategy and its environment.
* Capabilities are realized by various elements (people, processes, systems, and so on) that can be described, designed, and implemented using Enterprise Architecture approaches.
* Capabilities may also have serving relationships; for example, to denote that one capability contributes to another.

A capability can contain sub-capabilities as shown in the figure below.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Capability-Decomposition-1.png)Figure 7: Capability Decomposition: capability and sub-capabilities.
A capability is a basic building block of an organization. Though, a capability is just a container, representing the behavioral unit in an organization. A capability consists of actual behavioral and structural elements. A capability can be decomposed as shown in the figure below. On the left, the core elements (actor, function and application) are nested in the capability element. This visualization can be used for saving space in a large diagram. On the right, we can see that the core elements are realizing the capability. These relations are kept intact in the EA model, even though they are not visible when the elements are nested into the composition element – the capability. (Note! The nested elements can be connected to the capability by using e.g. association relationship.)

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Capability-Decomposition.png)Figure 8: Capability Decomposition.
In large EA models of hundreds of applications, we can simplify the high-level Milky Way Map overview -diagram by abstracting applications in groups. For example, we can use abstractions such as “Financial systems” or “Payment applications” etc. in the diagrams. Even though using nesting and hiding some relations visually, all the relations are kept intact in the EA model so that it remains coherent.

A capability consists of both behavioral and structural elements (resources) as shown below.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2016/12/Capability-composition.png)Figure 9: Capability composition.
##### Capabilities and Value Streams

Capabilities and Value Streams are interrelated with each other: capabilities define WHAT an organization does, and value streams define WHY an organization does what it does. Capabilities “serve” certain value stages of a value stream

Value Stream definintion [[ArchiMate](https://pubs.opengroup.org/architecture/archimate3-doc/chap07.html#_Toc10045360)]:

* A value stream represents a sequence of activities that create an overall result for a customer, stakeholder, or end-user.
* A value stream describes how an enterprise organizes its activities to create value.
* A key principle of value streams is that value is always defined from the perspective of the stakeholder – the customer, end-user, or recipient of the product, service, or deliverable produced by the work.
* Value streams may be defined at different levels of the organization; e.g., at the enterprise level, business unit level, or department level.
* Capabilities can serve (i.e., enable) a value stream.

The figure below illustrates that the capability -element is related to the Value Stream -element (named “Plan”) with the *serving* -relationship. The value stream elements are connected with the *flow* -relationships. All the elements and their relationships are introduced in the ArchiMate standard (see the specification from [here](https://pubs.opengroup.org/architecture/archimate3-doc/)).

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Capability-and-Value-Stream-2.png)Figure 10: Capability and Value Stream.
There can be several value streams in an organization: operational value streams [[SAFe](https://www.scaledagileframework.com/operational-value-streams/)] and development value streams [[SAFe](https://www.scaledagileframework.com/development-value-streams/)].

It is worth noticing that a value stream gives the capabilities reason to exist. A capability is a potentiality, but meaningless without a value stream. The value stream is the definition of how the organization creates value to its customers. It is the value stream that gives meaning for a capability.

The topic of value stream analysis is covered in more detail by Christine Dessus in “*Value analysis with Value Stream and Capability modeling*”, see this [link](https://www.slideshare.net/chdessus/value-analysis-with-value-stream-and-capability-modeling). Some more about value stream modelling can be found [here](https://www.hosiaisluoma.fi/blog/value-stream-modelling/).

##### Capability relations

As capabilities are defined at a high level, they represent organizational behavior, not the concrete elements/entities such as services, processes, actors or applications (IT systems). Some capabilities can be stand-alone (within a value stream to which they are connected), or capabilities can be integrated with each other as shown in the figure below. For example, a capability can serve another capability logically (1 ), capabilities can be integrated when their elements switch the information (2), or some element of a capability can serve an element in another capability (3).

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Capability-relations-2-1.png)Figure 11: Capability relations.
At the highest level of organization development, there can be information flows between capabilities as shown below. However, further analysis introduces the actual parties of the information switching: typically the information is transferred between the actors, processes and/or applications.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2016/12/Capability-cooperation.png)Figure 12: Capability cooperation.
##### Relations between the elements of the Milky Way Map

The relationships between the elements in a Milky Way Map are based on standard ArchiMate relationships as shown in the figure below.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Relations-between-the-elements-2.png)Figure 13: Relations between the elements.
**Application Integration**. It is depending on the case in which the architectural model is implemented in integrations between the applications. Large organizations, with hundreds of systems, may have guidelines defined in their integration architecture, e.g. which integration mechanisms are recommended or allowed. In the case of Event-Driven Architecture (EDA), applications switch data by throwing and catching events (modelled by Application Events and trigger relationships in ArchiMate). In case of API -architecture, applications expose interfaces (modelled by Application Services or Application Interfaces in ArchiMate) to each other and to be used via API-Gateway or such.

For more details of integration patterns see *Enterprise Integration Patterns*, G. Hohpe & B. Woolf, from [here](https://www.enterpriseintegrationpatterns.com/). All the details related to the topic of application integration can be modelled with ArchiMate – in any relevant level of details – depending on what is appropriate in the organization.

##### Examples

###### IT organization

Here is a Milky Way Map example of an IT organization at a high level. This map is on the 1st level, showing only the capabilities. The next level shows how the capabilities are built: their services, functions and/or processes.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Milky-Way-example-IT-organization.png)Figure 14: Milky Way example at level-1 : an IT organization.
###### Training Organization

This fictive training organization introduces the basic concepts of the Milky Way Map. The idea is adapted from the book *The Milky Way – map, navigate and accelerate change*, Cecilia Nordén, and applied and simplified here for introduction purposes.

The first insight/iteration (level-1) into the organization is as follows:

1. Identify the main steps in the value flow
2. Make rough division within the sectors
3. Capture capabilities…

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/MW-Training-Organization-Level-1.png)Figure 15: Training Organization – Milky Way Map – Level-1.
The concepts used in the diagrams are listed in the figure below. Note! The coloring scheme of the elements is to be decided in the organization. Here the internal elements are shown in light colors, and external elements are shown grayed (the “book” suggests another coloring).

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Legends-1.png)Figure 16: Concepts in diagrams.
The next iteration (level-2) into the overview is as follows:

4. Capture the actual *behavior* and *structure* of each capability (services, processes/functions and applications)

5. Capture information flows

The figure below illustrates the iterative and incremental method of adding more details during the co-operative process, in which the multidisciplinary team creates more content into the overall DRAFT version of the Milky Way Map. Some of the information flows are already analyzed, and some more analysis needs to be done for getting all the interactions between applications defined.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/MW-Training-Organization-Level-2-1.png)Figure 17: Training Organization – Milky Way Map – Level-2.
**A customer journey** can be added to the outer circle of the Milky Way Map as shown in the figure below (yellow elements with arrow symbols). It is good practice to place those customer-facing capabilities in the outer circles of the map so that the customer journey can be easily mapped. This version of the Milky Way Map can be used for analyzing the customer experience aspects in service design purposes.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/MW-Training-Organization-Level-2-Customer-Journey-2.png)Figure 18: Training Organization – Milky Way Map – Level-2 with a Customer Journey.
Again, we can create distinct diagrams for many specific cases in more detail, but we can illustrate the big picture with the Milky Way Map. It is a good overview picture for communication purposes to start with, from which we can continue e.g. by focusing on specific parts or aspects.

##### At the end of the day – why to model the Milky Way Map?

Finally, why use a modelling tool and a modelling language to create a Milky Way Map? Such a picture can be created with any tool. The simpler the better. Yes, for sure. It is just that most of the large organizations already have some modelling tool – or perhaps a professional EA tool with repository and ArchiMate support. Why not use that?

An EA tool ideally contains all the elements of the organization (depending on the maturity of the EA). E.g. all the applications (a.k.a. information systems) are typically imported from the CMDB via integration to the EA tool. All the process- and actor elements etc. are also included in the repository of the EA tool. So all the elements, all the building blocks of the Milky Way Maps are already (or to be) harvested into the repository of the EA tool.

The EA tool’s repository is the inventory of all the elements of the organization. The EA tool provides the skeleton for the *Digital Twin of an Organization (DTO)*, on top of which the “near real-time business operating system” can be built in the near future (according to [Gartner](https://www.gartner.com/en/information-technology/glossary/digital-twin). See a video of [DTO](https://www.youtube.com/watch?v=mXKBfrJSjiA) by [Mavim](https://www.mavim.com/mavim-platform/digital-twin-of-an-organization)). And, the EA tool provides the standard language: the ArchiMate. That is why the EA modelling tool is a good choice for creating the Milky Way Maps. By modelling the Milky Way Map with the ArchiMate within an EA tool, we can be sure that all the names of the elements are correct, and elements are connected with each other correctly, and the very same elements can be re-used (not duplicated). The main difference between a drawing tool and a modelling tool is that in the modelling tool all the elements are reusable objects in the repository. When modelling lots of diagrams, it is important that we use the very same elements.

Why to use ArchiMate? Because it is the most comprehensive and expressive Enterprise Architecture modelling notation, and it is supported by many tools (see the Open Group register of certified ArchiMate tools from [here](https://certification.opengroup.org/register/archimate-tool)).

To enable and encourage communication is the most important. To be precise modeling enables better information for better decisions!

##### Discussion

The value proposition of the Milky Way Map is, that it is “an enterprise’s overall value flow”. Yes, definitely the Milky Wap Map is an innovative way to visualize the entire organization. Though it’s possible to provide an overview, it’s no doubt matter of simplifying and abstracting things.

The decision of the acceptable granularity level has to be taken: what level of details is enough and appropriate? By contrast, a large organization with hundreds of IT systems cannot be visualized in a reasonable way in one view. When the complexity increases in a picture, ambiguity arises, then any picture becomes too difficult to understand and too difficult to maintain. That is somewhat inevitable for any visualizations, no matter the method or model, or notation used. However, the Milky Way Map is an exceptionally expressive and powerful approach to provide an overall big picture. But again, as usual, we should always keep the visualizations as simple as possible – but no simpler than that.

One of the most promising approaches to visualize the overall overview of an organization is the Milky Way Map. It can be used as “an anchor model” for enabling and encouraging communication and knowledge sharing (figure below). The Milky Way Map can be used as the primary ***method*** and ***model*** among all the stakeholders and practices that have some interest in any change activities in an organization (designers, developers, partners, EAM, PMO, SMO etc.). The Milky Way Map ***philosophy*** is aligned with the Lean principles and agile development practices as well. And what is particularly important: the Milky Way Map can be used for opening & having the discussion and commitment with managers and business leaders. The Milky Way Map provides a nice visual layout for communication purposes. The map of the enterprise!

If a one-pager should be made covering any business-relevant area, the Milky Way Map is a practical, pragmatic and productive choice. Shared understanding for accelerating the change in an organization.

![](https://www.hosiaisluoma.fi/blog/wp-content/uploads/2021/03/Anchor-Model.png)Figure 19: Anchor Model.
For more details, see the following materials covering the Milky Way:

* *The Milky Way – map, navigate and accelerate change*, Cecilia Nordén, IRM, ISBN 978-91-977119-3-7
* *Enterprise Maps to navigate complexity*, Annika Klyver, 26 Oct 2020, Youtube, <https://www.youtube.com/watch?v=DbcdM-UNtes>
* The Milky Way Academy, <https://www.themilkywayacademy.com/>

For more ArchiMate examples in a structured way, check the **ArchiMate Cookbook**, via this [link](https://www.hosiaisluoma.fi/blog/archimate-cookbook/). (Also available as a pdf [link](http://www.hosiaisluoma.fi/ArchiMate-Cookbook.pdf) .)

– Eero Hosiaisluoma
