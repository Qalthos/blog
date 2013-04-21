Recent Projects: Groovebot
##########################
:date: 2012-07-24 18:47
:author: Nathaniel Case
:tags: groovebot

This is the first of a number of posts meant to overview the things I've
been doing recently. First up on the list is the long-overdue
`Groovebot`_ update.

Before this summer, Groovebot 'worked' on `Spotify`_, and also had a
fairly useful but undertested `MPD`_ backend that worked for me when I
could get MPD running properly. Unfortunately, I no longer had an active
Spotify subscription, which meant that I couldn't use the Spotify
backend, and I had moved off of RIT's campus, meaning I no longer had a
~100Mb connection to my fileserver, so streaming files that way was more
problematic.

While looking around for other things I could use to get Groovebot
running on, I rediscovered `Pithos`_, a Python frontend to Pandora.
Using Pithos as an authenticator, I could get URLs to music files that I
could play if I could figure out how to play them in Python. As a
temporary test, I just sent them to mplayer to play the files. This
worked well enough, but had the same problem I had encountered with
Spotify, namely that I could not get a callback properly positioned to
fire when the song finished.

I put the project aside for a time, until `Justin`_ pointed out
GStreamer is made to do this sort of thing. With this in mind, I took
another look at the task, first trying to run GStreamer in its own event
loop on top of Twisted, then giving up and processing events on a tick.
This means I have to respond to every event GStreamer throws out (which
is a fair number of them), but most of them can be thrown out without
looking at them. Some more tweaking later, and PandBot was born, able to
connect to a user's Pandora station, play music, and thumb songs up or
down based on user respones in the IRC channel.

At this point, I had been writing new bots each time I added a new
backend, with a lot of repeated code in each, leading to subtle bugs and
api implementations that were slowly drifting apart based on individual
needs. This made me a little annoyed, but I didn't have any particular
need to fix it, so I left it alone. Until an accidental click around the
Spotify website left me with another Premium subscription (and $10
poorer...) I poked around on SpotBot to see if it still worked. Turns
out it did... just not on the DJ computer in the FOSSBox. Turns out that
spytify, the python bindings for `despotify`_ have gotten a little stale
in the interim, and no longer compile with modern versions of Cython.
This meant I should probably break down and get an API key from Spotify
and use the proper official API instead.

However, in working on MPD and Pandora bots in the meantime had given me
a number of ideas and fixes that would be problematic to port back to
Spotify, which meant I had finally gotten an excuse to try to merge the
three seperate codebases into one unified version. Starting with MPD and
Pandora, I merged the files and ran the result through a three-way diff,
trying to identify important parts of each bot to make sure each worked
properly after the merge. Next, I looked into the architecture of
pyspotify, and immediately ran into some trouble. pyspotify works
differently to the backends I had been used to, having its own threading
I would need to juggle alongside my own. Additionally, the code is not
thread safe, which is a problem with the heavily-threaded Groovebot
code.

So now, the status is that we are down to two bots. One is the ancient
Grooveshark code that is in need of updating and integrating with the
second bot. This second bot has all the work I've been doing lately and,
some few remaining problems aside, mostly work. Ideally, I will soon
have a better host for the bot that will let me run Spotify, but for now
Pandora is working well enough.

.. raw:: html

   </p>

.. _Groovebot: https://github.com/Qalthos/groovebot
.. _Spotify: http://spotify.com/
.. _MPD: http://en.wikipedia.org/wiki/Music_Player_Daemon
.. _Pithos: http://kevinmehall.net/p/pithos/
.. _Justin: http://www.jlewopensource.com/
.. _despotify: http://despotify.se/
