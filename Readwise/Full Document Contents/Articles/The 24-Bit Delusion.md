# The 24-Bit Delusion

![rw-book-cover](https://cdn11.bigcommerce.com/s-210bb/product_images/uploaded_images/24-bit-off.jpg)

## Metadata
- Author: [[Arjuna Das]]
- Full Title: The 24-Bit Delusion
- Category: #articles
- Summary: The article discusses the reality of high-definition audio formats like 24-bit recordings, highlighting that they often do not provide significantly better sound quality than 16-bit recordings. It explains that most playback systems cannot fully utilize the dynamic range of 24-bit recordings, which leads to the compression of audio files. Ultimately, the perceived differences in sound quality are more often related to the quality of remastering rather than the bit depth itself.
- URL: https://www.mojo-audio.com/blog/the-24bit-delusion/

## Full Document
![The 24-Bit Delusion](https://cdn11.bigcommerce.com/s-210bb/images/stencil/789x789/uploaded_images/24-bit-off.jpg?t=1498412488)
###### UPDATED: 7.25.21

###### Introduction:

More and more music has become available in “high-definition” (HD) digital formats, such as 24-bit 192KHz downloads, 24-bit 88.2KHz MQA streaming, and DSD. Now I hear talk about developing a new 32-bit 384KHz standard for HD music. Interestingly enough, not everyone agrees that greater bit depth and higher sampling rates are good things.

This blog will explain the math and physics of digital recording and musical reproduction in layman's terms so that you can decide for yourself if this is progress or simply marketing madness.

If you're not sure if you should believe the statements in this blog which contradict much of the marketing hype, myth, and legend in the audiophile industry, feel free to check the references at the end.

You also may want to refer to my other blog on [“DSD vs. PCM: Myth vs. Truth.”](http://www.mojo-audio.com/blog/dsd-vs-pcm-myth-vs-truth/)

###### Bits, Bytes, and Digital Words:

So why did 24-bit become the new standard?

When digital data is transferred and manipulated it is moved in bytes rather than as individual bits. There are 8 bits to a byte and a byte is known as a digital word. This is why everything in the digital world is divisible by 8. So 16 bits = 2 bytes and 24 bits = 3 bytes. Both 16 bits and 24 bits became standards because each represented the next digital word.

Historical note: The 16-bit format existed long before 16-bit digital-to-analog converters (DACs) were available.

###### Sampling Rate and Bit Depth:

The process of converting analog sound waves into a digital format is known as “quantization,” which is often represented as points plotted on an XY axis. The horizontal X axis represents time or sampling frequency and the vertical Y axis represents amplitude or bit depth. In the graphic below the white wave form represents the musical signal being quantized and the green step pattern overlaid represents the quantized values.

[![PCM Quantizing](https://mojoaudiofiles.files.wordpress.com/2014/10/pcm-quantizing.jpg?w=379&h=234)](https://mojoaudiofiles.files.wordpress.com/2014/10/pcm-quantizing.jpg)
Sampling rate is the frequency at which the amplitude of the analog sound wave is sampled. The 44.1KHz sampling frequency specified for Red Book CDs sample the amplitude of the music 44,100 times each second. The 96KHz sampling frequency used in the 7.1 channel audio embedded into DVDs and Blu-Rays sample the amplitude 96,000 times each second.

Bit depth translates to the number of steps the amplitude of the analog sound wave is divided into at each sampling. A 16-bit recording has 65,536 steps, a 20-bit recording has 1,048,576 steps, and a 24-bit recording has 16,777,216 steps. Yes, you read that correctly: a 24-bit recording has 256 times the number of amplitude steps as a 16-bit recording.

The more bits and/or the higher the sampling rate used in quantization, the higher the theoretical resolution. So a 16-bit 44.1KHz Red Book CD has 28,901,376 sampling points each second (44,100 x 65,536). And a 24-bit 192KHz recording has 32,212,254,000,000 sampling points each second (192,000 x 16,777,216). This means 24-bit 192KHz recordings have over 111,455 times the theoretical resolution of a 16-bit 44.1KHz recording. No small difference.

So why is it that HD recordings sound only slightly better than a 16-bit 44.1KHz recordings made from identical masters? Later in this blog I’ll explain the difference between theoretical and actual resolution.

###### Dynamic Range and Bit Depth:

Dynamic range is the difference in volume between the quietest and the loudest passage. Dynamic range is measured in decibels (dB).

Just for reference, here are some examples of dynamic range that most of us can relate to:

* The sound of a mosquito flying 3 meters away is 0dB.
* The hum of an incandescent bulb at 1 meter away is 10dB.
* The background noise in a quiet recording studio is 20dB.
* The background noise in a normal quiet room is about 30dB.
* Early analog master tape had a dynamic range of only 60dB.
* LP micro-groove records have a dynamic range of 65dB.
* Dolby increased analog master tape dynamic range to 90dB.
* The sound of a jackhammer at 1 meter away is 110dB.
* The sound of a full orchestra at 1 meter away is 120dB.
* Over 130dB causes irreparable hearing loss.
* The sound of a jet aircraft at takeoff is 140dB.

In a digital recording 1-bit = 6dB:

* 16-bit Red Book CDs have a dynamic range of 96dB.
* 20-bit digital master tape has a dynamic range of 120dB.
* 24-bit HD formats have a dynamic range of 144dB.

But wait…isn’t the background noise in a quiet room 30dB?

So you can’t actually hear the difference between the dynamic range of a 16-bit recording and a 20-bit recording unless you turn the volume up high enough above the 30dB background noise that it would cause hearing damage.

So why on Earth would they even create a digital recording format that can't even be listened to?!?!?!?!?

Simple: bit-depths and sampling rates far above the range of human hearing are used during the recording, editing, mixing, and mastering processes to lower digital noise in audible spectrum when recordings are downsampled to the significantly lower resolution sold in commercially released recordings.

###### Noise Floor:

Dynamic range is the loudest possible sound and noise floor is the quietest.

We already know that a quiet room has a background noise level of about 30db that we need to rise above. Even if the system is playing above the 30db room noise, the power supply in a DAC will mask the LSB if the peak-to-peak voltage of the noise in the power supply is not less than the voltage of the LSB.

In order for a DAC to actually resolve a specific bit depth the peak-to-peak voltage of the ripple in the power supply has to be lower than the voltage of the LSB. And in order for a DAC to resolve a specific sampling rate the speed of the power supply has to be faster than the sampling frequency.

Based on a 2.5V output of a single-ended DAC (about average), below are the voltages power supply noise must be below in order to hear the LSB:

* 16-bit LSB noise floor voltage = 76uV
* 20-bit LSB noise floor voltage = 4.75uV
* 24-bit LSB noise floor voltage = 0.3uV

For a reference, the common LM317 power regulator, the quality used in most commercial electronics, has about 150uV peak-to-peak noise and the best ultralow-noise power regulators used in the best-of-the-best of audiophile electronics have about 5uV of peak-to-peak noise. So even the 5V output of a balanced DAC could not resolve anything close to the LSB voltage of a 24-bit recording.

Sorry to burst anyone's bubble and contradict the marketing hype, myth, and legend in the audiophile industry, but just because a DAC is capable of decoding 24-bits doesn't mean it is capable of actually resolving that bit-depth in its analog output stage.

According to the experts who manufacture the finest DAC chips, resistors, and power regulators, there is theoretically no way to make electronics that are capable of discerning much greater than a 20-bit resolution (120dB dynamic range). Any company who claims 24-bit resolution from their DAC is simply full of shit. Oh they can decode 24-bits, because 24-bits does exist on the digital side, but the analog output stage in the world's best DACs are not capable of resolving much more than 20-bits of dynamic range.

And don't even get me started on DACs with tube output stages: the lowest noise floor of a tube output stage is about 90dB which means despite whatever a manufacturer may claim no tube DAC can even resolve the dynamic range in a 16-bit recording let alone a 24-bit recording.

###### Theoretical vs. Actual Resolution:

According to [Dr. Nyquist's theorem](https://www.sciencedirect.com/topics/engineering/nyquist-theorem), sampling at twice the maximum audible frequency yields a perfect reproduction of the audio waveform. Any higher resolution will only plot more points along the same curves.

So in order to correctly sample a 20KHz note, the maximum frequency human ears can hear, you would need to sample at greater than 40KHz. The 44.1KHz sampling rate of a Red Book CD was engineered to allow a 20KHz sound to be recorded accurately.

Sorry to be the one to burst your bubble, but despite what many audiophiles may believe, less than one person in a thousand can hear anything above 20KHz as a child and there is almost no one over the age of 40 who can hear much above 15KHz.

So why would there be any need for higher sampling frequencies than 44.1KHz?

One reason is quantization noise. Since quantization noise is present around the sampling frequency of a PCM recording, a 44.1KHz recording has quantization noise one octave above the human hearing limit of 20KHz. This quantization noise needs to be filtered out, so all DACs have a low-pass filter at the output. Because the quantization noise is only one octave above audibility the filters used have a very steep slope so as to not filter out desirable high frequencies. These steeply sloped low-pass digital filters are commonly known as "brick wall" filters.

Though you hear a lot about "brick wall" filters causing an audible distortion in the top end of early Red Book CD players , the fact is that was only a small part of the reason early Red Book CDs and players had an unnatural sounding top end. Most of the hard, harsh, unnatural sounding high frequencies in early digital had more to do with flaws in the power supplies and flaws in the recording process, not "brick wall" filters.

In order to lower the quantization noise in the audible spectrum professional formats, such as 24-bit 352.8KHz DXD, were developed for recording studios. The reasons 24-bit DAC chips were developed was so recording engineers could monitor their their recording, editing, mixing, and mastering in real-time without having to downsample. Of course the companies who produced DAC chips stopped producing the lower resolution DAC chips. And companies who manufactured consumer electronics used these 24-bit DAC chips and began to make creative marketing claims about their products.

Even though many recordings are advertised as being 24-bit, only a small portion of the 24 bits of dynamic range are actually used. These so-called 24-bit recordings are compressed down to a dynamic range that most electronics are capable of producing. I'm not talking high-end audiophile electronics, but rather your average car stereo, phone, or MP3 player. Commercial recordings with more than 40dB of dynamic range have peaks which would clip out most electronics at a very low volume. There are more details on how dynamic range effects electronics in the following section on "Playback Equipment Requirements."

So what do they do with commercially marketed so-called 24-bit recordings? They simply fill in the Most Significant Bits (MSB) with 1s and the Least Significant Bits (LSB) with 0s and center the actual dynamic range. Even most of the best of audiophile recordings have less than 70dB of dynamic range. They could have released a recording of identical performing in 16-bits, but because naive consumers have been tricked into believing the BS marketing messages regarding 24-bits, the record companies put an average of 5-7 bits of dynamic range in a 24-bit format. How silly.

DSD is no different. Though you can't directly relate DSD in terms of bit depth and sampling frequency, a rough estimate is that DSD64 (aka SACD or single-rate DSD) is fairly close in resolution to a 24-bit 88.2KHz PCM recording. But instead of having quantization noise centered around the sampling frequency like PCM, DSD64 has significant amounts of digital noise just above 25KHz, as is shown in the graphic below.

![](https://www.mojo-audio.com/product_images/uploaded_images/dsd-noise.jpg)
To get around this problem Delta-Sigma DACs have noise-shaping algorithms and many upsample to higher frequencies to move the quantization noise to a high enough frequency so that it can be filtered out with a minimum of distortion in the audible range. This is one of the reasons why computer audio player software that upsamples DSD64 to Double-Rate or Quad-Rate DSD makes such an improvement in Delta-Sigma DAC performance. This is also one of the reasons why upsampling to high rates improves the performance of PCM files decoded by most Delta-Sigma DACs.

Another reason why upsampling improves the performance in Delta-Sigma DACs is that they use statistical error correction algorithms, so the more data points, the more accurate the error correction. This is what tricks many audiophiles into believing that higher sampling frequencies above the 2X bandwidth that Dr. Nyquist stated will yield higher resolution. This is not true for R-2R ladder DACs. Upsampling to 88.2KHz is enough to remove any digital artifacts from the audible spectrum when using an R-2R DAC.

For more detailed information on this topic refer to my blog on [“DSD vs. PCM: Myth vs. Truth.”](http://www.mojo-audio.com/blog/dsd-vs-pcm-myth-vs-truth/)

Another consideration of higher sampling rates and greater bit depth is system resources. Both require more storage space, more RAM, faster processors, and higher current power supplies. Though the optimal sampling frequency and bit-depth which are required to reproduce accurate music are a matter of heated debate, there is no doubt that excessive resolution unnecessarily uses up system resources and unnecessarily increases the size and cost of components. Also note that the faster processors and higher current power supplies required to process higher resolutions or to do high upsampling are inherently noisier.

###### Playback Equipment Requirements:

There are very few systems, even among the best-of-the-best, which can accurately play back the full 120dB dynamic range of a 20-bit recording. This is why few commercial recordings have higher than 6-bits of dynamic range , let alone the 144dB dynamic range of a 24-bit recording. Keep in mind that the maximum dynamic range of micro-groove LP records is only 65dB and the maximum dynamic range of pro-audio Dolby analog master tapes is 90dB.

There was wisdom to the LP record and the analog tape standards. The relationship between amplifier wattage and decibels (dB) of volume is logarithmic not linear. Manufacturers knew that for every 3dB consumers raised their volume, they would have to double the wattage of their amplifier and double the output of the speakers. So keeping the dynamic range of consumer recording under 60dB is much of what allowed home entertainment equipment to be affordable, of modest size, and relatively high-fidelity.

So that 120dB live music can be played on most systems, recording studios limit the dynamic range using a process called “dynamic compression.” The process of dynamic compression makes the quieter passages relatively louder and the louder passages relatively more quiet. This makes it easier to discern low-level details from the louder passages. When music is properly dynamically compressed it allows you to listen at a reasonable volume and still hear all the subtle harmonic cues that reveal the tone, timbre, and room acoustics in a recording.

Think about it: a 60dB dynamic range on top of a 30dB background noise equals 90db. How much louder than 90dB do you want to listen to music in your home? More importantly, for every additional 3dB you increase dynamic range, you would need to double the wattage of your amplifier and double the output of your speakers.

All things being equal, to go from 90dB output up to 99dB, you would need an amplifier with 8 times the wattage and speakers with 8 times the output. To accurately reproduce a recording at 120dB, you would need an amplifier with 1,024 times the wattage and speakers with 1,024 times the output than it would take to reproduce the same recording at 90dB. I don’t know about you, but a system like that will neither fit in my room nor my budget.

###### Summary:

Well, all that’s a real ear opener, isn’t it?

When people claim to hear significant differences between 16-bit and 24-bit recordings it is not the difference between the bit depths that they are hearing, but most often the difference in the quality of the digital remastering. And most recordings are engineered to sound best on a car stereo or portable device as opposed to on a high-end audiophile system. It’s a well-known fact that artists and producers will often listen to tracks on an MP3 player or car stereo before approving the final mix.

The quality of the recording plays a far more significant role than the format or resolution it is distributed in. But to increase profits, many modern recording studio executives insist that errors be edited out in post-production, significantly compromising the quality of the original master tapes. So no matter what format these recordings are released in, the music will always sound mediocre, since you can never have higher performance than what is on the original masters.

In contrast, some of my favorite digital recordings were digitally mastered from 1950s analog recordings. Many of these recordings were done as a group of musicians playing in a room with one take per track and no post-production editing. Though these recordings have much higher background noise being limited by old-school pre-Dolby 60dB dynamic range master tape, they retain an organic character and in-the-room harmonic cues that can't be duplicated any other way.

###### Hear It for Yourself:

Are you curious about the potential of digital-to-analog conversion?

[Mojo Audio’s Mystique EVO DAC](https://mojo-audio.com/digital-to-analog-converters/) has the purest digital conversion possible.

* A true non-oversampling R-2R ladder DAC design.
* No noise-shaping, upsampling, or oversampling algorithms.
* MSB zero-crossing voltage adjustment circuitry to optimize linearity.
* Perfectly bit-aligned left and right channel hardware-based demultiplexing.
* Direct-coupled with no output capacitors or transformers to distort phase and time or narrow bandwidth.
* LC choke-input power supplies, which unlike capacitive power supplies, store both current and voltage.

The [Mystique](https://mojo-audio.com/digital-to-analog-converters/) is in a class by itself. Explosive micro-dynamics combined with harmonically coherent micro-details reveal the true time, tune, tone, and timbre of the original musical performance.

With [Mojo Audio’s 45-day no-risk audition](http://www.mojo-audio.com/terms-of-sale/) you can hear the [Mystique DAC](https://mojo-audio.com/digital-to-analog-converters/) for yourself, in your own system, with no-risk and no restocking fees. Experience all the harmonic coherency and emotional content digital music is capable of delivering.

If you like what you've read in this blog and are interested in getting more free tips and tricks, check out the rest of my [blogs](https://www.mojo-audio.com/blog/) on our website. Also, sign up for our [e-newsletter](https://mojo-audio.us5.list-manage.com/subscribe?u=dac4cb8b1a9c1ae066c296308&id=ab0c47357f) to get more useful info as well as discount coupons, special offers, and first looks at new products.

Enjoy!

Benjamin Zwickel   

 Owner, Mojo Audio

###### References:

[http://www.lavryengineering.com/lavry-white-papers/](http://www.lavryengineering.com/pdfs/lavry-white-paper-the_optimal_sample_rate_for_quality_audio.pdf)

<http://www.highendnews.info/technology/oversampling_and_bitstream_metho.htm>

<http://www.grimmaudio.com/site/assets/files/1088/dsd_myth.pdf>

<http://bitperfectsound.blogspot.com/2014/12/dst-compression.html>

<http://www.soundonsound.com/sos/sep07/articles/digitalmyths.htm>

<http://www.digitalpreservation.gov/formats/fdd/fdd000230.shtml>

<https://en.wikipedia.org/wiki/Direct_Stream_Digital>

<http://hometheaterreview.com/super-audio-compact-disc-sacd/>

<http://en.antelopeaudio.com/blog/>

<http://benchmarkmedia.com/blogs/news/15121729-audio-myth-24-bit-audio-has-more-resolution-than-16-bit-audio>

Note: many of the graphics used in this blog were adapted from graphics taken from these reference sources.
