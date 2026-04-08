# Apple's encryption capitulation (permalink)

![rw-book-cover](https://i0.wp.com/pluralistic.net/wp-content/uploads/2020/02/cropped-guillotine-French-Revolution.jpg?fit=192%2C192&ssl=1)

## Metadata
- Author: [[Cory Doctorow]]
- Full Title: Apple's encryption capitulation (permalink)
- Category: #articles
- Summary: The UK government has ordered Apple to weaken its encryption for all iOS users, putting British users' sensitive data at risk. In response, Apple plans to disable a key security feature for UK users instead of compromising encryption worldwide. This decision raises serious concerns about user privacy and security, as it could expose millions of people to criminal threats.
- URL: https://pluralistic.net/2025/02/25/sneak-and-peek/#pavel-chekov

## Full Document
[![](https://i0.wp.com/craphound.com/images/25Feb2025.jpg?w=840&ssl=1)](https://pluralistic.net/2025/02/25/sneak-and-peek/)
### Today's links

* [Apple's encryption capitulation](https://pluralistic.net/2025/02/25/sneak-and-peek/#pavel-chekov): They put the gun on the mantelpiece in Act One, they don't get to be surprised now.
* [Hey look at this](https://pluralistic.net/2025/02/25/sneak-and-peek/#linkdump): Delights to delectate.
* [Object permanence](https://pluralistic.net/2025/02/25/sneak-and-peek/#retro): 2005, 2010, 2015, 2020
* [Upcoming appearances](https://pluralistic.net/2025/02/25/sneak-and-peek/#upcoming): Where to find me.
* [Recent appearances](https://pluralistic.net/2025/02/25/sneak-and-peek/#recent): Where I've been.
* [Latest books](https://pluralistic.net/2025/02/25/sneak-and-peek/#latest): You keep readin' em, I'll keep writin' 'em.
* [Upcoming books](https://pluralistic.net/2025/02/25/sneak-and-peek/#upcoming-books): Like I said, I'll keep writin' 'em.
* [Colophon](https://pluralistic.net/2025/02/25/sneak-and-peek/#bragsheet): All the rest.

![An ornate fireplace and mantlepiece. There is a roaring fire in the grate. Over the mantlepiece is an AR-15 assault rifle, surmounted by Apple's 'Think Different' wordmark. The scene is pockmarked with bullet-holes.](https://i0.wp.com/craphound.com/images/apple-gun-on-mantlepiece.jpg?w=840&ssl=1)
The UK government has just ordered Apple to secretly compromise its security for every iOS user in the world. Instead, Apple announced it will disable a vital security feature for every UK user. This is a terrible outcome, but it just might be the best one, given the circumstances:

<https://www.bbc.com/news/articles/cgj54eq4vejo>

So let's talk about those circumstances. In 2016, Theresa May's Conservative government passed a law called the "Investigative Powers Act," better known as the "Snooper's Charter":

<https://www.snooperscharter.co.uk/>

This was a hugely controversial law for many reasons, but most prominent was that it allowed British spy agencies to order tech companies to secretly modify their software to facilitate surveillance. This is alarming in several ways. First, it's hard enough to implement an encryption system without making subtle errors that adversaries can exploit.

Tiny mistakes in encryption systems are leveraged by criminals, foreign spies, griefers, and other bad actors to steal money, lock up our businesses and governments with ransomware, take our data, our intimate images, our health records and worse. The world is already awash in cyberweapons that terrible governments and corporations use to target their adversaries, such as the NSO Group malware that the Saudis used to hack Whatsapp, which let them lure Jamal Khashoggi to his death. The stakes couldn't be higher:

<https://pluralistic.net/2025/02/04/citizen-lab/#nso-group>

Encryption protects everything from the software updates for pacemakers and anti-lock braking to population-scale financial transactions and patient records. Deliberately introducing bugs into these systems to allow spies and cops to "break" encryption when they need to is impossible, which doesn't stop governments from demanding it. Notoriously, when former Australian PM Malcolm Turnbull was told that the laws of mathematics decreed that there is no way to make encryption that only stops bad guys but lets in good guys, he replied "The laws of mathematics are very commendable but the only law that applies in Australia is the law of Australia":

<https://www.eff.org/deeplinks/2017/07/australian-pm-calls-end-end-encryption-ban-says-laws-mathematics-dont-apply-down>

The risks don't stop with bad actors leveraging new bugs introduced when the "lawful interception" back-doors are inserted. The keys that open these back-doors inevitably circulate widely within spy and police agencies, and eventually – inevitably – they leak. This is called the "keys under doormats" problem: if the police order tech companies to hide the keys to access billions of peoples' data under their doormats, eventually, bad guys will find them there:

<https://academic.oup.com/cybersecurity/article/1/1/69/2367066>

Again, this isn't a theoretical risk. In 1994, Bill Clinton signed a US law called CALEA that required FBI back-doors for data switches. Most network switches in use today have CALEA back-doors and they have been widely exploited by various bad guys. Most recently, the Chinese military used CALEA backdoors to hack Verizon, AT&T and Lumen:

<https://pluralistic.net/2024/10/07/foreseeable-outcomes/#calea>

This is the backdrop against which the Snooper's Charter was passed. Parliament stuck its fingers in its ears, covered its eyes, and voted for the damned thing, swearing that it would never result in any of the eminently foreseeable harms they'd been warned of.

Which brings us to today. Two weeks ago, the *Washington Post*'s Joseph Menn broke the story that Apple had received a secret order from the British government, demanding that they install a back-door in the encryption system that protects cloud backups of iOS devices:

<https://www.washingtonpost.com/technology/2025/02/07/apple-encryption-backdoor-uk/>

Virtually every iOS device in the world regularly backs itself up to Apple's cloud backup service. This is very useful: if your phone or tablet is lost, stolen or damaged, you can recover your backup to a new device in a matter of minutes and get on with your day. It's also very lucrative for Apple, which charges every iOS user a few dollars every month for backup services. The dollar amount here is small, but that sum is multiplied by the *very* large number of Apple devices, and it rolls in every single month.

Since 2022, Apple has offered its users a feature called "Advanced Data Protection" that employs "end-to-end" encryption (E2EE) for these backups. End-to-end encryption keeps data encrypted between the sender and the receiver, so that the service provider can't see what they're saying to each other. In the case of iCloud backups, this means that while an Apple *customer* can decrypt their backup data when they access it in the cloud, Apple itself cannot. All Apple can see is that there is an impenetrable blob of user data on one of its servers.

2022 was very late for Apple to have added E2EE to its cloud backups. After all, in 2014, Apple customers suffered a massive iCloud breach when hackers broke into the iCloud backups of hundreds of celebrities, leaking nude photos and other private data, in a breach colloquially called "Celebgate" or "The Fappening":

<https://en.wikipedia.org/wiki/2014_celebrity_nude_photo_leak>

Apple *almost* rolled out E2EE for iCloud in 2018, but scrapped the plans after Donald Trump's FBI leaned on them:

<https://www.reuters.com/article/world/exclusive-apple-dropped-plan-for-encrypting-backups-after-fbi-complained-sour-idUSKBN1ZK1CO/>

Better late than never. For three years, Apple customers' backups have been encrypted, at rest, on Apple's servers, their contents fully opaque to everyone except the devices' owners. Enter His Majesty's Government, clutching the Snooper's Charter. As the eminent cryptographer Matthew Green writes, a secret order to compromise the cloud backups of British users is *necessarily* a secret order to compromise *all* users' encrypted backups:

<https://blog.cryptographyengineering.com/2025/02/23/three-questions-about-apple-encryption-and-the-u-k/>

There's no way to roll out a compromised system in the UK that differs from non-British backups without the legion of reverse-engineers and security analysts noticing that something new is happening in Britain and correctly inferring that Apple has been served with a secret "Technical Capability Notice" under the Snooper's Charter:

>  Even if you imagine that Apple is only being asked only to target users in the U.K., the company would either need to build this capability globally, or it would need to deploy a new version or “zone”1 for U.K. users that would work differently from the version for, say, U.S. users. From a technical perspective, this would be tantamount to admitting that the U.K.’s version is somehow operationally distinct from the U.S. version. That would invite reverse-engineers to ask very pointed questions and the secret would almost certainly be out. 
> 
> 

For Apple, the only winning move was not to play. Rather than breaking the security for its iCloud backups worldwide, it simply promised to turn off *all* security for backups in the UK. If they go through with it, every British iOS user – doctors, lawyers, small and large business, and individuals – will be exposed to incalculable risk from spies and criminals, both organized and petty.

For Green, this is Apple making the best of an impossible conundrum. Apple *does* have a long and proud history of standing up to governmental demands to compromise its users. Most notably, the FBI ordered Apple to push an encryption-removing update to its phones in 2016, to help it gain access to a device recovered from the bodies of the San Bernardino shooters:

<https://www.eff.org/deeplinks/2016/02/eff-support-apple-encryption-battle>

But it's worth zooming out here for a moment and considering all the things that led up to Apple facing this demand. By design, Apple's iOS platform blocks users from installing software unless Apple approves it and lists it in the App Store. Apple uses legal protections (such as Section 1201 of the US Digital Millennium Copyright Act and Article 6 of the EUCD, which the UK adopted in 2003 through the Copyright and Related Rights Regulations) to make it a jailable offense to reverse-engineer and bypass these blocks. They also devote substantial technical effort to preventing third parties from reverse-engineering its software and hardware locks. Installing software forbidden by Apple on your own iPhone is thus both illegal and very, very hard.

This means that if Apple removes an app from its App Store, its customers can no longer get that app. When Apple launched this system, they were warned – by the same cohort of experts who warned the UK government about the risks of the Snooper's Charter – that it would turn into an attractive nuisance. If a corporation has the power to compromise billions of users' devices, governments will *inevitably* order that corporation to do so.

Which is *exactly* what happened. Apple has already removed all working privacy tools for its Chinese users, purging the Chinese App Store of secure VPN apps, compromising its Chinese cloud backups, and downgrading its Airdrop file-transfer software to help the Chinese state crack down on protesters:

<https://pluralistic.net/2022/11/11/foreseeable-consequences/#airdropped>

These are the absolutely foreseeable – and foreseen – outcomes of Apple arrogating total remote control over its customers' devices to itself. If we're going to fault Theresa May's Conservatives for refusing to heed the warnings of the risks introduced by the Snooper's Charter, we should be every bit as critical of Apple for chasing profits at the expense of billions of its customers in the face of warnings that its "curated computing" model would *inevitably* give rise to the Snooper's Charter and laws like it.

As Pavel Chekov famously wrote: "a phaser on the bridge in act one will always go off by act three." Apple set itself up with the power to override its customers' decisions about the devices it sells them, and then that power was abused in a hundred ways, large and small:

<https://pluralistic.net/2023/09/22/vin-locking/#thought-differently>

Of course, there are plenty of third-party apps in the App Store that allow you to make an end-to-end encrypted backup to non-Apple cloud servers, and Apple's onerous App Store payment policies mean that they get to cream off 30% of every dollar you spend with its rivals:

<https://www.reddit.com/r/privacy/comments/1iv072y/endtoend_encrypted_alternative_to_icloud_drive/>

It's entirely possible to find an end-to-end encrypted backup provider that has no presence in the UK and can tell the UK government to fuck off with its ridiculous back-door demands. For example, Signal has repeatedly promised to pull its personnel and assets out of the UK before it would compromise its encryption:

<https://pluralistic.net/2023/03/05/theyre-still-trying-to-ban-cryptography/>

But even if the company that provides your backup is impervious to pressure from HMG, *Apple isn't*. Apple has the absolute, unchallenged power to decide which apps are in its App Store. Apple has a long history of nuking privacy-preserving and privacy-enhancing apps from its App Store in response to complaints, even petty ones from rival companies like Meta:

<https://www.theverge.com/2022/9/29/23378541/the-og-app-instagram-clone-pulled-from-app-store>

If they're going to cave into Zuck's demand to facilitate spying on Instagram users, do we really think they'll resist Kier Starmer's demands to remove Signal – and any other app that stands up to the Snooper's Charter – from the App Store?

It goes without saying that the "bad guys" the UK government claims it wants to target will be able to communicate in secret no matter what Apple does here. They can just use an Android phone and sideload a secure messaging app, or register an iPhone in Ireland or any other country and bring it to the UK. The only people who will be harmed by the combination of the British government's reckless disregard for security, and Apple's designs that trade the security of its users for the security of its shareholders are millions of law-abiding Britons, whose most sensitive data will be up for grabs by anyone who hacks their accounts.

(*Image: [Mitch Barrie](https://commons.wikimedia.org/wiki/File:Daytona_Skeleton_AR-15_completed_rifle_%2817551907724%29.jpg), [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/deed.en); [Kambanji](https://www.flickr.com/photos/kambanji/4135216486/), [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/); [Rawpixel](https://www.rawpixel.com/image/12438797/png-white-background); modified*)

### Hey look at this ([permalink](https://pluralistic.net/2025/02/25/sneak-and-peek/#linkdump))

![](https://i0.wp.com/craphound.com/images/heylookatthis.jpg?w=840&ssl=1)
* The Coup Has Failed <https://prospect.org/politics/2025-02-24-trump-coup-has-failed/>
* There Is No AI Revolution <https://www.wheresyoured.at/wheres-the-money/>
* Tesla Is More Vulnerable Than You Think <https://www.hamiltonnolan.com/p/tesla-is-more-vulnerable-than-you>

![A Wayback Machine banner.](https://i0.wp.com/craphound.com/images/wayback-machine-hed-796x416.png?resize=796%2C416&ssl=1)
### Object permanence ([permalink](https://pluralistic.net/2025/02/25/sneak-and-peek/#retro))

#20yrsago iPod acoustic hack: what it means <https://web.archive.org/web/20050301014904/http://vitanuova.loyalty.org/weblog/nb.cgi/view/vitanuova/2005/02/25/1>

#15yrsago Golden-age computer manual encourages you to break DRM, rants against EULAs <https://www.ironicsans.com/2010/02/they_dont_make_computer_manual.html>

#15yrsago ACTA leak: Now we know who is against transparency – USA, Korea, Singapore, Denmark <https://web.archive.org/web/20100227072335/http://www.michaelgeist.ca/content/view/4819/125/>

#10yrsago Grim meathook future, Singapore style <https://www.antipope.org/charlie/blog-static/2015/02/a-different-cluetrain.html>

#10yrsago Billboards tell the stories of professionals who can’t afford London anymore <https://www.dazeddigital.com/artsandculture/gallery/19402/0/london-is-changing>

#10yrsago Don’t argue about vaccination with Rob Schneider if you value your sanity <https://web.archive.org/web/20150221073129/https://www.10news.com/news/local-politician-goes-toe-to-toe-with-deuce-bigalow-actor-over-proposed-changes-to-vaccination-law>

#10yrsago Yahoo’s security boss faces down NSA director over crypto ban < ahref="https://arstechnica.com/tech-policy/2015/02/yahoo-exec-goes-mano-a-mano-with-nsa-director-over-crypo-backdoors/">https://arstechnica.com/tech-policy/2015/02/yahoo-exec-goes-mano-a-mano-with-nsa-director-over-crypo-backdoors/

#10yrsago UK Tory MP says astrology would improve NHS health outcomes <https://www.theguardian.com/politics/2015/feb/25/astrology-help-nhs-claim-conservative-mp-david-tredinnick>

#5yrsago New podcast about the history of Gopher and adversarial interoperability <https://pluralistic.net/2020/02/25/pluralistic-your-daily-link-dose-25-feb-2020/#internetducttape>

#5yrsago Private equity looters underperform the S&P 500 <https://pluralistic.net/2020/02/25/pluralistic-your-daily-link-dose-25-feb-2020/#extraordinaryclaims>

#5yrsago Bloomberg's Plan B: buying the DNC <https://pluralistic.net/2020/02/25/pluralistic-your-daily-link-dose-25-feb-2020/#plutewatch>

#5yrsago Cops' qualified immunity <https://pluralistic.net/2020/02/25/pluralistic-your-daily-link-dose-25-feb-2020/#moralhazard>

#5yrsago Russian Multiplication <https://pluralistic.net/2020/02/25/pluralistic-your-daily-link-dose-25-feb-2020/#mathski>

### Upcoming appearances ([permalink](https://pluralistic.net/2025/02/25/sneak-and-peek/#upcoming))

![A photo of me onstage, giving a speech, pounding the podium.](https://i0.wp.com/craphound.com/images/appearances2.jpg?w=840&ssl=1)
* NYC: Picks and Shovels with John Hodgman, Feb 26  
 <https://www.eventbrite.com/e/cory-doctorow-john-hodgman-picks-and-shovels-tickets-1131132841779>
* Penn State: Picks and Shovels, Feb 27  
 <https://www.bellisario.psu.edu/assets/uploads/CoryDoctorow-Poster.pdf>
* Doylestown, PA: Picks and Shovels at the Doylestown Bookshop, Mar 1  
 <https://www.eventbrite.com/e/cory-doctorow-picks-and-shovels-a-martin-hench-novel-tickets-1146230880419>
* Baltimore: Picks and Shovels with Maximillian Alvarez, Mar 2  
 <https://redemmas.org/events/cory-doctorow-presents-picks-and-shovels/>
* DC: Picks and Shovels with Matt Stoller, Mar 4  
 <https://www.loyaltybookstores.com/picksnshovels>
* Richmond, VA: Picks and Shovels with Lee Vinsel, Mar 5  
 <https://fountainbookstore.com/events/1795820250305>
* Virtual: With Great Power Came No Responsibility: How Enshittification Conquered the 21st Century and How We Can Overthrow It (Indiana University), Mar 7  
 <https://events.iu.edu/mediaiub/event/1783095-with-great-power-came-no-responsibility-how-enshitti>
* Austin: Reclaim, Reframe, Reimagine, Mar 7  
 <https://schedule.sxsw.com/2025/events/PP150498>
* Austin: Tensions in Creative Labor & Generative AI, Mar 8  
 <https://schedule.sxsw.com/2025/events/PP149418>
* Austin: The Next 25: A Conversation About the Future of Open, Mar 8  
 <https://www.classy.org/event/creative-commons'-open-house-for-an-open-future/e663144>
* Austin: Fediverse House, Mar 10  
 <https://about.flipboard.com/fediverse-house/>
* Austin: Picks and Shovels at First Light Books, Mar 10  
 <https://thethirdplace.is/event/cory-doctorow-picks-shovels-1>
* Burbank: Picks and Shovels with Wil Wheaton, Mar 13  
 <https://www.darkdel.com/store/p3257/Thu%2C_Mar_13th_6_pm%3A_Pick_%26_Shovel%3A_A_Martin_Hench_Novel_HB.html#/>
* Europa Park: Cloudfest, Mar 17-20  
 <https://cloudfest.link/>
* San Diego: Picks and Shovels at Mysterious Galaxy, Mar 24  
 <https://www.mystgalaxy.com/32425Doctorow>
* Virtual: Picks and Shovels at Imagine! Belfast, Mar 24  
 <https://www.eventbrite.co.uk/e/cory-doctorow-in-conversation-with-alan-meban-tickets-1106421399189>
* Chicago: Picks and Shovels with Peter Sagal, Apr 2  
 <https://exileinbookville.com/events/44853>
* Chicago: ABA Techshow, Apr 3  
 <https://www.techshow.com/>
* Bloomington: Picks and Shovels at Morgenstern, Apr 4  
 <https://morgensternbooks.com/event/2025-04-04/author-event-cory-doctorow>
* PDX: Teardown 2025, Jun 20-22  
 <https://www.crowdsupply.com/teardown/portland-2025>
* New Orleans: DeepSouthCon63, Oct 10-12, 2025  
 <http://www.contraflowscifi.org/>

![A screenshot of me at my desk, doing a livecast.](https://i0.wp.com/craphound.com/images/recentappearances2.jpg?w=840&ssl=1)
### Recent appearances ([permalink](https://pluralistic.net/2025/02/25/sneak-and-peek/#recent))

* The Culture Show  
 <https://www.wgbh.org/podcasts/the-culture-show/february-20-2025-chelsea-handler-cory-doctorow-and-the-red-bull-heavy-metal-contest-at-boston-city-hall>
* Picks and Shovels with Yanis Varoufakis and David Moscrop (Jacobin)  
 <https://www.youtube.com/watch?v=xkIDep7Z4LM>
* Forthright Radio  
 <https://forthright.media/2025/02/14/cory-doctorow-picks-and-shovels/>

![A grid of my books with Will Stahle covers..](https://i0.wp.com/craphound.com/images/recent.jpg?w=840&ssl=1)
### Latest books ([permalink](https://pluralistic.net/2025/02/25/sneak-and-peek/#latest))

* + Picks and Shovels: a sequel to "Red Team Blues," about the heroic era of the PC, Tor Books (US), Head of Zeus (UK), February 2025 (<https://us.macmillan.com/books/9781250865908/picksandshovels>).
* The Bezzle: a sequel to "Red Team Blues," about prison-tech and other grifts, Tor Books (US), Head of Zeus (UK), February 2024 ([the-bezzle.org](http://the-bezzle.org)). Signed, personalized copies at Dark Delicacies (<https://www.darkdel.com/store/p3062/Available_Feb_20th%3A_The_Bezzle_HB.html#/>).
* "The Lost Cause:" a solarpunk novel of hope in the climate emergency, Tor Books (US), Head of Zeus (UK), November 2023 (<http://lost-cause.org>). Signed, personalized copies at Dark Delicacies (<https://www.darkdel.com/store/p3007/Pre-Order_Signed_Copies%3A_The_Lost_Cause_HB.html#/>)
* "The Internet Con": A nonfiction book about interoperability and Big Tech (Verso) September 2023 (<http://seizethemeansofcomputation.org>). Signed copies at Book Soup (<https://www.booksoup.com/book/9781804291245>).
* "Red Team Blues": "A grabby, compulsive thriller that will leave you knowing more about how the world works than you did before." Tor Books <http://redteamblues.com>. Signed copies at Dark Delicacies (US):  [and Forbidden Planet (UK):](https://www.darkdel.com/store/p2873/Wed%2C_Apr_26th_6pm%3A_Red_Team_Blues%3A_A_Martin_Hench_Novel_HB.html#/) <https://forbiddenplanet.com/385004-red-team-blues-signed-edition-hardcover/>.
* "Chokepoint Capitalism: How to Beat Big Tech, Tame Big Content, and Get Artists Paid, with Rebecca Giblin", on how to unrig the markets for creative labor, Beacon Press/Scribe 2022 <https://chokepointcapitalism.com>
* "Attack Surface": The third Little Brother novel, a standalone technothriller for adults. The *Washington Post* called it "a political cyberthriller, vigorous, bold and savvy about the limits of revolution and resistance." Order signed, personalized copies from Dark Delicacies <https://www.darkdel.com/store/p1840/Available_Now%3A_Attack_Surface.html>
* "How to Destroy Surveillance Capitalism": an anti-monopoly pamphlet analyzing the true harms of surveillance capitalism and proposing a solution. <https://onezero.medium.com/how-to-destroy-surveillance-capitalism-8135e6744d59?sk=f6cd10e54e20a07d4c6d0f3ac011af6b>) (signed copies: <https://www.darkdel.com/store/p2024/Available_Now%3A__How_to_Destroy_Surveillance_Capitalism.html>)
* "Little Brother/Homeland": A reissue omnibus edition with a new introduction by Edward Snowden: <https://us.macmillan.com/books/9781250774583>; personalized/signed copies here: <https://www.darkdel.com/store/p1750/July%3A__Little_Brother_%26_Homeland.html>
* "Poesy the Monster Slayer" a picture book about monsters, bedtime, gender, and kicking ass. Order here: <https://us.macmillan.com/books/9781626723627>. Get a personalized, signed copy here: <https://www.darkdel.com/store/p2682/Corey_Doctorow%3A_Poesy_the_Monster_Slayer_HB.html#/>.

![A cardboard book box with the Macmillan logo.](https://i0.wp.com/craphound.com/images/upcoming-books.jpg?w=840&ssl=1)
### Upcoming books ([permalink](https://pluralistic.net/2025/02/25/sneak-and-peek/#upcoming-books))

* Enshittification: Why Everything Suddenly Got Worse and What to Do About It, Farrar, Straus, Giroux, October 2025  
 <https://us.macmillan.com/books/9780374619329/enshittification/>
* Unauthorized Bread: a middle-grades graphic novel adapted from my novella about refugees, toasters and DRM, FirstSecond, 2026
* Enshittification, Why Everything Suddenly Got Worse and What to Do About It (the graphic novel), Firstsecond, 2026
* The Memex Method, Farrar, Straus, Giroux, 2026

![](https://i0.wp.com/craphound.com/images/colophon2.jpeg?w=840&ssl=1)
### Colophon ([permalink](https://pluralistic.net/2025/02/25/sneak-and-peek/#bragsheet))

Today's top sources:

**Currently writing:** 

* Enshittification: a nonfiction book about platform decay for Farrar, Straus, Giroux. Status: second pass edit underway (readaloud)
* A Little Brother short story about DIY insulin PLANNING
* Picks and Shovels, a Martin Hench noir thriller about the heroic era of the PC. FORTHCOMING TOR BOOKS FEB 2025

**Latest podcast:** Picks and Shovels virtual launch with Yanis Varoufakis and David Moscrop, presented by Jacobin <https://craphound.com/novels/redteamblues/2025/02/16/picks-and-shovels-virtual-launch-with-yanis-varoufakis-and-david-moscrop-presented-by-jacobin/>

![](https://i0.wp.com/craphound.com/images/by.svg.png?w=840&ssl=1)
This work – excluding any serialized fiction – is licensed under a Creative Commons Attribution 4.0 license. That means you can use it any way you like, including commercially, provided that you attribute it to me, Cory Doctorow, and include a link to pluralistic.net.

<https://creativecommons.org/licenses/by/4.0/>

Quotations and images are not included in this license; they are included either under a limitation or exception to copyright, or on the basis of a separate license. Please exercise caution.

### How to get Pluralistic:

Blog (no ads, tracking, or data-collection):

[Pluralistic.net](http://pluralistic.net)

Newsletter (no ads, tracking, or data-collection):

<https://pluralistic.net/plura-list>

Mastodon (no ads, tracking, or data-collection):

<https://mamot.fr/@pluralistic>

Medium (no ads, paywalled):

<https://doctorow.medium.com/>

Twitter (mass-scale, unrestricted, third-party surveillance and advertising):

<https://twitter.com/doctorow>

Tumblr (mass-scale, unrestricted, third-party surveillance and advertising):

<https://mostlysignssomeportents.tumblr.com/tagged/pluralistic>

"*When life gives you SARS, you make sarsaparilla*" -Joey "Accordion Guy" DeVilla

ISSN: 3066-764X

The EU’s Digital Markets Act is playing on the hardest setting (and it doesn’t need to). The EU’s Digital Markets Act (DMA) is set to become law; it will require the biggest tech companies in the world (Apple, Google and Facebook, and maybe a few others) to open up their instant…

In "Medium"

Today's links The largest campaign finance violation in US history: The "greater fools" election. Hey look at this: Delights to delectate. This day in history: 2004, 2009, 2014, 2019, 2023 Upcoming appearances: Where to find me. Recent appearances: Where I've been. Latest books: You keep readin' em, I'll keep writin'…

In "bezzles"

Today's links Surveillance electoralism: Comparing the surveillance of the Biden and Trump apps. Blueleaks: Dox the police. Virtual Ignite talks: Weds at 6PM. Congress wants to read all your DMs: The EARN-IT Act doesn't mention encryption, but it still bans encryption. Privacy in tracing tokens: Bunnie Huang's parameters for a…

In "2020"
