# Why we need an edge data architecture to digitize the world — sustainably

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2022/08/GettyImages-1305428682.jpg?w=1024?w=1200&strip=all)

## Metadata
- Author: [[Vivien Dollinger]]
- Full Title: Why we need an edge data architecture to digitize the world — sustainably
- Category: #articles
- Summary: Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. Learn More Our world is inherently decentralized.
- URL: https://venturebeat.com/data-infrastructure/why-we-need-edge-data-architecture-digitize-world-sustainably/

## Full Document
Community

[@ObjectBox\_io](https://twitter.com/ObjectBox_io)

![binary data wave](https://venturebeat.com/wp-content/uploads/2022/08/GettyImages-1305428682.jpg?w=750)A glowing particle and binary wave pattern on dark background.
*Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. [Learn More](https://venturebeat.com/newsletters/?utm_source=VBsite&utm_medium=desktopNav)*

Our world is inherently decentralized. Over the last two decades, the trend in IT has been to ignore the decentralized world and work around it by combining impressive technologies and organizational structures in approaches such as cloud data warehouses. This is a huge obstacle for digitization projects.

To really, finally digitize across industries, we need a broader spectrum of data architecture options reflecting the diverse world. Only if we discard the domination of a centralized cloud-based approach and acknowledge the need for a distributed paradigm can we harness the potential of digitization and enable new use cases. In short: We need a true edge to open up the full spectrum of edge-cloud data architectures.

There are, of course, also many cases where centralization makes sense, but the centralized paradigm is of no or only limited use for all those cases that are inherently decentralized.

Forcing centralized cloud-use on decentralized/distributed use cases is economically, environmentally and socially wasteful. It is unsustainable and a major reason why digitization is stalling. On a broader level, this mismatch of topology and use case is detrimental to creating bottom-line value and harmful to the ecosystem’s welfare. On top of that, “edge washing” (a large cloud with a small edge under the “edge computing label”) is just worsening the situation and hindering the uptake of a paradigm that can create huge value.

For a thriving and innovative ecosystem, developers must have simple and efficient tools for decentralized and distributed computing in addition to the cloud, so they can choose the most useful and sustainable data architecture for a given project.

That’s in essence why we need a “new” data architecture reflecting the world as it is. Or, more specifically: we need infrastructure software — tools — that enable developers to digitize and capture the decentralized world so that they can build powerful new apps quickly and efficiently.

#### Why is data architecture central to successful digitization?

##### Data follows business needs

The goals of data architecture are to match business requirements with data and system requirements and to manage data flow through the enterprise in accordance with organizational strategy. Good data architectures make data available when and where it is required; data follows the business needs.

A closely related term is data modeling. Both data architecture and data modeling aim to bridge the gap between business objectives and technology. Data architecture, however, spans the organization and takes a high-level, holistic view, whereas data modeling focuses on specific systems or business cases.

In any case, the architecture or modeling should follow business needs. Often, however, the data architecture is on the highest level already given — it is centralized/cloud-based. As McKinsey puts it: “Using data effectively requires the right data architecture, built on a foundation of business requirements. However, most companies take a technology-first approach, building major platforms while focusing too little on killer use cases.“

With this dominance of centralized cloud computing comes an ”inaccessibility of edge data” and with it lost business opportunities and a blocker of innovation and value creation. In other words: We need an edge over the cloud.

The cloud needs an edge. (image by author)
##### Compute follows data

Today, data is produced and needed everywhere. “Edge data” is data generated on a myriad of decentralized devices like smartphones, cars, machines and consoles. Valuable data is therefore increasingly generated and used outside traditional data centers and cloud environments.

Many businesses struggle to access and use this decentralized edge data, which comes from sources like machines on factory floors, cars on the street, and batteries in airplanes. Yet there are already more connected devices than people on this planet. Every day their number grows. They produce huge amount of data. And the opportunities to create value from this data are manifold.

Transferring all this data to the cloud to make it accessible is currently not feasible, due purely to bandwidth. There are, however, several more good reasons why the cloud is not a viable option for making this data usable:

* No or intermittent connectivity
* Networking and cloud costs
* Data security concerns
* Data privacy concerns
* Latency

Edge computing refers to an inherently distributed computing paradigm that moves computation and data storage closer to the edge and to data sources. And [edges](https://venturebeat.com/data-infrastructure/ntt-unveils-what-it-calls-the-first-edge-and-private-5g-service/) are often distributed systems in themselves (edge of edges). However, [edge computing](https://venturebeat.com/business/how-edge-computing-impacts-data-infrastructure-strategies/) still lacks core infrastructure software that would facilitate its use. Unlike the centralized paradigm with its long-established cloud infrastructure, the decentralized/distributed paradigm has little infrastructure software yet available to help establish new projects quickly and easily.

Legacy systems combined with a cloud-centric infrastructure make it difficult to access and capture the value of edge data — and there is no easy option available. Because “distributed systems are hard,” it is nothing that is easily or quickly solved in-house.

And while there are always options to get (at least some of) that data, DIY solutions for these kinds of challenges typically cost a lot of time to implement, don’t scale well, are slow, and are later hard to maintain. In short, such costs do kill edge projects.

Lack of core edge tech (image by author)
There are many use cases that *only work* based on the decentralized edge computing topology and many that only *make sense* based on that topology. Some examples:

##### Smart vehicles

“Smart vehicles,” anything from connected cars to autonomous driving, need to satisfy high availability and reliability requirements and depend on lightning-fast data processing and transmission onboard. A car of course is a distributed system itself and cannot afford the latency and uncertainty a cloud-based approach brings. Intermittent connections can be used to transport some parts of the data to the cloud.

##### Remote locations

Anything in a remote location without (reasonable) internet access, e.g. oil and gas fields, tunnels and Points of Sales (PoS), really need applications that work without an internet connection on the edge. In the oil and gas industry, for example, failures can be disastrous. The many assets on-site therefore need to be carefully monitored but are typically in a remote location with little to no internet connectivity. Once a connection is available, some data can be transferred to the cloud. However, high MNO costs and limited bandwidth as well as flaky networks often require frugal choices with regard to data transferal.

##### Smart manufacturing

Smart manufacturing applications, at least in Europe, typically need to satisfy high data protection and security requirements, and for this very reason there may often be no direct connection to the internet — and many manufacturers are reluctant to have their data in the cloud. On site, you can find everything from low-frequency brownfield devices to high-frequency greenfield devices on a factory floor. As a rule, the machine controllers in use are not designed to store or transmit data. They usually lack not only the functionality but also the resources to support this. The clear separation of machine control and the edge data processing unit ensures that there is no risk of unintentional interference with the machine controller.

In all these examples, the typical use case entails a number of different devices, from controlling units to machines to phones to tablets to PCs. The edge consists of many edges that need to exchange data; however, the use cases really need at least guaranteed response times, and often speed is also of the essence, and so on. If you look closer at the cases, they all have the same base requirements:

* Decentralized devices
* Quality of Service (QoS) control
* Fast response times
* High availability
* Secure data handling
* Scalability and resilience
* Fault-resilient capabilities

And all those requirements aim at one thing: Having the right data available when needed and where needed.

Having the right data where it’s needed (image by author)
#### Anything that can go wrong will go wrong

What sounds trivial conceals a number of more complicated challenges arising from the challenge of data access in distributed systems (plus industry-specific challenges). The complexity becomes clear in the context of the system environment:

* The network is unreliable.
* Latency is not zero.
* Bandwidth is finite.
* The network is not secure.
* Topology can change.
* It’s unknown if there is an administrator at all, or how many.
* Transport is costly.
* The network is heterogeneous.

Fun fact: these have arisen from the “8 fallacies of distributed systems” that were defined back in the ’90s (e.g. the false assumption that the network is reliable). Bottom line: Anyone working on a distributed system needs to assume that “anything that can go wrong, will go wrong” — and it can be hard to take care of all the individual parts failing at any given moment, let alone any possible combinations thereof.

The complexity therefore already begins before the solution is implemented, as it necessitates a thoughtful approach to data architecture and the governance of a distributed system. What makes it even more difficult is the fact that distributed systems have multiple components spread across multiple locations, domains and technologies. This is likely to be one of the first stumbling blocks for many projects that need the edge: It already takes time and money — an investment — to come up with a solid conception.

Moreover, without core infrastructure software for the edge, every project will take a lot of time, money and nerves to implement just the basic mechanisms of such a complex system. And this will only be a foundation for what the project eventually wants to achieve based on the usable edge data. On top of that, due to the distributed nature, such a project will be error-prone and take diligent testing and iterations to get to a good level.

Visible and hidden requirements (image by author)
Last not least, such projects face another reality: It’s far easier to get budgets for visible and shiny features than for hidden features that “no one ever sees.” A “quick PoC” might be set up using the cloud to demonstrate the value of the application and using that data. However, it cannot be used in production later on due to all the reasons given above. So, digitization is stalling. The reality today is that, across verticals, a ton of data is unused and companies struggle to access edge data.

#### Why should I care about edge data architecture?

##### The power of the edge

Pushing data management capabilities toward edge environments adds value in a variety of ways. Once you can manage edge data on the edge, you can:

* Act with extreme speed and empower real-time use cases. By uniting data and computation on the edge, you get to a completely new level of efficiency and speed.
* Enable smarter devices and make more use of the already available and distributed hardware, including remote management or autonomous behavior via onboard (edge) data.
* Overcome data inconsistencies, protection, privacy and other data governance issues that arise from siloed or unused edge data or cloud-centric data architectures.
* Reap the benefits of digitization independent of an internet connection. Bandwidth costs and scenarios with limited or intermittent connectivity are no longer obstacles.
* Provide greater fault tolerance and resiliency.

Just imagine what else you can do … and all of this while using fewer resources and making the digitization as sustainable as possible.

There is also a silver lining in terms of development: New solutions in the edge computing space aim to deliver core infrastructure software to developers, allowing them to easily manage edge data on the edge. So-called edge database management systems (or edge databases) provide the fundamental capabilities for making decentralized edge data usable outside of traditional data centers and public cloud environments. They take care of collecting, retrieving, storing, distributing and governing data within the decentralized/distributed edge computing topology.

##### Last but not least: Inefficient data architectures hurt the planet!

Already feeling the drastic effect of our actions on the planet, we cannot wait any longer before starting to embed the sustainable mindset into everything we do. Making the investment into carefully chosen data architectures including the edge computing topology will prove to accomplish a lot more than just lowering your carbon emissions. Choosing a fitting and efficient data architecture will also pay off economically and have a positive social impact.

###### Economical

Cloud waste is generally defined as unused or underutilized cloud services (e.g. idle VMs, over-provisioning). And while estimates vary, between 30% and 50% of cloud spending is literally wasteful — wasting not only CO2 but money. For example, Andreessen Horowitz recently estimated that across the top 50 public companies, $100 billion is lost in market value due to cloud waste. However, that is only looking at it from one side of the coin. The cloud also encourages wasteful development behavior and data architecture: A lot of data is needlessly transferred to the cloud and back, while it is really primarily used and useful on the edge. From an unnecessary cloud setup for decentralized cases to ignoring CPU and memory consumption of the code to inefficient data management (e.g. unnecessary data streaming, repeat transferals, full dumps) — it all increases ongoing costs and CO2 emissions.

###### Environmental

Did you know that cloud data centers already use 2%-3% of the world’s electricity? They, therefore, contribute to 2%-3% of the world’s CO2 emissions. Additionally, with ongoing digitization, a rapidly soaring number of devices, and exponentially growing data volumes, the CO2 impact of digitization is growing. Therefore, the potential global impact of more sustainable digitization projects is enormous. And the greatest leverage lies in choosing efficient data architectures that avoid unnecessary and wasteful networking and cloud use.

###### Social

From a societal standpoint, edge data management solutions make it easy for developers to keep data at or close to the source, e.g. on the user’s device. Keeping data on the device increases data ownership, data privacy and data security. Individual devices can be hacked, but the potential loss is much smaller than when a massive central cloud server is corrupted, making the data of millions of users subject to compromise. A wider spectrum of data architectures and solution providers will also strengthen the ecosystem, empowering more innovations and greater independence from hyperscalers.

All in all: Sustainable digitization needs an edge.

#### 

#### TL;DR

The world is decentralized; data is generated all over the place. The dominant computing model, the cloud, is inherently centralized. It is infeasible, inefficient and unsustainable to force the decentralized world to conform to this centralized topology. This is one of the reasons why digitization is stalling. To capitalize on the value of edge data, we require a new data architecture that reflects this decentralized reality.

Edge computing is a distributed topology that brings computing and data storage closer to the edge and to data sources. But edge computing still lacks core infrastructure software to make it easy to implement edge projects. Edge databases present a silver lining empowering developers to easily manage edge data on the fly.

*Vivien Dollinger is co-founder and CEO of [ObjectBox](https://objectbox.io/)*.

**DataDecisionMakers**

Welcome to the VentureBeat community!

DataDecisionMakers is where experts, including the technical people doing data work, can share data-related insights and innovation.

If you want to read about cutting-edge ideas and up-to-date information, best practices, and the future of data and data tech, join us at DataDecisionMakers.

You might even consider [contributing an article](https://venturebeat.com/guest-posts/) of your own!

[Read More From DataDecisionMakers](https://venturebeat.com/category/DataDecisionMakers/)

 #### The AI Impact Tour Dates

 Join leaders in enterprise AI for networking, insights, and engaging conversations at the upcoming stops of our AI Impact Tour. See if we're coming to your area!
