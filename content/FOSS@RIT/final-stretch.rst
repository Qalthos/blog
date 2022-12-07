Final Stretch
#############
:date: 2012-02-29 16:15
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: pybotwar, hackathon, FLOSS-seminar, webbotwar, openshift

So the past two days have been madness trying to get the recently
christened WebBotWar (or just WebBot) to actually work on the web.

We had it working locally some time last week (I think... the days are
really starting to mush together), but OpenShift was a whole other
thing. This boiled down to two basic problems we had:

-  pybotwar depended on pyBox2D, which needs to compile, which doesn't
   work well even when you have control of the machine
-  We were relying on memcached to provide cheap communication between
   the pybotwar process and the frontend. As near as I can tell,
   memcached is not actually supported on OpenShift Express, though that
   might not actually be true.

The first was surprisingly easy to fix, though it took me some time to
actually think of the solution. In the final setup, there are
essentially three repositories: our modified pybotwar, the TG2 webbot
frontend, and a meta-repository containing both of the previous two in
the proper places. This third repo is not meant to be actually used to
develop, its only purpose is to be pushed to OpenShift and act as a
quick pull for someone looking to run WebBotWar themselves. The
practical upshot of this is that if we commit pyBox2D inside the
pybotwar directory of our meta-repo, pybotwar can find its dependencies,
and no one else needs to have to bother with it.

The second problem was more tricky, and eventually resulted in a rather
simple patch that just happened to take me around 12 hours to get right.
A quick Google of OpenShift Express Python and `NoSQL`_ led me to
MongoDB, which has some benefits and drawbacks compared to just shoving
bits into memory, but seems to work very well in practice and is
probably the right way to go regardless. To be perfectly fair, memcached
*is* a type of NoSQL, but MongoDB is actually supported by OpenShift in
an easily-installable manner, and despite its more finicky syntax, it
works, which is something I failed to get with memcached.

Meanwhile, the rest of my team was hard at work making massive progress
on other fronts. Facebook authentication works, as does uploading custom
robot definitions, though I don't think the two are plugged into each
other yet. As well, there are brand new pretty images for the robots and
the turrets.

There's a few outstanding problems left, but (as long as I don't push
anything broken) you can have a look at webbotwar in action `here`_.

.. _NoSQL: http://en.wikipedia.org/wiki/NoSQL
.. _here: webbotwar-qalthos.rhcloud.com
