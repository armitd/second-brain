# What are components to build modern web app? - Quora

![rw-book-cover](https://qsf.cf2.quoracdn.net/-4-images.share_default_image.png-26-2f12660e125b218f.png)

## Metadata
- Author: [[Quora]]
- Full Title: What are components to build modern web app? - Quora
- Category: #articles
- Summary: Answer (1 of 3): Modern web apps can come in two forms - server-side rendered web application and a single-page web application (SPA).

Let’s first discuss the main components:

 * Database - A database is the central data repository which represents the global state of your web application. Web ...
- URL: https://www.quora.com/What-are-components-to-build-modern-web-app

## Full Document
![Profile photo for Assistant](https://qsf.fs.quoracdn.net/-4-ans_frontend_assets.images.poe.multibot_app_icon_small.png-26-19d3ce9935f40287.png)
Assistant

Bot

·

Aug 17

Building a modern web application typically involves several key components and technologies. Here’s a breakdown:

1. Frontend Development

* HTML/CSS: The foundational markup and styling languages for structuring and designing web pages.
* JavaScript: The primary programming language for adding interactivity to web pages.
* Frameworks/Libraries:
+ React: A library for building user interfaces, particularly single-page applications (SPAs).
+ Vue.js: A progressive framework for building UIs and SPAs.
+ Angular: A platform for building mobile and desktop web applications.

* State Management: Tools like Redux or Vuex to

Building a modern web application typically involves several key components and technologies. Here’s a breakdown:

1. Frontend Development

* HTML/CSS: The foundational markup and styling languages for structuring and designing web pages.
* JavaScript: The primary programming language for adding interactivity to web pages.
* Frameworks/Libraries:
+ React: A library for building user interfaces, particularly single-page applications (SPAs).
+ Vue.js: A progressive framework for building UIs and SPAs.
+ Angular: A platform for building mobile and desktop web applications.

* State Management: Tools like Redux or Vuex to manage application state in a predictable way.
* CSS Preprocessors: Tools like SASS or LESS for more powerful styling capabilities.

2. Backend Development

* Programming Languages:
+ JavaScript (Node.js): For server-side development.
+ Python (Django/Flask): For rapid development and clean design.
+ Ruby (Ruby on Rails): For convention over configuration.
+ Java (Spring): For enterprise-level applications.
+ PHP: Commonly used for web development.

* Frameworks: Frameworks that simplify server-side development, like Express.js for Node.js, Django for Python, etc.

3. Database

* Relational Databases: Such as PostgreSQL or MySQL for structured data.
* NoSQL Databases: Such as MongoDB or Firebase for unstructured data and flexibility.
* ORMs (Object-Relational Mappers): Tools like Sequelize or Hibernate to interact with databases more easily.

4. APIs

* RESTful APIs: For standard client-server communication.
* GraphQL: For more flexible data querying.
* Authentication APIs: Like OAuth or JWT for secure user authentication.

5. DevOps and Deployment

* Version Control: Git for tracking changes in the codebase.
* CI/CD Tools: Continuous integration and deployment tools like Jenkins, GitHub Actions, or Travis CI.
* Containerization: Using Docker to create isolated environments for applications.
* Cloud Services: Platforms like AWS, Google Cloud, or Azure for hosting applications.
* Web Servers: Nginx or Apache for serving web applications.

6. Testing

* Unit Testing: Frameworks like Jest or Mocha for testing individual components.
* Integration Testing: Tools like Cypress or Selenium for testing interactions between components.
* End-to-End Testing: Ensuring the entire application works as intended.

7. User Experience (UX) and Design

* Wireframing Tools: Figma, Sketch, or Adobe XD for designing UI/UX.
* Responsive Design: Ensuring the application works well on various devices using frameworks like Bootstrap or Tailwind CSS.

8. Monitoring and Analytics

* Error Tracking: Tools like Sentry or Rollbar to monitor application errors.
* Performance Monitoring: Tools like New Relic or Google Analytics to analyze user behavior and app performance.

Conclusion

Combining these components effectively allows developers to create scalable and maintainable modern web applications. The specific choice of technologies may vary based on project requirements, team expertise, and other factors.

[![Profile photo for Ron Reiter](https://qph.cf2.quoracdn.net/main-thumb-500972-50-hvlakxnvivhjlnqgzmewzyzbdgaqyjzm.jpeg)](https://www.quora.com/profile/Ron-Reiter)

[Ron Reiter](https://www.quora.com/profile/Ron-Reiter)

Computer geek · Author has 183 answers and 419.4K answer views

· [8y](https://www.quora.com/What-are-components-to-build-modern-web-app/answer/Ron-Reiter)

Originally Answered: what are components to build modern web app? ·

Modern web apps can come in two forms - server-side rendered web application and a single-page web application (SPA).

Let’s first discuss the main components:

* Database - A database is the central data repository which represents the global state of your web application. Web applications need a central data repository because of their stateless nature. However, in some cases, you can work without a database - for example building a chat server does not require a database. Common choices are MySQL and PostgreSQL for relational databases, MongoDB for a document store, and Redis for a key-value stor

Modern web apps can come in two forms - server-side rendered web application and a single-page web application (SPA).

Let’s first discuss the main components:

* Database - A database is the central data repository which represents the global state of your web application. Web applications need a central data repository because of their stateless nature. However, in some cases, you can work without a database - for example building a chat server does not require a database. Common choices are MySQL and PostgreSQL for relational databases, MongoDB for a document store, and Redis for a key-value store.
* Object-relational Mapping (ORM) - The API bindings for connecting your web server to the database. Used to be just an SQL query interface but now people realized that it makes more sense to use an ORM. An ORM maps an object-oriented class to a database table in a very convenient manner. Common choices for a Python ORM are SQLAlchemy and the Django ORM.
* Web Server - The server is responsible for receiving and processing requests from the client, which is always a web browser. The server may return either a rendered template or raw data (which means that the web server is basically an API server - and usually conforms to the REST interface which means it uses JSON for data serialization). More complicated servers support push via websockets or older push technologies and are able to push data to the web browser without the client initiating a request, just by opening a channel. The web server is also responsible for session management, authentication, authorization, etc. Common choices for a web server framework in the Python world are Flask and Django.
* Templating engine - Either the server or the client will need to render HTML which is displayed to the user. An SPA will have a client-side JavaScript templating framework loaded, and will use raw data returned from the server. A server-side rendered web application will use server-side rendering and will simply load a new page every time the server sends a new rendered HTML page to the client. For server-side, a common choice would be Jinja2. For client-side rendering, there are many choices including Handlebars, Mustache.js, Angular templating and React templating.
* Stylesheets - Sets the view configuration of the displayed HTML.
* Client-side JavaScript Framework - Client-side code may manipulate the HTML using something called the DOM bindings. In an SPA, client-side JavaScript has a crucial role in the rendering of the page. However, in server-side rendered web applications, client-side JavaScript is sometimes optional. It can still be used for creating dynamic objects such as graphs, even if the data is rendered within the page itself. For an SPA, you can use a client-side MVC framework such as Angular, React or Backbone to manage your dynamic web application, since you would need to sync both data coming in from the server with the user interface, and responding to user actions within the web browser dynamically.

I hope web applications makes more sense now.

What is your approach to custom web app development?

Why are Web Components slow to be adopted? What are their advantages?

What are the best components for creating scalable Python web applications?

How can I build a self contained web app?

What kind of web application should never be built by using Node.js?

[![Profile photo for Quora User](https://qsf.cf2.quoracdn.net/-4-images.new_grid.profile_default.png-26-688c79556f251aa0.png)](https://www.quora.com/What-are-components-to-build-modern-web-app#)

[Quora User](https://www.quora.com/What-are-components-to-build-modern-web-app#)

MBA in Rady School of Management, UC San Diego, University of California, San Diego (Graduated 2004) · Author has 255 answers and 1.1M answer views

· [6y](https://www.quora.com/What-are-the-components-needed-in-making-a-web-application/answers/87141413)

Originally Answered: [What are the components needed in making a web application?](https://www.quora.com/What-are-the-components-needed-in-making-a-web-application?no_redirect=1) ·

When we talk about components of a web application, we mean two things:

* UI/UX web application components: dashboards, notifications, activity logs, statistics, settings, and many others.
* Client and server side:
+ A client is a user-friendly representation of a web app’s functionality that a user interacts with. Developed in HTML, Javascript and CSS and existing within the user’s web browser, it doesn’t need any specific OS/device-related adjustments.
+ To build a server side you need PHP, Python, Java, Ruby on Rails, .NET or Node.js development skills. The side usually consists of at least two more pa

When we talk about components of a web application, we mean two things:

* UI/UX web application components: dashboards, notifications, activity logs, statistics, settings, and many others.
* Client and server side:
+ A client is a user-friendly representation of a web app’s functionality that a user interacts with. Developed in HTML, Javascript and CSS and existing within the user’s web browser, it doesn’t need any specific OS/device-related adjustments.
+ To build a server side you need PHP, Python, Java, Ruby on Rails, .NET or Node.js development skills. The side usually consists of at least two more parts: app logic, or the main control center, and database, where all persistent data is stored.

[![Profile photo for Kunal Vaja](https://qph.cf2.quoracdn.net/main-thumb-1425799706-50-yqmahoqgaeoomowlfnjygpmkiewxmxsw.jpeg)](https://www.quora.com/profile/Kunal-Vaja-4)

[Kunal Vaja](https://www.quora.com/profile/Kunal-Vaja-4)

Lives in N1E2M8, Canada (1992–present) · Author has 171 answers and 50.5K answer views

· [3y](https://www.quora.com/What-are-the-components-of-a-web-application/answer/Kunal-Vaja-4?no_redirect=1)

Originally Answered: [What are the components of a web application?](https://www.quora.com/What-are-the-components-of-a-web-application?no_redirect=1) ·

All web-based database applications have three essential parts: A web program (or customer), a web application server, and a database server. Web-based database applications depend on a database server, which gives the information to the application.

All web-based database applications have three essential segments: A web program (or customer), a web application server, and a database server.

Web-based database applications depend on a database server, which gives the information to the application. The database server here and there additionally gives business rationale as put away methods. Put

All web-based database applications have three essential parts: A web program (or customer), a web application server, and a database server. Web-based database applications depend on a database server, which gives the information to the application.

All web-based database applications have three essential segments: A web program (or customer), a web application server, and a database server.

Web-based database applications depend on a database server, which gives the information to the application. The database server here and there additionally gives business rationale as put away methods. Put away systems can offer huge execution benefits, particularly in a multi-layered design. Notwithstanding database servers, other undertaking data framework parts incorporate IMS databases, IBM® MQ messages, and CICS® records.

The customers handle the show rationale, which controls the manner by which clients communicate with the application. Sometimes, the customer approves client gave input. Web applications in some cases coordinate Java™ applets into the customer side rationale to further develop the show layer.

Applet

A Java program that is important for a Hypertext Markup Language (HTML) page. (HTML is the standard strategy for introducing web information to clients.) Applets work with Java-empowered programs, like Microsoft Internet Explorer; they are stacked when the HTML page is handled.

Web application servers deal with the business rationale. The business rationale, normally written in Java, upholds multitiered applications. The web application server can oversee demands from an assortment of distant customers. The web application layer may incorporate JavaServer Pages (JSP) records, Java servlets, Enterprise JavaBeans (EJB) segments, or web administrations.

JSP

An innovation that gives a predictable method to broaden web server usefulness and make dynamic web content. The web applications that you create with JSP innovation are server and stage autonomous.

Servlet

A Java program that reacts to customer demands and creates reactions powerfully.

EJB

A segment engineering for building dispersed applications with the Java programming model. Server conditional segments are reusable and give compactness across application servers.

Web administrations

Independent, particular applications that give an interface between the supplier and the shopper of application assets. You can peruse more about web benefits later in this data.

[![Profile photo for Sugandhi Saxena](https://qph.cf2.quoracdn.net/main-thumb-1625174085-50-eppihwubpveivxlfkwwbacvozvdozihh.jpeg)](https://www.quora.com/profile/Sugandhi-Saxena-2)

[Sugandhi Saxena](https://www.quora.com/profile/Sugandhi-Saxena-2)

Content Writer at Webnotics Pvt Ltd (2021–present)

· [3y](https://www.quora.com/What-are-the-components-of-a-web-application/answer/Sugandhi-Saxena-2?no_redirect=1)

Originally Answered: [What are the components of a web application?](https://www.quora.com/What-are-the-components-of-a-web-application?no_redirect=1) ·

Following are the components of a Web Application -

* UI/UX Web Application Components - This covers aspects like activity logs, dashboards, notifications, settings, analytics, and so forth. These components have nothing to do with how a web application structure operates. Instead, they are part of a web app's interface layout.
* Structural Components - The client and the server sides are a web application's two fundamental essential constituents.
* Client Component - CSS, HTML, and JS are used to construct the client part. There is no requirement for an operating system or device-related changes becau

Following are the components of a Web Application -

* UI/UX Web Application Components - This covers aspects like activity logs, dashboards, notifications, settings, analytics, and so forth. These components have nothing to do with how a web application structure operates. Instead, they are part of a web app's interface layout.
* Structural Components - The client and the server sides are a web application's two fundamental essential constituents.
* Client Component - CSS, HTML, and JS are used to construct the client part. There is no requirement for an operating system or device-related changes because it resides within the user's web browser. The client part is a depiction of the functionality of a web application with which the end-user connects.
* Server Component - The server component can be developed with one or more programming frameworks, including Java,.Net, NodeJS, PHP, Python, and Ruby on Rails. The server component is made up of at least two sections: application logic and a database. The first is the web application's central command center, while the latter is collected information.

I hope my answer to your question helps!

What web applications can be made through Node.js?

How can I build a self contained web app?

What are the simple steps to build a web app company?

How can I create a web app?

What's the easiest web app to build that you might still be able to charge for?

[![Profile photo for Rahul Panchal](https://qph.cf2.quoracdn.net/main-thumb-55782168-50-qacohtcupjcntnnrieyuvrhpolyxloxk.jpeg)](https://www.quora.com/profile/Rahul-Panchal-13)

[Rahul Panchal](https://www.quora.com/profile/Rahul-Panchal-13)

Founder at Rlogical Techsoft Pvt. Ltd. (2010–present) · Author has 396 answers and 308.2K answer views

· [2y](https://www.quora.com/What-are-the-components-of-a-web-application/answers/317916220?no_redirect=1)

Originally Answered: [What are the components of a web application?](https://www.quora.com/What-are-the-components-of-a-web-application?no_redirect=1) ·

Let’s know here components of a web application.

There are many advantages of web apps that make them such significant. Foremost of all, these apps have nothing to do with the type of device one uses or the operating system. This is why many businesses are interested in developing a web app for their business. In this context, the below abstracts throw more light on the introductory features and an analysis of overall development cost. It can be a useful reference for anyone planning to [hire web app developers](https://www.rlogical.com/hire-dedicated-developers/hire-web-app-developer/)[.](https://www.rlogical.com/hire-dedicated-developers/hire-web-app-developer/)

Data Recovery Assurance

The app should assure data recovery on those occasions when lo

Let’s know here components of a web application.

There are many advantages of web apps that make them such significant. Foremost of all, these apps have nothing to do with the type of device one uses or the operating system. This is why many businesses are interested in developing a web app for their business. In this context, the below abstracts throw more light on the introductory features and an analysis of overall development cost. It can be a useful reference for anyone planning to [hire web app developers](https://www.rlogical.com/hire-dedicated-developers/hire-web-app-developer/)[.](https://www.rlogical.com/hire-dedicated-developers/hire-web-app-developer/)

Data Recovery Assurance

The app should assure data recovery on those occasions when loss of data occurs due to some kind of technical error.

Greater Security Assurance

Web apps are such immensely popular for the incredible security it provides, thus maintaining the customer loyalty.

Competitive

The scope of offering greater creativity and facilitating better customer engagement is another fundamental yet prominent feature that one can expect with web apps.

Superior Performance

Performance is another foremost aspect one should expect with web apps. Moreover, this is one of the reasons that web apps are such widely popular.

Superior Visibility

The specialty of web apps is their ability to streamline the business process to deliver greater level perfection. Additionally, when the entire data is centralized in a single place, the business can reap the benefits of greater visibility.

24/7 Accessibility

24x7 accessibility across the device type is another key reason behind many people interested in web apps.

If you want to know more about [Overall Web App Development Costs and Introductory Features](https://www.linkedin.com/pulse/in-depth-analysis-overall-web-app-development-/) then just click into it..

[![Profile photo for Abhay Ojha](https://qph.cf2.quoracdn.net/main-thumb-1339483607-50-qprvckscjxntnoezywwmqfvwyerumcas.jpeg)](https://www.quora.com/profile/Abhay-Ojha-54)

[Abhay Ojha](https://www.quora.com/profile/Abhay-Ojha-54)

Bacheor of Technology in Computer Programming & Web Designers, Rajiv Gandhi Proudyogiki Vishwavidyalaya, Bhopal (Graduated 2024)

· [2y](https://www.quora.com/What-are-the-components-of-a-web-application/answer/Abhay-Ojha-54?no_redirect=1)

Originally Answered: [What are the components of a web application?](https://www.quora.com/What-are-the-components-of-a-web-application?no_redirect=1) ·

Web application has user interface components and structural components. The last ones are also divided into client-side and server-side.

User interface components

The user interface components stand for all the interface elements like activity logs, dashboards, notifications, settings, and more. They’re a part of the web app’s interface layout.

Structural components

Structural components consist of client and server sides:

* The client component is developed with HTML, CSS, or JavaScript. Web browsers run the code and convert it into the interface, so there is no need for an operating system adjustm

Web application has user interface components and structural components. The last ones are also divided into client-side and server-side.

User interface components

The user interface components stand for all the interface elements like activity logs, dashboards, notifications, settings, and more. They’re a part of the web app’s interface layout.

Structural components

Structural components consist of client and server sides:

* The client component is developed with HTML, CSS, or JavaScript. Web browsers run the code and convert it into the interface, so there is no need for an operating system adjustment.
* As for the server component, it’s built with Java, .Net, NodeJS, Python, and other programming languages. The server consists of two parts — app logic and database. The app logic is the control center of the web app. The database is responsible for storing the information (like your login credentials).

[![Profile photo for Soykot Ahmed](https://qph.cf2.quoracdn.net/main-thumb-2235136288-50-hpuzjxzuozhtiqqwlxahlwslofmcbqbh.jpeg)](https://www.quora.com/profile/Soykot-Ahmed-11)

[Soykot Ahmed](https://www.quora.com/profile/Soykot-Ahmed-11)

Software Sales Engineer at CodeMoly (2021–present)

· [Jun 29](https://www.quora.com/What-essential-components-are-needed-to-build-a-web-application/answer/Soykot-Ahmed-11?no_redirect=1)

Originally Answered: [What essential components are needed to build a web application?](https://www.quora.com/What-essential-components-are-needed-to-build-a-web-application?no_redirect=1) ·

1. Frontend (Client-side): The User's Experience Playground

This is the part users interact with directly. Think of it as the shop window of your web application. Here's what makes it tick:

* HTML (Hypertext Markup Language): The foundation, providing structure and content to your web pages.
* CSS (Cascading Style Sheets): The fashion designer, applying styles and making your application visually appealing and user-friendly.
* JavaScript: Adds interactivity, making your application dynamic and engaging. It's like the salesperson in your shop window, responding to user actions and creating a smooth exper

1. Frontend (Client-side): The User's Experience Playground

This is the part users interact with directly. Think of it as the shop window of your web application. Here's what makes it tick:

* HTML (Hypertext Markup Language): The foundation, providing structure and content to your web pages.
* CSS (Cascading Style Sheets): The fashion designer, applying styles and making your application visually appealing and user-friendly.
* JavaScript: Adds interactivity, making your application dynamic and engaging. It's like the salesperson in your shop window, responding to user actions and creating a smooth experience.

2. Backend (Server-side): The Engine Room

The unseen force that powers your application. Here's what happens behind the scenes:

* Server-side programming languages: These languages (like Python, Java, or PHP) handle complex tasks like data processing, business logic execution, and communication with databases.
* Web Server: Acts as the middleman, receiving user requests from the frontend, fetching data as needed, and delivering the response.
* Database: The central storage unit, housing all your application's data – think product information, user details, or order history. Choosing the right database type (relational, NoSQL, etc.) depends on your specific data needs.

3. Deployment & Infrastructure: Building the Foundation

This is where your application comes to life on the internet:

* Web Hosting: Renting space on a server to store your application's code and data. There are various options like shared hosting, cloud hosting, or dedicated servers, depending on your needs.
* Security Measures: Protecting your application and user data is paramount. This includes features like user authentication, authorization, and encryption.

Bonus: UI/UX Design - For a User Experience

While not a strictly technical component, a well-designed user interface (UI) and user experience (UX) are crucial for web application success. A user-friendly and intuitive interface keeps users engaged and coming back for more.

[![Profile photo for Manuel Valdez](https://qph.cf2.quoracdn.net/main-thumb-1060605058-50-culnbidratrxggunwkizhsjqlcigusjw.jpeg)](https://www.quora.com/profile/Manuel-Valdez-63)

[Manuel Valdez](https://www.quora.com/profile/Manuel-Valdez-63)

Former IT & Telecomunications Director at Higher Education · Author has 1.4K answers and 191.6K answer views

· [Sep 2](https://www.quora.com/What-are-the-main-components-of-a-web-application/answer/Manuel-Valdez-63?no_redirect=1)

Originally Answered: [What are the main components of a web application?](https://www.quora.com/What-are-the-main-components-of-a-web-application?no_redirect=1) ·

A website is a file storage server with a file copy service based on a tcp/ip protocol (http). Websites generally store static files. That is, web documents and mutimedia files, or any other text file. The first component is the physical server. The second component is the http service called web server. Both the service in conjunction with the web service are called web server: a web server. The third component is the site which is just a repository of documents: HTML, PDF, Word, videos, images, and so on.

In constras with FTP which need an ftp client to connect and copy files from a server to

A website is a file storage server with a file copy service based on a tcp/ip protocol (http). Websites generally store static files. That is, web documents and mutimedia files, or any other text file. The first component is the physical server. The second component is the http service called web server. Both the service in conjunction with the web service are called web server: a web server. The third component is the site which is just a repository of documents: HTML, PDF, Word, videos, images, and so on.

In constras with FTP which need an ftp client to connect and copy files from a server to a local PC, http is accessed through a browser. Browsers request files to webservers which are transfered and displayed to users. Files are layout according to the rules embedded in the web document or a companion style document (a CSS file), if the web document is an HTML file. For any file type the browser makes use of a helper pluging like a PDF reader, for example.

A web apps add dynamic functionality to websites. They not composed of static files only. Web apps include an additional component: intermediate programs to catch you requests, perform calculations, retrieve information from backend database or any other computer resource or service and compute a result which consist of a dynamically composed web document.

Suppose you go to Amazon web site. It shows a web document or web form (HTML document) which contains a search field. When you enter the name of a product and hit submit, a program is called to extract the name of your item and search for it on database and as a secretary compose a web document with your response.

In summary, a web app is a combination of static documents, intermediate programs, a document copy/transfer service (a main program called web server), and very likely a database server, and of course the storage server running the webserver. By the way, the web server and the storage can be on separate physical server.

[![Profile photo for Jebin BV](https://qph.cf2.quoracdn.net/main-thumb-54131918-50-yrbmzbekffmkbquzwmptwahsnierykmf.jpeg)](https://www.quora.com/profile/Jebin-BV)

[Jebin BV](https://www.quora.com/profile/Jebin-BV)

Developed Big scale Analytics and Messaging Apps with Javascript. · Author has 114 answers and 349.6K answer views

· [9y](https://www.quora.com/Can-you-help-me-source-the-components-I-need-to-build-this-web-app/answer/Jebin-BV)

Originally Answered: [Can you help me source the components I need to build this web app?](https://www.quora.com/Can-you-help-me-source-the-components-I-need-to-build-this-web-app?no_redirect=1) ·

I have quite a bit experience in the stack you have mentioned and so let me try to help you.

Server:  

Phpmailer for mailing the confirmation.   

A php framework that can provide you ways to build REST api. (YII, Symfony, Zend)  

Payment gateways if required. (Braintree, stripe, PayPal)

Client:  

A front-end framework to manage the UI. Backbone, react would do.   

List.js to search and sort lists if any in the client side.   

Charting library if you want to show the drivers in a map. D3.js is good choice.   

Bootstrap, MUI css frameworks for modern appealing styles and responsiveness.   

Modernizr for featur

I have quite a bit experience in the stack you have mentioned and so let me try to help you.

Server:  

Phpmailer for mailing the confirmation.   

A php framework that can provide you ways to build REST api. (YII, Symfony, Zend)  

Payment gateways if required. (Braintree, stripe, PayPal)

Client:  

A front-end framework to manage the UI. Backbone, react would do.   

List.js to search and sort lists if any in the client side.   

Charting library if you want to show the drivers in a map. D3.js is good choice.   

Bootstrap, MUI css frameworks for modern appealing styles and responsiveness.   

Modernizr for feature detection and progressive enhancement.   

Fontawesome for icon fonts.  

Noty.js for client notifications.   

Moment.js for better date handling.

[Socket.io](http://socket.io/) if you want to implement socket based client updates.

That's all I could think for now.

[![Profile photo for Martin O'Shea](https://qsf.cf2.quoracdn.net/-4-images.new_grid.profile_default.png-26-688c79556f251aa0.png)](https://www.quora.com/profile/Martin-OShea-1)

[Martin O'Shea](https://www.quora.com/profile/Martin-OShea-1)

Lives in London · Author has 2.2K answers and 3.8M answer views

· [Updated 6y](https://www.quora.com/What-are-components-to-build-modern-web-app/answer/Martin-OShea-1)

Originally Answered: what are components to build modern web app? ·

As [Silvio Pereira](https://www.quora.com/profile/Silvio-Pereira-3) has said below, there are a “lot of technologies and frameworks one can use.”

But it is useful to know something of the architecture of web applications. Although other architectures exist for peer-to-peer and streaming applications, web applications typically implement a layered architecture as follows:

![](https://qph.cf2.quoracdn.net/main-qimg-7860c44ef5d2b1e39fac7b4d39708e4e-pjlq)
Although the graphic above is primarily for the Java platform, the architecture is generic and many of the available platforms and frameworks provide variants on it. Examples of these include frameworks such as Struts, Spring MVC, Hibernate and so on.

A more recent alternative i

As [Silvio Pereira](https://www.quora.com/profile/Silvio-Pereira-3) has said below, there are a “lot of technologies and frameworks one can use.”

But it is useful to know something of the architecture of web applications. Although other architectures exist for peer-to-peer and streaming applications, web applications typically implement a layered architecture as follows:

![](https://qph.cf2.quoracdn.net/main-qimg-7860c44ef5d2b1e39fac7b4d39708e4e-pjlq)
Although the graphic above is primarily for the Java platform, the architecture is generic and many of the available platforms and frameworks provide variants on it. Examples of these include frameworks such as Struts, Spring MVC, Hibernate and so on.

A more recent alternative is the use of microservices where an application’s architecture is broken down into a set of services, as follows:

![](https://qph.cf2.quoracdn.net/main-qimg-b7b363e18f0c62a7b91018bce532c75c-pjlq)
Where each service has a narrow, focused set of responsibilities, and are independently exposed in the form of remote accessible APIs, e.g. REST, consumed using protocols such as HTTP.

An on-line shopping service could have separate microservices for user accounts, product catalogue, maintaining the shopping cart and order processing.

The Spring Boot framework is designed for this type of implementation.

[![Profile photo for Jason Kane](https://qph.cf2.quoracdn.net/main-thumb-713986-50-bcrjkzkconbberszusoifyeoflrqpiyr.jpeg)](https://www.quora.com/profile/Jason-Kane)

[Jason Kane](https://www.quora.com/profile/Jason-Kane)

Web Developer · Author has 229 answers and 763.3K answer views

· [12y](https://www.quora.com/What-are-the-pieces-that-go-together-to-make-a-web-app/answer/Jason-Kane)

Originally Answered: [What are the pieces that go together to make a web app?](https://www.quora.com/What-are-the-pieces-that-go-together-to-make-a-web-app?no_redirect=1) ·

A question drenched in new-car smell.

HTML. HTML is a markup syntax. It is interpreted by a web browser. It is intended to let a document author present their work with more structure than plain text. HTML might be used to indicate that a section of text is a paragraph or a heading.

CSS is used to give detailed instructions about how a browser should display HTML. For example you might want all those headings to be bold.

Django, Rails and Tornado are all "Web Servers". A Server is a piece of software that provides a "Service". In this case the service they provide is responding to web page

A question drenched in new-car smell.

HTML. HTML is a markup syntax. It is interpreted by a web browser. It is intended to let a document author present their work with more structure than plain text. HTML might be used to indicate that a section of text is a paragraph or a heading.

CSS is used to give detailed instructions about how a browser should display HTML. For example you might want all those headings to be bold.

Django, Rails and Tornado are all "Web Servers". A Server is a piece of software that provides a "Service". In this case the service they provide is responding to web page requests with the actual pages. This can include HTML, CSS and images.

Linux is an operating system. Windows and OS X are also operating systems. If you want a computer to be dedicated as a Web Server you can use any operating system. However there are a number of advantages to using Linux.

It doesn't actually matter if they are hosting the site themselves or are using a web hosting provider. In both cases Linux is a very common choice for the operating system.

----

Node.js is also a Web Server.

redis is a key/value database server. It provides a very specific kind of service. You store some value inside it with a key. redis.put('bob', 'this is the data I want to store'). Then later you can run redis.get('bob') and you'll get 'this is the data I want to store' as the answer.

hadoop is a system for spreading a task over multiple computers. Some kinds of problems are easy to break up into pieces. Once they are broken up you have one computer do one part while another computer does another part. hadoop is a system that makes it easier to track who is doing what and make sure all the computing resources you have are being used effectively. It also collects all the answers and returns them.

[![Profile photo for Silvio Pereira](https://qph.cf2.quoracdn.net/main-thumb-128801159-50-hjobietmtbxirnydkhcuehmvdjluhxap.jpeg)](https://www.quora.com/profile/Silvio-Pereira-3)

[Silvio Pereira](https://www.quora.com/profile/Silvio-Pereira-3)

Web/Android Developer at Crave Food Services (2017–present)

· [8y](https://www.quora.com/What-are-components-to-build-modern-web-app/answer/Silvio-Pereira-3)

Originally Answered: what are components to build modern web app? ·

When you are building a web application, there are a lot of technologies and frameworks one can use.

These frameworks have the fucntion to glue the fundamental pieces of a web application, for example, the front-end to the server (with Flask delivering a Rest API).

I can talk about Java, where you can use Spring MVC for the Rest API, Spring Security for authentication and permission layer, Spring JPA and Hibernate for database manipulation…

There are a lot of layers you can have in a web app and there will always exist lots of frameworks and technologies to help delivering and improving them.

[![Profile photo for Quora User](https://qsf.cf2.quoracdn.net/-4-images.new_grid.profile_default.png-26-688c79556f251aa0.png)](https://www.quora.com/What-are-components-to-build-modern-web-app#)

[Quora User](https://www.quora.com/What-are-components-to-build-modern-web-app#)

Entrepreneur

· [Updated 10y](https://www.quora.com/What-are-the-essential-parts-of-a-modern-web-development-stack/answers/1435606)

Related

What are the essential parts of a modern web development stack?

Modern simple web stacks are usually built as follows:

* Databases: databases are used to permanently or temporarily store data for your application. You may choose a relational database, document database, tree database, key-value database, etc. It all comes down to the type of data you need to store and the type of operations you need to make on the data.   
You'll almost always have a database, and it's fairly common to use more than one type of database in a project for different types of data.
* Backend: you'll need some backend code to serve your files and data. This can be based on various lan

Modern simple web stacks are usually built as follows:

* Databases: databases are used to permanently or temporarily store data for your application. You may choose a relational database, document database, tree database, key-value database, etc. It all comes down to the type of data you need to store and the type of operations you need to make on the data.   
You'll almost always have a database, and it's fairly common to use more than one type of database in a project for different types of data.
* Backend: you'll need some backend code to serve your files and data. This can be based on various languages: Python, Ruby, PHP, C#, Java, JavaScript, and various frameworks which usually provide some common functionality and libraries, such as: Django, Rails, Symfony, Zend, CakePHP, IgnitePHP, Play Framework, Node.js, etc. In addition, you can find libraries that perform common tasks for you in just about any language.  
In the past, almost all of the website logic & functionality were implemented on the backend. However, modern web apps are required to be very fast and responsive, and usually offer great amount of functionality on the client side - without refreshing the page. Therefore, some newer web application are lean on the backend and thick on the frontend.
* Frontend: almost always based on a combination HTML, JavaScript and CSS. Commonly, HTML usually defines the content of the page, JavaScript defines the functionality, and CSS optimally defines the style, design and layout, There are various templating engines HTML and CSS, either on the client side (the browser), or on the server side (the backend). It's mainly a matter of personal taste. There are many libraries for JavaScript as well. jQuery allows you to manipulate the page easily, Underscore allow common operations. There are libraries for just about anything. Backbone.js and Ember.js allow some sort of framework to help keep your code more organized.

Nowadays, you can mix almost any backend with with any common database, and you can use any libraries or frameworks you want in the frontend, regardless of the backend and database.  

Bottom line, this is my recommendation:

1. Choose a database based on the type of data you need to store and the type of operations you need to perform on it (table, documents, trees, pairs, etc.).
2. Choose a backend language you're most familiar with and makes you happy. It doesn't really matter. Once you choose a language, it's preferred to use a framework to avoid boilerplate code and keep things more secure and structured. Again, it's a matter of your needs and personal preference.
3. Build the frontend using HTML, JavaScript and CSS. Manipulating the HTML using JavaScript is cumbersome, so I'd recommend you to use a library like jQuery, Zepto or similar to do that. If you think you'll have several thousand lines of JS code, consider using an MVC framework like Angular.js, Backbone.js or Ember.js. If you're site is HTML or CSS heavy, consider using a HTML templating engine or a language like SASS/LESS.
4. Based on the databases and backend you've chosen, figure out what's the best place to host your app. Several common options are Heroku, Amazon EC2, Rackspace Cloud, Google AppEngine and EngineYard

Hope this answers your question.

[![Profile photo for GoHostingSite GoHostingSite](https://qsf.cf2.quoracdn.net/-4-images.new_grid.profile_default.png-26-688c79556f251aa0.png)](https://www.quora.com/profile/GoHostingSite-GoHostingSite)

[GoHostingSite GoHostingSite](https://www.quora.com/profile/GoHostingSite-GoHostingSite)

Web Development · Author has 71 answers and 25.1K answer views

· [3y](https://www.quora.com/What-are-web-application-components/answer/GoHostingSite-GoHostingSite?no_redirect=1)

Originally Answered: [What are web application components?](https://www.quora.com/What-are-web-application-components?no_redirect=1) ·

Web application components are a collection of technologies and concepts that, taken together, enable web-based applications to be built dynamically for purposes ranging from user management over content publication to data storage. They are traditionally divided into two categories: server-side framework and client-side script.

The idea behind using [baby generator free](https://www.venostech.com/best-baby-face-generator-apps-site/) frameworks is that there is an idiom "everything in its place", which can give the complicated task of maintaining a modern dynamic web site structure some order.

[![Profile photo for Ssoyuz Moitra](https://qsf.cf2.quoracdn.net/-4-images.new_grid.profile_default.png-26-688c79556f251aa0.png)](https://www.quora.com/profile/Ssoyuz-Moitra-2)

[Ssoyuz Moitra](https://www.quora.com/profile/Ssoyuz-Moitra-2)

Lives in Canada (2022–present)

· [Apr 25](https://www.quora.com/What-are-the-key-components-for-building-a-modern-user-centric-website-in-todays-dynamic-web-development-landscape/answer/Ssoyuz-Moitra-2)

Related

What are the key components for building a modern, user-centric website in today's dynamic web development landscape?

Certainly! Let's delve deeper into each key component for building a modern, user-centric website:

![](https://qph.cf2.quoracdn.net/main-qimg-6d8e39033d6d799d21e0a734cf5e2a51)
To build a website people love, make it work well on all devices, easy to navigate, and filled with helpful content. Keep it safe and add fun features like quizzes. Listen to feedback and keep improving. That way, your website will be user-friendly and effective for your business.

1. Responsive Design: In today's multi-device landscape, a responsive website is essential. This means designing and developing a site that adapts seamlessly to various screen sizes and resolutions, including smartphones, ta

Certainly! Let's delve deeper into each key component for building a modern, user-centric website:

![](https://qph.cf2.quoracdn.net/main-qimg-6d8e39033d6d799d21e0a734cf5e2a51)
To build a website people love, make it work well on all devices, easy to navigate, and filled with helpful content. Keep it safe and add fun features like quizzes. Listen to feedback and keep improving. That way, your website will be user-friendly and effective for your business.

1. Responsive Design: In today's multi-device landscape, a responsive website is essential. This means designing and developing a site that adapts seamlessly to various screen sizes and resolutions, including smartphones, tablets, laptops, and desktops. Responsive design ensures that users have a consistent and optimized experience regardless of the device they use, improving accessibility and engagement.
2. Intuitive Navigation: The navigation structure of your website should be intuitive and easy to use, allowing users to quickly find the information they're seeking. Clear and organized menus, breadcrumbs, and search functionality contribute to a smooth navigation experience. User testing and feedback can help identify areas for improvement and refine navigation elements accordingly.
3. User-Centered Content: Content is king in the digital world, and user-centric content is paramount for engaging and retaining visitors. Understand your target audience's needs, preferences, and pain points to create content that resonates with them. Utilize techniques such as personas, user journey mapping, and A/B testing to tailor content to different user segments and optimize engagement and conversions.
4. Performance Optimization: Website performance directly impacts user experience and SEO rankings. Optimize load times by compressing images, minifying code, leveraging browser caching, and utilizing content delivery networks (CDNs). Regularly monitor performance metrics using tools like Google PageSpeed Insights and GTmetrix, and address any issues to ensure a fast and seamless browsing experience.
5. Accessibility Compliance: Accessibility is a critical consideration to ensure that your website is usable by everyone, including those with disabilities. Follow WCAG (Web Content Accessibility Guidelines) standards to make your site perceivable, operable, understandable, and robust. Provide alternatives for non-text content, ensure keyboard navigation, and conduct accessibility audits to identify and address potential barriers.
6. Security Measures: Protecting user data and maintaining trust is paramount in today's digital landscape. Implement SSL/TLS encryption (HTTPS), regularly update software and plugins, and employ strong authentication methods to safeguard against security threats. Conduct security audits and vulnerability assessments to identify and mitigate risks proactively.
7. Seamless Integration: Integrating with third-party tools and platforms enhances functionality and user experience. Whether it's integrating social media feeds, payment gateways, CRM systems, or marketing automation tools, ensure seamless integration to provide users with a cohesive experience across different touchpoints.
8. Interactive Elements: Interactive elements such as forms, quizzes, calculators, and chatbots engage users and encourage interaction. Incorporate intuitive and user-friendly interfaces, provide instant feedback, and personalize interactions based on user preferences and behavior to enhance engagement and conversion rates.
9. Analytics and Tracking: Utilize web analytics tools like Google Analytics to track user behavior, monitor website performance, and gather actionable insights. Analyze metrics such as traffic sources, user demographics, and conversion rates to understand user preferences and behavior, identify areas for improvement, and optimize website performance continuously.
10. Continuous Improvement: Building a user-centric website is an ongoing process. Regularly solicit user feedback through surveys, usability testing, and user interviews to understand evolving needs and preferences. Use data-driven insights to iterate on website design, content, and functionality, ensuring that your website evolves in alignment with user expectations and industry trends.

By focusing on these detailed aspects, you can create a modern, user-centric website that not only meets users' needs but also exceeds their expectations, driving engagement, conversions, and business success in today's dynamic web development landscape.

[![Profile photo for Digital Empire ✪](https://qph.cf2.quoracdn.net/main-thumb-16800465-50-btvsizxprvlqiguoivqqfarczenskcdv.jpeg)](https://www.quora.com/profile/Digital-Empire-15)

[Digital Empire ✪](https://www.quora.com/profile/Digital-Empire-15)

Founder @ "Digital Empire", 11 Years in Digital Marketing · Author has 2.6K answers and 388.6K answer views

· [Feb 6](https://www.quora.com/What-are-three-essential-components-for-the-best-web-development-approach/answer/Digital-Empire-15)

Related

What are three essential components for the best web development approach?

In the dynamic realm of web development, devising the most effective strategy is paramount to ensure the success of your online endeavors. Having spent years in the industry, I've come to understand that the recipe for the best web development approach is a blend of precision, innovation, and adaptability.

Here, I will delineate the three essential components that lay the foundation for a stellar web development strategy:

![](https://qph.cf2.quoracdn.net/main-qimg-56cc35684a654e6d4eccf74521d1c167)
Thorough Planning

* Detailed project analysis: Commence your journey with an in-depth examination of your project's objectives, target audience, and competition. This will help yo

In the dynamic realm of web development, devising the most effective strategy is paramount to ensure the success of your online endeavors. Having spent years in the industry, I've come to understand that the recipe for the best web development approach is a blend of precision, innovation, and adaptability.

Here, I will delineate the three essential components that lay the foundation for a stellar web development strategy:

![](https://qph.cf2.quoracdn.net/main-qimg-56cc35684a654e6d4eccf74521d1c167)
Thorough Planning

* Detailed project analysis: Commence your journey with an in-depth examination of your project's objectives, target audience, and competition. This will help you formulate a clear roadmap and set achievable milestones.
* Robust project documentation: Create comprehensive project documentation outlining the scope, specifications, and timelines. This document serves as a reference point throughout development, ensuring everyone involved is on the same page.
* Scalable architecture: Craft a scalable architecture that can accommodate future growth and evolving technologies. Ensure your codebase is organized, well-documented, and adheres to best coding practices.

Cutting-Edge Technologies

* Framework selection: Choose the right web development framework that aligns with your project's requirements. Evaluate factors such as speed, security, and community support.
* Responsive design: Develop websites that are responsive across devices and screen sizes. Embrace mobile-first design principles to cater to the growing mobile user base.
* Security measures: Implement robust security protocols to safeguard against cyber threats. Regularly update libraries, plugins, and frameworks to patch vulnerabilities.

Continuous Learning and Improvement

* Agile development: Adopt an agile approach to facilitate flexibility and adaptability in your development process. Regularly review and adjust your strategy to accommodate changing business needs and market trends.
* Skill enhancement: Encourage your development team to stay updated with the latest industry trends and technologies through continuous learning. Invest in training and workshops to foster skill development.
* User feedback: Collect and analyze user feedback to make data-driven improvements. Conduct usability testing and A/B testing to optimize the user experience.

In the ever-evolving landscape of web development, a meticulous plan, advanced technologies, and a commitment to continuous improvement stand as the three pillars of a winning approach. By integrating these components into your web development strategy, you'll be well-equipped to create innovative, user-centric, and successful web applications that thrive in the digital age.

[![Profile photo for Brecht Corbeel](https://qph.cf2.quoracdn.net/main-thumb-179611577-50-kjrjhfdecvsrrogqzopgtaedcrtlqhkm.jpeg)](https://www.quora.com/profile/Brecht-Corbeel)

[Brecht Corbeel](https://www.quora.com/profile/Brecht-Corbeel)

Datamathematics and software engineering · Author has 6.5K answers and 2M answer views

· [1y](https://www.quora.com/What-are-the-fundamental-components-of-web-development-and-how-do-they-interact/answer/Brecht-Corbeel)

Related

What are the fundamental components of web development, and how do they interact?

I. The Electronic Symphony of Web Technologies

In the vast soundscape of the Internet, the triumvirate of HTML, CSS, and JavaScript resonates as the foundational symphony of web design and development. These languages play a role akin to the three oscillators in a synthesizer, each contributing their distinct sonic layers to produce an immersive web experience.

![](https://qph.cf2.quoracdn.net/main-qimg-87c2ebd31a39e191479f5cecceb35ddb)
HTML (HyperText Markup Language) creates the backbone of a website, defining the underlying structure, like a bassline laying down the steady rhythm in a piece of electronic music. The ‘bassline’ composed by HTML consists of various eleme

I. The Electronic Symphony of Web Technologies

In the vast soundscape of the Internet, the triumvirate of HTML, CSS, and JavaScript resonates as the foundational symphony of web design and development. These languages play a role akin to the three oscillators in a synthesizer, each contributing their distinct sonic layers to produce an immersive web experience.

![](https://qph.cf2.quoracdn.net/main-qimg-87c2ebd31a39e191479f5cecceb35ddb)
HTML (HyperText Markup Language) creates the backbone of a website, defining the underlying structure, like a bassline laying down the steady rhythm in a piece of electronic music. The ‘bassline’ composed by HTML consists of various elements like headers, paragraphs, lists, links, and images that construct the layout of the webpage.

Meanwhile, CSS (Cascading Style Sheets) acts as the synthesizer’s filter, modifying the look and feel of a website by applying styles to HTML elements, much like a filter shapes and enhances a soundwave to achieve a desired timbre. From typography, colors, to the positioning of elements, CSS styles the raw HTML structure into an aesthetically pleasing webpage, refining the sonic palette of our web symphony.

Finally, JavaScript enters the mix like an LFO (Low Frequency Oscillator) modulating various aspects of a soundwave. It interacts with HTML and CSS to add interactive functionality, creating a dynamic web experience. With its ability to manipulate HTML elements and CSS styles, JavaScript turns static webpages into dynamic, interactive experiences, bringing the beat to life, and making the web dance to its rhythm.

![](https://qph.cf2.quoracdn.net/main-qimg-ea73edf6d4b91835a6491636452f4846)
Amidst these oscillating waves of web technologies, the RESTful API, akin to a MIDI (Musical Instrument Digital Interface) protocol, comes into play. Just as MIDI facilitates communication among various electronic musical instruments and computer software, a RESTful (Representational State Transfer) API (Application Programming Interface) enables different software systems to interact and exchange information over the Internet, keeping the groove of our web symphony flowing seamlessly.

As we continue our exploration, we’ll dive deeper into each of these ‘synthesizer’ components and how they come together to shape the resonant landscape of the Internet.

II. HTML: Laying Down the Bassline

HTML, or HyperText Markup Language, is akin to the bassline in a piece of electronic music. Just as a bassline provides the foundational rhythm and structure for a song, HTML serves as the backbone of a website, defining its essential structure.

![](https://qph.cf2.quoracdn.net/main-qimg-4a1a7e591fa2e39c4a30fa86699237d6)
HTML consists of a series of elements or ‘notes’ that make up this web bassline. These elements, denoted by tags, define the type and function of the content they enclose, akin to how different bass notes give unique color and texture to a piece of music. From headers (represented by <h1> to <h6> tags) that bring emphasis to track titles, to paragraphs (<p> tags) which flow like the steady beats of a song, every HTML element plays a crucial part in the composition of a webpage.

Images (<img> tags) and links (<a> tags) are two key elements that give depth to this HTML bassline. Images add a visual dimension to the webpage, much like a rich bassline can bring a full-bodied sound to a track. Links, on the other hand, allow for connectivity between different webpages or sites, keeping the web rhythm interconnected and dynamic.

HTML also uses nested elements to create complex structures, akin to layering bass sounds to create intricate rhythms. For instance, an unordered list element (<ul>) can have multiple list item (<li>) elements nested within it, allowing for a multi-level, rhythmic structure on the webpage.

![](https://qph.cf2.quoracdn.net/main-qimg-ce08193ae98e4d8681ca75549a56ffbe)
The bassline laid down by HTML provides the structure and rhythm for a webpage. However, to fully realize the potential of this bassline, it needs to be shaped and enhanced. This is where CSS comes into play, acting as the filter to the HTML structure, shaping and coloring the webpage to achieve a desired aesthetic resonance.

III. CSS: Shaping the Sound with Filters

Cascading Style Sheets, or CSS, serve as the filters to our HTML bassline, sculpting and transforming the raw structure into a polished, visually pleasing webpage. Much like how a music producer uses filters to adjust and enhance the sonic characteristics of a bassline, CSS tweaks the visual attributes of HTML elements, refining the aesthetics of a webpage.

CSS works by targeting HTML elements and applying various styles to them, controlling layout properties like width, height, padding, and margin; font properties such as typeface, size, and color; and even introducing background images and colors. It manipulates the visual experience in the same way a synthesizer would shape the sound of a song.

![](https://qph.cf2.quoracdn.net/main-qimg-74e233eb190bdb61f9f5e5ac679f386a)
Think of the HTML elements as the raw bass notes, while CSS acts as the equalizer, enhancing or reducing certain frequencies, and therefore creating a more dynamic mix. For instance, you might have a paragraph of text — a steady bass rhythm. CSS would be the tool to change the rhythm’s tone, maybe adjusting the color, size, or font of the text, changing the spacing between lines, or adding a background color.

CSS also enables the creation of responsive designs that adapt to different device screen sizes, similar to how a music track might be mixed and mastered differently depending on the listening environment. This responsive design ensures a consistent user experience, just like a well-mastered track ensures a consistent listening experience whether it’s played on high-end studio monitors, a car stereo, or a pair of earbuds.

In a webpage, this layer of CSS “filtering” adds depth and diversity, creating a seamless user interface. However, for a fully immersive and interactive experience, akin to a captivating live performance, we need JavaScript to choreograph dynamic elements and user interactions on our webpage.

![](https://qph.cf2.quoracdn.net/main-qimg-8a53dad5d11a090517292acf005c80f3)
IV. JavaScript: The Rhythm of Interactivity

JavaScript enters the stage as the rhythm section in our webpage symphony, introducing a beat that adds an interactive dimension, enhancing user engagement. Like a drummer injecting dynamic changes and transitions into a piece of electronic music, JavaScript brings a webpage to life by scripting dynamic, interactive elements that respond to user inputs and actions.

This versatile language enables developers to create elements such as drop-down menus, form validations, interactive maps, animated graphics, and many other user-friendly features. Think of these elements as rhythmic variations in a song — an unexpected drum fill or a shifting tempo — that keep the listener engaged and invested.

![](https://qph.cf2.quoracdn.net/main-qimg-c939a074fdefcd16fd05af6c31c0ea86)
In the same vein as a sequencer controlling the flow and structure of a song, JavaScript manages events on a webpage. Events such as clicking a button, submitting a form, or even just moving the mouse can trigger JavaScript code. The language listens for these events, and when they occur, it responds with pre-defined functions, akin to a triggered sample or sound effect in a song.

Beyond the client-side, JavaScript also powers server-side programming, thanks to environments like Node.js. This capability is akin to a DJ using the same equipment to create a song in a studio and also play it live, adjusting on-the-fly based on the audience’s response. This server-side programming allows for features like real-time updates and data persistence, essential for today’s interactive and dynamic web applications.

However, to fully embrace the web’s potential, our symphony needs one more instrument — a tool that allows our webpage to communicate with servers and databases, retrieve data, and update the page without needing a refresh. That’s where RESTful APIs come in, acting as a MIDI controller, bridging our JavaScript sequencer with external sound modules, or in this case, servers and databases.

![](https://qph.cf2.quoracdn.net/main-qimg-4f965a9cd510f7324b1280d75959fcbe)
V. RESTful APIs: The MIDI Controllers of the Web

Entering as the MIDI controller of our web symphony, RESTful APIs serve as the conductive link between our webpage and external servers and databases. Like the way MIDI controllers enable electronic musicians to interface with different sound modules, RESTful APIs allow our webpage to communicate with and access data from various web services.

REST (Representational State Transfer) is an architectural style for networked applications on the web. It provides a set of constraints that, when applied as a whole, allows for a more performant, scalable, and maintainable system. In the same vein as a MIDI controller transmitting signals based on the user’s actions, RESTful APIs send HTTP requests to servers based on user interactions and then handle the responses.

![](https://qph.cf2.quoracdn.net/main-qimg-398a573ef488cb0f5a569724b486eba0)
With RESTful APIs, JavaScript can retrieve, create, update, or delete data from a server in the background, without causing the entire page to refresh. It’s like a musician adjusting the volume, pitch, or timbre of a sound while the music continues to play, providing a seamless user experience.

GET, POST, PUT, DELETE — these HTTP methods used in REST are akin to the different types of MIDI messages — note on, note off, control change, program change, etc. Each method carries out a specific action on the server, from reading data to modifying it, providing the right beat and rhythm to our interactive webpage.

Much like how MIDI controllers can connect to various sound modules, RESTful APIs are not limited to a single server or database. This makes them a powerful tool for integrating third-party services into our webpage, such as social media feeds, weather forecasts, map services, and much more. This level of connectivity is akin to a synthesizer incorporating different sound modules, creating a rich, layered soundscape.

![](https://qph.cf2.quoracdn.net/main-qimg-c2977516b51b2961b54f5d29d05f5579)
Through RESTful APIs, our webpage becomes an interactive symphony, capable of communicating with servers and databases in a harmonious, rhythmic exchange. It forms a connection that enhances the webpage’s functionality and interactivity, playing the beat of the ever-evolving, rich, and complex world of web development.

VI. HTML, CSS, JavaScript, and RESTful APIs: The Symphony of Interactions

As we venture deeper into the intricate world of web development, it’s essential to understand the synchronicity of HTML, CSS, JavaScript, and RESTful APIs. Similar to how different instruments in a symphony work in harmony, each of these elements collaboratively shapes and breathes life into the web.

HTML, the bassline, provides the underlying structure of a webpage. It defines the various components of the webpage, such as headers, paragraphs, images, forms, and more. This is akin to establishing the melodic foundation upon which the other parts of our musical composition are built.

![](https://qph.cf2.quoracdn.net/main-qimg-ce64435791446c1a6735dbec9f6bd91f)
CSS, acting as the filter, transforms the basic structure into an engaging, aesthetically pleasing experience. It takes the HTML elements and adds color, spacing, fonts, layouts, and animations. Much like a filter adjusts the sound’s properties, such as resonance and cutoff, CSS modifies the look and feel of a webpage.

JavaScript, our choreographer, dynamically changes the HTML and CSS based on user interactions. It adds an interactive dimension that enhances user engagement by implementing functions such as slideshows, form validations, dynamic updates, and much more. In a musical analogy, JavaScript would be the conductor, directing when and how the instruments (HTML and CSS) should play.

Finally, RESTful APIs, the MIDI controllers of the web, bridge the gap between our webpage and external servers and databases. They enable our JavaScript to retrieve, create, update, or delete data in the background, without interrupting the user experience. In our symphony, the RESTful APIs are like the sound modules that the MIDI controller communicates with, extending the range of sounds and possibilities.

![](https://qph.cf2.quoracdn.net/main-qimg-74c0854032e83a3cd1e79945c4d109c4)
To illustrate these interactions, let’s consider an example. Suppose we have a music blog. The HTML sets up the structure, outlining sections for the blog posts, comments, and a form for visitors to add their own comments. CSS then styles these elements, setting a pleasing color scheme, defining typography, creating a responsive layout.

When a visitor decides to leave a comment, JavaScript steps in. It checks the form data, perhaps validates it, and then uses a RESTful API to send a POST request to the server. The server adds the comment to the database and responds, at which point JavaScript updates the webpage, adding the new comment for all to see — all without needing a page refresh. This seamless, rhythmic exchange of data between client and server enriches the webpage’s interactivity, providing a pleasing, dynamic experience for the users.

Through this intricate interplay, HTML, CSS, JavaScript, and RESTful APIs create a symphony that is the modern web — a harmonious convergence of structure, style, interactivity, and data exchange. This is the music of web development, an ever-evolving composition of technologies that brings the internet to life.

VII. The Future of Web Development: Emerging Trends and Technologies

In our journey through the symphony of web development, we’ve delved into the core components that shape and animate the internet. However, as we’ve seen, the melody of the web is never static. It continually evolves, shaped by new trends, technologies, and the ever-changing needs of users. Let’s take a look at how HTML, CSS, JavaScript, and RESTful APIs are evolving and what the future might hold for web development.

![](https://qph.cf2.quoracdn.net/main-qimg-4cc34b1178f7307c127d349ce48abac2)
HTML, while maintaining its fundamental structure, continues to evolve with each new version, offering more semantics and accessibility. The development of HTML5 saw the introduction of more semantic elements and APIs, making the web more accessible and easier to develop. Looking forward, we expect HTML to continue to expand on this path, focusing on further improving accessibility, semantics, and interoperability.

CSS, on the other hand, is growing in complexity and power. With the advent of CSS3, we saw the addition of animations, transitions, gradients, and more. More recently, CSS Grid and Flexbox have made layout design much more intuitive and responsive. The future of CSS likely holds more improvements in responsiveness, ease of use, and perhaps even more powerful animation and design capabilities.

JavaScript has arguably experienced the most dramatic evolution. From a simple scripting language for basic interactivity, JavaScript has grown into the powerhouse language of the web. The creation of Node.js, for example, extended JavaScript beyond the browser, allowing it to be used on the server side. We also see JavaScript frameworks and libraries like React, Angular, and Vue.js facilitating faster and more efficient web development. As we look to the future, JavaScript’s evolution seems to be focused on improving performance, security, and capabilities through new frameworks, libraries, and features.

![](https://qph.cf2.quoracdn.net/main-qimg-0a8a45d95d68ef0ad29d2f16c05e651c)
The REST architecture style, while still widely used, is also being complemented and in some cases replaced by newer technologies. GraphQL, for instance, is a query language developed by Facebook that provides a more efficient, powerful, and flexible alternative to REST. Similarly, gRPC, developed by Google, is a high-performance, open-source framework that supports several programming languages, making it more versatile. It’s likely we’ll see continued innovation in this space, providing developers with more efficient ways to manage data exchange between client and server.

While the fundamental melody of web development remains the same, the future promises to bring new and exciting changes to the harmony. These changes are not just about new technologies and languages; they also reflect broader shifts in how we use the web and what we expect from it. As we move forward, it’s crucial to keep an ear to the ground, listening to the changing rhythm of the web development symphony and adapting our skills and knowledge accordingly.

With that, our journey through the music of web development comes to a close. We’ve explored the symphony that is HTML, CSS, JavaScript, and RESTful APIs, and looked forward to what the future might bring. As you compose your own web development symphony, remember the interplay of these key components and the melody they create together. Keep learning, keep innovating, and most importantly, keep enjoying the music of the web.

[![Profile photo for Abu Bakar](https://qph.cf2.quoracdn.net/main-thumb-2055990161-50-ywmbziboxsdafeglljcakigcgljbvifc.jpeg)](https://www.quora.com/profile/Abu-Bakar-2456)

[Abu Bakar](https://www.quora.com/profile/Abu-Bakar-2456)

Full Stack Web Developer (2022–present)

· [Jul 1](https://www.quora.com/Can-you-explain-how-web-applications-function-and-what-elements-make-up-a-web-application/answer/Abu-Bakar-2456)

Related

Can you explain how web applications function and what elements make up a web application?

Sure! A web application is a software program that runs on a web server and is accessed through a web browser. Here’s a breakdown of how web applications function and the key elements that make up a web application:

How Web Applications Function

1. Client-Server Architecture: Web applications operate on a client-server architecture. The client (user) interacts with the application through a web browser, while the server processes requests and sends back responses.
2. Request-Response Cycle:

* Client Request: The client sends an HTTP request to the server, typically by entering a URL, clicking a link, or s

Sure! A web application is a software program that runs on a web server and is accessed through a web browser. Here’s a breakdown of how web applications function and the key elements that make up a web application:

How Web Applications Function

1. Client-Server Architecture: Web applications operate on a client-server architecture. The client (user) interacts with the application through a web browser, while the server processes requests and sends back responses.
2. Request-Response Cycle:

* Client Request: The client sends an HTTP request to the server, typically by entering a URL, clicking a link, or submitting a form.
* Server Processing: The server receives the request, processes it, and interacts with a database if necessary.
* Server Response: The server sends an HTTP response back to the client, which includes the requested data or a web page.

1. Rendering: The web browser renders the HTML, CSS, and JavaScript received from the server, displaying the web application's user interface to the user.

Key Elements of a Web Application

1.Frontend(Most Recommended):

* HTML (Hypertext Markup Language): Defines the structure and content of web pages.
* CSS (Cascading Style Sheets) or Tailwind CSS: Styles the HTML content, controlling the layout, colors, fonts, and overall appearance.
* React.js(Only Client-Side) or Next.js(Server-side and Client-Side Work): Adds interactivity and dynamic behavior to web pages. It can manipulate HTML and CSS, handle user inputs, and communicate with the server.

2.Backend:

* Server(Basic Level): Handles client requests, processes data, and serves responses. Popular server-side languages include JavaScript (Node.js), if you are become a experienced developer then Python, Ruby, PHP, and Java.
* Database(Basic Level): Stores and manages application data. Common databases include MySQL, PostgreSQL, MongoDB, and SQLite.
* Server-Side Frameworks: Facilitate the development of web applications by providing tools and libraries. Examples include Express (Node.js), Django (Python), Ruby on Rails (Ruby), and Laravel (PHP).

3.APIs (Application Programming Interfaces):

* APIs allow the web application to communicate with other services or components, either within the application or with external services. RESTful APIs and GraphQL are common methods for this communication.

4.Middleware:

* Middleware is software that sits between the client and the server, handling tasks such as authentication, logging, and data transformation.

5.Web Server:

* The web server (e.g., Apache, Nginx) handles HTTP requests from the client, routes them to the appropriate backend application, and returns the HTTP responses.

6.Security:

* Security measures protect the web application and user data from threats. This includes HTTPS, data encryption, authentication, authorization, and protection against common vulnerabilities (e.g., SQL injection, cross-site scripting).

By understanding these elements and their interactions, you can see how web applications function as cohesive systems to deliver dynamic and interactive experiences to users.

Thanks

[![Profile photo for Matt West](https://qph.cf2.quoracdn.net/main-thumb-619535591-50-jweoemrurrvfdasxqeyxdndkkctqfzzk.jpeg)](https://www.quora.com/profile/Matt-West-132)

[Matt West](https://www.quora.com/profile/Matt-West-132)

Software Engineering Manager · Author has 3.5K answers and 3.3M answer views

· [4y](https://www.quora.com/What-is-a-component-in-web-development/answer/Matt-West-132?no_redirect=1)

Related

What is a component in web development?

“Component” is a term you hear thrown around with front-end frameworks like React or Angular.

A component can basically be whatever you want it to be as a developer but it is usually a logical section of an application view (a view being a web page or section of a page.)

Components usually have everything in them that they need to run in terms of JavaScript functions, HTML, and properties. Some components even track their own state, which can be changed by user input or other events.

Components are also reusable, so in that way, they are similar to templates. For example, in Quora, you might see

“Component” is a term you hear thrown around with front-end frameworks like React or Angular.

A component can basically be whatever you want it to be as a developer but it is usually a logical section of an application view (a view being a web page or section of a page.)

Components usually have everything in them that they need to run in terms of JavaScript functions, HTML, and properties. Some components even track their own state, which can be changed by user input or other events.

Components are also reusable, so in that way, they are similar to templates. For example, in Quora, you might see multiple answers to the same question. I’d bet you five bucks that each of those answers is a component, and the only difference between them is the data being fed into them, which would include the answer text.

Those answers might also have sub-components, which would be in charge of displaying the author’s name, credential, and picture. Note: these are just guesses, I’m not a Quora developer.

Components can make it very efficient to create views for data-driven sites. Going back to the Quora example, all of the answer data that is going to be rendered on a page is probably brought in as JSON when the page is first loaded. That JSON can be fed into a simple JavaScript Array.map function, with each iteration creating a new “answer component” with the appropriate data.

I hope that helps!

[![Profile photo for Quora User](https://qsf.cf2.quoracdn.net/-4-images.new_grid.profile_default.png-26-688c79556f251aa0.png)](https://www.quora.com/What-are-components-to-build-modern-web-app#)

[Quora User](https://www.quora.com/What-are-components-to-build-modern-web-app#)

Sr. Software Engineer (1988–present) · Author has 22K answers and 8.7M answer views

· [1y](https://www.quora.com/What-are-the-essential-components-of-a-web-application/answers/1477743676455393?no_redirect=1)

Originally Answered: [What are the essential components of a web application?](https://www.quora.com/What-are-the-essential-components-of-a-web-application?no_redirect=1) ·

* server
* content

Without those, there’s nothing. That makes them essential. Anything else is ancillary.

[![Profile photo for Kanhasoft](https://qph.cf2.quoracdn.net/main-thumb-2559974696-50-npnggayztqvvbymqkxeqbavypivwjiax.jpeg)](https://www.quora.com/profile/Kanhasoft-2)

[Kanhasoft](https://www.quora.com/profile/Kanhasoft-2)

Mobile Application and Web Application Solution Developer

· [Jun 14](https://www.quora.com/How-do-you-create-a-modern-web-application/answer/Kanhasoft-2)

Related

How do you create a modern web application?

Creating a modern web application involves strategic planning, innovative design, robust development, and seamless deployment. Here’s how we approach it at our software development agency:

1. Requirement Analysis and Planning

- Gather detailed requirements through stakeholder meetings and market research.

- Define project scope and select appropriate technologies.

2. Design and Prototyping

- Develop wireframes and high-fidelity mockups for UX/UI design.

- Focus on intuitive interfaces and responsive design principles.

3. Front-End Development

- Utilize modern frameworks like React or Angular for dynam

Creating a modern web application involves strategic planning, innovative design, robust development, and seamless deployment. Here’s how we approach it at our software development agency:

1. Requirement Analysis and Planning

- Gather detailed requirements through stakeholder meetings and market research.

- Define project scope and select appropriate technologies.

2. Design and Prototyping

- Develop wireframes and high-fidelity mockups for UX/UI design.

- Focus on intuitive interfaces and responsive design principles.

3. Front-End Development

- Utilize modern frameworks like React or Angular for dynamic user interfaces.

- Optimize performance with techniques like lazy loading and code splitting.

4. Back-End Development

- Build robust server-side logic with frameworks like Node.js or Django.

- Design and implement databases and develop RESTful or GraphQL APIs.

5. Integration and Testing

- Implement CI/CD pipelines for automated testing and integration.

- Conduct rigorous manual testing to ensure functionality and user experience.

6. Deployment and Monitoring

- Deploy on cloud platforms like AWS or Azure using Docker and Kubernetes.

- Monitor performance and logs with tools like Prometheus and Grafana.

7. Maintenance and Updates

- Continuously update with new features and security patches.

- Optimize performance based on user feedback and monitoring data.

By following these steps, you can create a modern web application that excels in functionality, performance, and user experience.

Feel free to reach out if you have any questions or need assistance with your web development projects.

[![Profile photo for Airyourskills](https://qph.cf2.quoracdn.net/main-thumb-1467557141-50-dsqylckizvthamsljxhmsbvkituibpjj.jpeg)](https://www.quora.com/profile/Airyourskills)

[Airyourskills](https://www.quora.com/profile/Airyourskills)

Blogger · Author has 68 answers and 21.5K answer views

· [3y](https://www.quora.com/What-are-the-essential-parts-of-a-modern-web-development-stack/answer/Airyourskills)

Related

What are the essential parts of a modern web development stack?

CODING

All these web developers use multiple programming languages. These languages consist of various variables, syntax, and commands. Each coding language has its unique way of operating. Some of the most common coding languages embrace the following:

* HTML
* CSS
* JavaScript
* Python
* C/C++
* C#

Further, these coding languages fall into two categories, Front-end development, and Back-end development.

FRONT-END DEVELOPMENT

In the early 2000s when we used to browsed website homepages, blogs, and informative sites all we got was unorganized text without proper framing and styles.

However, there is a big improvemen

CODING

All these web developers use multiple programming languages. These languages consist of various variables, syntax, and commands. Each coding language has its unique way of operating. Some of the most common coding languages embrace the following:

* HTML
* CSS
* JavaScript
* Python
* C/C++
* C#

Further, these coding languages fall into two categories, Front-end development, and Back-end development.

FRONT-END DEVELOPMENT

In the early 2000s when we used to browsed website homepages, blogs, and informative sites all we got was unorganized text without proper framing and styles.

However, there is a big improvement than ever since as practice in HTML, CSS, and other front-end development frameworks/languages, website layouts improved impressively.

There are also responsive web pages, is the frontend developer’s job to make sure that the websites or applications work, regardless of device type and OS. To ensure the UI is functional and good-looking on a never-ending stream of desktops, mobile phones, tablets, and all manner of other web-enabled devices.

To sum up, the job of a front-end developer is to make sure that their focus is on user experience, and the technology they implement hinges on how well it'll accomplish that potency, speed, and sleek practicality.

BACK-END DEVELOPER

Back-end developer refers to the side where a website consists of a server, an application, and a database. It is a combination of both technology and programming that holds the website. It's the portion of the software package that doesn't are available direct contact with the users.

This is called the client-side of the website. Activities, like writing Apis, making libraries, and dealing with system parts while not user interfaces or perhaps systems of scientific programming, are enclosed within the backend.

To make a server, the application communicates with each other, back-end developers use languages like PHP, Ruby, Python, to build an application and tools like MySQL, Oracle, and SQL Server to search out, save, or amend knowledge and serve it to the user ahead finish code.

They come up with the most effective and efficient solutions by returning data into front-end code a user can interact with, such as: filling out a form, creating a profile, shopping online, etc.

If you want to read more about it then search for web development airyourskills and click on the first result.

[![Profile photo for Hidile Marketing](https://qph.cf2.quoracdn.net/main-thumb-937057613-50-dwdeztmmzuxwgibfrpwvfmhvwpvbgmlk.jpeg)](https://www.quora.com/profile/Hidile-Marketing)

[Hidile Marketing](https://www.quora.com/profile/Hidile-Marketing)

Information Technology

· [1y](https://www.quora.com/What-are-the-steps-and-services-needed-to-build-a-web-app/answer/Hidile-Marketing)

Related

What are the steps and services needed to build a web app?

Hello! Building a web app requires several steps and services. Here's a friendly guide to help you get started:

1. Define your concept: Start by defining your web app concept, outlining its purpose, features, and user experience.
2. Choose a tech stack: Select a tech stack that includes programming languages, frameworks, and tools that will support your app development. This may include HTML, CSS, JavaScript, React, Angular, and more.
3. Create wireframes and mockups: Design the layout and user interface of your web app using wireframes and mockups. This will help you visualize your app and make adjustmen

Hello! Building a web app requires several steps and services. Here's a friendly guide to help you get started:

1. Define your concept: Start by defining your web app concept, outlining its purpose, features, and user experience.
2. Choose a tech stack: Select a tech stack that includes programming languages, frameworks, and tools that will support your app development. This may include HTML, CSS, JavaScript, React, Angular, and more.
3. Create wireframes and mockups: Design the layout and user interface of your web app using wireframes and mockups. This will help you visualize your app and make adjustments before moving on to development.
4. Develop your app: Build your web app using your chosen tech stack, ensuring it is scalable, secure, and optimized for performance.
5. Test and debug: Test your web app thoroughly to identify and fix any bugs or errors. Conduct user testing to gather feedback and improve the user experience.
6. Deploy your app: Deploy your web app to a web server and make it accessible to users. You can use services like Amazon Web Services or Google Cloud Platform for hosting and deployment.
7. Maintain and update your app: Regularly update your web app to improve its functionality, security, and performance. You may also need to provide customer support and troubleshoot issues that arise.

Remember that building a web app is a complex process that requires expertise in web development and design. Don't be afraid to seek help from professionals or resources online, keep learning, and always focus on providing a great user experience.

If you want an experienced professional to build your Web app then Hidile is the right place for you. Hidile has 6+ yrs of experience in developing Web Apps and Mobile apps for various industries. Contact them for any assistance or enquiry.

[![Profile photo for Ankit Thakur](https://qph.cf2.quoracdn.net/main-thumb-1112775340-50-xqthyuqdguarqqvnvvyliicnfezvabqn.jpeg)](https://www.quora.com/profile/Ankit-Thakur-948)

[Ankit Thakur](https://www.quora.com/profile/Ankit-Thakur-948)

Enterprenure

· [2y](https://www.quora.com/How-do-you-create-a-modern-web-application/answer/Ankit-Thakur-948)

Related

How do you create a modern web application?

Create a Web Application That Sells

Successful web applications are applications that solve unmet needs, are easy to use and have a simple yet powerful marketing process to get people in the door. Most of the effort in creating a web application comes up front, in the development process.

Once development is complete, if your product is a success you'll be able to make a lot more money with less work than other online business models. (For example, through advertising, blogging, etc.)

Here's how to create a web application that sells.

=> Fulfill an Unmet Need

The most important thing about your web

Create a Web Application That Sells

Successful web applications are applications that solve unmet needs, are easy to use and have a simple yet powerful marketing process to get people in the door. Most of the effort in creating a web application comes up front, in the development process.

Once development is complete, if your product is a success you'll be able to make a lot more money with less work than other online business models. (For example, through advertising, blogging, etc.)

Here's how to create a web application that sells.

=> Fulfill an Unmet Need

The most important thing about your web application is that it has to fulfill an unmet need that the market truly wants.

Basecamp, for example, was the first online project management tool that was both easy to us and affordable for the small business owner. As a result, the web app has really taken off.

A good indication of whether or not a web app will be useful is to ask yourself what you would genuinely use. Founders who use their own products generally create better products and have a better chance at success.

=> Ease of Use and Minimalist on Features

Don't over develop. Don't add too many features. Products can be killed by having too many features rather than too few.

Dropbox wasn't the first to market in the online back-up industry. They overtook the industry not because they had more features, but because their proposition was simpler. They backed up everything you put in one folder on your computer, automatically, all the time. It was much easier to use than other systems with complex set-up and myriads of options that nobody understood.

Make your product easy to use. Reduce feature sets and get it down to the core of solving your user's problems.

=> Development

Development can be very easy if you already have the skills, while being tricky for an entrepreneur who isn't also a coder.

Outsourcing an integral part of your business generally isn't a good idea. If your business is a software business, don't outsource the coding of your product.

Instead, the coding is best done either by a technical co-founder or a trusted employee. You want to have a close relationship with whoever is developing your code.

=> Generating Traffic and Getting Sales

Do your round one beta testing with friends and friends of friends. This will be your ground zero ground. From there, contact high-impact individuals in the industry you serve to get the word out.

Take for example 99designs, a service that hosts design competitions amongst designers where only the winning design is selected and paid for by the client. When they first launched, nobody had heard of them, though a few people had used the concept and liked it.

By targeting key individuals in the CSS communities and design communities, the founder was quickly able to get the word out.

Experiment with PPC traffic as well as SEO traffic. Email bloggers and publishers in your space about your new product. If you're truly solving a problem, they'll want to know about it.

Also target tech-oriented sites that follow web applications. Hacker News is easy to get into, though not necessarily easy to rank for. TechCrunch is much harder to get into, but can get a lot of exposure to truly market changing applications.

Creating a web application that sells isn't easy, but can be incredibly rewarding both emotionally and financially. Most of the work is up front - once you have the product and it's taken off, you'll have a stream of income with little work that will last a long time.

[![Profile photo for Jérôme Cukier](https://qph.cf2.quoracdn.net/main-thumb-74734-50-xdljdhinhgzzxzvmumxjcagaxslwgffg.jpeg)](https://www.quora.com/profile/J%C3%A9r%C3%B4me-Cukier)

[Jérôme Cukier](https://www.quora.com/profile/J%C3%A9r%C3%B4me-Cukier)

software engineer at Uber · Author has 4.2K answers and 83.4M answer views

· [4y](https://www.quora.com/What-is-a-component-in-web-development/answer/J%C3%A9r%C3%B4me-Cukier?no_redirect=1)

Related

What is a component in web development?

A very common pattern to write web application is Model-View Controller ([Model–view–controller - Wikipedia](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)) or MVC.

In the world of MVC, the logic for an application is split into 3 parts, which are somewhat unsurprisingly called model, view and controller.

The model is where all the data is stored, and all the logic to process or transform the data.

The view is how the application is rendered. The model passes data to the view, and based on that the view knows how to generate a visual representation.

The controller is how user input is handled.

But each of these 3 parts is (typically) not a monoli

A very common pattern to write web application is Model-View Controller ([Model–view–controller - Wikipedia](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)) or MVC.

In the world of MVC, the logic for an application is split into 3 parts, which are somewhat unsurprisingly called model, view and controller.

The model is where all the data is stored, and all the logic to process or transform the data.

The view is how the application is rendered. The model passes data to the view, and based on that the view knows how to generate a visual representation.

The controller is how user input is handled.

But each of these 3 parts is (typically) not a monolithic piece of code.

The view part is made of components (here we are). Components are independent pieces of code which, when given data as input, display something as an output.

Components are designed to be reusable. For instance, let’s suppose you have many submit buttons in your application. Instead of rewriting exactly how a submit button should look like, and what it does, each time you need one, you could create a submit button component and use it each time you need one. If later, you want to change how submit buttons look in your application, you only have to make changes in one place. If you want to verify that the button functionality works, you can write unit tests for the component and opposed to test it on every page it’s used.

[![Profile photo for Stuart Green](https://qph.cf2.quoracdn.net/main-thumb-1519671786-50-nrxiteaahndfdpzjkdhiatgybztcfcsh.jpeg)](https://www.quora.com/profile/Stuart-Green-156)

[Stuart Green](https://www.quora.com/profile/Stuart-Green-156)

Business Development Manager · Author has 1.5K answers and 475.9K answer views

· [1y](https://www.quora.com/What-are-the-steps-and-services-needed-to-build-a-web-app/answer/Stuart-Green-156)

Related

What are the steps and services needed to build a web app?

Building a web app involves a series of steps and requires several services to be in place. Here is a general overview of the process:

1. Planning: Define the purpose and scope of the web app, identify the target audience, and determine the features and functionality needed to meet their needs.
2. Design: Create a wireframe and visual design for the web app. This step may include creating mockups, choosing color schemes, and selecting fonts.
3. Development: Write code for the web app, using programming languages such as HTML, CSS, JavaScript, and back-end technologies such as PHP, Python, Ruby on Rails, o

Building a web app involves a series of steps and requires several services to be in place. Here is a general overview of the process:

1. Planning: Define the purpose and scope of the web app, identify the target audience, and determine the features and functionality needed to meet their needs.
2. Design: Create a wireframe and visual design for the web app. This step may include creating mockups, choosing color schemes, and selecting fonts.
3. Development: Write code for the web app, using programming languages such as HTML, CSS, JavaScript, and back-end technologies such as PHP, Python, Ruby on Rails, or Node.js.
4. Database design: Determine the structure of the database, define tables and columns, and establish relationships between them.
5. Testing: Test the web app to ensure that it works as intended, is free of bugs, and is accessible and user-friendly.
6. Deployment: Upload the web app files to a web server and configure the server to run the app. This step may involve setting up a domain name, DNS, and SSL certificates.
7. Maintenance: Monitor the web app to ensure that it remains secure, perform regular updates to keep it up-to-date, and fix any issues that arise.

In addition to the steps above, there are several services that are often used to build a web app, such as:

* Web hosting: A service that provides a server to store the web app files and make them accessible on the internet.
* Content delivery network (CDN): A service that distributes the web app content to multiple servers around the world, improving its performance and availability.
* Cloud services: Cloud services such as AWS or Azure offer a wide range of resources and tools that can be used to build, deploy, and scale web apps.
* Version control: A service such as Git provides a way to manage and track changes to the codebase, allowing multiple developers to work on the same project.
* Analytics: A service such as Google Analytics can be used to track user behavior and gain insights into how the web app is being used.

Overall, building a web app requires careful planning, design, development, testing, and deployment, along with access to a range of services and tools to support the process.

[![Profile photo for Quora User](https://qsf.cf2.quoracdn.net/-4-images.new_grid.profile_default.png-26-688c79556f251aa0.png)](https://www.quora.com/What-are-components-to-build-modern-web-app#)

[Quora User](https://www.quora.com/What-are-components-to-build-modern-web-app#)

Programmed in a couple dozen languages for more than 30 years. · Author has 2.5K answers and 11.8M answer views

· [7y](https://www.quora.com/What-is-the-modern-way-of-creating-a-web-application/answers/37986740)

Related

What is the modern way of creating a web application?

I was going to pass on this but whatever works for you seems like the best way to do it. Lots of people start with frameworks which speed up development at the potential cost of overhead. I’m old school I have a library of my own code I’ve been building, updating and tweaking since the 90’s.

Since I wrote it all myself I use the same standards and practices on everything, it’s all modular and I can plug and play anything I’ve built in with anything else I’ve built. I use the same code over and over with added bits for the specific project and only with the “modules” that the particular project

I was going to pass on this but whatever works for you seems like the best way to do it. Lots of people start with frameworks which speed up development at the potential cost of overhead. I’m old school I have a library of my own code I’ve been building, updating and tweaking since the 90’s.

Since I wrote it all myself I use the same standards and practices on everything, it’s all modular and I can plug and play anything I’ve built in with anything else I’ve built. I use the same code over and over with added bits for the specific project and only with the “modules” that the particular project needs.

The upside is things like I haven’t written a new regex in a long time because the regex for the data I’m expecting never really changes. I’ve frequently considered moving my code base to an OO based approach but procedural code is actually more light weight and the modularity of how I implement my code “sort” of duplicates many of the benefits of OO.

[![Profile photo for Aung Thu Rha Hein](https://qph.cf2.quoracdn.net/main-thumb-5024656-50-vtononyfeayfmwpgmwlkgtbdphpdvjkz.jpeg)](https://www.quora.com/profile/Aung-Thu-Rha-Hein)

[Aung Thu Rha Hein](https://www.quora.com/profile/Aung-Thu-Rha-Hein)

SSCP, Senior Security Engineer · Author has 265 answers and 854.5K answer views

· [10y](https://www.quora.com/What-is-the-anatomy-of-a-modern-web-application/answer/Aung-Thu-Rha-Hein)

Related

What is the anatomy of a modern web application?

![](https://qph.cf2.quoracdn.net/main-qimg-a9827a8407accd815256ab5ed17f0411-pjlq)
[![Profile photo for William Teo](https://qph.cf2.quoracdn.net/main-thumb-45467535-50-uyalkqqmzougfhmntpovunzbjerdfntn.jpeg)](https://www.quora.com/profile/William-Teo-3)

[William Teo](https://www.quora.com/profile/William-Teo-3)

I do data visualization and build data analytics products · Author has 364 answers and 792.7K answer views

· [7y](https://www.quora.com/What-is-the-modern-way-of-creating-a-web-application/answer/William-Teo-3)

Related

What is the modern way of creating a web application?

Google has been pushing for the progressive web application

[[1]](https://www.quora.com/What-are-components-to-build-modern-web-app#zhYva)

for a few years already.

Pick up had been relatively slow, but I think it is the way forward and Google/Chrome has been pushing out a lot of stuff to support that - webcomponents, http2, service worker, etc.

Essentially, web app should feels as smooth as a native mobile app. Because most pple spend 80% of their time on only 3 apps on their mobile. There is little point creating more apps if they dun use or install them.

Instead, if u should overhaul ur website to be mobile friendly and progressive (fast and smooth loading ux), as such i

Footnotes

[[1]](https://www.quora.com/What-are-components-to-build-modern-web-app#cite-zhYva) [Web | Google Developers](https://developers.google.com/web/progressive-web-apps/)

Google has been pushing for the progressive web application

[[1]](https://www.quora.com/What-are-components-to-build-modern-web-app#zhYva)

for a few years already.

Pick up had been relatively slow, but I think it is the way forward and Google/Chrome has been pushing out a lot of stuff to support that - webcomponents, http2, service worker, etc.

Essentially, web app should feels as smooth as a native mobile app. Because most pple spend 80% of their time on only 3 apps on their mobile. There is little point creating more apps if they dun use or install them.

Instead, if u should overhaul ur website to be mobile friendly and progressive (fast and smooth loading ux), as such it has the exact same experience as a mobile app.

Having said that, sweltejs

[[2]](https://www.quora.com/What-are-components-to-build-modern-web-app#NjnwM)

is the most recent baby.

Footnotes

[[1]](https://www.quora.com/What-are-components-to-build-modern-web-app#cite-zhYva) [Web | Google Developers](https://developers.google.com/web/progressive-web-apps/)

[[2]](https://www.quora.com/What-are-components-to-build-modern-web-app#cite-NjnwM) [sveltejs/svelte: The magical disappearing UI framework](https://github.com/sveltejs/svelte)

[![Profile photo for Iqra Iltaf](https://qph.cf2.quoracdn.net/main-thumb-1128639466-50-ylqhpqchtdoydiceabkippvshukoztpw.jpeg)](https://www.quora.com/profile/Iqra-Iltaf-3)

[Iqra Iltaf](https://www.quora.com/profile/Iqra-Iltaf-3)

Web Developer at Fiverr (Market Place) (2022–present)

· [10mo](https://www.quora.com/What-are-the-key-components-for-building-a-modern-user-centric-website-in-todays-dynamic-web-development-landscape/answer/Iqra-Iltaf-3)

Related

What are the key components for building a modern, user-centric website in today's dynamic web development landscape?

Certainly! If you want to build a modern, user-friendly website, focus on these key components:

* Responsive Design: Ensure your site works well on all devices.
* Intuitive Navigation: Make it easy for users to find what they need.
* Compelling Visuals: Use engaging images and a consistent design.
* Fast Loading: Optimize for speed with techniques like lazy loading.
* Mobile-First Approach: Design for mobile devices first.
* SEO Optimization: Improve visibility with proper keywords and tags.
* Interactive Features: Include elements that engage users.
* Security: Protect user data with SSL certification.
* Social Media I

Certainly! If you want to build a modern, user-friendly website, focus on these key components:

* Responsive Design: Ensure your site works well on all devices.
* Intuitive Navigation: Make it easy for users to find what they need.
* Compelling Visuals: Use engaging images and a consistent design.
* Fast Loading: Optimize for speed with techniques like lazy loading.
* Mobile-First Approach: Design for mobile devices first.
* SEO Optimization: Improve visibility with proper keywords and tags.
* Interactive Features: Include elements that engage users.
* Security: Protect user data with SSL certification.
* Social Media Integration: Allow easy sharing of your content.

For expert help in dynamic website development, check out my services on [Fiverr.](https://www.fiverr.com/s/EDrN9e)

[![Profile photo for Cloud Analogy](https://qph.cf2.quoracdn.net/main-thumb-452421488-50-ijwdpyagqcsnyqucynhmgjhpvrzzecmh.jpeg)](https://www.quora.com/profile/Cloud-Analogy-1)

[Cloud Analogy](https://www.quora.com/profile/Cloud-Analogy-1)

Senior Salesforce Developer · Author has 1.1K answers and 450.3K answer views

· [3y](https://www.quora.com/What-are-Web-Components/answer/Cloud-Analogy-1)

Related

What are Web Components?

Web Components is a suite of different technologies allowing you to create reusable custom elements — with their functionality encapsulated away from the rest of your code — and utilize them in your web apps.

Concepts and Usage

As developers, we all know that reusing code as much as possible is a good idea. This has traditionally not been so easy for custom markup structures — think of the complex HTML (and associated style and script) you've sometimes had to write to render custom UI controls, and how using them multiple times can turn your page into a mess if you are not careful.

Web Components

Web Components is a suite of different technologies allowing you to create reusable custom elements — with their functionality encapsulated away from the rest of your code — and utilize them in your web apps.

Concepts and Usage

As developers, we all know that reusing code as much as possible is a good idea. This has traditionally not been so easy for custom markup structures — think of the complex HTML (and associated style and script) you've sometimes had to write to render custom UI controls, and how using them multiple times can turn your page into a mess if you are not careful.

Web Components aims to solve such problems — it consists of three main technologies, which can be used together to create versatile custom elements with encapsulated functionality that can be reused wherever you like without fear of code collisions.

* Custom elements: A set of JavaScript APIs that allow you to define custom elements and their behavior, which can then be used as desired in your user interface.
* Shadow DOM: A set of JavaScript APIs for attaching an encapsulated "shadow" DOM tree to an element — which is rendered separately from the main document DOM — and controlling associated functionality. In this way, you can keep an element's features private, so they can be scripted and styled without the fear of collision with other parts of the document.
* HTML templates: The `<template>` and `<slot>` elements enable you to write markup templates that are not displayed in the rendered page. These can then be reused multiple times as the basis of a custom element's structure.

[![Profile photo for Robin Mountford](https://qph.cf2.quoracdn.net/main-thumb-28588040-50-pfpzzsdhgyvhnkwsuwnwvegwocwxoezh.jpeg)](https://www.quora.com/profile/Robin-Mountford)

[Robin Mountford](https://www.quora.com/profile/Robin-Mountford)

Renegade Broadcast & Interactive (1996–present)

· [7y](https://www.quora.com/What-are-the-4-most-important-components-of-a-web-application-from-a-developers-perspective/answer/Robin-Mountford)

Related

What are the 4 most important components of a web application from a developer's perspective?

As a developer I would say:

1. You’re going to be building an interface and preferably not from scratch. Finding an admin theme with very little bloat is crucial to getting off the ground running. Find a theme that has starter pages that you add scripts into rather than 100s of pages you have to take script out of.
2. Your choice of a server side language is probably going to be based on what you already know. As a developer you should at some stage encourage yourself to try new things. You may find a better way to structure your code or even be introduced to a new paradigm like MVC or even using NODE

As a developer I would say:

1. You’re going to be building an interface and preferably not from scratch. Finding an admin theme with very little bloat is crucial to getting off the ground running. Find a theme that has starter pages that you add scripts into rather than 100s of pages you have to take script out of.
2. Your choice of a server side language is probably going to be based on what you already know. As a developer you should at some stage encourage yourself to try new things. You may find a better way to structure your code or even be introduced to a new paradigm like MVC or even using NODE JS over the usual .NET or PHP
3. Your choice of client side language. Are you going to render HTML on your server or are you going to rely totally on client side code to fetch your data?
4. File structure on both server and client side. If you build haphazardly adding new files as you go along without any specific methodology, you are going to have a very hard time figuring out your own code months from now and you are going to have a hard time enhancing the application at a later stage. Using a framework that forces you into a disciplined file structure will help. Something like Laravel, Codeigniter, Hapi JS on the server and Bootstrap or even a very minimal CSS starter if you are not going to be using an admin theme.

[![Profile photo for Alex Deva](https://qph.cf2.quoracdn.net/main-thumb-1157751-50-HVstEx4SrDHGpSVScnvnIi2V0MSsjMTp.jpeg)](https://www.quora.com/profile/Alex-Deva)

[Alex Deva](https://www.quora.com/profile/Alex-Deva)

has been writing code for a very long time · Author has 2.7K answers and 8.8M answer views

· [8y](https://www.quora.com/How-can-I-make-a-web-application-Please-read-the-details/answer/Alex-Deva)

Related

How can I make a web application (Please read the details)?

You don't start a web app by choosing a framework.

You start a web app by thinking about the problem it solves. Then, you think about how it solves it in a new, better way than all the other apps out there that do the same thing. Then, assuming you had answers for the above, you think about the hurdles you have to overcome to achieve that.

And only once you have a fair idea of the challenges you'll face, you investigate which language/framework is best suited to address them, from a technical or economical perspective.

As for your project, you've just described the existing, highly successful Goo

You don't start a web app by choosing a framework.

You start a web app by thinking about the problem it solves. Then, you think about how it solves it in a new, better way than all the other apps out there that do the same thing. Then, assuming you had answers for the above, you think about the hurdles you have to overcome to achieve that.

And only once you have a fair idea of the challenges you'll face, you investigate which language/framework is best suited to address them, from a technical or economical perspective.

As for your project, you've just described the existing, highly successful Goodreads.com.

If, however, you're just building something for your own entertainment, then it doesn't really matter. Pick the tools that you like best. Try a few out, it'll take you a few days. Let us know which one stuck.

[![Profile photo for Jeff Scott Ward](https://qph.cf2.quoracdn.net/main-thumb-4340615-50-geywpealqxlzqldffreptqivvcdtncgl.jpeg)](https://www.quora.com/profile/Jeff-Scott-Ward)

[Jeff Scott Ward](https://www.quora.com/profile/Jeff-Scott-Ward)

Works at Marvel Comics (company)

· [10y](https://www.quora.com/What-are-Web-Components/answer/Jeff-Scott-Ward)

Related

What are Web Components?

Web Components are meant to be encapsulated pieces of funcionality like widgets that don't need extra scoping to protect it from the global namespace/runtime.

WATCH:

READ:  

Checkout [Brick](http://mozilla.github.io/brick/) by Mozilla and [Polymer](http://www.polymer-project.org/) by Google.

[![Profile photo for Web Hosting World](https://qph.cf2.quoracdn.net/main-thumb-1723388307-50-twpgjgjtjmswusytcazzllalehzyythi.jpeg)](https://www.quora.com/profile/Web-Hosting-World-1)

[Web Hosting World](https://www.quora.com/profile/Web-Hosting-World-1)

We are a reliable company into web hosting and services · Author has 1.6K answers and 143.9K answer views

· [Mar 21](https://www.quora.com/What-are-web-components-and-how-do-they-enhance-development/answer/Web-Hosting-World-1)

Related

What are web components, and how do they enhance development?

Web components are a set of web platform APIs that allow developers to create reusable custom elements for web applications. They consist of four main technologies: Custom Elements, Shadow DOM, HTML Templates, and HTML Imports. These components can encapsulate specific functionality or design elements, making it easier to maintain and reuse code across different parts of a website.

[![Profile photo for Lightbulb Infotech](https://qph.cf2.quoracdn.net/main-thumb-2795621104-50-lkfiealvgbzihppezzlzztgvvmamgjgy.jpeg)](https://www.quora.com/profile/Lightbulb-Infotech)

[Lightbulb Infotech](https://www.quora.com/profile/Lightbulb-Infotech)

[Sep 26](https://www.quora.com/What-are-the-essential-parts-of-a-modern-web-development-stack/answer/Lightbulb-Infotech)

Related

What are the essential parts of a modern web development stack?

There are mainly three parts of web development

:1) Front-end

2) Back-end

3) full-task

- Front-end involves the design , layout and interactivity. Developers uses many languages like HTML, CSS, and JavaScript.

- The server side of a website is known as back-end which involves how the website will work. Back-end developers use server-side languages like PHP, Python and Java.

- A combination of front-end and back-end development is known as full-task.

[![Profile photo for Tinashe Matate](https://qph.cf2.quoracdn.net/main-thumb-59682497-50-guptfsxsuysukerevuffthnqqsrxxzba.jpeg)](https://www.quora.com/profile/Tinashe-Matate)

[Tinashe Matate](https://www.quora.com/profile/Tinashe-Matate)

Software Developer at Allmyhomes (2021–present)

· [7y](https://www.quora.com/What-technologies-to-use-for-building-a-web-app/answer/Tinashe-Matate)

Related

What technologies to use for building a web app?

You will need an API that gives you access to geolocations.

You may check some examples here [Discuss & share web components](https://beta.webcomponents.org/element/GoogleWebComponents/google-map/demo/demo/kml.html)

This is for the interface, the map itself. Once you have the API which allows you to pick a point on the map by clicking on it you will need a way to persist that, get the information saved somewhere durable. You may use any backend you like. Django for example may be what you need, lightweight and allows the fileupload part be done for you without much smart if you are to use the Django models.

To do the upload of photo, you can use ajax, as pointed out by others so you don

You will need an API that gives you access to geolocations.

You may check some examples here [Discuss & share web components](https://beta.webcomponents.org/element/GoogleWebComponents/google-map/demo/demo/kml.html)

This is for the interface, the map itself. Once you have the API which allows you to pick a point on the map by clicking on it you will need a way to persist that, get the information saved somewhere durable. You may use any backend you like. Django for example may be what you need, lightweight and allows the fileupload part be done for you without much smart if you are to use the Django models.

To do the upload of photo, you can use ajax, as pointed out by others so you don’t have to reload the page when form is submitted. You may like to checkout [vue.js](https://vuejs.org/). You can do interesting things with it efficiently without messing up with the DOM directly.

[![Profile photo for Rosario Rascuna](https://qsf.cf2.quoracdn.net/-4-images.new_grid.profile_default.png-26-688c79556f251aa0.png)](https://www.quora.com/profile/Rosario-Rascuna)

[Rosario Rascuna](https://www.quora.com/profile/Rosario-Rascuna)

[10y](https://www.quora.com/How-do-you-build-a-contemporary-web-page-web-app/answer/Rosario-Rascuna)

Related

How do you build a contemporary web page/web app?

You want to start learning HTML and CSS. You can do it very quickly by just saving a file.html inside a text-editor (like sublime text) and open up the file in your browser.

The good thing is that you won't need to install any software at this stage. I learnt a lot by just looking at other people pages, and trying to replicate the same HTML/CSS design.

The next step would be learning about Javascript. You can include/import javascript files and start learning how to make more interactive pages.

Ruby on Rails would be the last step. You'll see how to handle databases, how to submit forms and how

You want to start learning HTML and CSS. You can do it very quickly by just saving a file.html inside a text-editor (like sublime text) and open up the file in your browser.

The good thing is that you won't need to install any software at this stage. I learnt a lot by just looking at other people pages, and trying to replicate the same HTML/CSS design.

The next step would be learning about Javascript. You can include/import javascript files and start learning how to make more interactive pages.

Ruby on Rails would be the last step. You'll see how to handle databases, how to submit forms and how to publish your website online.

[![Profile photo for Aykut Can](https://qph.cf2.quoracdn.net/main-thumb-167069612-50-gzxidbptijtbynxepjdlcxiexhqccswk.jpeg)](https://www.quora.com/profile/Aykut-Can-1)

[Aykut Can](https://www.quora.com/profile/Aykut-Can-1)

Web / Mobile Developer

· [7y](https://www.quora.com/What-is-the-modern-way-of-creating-a-web-application/answer/Aykut-Can-1)

Related

What is the modern way of creating a web application?

* use MEAN stack.
* use some bloated javascript frameworks.
* use webpack/gulp/grunt/elixir whatever you like
* use git
* use some testing tools. Continuous integration systems. Continious deployment systems
* use containers for scaling your app, when you doesnt need to.

Do some overengineering buddy. Thats the way of 2017.

[![Profile photo for Brian Lange](https://qph.cf2.quoracdn.net/main-thumb-888155-50-pwspaogubimepvexpbulkefxcllrjodp.jpeg)](https://www.quora.com/profile/Brian-Lange)

[Brian Lange](https://www.quora.com/profile/Brian-Lange)

I design + code interactive web apps at Datascope

· [10y](https://www.quora.com/How-do-you-build-a-contemporary-web-page-web-app/answer/Brian-Lange)

Related

How do you build a contemporary web page/web app?

There are a lot of answers to this, but I'd say start with HTML and CSS- you'll be surprised how many useful things you can build just making "static" sites, and you need to know how web pages are structured before you go interacting with them via JS or writing templates in a framework.

From there, learning some Javascript will allow you to make things more interactive, and you can play around using things like HTML5 local storage or Parse before you concern yourself with learning some sort of framework/backend stack. If you haven't done any real programming before, you can get your feet wet he

There are a lot of answers to this, but I'd say start with HTML and CSS- you'll be surprised how many useful things you can build just making "static" sites, and you need to know how web pages are structured before you go interacting with them via JS or writing templates in a framework.

From there, learning some Javascript will allow you to make things more interactive, and you can play around using things like HTML5 local storage or Parse before you concern yourself with learning some sort of framework/backend stack. If you haven't done any real programming before, you can get your feet wet here and learn the basics.

Finally, when you're tired of relying on local storage or external services and you want more control, look into learning a web framework like RoR, Django or Node.

[![Profile photo for Vipin Kumar](https://qph.cf2.quoracdn.net/main-thumb-5888736-50-cfgbrtttvaqujxhiteoofgfwcnevgtyz.jpeg)](https://www.quora.com/profile/Vipin-Kumar-1)

[Vipin Kumar](https://www.quora.com/profile/Vipin-Kumar-1)

Full stack developer (2018–present)

· [7y](https://www.quora.com/What-technologies-should-I-use-for-building-a-web-app/answer/Vipin-Kumar-1?no_redirect=1)

Related

What technologies should I use for building a web app?

Here you should consider technology

1. PWA
2. Push notification
3. Node.js
4. make API
5. Redis
6. mongoDB
7. GraphSQL

these are the technology you have look once

What is your approach to custom web app development?

Why are Web Components slow to be adopted? What are their advantages?

What are the simple steps to build a web app company?

What web applications can be made through Node.js?

What are the steps and services needed to build a web app?

What's the best platform to build a web app on?

How can I build a self contained web app?

Why is JavaScript required to build web applications?

What are some simple web apps I can make or duplicate to practice web app development?

Which is the best framework or tool for designing modern look multi-module based web application?

How do I build a web app and software development?

Why is there a wide variety of web application development tools? However, they all do the same thing.

What are the benefits of custom web applications?

What is component-based web development?

What all type of developer do I need to build an web-app?

What is your approach to custom web app development?

Why are Web Components slow to be adopted? What are their advantages?

Should developers use frameworks or build from scratch for web applications?

What are the components needed in making a web application?

What is it like to build web apps with Polymer and Web Components?

What are the best components for creating scalable Python web applications?
