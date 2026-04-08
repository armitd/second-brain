# How Microsoft uses Conditional Access - Endpoint Zone 1812

![rw-book-cover](https://i.ytimg.com/vi/offk-KH7eIA/maxresdefault.jpg)

## Metadata
- Author: [[Microsoft Developer]]
- Full Title: How Microsoft uses Conditional Access - Endpoint Zone 1812
- Category: #articles
- Document Tags: [[ifttt]] [[twitter]] 
- Summary: In this episode of the Endpoint Zone with Brad Anderson you'll hear from Microsoft's Chief Information Security Officer, Bret Arsenault, about how Microsoft protects it's employees mobile devices.
- URL: https://www.youtube.com/watch?v=offk-KH7eIA&feature=youtu.be

## Full Document
>> Hi there, we want you to watch
Endpoint Zone Episode 1812. >> This is going to be one of the most important episodes
for you to watch because we're going to
have Microsoft CISO, Bret Arsenault with us. >> I'll be telling you
about how we've rolled out Conditional Access and Intune, internal to Microsoft to
protect the corporation. [MUSIC]. >> Hey, welcome to Endpoint
Zone Episode 1812. Brad, Welcome back to the studio. >> Eighteen twelve, the grand finale
is going to be a good one too. This is one of the best ones I
think we've done a long long time. 

>> Yeah. This is going be awesome. We've been getting a lot
of questions were asked. We've been doing our customer
meetings in the EBC here in Redmond. Just generally meets with customers. They all want to know what
it is that we're doing inside of Microsoft to keep
ourselves safe and secure. >> Yeah. So, in a few minutes
we're going to being on our Chief Information Security
officer, Bret Arsenault. But before that, we just
want to make sure everyone understands what
Conditional Access is, give a quick demo of it and then set the stage and then talk about
exactly how we rolled it out, 

what the benefits,
what are the issues we were seeing, were internally. So, first, let me give
a little history of what Conditional Access is. So, the concept here is ensuring
that only trusted users, using trusted devices,
using trusted apps, get access to your data. Yeah. The way that we build Conditional Access within
Microsoft 365 traces back five or six years ago, to really the early days
of Office 365 and go back to 2012 and
the number of users, the number of mailboxes
and files we had an Office 365 was actually
relatively small. But you start to see
all the trends behind 

and the momentum building. So, IT would make a decision, "Hey, we want to move to Office 365." Then, the security team would
take a look at and go like, "Well, hey, wait a minute. The way that we have
historically protected data is a permanent based
security model where at the perimeter of the company, we ensure that the device
was compliant and trusted. Well, now if the data's
outside of the perimeter, outside of the firewall, how are
we going to protect the data?" So, this is where we
really started to realize that this perimeter
based security model that all of us had
relied upon for decades, 

so it's just not
going to be effective in this mobile first
cloud first world. So, we started to see literally
organizations stopping their Office 365 deployments
because of the security concern, which is a valid concern. So, this is when the Office team
started working with the EMS team and this is just
right before we announced EMS. We had to go and pioneer
with this concept of Conditional Access in a mobile
first, cloud first world. Why? Because it didn't exist before.
So, we had to go engineer it. So, what we engineered is a way where the Office 365 services are
in constant communication 

with the services that make up EMS, so Azure Active Directory Premium,
Intune, and others. Anytime there is a request
made for access to data, that can be behind the firewall, that could be the Office
365 or Microsoft services, it could be any cloud service. There's a set of communications
and calculations that happen where we have a point of view on the trust level of the user, the trust level of the device,
and the trust level of an app. Then, IT can assign
different policies based upon the significance or value of
the data and then apply the policies 

in a way where in
real time, we're able to either grant access
or block access but guide the user on what they
have to do to get compliant. Now, one of the key things we had to work through here
is how do you balance those needs of IT with
the end-user experience. Because for all too long,
I think as an industry, as we have delivered what IT
needs in terms of security, it's been at the expense
of the user experience. So, we wanted to do
this in a way that both met IT's needs and was
easy and safer users. 

We wanted to deliver a solution
that we describe it as being loved by users and
trusted by IT, okay? So, that's what conditional axis is, that's how we pioneered it. Now, to give you a couple
of data points on this, this is the most used
feature of EMS by far. What we see is, over 70 percent
of all the devices that are being MDM managed by Intune have
Conditional Access turned on. As we think about the advice
that we give organizations, things like multi-factor
authentication, couple of our identity knowledge
and our identity protection. 

The turning on of Conditional
Access to ensure then again, trusted users using trusted devices, using trusted ask, these are two
of the most important things that any organization has to deploy
in order to secure their data. So, that's the background,
that's a history. Let's just give
a two or three minute demo of what Conditional Access and
we'll start with you Simon. >> Yeah. I've got my iPad. So, I'm just going to go
click this link inside of my notebook here and
it's going to open up into the Safari browser. It's going to ask me to sign in
to my Azure Active Directory, and I'm going to select
this account here. 

We already signed in
recently and it's cached in my Keychain on iOS
and I hit "Sign in". Now, as soon as I do,
that it's going to tell me that I can't
get there from here and I've got to be using
a Intune Managed Browser. >> Yes. So, the policy
that IT is set is, corporate websites have to be accessed in the managed
secure browser. >> Exactly. >> So, because you're
using Safari which is not the Managed Browser that
comes a part of Microsoft, 365 access is blocked. This is a key way where
IT can separate personal browsing from corporate browsing
or or commercial browsing. >> Yeah. If I look at the experience
of doing that inside of Edge, 

so which is my corporate
Managed Browser. If I go in here and I select
my link to that same website, then it immediately loads. But not only that, because I'm in my corporate Managed Browser
and it's actually able to access my
authentication tokens from- >> SSO. >> -authenticator app, SSO
straight into the application. I'm not even prompted
to enter password yet it's all still safe and secure. Now, if we switch over to my PC, we'll be able to see the admin
experience for creating one of 

these rules inside of the Microsoft
device management console. So, the very first thing
I have to go do is select which users this
is going to apply to. You can see here that I have a group of users for Exchange Online
Conditional Access. I could also select my guest users or particular roles
inside of my directory. Then I'm going to go and select which apps I want to apply this rule to. In this case, I'm
creating a rule that's going to manage access
to Exchange Online. So, I've selected
the Exchange Online application. 

Then, I can go select the conditions. So, I can say my "Sign-in Risk", so that's the automatically
identified level of risk for my session. Yeah. In this case, I
will select to that. I can also select which platforms
is going to target. So, you get "iOS", "Android", "Windows", "Windows Phone", "Mac OS". I can select which locations that I actually want
to apply this rule to. So, I could add trusted IP ranges, I could add IP ranges for particular
countries around the world. 

I can also go and say which client
apps this is going to apply to. I kind of feel like
we'll be able to say protocols here because
that's what it means. But its of apps, I think, is also a good name for this. So, in this case, this rule is going to apply to any mobile apps and desktop clients
using modern authentication, so it won't apply to
a legacy authentication. I would want to have a different
rule configured to do that. Then, I can have a device
state in there as well. Next, I'm able to say what
my controls are going to be, 

that we're going to
place around the axis. So, with Conditional Access, we're thinking about what
are the conditions of access and how are we going
to protect the access. So, I can say that it always needs to be
multi-factor authenticated. I can say that we need
to have the device marked as compliant inside of
Azure Active Directory and Intune. I can say that I need
Hybrid Azure AD join. I can say that it has
to be on the list of approved client apps and I can
require any or all of these rules. Then, a little further down, 

here I have the ability
to control "Session". With this, Brad is going to show us an example
of this in a second, I can put restrictions in place that will say that Conditional
Access will actually prevent me from being able
to do certain actions inside of my browser session
and I can also tie that into Microsoft Planet Security to go and have these controls run against things like
Salesforce, if I wanted to. So, once I've selected all of those, discard those as is, and I select what
the policy is going to be on and I've saved it,
it's going to apply. 

Literally, what I've built
here is a policy that says that any of these users in
these groups coming from iOS where they are using the native mail application
with modern authentication, will have to be coming from
an enrolled and compliant device. So, we know that that device has all of my companies
protections applied to. >> Which is actually
the policy we we've applied at Microsoft and are going to
talk about in a few minutes. >> Exactly. Let me show you then one more end user experience.
Switch over to my PC. So, imagine that now
this is my home PC, I'm working from home
and my organization 

wants me to be able to access and do my work from any device but
if it's not a trusted device, IT is going to want to say, "Listen, I want to guarantee
that the data never leaves the browser when
that browser has shut down. There's never any trace of my company's data left on
that untrusted device." That's one of these classics
that we have been now build across EMS and Office 365. So, what I've done here
is I've gone in on my home PC which by definition
from an IT perspective is untrusted and I've logged into "office.com" I've gone and
I've gone into my OneDrive. The first thing to point out
here is this little yellow bar, the to here and look what it says 

"Your organization doesn't
allow you to download, print or sync to this device"
Because it's being managed. So, right there, we're
giving the user the data. They can do their work, we're going to keep it on the browser but the data will never
leave the browser. So, now if I come down
here and you take a look at all the files here,
let me go highlight one. In this case, you see here in the toolbar that comes up right here, there's a couple of options that are missing, that are not displayed. Like you can't sync.
If I come in to open, knows I can only open
into Excel Online, I cannot open into Excel, 

because we're going to keep
the data in the browser. What's happening on the back and it's where you're actually changing the HTML that's coming from the
office server down to the device. Because I'm pointing out here, I'm
actually in the Chrome browser. I did that intentionally here
because this works in any browser. So, now, if I go ahead and
open that in Excel Online, it's going to go ahead
and open that document. I'm able to get my work done. The web apps are becoming
just amazing apps, there are days at work, I
live expressly on only in the web apps these days and I get
my work done in these very well. So, now, I come in here and
the other thing that we do is we're 

able to disable things
like copy and paste. If I come here, if I right-click, notice, there's no copy option. This is on an unmanaged device but it is able to deliver
that promise of give the user that great experience
they love in a way that provides the security and
management that IT requires. That's Conditional Access
on an untrusted device. >> Yeah. It's actually amazing
how these controls can span so many different scenarios that can be built to face
any of our customers. >> The other reality is not
all data has the same value. So, you have different policies, 

applied to different datasets. That's one of
the beauties of this is, you can have different
policies that apply to different datasets based
upon the confidentiality, the value of that data and that's one of the great things
about using Conditional Access. So, it's one again, one of
the most important things for you to enable we tell people enable MFA, you have to protect those identities and then enable Conditional Access. So, I think it's time
to actually now talk about how we deploy
all this internally. To do that, let's bring in our CISO, Bret Arsenault. Thanks
for joining us. >> You bet Brad, thanks so
much. Simon how are you? 

>> Hey, how are you doing? >> Good to see you. >> As we were driving over, I was
thinking about the first time I met you Bret, 2007. >> When you left school. >> Not exactly. You've
always describe it, you've been at Microsoft since the Earth cool but you and I
met for the first time in 2007, you had just come into
the engineering team and you were the CTO for all of the security work
that we were doing. I think one of the things I
love about you as our CISO is the fact that you've spent time in the engineering teams and in IT. So, you're able to like translate
the language between us. >> Yeah. It's also what you build, 

you find out this industry and
how it runs in the real world, so it's also super helpful. >> So, first of all, tell us
about your responsibilities. What is it that you do at Microsoft?
I've wanted to ask you that. >> Well, I mean as
the CISO for Microsoft, I'm just protecting the assets
of the enterprise like any other large company and I
have a business continuity, disaster recovery in my remit
for accountabilities, and of course, security
for the company. >> All right. So we wanted
to have you talk about the internal robot of in
tune of condition access. 

>> Yeah. >> Because I'll tell it,
first of all, what were you seeing and what were the things
that we're saying like, "Hey, we need to have this
deployed at Microsoft." >> Yeah. It's one of
the thing you just try to look forward to
see what's happening. I think one of our board members
just saying how do you see into the future and not
just the current piece. It was obvious. I mean, in
hindsight, it was always obvious. >> Of course. >> The trends about
this whole mobile and client, the cloud world was changing, and so this idea that the perimeter, which is a very effective
control for us, I mean, you're either wired or
wireless in building 

or you were coming through a concentrated VPN connection or a virtual private network
connection wasn't working anymore. I mean, as an effective control, you have people coming in
from a local coffee shop or any number of remote locations. So we started realizing if that's as a control effectiveness point is
not as good as it used to be, what's the new model going forward? So while for years, even back
when we all fought endpoint because it's a lot easier
to manage 8,000 routers that it is 10 million endpoints, but the reality was, you just
have to start managing things 

from the endpoint. So we realized at that point, we just really have to
take all those policies we used to do it at
network level and apply them through this
conditional access model at the actual endpoint itself, and the endpoint being client
device or service endpoint. >> Okay. So then, talk
to us about then, as you first start to
go out and talk about, "Hey, we're going to
require every device to be enrolled to be managed
and compliant." Was there resistance internally
at Microsoft to rolling that out? >> Resistance is an interesting word. 

Depends on who you talked to, who had the different perspectives. I think one of the things
we had to do is simplify security for enterprise in general, which was the whole BYOD craze, it started happening,
so it gave people a different perspective on devices. Now, we think about managing those. I mean, in your background
and system center, we had a large system
center deployment where the device is managed, we know everything about it, we can ensure it's encrypted,
all the other things. When you get into BYOD, you start to lose some
of that capability. 

So how do you bring
that back and have the benefits of bring
your own device, the benefits of cloud computing, yet with a really good
management paradigm for security and
a good user experience? So basically, everybody
wanted everything. I think we simplified it
down to make it easy, which was just three things
you have to do. Number one, you have to
have strong identity. That's the number one thing. Identity is the new perimeter. So how do you ensure you have
a strong identity and you have a great seamless multi-factor
authentication experience regardless of what corporate asset
you're trying to access? Number two, having
good identity is awesome, 

but if you have a compromised device, it doesn't matter because I
owned everything underneath it. >> Right. >> Then number three, how do we
make sure we have the telemetry in reporting from the endpoints so we can take that enriched data set? One, to find anomalous behavior,
but two actually, just it turns out it
was really helpful in defining the user experience
and making it better. Those are the three
big things for us. >> That's one of the things that
I think our teams met weekly for a year as you were helping us
to refine that user expansion. We always talk about Microsoft being from an
engineering perspective, 

as we build a product,
Microsoft internal IT is our what we call our
first and best customer. >> Yeah. >> So you're rolling things out
way before the world sees it. >> Yeah. I think we're a good proxy. Some people say, "Oh, you know? You're perpetual unique,
you're a snowflake." But reality is I'm
not and I'm also not, there's this myth that
I'm all Microsoft. So we had like 32 or 34 versions of operating systems
we support today. Plus one thing I do most people
don't is I support n plus one. So when you look at your third party software like
Adobe or something like that, 

that's not certified yet for
the next version of Windows. We still have to support it
and make sure it's secure. We have at probably the
second largest Mac shop in the world today or at least
the top 10 of large Mac shelf. So I know for sure,
there's one bigger. >> Yeah. I want everyone to hear, that's a fascinating data. The second, certainly the top 10
largest Mac shop in the world. >> Yeah. We have over a half million
Linux host in this environment. We have over a 160,000
Android and iOS devices. So I think there's
this myth that we're 

just a pure Microsoft shop
and it's just not true. >> Yeah. >> Well then, first to
talk, tell us a little bit about how you roll it out. >> Yeah. >> Then you've got
your dashboard up apparently. Now, tell us about
the dashboard as well. >> Yeah. I think so, to your point, we have this big thing
about being vision led, and so let me just walk
through two things if I could. >> Yeah. >> One was landing
this multi-factor authentication. We had this idea and you've been here long enough to know
like we're going to have multi-factor auth everywhere, which seems like a penalty. So you do these things like
the smart card badges you have, 

and if they're of the reader, and all these different things. We had virtual smart card and all these different things that made the multi-factor auth really hard. We change to say, "Hey, how
about if we just eliminate passwords? Let's just
get rid of them." That now, it completely flipped
how we engineer things, it completely flips
the experience that we built in. So you're going to do Hello for Windows and you have
this great experience, which is you walk up to the machines, no username, no password. It just works. You are the password. >> I know. >> So getting that implemented
throughout the ecosystem took a little while to go do
that. So that's great. 

Now, over 86 percent of our employees don't
log in when they come in, don't have to log in with
their username, password. They just get authenticated
into the system. But then again, remember,
I have this population that doesn't know Hello for Business. So we use the wonderful
biometrics features of the phone conditions and with Azure Authenticator to give you
a better multi-factor experience, and having a CatCard or whatever, other thing and device, which
you just use your phone. So a lot of the condition
asked us questions that came up as I'm not going
to use my phone for that, but can I still do two-factor auth? 

There was like
a big piece of feedback. There's the third most
popular question we had. So this idea again, be vision led. So don't force multi-factor auth. Then, next vision was, how do we provide the best seamless working experience
no matter where you are? Conditional access enables it, but conditional access isn't the way
we think of it as the answer. We said multi-factor
is not the answer. The answer is no passwords
and the answer is best experience anywhere
from any device. So those really helped us. Now, we'll get into
the nitty-gritty. I'm sure. >> What you're talking about
that amazing experience, 

obviously, we're using
things that aren't out yet. But when I picked up my new iPhone
a couple of weeks ago, I didn't have to even ever put
my username and password into that using the technology that went in coming out over
the next couple of months. I just brought it up, that some of the new technology
just enabled it. >> Yeah. Password list phone
and password line of business, it's the next stuff
we're doing right now. >> It just made it so seamless. I can't wait to be able to
roll some of that stuff out. >> Yeah. >> Tell us a bit about
the dashboard here. If we could actually have it
pop up on the screen here for everybody and tell us a bit about the dashboard that you look at. >> Yeah. I think it's interesting. 

So we asked how the first reaction was in a lot of people who said, "No. I totally get it." Some other people
were on the, "Well, hang on. We're just as long as we have two FA, why do we have to have
this managed device?" We had to remind people if
you undermine the device, then the identity doesn't matter. If you have a really strong device, but you have lousy identity
again, it doesn't matter. Encryption doesn't do
you any good if you have a really bad identity system because then I'm just
getting your encrypted data. So really, really good. We are about 50,000, 

we roll waves to make
sure we're not doing anything bad and we were
monitoring the experience. I've always talked about that
third leg telemetry and reporting. We have good telemetry reporting. What I didn't think about was telemetry reporting from
the user experience, not just the email tickets and helped those tickets
which we looked at, those numbers really small like
0.003 percent of any issues. >> No uptake and the help desk at all as you roll virtual access
to every user. >> Virtually nothing except we also have this thing
called the Gestalt, 

which is just sentiment analysis
against Yammer groups, we're a large Yammer user, right? We started seeing a vocal minority
spike around 50,000 users. Like okay, from a math background, if I'm at 0.003, it's a blip. We're just going to
keep moving forward. But actually,
our leadership team said, "Well, hold on what is the blip? Let's start looking into and digging into it and understanding
what it actually was." That it wasn't concerned with
conditional access per se, it was privacy concerns and the deal. 

Which honestly, we argued
for a couple of weeks, over what do you mean the deal? >> The employee deal with Microsoft. >> Microsoft. Yeah. What's
the deal with Microsoft? Meaning, I came here, I'm
doing all this great work, but now, you want to
go do this piece. So, it made me realized
they didn't understand; one, what the risks were, and
two, yeah, I'm this place, I don't think I'm in
a role that affects that. But they don't understand the pivot of getting an identity and start
pivoting your [inaudible]. >> The risk you're
talking about here was, that Sam was coming up with, why does Microsoft want to
take over my personal phone? 

>> Right, and there is this, I
don't want Bret reading my email, and as you are well aware, I don't even read the email
from you half the time, so I'm sure not going to
read everybody's email. >> When I send it to you. >> We have no interest
in doing any of that. So, what really happened
though was it did create this legitimate concern
I think around for, again being a proxy for other people, what can we see? What will we do? Also, the experience wasn't
ideal at the beginning. There's experiences that we control but there's experiences we don't. 

For example Apple pops a dialogue that scary and we don't
control that message, so how do we deal with that? So, we made a lot of
improvements in that. >> You gave us a ton of feedback
on, you shouldn't use this one, I mean like literally you're
giving us guidance on the words we should use even on the screens,
and it was fantastic. You helped us make
the product much better. >> We did and there was
this pause though, like I said, it just seems strange to let
the vocal minority slowdown an important roll out.
That it reminded us one, not everyone had been bought
into the vision and understood. We're not just a botched product
company that delivers a product, 

we're the custodian of
the world's data and so, you just have a different level
of responsibility than we had in 2007, even in 2010. >> You think about the data
that everyone has now stored in our services in Office 365. I mean, that our need to
protect that is life itself. >> That's paramount, right.
There's nothing more important for us to do and trust is
such a critical thing. I think people just generally don't
understand some of the things. I'll give you
a really simple example. Most people will say,
hey, my camera's at home. I don't put passwords
on them because I don't 

have anything that I
care for anyone sees, I just have a camera
on my tree so I can see the birds. So, why should I care? This is a secondhand
smoke problem which is, sure you don't care but it turns out someone took over
a bunch of the cameras, then used that to launch
a denial-of-service attack against public cloud-based services, not ours, but in
the gaming industry and others. You forget, you realize, it's
a very connected digital fabric and there's a fine thread you
have to just be careful of. So, reminding people
that was important. Then training, doing
a lot more around 

user education and awareness
on what we can and can't do, what we will do, what we won't do, and making the experience
more seamless, like you said so it just
works when you turn it in. As long as it just works,
it tends to be really good. So, that was a really big deal
for us was to take the data, slow it down, hold brown-bag
sessions, hear their feedback. So, I think that
ability to go do that, not just helped those tickets, but sentiment analysis that we built in on top of what we do with
both SharePoint, Yammer, 

and a number of
the other social technologies, really gave us insights we never
had before which I think, one, made the product better but
and while I liked that, most importantly I wanted
the user experience to be better. So, there's some pretty
interesting findings I think on how many people
decided to opt out of that. That's the big part,
could you opt out? What if you didn't want to be,
you still had security concerns? >> Yeah. It's actually, it's used in the dashboard, take
a look in the bottom left there, you can see we're holding
back in March and April, as we were working through
a couple of these issues. Once you turn it on for
the rest of the company, 

see how it fast it went
from May up into June, where we went from 40,000 devices up to a 140,000 devices
under management. >> Yeah, and it's also the classic, the curve is partially because
when we do these rings, you expand your base. >> You say you can see the steps. >> So, we're doing 1000,
2005 and of course, the first two groups are, one, the group that has
the most vested interests, your group, and then my
group as the security team. So, we are using it
first, then we expand it. Then when we get to the next way, once we get past the feedback pieces 

and understand what we can go do, then we started rolling in 10
and 20,000 person increments. >> Well, I think that's
good advice for everyone who's listening to this is, as you're thinking about
your deployment is, first start with the groups that have a vested interest
and it might be IT, but you also want to have
it go out to a set of individuals who are
representative of the company. >> That's right. >> Because this would
be feedback that comes from a normal employee that's
not going to come from IT. >> Well in fact,
the other thing we did was, once we knew we got
past the initial rings, we actually started targeting
the most sensitive groups, 

finance, HR, marketing and
areas that we know are targets, which was the second point
in educating people just on the mobile side,
because PC side with system certain things we
already had a good solution, but we know we need to move that
to in tune and make it more cloud-based and move forward on that. But at least we had a solution.
On the mobile side though, we see you at four million
threats in 2017 alone on the Android platform and I don't
think people actually recognize or saw those things. So, we had to educate
people that we're protecting those from
happening and then, there are a number of crisistunities,
I think we call them. 

>> Crisistunities, I've got
to write that one down. >> Crisistunity, yeah. There
are crisis tools you can use to move the agenda forward,
these are all public things. So, we had an issue where one
of the network companies you could walk by with an iPhone
and be completely owned. Right, and so you use that,
and so okay, what do we do? Well, if you have conditional access and if you don't have
the update to the iOS then you're exposing us to
a risk where if you can say, hey, guess what, if
you're not at this pack, this revision level of iOS, you can't connect and
here's how to go get it. 

>> So, what is the
conditional access policy you have applied right now at Microsoft? >> Well, there's a number of ones that we do on the mobile side though the biggest thing is the things
like, you have to have a PIN. In fact, the PIN was
the third biggest complaint. To be fair, back to our company, so we had multiple ways you could
do multi-factor authentication. So, the card you'd
use, the smart card, had a different PIN length,
then the hello PIN length was, one was hardcoded so
you couldn't change it. The phone factor authentication
was a different PIN length and then we added
all these different pieces. 

So, we had a big argument
about four, six, or eight and we have
all the math arguments, but again, what's
the user experience. It turns out, when we
went with just six, which mathematically was fine for us, what people underestimated
was actually people loved it because it was consistent
between all of them now, it wasn't 4418, 416 for the other. So, PIN encryption,
again, data came back. Guess what, there's about
a two percent population that wasn't working, the
encryption wasn't there. >> It was predominantly Android. >> It was predominantly and it was on low-end devices in emerging markets. 

>> We actually see that, these low-end devices, that
just cannot do encryption. >> They can't do it. >> Your policy, I don't
want them accessing the data then, plain and simple. >> Yeah, but I I'll give
you a fallback method. There's two ways to fallback
and that went like, okay, I can give you
limited mail access with no attachments and
that's a risk window, or you can do a virtual VDI-type
environment where you can do it. >> Working on the phone is
not the best experience. >> No, it's not great. But most
people have already [inaudible]. >> So, PIN, encryption, patch level, you have a minimum OS
level you enforce? >> Minimal OS, jailbreak,
is the device jailbroken, and which is surprisingly
a low number 

that we thought we'd see more just because of our engineering culture, but it wasn't too bad and
so, if they're jailbroken, don't let them in and
number of things like that. >> Okay. So then, as we've
done the roll out now. >> Yeah. >> I saw 77 percent of
all the Microsoft employees now have a device enrolled in
iOS or Android device. >> Yup. >> What are the benefits
that you're seeing now from conditional access and having
this policy about a trusted device? >> I'd probably say there's
a couple of things, and there's probably
a few epiphanies in here or insights that I
thought were interesting. 

When we were doing the roll
out on the devices, we expect that this has
financial implications. Because there are people
who are going to say it's just not for me, and
that's totally expected. We looked into the industry both
in tech and financial services and a number of the
different industry numbers. The numbers range, and I
won't pick out any industry, but they basically range from about five to 25 percent of
employees may opt out. >> They said that, yeah, that I
don't want email on my phone. >> That's right. >> Which is a bad thing actually. 

>> It can be but again, remember, actually, the OWA-based mail
experience is great. >> Yeah, true. >> So, you can still
do OWA-based mail and you can still the
OWA-based calendar, which is an awesome experience from my perspective but
doing other work wasn't. So, but at least you could
do the minimum viable work, at least at this company
to make that happen. So, we said okay, well,
we should create a policy for corporate liable devices
where we own the device and that's really simple. So, we of course had to go
to our CFO and explain. Well, listen if we
think it's 25 percent. >> A lot of money. >> Kind of do the math, 

it's in the tens of millions
of dollars potentially. So, how do you deal with that? We said okay, well, first of all, we had just acquired a company
in the valley, a large company, and they had their data
showed more in tech and other places more
like five to 10 percent. But even at five and 10 percent, over 160,000 people buying 6,000
devices is fairly expensive. But we at least planned for it. We decided not to create new budget, we said, listen, it's up
to the manager discretion. If it's needed for your business to have that kind of access, 724 access, as opposed to the stuff you do
on PC or other managed devices, 

you can make that decision and
suck it up in your own budget. So, that is number one. Number two, we overly communicated on
what we would and wouldn't, and we changed a lot
of legal language in that to make it super clear. >> We actually changed the language
in our employment contract. When you actually drove in the deal, and then you drove
changes in the product itself and the screens
that we pop up. >> Yeah exactly. So, I
expected we'd probably be in that five percent range and that it would be
absorbed by the management. So then, there's the, I'd say like, make sure you're
educating the managers, so the managers become
your first line of defense and 

doesn't just all roll back
to the IT department. We're all on board but
we need to go do this. So yeah, I learned
this lesson from one of our CEOs a long time ago when
you're trying to play with numbers. So, we thought that there was
going to be five percent. So, what do you think
Simon the percentage was? I'm holding up my hand,
more or less than. >> Naming the percentage,
the number of phones requested, it's
on your dashboard here. >> That was crazy. Either
we'd been one percent, it was four, it was four phones. >> Four phones. >> They had four phones,
four percent, four phones. 

So, it became a complete non. I wish I had made
a bet that the money we save that could have reapplied
to our security budget. But it was four phones. But which was great and then there may be a few more
that we will do in that. But I think we see a lot
of people that are in this different trend of carrying multiple devices and other things. But yeah, it's been
phenomenal as far as. >> So, it's not a surprise
is then number. That small the number
[inaudible] requests. >> I'm glad we did
the delay, if we hadn't, there was a larger faction
that asked for a reference. So, when I say larger, it's 41 people 

that are within a specific group. Then when we went and explained
to them what we could do, what we wouldn't do,
what the policies were, and the experience,
they all backed out. There are a couple of
cases where I think, there are some cases where
it completely makes sense. >> Then if you think about
the increased security that you now have at Microsoft,how
would you quantify that? >> It's hard. Well, to quantify that, the first thing is that we do
a dashboard with our LT about the devices under management
and our problem was mobile was, we had limited management with
the Exchange Act, the sink policy. But full management just
wasn't there and so 

it was a complete space
for us that I was never comfortable with and now I can show that there are no mobile devices
that connect to our environment. Our managed PC
environment has a grade. Still have work to
do on Mac and Linux, I'm counting on you for that, and that's the next phase
we go roll out, and so yeah, I think it's
been. I feel much better. This job I sleep like a baby. Wake up at two, crying every night. No crying as much
now, but it's better. 

So, no, I feel good about, I feel especially good about
this issue like I said. When things like Spectre
and Meltdown happened or other things happen, we
have the ability instantly and some of the tools used, so
you're saying, "Hey, guess what? We're going to stop until we
can get a fix at everything and so we reduced that attack back." >> When a new zero-day
attack is identified and they're going to happen, you can go change a policy
inside the console and immediately goals are applied. >> So, I know you have to
win the policy though. One of them is that the current OS or current patch revision
or pressure kind of days. 

So, in those cases
when we say this is the policy that you said those things are just happening for us all. So that's been, I feel like
we have an environment that is cleaner. There's
always work to do. There's these other systems
we're going to get to but, it's a huge boon forward for us. It's also setting the tone for how we want to do
all the other stuff. >> If you were to give
advice to the IT pros or even at the overseas
organizations that are watching us, what advice would you give them, on rolling out Conditional Access
and these security things? >> Well I think for
one, the first thing is 

getting simple that
people understand, it's part of a defensive network. You got to have
really good multifactor app, then you have to have vice out, and you have to have the
telemetry in reporting, that getting that simplified view
is super important. Number two is, don't underestimate
the user experience. Like I said we were
using math to say, we used Statistics to drive it
as opposed to a vocal minority, that turns out the vocal minority
had some really good feedback. We were just listening
wrong mindedly. 

It wasn't because of
arrogance honestly, it was just because we were so
used to doing these things and so, I think that was
the second thing which honestly just by doing
that and saving time, but also we saved
the company a lot of money. That wasn't the primary goal here, but we ended up doing that. So I think that was- >> That's where you can say that
the security of the posture of the organization increased
dramatically and the cost didn't. >> The user experience got better. >> Right. >> So, there's this triangle, that's the same thing with password. 

I have such better security now with the Azure Authenticator
and Hello for Business, and yet the user
experience is awesome, and just then again cost changing passwords on our 70 day rotation. >> Now because of
all the work we've been doing with our intelligence
from our Cloud sources and some of these elements
like we're moving to once a year and hopefully
never change password again. The user never sees it now,
but once a year we'll do it. So, that's four times less
you don't have to do it and- >> You were sharing with me
the research that you had that 

showed when you change
the password once a year, your users put in
more sophisticated passwords because they're less concerned
about forgetting it. >> Yeah, and then also
we've done some work to do easily guessable leveraging the data and telemetry that we get
from our Cloud services. So I think that's good. The other thing that I
would say though and I've sent you this email after which
was once you go to this model, which basically everything's
multi-factored, everything has to be healthy before you can get
access to anything. Access is a number one thing
employees want. 

All the data will show that.
So, as I said, I go well. Conditional access and in-tune
become the oxygen of the company. If you hiccup, Microsoft coughs, so makes sure that when you do
these things that you kind of understand that that's going
to do all those things. That's the partnership
we have and so, there has been no coffee
nor been sick, I feel really good about it. >> Couple of points here.
Really would encourage you to go learn more about
Conditional Access and two most easiest
places to go learn, go to microsoft.com/ems or
microsoft.com/security. 

There's a number of customers studies out there that you can
also go and read about. Actually today we just published
a new one program about Wipro. With Wipro, here you have
this massive organization, one of the largest Systems
Integrators on the planet. They rolled out in-tune
and conditional access and removed one of
the competitors on there. But they now have
that running for over 90,000 employees on
their Windows 10 deployment, over 70,000 employees for
their iOS and android devices. They talk about how significant their improvement is
on their securities 

it's like Brett said
the user experience improved. So, there's golden triangle of
a better user experience and more secure an organization at
a lower cost or at the same cost, that's an amazing breakthrough. Then the last thing
is, get it deployed. Get that identity protection deployed with multifactor
authentication. Get conditional access deployed
so you can actually ensure that only healthy and compliant devices
access your data, and then have the listening. As Brett talked about
the telemetry, have those listening tools in place. You get that feedback and
adjust quickly as you get the feedback from your people.
I think that's a wrap. 

>> Yeah, I think so. >> Happy new year everybody. >> We'll see you on the next episode
of the EndPoint Zone. [MUSIC]
