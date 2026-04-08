# 10 Common Software Architectural Patterns in a nutshell

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1039/1*M22DR3WPqbWXWidYIq2GwA.png)

## Metadata
- Author: [[Vijini Mallawaarachchi]]
- Full Title: 10 Common Software Architectural Patterns in a nutshell
- Category: #articles
- Summary: The article discusses the importance of choosing the right software architectural patterns for designing large systems. It defines an architectural pattern as a reusable solution for common problems in software architecture. The author explains ten common patterns, including layered and client-server patterns, along with their uses, pros, and cons.
- URL: https://towardsdatascience.com/10-common-software-architectural-patterns-in-a-nutshell-a0b47a1e9013

## Full Document
Ever wondered how large enterprise scale systems are designed? Before major software development starts, we have to choose a suitable architecture that will provide us with the desired functionality and quality attributes. Hence, we should understand different architectures, before applying them to our design.

![](https://miro.medium.com/v2/resize:fit:700/1*M22DR3WPqbWXWidYIq2GwA.png)
### What is an Architectural Pattern?

According to Wikipedia,

> An **architectural pattern** is a general, reusable solution to a commonly occurring problem in software architecture within a given context. Architectural patterns are similar to software design pattern but have a broader scope.
> 
> 

In this article, I will be briefly explaining the following 10 common architectural patterns with their usage, pros and cons.

1. **Layered pattern**
2. **Client-server pattern**
3. **Master-slave pattern**
4. **Pipe-filter pattern**
5. **Broker pattern**
6. **Peer-to-peer pattern**
7. **Event-bus pattern**
8. **Model-view-controller pattern**
9. **Blackboard pattern**
10. **Interpreter pattern**

### 1. Layered pattern

This pattern can be used to structure programs that can be decomposed into groups of subtasks, each of which is at a particular level of abstraction. Each layer provides services to the next higher layer.

The most commonly found 4 layers of a general information system are as follows.

* **Presentation layer** (also known as **UI layer**)
* **Application layer** (also known as **service layer**)
* **Business logic layer** (also known as **domain layer**)
* **Data access layer** (also known as **persistence layer**)

#### Usage

* General desktop applications.
* E commerce web applications.

### 2. Client-server pattern

This pattern consists of two parties; a **server** and multiple **clients**. The server component will provide services to multiple client components. Clients request…
