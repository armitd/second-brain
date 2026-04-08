# Payments Are Easy (If You Know Who Everyone Is)

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4b4b43b-48aa-47c7-b03b-b2c4ec11aea3_1024x593.jpeg)

## Metadata
- Author: [[David G.W. Birch]]
- Full Title: Payments Are Easy (If You Know Who Everyone Is)
- Category: #articles
- Summary: In the year 1540, Sir Thomas Gresham (who later became Queen Elizabeth I's banker and is in many ways the father of the modern City of London) set out in true fintech pioneer style to evade capital controls and smuggle the equivalent of some $40 million in today's money from Antwerp to Calais on beh
- URL: https://dgwbirch.substack.com/p/payments-are-easy-if-you-know-who

## Full Document
### Payments Are Easy (If You Know Who Everyone Is)

##### When it comes down to it, it doesn't matter whether you are sending dollars or Dogecoin, the cost of identity is more than the cost of money.

In the year 1540, Sir Thomas Gresham (who later became Queen Elizabeth I's banker and is in many ways the father of the modern City of London) set out in true fintech pioneer style to evade capital controls and smuggle the equivalent of some $40 million in today's money from Antwerp to Calais on behalf of King Henry VIII. Nowadays he would have used bitcoins and run them through a few mixers, but due to the technological limitations of Tudor money transfer, he was forced to sneak out of the Low Countries with 25 bags of gold and silver coins.

(You would think that absolutely everyone would use bitcoins instead of gold for money transfer today but apparently not! Someone left 3Kg of gold on [a train in Switzerland](https://www.bbc.co.uk/news/world-europe-53041884) recently.)

Anyway, as John Guy notes [in his superb biography of Sir Thomas](https://www.amazon.co.uk/Greshams-Law-World-Elizabeth-Banker/dp/1788162366), for this highly risky cross-border transfer he was paid in the King’s cash money:

```
To [Thomas] now fell the risky task of conveying cash amounting to over £31,000(worth over £31 million today) for the mercenaries...

Gresham was lucky. The journey, in the event, took him less than a month.. he claimed the expedition had cost him £28 18s. od. (some £29,000).

Six weeks later, Henry's councillors finally issued the warrant that allowed Thomas to seek payment from the treasurer of the king's chamber. 
```

This means that the cost to the King was around nine basis points, or about one fifth as much as Wise charged me to transfer money from the US to the UK last week, although to be fair it did take Sir Thomas a month to get Henry's loot to him whereas with Wise it was a matter of seconds.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4b4b43b-48aa-47c7-b03b-b2c4ec11aea3_1024x593.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4b4b43b-48aa-47c7-b03b-b2c4ec11aea3_1024x593.jpeg)
*Sir Thomas Gresham. What a guy.*

But it does make me wonder about trajectory of the costs. Since Sir Thomas' escapades, we have invented laser beams and transistors: so how come it costs so much money to send money around? According to the World Bank, while remittances to low and middle-income countries reached a record high last year, the average transaction cost remains around [seven percent](https://bestexchangerates.com/info/remittances-reach-all-time-high).

The World Bank calculates an overall indicator called the “Global Weighted Average” remittance cost. This weights the average costs in a corridor by the estimated flow size to give a [useful global benchmark](https://bkauer.medium.com/338341e2493b). In Q1 2021 this was approximately 4.5%, around ten times what `I paid to move money between transatlantic bank accounts and about fifty times what it cost Henry VIII to move money across the Channel.

How can sending some photons cost so much more than sending a horse and cart?

Well, the fact is that the cost of moving the photons around is not the problem. The costs are not because of payments, they are because of identity. Cross-border funds transfers will at some point involve a regulated institution. A money transmitter might take money from a bank account in the UK and deposit it in a bank account in, say, India. This means that the bank has to carry out massively expensive Know-Your-Customer (KYC) investigations on the money transmitter and its customers as well as massively expensive Anti-Money Laundering (AML) monitoring of the transactions as well as massively expensive sanctions screening and so on. Meeting these Customer Due Diligence (CDD) standards is [expensive](https://www.moneyandbanking.com/commentary/2018/2/18/the-stubbornly-high-cost-of-remittances). As a result, there are significant barriers against cost-competitive technology firms who want to make inroads into the remittance business.

#### Costs Are Rising

A couple of years ago the Financial Action Task Force (FATF) extended their recommendations on CDD to include cryptocurrency exchanges and wallet providers (together referred to as Virtual Asset Service Providers, or "VASPs"). This meant that all countries should apply anti-money laundering and anti-terrorist financing controls whether the money is going by bank or by blockchain: that is, CDD and all that. All that, in particular, means applying the “Travel Rule" that aims to prevent money laundering by identifying the parties to a transaction when value over a certain amount are transferred.

The decision to apply [the same travel rule on VASPs](https://www.forbes.com/sites/pawelkuskowski/2020/05/10/fatf-travel-rule-beware-of-false-prophets/) as on traditional financial institutions was greeted with some dismay in the cryptocurrency world, because it meant that service providers must collect and exchange customer information during transactions. The technically non-binding guidance on how member jurisdictions should regulate their 'virtual asset' marketplace [included the contentious detail](https://www.paymentsjournal.com/new-guidelines-significantly-impacting-cryptocurrecy-exchanges/) that whenever a user of one exchange sends cryptocurrency worth more than 1,000 dollars or euros to a user of a different exchange, the originating exchange must send identifying information about both the sender and the intended recipient to the beneficiary exchange. Many people think even that limit is too high: Speaking at the "[V20 Virtual Asset Service Providers Summit](https://www.v20.io/)", Carole House from the Financial Crimes Enforcement Network, FinCEN, said that they want to see this threshold reduced to $250 for any transfers that go outside the US.

(The FATF has actually just completed its [second 12-month review](https://www.fatf-gafi.org/publications/fatfrecommendations/documents/second-12-month-review-virtual-assets-vasps.html) of the implementation of these VASP amendments, noting that less than half of their reporting jurisdictions have the rules in place and "gaps in implementation" mean that there is not yet a global regime in place to prevent the misuse of virtual assets for money laundering or terrorist financing.)

The information demanded is extensive. According to the [FATF Interpretive Note to Recommendation 16](https://ciphertrace.com/q3-2019-cryptocurrency-anti-money-laundering-report/), the information should include name and account number of the originator and benefactor, the originator's (physical) address, national identity number (or something similar) or date and place of birth. In essence, this means that counterparty's personal information will sent around the web.

(Simon Lelieveldt is a former Head of Department on Banking Supervision at the Dutch Central Bank. He is level-headed about such things, and he called this a "[disproportional silly measure by regulators who don't understand blockchain technology](http://moneyandpayments.simonl.org/2019/06/g20-and-fatf-should-not-infringe-on.html)", which may be a little harsh, but whatever the cryptocurrency folks might think about it they have no choice but to implement it.)

#### So What Will Reduce Costs?

Pär Liljert of the International Organization for Migration’s (IOM) says that compliance has been identified as a key cost for remittance service providers and said that [Now is the time to reduce remittance costs](https://weblog.iom.int/now-time-reduce-remittance-costs). So how can fintech help?

Perhaps fintech can attack the problem with the blockchain? The OECD's April 2020 Working Paper "[Can blockchain technology reduce the cost of remittances](https://read.oecd-ilibrary.org/development/can-blockchain-technology-reduce-the-cost-of-remittances_d4d6ac8f-en#page2)?" (Hint:no) identifies a number of limitations on the ability of blockchain technology to reduce remittance costs. In particular, it notes that cryptocurrency is unlikely to solve the "last mile" problem.

The OECD paper does, though, highlight the cost of KYC as one of the significant cost drivers and note the potential for the use of **digital identities** to help. At the same time, it raised questions about the possibilities of data misuse thereby deepening, as they put it, the "existing political asymmetries". The Brookings Institution "[How to keep remittances flowing](https://www.brookings.edu/blog/future-development/2020/06/11/how-to-keep-remittances-flowing/)" makes a similar point, calling for digital technology to meet risk-based KYC requirements to help address "de-risking" practices by correspondent banks (intended to avoid rather than manage risks) that continue to affect access to bank accounts for money transfer businesses operating in smaller and poorer remittance corridors, thus reducing competition. It seems to me, then, that if we can find a way to use digital identities but prevent the data misuse, then we (ie, the fintech industry) may actually be able to help the less well off.

When it comes to payments, the identity expenses are far greater than the payment expenses. So if we are going to reduce the cost of remittances, that is where we need to focus. Not as a special fix or temporary patch for remittances, but as part of a more general strategy to improve financial inclusion.

Carlos Torres Vila, Chairman of BBVA, has put forward [an interesting idea](https://www.weforum.org/agenda/2021/04/digital-id-is-the-catalyst-of-our-digital-future/) based on digital identities and data sharing. He suggests something along the lines of the [Financial Stability Board](https://www.fsb.org) (a global panel of regulators) but built for global digital assets. Such a body would develop data model standards, regulations and policies building in privacy protection along the lines of Europe's GDPR.

This "digital stability board" would give members the platform to share best practices and monitor risks in online commerce and other sectors. With such a board in place, data trusts (a structure that I think holds great promise: see [this piece](https://www.technologyreview.com/2021/02/24/1017801/data-trust-cybersecurity-big-tech-privacy/) in MIT Technology Review) could be built to manage individual and organisational data associated with digital identities. This would make the controlled and well-regulated sharing of vital information easier and more fluid while simultaneous protecting personally-identifiable information through the use of maturing privacy-enhancing technologies.

You see, the thing is, if someone knows who everyone is, then payments are easy. And cheap. Let’s stop talking about cryptocurrency and start talking about about digital identity. Who should that “someone” behind the digital identities be? The government? The central bank? Financial institutions? Telcos? Trusts run by financial institutions in some countries and perhaps the UN or NGOs in some countries? Let’s put our thinking caps on.
