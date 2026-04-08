# Measuring Network Effects: Metrics in Context

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/1*y76f9n0txCLrniAVUpbPsA.png)

## Metadata
- Author: [[Sameer Singh]]
- Full Title: Measuring Network Effects: Metrics in Context
- Category: #articles
- Summary: Metrics are crucial for measuring the effectiveness of network effects in startups. The most relevant metrics vary depending on the lifecycle stage of the startup and the type of network. Pre-liquidity metrics focus on reaching critical mass and include user acquisition and retention. Different types of networks, such as data networks and interaction networks, have different core actions that drive liquidity. Post-liquidity metrics measure growth and the "flywheel" effect, where organic user acquisition and engagement lead to increased value and participation. Unit economics and defensibility are also important metrics to consider. Ultimately, a deep qualitative understanding of the network is necessary to determine the most applicable metrics.
- URL: https://breadcrumb.vc/measuring-network-effects-metrics-in-context-e4c3c98dbf4d

## Full Document
#### There is a long list of metrics that attempt to measure network effects — putting them in context is the best way to identify the most relevant KPIs for each situation

![](https://miro.medium.com/v2/resize:fit:700/1*buVlWK3VHxDvELbfP7LHFg.jpeg)Image credit: Unsplash
Metrics (or KPIs) are among the most well-researched topics within the startup ecosystem. This is just as true for those built on network effects. There are great resources available from [A16Z](https://a16z.com/2018/12/13/16-metrics-network-effects/), [Point Nine Capital](https://medium.com/point-nine-news/wtf-is-marketplace-liquidity-f2caca3802c0), and [Speedinvest Pirates](https://get.speedinvest-pirates.com/metrics-guide/) just to name a few. The goal of this post is not to simply list all these metrics again. Rather, it is to put these metrics in context and explain when each is most relevant.

The most important metrics for any startup can vary based on their lifecycle stage. Network startups have an additional consideration because they need to [gain critical mass (or liquidity)](https://medium.com/breadcrumb/marketplace-liquidity-how-side-switching-can-help-cedf08512c74) before network effects can kick in. As a result, the most important **pre-liquidity** metrics vary from those that should be prioritized **post-liquidity**. And finally, some of these metrics can also vary based on the [**type of network**](https://medium.com/breadcrumb/layering-network-effects-how-to-multiply-unfair-advantages-dddf35809fa1). Let’s take a deeper look at this.

### **Pre-Liquidity Metrics**

The first goal for any network is to reach critical mass or liquidity. Before this point is reached, the network has little to no value. However, the route to critical mass and key metrics differ based on the type of network.

#### Data & Interaction Networks

[**Data networks**](https://medium.com/breadcrumb/the-data-matrix-and-the-data-decay-dilemma-5c9b43f187c2) like Waze or Mapbox and most [**interaction networks**](https://medium.com/breadcrumb/the-network-matrix-bridges-identity-2fa9686eb978) like Facebook or Discord are **one-sided** — they connect participants and allow them to exchange information, either directly or indirectly. Like all types of networks, their route to liquidity begins with user acquisition. However, the primary driver of liquidity is **conversion to a “core action”**, i.e. the specific action (or set of actions) which makes the network more valuable for other participants. This core action needs to be completed on a recurring basis, and so **retention** (at a cohort-level, if you have enough data) becomes the most important metric.

![](https://miro.medium.com/v2/resize:fit:700/1*jLxGBnPDbFiL_6ueQqimeA.png)
The nature of the core action can vary based on the value proposition of the network. For data networks with [active crowdsourcing like Waze](https://medium.com/breadcrumb/data-networks-and-liquidity-how-to-avoid-dead-ends-3b4bd5d842e8), the core action would be submitting a report (contributing data). For data networks with [passive crowdsourcing like Mapbox](https://medium.com/breadcrumb/data-networks-and-liquidity-how-to-avoid-dead-ends-3b4bd5d842e8), all users automatically perform the core action, so the relevant metric would effectively boil down to the number of opt-ins.

For ([asynchronous](https://medium.com/breadcrumb/the-network-liquidity-map-why-time-matters-1cda5901fb49)) interaction networks like Facebook, the core action could be completing their profile or creating a post. Finally, [synchronous interaction networks](https://medium.com/breadcrumb/the-network-liquidity-map-why-time-matters-1cda5901fb49) like Discord or Clubhouse are a special case and need to measure **concurrent conversion to “core action”**, i.e. the number of participants that complete the desired action (e.g. active logins) *at the same time*.

#### Marketplaces & Platforms

Things become more complicated when we move to [**marketplaces**](https://medium.com/breadcrumb/defensibility-x-scalability-the-marketplace-matrix-9d8b02a1e6fa) like Airbnb or Uber and [**platforms**](https://medium.com/breadcrumb/the-platform-matrix-all-platforms-are-not-created-equal-f8c8b5100858) like iOS or Shopify — **multi-sided networks** that allow different types of participants to interact and transact. As a result, liquidity needs to be maintained on both the demand and supply sides — this makes it more complex to measure.

Measuring liquidity begins with the **search-to-fill ratio**, i.e. the proportion of demand-side searches that lead to a *fulfilled* transaction. This can be strengthened by defining additional attributes for a successful transaction (e.g. a [positive review](https://medium.com/breadcrumb/curation-how-to-beat-negative-network-effects-229dffff166b) after the transaction, minimum basket size, etc.). In some cases, this can be complemented or substituted with **time-to-fill**, i.e. the time taken to fulfill a demand-side request. This is most relevant for marketplaces with [commoditized supply](https://medium.com/breadcrumb/defensibility-x-scalability-the-marketplace-matrix-9d8b02a1e6fa) — e.g. Uber, Deliveroo, etc. This gives us a good idea of available liquidity from the perspective of the demand side.

Next, we need to assess liquidity from the perspective of the supply side. This varies based on the nature of supply. For marketplaces with [high-touch supply](https://medium.com/breadcrumb/curation-how-to-beat-negative-network-effects-229dffff166b) (those that require direct interaction between participants) like Airbnb or Uber, we need to look at the **utilization rate**, i.e. the proportion of available supply-side *capacity* that is utilized. However, on [low-touch](https://medium.com/breadcrumb/curation-how-to-beat-negative-network-effects-229dffff166b) marketplaces like Udemy or platforms like iOS, each unit of supply can support any amount of demand — the capacity is infinite. As a result, the utilization rate ceases to be a relevant liquidity metric. Instead, it needs to be substituted with a measure for the [economic incentive](https://medium.com/breadcrumb/platform-liquidity-impact-of-economic-incentives-72ac4ed6e9dc) — **incremental revenue or traffic** — for the supply-side.

A shortfall in any of these metrics suggests that a liquidity problem exists, but not *where* it exists. To answer that question, we need to take a granular look at [**supply density**](https://medium.com/breadcrumb/marketplace-liquidity-how-side-switching-can-help-cedf08512c74), i.e. the ratio of buyers to suppliers in each relevant region and/or in each relevant category. This can change quickly for [marketplaces with side-switching](https://medium.com/breadcrumb/marketplace-liquidity-how-side-switching-can-help-cedf08512c74) — for example, Shpock. So in this case, we also need to keep an eye on the **rate of conversion from buyers to sellers**.

Finally, there one additional liquidity metric that is specific to platforms. Platforms are never an isolated business. Rather, they are built on an [underlying product](https://medium.com/breadcrumb/curation-how-to-beat-negative-network-effects-229dffff166b) that has pre-existing customers. So liquidity also depends on **customer penetration**, i.e. the proportion of the underlying product’s customers that have adopted developer applications. This can also be applied to [marketplaces that are bootstrapped with SaaS](https://medium.com/breadcrumb/when-networks-meet-saas-f4307bf3b296).

Liquidity is the point where we can say that *product-market fit* has been achieved. After crossing this threshold, startups should continue to track these metrics to maintain liquidity. However, growth, unit economics, and defensibility take precedence at this point.

### Post-Liquidity Metrics

#### Growth and the “Flywheel”

Once liquidity is achieved, network effects come alive — in theory. At this point, the product *should* become more useful and valuable as more participants or users are added. This *should* help organic user acquisition rapidly outpace paid user acquisition. The only way to verify this is to measure it.

Organic user acquisition has two primary components — (1) **organic search**, i.e. new users seeking out your product, and (2) **user referrals**, i.e. existing users inviting others to your product. Organic search can be verified by tracking **traffic sources**. And the pace of user referrals can be tracked with the [**viral coefficient (or K-Factor)**](https://en.wikipedia.org/wiki/K-factor_(marketing)) — a measure for the number of new sign-ups generated by each user. On the whole, the efficacy of organic acquisition overall can be measured by the [**word of mouth coefficient**](https://www.reforge.com/blog/word-of-mouth-coefficient) — the ratio of new organic users to returning users and new non-organic users.

The combination of these factors should drive down **customer acquisition costs (CAC)** over time (blended across all acquisition channels). This can also be broken down by region — networks with [cross-border network effects](https://medium.com/breadcrumb/marketplaces-scalability-lessons-from-uber-and-airbnb-d461aded18a2) would be able to leverage growth in one region to drive down CAC in another region.

Increasing organic adoption has a direct impact on [**network density**](https://medium.com/breadcrumb/how-network-structure-shapes-defensibility-and-scalability-1b258a6f2d64), i.e. the ratio of the number of connections or interactions to the number of participants. Alternatively, on marketplaces and platforms, it can help maintain optimal [**supply density**](https://medium.com/breadcrumb/marketplace-liquidity-how-side-switching-can-help-cedf08512c74) at a larger scale. This should increase the value of the network, leading to increased engagement over time (from all types of participants).

The exact nature of this engagement can differ by the type of network and type of participant — it could be a specific action such as creating a post (e.g. the core action defined above) or a set of actions involved in completing a transaction. This can be verified with [**engagement and retention cohorts**](https://medium.com/swlh/diligence-at-social-capital-part-4-cohorts-and-engagement-ltv-80b4fa7f8e41)**.** Each cohort should get more engaged over time and later cohorts should be more engaged than previous cohorts (after adjusting for early adopters, who are often power users). For networks with low frequency of use, the latter should be more useful than the former.

This works the same way for marketplaces and platforms, except that scaling the demand side organically grows the supply side (cross-side network effects). As a result, they require separate cohorts for the demand and supply sides — this can take the form of engagement cohorts on the demand-side and **net revenue retention cohorts** to verify supplier stickiness.

In all cases, establishing a direct relationship between growth, engagement, and product value is the only way to prove that a network effect exists. This describes the oft-mentioned **flywheel** that causes runaway growth.

![](https://miro.medium.com/v2/resize:fit:700/1*y76f9n0txCLrniAVUpbPsA.png)
Keep in mind that this flywheel is not the same as a “[growth loop](https://www.reforge.com/blog/growth-loops#:~:text=The%20fastest%20growing%20products%20are,be%20reinvested%20in%20the%20input.)” (although they are similar concepts). Growth loops are not specific to products built on network effects and are also seen in [viral products like Zoom](https://medium.com/breadcrumb/the-difference-between-virality-and-network-effects-6bf00723bda5) (without network effects). The primary difference between the two is that growth loops for purely viral products is not linked to the value of the product. This can make it harder to defend and sustain organic growth over time. On the other hand, a flywheel powered by network effects is not only self-sustaining, it actually gets stronger over time.

#### Impact of Growth on Unit Economics

Growth, leading to higher engagement and retention, also has an impact on potential earnings from a customer. The most effective way to measure this is with [**customer lifetime value (LTV)**](https://en.wikipedia.org/wiki/Customer_lifetime_value) — best measured at a [cohort-level](https://medium.com/swlh/diligence-at-social-capital-part-3-cohorts-and-revenue-ltv-ab65a07464e1). Depending on the monetization model that is used, this is also influenced by ad load, basket size, purchase frequency, conversion, and/or take rate.

In general, we should expect LTV to grow over time as network effects kick in. As I explained earlier, the CAC should continue to decline over this time as well. So the **LTV/CAC ratio** should rise sharply as the network scales — although the degree of this depends on the [type of network effect](https://medium.com/breadcrumb/defensibility-x-scalability-the-marketplace-matrix-9d8b02a1e6fa). This is valid for platforms as well, but it provides an incomplete understanding. One of the goals of a platform is to make the [underlying product](https://medium.com/breadcrumb/the-platform-matrix-all-platforms-are-not-created-equal-f8c8b5100858) more valuable to customers. As a result, we primarily need to measure the **LTV/CAC ratio of the underlying product**.

The complete relationship between metrics that influence growth and unit economics can be summarized as follows:

#### Defensibility

Finally, the last important facet to measure is defensibility. The primary drivers of defensibility tend to be structural and do not change often. Depending on the type of network, this can include the [importance of unique user identity](https://medium.com/breadcrumb/the-network-matrix-bridges-identity-2fa9686eb978), [network structure](https://medium.com/breadcrumb/how-network-structure-shapes-defensibility-and-scalability-1b258a6f2d64), [differentiated supply](https://medium.com/breadcrumb/defensibility-x-scalability-the-marketplace-matrix-9d8b02a1e6fa), [transaction frequency](https://medium.com/breadcrumbs-guiding-startups/why-marketplaces-fail-the-role-of-engagement-e372fb3edd03), [rate of data decay](https://medium.com/breadcrumb/the-data-matrix-and-the-data-decay-dilemma-5c9b43f187c2), or the [importance of truly native apps](https://medium.com/breadcrumb/the-platform-matrix-all-platforms-are-not-created-equal-f8c8b5100858). Even relatively simple means of defensibility like [switching costs](https://medium.com/breadcrumb/when-networks-meet-saas-f4307bf3b296) do not change meaningfully without significant product changes. As a result, they are not critical to measure regularly even though they are exceptionally important to understand.

There is one exception to this. [**Multi-tenanting**](https://medium.com/breadcrumb/defensibility-x-scalability-the-marketplace-matrix-9d8b02a1e6fa) — participants using multiple networks for the same need — can serve as an early warning system to flag competitive concerns. This makes it important to track on a semi-regular basis. Since it relies on measuring usage across competitor products, in addition to your own, it can only be measured with **surveys** and/or **third-party datasets**. Snap’s well-publicized [exclusive reach](https://forbusiness.snapchat.com/blog/snapchat's-unique-reach-around-the-world) analysis is one example. Note that extensive multi-tenanting can be a leading indicator of churn. Over time, this can be verified with engagement and retention cohorts — some participants may become less engaged as they begin using other networks. However, engagement and retention are *lagging indicators* — by the time you see the impact here, the damage is already in progress.

In closing, metrics are critical to measure your progress and inform necessary adjustments. However, they are *not* a substitute for a [deep qualitative understanding of your network](http://breadcrumb.vc/). The most applicable variations of these metrics are entirely dependent on this qualitative understanding.

### What you should do next…

#### 1. [Pitch me](mailto:sameer@breadcrumb.vc): No warm intros required

I invest in pre-seed/seed-stage startups as a Venture Partner at Speedinvest and also via the Atomico Angel Program. If your startup is built on network effects and based in Europe, [**pitch me here**](mailto:sameer@breadcrumb.vc)**.**

#### 2. [Take the network effects assessment](https://ktmc6jt487x.typeform.com/to/LHLrqJfb)

Benchmark your network effects by answering a 1 min quiz about your startup or a potential startup investment. [**Try it here**](https://ktmc6jt487x.typeform.com/to/LHLrqJfb).

#### 3. [Apply for my cohort-based course](https://maven.com/breadcrumb/applied-network-effects/)

Want to learn more about network effects? I run a 3-week long, workshop-style course on building, evaluating, scaling, and monetizing network effects. [**Register now**](https://maven.com/breadcrumb/applied-network-effects/) to secure your place or watch this free [**network effects crash course**](https://maven.com/p/350c14) to get a taste of what to expect.

#### 4. [Book a consultation](https://superpeer.com/sameersingh)

Do you have a specific question about creating, scaling, or monetizing network effects? [**Book a consultation**](https://superpeer.com/sameersingh) or [**sign up**](https://zcal.co/sameersingh/officehours) for my free weekly office hours (they tend to get booked out fast).
