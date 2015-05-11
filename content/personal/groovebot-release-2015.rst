GrooveBot 2015
##############
:date: 2015-05-11 17:28
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: groovebot

So `GrooveShark`_ shut down a few days ago.

I haven't really followed them much since I took over the original `GrooveBot`_
codebase `sometime in 2011`_.

But now GrooveBot's namesake is gone, which marks a neat sort of milestone for
the project. It has now outlived its inspiration.

In any case, that isn't what I really want to talk about today. Instead of
talking about the loss of GrooveShark, let me tell you about what GrooveBot has
gained.

When I was last fiddling with GrooveBot sometime in 2014, I came to a sudden
realization. If I wanted to subject the people of the FOSSBox to the mad fever
dream of Smash Mouth mashups that is `Neil Cicierega`_'s `Mouth Sounds`_, I
would have to add some form of SoundCloud integration [#need]_.

At the time, I was busy working on one of the issues that had been annoying me
(and others) since the bot's early beginnings, namely the lack of a permanent
queue that persisted through crashes (and live-coding restarts). Along with that
came some architectural updates that should make it easier to one day support
multiple backends at the same time, which is another longstanding issue that I
would dearly like to fix one day. Point being, I had a lot of other things I
wanted to accomplish, and not a lot of percieved benefit to stopping that and
dropping in a new backend instead.

Fast-forward to PyCon 2015 sprints, and Neil Cicierega has not only made another
ridiculous mashup album with `Mouth Silence`_, but has also been posting a
number of not-yet-albumized music to SoundCloud individually. So, I took a look
through SoundCloud's `API`_, and went through some of GrooveBot's less atrophied
backends [#old]_, and put together a new version that supports SoundCloud.

And then I proceeded to play `Bustin'`_ on repeat for a while.

.. [#need] Well, I mean, I could use the mpd backend, but without multiple
    backend support, the pool of music would get stale quickly, and as much as
    this is a project to force my musical tastes onto others, it is important to
    me to let them do the same to me in return.
.. [#old] The 2014 changes I mentioned were actually pretty deep in scope, and
    while I am happier with where the bot is now, for a while Spotify was the
    only supported backend because it was the only one in use, and the only one
    that made the switch. Obviously now SoundCloud works, and I think MPD should
    be working, but Pandora has been broken for years, and GrooveShark never
    worked in the first place.

.. _GrooveShark: http://www.grooveshark.com/
.. _GrooveBot: https://github.com/Qalthos/groovebot
.. _sometime in 2011: /personal/groovebot-updates.html
.. _Neil Cicierega: http://neilcic.com
.. _Mouth Sounds: http://neilcic.com/mouthsounds
.. _Mouth Silence: http://neilcic.com/mouthsilence
.. _API: https://developers.soundcloud.com/docs/api/guide
.. _Bustin': https://soundcloud.com/neilcic/bustin
