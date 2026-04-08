# What is Digital Architecture and how to Design One

![rw-book-cover](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjyPYeVTsqT5Oq7Qy_4OZX3IzTltMd3vGiYdcRq61_oZZg0Ikh7-yiJ4gnlS-MYb9pWnJMWIQHm_EnmXva0sXbj7kcgbVstqle3VN7MaxF87Q3ejA56Oprgf7S4y85k97gZjBHqGviX0hu/w1200-h630-p-k-no-nu/digital_architectureB.png)

## Metadata
- Author: [[itarch.info]]
- Full Title: What is Digital Architecture and how to Design One
- Category: #articles
- Summary: Times have changed, not only for businesses but also for IT. Companies are not competing anymore between themselves, but are threatened nowadays more by its digital equivalents: Netflix vs Blockbusters, Amazon vs bookshops and Uber vs. Taxi companies are just a few examples.
- URL: https://www.itarch.info/2020/05/what-is-digital-architecture-and-how-to.html

## Full Document
Times have changed, not only for businesses but also for IT. Companies are not competing anymore between themselves, but are threatened nowadays more by its digital equivalents: Netflix vs Blockbusters, Amazon vs bookshops and Uber vs. Taxi companies are just a few examples. These new digital businesses have the advantage that they started building recently from scratch without legacy debt, the latter inhibiting many traditional companies to allow rapidly and smoothly transforming towards a digital business.

The only way traditional business can compete is by having an architecture that leverage their existing IT, enable a way to expand and obtain omnipresence in their sales channels and obtain better capabilities to understand and interact with their customers.

> **Digital architecture key objectives are:*** **Leverage technology debt**
> * **Enable omnipresence**
> * **Optimize client interactions**
> 

A digital architecture is the fundament on which a company can transform towards new and improved business model.

#### Traditional architecture challenges

But before we go into the details of what is and how to design a digital architecture, we need to understand what the current challenges with traditional architectures are:

###### Challenge 1: Client Perspective and Channels

Let us look first from a client perspective. In the old days in the traditional world, companies only sold through physical shops. Clients enter the shop, search for a product, pay and leave.

In the late 1990's ecommerce came alive with shops building websites to sell their products through its new digital channel. Customers enter the website, search a product, buy and wait for its delivery at home.

Over time these solutions expanded with multiple channels where clients can search the products not only on the companies' website, but also browse and buy through a mobile application or on their tablet. This multichannel architecture allows customers to do their buying within a specific channel, but not yet cross.

The next evolution step is the **omnichannel presence** where clients can interact during their buying experience through various channels transparently, such as browse a product in their mobile, look it up in the web and pay it in the shop. It does not matter if a customer stops in the middle of the process, he or she continues in another moment on another device buying the product without starting the process from the beginning.

###### Challenge 2: Integration with inflexible back-end systems and heavy front-ends

So, knowing that we need to build towards omnichannel solutions, why else do we need digital architectures? The answer lies in the current challenges companies face when trying to build a digital business:

* Companies have a **technology debt with existing back-ends**, that are expensive to upgrade and in its current state are not flexible nor scalable enough to connect with different front-end channels.

* Companies build their **"heavy" front-end applications** (such as their ecommerce website) specifically for that specific channel and was never meant to be re-used or shared with other (not yet anticipated at time of design) channels.

Let us look at the picture below to show how companies used to build their IT solutions with various channels:A traditional shop checks its ERP supply chain systems to check for its order deliveries, stocks it for display in the store and once sold, refills with new product orders. Product prices may reflect updates which are sent daily to the store from its product management system. Over time this company expands its reach with new digital channels and each channel builds its own heavy front-end application with its own business logic and the same back-end integrations: the web portal checks with ERP and product management systems for updates and orders and so does its mobile application, third party marketplaces and so on.

These vertical integrations between various back-end systems (systems of records) and different heavy front-ends for each channel (systems of engagement) end up in a classic spaghetti of connections, difficult to build and maintain.

###### Challenge 3: Understanding your customers

But there is a third challenge: the lack of understanding its customers. Most companies do not have the capability nor the information to understand better their customers. We know what the customer wants to buy, but we could improve the interaction by reviewing his or her history of interests and previous interactions to better cross- and upsell.

In some cases, the company does **not have that information nor feeds**, in other cases, it lacks the **analytical capabilities** to create those profiles, nor is that **information integrated** in its customer processes.

It is easy to see that these traditional architectures have become an inhibiting factor in transforming towards a digital business. Traditional architectures do not only slow down the agility and flexibility to expand and optimize new channels, but the maintenance of such a complex architecture will also become a subsequent heavy burden for the company without a way out. So how to improve this situation?

> **It is easy to see that traditional architectures have become an inhibiting factor in transforming towards a digital business.**

#### Digital Architecture

So, businesses need a more efficient architecture to build their digital future. To respond to those needs, a digital enterprise architecture needs to address three main enablers to build a digital business:

1. **Decouple** from **Technology Debt**
2. Enable **Omni-channel** presence
3. **Optimize customers interactions** through analytical capabilities

We will explain each enabler in the following sections.

###### 1. Decouple from Technology Debt

