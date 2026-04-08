# What Are Linked Data and Linked Open Data?

![rw-book-cover](https://www.ontotext.com/wp-content/uploads/2018/02/image_200x200-1.png)

## Metadata
- Author: [[Ontotext]]
- Full Title: What Are Linked Data and Linked Open Data?
- Category: #articles
- Summary: Linked Data is a set of principles for connecting and sharing data on the Web in a way that is understandable to both humans and machines. It allows for the integration of diverse datasets through unique identifiers called URIs, and it can be enhanced when combined with Open Data, creating what is known as Linked Open Data. This combination improves data accessibility and enables richer queries and knowledge discovery.
- URL: https://www.ontotext.com/knowledgehub/fundamentals/linked-data-linked-open-data/

## Full Document
![Linked Data Prinicples](https://www.ontotext.com/wp-content/uploads/2016/06/What-are-Linked-Data-and-Linked-Open-Data.png)Linked Data Prinicples
Linked Data is one of the core pillars of the [Semantic Web](https://www.ontotext.com/knowledgehub/fundamentals/what-is-the-semantic-web/), also known as the Web of Data. The Semantic Web is about making links between datasets that are understandable not only to humans, but also to machines, and Linked Data provides the best practices for making these links possible. In other words, Linked Data is a set of design principles for sharing machine-readable interlinked data on the Web.

#### The Linked Data Rules of the Game

The more things, events, people, locations, etc. are connected together, the more powerful the Web of Data is. However, in order to link, merge and integrate huge sets of data from disparate sources, some basic guidelines must be followed.

The inventor of the World Wide Web and the creator and advocate of the Semantic Web and Linked Data, Sir Tim Berners-Lee, laid down the [four design principles](https://www.w3.org/DesignIssues/LinkedData.html) of Linked Data as early as in 2006.

##### 1. Use URIs as names for things.

The Uniform Resource Identifier (URI) is a single global identification system used for giving unique names to anything – from digital content available on the Web to real-world objects and abstract concepts. With the help of URIs, we can distinguish between different things or know that one thing from one dataset is the same as another in a different dataset.

##### 2. Use HTTP URIs so that people can look up these names.

As the HTTP protocol provides a simple mechanism for retrieving resources, when things can be identified by URIs in conjunction with this protocol, they become easier to find. This expedites publishing any kind of data and adding it to the global data space.

##### 3. When someone looks up a URI, provide useful information, using the standards (RDF, SPARQL).

To be able to use URIs efficiently, we should use [RDF](https://www.ontotext.com/knowledgehub/fundamentals/what-is-rdf-triplestore/) or [SPARQL](https://www.ontotext.com/knowledgehub/fundamentals/what-is-sparql/) for querying.

The RDF is a graph-based representation format for data publishing and interchange on the Web developed by the [W3C](https://www.w3.org/). It is also used in semantic graph databases (also known as [RDF triplestores](https://www.ontotext.com/knowledgehub/fundamentals/what-is-rdf-triplestore/)) – a technology developed for storing interconnected data and inferring new facts out of existing ones.

SPARQL, on the other hand, is the W3C-standardized query language for retrieving and manipulating data stored in RDF format. As such, it allows us to search the Web of Data (or any database) and discover relationships.

##### 4. Include links to other URIs so that they can discover more things.

Similarly to the hypertext web, links to other URIs makes data interconnected and enables us to find different things. By interlinking new information with existing resources, we maximize the reuse and interlinking among existing data and create a richly interconnected network of machine-processable meaning.

Some content could not be imported from the original document. [View content ↗](https://www.slideshare.net/slideshow/embed_code/key/K40gV5glHmIUEK) 

#### Linked Data vs. Open Data

When data can be freely used and distributed by anyone (subject only to the requirement to attribute and share-alike), it is called Open Data.

But Open Data does not equal Linked Data. Open Data can be made available to everyone without links to other data. At the same time, data can be linked without being freely available for reuse and distribution.

Therefore, the W3C community puts a lot of efforts in enriching the [Linked Open Data (LOD) cloud](http://linkeddata.org/).

#### Linked Open Data

Linked Open Data is a powerful blend of Linked Data and Open Data: it is both linked and uses open sources. One notable example of an LOD set is [DBpedia](http://wiki.dbpedia.org/) – a crowd-sourced community effort to extract structured information from Wikipedia and make it available on the Web.

A semantic graph database such as Ontotext’s [GraphDB](https://www.ontotext.com/products/graphdb/) is able to handle huge datasets coming from disparate sources and link them to Open Data. This provides richer queries, boosting untapped knowledge discovery and efficient data-driven analytics.

In 2010, Sir Tim Berners-Lee suggested a [5-star deployment scheme](https://www.ontotext.com/knowledgehub/fundamentals/five-star-linked-open-data/) for Linked Open Data. The rating begins at one star and the more proprietary formats are removed and links added, the more stars data gets.

#### The Benefits of Linked (Open) Data

To sum it up, Linked Data breaks down the information silos that exist between various formats and brings down the fences between various sources. It facilitates the extension of the data models and allows easy updates. As a result, data integration and browsing through complex data become easier and much more efficient.

In semantic graph databases, the linking of disparate sources and formats enables the [inference](https://www.ontotext.com/knowledgehub/fundamentals/what-is-inference/) of new knowledge out of existing facts. In this way, Linked Data empowers organizations to put their proprietary knowledge in the context of open-world knowledge and/or commercially specialized knowledge and enhances [cognitive and semantic technology innovation](https://www.ontotext.com/services/technology-innovation-consulting/).

**Want to learn more about how to best store and manage your Linked Open Data in an RDF triplestore like Ontotext’s GraphDB?**

|  |  |
| --- | --- |
|  | White Paper: The Truth About Triplestores The Top 8 Things You Need to Know When Considering a Triplestore  |

[schemaapprating]

###### Ontotext Newsletter
