# How many bots are on Twitter? The question is tough to answer — and misses the point

![rw-book-cover](https://www.niemanlab.org/images/bots-Getty-Images-700x467.jpeg)

## Metadata
- Author: [[Simon Potter]]
- Full Title: How many bots are on Twitter? The question is tough to answer — and misses the point
- Category: #articles
- Summary: Twitter reports that fewer than 5% of accounts are fakes or spammers, commonly referred to as “bots.” Since his offer to buy Twitter was accepted, Elon Musk has repeatedly questioned these estimates, even dismissing CEO Parag Agrawal’s public response.
- URL: https://www.niemanlab.org/2022/05/how-many-bots-are-on-twitter-the-question-is-tough-to-answer-and-misses-the-point/

## Full Document
![](https://www.niemanlab.org/images/bots-Getty-Images-2048x1365.jpeg)
“We have observed a broad spectrum of behaviors mixing the characteristics of bots and people.”

Twitter [reports that fewer than 5% of accounts are fakes or spammers](https://www.reuters.com/technology/twitter-estimates-spam-fake-accounts-represent-less-than-5-users-filing-2022-05-02/), commonly referred to as “bots.” Since his offer to buy Twitter was accepted, Elon Musk has repeatedly questioned these estimates, even dismissing [CEO Parag Agrawal’s public response](https://twitter.com/paraga/status/1526237578843672576).

Later, Musk [put the deal on hold and demanded more proof](https://twitter.com/elonmusk/status/1526465624326782976).

So why are people arguing about the percentage of bot accounts on Twitter?

As the creators of [Botometer](https://botometer.osome.iu.edu/), a widely used bot detection tool, our group at the Indiana University [Observatory on Social Media](https://osome.iu.edu/) has been studying inauthentic accounts and manipulation on social media for over a decade. We brought the concept of the “[social bot](https://cacm.acm.org/magazines/2016/7/204021-the-rise-of-social-bots/fulltext)” to the foreground and [first estimated](https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15587) [their prevalence](https://www.cnbc.com/2017/03/10/nearly-48-million-twitter-accounts-could-be-bots-says-study.html) on Twitter in 2017.

Based on our knowledge and experience, we believe that estimating the percentage of bots on Twitter has become a very difficult task, and debating the accuracy of the estimate might be missing the point. Here is why.

##### What, exactly, is a bot?

To measure the prevalence of problematic accounts on Twitter, a clear definition of the targets is necessary. Common terms such as “fake accounts,” “spam accounts,” and “bots” are used interchangeably, but they have different meanings. Fake or false accounts are those that impersonate people. Accounts that mass-produce unsolicited promotional content are defined as spammers. Bots, on the other hand, are accounts controlled in part by software; they may post content or carry out simple interactions, like retweeting, automatically.

These types of accounts often overlap. For instance, you can create a bot that impersonates a human to post spam automatically. Such an account is simultaneously a bot, a spammer and a fake. But not every fake account is a bot or a spammer, and vice versa. Coming up with an estimate without a clear definition only yields misleading results.

Defining and distinguishing account types can also inform proper interventions. Fake and spam accounts degrade the online environment and violate [platform policy](https://help.twitter.com/en/rules-and-policies/platform-manipulation). Malicious bots are used to [spread misinformation](https://doi.org/10.1038/s41467-018-06930-7), [inflate popularity](https://www.nytimes.com/interactive/2018/01/27/technology/social-media-bots.html), [exacerbate conflict through negative and inflammatory content](https://doi.org/10.1073/pnas.1803470115), [manipulate opinions](https://ojs.aaai.org/index.php/ICWSM/article/view/14127), [influence elections](https://doi.org/10.1371/journal.pone.0214210), [conduct financial fraud](https://doi.org/10.1109/TCSS.2021.3059286), and [disrupt communication](https://doi.org/10.1007/978-3-319-47874-6_19). However, some bots can be harmless or even [useful](https://doi.org/10.1080/21670811.2015.1081822), for example by helping disseminate news, delivering disaster alerts, and [conducting research](https://doi.org/10.1038/s41467-021-25738-6).

Simply banning all bots is not in the best interest of social media users.

For simplicity, researchers use the term “inauthentic accounts” to refer to the collection of fake accounts, spammers, and malicious bots. This is also the definition Twitter appears to be using. However, it is unclear what Musk has in mind.

##### Hard to count

Even when a consensus is reached on a definition, there are still technical challenges to estimating prevalence.

External researchers do not have access to the same data as Twitter, such as IP addresses and phone numbers. This [hinders the public’s ability](https://doi.org/10.37016/mr-2020-49) to identify inauthentic accounts. But even Twitter acknowledges that the actual number of inauthentic accounts [could be higher than it has estimated](https://investor.twitterinc.com/financial-information/annual-reports/default.aspx), because [detection is challenging](https://twitter.com/paraga/status/1526237581419040768).

Inauthentic accounts evolve and develop new tactics to evade detection. For example, some fake accounts [use AI-generated faces as their profiles](https://twitter.com/conspirator0/status/1502772800146313223). These faces can be indistinguishable from real ones, [even to humans](https://doi.org/10.1073/pnas.2120481119). Identifying such accounts is hard and requires new technologies.

Another difficulty is posed by [coordinated accounts](https://ojs.aaai.org/index.php/ICWSM/article/view/18075) that appear to be normal individually but act so similarly to each other that they are almost certainly controlled by a single entity. Yet they are like needles in the haystack of hundreds of millions of daily tweets.

Finally, inauthentic accounts can evade detection by techniques like [swapping handles](https://ojs.aaai.org/index.php/ICWSM/article/view/18075) or automatically [posting and deleting](https://arxiv.org/abs/2203.13893) large volumes of content.

The distinction between inauthentic and genuine accounts gets more and more blurry. Accounts can be hacked, [bought, or rented](https://www.nytimes.com/interactive/2018/01/27/technology/social-media-bots.html), and some users “donate” their credentials to [organizations](https://www.washingtonpost.com/politics/turning-point-teens-disinformation-trump/2020/09/15/c84091ae-f20a-11ea-b796-2dd09962649c_story.html) who post on their behalf. As a result, so-called [“cyborg” accounts](https://www.washingtonpost.com/business/economy/as-a-conservative-twitter-user-sleeps-his-account-is-hard-at-work/2017/02/05/18d5a532-df31-11e6-918c-99ede3c8cafa_story.html) are controlled by both algorithms and humans. Similarly, spammers sometimes post legitimate content to obscure their activity.

We have observed a broad spectrum of behaviors mixing the characteristics of bots and people. Estimating the prevalence of inauthentic accounts requires applying a simplistic binary classification: authentic or inauthentic account. No matter where the line is drawn, mistakes are inevitable.

##### Missing the big picture

The focus of the recent debate on estimating the number of Twitter bots oversimplifies the issue and misses the point of quantifying the harm of online abuse and manipulation by inauthentic accounts.

Through [BotAmp](https://botometer.osome.iu.edu/botamp), a new tool from the Botometer family that anyone with a Twitter account can use, we have found that the presence of automated activity is not evenly distributed. For instance, the discussion about cryptocurrencies tends to show more bot activity than the discussion about cats. Therefore, whether the overall prevalence is 5% or 20% makes little difference to individual users; their experiences with these accounts depend on whom they follow and the topics they care about.

Recent evidence suggests that inauthentic accounts might not be the only culprits responsible for the spread of misinformation, hate speech, polarization and radicalization. These issues typically involve many human users. For instance, our analysis shows that [misinformation about Covid-19 was disseminated overtly](https://doi.org/10.1177/20539517211013861) on both Twitter and Facebook by verified, [high-profile accounts](https://apnews.com/article/how-rfk-jr-built-anti-vaccine-juggernaut-amid-covid-4997be1bcf591fe8b7f1f90d16c9321e).

Even if it were possible to precisely estimate the prevalence of inauthentic accounts, this would do little to solve these problems. A meaningful first step would be to acknowledge the complex nature of these issues. This will help social media platforms and policymakers develop meaningful responses.

[Kai-Cheng Yang](https://www.kaichengyang.me) is a doctoral student in informatics at Indiana University. [Filippo Menczer](https://cnets.indiana.edu/fil/) is a professor of informatics and computer science at Indiana University. This article is republished from [The Conversation](https://theconversation.com/how-many-bots-are-on-twitter-the-question-is-difficult-to-answer-and-misses-the-point-183425) under a Creative Commons license.

Show tags

Some content could not be imported from the original document. [View content ↗](https://disqus.com/embed/comments/?base=default&f=niemanlab&t_i=203417%20https%3A%2F%2Fwww.niemanlab.org%2F%3Fp%3D203417&t_u=https%3A%2F%2Fwww.niemanlab.org%2F2022%2F05%2Fhow-many-bots-are-on-twitter-the-question-is-tough-to-answer-and-misses-the-point%2F&t_e=How%20many%20bots%20are%20on%20Twitter%3F%20The%20question%20is%20tough%20to%20answer%20%E2%80%94%C2%A0and%20misses%20the%20point&t_d=How%20many%20bots%20are%20on%20Twitter%3F%20The%20question%20is%20tough%20to%20answer%20%E2%80%94%C2%A0and%20misses%20the%20point%20%7C%20Nieman%20Journalism%20Lab&t_t=How%20many%20bots%20are%20on%20Twitter%3F%20The%20question%20is%20tough%20to%20answer%20%E2%80%94%C2%A0and%20misses%20the%20point&s_o=default#version=cec689ad95ce51d4ec01d71f9fdfa613)
