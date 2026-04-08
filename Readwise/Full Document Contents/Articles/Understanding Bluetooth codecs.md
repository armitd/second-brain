# Understanding Bluetooth codecs

![rw-book-cover](https://sgatlas.wpengine.com/wp-content/uploads/2017/12/Understanding-Bluetooth-codecs-hero.jpg)

## Metadata
- Author: [[Lily Katz]]
- Full Title: Understanding Bluetooth codecs
- Category: #articles
- Summary: All products featured are independently chosen by us. However, SoundGuys may receive a commission on orders placed through its retail links. See our ethics statement. Thanks to the frustrating demise of the cellphone headphone jack, Bluetooth’s presence is more ubiquitous than ever.
- URL: https://www.soundguys.com/understanding-bluetooth-codecs-15352/

## Full Document
![Title card which reads, "understanding Bluetooth codecs."](https://sgatlas.wpengine.com/wp-content/uploads/2017/12/Understanding-Bluetooth-codecs-hero.jpg)
Thanks to the frustrating demise of the cellphone [headphone jack](https://www.soundguys.com/was-ditching-the-headphone-jack-a-good-idea-13825/), Bluetooth’s presence is more ubiquitous than ever. Now, you don’t have to be an audio geek for Bluetooth codecs to be of importance: as well as audio quality variations, different codecs introduce different latencies, have varying degrees of energy efficiency, and different levels of stability. These might be important considerations, depending on your use case. If you’re going wireless, invest in headphones that support a high bitrate codec like aptX or AAC for iPhone users. In order to bring you up to speed in a matter of minutes, we’ve put together this guide for understanding Bluetooth codecs.

*Editor’s note: this article was updated on July 6, 2021, to update some technical wording and to add a contents menu.*

#### What you should know about audio and compression

[![SBC aptX aptX HD AAC LDAC bluetooth codecs profile audio](https://sgatlas.wpengine.com/wp-content/uploads/2017/12/Types-of-audio-formats_LK.jpg)[Uncompressed, lossless compressed and lossy compressed formats each have their own place in the digital audio ring.](https://www.soundguys.com/wp-content/uploads/2017/12/Types-of-audio-formats_LK.jpg)](https://www.soundguys.com/wp-content/uploads/2017/12/Types-of-audio-formats_LK.jpg)

* Basic terms
	+ *Sample rate (Hz):* the number of points of data per second in an audio file. You need at least two samples per cycle for a digital signal to represent any given frequency, so audio is typically sampled at a rate of 44.1kHz—approximately twice the upper limit of human hearing (20kHz). “High-resolution” file formats are considered to be 96kHz or greater. A greater sample rate means a greater file size.
	+ *[Bit depth](https://www.soundguys.com/audio-bit-depth-explained-23706/) (-bit):* the number of digital bits used to represent each audio sample. A higher bit depth records a signal more accurately. CD-quality is 16-bit, but high-resolution files extend this to 24-bit. A greater bit depth multiplies the file size.
	+ *[Bit rate](https://www.soundguys.com/high-bitrate-audio-is-overkill-cd-quality-is-still-great-16518/) (kbps or Mbps):* the amount of audio data transferred per second. This is calculated by multiplying the sample rate by the bit-depth.
* Data rates can be [unstable](https://www.soundguys.com/5-reasons-not-to-buy-bluetooth-headphones-12150/).
	+ Bluetooth devices have an assigned range (typically 10 meters for headphones). This is because the further you get from the source, the more [interference](https://www.soundguys.com/why-true-wireless-connectivity-bad-20673/) from physical barriers (e.g., walls, objects, people) and overlapping radio frequencies (e.g., microwaves, Wi-Fi signals).
* [*Psychoacoustics*](https://www.soundguys.com/podcast-the-mp3-revolution-17850/) studies how humans perceive sound. A psychoacoustic model is applied to digital media, and determines what can be deleted to save space without a noticeable loss of sound quality.
	+ This is how [MP3 compression](https://www.soundguys.com/podcast-the-mp3-revolution-17850/) came into the world. Its influence on strategic compression extends to virtually every audio format.
* There are three main types of [audio compression](https://www.soundguys.com/audio-compression-explained-29148/) formats, *uncompressed*, *lossless*, and *lossy*.

#### What are Bluetooth codecs?

[![A picture of the Plantronics BackBeat Pro 5100 true wireless earbuds outside of the case and surrounded by water splashes.](https://sgatlas.wpengine.com/wp-content/uploads/2019/12/Plantronics-BackBeat-Pro-5100-true-wireless-earbuds-case-water-resistant-ip.jpg)[Not all true wireless earbuds support aptX and AAC, the Plantronics BackBeat Pro 5100 only supports the latter.](https://www.soundguys.com/wp-content/uploads/2019/12/Plantronics-BackBeat-Pro-5100-true-wireless-earbuds-case-water-resistant-ip.jpg)](https://www.soundguys.com/wp-content/uploads/2019/12/Plantronics-BackBeat-Pro-5100-true-wireless-earbuds-case-water-resistant-ip.jpg)

Now that you’ve passed *Wireless Audio 101*, let’s continue.

A *codec* determines how Bluetooth transmits from the source device to your headphones. It encodes and decodes digital audio data into a specific format. In an ideal world, a high-fidelity signal would be possible at the minimum specified bit rate, resulting in the least amount of space and bandwidth required for storage and transmission. Lower bitrates actually mean better compression but *worse* sound quality, a high bitrate means *better* sound quality and worse compression. So how do codecs navigate this compromise?

##### Low-complexity sub-band codec (SBC)

[![SBC aptX aptX HD AAC LDAC bluetooth codecs profile audio](https://sgatlas.wpengine.com/wp-content/uploads/2017/12/BT-Codecs-kbps_LK-2.jpg)[Represented is the max transfer rate (kbps) of each respective Bluetooth codec (greater is better). Each waveform depicts a transfer rate of 100kbps.](https://www.soundguys.com/wp-content/uploads/2017/12/BT-Codecs-kbps_LK-2.jpg)](https://www.soundguys.com/wp-content/uploads/2017/12/BT-Codecs-kbps_LK-2.jpg)

SBC divides the signal into multiple frequency bands and encodes each one independently. Think of SBC as the lowest common denominator among Bluetooth codecs. It’s not the best. It is, however, mandatory among *all* A2DP-enabled devices, making it virtually universal. Manageable transfer rates (192-320kbps) are delivered at the expense of significant data loss.

##### Qualcomm aptX, aptX LL, aptX HD, and aptX Adaptive

[![Graph of Bluetooth Codec Latency by Android Smartphone](https://sgatlas.wpengine.com/wp-content/uploads/2019/04/Bluetooth-Codec-Latency-by-Smartphone-e1554288678837.jpg)[Android's Bluetooth latency is all over the map.](https://www.soundguys.com/wp-content/uploads/2019/04/Bluetooth-Codec-Latency-by-Smartphone-e1554288678837.jpg)](https://www.soundguys.com/wp-content/uploads/2019/04/Bluetooth-Codec-Latency-by-Smartphone-e1554288678837.jpg)

Now, Qualcomm’s proprietary codecs, [aptX, aptX LL, and aptX HD](https://www.soundguys.com/the-ultimate-guide-to-bluetooth-aptx-and-aptx-hd-19914/) receive frequent recommendations here at *SoundGuys*, not to mention [aptX Adaptive](https://www.soundguys.com/aptx-adaptive-explained-18768/). Though only aptX LL supports a latency of fewer than 40 milliseconds. What’s more, Android’s wireless [efficiency is inconsistent](https://www.soundguys.com/android-bluetooth-latency-22732/) depending on what source device is used.

Bluetooth's Achilles' Heel is its limited bandwidth. High transfer rates may overload available bandwidth, causing a stutter—or complete crash—of the streaming service.

Why choose aptX over SBC? Greater transfer rates preserve more data. The simpler aptX codec supports 48kHz/16-bit LPCM audio data (352kbps), while aptX HD supports 48kHz/24-bit LPCM audio data (576kbps). Though both are lossy formats, they’re leagues ahead of SBC. Plus, they support a fine enough bit rate to keep everything running smoothly and sounding phenomenal.

**You might like: [Best aptX Bluetooth headphones](https://www.soundguys.com/best-aptx-bluetooth-headphones-29530/)**

[![A chart showing the AAC Bluetooth codec's performance on the Huawei P20 Pro, Samsung Galaxy Note 8, LG V30, and Apple iPhone 7.](https://sgatlas.wpengine.com/wp-content/uploads/2018/10/aac-enhanced-view-fr.jpg)[AAC performance differs depending on your source device.](https://www.soundguys.com/wp-content/uploads/2018/10/aac-enhanced-view-fr.jpg)](https://www.soundguys.com/wp-content/uploads/2018/10/aac-enhanced-view-fr.jpg)

[AAC](https://www.soundguys.com/the-ultimate-guide-to-bluetooth-headphones-aac-20296/) is the audio standard for lossy digital audio compression. It also happens to be the license-free standard for [YouTube](https://www.soundguys.com/youtube-music-premium-review-25622/), and for [Apple](https://www.soundguys.com/apple-airpods-pro-review-27106/) devices. If you have an Android phone, you won’t necessarily benefit from AAC as its performance is unreliable: it’s a power-hungry codec, and [our testing](https://www.soundguys.com/dont-use-airpods-android-20767/) has shown that Android devices don’t handle it effectively. iPhone users will certainly benefit from its higher-resolution playback though. It has a transfer rate cap of 250kbps, creating a file similar to that of a mid-quality MP3.

[![A photo showing someone using the touch controls of the Sony WF-1000XM4.](https://sgatlas.wpengine.com/wp-content/uploads/2021/06/sony-wf-1000xm4-review-in-use.jpg)[Most of Sony’s Bluetooth headphones use the LDAC codec, including the WF-1000XM4. You need a compatible phone to take advantage of, however.](https://www.soundguys.com/wp-content/uploads/2021/06/sony-wf-1000xm4-review-in-use.jpg)](https://www.soundguys.com/wp-content/uploads/2021/06/sony-wf-1000xm4-review-in-use.jpg)

Like Qualcomm, Sony has its own Bluetooth codec, [LDAC](https://www.soundguys.com/ldac-ultimate-bluetooth-guide-20026/). Its variable bit rate is the defining feature. In theory, it should consistently transfer up to 3x the data compared to SBC. But both aptX and SBC outperform LDAC when it streams at 330kbps, which is the default chosen by many phones. In order to change this, you have to enter developer settings and force a higher bit rate, but smartphones’ “best efforts” vary greatly.

| Phone | LG V30+ | Samsung Galaxy Note 8 | Huawei P20 Pro | Huawei P20 | Google Pixel 3 XL | Google Pixel 3 |
| --- | --- | --- | --- | --- | --- | --- |
| LDAC 'Best Effort' Setting | 990kbps | 660kbps | 660kbps | 660kbps | 330kbps | 330kbps |

LDAC was initially limited to Sony products but has been part of the [Android Open Source Project](https://www.androidauthority.com/android-4-2-1-aosp-134726/) (AOSP) since Android 8.0 “Oreo.”

[![A picture of the Huawei P30 (rear) with an Android Authority Editor's Choice badge in the top-right corner.](https://sgatlas.wpengine.com/wp-content/uploads/2019/06/Huawei-P30-Back-Editors-Choice-1000x563-1.jpg)[Android Authority The Huawei P30 Pro also includes a headphone jack for listeners serious about audio quality.](https://www.soundguys.com/wp-content/uploads/2019/06/Huawei-P30-Back-Editors-Choice-1000x563-1.jpg)](https://www.soundguys.com/wp-content/uploads/2019/06/Huawei-P30-Back-Editors-Choice-1000x563-1.jpg)

LHDC stands for low-latency and high-definition audio codec and was developed by the Hi-Res Wireless Audio (HWA) Union and Savitech. This codec allows for three times the data transmission afforded by SBC and supports a maximum bitrate of 900kbps with a max sample rate of 96kHz. The [Huawei Mate 10](https://www.androidauthority.com/huawei-mate-10-pro-review-807465/) was the first smartphone to support LHDC. It’s supported by Android 10 and up, and is part of the AOSP.

The low-latency audio codec (LLAC/LHDC LL) is an alternative to LHDC and boasts low-latency features that are ideal for [gamers](https://www.soundguys.com/gaming-headset-guide-21951/). End-to-end latency is as low as 30ms, and it supports bitrates of 400/600kbps and a max sample rate of 48kHz up to 24bits. The Huawei P30 was the first smartphone to support LLAC.

##### Bluetooth LE Audio LC3 codec

[Bluetooth LC3](https://www.soundguys.com/bluetooth-le-audio-lc3-explained-28192/) is a relatively recent addition, which offers more efficient and higher quality audio, and aids the deaf and [hard of hearing](https://www.soundguys.com/noise-induced-hearing-loss-17420/). According to [Fraunhofer](https://www.iis.fraunhofer.de/en/ff/amm/communication/lc3.html), the company that helped develop LC3, packet loss management is more advanced which results in a smoother degradation process. This means when you reach the outer edge of the wireless range afforded by your headset, rather than hearing distinct, distracting stutters and drops, the data loss will be audibly smoother.

LE Audio benefits the hearing impaired by expanding the functionality of Bluetooth hearing aids due to multi-stream support. Multi-stream audio allows multiple audio streams to be transmitted between a smartphone and earbuds simultaneously. In practice, this means your hearing aids can stream audio while also keeping you aware of your surroundings.

Similarly, it can transmit different streams to a pair of [true wireless earphones](https://www.soundguys.com/best-true-wireless-earbuds-14313/) simultaneously: rather than a single 160kbps stream, it may send two streams of 80kbps each. If you and your friend are at a bar watching a game, one of you can tune into the home team’s announcer with the left earbud while the other can opt for information about the visitors via the right bud.

[![A picture of the Samsung Galaxy Buds earbuds in the case on top of a Samsung Galaxy S10e in Flamingo Pink.](https://sgatlas.wpengine.com/wp-content/uploads/2019/03/Samsung_Galaxy-Buds-4.jpg)[The Samsung Galaxy Buds are the perfect companion to the Samsung Galaxy S10 phones.](https://www.soundguys.com/wp-content/uploads/2019/03/Samsung_Galaxy-Buds-4.jpg)](https://www.soundguys.com/wp-content/uploads/2019/03/Samsung_Galaxy-Buds-4.jpg)

The Samsung Scalable Codec was announced with the [Samsung Galaxy Buds](https://www.soundguys.com/samsung-galaxy-buds-plus-vs-galaxy-buds-29427/) which was developed with [AKG](https://www.soundguys.com/akg-k371-review-30284/). It prioritizes stability by making constant adjustments to streaming rates, so listeners are less likely to experience connection stutters and drops. It’s similar to how LC3 audio is said to manage packet loss, both result in less audio chopping by actively accommodating bitrate to signal strength.

#### Now what?

As you can see, it’s easy to get lost in Bluetooth jargon. Remember that higher transfer rates are good, but no matter how great the kbps: you need both your phone and headphones to speak the same language. Again, aptX and aptX **Adaptive** are usually your best bet with consumer-grade headphones. Qualcomm’s codec is becoming increasingly prevalent and low latency is a feature that many of us greatly appreciate.

We’ve barely scratched the surface here. In fact, we’re just beginning to look upon the surface. If you want to learn more, head over to our all-encompassing [Bluetooth codec guide](https://www.soundguys.com/ultimate-guide-to-bluetooth-headphones-20019/).

**Next: [Why I’m sticking to wired headphones](https://www.soundguys.com/why-wired-headphones-20518/)**

#### FAQ

AAC, aptX Low Latency, and the upcoming LC3/LC3+ codecs will have the least delay over wireless. However, we can’t guarantee which codecs will be available to you with your computer—that varies from device to device. [Android devices in particular](https://www.soundguys.com/android-bluetooth-latency-22732/) are all over the map when it comes to latency, but Windows should be fine.

This depends on your source device. iOS devices will fair best with AAC, while Android devices will do well with aptX or [aptX LL](https://www.aptx.com/aptx-low-latency). LDAC is fine, but its higher kbps performance isn’t quite as reliable as 660kbps and support for the codec is relatively difficult to find compared to [aptX](https://www.soundguys.com/best-aptx-bluetooth-headphones-29530/).
