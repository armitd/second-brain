# Why Use Feature Flags?

![rw-book-cover](https://images.prismic.io/launchdarkly/0b397bd9-7379-4544-8218-3aaecbdf1699_2021_06_WhatItMeansToBeTechnical.png?ixlib=gatsbyFP&auto=compress%2Cformat&fit=max)

## Metadata
- Author: [[LaunchDarkly]]
- Full Title: Why Use Feature Flags?
- Category: #articles
- Summary: Conceptually, this flow is not much different than other authorization logic your app might have. Consider a blogging site with support for both free-tier and premium-tier writers.
- URL: https://launchdarkly.com/blog/why-use-feature-flags/

## Full Document
![Why Use Feature Flags? featured image](https://images.prismic.io/launchdarkly/0b397bd9-7379-4544-8218-3aaecbdf1699_2021_06_WhatItMeansToBeTechnical.png?ixlib=gatsbyFP&auto=compress%2Cformat&fit=max&rect=0%2C0%2C2560%2C1440&w=2000&h=1125)
Modern software development is guided by iterations. Product managers sift through feedback and define business requirements; developers and designers deploy updates that satisfy users’ needs; and data scientists observe user behaviors and collect feedback, kicking off the cycle once more. This is how an idea becomes software that people use.

In reality, though, the process is never this simple. Even the most well-tested code can’t account for all real-world situations. More often than not, bugs in production can create surprising issues. Monitoring can certainly report on whether a feature has unexpected consequences, but solving these errors requires deployment rollbacks and timing hotfixes.

Even outside of quality assurance, there are many reasons why a deployment might stall. For example, teams could have trouble deciding the best approach to take when building a new feature. A user experience study can help guide them towards building solutions people want, but these kinds of programs can take too long to set up and assess.

In these cases (and many others), using [feature flags](https://launchdarkly.com/blog/what-are-feature-flags/) is a powerful strategy for quickly surfacing what works—and what doesn’t. In this post, we’ll take a look at what feature flags are, when to use them, and why they make sense for large and small companies.

#### What Are Feature Flags?

**A feature flag is a software development technique used for releasing software to a limited subset of users.** For example, if you were redesigning your app and wanted to see how people would react to the changes, you might choose to show the new design to only half of your active users. Or, if you built some functionality aimed at enterprise teams, you might choose to target only those users who belong to a large organization. You can even run a beta program with feature flags. A user could sign up to get access to a new, rough-around-the-edges feature, and a target feature flag would grant them access.

Here at LaunchDarkly, we prefer this latter option. It’s not only more flexible, but it also takes the burden of maintaining a feature flag infrastructure off of your Ops teams, allowing them to focus on the more critical needs of your application.

Whenever a user navigates to a new page or route in your app, you can check for the value of the feature flag and choose to act on it. Here's an example of what the code for this might look like:

|  |  |
| --- | --- |
|  | const ldClient = LaunchDarkly.init(sdkKey); |
|  |  |
|  | const user = { |
|  |  "key": "user-type", |
|  |  "name": "Sandy" |
|  | }; |
|  |  |
|  | await ldClient.waitForInitialization(); |
|  | console.log("SDK successfully initialized!"); |
|  |  |
|  | let flagValue = ldClient.variation(featureFlagKey, user) |
|  |  |
|  | if (flagValue == "pro-user") { |
|  |  // redirect to new UI  |
|  | } |

Conceptually, this flow is not much different than other authorization logic your app might have. Consider a blogging site with support for both free-tier and premium-tier writers. Free-tier writers would have a limited amount of features; meanwhile, premium-tier writers have access to additional features, such as the ability to customize their design. These abilities, accessible only for paying customers, could be controlled by a feature flag. For a simple case like this, a feature flag backed by a database *might* make sense. However, the advantage of feature flags is that they scale much more easily. Let’s take a deeper look at where feature flags shine.

#### When Should I Use Feature Flags?

Imagine this scenario: After months of collecting user feedback, your teams have worked together to build a brand new, eye-popping user interface. All the links, colors, and buttons in your app have changed, resulting in an experience that’s both vastly different and—you feel—far superior than what currently exists. Since your company [dogfoods](https://en.wikipedia.org/wiki/Eating_your_own_dog_food) its own product, you're reasonably confident that the improvements will translate to your users, too. But how can you transform those beliefs into certainties?

One way to gain confidence is to give half of your users the new UI and leave the other half with the current UI. You can solicit feedback from the users with the new UI, or just observe their changing habits, to decide whether to make adjustments or move forward with the redesign. These practices—commonly referred to as [A/B testing](https://en.wikipedia.org/wiki/A/B_testing)—allow you to observe how users respond to new changes against a control group. Feature flagging, in conjunction with other data metrics, can help identify what works and what doesn’t.

With feature flags, you can toggle new changes for your users across any cross-section you want. Perhaps accounts that are less than six months old will get the new UI to gather more critical, real-time feedback. This might be a more conservative approach than changing *everything* for *everyone*. Or, maybe a random 10% of users get the changes, but you slowly increase that percentage every two weeks.

Because LaunchDarkly’s feature flags are API-based, you could even imagine a complex scenario where users are toggled into new functionality based on some kind of data. What if users were gradually toggled into a new design every weekday at 4 am so that they’re pleasantly surprised by new changes when they login to your app?

Feature flags aren’t limited to UI changes, of course. You could create a beta program for a new feature, and have users sign up for a waitlist. When you want to include a new batch of users for the feature, you can just feature flag them in with a single HTTP call.

You might even use feature flags as part of a new marketing campaign. You can deploy some new app functionality to production behind a feature flag and flip the flag on for everyone on a certain date. That way, you don’t have to worry about timing your deployment; the code is already live, you just have to toggle it for 100% of your users.

No matter what you’re creating, feature flags can serve as a sort of benevolent bouncer that grants users access to a party—one at a time—until you can open the doors.

#### The Advantages of Feature Flags

For every new feature that’s developed, it’s common practice to write test cases with expectations for how your app ought to behave. This ensures that future changes to your evolving code base don’t cause disruptions for your users. However, no matter how well-defined your integration and acceptance test coverage might be, once code lands in production, there is *always* the possibility for unexpected bugs or issues to arise.

Real users in production can reveal more about how a feature works than any test could ever anticipate. For example, you may have neglected to optimize your database queries. This is a serious performance problem that only manifests when you have many active users and records. Or, you might expect that you have enough CPU, memory, and disk space to run your app efficiently, only to find that your new feature is extremely popular, consuming all your available resources.

Gradually bringing users in through feature flags can help uncover—if not entirely mitigate—these issues. If you notice your database is unable to keep up with the activities of your feature flagged users, you can address the problem immediately, without incurring downtime for everyone. Feature flagging can help you monitor how your infrastructure handles an influx of new activity in scenarios you can’t predict.

Ultimately, feature flagging is about being careful, considerate, and controlled. Software can be fickle, but as long as you know that, you can introduce changes slowly, rather than being afraid to change anything for fear of breaking something.

#### Learn More About Feature Flagging

Feature flagging might sound like a complex topic, but it doesn’t have to be! You can learn more about [how to create your first feature flag](https://docs.launchdarkly.com/home/getting-started/feature-flags), or [read case studies](https://launchdarkly.com/case-studies/) from companies who have embraced the technique. If you’re curious about how to go about implementing feature flags in your app, we’ve provided [some best practices](https://launchdarkly.com/blog/best-practices-short-term-permanent-flags/) to help guide you on the journey.
