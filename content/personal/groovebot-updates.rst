GrooveBot updates
#################
:date: 2011-09-28 01:28
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: groovebot

Today I'm going to talk about something a bit more understandable, I
hope.

Back around the summer of 2010, the FOSSBox wanted some ambient music to
play in the background. One of the things we wanted was a way to have
control over the songs played be available to anyone, even if they
weren't here to listen with us. `Jlew`_ was working on some IRC bots at
the time, so he wrote up a bot that could hook into the `GrooveShark`_
API and play music that users requested through IRC. It was cool, when
it worked, and it was fun having community control over song selections,
even when that sometimes led to a bit of musical griefing.

Then GrooveShark kept changing it's API without warning, then they
changed their pricing for access to said API, and then the bot stopped
working. Plans to build a more robust bot around `GrooveBot`_, as it was
now called, were scrapped, and the FOSSBox was quiet once more.

Then `turntable.fm`_ happened. While we are not their optimal use-case,
it did allow us a measure of community choice in our songs, and
generally got us back to playing some sweet tunes while we work, with
the added bonus that anyone could run it, not just people with premium
access. Everything was pretty good, all things considered, and we could
continue on with our lives.

Except for one thing.

Now with GrooveBot, you could send all kinds of commands to the bot and
it would tell you what songs were playing, queue additional songs, pause
or resume playback, and so on, all from the IRC windows we were already
using to communicate with people outside of the area. I don't expect any
of this to be available for Turntable any time soon, but there is one
function that I have sorely missed. And that is the ability to change
the volume from my computer without having to get up and manually prod
whoever's running the audio.

So now there is a stripped version of GrooveBot on gitorious called
volbot, and all he does is respond to requests to change the volume.
Hopefully, when a new, free music API becomes available that we can hook
into, it should be easier to reimplement those functions in a more
general way so that multiple backends can be used for a more varied
music experience. And then we can get back to the OS grooving.

.. _Jlew: http://jlewopensource.com/
.. _GrooveShark: http://www.grooveshark.com/
.. _GrooveBot: https://gitorious.org/jlew/groovebot
.. _turntable.fm: http://turntable.fm/
