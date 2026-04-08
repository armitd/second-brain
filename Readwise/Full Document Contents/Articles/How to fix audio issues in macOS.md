# How to fix audio issues in macOS

![rw-book-cover](https://www.digitaltrends.com/wp-content/uploads/2015/05/Apple-MacBook-Gold-2015-speaker-grill.jpg?p=1)

## Metadata
- Author: [[Jeff Weisbein]]
- Full Title: How to fix audio issues in macOS
- Category: #articles
- Summary: If you have been particularly bugged by sound problems ever since upgrading to the latest version of macOS, this is the place to be. Let’s go through the most common macOS audio problems and show you how a little tinkering with settings can typically set things right.
- URL: https://www.digitaltrends.com/computing/how-to-fix-audio-issues-in-macos/

## Full Document
If you have been particularly bugged by sound problems ever since upgrading to the latest version of MacOS, this is the place to be. Let’s go through the most common MacOS Big Sur audio problems and show you how a little tinkering with settings can typically set things right.

#### Audio/sound features don’t work at all

We did it!

We're giving away a Samsung 55" The Frame TV, Dell XPS 13 Plus laptop and more to celebrate reaching 1 Million YouTube subscribers!

Click below to learn more and enter.

This is for those of you who gladly upgraded but then found that your audio had cut out completely. In this case, you get no sound at all from the speakers that you were using before the upgrade. It doesn’t matter what video or app you pull up; you get nothing. By now, you have tried to adjust volume controls, unplugged and replugged speakers, and tried to play media on a different device, but nothing seems to work.

When MacOS first boots up, it sometimes does strange things when assigning speaker outputs, which can lead to radio silence. Fortunately, this problem is easy to fix. Head over to your *System Preferences* in the *Apple Menu*, and look for the *Sound* icon. Inside the Sound settings, you will see a tab called *Output*. In this tab, you should see options for choosing a sound device. Try setting the sound to *Internal Speakers*. While you are at it, take a look at the volume bar below and make sure that your output volume is turned up and *Mute* is unchecked.

![The Apple audio options menu with a blue arrow pointing to the mute button.](https://www.digitaltrends.com/wp-content/uploads/2020/04/applesound01.jpg?fit=720%2C720&p=1)
This should restore audio to your native Mac speakers. “What about my headphones, external speakers, or Apple TV?” you may be asking. In the *Output* list, you should see options for all these devices, as long as they are connected. Choose the one that you want to use. As you may have guessed by now, MacOS — especially when it is loaded onto a computer that’s connected to HDMI speaker systems — can get confused about which speaker to automatically pick. Pick out your speaker options manually to circumvent this issue. You should only need to do this once.

#### Sound cuts in and out

This can be one of the most frustrating issues to experience. If MacOS is randomly cutting out the audio and then restoring it without rhyme or reason, there could be something wrong with how your computer is using memory. First, make sure the problem can’t be narrowed down to any particular app or service. Try restarting that particular program to test it.

If the problem is shared across all audio sources, it’s time to reset your parameter random-access memory (PRAM), which MacOS uses to retrieve basic settings for your Mac and connected devices. Begin by restarting your Mac. When your computer is about ready to pull up the black loading screen, press the *Option* + *Command +* *P +* *R* keys simultaneously. Keep holding those four keys down until you hear the second startup sound play (on older Macs) or until you see the Apple logo appear and disappear for the second time (on newer Macs). This lets you know that your PRAM has been fully reset.

Keep in mind that a PRAM reset may also change some of your other settings in addition to rebooting your sound. You may need to spend some time in System Preferences reconfiguring to reset any of the customized settings you had before.

#### Safari sound no longer works

![The Safari browser on a MacBook Pro.](https://www.digitaltrends.com/wp-content/uploads/2019/06/safari-screenshot.jpg?fit=720%2C720&p=1)[Safari website/Apple Inc.](https://www.apple.com/safari/)
If your tests have revealed that sound problems are primarily located in Safari, this may be another settings problem. In this case, the sound will probably work in other browsers like Chrome but not in Safari.

This problem is typically caused by a strange configuration change that MacOS applies to sound output if you have certain software loaded onto your Mac. If you visit *System Preferences* > *Sound*, you can check on your *Output* option, which will likely list several device options for audio output. If one of those options is *SoundFlower* or something similarly unusual, then that’s a sign that MacOS might be using the wrong sound output. Switch the output to *Internal Speakers* or another speaker device of your choice, then try Safari again. The problem should have been resolved.

Depending on your setup, you may find this audio problem occurs every time you restart your computer. You can stop the problem by [uninstalling the SoundFlower extension](https://support.shinywhitebox.com/hc/en-us/articles/202751790-Uninstalling-Soundflower) on your Mac.

#### Static problem

Are you hearing random crackling, popping, or other annoying static-like noises coming from your speakers ever since downloading MacOS? If you are using external speakers, check their connections and try them on another device, like a smartphone, to make sure it isn’t the wiring. If the problem seems to be MacOS, it’s time to visit settings again.

The first step is to access *System Preferences* and look for the *Sound* icon, which looks like a speaker cone. Under the *Sound Effects* section, you’ll see a list of effects, followed by several additional settings. You’ll find a box labeled *Play Feedback When Volume is Changed* about two-thirds down.

You’ll need to toggle the box to the off position if it isn’t already and then activate it again. If that doesn’t help, make sure you check that the output option is either Internal Speakers or any external device you’re listening on. MacOS has a reputation for being finicky when it comes to BlueTooth devices. Some devices pair with no issue and some don’t at all. Static results from being stuck in the middle ground. You have a connected, paired device, but the audio quality is awful.

Sometimes it’s just a matter of turning off both your Mac and the Bluetooth device, then restarting them both to wipe the static slate clean. You can also delete your Bluetooth connection under *BlueTooth* settings in *System Preferences* and then pair the device again as if it were new.

Some devices won’t work with MacOS. You can test to see if the issue is with the age of the Bluetooth device you’re using by seeing if you can successfully connect a newer Bluetooth device to your Mac. If there’s no problem with the new device, you might need to upgrade your system.

#### **Reminder about MacOS updates**

If you are a veteran MacOS or Apple user, chances are that you have had to deal with the time-consuming nature of repairing kinks that come with updating Apple apps. If you still experience MacOS sound problems, AirPlay issues, or other audio complications, make sure you install all new updates for your Mac. You might have to wait for Apple to release patches that fix these problems, but in the meantime, you can search the help topics to see if anyone has found a workaround while waiting for the patch.

Recommended Video

######  Editors' Recommendations
