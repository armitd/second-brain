# FacileThings Integration with Braintoss

![rw-book-cover](https://ft-docs.s3.amazonaws.com/en/braintoss-integration.png)

## Metadata
- Author: [[Francisco Sáez]]
- Full Title: FacileThings Integration with Braintoss
- Category: #articles
- Summary: During the last few months we have received many messages from FacileThings users who were unable to integrate Braintoss with FacileThings. The truth is that it could not be done directly, due to a technical issue.
- URL: https://facilethings.com/blog/en/facilethings-braintoss-integration

## Full Document
![FacileThings Integration with Braintoss](https://ft-docs.s3.amazonaws.com/en/braintoss-integration.png)
During the last few months we have received many messages from FacileThings users who were unable to integrate Braintoss with FacileThings. The truth is that it could not be done directly, due to a technical issue.

A few days ago I got in touch with the guys at Braintoss to explain the problem to them and their CEO, Marcel Wientjen, immediately replied that they would try to solve it as soon as possible. Just one day later, one of their engineers sent me the solution (thanks Michiel!).

If you don’t know [Braintoss](https://braintoss.com), it’s an app for Android and iPhone that allows you to **capture** in a very simple and fast way voice memos, images, and notes in your email inbox.

It is, therefore, a tool that can be very useful for anyone who practices [the GTD methodology](https://facilethings.com/blog/en/ultimate-guide-to-gtd).

The **audio capturing** feature is especially interesting, since the message goes through a voice recognition system that allows the audio file to be accompanied by a text that contains the first words of the message. Ideal for identifying at a glance each of the messages you have in your inbox.

Another useful feature is that Braintoss appears in the *share* option of the rest of the apps in your smartphone, so you can easily capture a web page from the browser, a tweet from Twitter, etc.

If you use Braintoss and want your captures to reach the FacileThings Inbox, these are the steps you must follow to set up the integration:

1. Set up Braintoss with your primary email address.
2. From Braintoss, send a note with the text `set from unique`. This configures your account so that Braintoss sends your emails from a unique email address, something necessary for FacileThings to recognize what emails are yours.
3. From Braintoss, send another note, now with the word `settings`. This causes Braintoss to send you an email with your setting values. Pay attention to the `BTid` parameter, because its value will be the prefix of your unique email address in Braintoss.
4. In the FacileThings Account option, Emails section, add an email address formed with the value of the `BTid` parameter followed by **@braintoss.com** (it will be something similar to *bt2c9a98105f3c5fa7feafa7e8469a3796@braintoss.com*).
5. Braintoss will forward the confirmation email issued by FacileThings to your inbox. Click on the button “Confirm your new email” that you will find in that email (if the message doesn’t arrive in HTML format, look for a link that begins with “https://app.facilethings.com/confirm\_mail” and click on it).
6. In Braintoss, change your primary email address to **inbox+BTid@facilethings.com** (replace `BTid` with the value of your unique identifier).

From now on, anything you capture in Braintoss should arrive in your FacileThings Inbox. If you have any problem, let us know through Support.

If you are one of the Android users for whom the option to capture audio memos in the FacileThings app doesn’t work (it happens with some Android systems that don’t include the built-in voice recorder app) or you simply want to capture ideas immediately and effectively, I recommend you try Braintoss.

![ebook cover](https://cdn-ft-site.nyc3.digitaloceanspaces.com/assets/the-gtd-workflow-ebook-email-en-348bd13d13e7970788066aa3ab4d8e52a2b3440b80ed4fe3bd571a5b724166d2.jpg)ebook cover
