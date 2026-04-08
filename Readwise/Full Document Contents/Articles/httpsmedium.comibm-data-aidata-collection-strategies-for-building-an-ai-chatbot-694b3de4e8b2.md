# https://medium.com/ibm-data-ai/data-collection-strategies-for-building-an-ai-chatbot-694b3de4e8b2

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/1*ySJz6sZ5FiCoO80qijs0PA.jpeg)

## Metadata
- Author: [[Cari Jacobs]]
- Full Title: https://medium.com/ibm-data-ai/data-collection-strategies-for-building-an-ai-chatbot-694b3de4e8b2
- Category: #articles
- Summary: To build an effective AI chatbot, you need the right training data, not just answers. This data should come from actual users expressing their needs in their own words and from the same communication channel as the chatbot. Continuous training and updates using real interactions are essential for improving chatbot performance over time.
- URL: https://medium.com/ibm-data-ai/data-collection-strategies-for-building-an-ai-chatbot-694b3de4e8b2

## Full Document
![](https://miro.medium.com/v2/resize:fit:700/1*ySJz6sZ5FiCoO80qijs0PA.jpeg)Photo by [Drew Graham](https://unsplash.com/@dizzyd718?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
As chatbots continue to be in high demand for companies who want to automate or provide 24x7 customer service, many still struggle with understanding what is necessary to get a chat solution off the ground. Simply put, AI needs data. However, not just any data will do.

When you build a chatbot, you must train it to understand the questions or requests that are most likely to be posed to the solution. This is the most common misunderstanding I encounter. Many organizations have plenty of “data” in the form of answers that they wish to provide within a chatbot. However, they often lack the most crucial data needed for training a chatbot: *examples of how users express their goals and needs (intents).*

I’ve seen more than one project get delayed due to a lack of training data.

AI chatbots are *trained* using inputs, they are then *configured* to provide outputs (answers or responses). So, the training data must be comprised of examples (a.k.a. utterances) of users asking questions or making requests. These utterances are used to train a machine learning model. Once the model is trained, it should be able to classify the intent of a request, even if the wording isn’t exactly like the examples it has already seen. This is the true power of AI.

> It is also critical to have representative training examples, which means:
> 
> 

#### Customer Voice

Data must be collected from the same type of end users targeted for the solution (NOT subject matter experts, NOT developers, NOT executives). The questions must be expressed in the voice of the user, using their vocabulary and phrasing.

When data is collected from SME’s, developers, and other people close to the project, they often introduce bias in their terminology. They submit questions with an idea in mind about the expected response. They often lack the background and real-world circumstances that drive users to engage with a chatbot solution.

![](https://miro.medium.com/v2/resize:fit:700/1*nhevdfA5s5odABoFtCTfUg.jpeg)Photo by [Louis Hansel](https://unsplash.com/@louishansel?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/customers?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
#### Channel Compatibility

Data must be collected from the SAME channel as the deployed solution (a text message solution must collect training data from text messages, a webchat solution must collect training data from chat logs, an IVR solution must collect training data from a voice channel).

Data from dissimilar channels is generally not suitable. The primary reason is that people express themselves very different when they speak, compared to how they type. (And people express themselves differently over email vs. text message, etc.)

![](https://miro.medium.com/v2/resize:fit:700/1*OgglWOF6vPxt2GfSulhlng.jpeg)Photo by [Ricardo Resende](https://unsplash.com/@rresenden?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
#### Outside Factors

Be aware of how seasonal events can influence the scope and frequency of certain topics. If your candidate training examples are harvested from a particular point in time, some topics may be under-represented or over-represented.

Do outside factors such as holidays, tax season, open enrollments, year-end processing, etc. impact the kinds of questions your users may have?

I once worked with a banking client to build a chatbot that answered general account questions. The company offered an assistance program for loan customers who may have been impacted by hurricanes. This was a high-volume request, but only during certain times of the year. If our source chat transcripts had not covered a broad enough time frame, we might have missed this topic altogether.

#### So, How Can I Get Started?

Obtaining enough training data can be a challenge, especially in the early phases of chatbot design. There are essentially five options you can choose from. These are listed from most preferable to least preferable.

The more preferable approaches (1 & 2) will give you better predictions about how the chatbot will perform once it is launched. They will also help you identify the best areas (i.e. the most frequent topics) to invest your efforts, which can guide you in building a solution that delivers the most business value.

Without appropriate planning, the less preferable approaches (4 & 5) often result in unpredictable or poor performance. Sometimes these options are unavoidable, so read the caveats and be prepared for some immediate improvement phases. A bot that is not equipped to handle the range of requests it encounters from real-world users usually does not deliver business value (and it *really* frustrates users).

#### Data Collection Strategies

1. **Mine utterances from existing chatbot logs**  
***Pros:*** Contains the best possible representative utterances   
***Cons:*** Requires a chatbot to already exist   
***Useful for:*** Migrating a chatbot solution to a new classifier   
***Critical for:*** Continuous improvement — ensure that your solution’s training data is representative and able to handle the most common/current needs of the end user population
2. **Mine utterances from existing human-to-human chat logs**  
***Pros:*** Usually contains very good representative utterances  
***Cons:*** Requires a live chat solution to already exist  
***Useful for:*** Building a new classifier
3. **Add examples from the Watson Assistant Content Catalog**  
***Pros:*** Provides basic examples that can be immediately deployed. Several domains are available to choose from, including: banking, bot control, customer care, e-commerce, general, insurance, mortgage, telco, and utilities.  
***Cons:*** The examples may not be sufficient for complex use cases or more specialized domains  
***Useful for:*** Building a new classifier
4. **Create a question collection tool for targeted end users**  
***Pros:*** Collects questions that should be representative  
***Cons:*** Requires a user interface to solicit inputs. It can be difficult to obtain questions from a public/non-captive user population. This approach is generally suited for use cases that target an internal user population, such as agent-assist solutions or virtual agents built for internal employees.  
***Useful for:*** Building a new classifier
5. **Manufacture training examples**  
***Pros:*** Generally fastest and requires the least effort/resources   
***Cons:*** Typically results in **highly biased training data** that will not be representative of runtime inputs. Projects that launch using a manufactured training data set must have a fast-follow MVP release approach. Plan to review live data and incorporate it via iterative training cycles.  
***Useful for:*** Building a prototype, proof-of-concept, or a limited/exploratory pilot

#### Final Thoughts

Regardless of which strategy you employ to get your bot launched, you MUST plan on continuous, iterative training for your bot using the first strategy. Chatbots improve over time, with exposure to more real-world interactions.

Plan to review and mine your runtime logs for the most current and representative training data. This will help you improve the intent classifications you already have. It will also help you increase business value by identifying new intents to meet the ongoing demands of your user population.

![](https://miro.medium.com/v2/resize:fit:700/1*-Sz2unjVDqYXITcptiqF4w.jpeg)Photo by [photo-nic.co.uk nic](https://unsplash.com/@chiro?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
