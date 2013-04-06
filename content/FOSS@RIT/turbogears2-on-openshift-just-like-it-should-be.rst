TurboGears2 on OpenShift, just like it should be
################################################
:date: 2012-02-03 06:47
:author: Nathaniel Case (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, personal, hackfest, FOSSRIT, FLOSS-seminar, RIT, openshift

After much work and many trials, I finally have an app pushed to
OpenShift with no manual tweaking necessary. As often happens with these
things, the solution was much simpler than expected.

Note: I still don't have a foolproof 'follow this' solution ready, as
the one I built works exactly as I want it to, but:

-  It needs a lot of love and cleanup
-  It requires an external git script that isn't well documented

The first isn't much of a problem, and can be worked out over the next
few days. I'm more worried about the second one. For the curious, the
script is `git-subtree`_, which acts like a submodule except it is more
transparent to the repository which is a plus given OpenShift's odd
structure.

.. raw:: html

   </p>

Back on topic, when we last left off this topic, I had finally gotten
OpenShift to acknowledge a project in a directory other than tg2app.
This is useful because, at least for me, most of my projects are not
named tg2app. That turned out to be stupid problem I had made for
myself, but unfortunately, the next problem to tackle was not.

You see, when setting up an app on OpenShift, you have very little
control over the actual environment the app is running in (this isn't
entirely true, but is a useful fiction, especially as the service is
likely to become more 'plug-and-go'). One of the few ways you can retain
control is through a series of post-commit hooks, one of which was
starting off the problematic section of code. When you first push your
code to OpenShift, it needs to set up your database so it is ready to
store information and do other databasey things.

Naturally, this wasn't happening.

First up was a problem with OpenShift. Python's default egg cache (not
too important, it's a place python can use to extract files from
installed packages temporarily) is not writable in OpenShift, so that
needs to be set before anything else will work. Next, the proper MySQL
library is not installed by TurboGears by default (the default is to use
sqlite), so that had to be added to the requires list.

And then I hit yet another wall. Despite everything being set up
properly, I could not connect to the MySQL database on OpenShift. It
wasn't a problem with MySQL, because I could connect fine with the MySQL
client. It wasn't even a problem with SQLAlchemy, because I was able to
connect from a short example script. Finally, in a fit of insanity, I
tried running the build script directly. I'm not even sure why, I was
just at the point I would do anything just to see if it would work.

And, strangely enough, *it did*.

This had some pretty profound implications. It meant something was
different during the build hook than in normal execution. Armed with
this new knowledge, I headed over to OpenShift's IRC channel to get some
answers (I had actually been in there for some time prior, just not with
enough information for themore ruby-oriented users to help).

They told me that yes, indeed there was a difference. During the build
step, the database is stopped, hence why I could not connect to it.
There were, however, hooks for deploy and post\_deploy, during both of
which the database would be running. I moved the calls needing database
access to deploy, and suddenly everything worked! I made a few more
changes, cleaned up my tree, and tested it on a new app I wanted to get
on OpenShift, and it (mostly) worked. There were a few problems left,
but they seemed to be mostly my fault (and problems with the
application, not OpenShift), so it looked like I had finally fixed
deploying a standard TurboGears app. I've no doubt that there's
something I've left out, but I'm pretty amazed at the progress I've made
so far, and learned a lot about both OpenShift and TurboGears.

.. raw:: html

   </p>

.. _git-subtree: https://github.com/apenwarr/git-subtree
