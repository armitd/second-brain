# Web Application Architecture: Components, Models, and Types

![rw-book-cover](https://www.scnsoft.com/blog-pictures/web-apps/web-application-architecture-01.png)

## Metadata
- Author: [[Anastasia Yaskevich]]
- Full Title: Web Application Architecture: Components, Models, and Types
- Category: #articles
- Summary: Editor's note: The choice of web app architecture's type and component model is one of the most important yet challenging in web app development. Below, ScienceSoft gives you all necessary information for making a smart and informed decision.
- URL: https://www.scnsoft.com/software-development/web-application-architecture

## Full Document
* [Models of web app components](https://www.scnsoft.com/software-development/web-application-architecture#models-of-web-app-components)
	+ [Two+ web servers, one database](https://www.scnsoft.com/software-development/web-application-architecture#two-plus-web-servers-one-db)
	+ [Two+ web servers, two+ databases](https://www.scnsoft.com/software-development/web-application-architecture#two-plus-web-servers-two-plus-db)
	+ [Microservices and serverless](https://www.scnsoft.com/software-development/web-application-architecture#microservices-and-serverless)
* [Types of web application architecture](https://www.scnsoft.com/software-development/web-application-architecture#types-of-web-app-architecture)
	+ [Legacy HTML web app](https://www.scnsoft.com/software-development/web-application-architecture#legacy-html-web-app)
	+ [Widget web app](https://www.scnsoft.com/software-development/web-application-architecture#widget-web-app)
	+ [Single-page web app architecture](https://www.scnsoft.com/software-development/web-application-architecture#single-page-web-app-architecture)
	+ [Progressive web application architecture](https://www.scnsoft.com/software-development/web-application-architecture#progressive-web-apps)

***Editor's note:*** *The choice of web app architecture's type and component model is one of the most important yet challenging in web app development. Below, ScienceSoft gives you all necessary information for making a smart and informed decision. If you still have doubts or need professional help with implementing a web solution, feel free to contact our* *[web application development team](https://www.scnsoft.com/web-development/application)**.*

Throughout the three decades of its presence on the IT market, ScienceSoft has witnessed the slow but steady shift from the on-premises to web-based software. Despite my love and respect for on-premises software, we can’t deny the fact that today web apps are the best way of making sure your software concept reaches a wide audience and receives the return on investment it deserves.

In this article, I break down the key web development terms, tell you about the different types of web app architecture and help you choose the right one.

![Web app architecture](data:image/svg+xml;base64,CiAgICAgICAgICAgIDxzdmcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB2aWV3Qm94PScwIDAgOTAyIDUyOCc+CiAgICAgICAgICAgICAgICA8cmVjdCB3aWR0aD0nOTAyJyBoZWlnaHQ9JzUyOCcgZmlsbD0nI2YyZjJmMicvPgogICAgICAgICAgICA8L3N2Zz4KICAgICAgICA=)Web app architecture
#### Key terminology

##### Web application components

Before we start, let’s make sure we’re on the same page regarding the key technical web-related terms. Namely, the two *structural web app components* any web app consists of – **client** and **server** sides.

A **client** is a user-friendly representation of a web app’s functionality that a user interacts with. Written in HTML, JavaScript and CSS, it exists within the user’s web browser and doesn’t need any specific OS/device-related adjustments.

To build a **server** side you need [PHP](https://www.scnsoft.com/software-development/php), [Java](https://www.scnsoft.com/software-development/java), [.NET](https://www.scnsoft.com/software-development/dotnet), Python, Ruby on Rails or Node.js development skills. This side usually consists of at least two more parts: web server with app logic (or the main control center) and database (storage of all persistent data). If you **scale up** this side, it means that you increase the number of web servers and databases to boost your web app’s performance and stability.

##### Web app architecture

**Web application architecture** is a pattern of interaction between the web application components. The way this interaction is planned out determines the resilience, performance, and security of a future web application.

However, there are at least two different ways web app components can interact with each other, and the term ‘architecture’ can become ambiguous. In this article, I use the term ‘**web app** **component model**‘ to help you easily differentiate the architecture that focuses on the number of web server/database instances from the one that deals with the app logic distribution.

#### Models of web app components

ScienceSoft always reminds its customers that opting for the right web app architecture of components makes for the quality of the future web application’s performance. Let’s take a look at the pros and cons of the possible models.

##### One web server (with database)

This is the simplest and the riskiest model, where a single database is a part of the web app’s only server. If the server goes down, so does the web app. At ScienceSoft, we don’t usually suggest using this model unless your web app is a test project or private practice.

##### Two+ web servers, one database

The idea behind this model is that a webserver doesn’t have to store any data: even when it gets information from a client, the webserver processes it, writes the data to the database (located on a physically separate machine) and forgets about it.

With at least two web servers, you significantly reduce failure risks. Even if one of the web servers ever goes down, another one takes over immediately; all requests are automatically readdressed to the new server, and the web app keeps running. However, with only one database, you still have performance risks: if it crashes, the entire system will crash as well.

##### Two+ web servers, two+ databases

This model may be considered to be the most fail-proof: neither web servers nor databases have single points of failure. When our web development projects involve more than 5 web servers or databases, ScienceSoft installs *load balancers* that analyze all incoming requests and shrewdly allocate them to keep the workload under control.

Most likely, the ‘two+ database’ condition has left you wondering about the way data works in this model, and the truth is – it is yet another choice for you to make. Your ***first option*** is to store identical data on each of your database machines. Our experience shows that no more than 2 databases are usually needed in this case, since when one is down, the other can replace it, loss-free.

Your ***alternative*** is to evenly distribute data between your databases. Despite the obvious advantage of storage space saving, this option poses a risk of some data becoming temporarily unavailable in the event of a database crash. To guarantee the best web app performance, we at ScienceSoft usually combine the two approaches and replicate critical data while distributing the rest.

##### Microservices and serverless

The three models above are often referred to as ‘Monolithic’ due to the stable and rigid nature of web servers in them. Microservices and serverless architectures were invented in order to bring more agility to the web apps by simplifying upgrades and scaling. In both of these models, web servers are broken into smaller components: *‘services’* in microservices and *‘functions’* (small pieces of code that services consist of) in serverless. Each of these small components exists in a separate container and is treated independently, which makes it easier to modify or scale it.

At ScienceSoft, we see great business opportunities in these architectural models since - as one of our [microservices project](https://www.scnsoft.com/case-studies/java-backend-for-an-innovative-hotel-self-service-app) proved - they are cheaper to maintain and allow faster time to market. However, due to the increased interaction between multiple components, microservices and serverless web apps can offer poorer performance and pose security risks when implemented incorrectly.

Not Sure What Architecture Your Web App Needs?

Our team plans out and develops web app architectures that guarantee stability, security and high performance of your web application.

#### Types of web application architecture

As we always remind our clients, regardless of the model, all web application components work to create an integral web app. Depending on how the app logic is distributed among the client and server sides, there can be various types of web application architecture. Now, let’s look at what each of them can offer to your business.

##### Legacy HTML web app

According to the very basic web app architecture, a server, consisting of *web page construction logic* and *business logic* interacts with a client by sending out a complete HTML page. To see an update, the user needs to fully reload the page or, in other words, to have the client send a request for an HTML page to the server and load its entire code once again. Have a look at this type’s web application architecture diagram below.

![Legacy HTML web app architecture diagram](data:image/svg+xml;base64,CiAgICAgICAgICAgIDxzdmcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB2aWV3Qm94PScwIDAgOTAyIDUxMSc+CiAgICAgICAgICAgICAgICA8cmVjdCB3aWR0aD0nOTAyJyBoZWlnaHQ9JzUxMScgZmlsbD0nI2YyZjJmMicvPgogICAgICAgICAgICA8L3N2Zz4KICAgICAgICA=)Legacy HTML web app architecture diagram
This architecture type is highly secure, since all the logics and data are stored on the server, and the user doesn’t have any access to it. However, due to constant content reload and heavy data exchange, it is more common for static websites that are steadily dying out and making way to more agile and interactive web app types.

##### Widget web app

In this type, the *web page construction* logic is replaced by *web services,* and each page on the client has separate entities called *widgets*. By sending AJAX queries to web services, widgets can receive chunks of data in HTML or JSON and display them without reloading the entire page.

With real-time widget updates, this type is more dynamic, mobile-friendly and almost as popular among our clients as the next type. However, we always remind about these apps’ diminished security due to the app logic partially shifted to the exposed client side. And from ScienceSoft’s experience, this web application architecture requires the longest development time.

##### Single-page web app architecture

With single-page applications (SPAs), you only download a single web page once. On the client side, this page has a JavaScript layer that can freely communicate with web services on the server and, using the data from web services, make real-time updates to itself. The way it works is shown on the web app architecture diagram below:

Chunks of data transferred from the server to the client here are minimal, especially compared to the first type. We consider this web app type to be very agile, responsive, and lightweight, which makes it easy to transform this type of a web app into a hybrid mobile app with the help of such ‘wrappers’ as Cordova/PhoneGap.

##### Progressive web app architecture

Progressive web apps can be described as SPAs that introduce additional features, such as increased performance speed, push notifications, offline functionality, and home-screen installation. As you may have noticed, most of these features aim at improving web apps’ usability on mobile devices, and that’s exactly why we at ScienceSoft believe that PWAs are here to stay.

#### Make a Wise Choice

When making the choice of a web app architecture, be sure to take a close look at your business needs and evaluate all possible options. If you're still on the fence and need more information to make the right choice, don’t hesitate to [reach out to ScienceSoft](https://www.scnsoft.com/blog/web-application-architecture/contact-us-web-app-architecture) and request for our web development team's consultation.

    [Web Application Development](https://www.scnsoft.com/web-development/application)  Ready to upgrade your current website and drive user engagement with a web application? ScienceSoft is here to help.
