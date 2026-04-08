# Techniques for visualizing application landscapes

![rw-book-cover](https://media.licdn.com/dms/image/v2/C5612AQFIE_NPjthdFw/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1639709792483?e=2147483647&v=beta&t=WSx2SfiEsZ0NhAoPr5pvJ98oDogy16TplObQgikwzeA)

## Metadata
- Author: [[Ashutosh Shashi & Market Insight Group & Varun Digital Media & Richard Cottrill & Architect & Tech. Lead & Solutions]]
- Full Title: Techniques for visualizing application landscapes
- Category: #articles
- Summary: Most organizations are blind to the composition of their digital nervous system. Here we discuss the challenges, systems and techniques required to build software landscape visualizations.
- URL: https://www.linkedin.com/pulse/techniques-visualizing-application-landscapes-mark-crawshaw

## Full Document
Most organizations are blind to the composition of their digital nervous system. Here we discuss the challenges, systems and techniques required to build software landscape visualizations.

#### 
Introduction

Have you come across the need to visualize a large proportion or even your entire organization’s software landscape? Maybe to show the impact of a business transformation or even as an ongoing reference for other architects and engineers? Whatever the reason, many architects are seeking better techniques for visualizing software at scale.

Large-scale software landscape diagrams present a range of challenges compared with their small-scale counterparts. Poor methods can require considerable human effort, may have limited ongoing reuse and rather than help an audience understand a problem can instead lead to fear and confusion. Apart from scaring your audience away from your current state architecture, these visualizations have little use.

It is possible to visualize massive software ecosystems with little manual effort and in a way that considerably broadens who can understand your architecture. This article will explain the challenges, general systems, and specific rendering techniques that are required.

#### 
Scope

To be a little more specific, we are seeking to visualize the enterprise-wide logical software architecture, including:

* Applications/systems/micro-services
* Application groupings (e.g. ownership or capability model)
* Integrations or data flows between applications
* Components that support applications and integrations
* Cross-cutting concerns (e.g. lifecycle status or project scope)

Let’s use the term “software landscape” rather than “application landscape” as we would like to include the software used to integrate the applications. While it is common for landscape visualizations to exclude integrations for simplicity, it comes at the cost of accuracy since so much of an organization’s custom code is integration code.

#### 
Scale changes everything

As architects, we design many software architecture visualizations. The most common are those developed as part of change initiatives to communicate design decisions to engineers. Often they include a handful of systems, represent a mix of as-built/as-planned states, and are designed for a highly technical audience to consume. Unfortunately, regardless of the effort involved, it is rare for such visualizations to see the light after a project is complete. For this article, let’s refer to these as software system visualizations.

In comparison, software landscape visualizations are about the bigger picture, the system of systems. As a result, they often include many applications that wouldn’t be on the same page if they weren’t part of the same organization.

Landscape software visualizations are different because they must cope with a significantly larger scale and broader audience. For this reason, we cannot leverage the techniques available from system visualization. For example, imagine if the building industry leveraged visualization techniques between a building’s architectural plans with how that building was represented on a geographic map.

#### 
Challenges of scale

Before we dive into the details of what line drawing strategy we should use, let’s consider the broad challenges faced when visualizing an entire organization’s software landscape. These challenges don’t just relate to visualization; we must also consider how to collect the backing data and, once visualized, how we might publish to different audiences.

* How do we catalogue systems and keep the data up-to-date?
* How do we ensure our data is visualization ready?
* We won’t cover this here; subscribe to our blog for a future article.

* How do we render such large datasets to screen?
* How do we avoid spaghetti diagrams?
* How do we navigate around hundreds or thousands of systems?
* How do we keep the visualization in sync when the underlying data changes?
* Visualization is the main focus of this article, leading up to a discussion of software mapping.

* How do we reuse the visualization without significant effort?
* How do we convey information to different audiences?
* How do we present our visualizations to improve our ability to sell internally?
* We won’t cover this here; subscribe to our blog for a future article.

These challenges form a data pipeline; from the metadata source, to visualization, to a particular audience’s final consumption.

#### 
General visualization systems

There are various systems and standards for visualizing software landscapes, from whiteboards to advanced architecture tools. Here, we will compare some common methods used for visualizing large-scale software landscapes. The lens we will put on these methods is around their ability to seamlessly abstract scale. Please note that all these methods have benefits, especially when they are data-driven and cheap to generate.

Geographic maps are simpler and more intuitive when presented as part of an online mapping tool (like Google Maps) than in a 1000 page street directory. These online maps (or dynamic, multi-scale maps) present a range of benefits over building a massive unscalable map, or splitting your map into arbitrary smaller maps (like a street atlas with a grid index).

The most important thing to note, regardless of what is being mapped, is that the overall goal of any information visualization is to improve human cognition. Within information visualization, the study of graph drawing provides the best fit for the interconnected model of software landscapes.

#### 
Automation and consistency

Before discussing the primitives of graphs, we need to discuss who/what will be doing the work, both the initial build and the ongoing maintenance. We have three options:

Unless your organization is small, manual visualizations are not sufficiently scalable. When manually maintained, regardless of how amazing they are on day one, visualizations are at the mercy of effort available to keep them up-to-date. When they inevitably do fall out of date, people start to lose trust and consumption drops.

The downside of automatic maintenance (option 2) is that a small change to the backing data might completely change the visualization. If the visualization changes enough, our audience will need to spend significant mental effort to reprocess our visualization.

On the other hand, stateful maintenance (option 3) ensures consistency over time. This is where a software architecture diagram becomes a software map. The consistent shape of application groups and even the whitespace between them becomes meaningful to the viewer over time. The end result: each time our audience is reacquainted with our visualization, they will spend less time processing it, and more time listening to the point we are trying to convey.

#### 
Graph rendering techniques

Ok, let’s take the best of what we discussed above and delve into the specifics of rendering large-scale, interactive, auto-generated network graphs (a.k.a. software map).

##### #0 Network graph primitives

First, let’s define some primitives that are common to any network graph.

##### #1 Positioning vertices (nodes/applications)

At scale, how we draw any individual node isn’t as critical as where we position them. A sound system for positioning can greatly assist comprehension and navigation. There are two general techniques commonly available. Node-based positioning ignores the interconnectivity between systems and instead uses a common attribute across nodes for grouping (e.g. ownership). Edge-based positioning uses interconnectivity between nodes to decide how close a node should be from another node.

Some techniques (like interface and wheel) are useful for navigation (e.g. when you hover on a node it shows connected nodes), but provide no value in the overall comprehension of the landscape. While others (like ownership grouping) provide assistance with overall comprehension (e.g. scale of different ownership groups), but do not provide the ability to navigate connections.

We find that a combination of edge-based and node-based positioning provides the best result. By balancing the strength of both options as well as a repelling force between nodes, we gain the advantages of both systems.

##### #2 Drawing edges (lines/integrations)

Drawing lines between nodes at scale is a challenging task. It often turns what might have been a helpful visualization into a spaghetti mess, often scaring even architects away. There is no perfect solution for managing thousands of lines on a diagram, but some strategies are better than others.

Though edges might influence node position, we generally draw nodes first, then decide on a route for the edges. We have two options:

1. Free-form (straight, orthogonal, curved)
2. Grid (square, hex)

Free-form lines are very difficult to comprehend at scale. When too many lines travel on too many angles, our minds often scream “mess, avert my eyes!”, rather than making any meaningful interpretation. By tying edges to a grid, we can reduce the directions lines can traverse to 4 or 6 angles (square or hex grids, respectively). This is used to great effect in public transport maps.

When drawing on a grid, we must decide how to deal with lines that take part or all of the same grid paths with another line. There are two options here:

Either option has advantages and disadvantages. Option 1 is arguably simpler to implement, while option 2 provides a better sense of scale when many edges are travelling in the same direction (as above).

##### #3 Drawing symbols (icons/text)

Finally, we need to annotate the other primitives with helpful information. There are a range of challenges here:

* Symbols must stay readable as we zoom out
* Symbols may need to be excluded as we zoom out
* Symbols may overlap as we zoom out

We find the best solution to these challenges is to use a zoom-dependant dynamic styling system. Known as multi-scale maps, they can filter symbols based on zoom level or provide a function to continuously alter a symbol based on the zoom level.

##### #4 Layering & data overlays

It is worth thinking of your visualization as a series of overlapping layers. Some layers are part of your “base” visualization, while others are specific to the particular story you are telling. For example, when contrasted to geographic mapping, we can consider how weather radar or route markers layer upon a base map with cities and state boundaries.

The goal of layering is to improve reuse. This reduces both the effort the author puts into developing, and the viewer puts into understanding the software landscape.

#### 
Conclusion

However you choose to accomplish the task, we hope this article helped. The rewards of building a comprehensive and comprehensible software map for your organization can be significant. As architects, our role is not just about making decisions but also ensuring our stakeholders are well informed enough to come on the journey with us.

#### 
How can software mapping help?

At Aplas, we provide an end-to-end platform for visualizing your software landscape. This includes, automated collection of software asset metadata, a unique software mapping capability, and a multi-interface publication system. To view some published interfaces, visit aplas.com/acme. For an online walkthrough, book a demo. If you’d like to give it a try now, you can sign up for a 30-day trial.

##### Have we missed something?

Is there something we have missed here? Please reach out and let us know.

This article was originally published at https://aplas.com/blog/techniques-for-visualizing-application-landscapes
