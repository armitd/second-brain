# https://nextjeff.medium.com/my-ambient-information-display-e3c026a2d325

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/1*_aWb_Vk8qD6WLiun9bYHDQ.jpeg)

## Metadata
- Author: [[Jeff Barr]]
- Full Title: https://nextjeff.medium.com/my-ambient-information-display-e3c026a2d325
- Category: #articles
- Summary: Jeff Barr created an ambient information display using a 43" Fire TV and a Raspberry Pi with the open-source software MagicMirror. He customized his setup over months, adding various modules to display information like weather, clocks, and news. Barr uses an Elgato Stream Deck to easily control and switch between different pages on his MagicMirror.
- URL: https://nextjeff.medium.com/my-ambient-information-display-e3c026a2d325

## Full Document
I like to be immersed in useful information, and often dreamed of ways to have it literally floating above me so that I could glance up and see something new and interesting.

A few years ago I mounted a 43" [Fire TV](https://www.amazon.com/gp/product/B0874XJYW8) above my desk, tie-wrapped a [Raspberry Pi](https://www.raspberrypi.com/) to the back of it, and used [MagicMirror](https://magicmirror.builders/) to create the display of my dreams. I have spent several years improving my display and am finally ready to tell you all about it!

MagicMirror is a mature piece of open source code with a very active [community](https://forum.magicmirror.builders/). The base package includes a [default set](https://docs.magicmirror.builders/modules/introduction.html) of modules, and there are [hundreds more](https://github.com/MichMich/MagicMirror/wiki/3rd-party-modules) available. Most of these modules were built by developers to “scratch their own itch”, and subsequently shared far and wide, also in open source form.

The original MagicMirror concept was based on mounting a monitor behind a piece of half-silvered glass so that the overall project looked like a mirror. While this is one way to use MagicMirror, there’s no reason that it can’t be displayed on a standard monitor. Here’s how mine looks:

![](https://miro.medium.com/v2/resize:fit:700/1*_aWb_Vk8qD6WLiun9bYHDQ.jpeg)My MagicMirror in action!
To the right of my keyboard you can see an Elgato [Stream Deck](https://www.elgato.com/en/welcome-to-stream-deck). In addition to controlling my video stream and my lights, my all-powerful Stream Deck controls my MagicMirror, allowing me to switch between pages with the touch of a button.

There are dozens of detailed guides that will help you to set up and configure a MagicMirror of your very own, but this is not one of them. Instead, I will spend most of my time sharing the unique details of my own ever-evolving setup.

One thing that I particularly loved about this project (aside from the result), was that I got to use a very wide range of skills, including learning how to use a stud finder to securely mount the TV, using the Linux command line (not a new skill, but one always worth exercising), setting up an effective source code control system, debugging JavaScript and Node, and more. If you don’t have any of these skills, don’t let that stop you from getting started!

Before I dive in, I want to point out that I spent months slowly evolving my MagicMirror into its present form, adding, configuring, re-configuring, removing, updating, and even modifying modules to suit my needs. I would advise you to start simple, and to move at your own pace in order to avoid getting overwhelmed. There’s a lot of power and a lot of flexibility here, but take it one step at a time.

### Source Code Control

I treated this as a software project from the very beginning. I wanted to be able to track my changes and to revert them if necessary, and I also want to make sure that I can easily upgrade to a newer and more powerful Pi in the future.

To do this, I used [Amazon CodeCommit](https://aws.amazon.com/codecommit/) to set up my own [Git](https://git-scm.com/) repository. This is available as part of the [AWS Free Tier](https://aws.amazon.com/free), and I would have used it even if I was not an AWS employee.

I am not a Git expert, but I am able to do most of my work with relatively simple commands: `git checkout`, `git add`, `git commit`, and `git push`.

In addition to keeping the two main MagicMirror configuration files (`config.js` and `custom.css`) under source code control, I maintain a running README file that tracks my progress, also under Git control:

![](https://miro.medium.com/v2/resize:fit:700/1*vDu1h5zHY3Tq2wyhpVcyLg.png)My README for my MagicMirror project.
After re-reading this, I was reminded that I did my initial setup on an [Amazon EC2](https://aws.amazon.com/pm/ec2) instance. This is an important point: MagicMirror is simply a program that runs on a Linux server, and need not be run on a Raspberry Pi.

### Repeatable System Setup

Because I don’t set up fresh systems every day, I find that I need to keep track of all of the steps, and to confirm that they work each time that I use them. I used a [Google Doc](https://docs.google.com/) for this project. This document has 22 steps, and takes me from a raw Pi to one that has MagicMirror installed and running:

![](https://miro.medium.com/v2/resize:fit:700/1*jnFSHQldcPnYFjawCIbL2w.png)The first part of my MagicMirror setup script. 
### MagicMirror Configuration

The setup process for my MagicMirror consists of a long series of `git clone` and `npm install` commands. In keeping with my goal of making the process fully repeatable and fully automated, I created a Bash script and use it to do all of the setup steps. It creates a directory and then does every last bit of preparatory work (this takes 20–40 minutes):

![](https://miro.medium.com/v2/resize:fit:666/1*yJ9Im3kM9uj7IS5V_VenMA.png)The first part of my MagicMirror setup script.
### Directory / File Structure

My directory setup looks like this:

`Source/MagicMirror` — This is what I checkout from my Git repo.

`Source/MagicMirror/mm_setup.sh` — The setup script.

`Source/MagicMirror/config.js` — The configuration file.

`Source/MagicMirror/custom.css` — The custom CSS file.

`Source/MagicMirror/MagicMirror` — This is a sub-repo that comes from **github.com.** It contains the actual MagicMirror code.

`Source/MagicMirror/MagicMirror/modules` — This is where all of the modules (each a separate sub-repo from **github.com**) live.

To launch MagicMirror, I log in and run this command:

```
cd ~/Source/MagicMirror/MagicMirror/ ; cp ../config.js config ; cp ../custom.css css ; npm run start
```

### Module-by-Module Review

Let’s take a look at each of the modules that I use to make my MagicMirror work. As noted earlier, I started simple and added to this over time, and you should do the same.

Before I dive into the visible modules, I need to tell you about an invisible one! [MMM-Pages](https://github.com/edward-shen/MMM-pages) lets me have multiple pages, each composed of one or more modules. It has options to flip from page to page after a specified time interval, and I have also set up my Stream Deck to allow me to do the same on command.

Here is my first page:

![](https://miro.medium.com/v2/resize:fit:700/1*wNIR1JHrhCb77HPEQj16UA.png)First page of my MagicMirror (clock, calendar, weather, tide, AWS News, and more)
The left column uses the following modules:

* [clock](https://docs.magicmirror.builders/modules/clock.html)
* [MMM-OpenWeatherForecast](https://github.com/jclarke0000/MMM-OpenWeatherForecast)
* [MMM-SORT](https://github.com/mykle1/MMM-SORT) — Tides for Vashon Island.
* [MMM-Countdown](https://github.com/boazarad/MMM-CountDown) — A countdown to my ultimate retirement day.
* [MMM-SystemStats](https://github.com/BenRoe/MMM-SystemStats) — Pi stats.
* [MMM-WorldClock](https://github.com/BKeyport/MMM-Worldclock) — World clock, with time in Seattle and Ankara (Turkey).

The center column uses the [newsfeed](https://docs.magicmirror.builders/modules/newsfeed.html) module to display the [latest AWS news](https://aws.amazon.com/new/?whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc&awsf.whats-new-analytics=*all&awsf.whats-new-app-integration=*all&awsf.whats-new-arvr=*all&awsf.whats-new-blockchain=*all&awsf.whats-new-business-applications=*all&awsf.whats-new-cloud-financial-management=*all&awsf.whats-new-compute=*all&awsf.whats-new-containers=*all&awsf.whats-new-customer-enablement=*all&awsf.whats-new-customer+engagement=*all&awsf.whats-new-database=*all&awsf.whats-new-developer-tools=*all&awsf.whats-new-end-user-computing=*all&awsf.whats-new-mobile=*all&awsf.whats-new-gametech=*all&awsf.whats-new-iot=*all&awsf.whats-new-machine-learning=*all&awsf.whats-new-management-governance=*all&awsf.whats-new-media-services=*all&awsf.whats-new-migration-transfer=*all&awsf.whats-new-networking-content-delivery=*all&awsf.whats-new-quantum-tech=*all&awsf.whats-new-robotics=*all&awsf.whats-new-satellite=*all&awsf.whats-new-security-id-compliance=*all&awsf.whats-new-serverless=*all&awsf.whats-new-storage=*all) via an RSS feed.

And the right column uses these modules:

* [calendar](https://docs.magicmirror.builders/modules/calendar.html) — Events from three [Google Calendars](https://calendar.google.com) (personal, family, and social).
* [MMM-EmbedURL](https://github.com/Tom-Hirschberger/MMM-EmbedURL) — A live video feed from the camera attached to my 3D Printer.
* [MMM-Parcel](https://github.com/martinkooij/MMM-Parcel) — Shipment tracking using data from [tracktry.com](https://www.tracktry.com/) . Every time I receive a shipment notice from an ecommerce site, I enter the tracking number so that I can see where my packages are at a glance.
* [MMM-SpeedTest](https://github.com/bugsounet/MMM-SpeedTest) — An internet speed test, from the Pi’s (somewhat limited) perspective.

Here is the second page:

![](https://miro.medium.com/v2/resize:fit:700/1*Ru-eM3bbsek_IIFmOF-Zaw.png)Second Page (Ferry Cameras and FlightAware Map)
This page was the result of several experiments. It uses [MMM-Webview](https://github.com/Iketaki/MMM-WebView) to open an HTML page that resides on a Pi that is running [PiAware](https://flightaware.com/adsb/piaware/). The page loads images from the [Washington State Ferry cameras](https://wsdot.com/ferries/vesselwatch/cameradetail.aspx) on the left, and the [FlightAware](https://flightaware.com/) map from the Pi on the right. My home is on the approach to [Seattle-Tacoma International Airport](https://www.portseattle.org/sea-tac); I sometimes hear a plane outside and can look up to see it moving across the map. Getting this page to work and to look nice took some time, but I really like it!

Here’s the HTML that I used:

```
  <body class="outer">  
    <div class="container">  
      <div class"ferries">  
        <div class="inner"><img src="https://images.wsdot.wa.gov/wsf/fauntleroy/terminal/fauntleroy.jpg"  /></div>  
        <div class="inner"><img src="https://images.wsdot.wa.gov/wsf/fauntleroy/terminal/fauntterminal.jpg"  /></div>  
        <div class="inner"><img src="https://images.wsdot.wa.gov/wsf/fauntleroy/terminal/faunttrenton.jpg"  /></div>  
        <div class="inner"><img src="https://images.wsdot.wa.gov/wsf/fauntleroy/terminal/fauntlincoln.jpg"  /></div>  
      </div>  
  
      <div class="skyaware">  
        <iframe class="skyaware-iframe" src="http://192.168.7.242/skyaware/?aircraftTrails=show" />  
      </div>  
    </div>  
  </body>
```

Here is the third page. This one is brand new and I am having a lot of fun setting it up. The goal is to display all kinds of educational and informative infographics so that I can look up and learn something new:

![](https://miro.medium.com/v2/resize:fit:700/1*cgKIv-xCu6JPY8tQ8XvIqQ.png)Third page (AWS Fundamentals and other Infographics)
This page uses [MMM-WebView](https://github.com/Iketaki/MMM-WebView). This infographic is from the brand new [AWS Fundamentals](https://awsfundamentals.com/) book, and is shared with their permission. The book contains 13 infographics, each one jam-packed with very useful info:

![](https://miro.medium.com/v2/resize:fit:700/1*g6kdPtzgvaYAaizCEGmpCg.png)AWS Fundamentals Infographics
I am still building up my collection of infographics; here’s what I have so far, and your suggestions are welcome:

* [Physics Posters](https://www.cpepphysics.org/fundamental-particles/)
* [Binary Posters](https://github.com/corkami/pics)
* [NASA Solar System and Beyond](https://solarsystem.nasa.gov/resources/925/solar-system-and-beyond-poster-set/) (The “front” files only)

I still need to review and download these:

* [Free Science Posters](https://sciencelessonsthatrock.com/science-posters-html/)
* [Nine Best Science Posters to Brighten up Your Home in 2023](https://www.sciencefocus.com/future-technology/best-science-posters/)
* [World’s Best Book Ideas in One Piece](https://headway-store.com/products/doublePack)

And here’s the fourth page (image created using [ezgif.com](https://ezgif.com)):

![](https://miro.medium.com/v2/resize:fit:700/1*mnHtyQjE8smDHDM7eLXwYQ.gif)Animated rain map
This one uses [MMM-RAIN-MAP](https://github.com/jalibu/MMM-RAIN-MAP) and data from the [RainViewer API](https://www.rainviewer.com/api.html) to show historic and forecasted rain in my area.

And that’s what I have so far, with more to come when I can get my hands on a Pi 4B with more memory and compute power.

There’s also a fifth page, but it is not in the timed rotation. With a press of a key on my Stream Deck, I can see my calendar in full-page form, courtesy of [MMM-MonthlyCalendar](https://github.com/kolbyjack/MMM-MonthlyCalendar) (personal items have been covered with blue bars):

![](https://miro.medium.com/v2/resize:fit:700/1*UHynPXRfikIBxfCpH2rHKQ.png)My monthly calendar
### A Word or Two About Modules

Be aware that each of the modules that I mentioned was built by a well-intentioned developer that might or might not still be able to maintain and enhance it.

Over the years modules might fall into disrepair, and another maintainer might or might not step forward. If you find that a module is broken and no longer maintained, check the forks and see if you can find a fork that fixes the issue. Or, better yet, fix the bug and file a pull request.

Depending on your use case and the degree of repeatability that you want, you might want to create personal forks of each module and then clone those into your project. If you do this you will need to update your copies from time to time.

### Stream Deck / Remote Control

There’s one more module that you need to know about. [MMM-RemoteControl](https://github.com/Jopyth/MMM-Remote-Control) . If you are using **MMM-Pages**, you must configure the remote control as a fixed page:

```
fixed:  
[  
    "MMM-Remote-Control",  
],
```

MMM-RemoteControl implements a REST API that lets me control my MagicMirror from my Stream Deck. The config file includes an `apiKey` to protect against (local) mischief:

```
  
  /* Remote Control */  
  {  
      module: "MMM-Remote-Control",  
      position: "bottom_left",  
      config:  
      {  
          customCommand: {},  
          showModuleApiMenu: true,  
          secureEndpoints: false,  
          apiKey: "XYZ"  
      }  
  },
```

XYZ is not my actual key, of course!

The Stream Deck is configured to make an asynchronous HTTP GET request when I press a key; the 6 keys in the bottom left are set up in this way:

![](https://miro.medium.com/v2/resize:fit:700/1*0S63_x48gBnMTtW3QbeabA.png)Stream Deck Configured to call MMM-RemoteControl
For example, the **Home** key makes this request:

```
http://192.168.7.217:8080/api/notification/HOME_PAGE?apiKey=XYZ
```

Each module responds to a specific set of notifications. These are generally documented, but you might need to dig through the source code from time to time.

### Overall Information Flow

Here’s my attempt at showing how the information flows from various external sources and into my MagicMirror (created with [Dendron](https://www.dendron.so/) and [Mermaid](https://mermaid.js.org/#/)):

![](https://miro.medium.com/v2/resize:fit:700/1*yGSUGQTDMT4Ym1_iSyyArg.png)Information Flow
### What’s Next

And there you have it! I am very happy with the current configuration, but I will continue to look for and experiment with new modules.

### You Should Build One

As I noted earlier, I got to use a large number of disparate skills in the course of setting up my MagicMirror. As is often the case with these projects, acquiring new skills and improving current ones is an unavoidable positive side effect.

Build one yourself, and let me know how it goes!
