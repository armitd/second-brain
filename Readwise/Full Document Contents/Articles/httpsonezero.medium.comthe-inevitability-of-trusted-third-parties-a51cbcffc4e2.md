# https://onezero.medium.com/the-inevitability-of-trusted-third-parties-a51cbcffc4e2

![rw-book-cover](https://miro.medium.com/v2/resize:fit:838/1*23BdcHNlNP66l0xvBtWUVA.png)

## Metadata
- Author: [[Cory Doctorow]]
- Full Title: https://onezero.medium.com/the-inevitability-of-trusted-third-parties-a51cbcffc4e2
- Category: #articles
- Summary: The author argues that blockchain technology does not solve trust issues in transactions; it merely adds complexity and costs while still relying on trusted third parties. Despite the excitement around blockchain for social good, many projects fail to address underlying problems of fraud and mistrust. Ultimately, the belief that financial incentives are the best motivators may lead to exploitation rather than genuine cooperation.
- URL: https://doctorow.medium.com/the-inevitability-of-trusted-third-parties-a51cbcffc4e2

## Full Document
#### The search for a crypto use-case continues

![](https://miro.medium.com/v2/resize:fit:700/1*23BdcHNlNP66l0xvBtWUVA.png)*Monroe H. Rosenfeld, “Finnegan the Umpire,” courtesy of* [*Library of Congress*](https://www.loc.gov/item/ihas.200033373/)
“Did you know that 87% of all conversations about blockchain technology are nonconsensual?”

It’s already an old joke, but it’s sure aged well.

Hardly a day goes by without someone demanding that I listen to their explanation of their blockchain idea. A lot of times, I listen. Look, a lot of people I consider to be smart and thoughtful are really excited by this stuff, and I know them well enough to believe them when they say they’re not excited about the possibility that they can get in on the ground floor of [a Ponzi scheme](https://www.youtube.com/watch?v=YQ_xWvX1n9g) and exit with a bunch of suckers’ money.

There’s a common thread running through most — possibly all — of the blockchain-for-good pitches I listen to: the idea that we can replace fallible, untrustworthy people with immutable, decentralized ledgers, and ask them to serve as referees and/or escrow agents in complex transactions between strangers who don’t have any reason to trust one another.

That’s no trivial proposition! The lack of trust among strangers is the source of many costs and inefficiencies in our society. Thirty percent of American health care spending is administration, and nearly all of that is insurers making sure they’re not getting ripped off by doctors and doctors making sure they’re not getting ripped off by insurers. Grocers station watchful overseers by the self checkout to make sure we’re scanning before we bag. Insurance companies pay adjusters to come and inspect your house when you make a claim. There’s a whole sector of our economy, a vast workforce, that does nothing but try to detect and prevent betrayal.

Imagine if we could outsource that to math! Imagine the human liberation — the ability of all those people freed from the drudgery of checking ID and comparing signatures and scrutinizing expense reports to move on to rewarding, productive work.

On its face, the idea of a computer as umpire sounds plausible. It’s easy to think of a computer as “neutral” and “unbiased,” a system built up of crisp ones and zeroes, untroubled by squishy, qualitative factors.

But [qualitative factors are damned stubborn](https://locusmag.com/2021/05/cory-doctorow-qualia/).

Here’s an example. Back before the lockdown, I met a smart, committed person from an NGO who had a blockchain-for-good project they were very excited about. They were putting agricultural commodities on the blockchain, permanently and publicly recording the seed varietals, the pesticide use, the labor conditions, and the financial arrangements that went into the bag of grain or bushel of fruit you were being offered at the grocery store. This would prevent the “greenwashing” and fair-trade-washing that is (apparently?) a real problem with “ethical produce.”

If it’s true that there’s a lot of fakery going on in the labeling of our vegetables and grains (which sounds plausible), then I want to prevent it. But can this system really do that? Not as far as I could tell.

Here are the two questions I asked this committed, sincere person about this blockchain application:

1. How do I know that the information in the blockchain is accurate? That is, how do I know that if the blockchain says a potato was grown without pesticide, that the person who inscribed that entry upon the ledger wasn’t lying?
2. How do I know that the produce I find in the grocery store is the produce that the blockchain entry refers to? Maybe someone, somewhere, grew an ethical potato, but how can I tell that *this* potato, which I am holding in my hand, is that ethical potato?

And here was the answer: “You just have to trust it.” I mean, the answer was dressed up some: “We’ll have auditors who’ll certify that the blockchain entries are truthful, and that produce isn’t falsely associated with certificates of ethical production.”

That is to say, we’ll have umpires. Trusted third parties.

But the problem this sets out to solve is that we can’t trust the umpires. There is (apparently) produce on the shelves whose growing conditions aren’t what they’re claimed to be. Blockchain merely records those umpires’ judgement in a permanent and public place — it doesn’t make that judgement trustworthy, nor does it provide a way to detect liars.

In other words:

**if: problem + blockchain = problem - blockchain  

then: blockchain = 0**

The blockchain hasn’t added anything to the situation, except considerable cost (which could just as easily be spent on direct transfers to poor farmers, assuming you could find someone you trust to hand out the money) and complexity (which creates lots of opportunities for cheating).

This carries on beyond mere records in the blockchain. Every smart contract application I’ve heard of has this problem, too.

For example, [this](https://user.well.com/engaged.cgi?c=inkwell.vue&t=516&a=r) sounds like a really interesting and well-thought-through smart contract application:

```
This one is a contract between the NFT owner and my company, which  
guarantees that we have bought-and-retired carbon credits to cover  
the physical mining of the gold bullion that is being sold. It also  
covers the CO2 emissions of the NFT issuing process.Clause 20 has the arbitration machinery.We've worked fairly closely with the UK government on arbitration  
rules for blockchain asset disputes.<https://www.pinsentmasons.com/out-law/news/new-dispute-rules-envisage-direct-to->  
blockchain-enforcement-arbitral-decisionsThe rules themselves are here:  
<https://35z8e83m1ih83drye280o9d1-wpengine.netdna-ssl.com/wp-content/uploads/2021>  
/04/Lawtech_DDRR_Final.pdfWe get a name check on page 4.So what's being built out here is a very tightly bound legal  
framework for buying and selling physical goods, with suites of  
Ricardian contracts creating legally-enforceable claims about what  
the goods are **DRAWN ON THIRD PARTIES**. Those third parties do not  
benefit from the sale of the goods themselves, they make a living  
providing legal warranties on the goods - they're essentially third  
party inspectors with no economic interest in the situation other  
than by selling insurance on the fact that something (for example)  
contains no slave labour.We work with a world class anti-slavery expert on a long term  
project to drive slavery out of the supply chain using exactly these  
kinds of certification protocols. I would estimate it will be two  
years before we are doing this at an industrial scale - it is very  
complicated - but the will is overwhelming and the technical, legal  
and slavery-prevention expertise is sufficient. We are going to do  
this, do it right, and do it at scale. It took us a couple of years  
to get CO2 done, and now all the NFTs we produce attached are fully  
offset.
```

But the more I think about this smart contract, the fewer reasons I can find for it to be a smart contract instead of just, you know, a *contract.*

As Vinay Gupta — the creator of this system and someone I have a lot of respect for — says, right there in the text, the entire system relies on third party arbiters to make sure that the parties involved don’t rip each other off, that no one uses slave labor, that the carbon is all offset through various schemes, and so on.

The point is, all of that could be a deception. The only reason to trust it is that you trust the auditors who have signed the scheme.

I don’t mean to pooh-pooh the role of auditors here. Auditors are great. In fact, we’re in the middle of several kinds of serious economic crises because [we allowed auditors to become an oligopoly of hopelessly conflicted megafirms](https://pluralistic.net/2021/06/04/aaronsw/#crooked-ref), and they are [cheating like crazy](https://www.nakedcapitalism.com/2018/01/fallout-carillion-collapse-hits-kpmg.html), and so much of the world is broken as a result.

We know that the big auditing firms are riddled with fraud. We know that [carbon offsets](https://pluralistic.net/2021/11/17/do-well-do-good-do-nothing/#greenwashing) are among [the most fraudulent](https://pluralistic.net/2021/07/26/aggregate-demand/#murder-offsets) instruments that companies make.

I don’t get how blockchain fixes any of this.

But maybe, blockchain makes it worse.

I mean, let’s just stipulate that we all understand that [proof-of-work is a climate disaster](https://www.nytimes.com/2021/10/10/business/dealbook/crypto-climate.html). Let’s pretend for a moment that proof-of-stake (or, possibly, something based on [remote attestation](https://pluralistic.net/2022/01/30/ring-minus-one/#drm-political-economy)) will imminently replace proof-of-work and sort out the climate issue.

Fundamental to every blockchain project that I’ve looked at is the idea that getting good things out of groups of people involves aligning their financial incentives. That is the bedrock ideology of the blockchain, the unspoken belief that the best way to motivate people is to demonstrate that a certain course of action will make them, personally, better off.

This ideology is unspoken in blockchain circles, as is its corollary: that we can’t reliably motivate people in *other ways*, like, by appealing to their sense of solidarity or goodwill.

I don’t mean to say that no one in blockchainland believes in the public good. There are blockchain projects that are explicitly designed to fund actual *public goods*, those pernicious things that we all need but no one wants to pay for.

But the underlying method of coordinating groups of people by financial means is an absolute *fraud magnet.* The white-hot market for NFTs means that nearly everything that has NFT on it [is a fraud](https://web3isgoinggreat.com/?id=2022-01-27-3). The anonymity and speed of blockchain pile-ons means that you never know [when you’re giving $169,000,000 to a convicted thief](https://web3isgoinggreat.com/?id=2022-01-27-0).

Governance tokens sound like a great way to manage deliberations around collective enterprises, but unless you have an actual contract (that is, not a smart contract), [you have no way to make your project’s manager honor the votes you and your friends make](https://web3isgoinggreat.com/?id=2022-01-30-0) with your governance tokens.

Even assuming the climate issues can be solved, smart contracts and DAOs and ledger entries are needless complexity. (A smart contract is just a computer program, and computer programs are buggy, so you can think of a smart contract as a bug bounty whose potential value is everything in every wallet connected to it.) That complexity introduces more security vulnerabilities, not fewer.

And the ideology of smart contracts, DAOs and ledger entries is grifter catnip, which means that all that complexity will attract people who will exploit it.

Which is a shame. Because, honestly, we need more trust. Mistrust is a drag on our society and our species. Mistrust — and the bad actors who engender it — threatens every one of our collective enterprises, [even wonderful things like Creative Commons](https://doctorow.medium.com/a-bug-in-early-creative-commons-licenses-has-enabled-a-new-breed-of-superpredator-5f6360713299).

I’ve been mulling this over a lot, and I have come up with exactly *one* kind of transaction that smart contracts can make more efficient: synthetic, complex financial derivatives, of the sort that gave rise to the 2008 Great Financial Crisis.

Here’s how those worked. Alice borrows money from Bob’s Bank for her mortgage. Bob sells the mortgage to Carol, who gets the money from Alice every month when she pays her mortgage. (This is a “collateralized debt obligation” or CDO.) Carol is worried that Alice might decide not to pay her mortgage, so she takes out an insurance policy with Dan, who effectively makes a wager: “Every month, if Alice pays her mortgage on time, you have to pay me $10. If Alice doesn’t pay her mortgage, I’ll pay you the full outstanding amount.” (This is an insured CDO.)

But along comes Erin. She doesn’t want to lend money to Alice, but she does want to get in on the bet, so she goes to Dan and says, “I want the same wager. Every month, if Alice pays her mortgage, I’ll give you $10. Every month, if Alice doesn’t pay her mortgage, you give me the full, outstanding amount, same as you would for Carol.” (This is a “synthetic CDO.”)

These synthetic CDOs allowed the Dans of the finance world to create gigantic income flows of insurance premiums — bets on mortgages that the bettor had no stake in. It also allowed those Dans to create new bonds that were a mix of the payments from mortgages, the premiums for insurance policies on those payments, and the payments for side-bets on the ability of borrowers to pay. The Dans of the world could mint an effectively limitless number of these, because there was no limit to the number of bets they could take on Alice’s mortgage.

That’s what nearly destroyed the global financial system and ushered in [a crisis whose fallout is still raining down upon us](https://pluralistic.net/2022/01/27/extraordinary-popular-delusions/#wall-street-slumlords).

And as far as I can tell, this is one application where smart contracts are more efficient and better than plain old contracts.

You see, if Alice pays her mortgage to Carol via the blockchain, then Erin and Dan can have a smart contract based on those payments. If Alice misses a payment, the smart contract can see that — because it’s all on-chain — and settle Erin and Dan’s wager instantly and automatically.

As reference applications go, this isn’t very promising. The last thing we need are more complex financial derivatives. Fourteen years after the Great Financial Crisis, we still have a vast surplus of those.

And trust is still in short supply.

*Cory Doctorow (*[*craphound.com*](https://craphound.com/)*) is a science fiction author,* [*activist*](https://www.eff.org/about/staff/cory-doctorow)*, and* [*blogger*](https://pluralistic.net/)*. He has a* [*podcast*](http://craphound.com/podcast/)*, a* [*newsletter*](https://mail.flarn.com/mailman/listinfo/plura-list)*, a* [*Twitter feed*](https://twitter.com/doctorow/)*, a* [*Mastodon feed*](https://mamot.fr/@pluralistic)*, and a* [*Tumblr feed*](http://mostlysignssomeportents.tumblr.com/)*. He was born in Canada, became a British citizen and now lives in Burbank, California. His latest nonfiction book is* [*How to Destroy Surveillance Capitalism*](https://onezero.medium.com/how-to-destroy-surveillance-capitalism-8135e6744d59)*. 1His latest novel for adults is* [*Attack Surface*](http://craphound.com/attacksurface/)*. His latest short story collection is* [*Radicalized*](https://craphound.com/radicalized/)*. His latest picture book is* [*Poesy the Monster Slayer*](https://craphound.com/category/poesy/)*. His latest YA novel is* [*Pirate Cinema*](https://craphound.com/category/pc/)*. His latest graphic novel is* [*In Real Life*](https://us.macmillan.com/books/9781596436589)*. His forthcoming books include Chokepoint Capitalism: How to Beat Big Tech, Tame Big Content, and Get Artists Paid (with Rebecca Giblin), a book about artistic labor market and excessive buyer power; Red Team Blues, a noir thriller about cryptocurrency, corruption and money-laundering (Tor, 2023); and The Lost Cause, a utopian post-GND novel about truth and reconciliation with white nationalist militias (Tor, 2023).*
