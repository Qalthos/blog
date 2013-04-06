Election Night
##############
:date: 2011-03-29 02:59
:author: Nathaniel Case
:tags: journalism, FOSSRIT, election

So election night is tonight. I'll have free time soon.
The main reason for my lack of time lately has to do with the election.
On wednesday, just before I was going to classes, I got a call from Remy
asking what my schedule was and if I'd like to take a trip to WXXI to
talk with Rachel Ward and at their election coverage.
A few hours later, we're in the lobby of WXXI, being mistaken for
musicians (as anyone who meets Remy for the first time is likely to do),
and waiting for Rachel to come down.
We took a quick tour of the facilities, met a few other people, and got
down to business. Monroe County's Board of Elections hosts a server with
the live election information on a static ip and takes it down once the
election is done. Further, this information is released ing the form of
a flash app, making it harder to move the information.
After a short discussion, we decided that we weren't going to get
anywhere without making a call to the BoE. Rachel did her magic on the
phone, getting more information out of them than I ever could have done.
To make a long story short, this flash application is driven by an XML
file (actually two) and that the system was provided by the company who
made the machines and was pretty much a black box as far as they were
concerned.
A short bit of googling later, I had identified another location that
used these machines: London, Ontario. using their XML files as a base, I
made a quick scraper that spat out a basic table of races and
candidates. It wasn't pretty, but it worked.
Over the next few days, I poked and prodded at it, adding features and
eventually moving to an HTML output and checking against a few more
locations, and cleaned up the code some more. We met with Rachel once
more yesterday, set the site up to be running on innovationtrail.org,
and started the countdown.
The current version of the scraper is now running on
http://foss.rit.edu/election/ and should update its information every 30
seconds, once information exists.