The first digital architecture enabler is to leverage existing legacy debt. Companies cannot change nor update their existing back-end systems easily and instead of replacing them, need to think how to re-use them without adding additional complexity. To enable connectivity with various front-end channels, we need to construct a new layer in between back-end legacy and front-end channels that optimizes the interaction in between.

> **Companies cannot replace their technology debt at once and instead of replacing it, need to think how to re-use them without adding additional complexity.**

This new layer decouples (separates in a more efficient way) back-ends and builds on top new functionalities that can be used directly in the buying processes in the front-end channels. These functionalities are called **APIs** (application programming interfaces) and they become the new channel facing side of the legacy systems.

These APIs are different than the traditional existing legacy interfaces because of two main reasons:

  

* **Functional**:  
Traditional back-ends offer limited integration with just few rough business functionalities that needs more granularity when using in digital channels. On the contrary, APIs offer "more complete" functionalities interacting and integrating with various back-ends that can be used directly in new digital processes, not only making these interfaces more re-usable for more channels, but also easier to orchestrate front-end business processes with. It is moving the heavy logic from the traditional front-ends to the API layer.  
   

 Example: a new digital API for "search product" will not only interact with the product management system, but also with inventory back-end and CRM to optimize the list of products that we want to show the client. The business logic is within the API and can be re-used by various channels, compared to a traditional solution where each channel built its own logic.
  
* **Technology**:  
Where back-ends depend on older technology standards, new APIs leverage new open web standards and protocols.   

 Example: a back-end mainframe system that only offers integration with mainframe protocol can be converted in a new "digital" API that uses open web technology protocol.

This so-called decoupling strategy is key to achieve a digital foundation for a company as it leverages existing application landscape towards a digital architecture platform without investing in replacing all back-ends.

###### 2. Enable Omni-channel Presence

Second digital architecture enabler is its omnipresence capability. This is the layer that maintains a customer session (such as login) and orchestrates the client buying process.

This layer has several elements:

* **Session management**: its main element is to maintain a consistent session management handling throughout all channels with the same customer. It needs to recognize the client who searched on the web or reacted to the advertisement, is the same person who then wants to buy a product. This helps to optimize client interactions and increase cross and upselling.
* **Personalization**: clients need to be able to personalize their digital experience to their own needs in look & feel, but also to their own interests. For example, a a client who is only interested in certain categories of products, is shown his or her primary interests in the top section of the page.
* **Orchestration**: this is the component that enables the flow of the business process and interaction with the client. It typically involves a 5 step process: Landing page > Search product > Register Client > Buy > Process and deliver order, but depends on specific industry. Together with session management, it enables omnichannel presence, so a customer can enter or leave any time, any place and continue.
* **Channel Management**: manages and optimizes customer experience for each channel to get a seamless, integrated, and consistent look and feel. Based on the channel, user interface parameters may change due to screen size, resolution and user interaction possibilities.
* **Digital Marketing**: enables to improve up and cross selling, not only within its own channels but also in external social media. It leverages the customer profiles that is created through the analytical capabilities to understand a so called 360 degree view of the client based on previous interactions and interests. With that client profile, it can optimize current client interactions and display better matches to customer needs. Digital marketing also targets to obtain higher search rankings through Search Engine Optimization (SEO) and leverage search engine and social media advertising with Search Engine Marketing (SEM).

###### 3. Optimize Client Interactions through analytical capabilities

The third digital architecture component is its analytical capabilities that includes three components:

* **Data Warehouse**: most companies do have a data warehouse that contains various perspectives on company corporate performance in sales, products and key indicators. Its data is uploaded from different back-ends.
* **Datalake**: a new kid on the block for most traditional companies. It is a storage for all kinds of data, not just corporate performance, but also social media feeds and other information. It is used to create a 360 view of clients to understand previous interactions and his or her social media interests. Data is stored as it comes from its back-ends, social media and external sites and analyzed when needed.
* **Analytical capabilities**: allows to create a 360 view with information from its data lake and sends the information and profile to the experience management capability so it can optimize client interaction. It also allows reporting to measure sales and channel performance.

Following diagram shows the analytical capabilities data flows and how it feeds experience management capability.

So one can see that digital architecture is not just a nice-to-have but a critical prerequisite to ensure companies can decouple their existing IT debt, create omnipresence and stronger analytical capabilities to better interact and understand their customers.

Read more about how digital architecture relate to enterprise and IT architectures and who is responsible for formulating one in the following post "[What is IT Architecture and Different Types of Architectures](https://www.itarch.info/2020/05/what-is-it-architecture-and-different.html)".

I am [**Michael Widjaja**](https://www.itarch.info/p/about-us.html), retired Partner after 25+ years consultancy with Accenture. I was leading Technology Architecture Practice within Europe till 2010 and then for Latin America. Worked with 100+ companies across the world, advising them on IT, Technology & Enterprise Architectures. Always want to make complex things look simple and therefore this Guide to Practical and Pragmatic IT Architecture Design to design IT architectures for simple as well as complex applications. Now spending time with family and co-founded [InAdvance Consulting Group](https://www.inadvancecg.com), and as its managing director, I am sitting in number of IT advisory committees and steering groups to help large companies with IT guidance. Material is free to use, but as a courtesy, please do refer [ITarch.info](https://www.itarch.info).
