# Bitcoin and the Rise of the Cypherpunks

![rw-book-cover](https://blog.lopp.net/content/images/2020/04/CYPHERPUNK.jpg)

## Metadata
- Author: [[Cypherpunk Cogitations]]
- Full Title: Bitcoin and the Rise of the Cypherpunks
- Category: #articles
- Summary: The text discusses the history and motivations behind the Cypherpunk movement that led to the creation of Bitcoin and its focus on privacy. It highlights key figures in the Cypherpunk community and their contributions to privacy and encryption technologies. The future of privacy in cryptocurrencies looks promising with ongoing developments such as zero-knowledge proofs and privacy-focused cryptocurrencies like Zcash.
- URL: https://blog.lopp.net/bitcoin-and-the-rise-of-the-cypherpunks/

## Full Document
While many of the innovations in the space are new, they’re built on decades of work that led to this point. By tracing this history, we can understand the motivations behind the movement that spawned bitcoin and share its vision for the future.

![Bitcoin and the Rise of the Cypherpunks](https://blog.lopp.net/content/images/size/w1140/2020/04/CYPHERPUNK.jpg)
From bitcoin to blockchain to distributed ledgers, the cryptocurrency space is fast evolving, to the point where it can be difficult to see in which direction it’s headed.

But, we’re not without clues. While many of the innovations in the space are new, they’re built on decades of work that led to this point. By tracing this history, we can understand the motivations behind the movement that spawned bitcoin and share its vision for the future.

Before the 1970s, cryptography was primarily practiced in secret by military or spy agencies. But, that changed when two publications brought it into the open: the US government publication of the [Data Encryption Standard](http://csrc.nist.gov/publications/fips/fips46-3/fips46-3.pdf) and the first publicly available work on public-key cryptography, “[New Directions in Cryptography](https://www-ee.stanford.edu/~hellman/publications/24.pdf)” by Dr Whitfield Diffie and Dr Martin Hellman.

In the 1980s, Dr David Chaum wrote extensively on topics such as anonymous digital cash and pseudonymous reputation systems, which he described in his paper “[Security without Identification](http://www.chaum.com/publications/Security_Wthout_Identification.html): Transaction Systems to Make Big Brother Obsolete”.

Over the next several years, these ideas coalesced into a movement.

In late 1992, Eric Hughes, Timothy C May, and John Gilmore founded a small group that met monthly at Gilmore’s company Cygnus Solutions in the San Francisco Bay Area. The group was humorously termed “cypherpunks” as a derivation of “cipher” and “cyberpunk.”

The Cypherpunks mailing list was formed at about the same time, and just a few months later, Eric Hughes published “[A Cypherpunk’s Manifesto](http://www.activism.net/cypherpunk/manifesto.html)“. He wrote:

> “Privacy is necessary for an open society in the electronic age. Privacy is not secrecy. A private matter is something one doesn’t want the whole world to know, but a secret matter is something one doesn’t want anybody to know. Privacy is the power to selectively reveal oneself to the world.”

That’s all good and well, you may be thinking, but I’m not a Cypherpunk, I’m not doing anything wrong; I have nothing to hide. As Bruce Schneier has noted, the “nothing to hide” argument stems from a faulty premise that privacy is about hiding a wrong.

For example, you likely have curtains over your windows so that people can’t see into your home. This isn’t because you are undertaking illegal or immoral activities, but simply because you don’t wish to worry about the potential cost of revealing yourself to the outside world.

If you’re reading this, you have directly benefited from the efforts of Cypherpunks.

Some notable Cypherpunks and their achievements:

* Jacob Appelbaum: Tor developer
* Julian Assange: Founder of WikiLeaks
* Dr Adam Back: Inventor of Hashcash, co-founder of Blockstream
* Bram Cohen: Creator of BitTorrent
* Hal Finney: Main author of PGP 2.0, creator of Reusable Proof of Work
* Tim Hudson: Co-author of SSLeay, the precursor to OpenSSL
* Paul Kocher: Co-author of SSL 3.0
* Moxie Marlinspike: Founder of Open Whisper Systems (developer of Signal)
* Steven Schear: Creator of the concept of the “warrant canary”
* Bruce Schneier: Well-known security author
* Zooko Wilcox-O’Hearn: DigiCash developer, Founder of Zcash
* Philip Zimmermann: Creator of PGP 1.0

#### **The 1990s**

This decade saw the rise of the Crypto Wars, in which the US Government attempted to stifle the spread of strong commercial encryption.

Since the market for cryptography was almost entirely military up to this point, encryption technology was included as a Category XIII item into the US Munitions List, which had strict regulations preventing its “export.”

This limited “export compatible” SSL key length to 40 bits, which could be broken in a matter of days using a single personal computer.

Legal challenges by civil libertarians and privacy advocates, the widespread availability of encryption software outside the US and a successful attack by Matt Blaze against the government’s proposed backdoor, the [Clipper Chip](https://en.wikipedia.org/wiki/Clipper_chip), led the government to back down.

![](https://blog.lopp.net/content/images/2020/04/clipper.gif)
In 1997, Dr Adam Back [created Hashcash](http://www.hashcash.org/papers/announce.txt), which was designed as an anti-spam mechanism that would essentially add a (time and computational) cost to sending email, thus making spam uneconomical.

He envisioned that Hashcash would be easier for people to use than Chaum’s digicash since there was no need for the creation of an account. Hashcash even had some protection against “double spending.”

Later in 1998, Wei Dai [published a proposal](http://www.weidai.com/bmoney.txt) for “b-money”, a practical way to enforce contractual agreements between anonymous actors. He described two interesting concepts that should sound familiar. First, a protocol in which every participant maintains a separate database of how much money belongs to user. Secondly, a variant of the first system where the accounts of who has how much money are kept by a subset of the participants who are incentivized to remain honest by putting their money on the line.

Bitcoin uses the former concept while quite a few other cryptocurrencies have implemented a variant of the latter concept, which we now call [proof of stake](https://en.wikipedia.org/wiki/Proof-of-stake).

#### **The 2000s**

It’s clear that Cypherpunks had already been building on each other’s work for decades, experimenting and laying the frameworks we needed in the 1990s, but a pivotal point was the creation of cypherpunk money in the 2000s.

In 2004, Hal Finney [created reusable proof of work](https://cryptome.org/rpow.htm) (RPOW), which built on Back’s Hashcash. RPOWs were unique cryptographic tokens that could only be used once, much like unspent transaction outputs in bitcoin. However, validation and protection against double spending was still performed by a central server.

Nick Szabo [published a proposal](http://unenumerated.blogspot.com/2005/12/bit-gold.html) for “bit gold” in 2005 – a digital collectible that built upon Finney’s RPOW proposal. However, Szabo did not propose a mechanism for limiting the total units of bit gold, but rather envisioned that units would be valued differently based upon the amount of computational work performed to create them.

Finally, in 2008, Satoshi Nakamoto, a pseudonym for a still-unidentified individual or individuals, published the [bitcoin whitepaper](http://bitcoin.org/bitcoin.pdf), citing both hashcash and b-money. In fact, [Satoshi emailed Wei Dai](http://www.gwern.net/docs/2008-nakamoto#section) directly and mentioned that he learned about b-money from Dr Back.

Satoshi dedicated a section of the [bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf) to privacy, which reads:

> “The traditional banking model achieves a level of privacy by limiting access to information to the parties involved and the trusted third party. The necessity to announce all transactions publicly precludes this method, but privacy can still be maintained by breaking the flow of information in another place: by keeping public keys anonymous. The public can see that someone is sending an amount to someone else, but without information linking the transaction to anyone. This is similar to the level of information released by stock exchanges, where the time and size of individual trades, the ‘tape’, is made public, but without telling who the parties were.”

*Bitcoin’s Privacy Model, from the Bitcoin whitepaper*
Satoshi Nakamoto triggered an avalanche of progress with a working system that people could use, extend and fork.

Bitcoin strengthened the entire cypherpunk movement by enabling organizations such as WikiLeaks to continue operating via bitcoin donations, even after the traditional financial system had cut them off.

#### **The Struggle for Privacy**

However, as the bitcoin ecosystem has grown over the past few years, privacy concerns seem to have been pushed to the backburner.

Many early bitcoin users assumed that the system would give them complete anonymity, but we have learned otherwise as various law enforcement agencies [have revealed](http://www.wired.com/2015/01/prosecutors-trace-13-4-million-bitcoins-silk-road-ulbrichts-laptop/) that they are able to deanonymize bitcoin users during investigations.

The [Open Bitcoin Privacy Project](http://www.openbitcoinprivacyproject.org/) has picked up some of the slack with regard to educating users about privacy and recommending best practices for bitcoin services. The group is developing a threat model for attacks on bitcoin wallet privacy.

Their model currently breaks attackers into several categories:

* **Blockchain Observers** – link different transactions together to the same identity by observing patterns in the flow of value.
* **Network Observers** – link different transactions and addresses together by observing activity on the peer to peer network.
* **Physical Adversaries** – try to find data on a wallet device in order to tamper with it or perform analysis upon it.
* **Transaction Participants –** create transactions that aid them in tracing and deanonymizing activity on the blockchain.
* **Wallet Providers** – may require personally identifiable information from users and then observe their transactions.

Jonas Nick at Blockstream has also done a fair amount of research regarding privacy concerns for bitcoin users.

He has an excellent presentation in which he uncovers a number of privacy flaws, some of which are devastating to SPV bitcoin clients:

Some content could not be imported from the original document. [View content ↗](https://www.youtube.com/embed/HScK4pkDNds?feature=oembed) 

One of the greatest privacy issues in bitcoin is from blockchain observers – because every transaction on the network is indefinitely public, anyone in the present and future can be a potential adversary.

As a result, one of the oldest recommended best practices is to never reuse a bitcoin address.

Satoshi even made note of it in the bitcoin whitepaper:

> “As an additional firewall, a new key pair should be used for each transaction to keep them from being linked to a common owner. Some linking is still unavoidable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner. The risk is that if the owner of a key is revealed, linking could reveal other transactions that belonged to the same owner.”

#### **Recent Cypherpunk Innovations**

A multitude of systems and best practices have been developed in order to increase the privacy of bitcoin users. Dr Pieter Wuille authored [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), hierarchical deterministic (HD) wallets, which makes it much simpler for bitcoin wallets to manage addresses.

While privacy was not Wuille’s primary motivation, HD wallets make it easier to avoid address reuse because the tech can easily generate new addresses as transactions flow into and out of the wallet.

Elliptic Curve Diffie-Hellman-Merkle (ECDHM) addresses are bitcoin address schemes that increase privacy. ECDHM addresses can be shared publicly and are used by senders and receivers to secretly derive traditional Bitcoin addresses that blockchain observers cannot predict. The result is that ECDHM addresses can be “reused” without the loss of privacy that usually occurs from traditional Bitcoin address reuse.

Some examples of ECDHM address schemes include [Stealth Addresses](https://github.com/genjix/bips/blob/master/bip-stealth.mediawiki) by Peter Todd, [BIP47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki) reusable payment codes by Justus Ranvier and [BIP75](https://github.com/techguy613/bips/blob/master/bip-0075.mediawiki) Out of Band Address Exchange by Justin Newton and others.

Bitcoin mixing is a more labor intensive method by which users can increase their privacy. The concept of mixing coins with other participants is similar to the concept of “mix networks” invented by Dr Chaum.

Several different mixing algorithms have been developed:

* [**CoinJoin**](https://bitcointalk.org/index.php?topic=279249.0) – Blockstream co-founder Gregory Maxwell’s original proposal for mixing coins, CoinJoin essentially lets users create a transaction with many inputs from multiple people and then send the coins to many other outputs that pay back to the same people, thus ‘mixing’ the values together and making it difficult to tell which inputs are related to which outputs.

Example of a naïve CoinJoin transaction.
[**JoinMarket**](https://github.com/JoinMarket-Org/joinmarket/wiki) – Built by developer Chris Belcher, JoinMarket enables holders of bitcoin to allow their coins to be mixed via CoinJoin with other users’ coins in return for a fee. It uses a kind of smart contract so that your private keys never leave your computer, thus reducing the risk of loss. Put simply, JoinMarket allows you to improve the privacy of bitcoin transactions for low fees in a decentralized fashion.

* [**CoinShuffle**](http://crypsys.mmci.uni-saarland.de/projects/CoinShuffle/coinshuffle.pdf) – A decentralized mixing protocol developed by a group of researchers at Saarland University in Germany, CoinShuffle improves upon CoinJoin. It does not require a trusted third party to assemble the mixing transactions and thus does not require additional mixing fees.
* [**CoinSwap**](https://bitcointalk.org/index.php?topic=321228) – Another concept developed by Maxwell, CoinSwap is substantially different from CoinJoin in that it uses a series of four multisig transactions (two escrow payments, two escrow releases) to trustlessly swap coins between two parties. It is much less efficient than CoinJoin but can potentially offer much greater privacy, even facilitating the swapping of coins between different blockchains.

While mixing is tantamount to “hiding in a crowd”, often the crowd is not particularly large. Mixing should be considered as providing obfuscation rather than complete anonymity, because it makes it difficult for casual observers to trace the flow of funds, but more sophisticated observers may still be able to deobfuscate the mixing transactions.

Kristov Atlas (founder of the Open Bitcoin Privacy Project) [posted his findings](https://www.coindesk.com/blockchains-sharedcoin-users-can-identified-says-security-expert/) on weaknesses in improperly implemented CoinJoin clients back in 2014.

*CoinJoin input and output grouping*
Atlas noted that even with a fairly primitive analysis tool, he was able to group 69% of inputs and 53% of a single CoinJoin transaction’s outputs.

There are even separate cryptocurrencies that have been developed with privacy in mind.

One example is Dash, designed by Evan Duffield and Daniel Diaz, which has a feature called “[Darksend](https://www.dash.org/darksend/)“ – an improved version of CoinJoin. The two major improvements are the value amounts used and frequency of mixing.

Dash’s mixing uses common denominations of 0.1DASH, 1DASH, 10DASH AND 100DASH in order to make grouping of inputs and outputs much more difficult. In each mixing session, users submit the same denominations as inputs and outputs.

To maximize the privacy offered by mixing and make timing attacks more difficult, Darksend runs automatically at set intervals.

*DASH mixing. Source: DASH whitepaper*
Another privacy-focused cryptocurrency is not even based on bitcoin. The [CryptoNote](https://cryptonote.org/inside/) whitepaper was released in 2014 by Nicolas van Saberhagen, and the concept has been implemented in several cryptocurrencies such as Monero. The primary innovations are cryptographic ring signatures and unique one-time keys.

Regular digital signatures, such as those used in bitcoin, involve a single pair of keys – one public and one private. This allows the owner of a public address to prove that they own it by signing a spend of funds with the corresponding private key.

Ring signatures were [first proposed in 2001](http://download.springer.com/static/pdf/432/chp%253A10.1007%252F3-540-45682-1_32.pdf?originUrl=http%3A%2F%2Flink.springer.com%2Fchapter%2F10.1007%2F3-540-45682-1_32&token2=exp=1458913055~acl=%2Fstatic%2Fpdf%2F432%2Fchp%25253A10.1007%25252F3-540-45682-1_32.pdf%3ForiginUrl%3Dhttp%253A%252F%252Flink.springer.com%252Fchapter%252F10.1007%252F3-540-45682-1_32*~hmac=9ced274de2c18a3f6ef7ca4a1147092b366f1b5f0167b6e45835a24f2c9ec5da) by Dr Adi Shamir and others, building upon the group signature scheme that was [introduced in 1991](http://download.springer.com/static/pdf/412/chp%253A10.1007%252F3-540-46416-6_22.pdf?originUrl=http%3A%2F%2Flink.springer.com%2Fchapter%2F10.1007%2F3-540-46416-6_22&token2=exp=1458913679~acl=%2Fstatic%2Fpdf%2F412%2Fchp%25253A10.1007%25252F3-540-46416-6_22.pdf%3ForiginUrl%3Dhttp%253A%252F%252Flink.springer.com%252Fchapter%252F10.1007%252F3-540-46416-6_22*~hmac=9007c9e97a349ddd8789d9a97e26f496a6ff6b761af18c704ba28ff1e2c744ac) by Dr Chaum and Eugene van Heyst. Ring signatures involve a group of individuals, each with their own private and public key.

The “statement” proved by a ring signature is that the signer of a given message is a member of the group. The main distinction with the ordinary digital signature schemes is that the signer needs a single secret key, but a verifier cannot establish the exact identity of the signer.

Therefore, if you encounter a ring signature with the public keys of Alice, Bob and Carol, you can only claim that one of these individuals was the signer, but you will not be able to know exactly to whom the transaction belongs. It provides another level of obfuscation that makes it more difficult for blockchain observers to track the ownership of payments as they flow through the system.

Interesting enough, ring signatures were developed specifically in the context of whistleblowing, as they enable the anonymous leaking of secrets while still proving that the source of the secrets is reputable (an individual who is part of a known group.)

*Ring Signatures. Source: https://cryptonote.org/inside/*
CryptoNote is also designed to mitigate the risks associated with key reuse and input-to-output tracing. Every address for a payment is a unique one-time key, derived from both the sender’s and the recipient’s data. As soon as you use a ring signature in your input, it adds more uncertainty as to which output has just been spent.

If a blockchain observer tries to draw a graph with used addresses, connecting them via the transactions on the blockchain, it will be a tree because no address was used twice. The number of possible graphs rises exponentially as you add more transactions to the graph since every ring signature produces ambiguity as to how the value flowed between the addresses.

Thus, you can’t be certain of which address sent funds to another address.

Depending on the size of the ring used for signing, the ambiguity for a single transaction can vary from “one out of two” to “one out of 1,000”. Every transaction increases the entropy and creates additional difficulty for a blockchain observer.

*Blockchain analysis resistance. Source: https://cryptonote.org/inside/*
#### **Upcoming Cypherpunk Innovations**

While there are still many privacy concerns for cryptocurrency users, the future is bright due to the ongoing work of Cypherpunks.

The next leap forward in privacy will involve the use of zero-knowledge proofs, which were [first proposed in 1985](https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Proof%20Systems/The_Knowledge_Complexity_Of_Interactive_Proof_Systems.pdf) in order to broaden the potential applications of cryptographic protocols.

[Originally proposed](https://bitcointalk.org/index.php?topic=305791.0) by Dr. Back in 2013 as “bitcoins with homomorphic value”, Maxwell has been working on [Confidential Transactions](https://youtu.be/9pyVvq-vrrM?t=2107), which use zero-knowledge range proofs to enable the creation of bitcoin transactions in which the values are hidden from everyone except the transaction participants.

This is a great improvement on its own, but when you combine Confidential Transactions with CoinJoin then you can build a mixing service that severs any links between transaction inputs and outputs.

When Maxwell presented Sidechain Elements at the San Francisco Bitcoin Devs meetup, I recall him saying “One of the greatest regrets held by the greybeards at the [IETF](https://www.ietf.org/) is that the Internet was not built with encryption as the default method of transmitting data.”

Maxwell clearly feels the same way about privacy in bitcoin and wishes that we had Confidential Transactions from the very beginning. We have already seen Blockstream [implement confidential transactions](https://www.coindesk.com/blockstream-commercial-sidechain-bitcoin-exchanges/) within the Liquid sidechain in order to mask transfers between exchanges.

We also recently saw Maxwell conduct the first successful [zero-knowledge contingent payment](https://bitcoincore.org/en/2016/02/26/zero-knowledge-contingent-payments-announcement/) on the bitcoin network. ZKCP is a transaction protocol that allows a buyer to purchase information from a seller using bitcoin in a trustless manner. The purchased information is only transferred if the payment is made, and it is guaranteed to be transferred if the payment is made. The buyer and seller do not need to trust each other or depend on arbitration by a third party.

I [wrote about Zerocoin](https://medium.com/@lopp/zerocoin-zero-knowledge-for-infinite-anonymity-b38322a46767) several years ago and noted the technical challenges that it needed to overcome before the system could be useable. Since then, researchers have managed to make the proofs much more efficient and have [solved the trust problem](https://z.cash/blog/snark-parameters.html) with the initial generation of the system parameters. We are now on the cusp of seeing Zerocoin’s vision realized with the release of [Zcash](https://z.cash/), headed by Wilcox-O’Hearn.

Zcash offers total payment confidentiality while still maintaining a decentralized network using a public blockchain. Zcash transactions automatically hide the sender, recipient and value of all transactions on the blockchain. Only those with the correct view key can see the contents of a transaction. Since the contents of Zcash transactions are encrypted and private, the system uses a novel cryptographic method to verify payments.

Zcash uses a zero-knowledge proof construction called a zk-SNARK, developed by its team of experienced cryptographers.

Instead of publicly demonstrating spend-authority and transaction values, the transaction metadata is encrypted and zk-SNARKs are used to prove that the transaction is valid. Zcash may very well be the first digital payment system that enables foolproof anonymity.

#### **Putting the Punk in Cypherpunk**

In the decades since the Cypherpunks set forth on their quest, computer technology has advanced to the point where individuals and groups can communicate and interact with each other in a totally anonymous manner.

Two persons may exchange messages, conduct business and negotiate electronic contracts without ever knowing the true name or legal identity of the other. It is only natural that governments will try to slow or halt the spread of this technology, citing national security concerns, use of the technology by criminals and fears of societal disintegration.

![](https://pbs.twimg.com/profile_images/1025457837026275329/F51xxiuX.jpg)

[CNBC Now](https://twitter.com/CNBCnow)
[@CNBCnow](https://twitter.com/CNBCnow)

Obama: If govt. can’t crack encryption, then people are walking around "with a Swiss bank account in their pocket."  
[amp.twimg.com/v/7aa7d704-eb4…](https://amp.twimg.com/v/7aa7d704-eb42-4f20-87ec-a9ab6e9badc3)

[Posted Mar 11, 2016 at 10:07PM](https://twitter.com/CNBCnow/status/708414144181972992)

Cypherpunks know that we must defend our privacy if we expect to have any. People have been defending their privacy for centuries with whispers, darkness, envelopes, closed doors, secret handshakes and couriers.

Prior to the 20th century, technology did not enable strong privacy, but neither did it enable affordable mass surveillance.

We now live in a world where surveillance is to be expected, but privacy is not, even though privacy enhancing technologies exist. We have entered a phase that [many](http://www.economist.com/news/business/21631055-intelligence-agencies-and-tech-firms-have-little-choice-compromise-crypto-wars-20) [are](https://www.techdirt.com/articles/20141107/08193529077/demonizing-strong-encryption-welcome-to-crypto-wars-20.shtml) [calling](http://www.gnovisjournal.org/2016/03/17/crypto-wars-2-0-fbi-v-apple/) The Crypto Wars 2.0.

Although the Cypherpunks emerged victorious from the first Crypto Wars, we cannot afford to rest upon our laurels. Zooko has experienced the failure of Cypherpunk projects in the past and [he warns](https://epicenterbitcoin.com/podcast/122/) that failure is still possible.

![](https://pbs.twimg.com/profile_images/1008479914612277248/xcnlNQOu.jpg)

[zooko❤ⓩ🛡🦓🦓🦓](https://twitter.com/zooko)
[@zooko](https://twitter.com/zooko)

Dear fellow Bitcoiners: no, we cannot just rest assured that Bitcoin's unique value prop outweighs all other considerations.

[Posted Jan 6, 2016 at 8:26PM](https://twitter.com/zooko/status/684833495278026756)

Cypherpunks believe that privacy is a fundamental human right, including privacy from governments. They understand that the weakening of a system’s security for any reason, including access by “trusted authorities”, makes the system insecure for everyone who uses it.

Cypherpunks write code. They know that someone has to write software to defend privacy, and thus they take up the task. They publish their code so that fellow Cypherpunks may learn from it, attack it and improve upon it.

Their code is free for anyone to use. Cypherpunks don’t care if you don’t approve of the software they write. They know that software can’t be destroyed and that widely dispersed systems can’t be shut down.

—–BEGIN PGP SIGNED MESSAGE—–  

Hash: SHA256

Public Key: https://keybase.io/lopp/key.asc

The original Cypherpunks mailing list no longer exists, but there are more Cypherpunks now than ever before. We discuss our ideas on a wide variety of email lists, chat rooms, and social media platforms. There is much work to be done; while great progress has been made designing and deploying privacy enhancing systems, they are still far from perfect and it is still far too difficult for the average person to benefit from them. There are many battles left to be fought in the Crypto Wars; take up your keyboards and let us proceed together apace.  

—–BEGIN PGP SIGNATURE—–

wsFcBAEBCAAQBQJW9VrFCRAnjdn7DA6bSQAAI68QAKxMRyGXfr8g0xhNJadJFaH6  

iXJlv+PA74h3oSKV97lOAejY8yGyhyb8UodF5H3YBqSrLUCEF2Xj8U4pCl5imvSe  

uuRfxbSeyUcgMonxF8W4dswcU0Ls1znLbpVkoLiRNAkkFVG+LyGY0eC7dDQ17okf  

mTzjaW6/3Ed289+yz7Lj5fE6pST4L7IsOEdlyPSm/1Rn6jLVaQ/WoNGB/xPUjNZw  

zagpg5qHGgcTCHCPZR9i1obsJtKLHLCRhCCxHQ6ldAiLXJn0WeOCHYIRhaC4fr0P  

C+yBB2BwzXccVh4PUvgc4OEXTFvZUCkvUd88Z3j5ZN8r0ZJB83ZPITk7TMueneYW  

Ery21LXG2Wv+CACwPzE+LM9GkaOLkEDgiENDq20CsM6VQl3GkiCj3KdFl9btYvzw  

tpiHbmvE4HMepiVc4TjhEmIiCTMAjkcn0MRQl/tJsPw5dyQBs22++O/cslzc3w+T  

Ky+7DA4jIbMk993FpDsZwyqpvkPXWylLofbqq6DmLYCu1ahpdV8X18kApeY0W2E8  

rsPDr4eukXnLdDemoqFDtsIYDPb/LdQe5RaXuH7/xpWzWuOccOe305pUZnic7CO3  

5cVnSg7KgUjfZhfHPijyTzHKO8QShSl7bSMW/botaO9C/wha0/+qmnWVMdUwBVyj  

BLDeMjqvB87UbJE5E7rl  

=hR9e  

—–END PGP SIGNATURE—–
