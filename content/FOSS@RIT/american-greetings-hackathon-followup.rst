American Greetings Hackathon Followup
#####################################
:date: 2013-01-24 22:33
:author: Nathaniel Case (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, hackfest, FOSSRIT

Last weekend was the `American Greetings Hackathon`_, and it was one of
the most successful yet. We got more than 70 people attending and
working on projects, and most of those projects had at least something
working by the end of the 24 hours.

I worked with `Ross Delinger`_, with occasional controbutions from `Ryan
S. Brown`_ on a project eventually called `netHUD`_. The idea was to
take the new `NetHack 4`_ network `protocol`_ and try to make something
more than just another interface to nethack.

Originally, we set out simply to connect to the nethack server and have
a second channel of information. Ideally, we would make calls to the
server and have it update us about games in progress. This turned out to
be problematic for a number of reasons, but the most immediate was that
we could not get two simultaneous connections to the server.

This meant we had to redesign our service. Instead of being a second
stream, we would need to piggyback on the initial connection, which
meant writing a server proxy. This may not have been the only way to do
it, or even the best way to do it, but that's just how we roll. The
eventual structure (all written in delicious `twisted`_ protocols)
looked something like this:

::

     [Nethack Server]    ----    | |    | |   [tee]============[controller]    | |                 | |    | |                 | |    ----                ---- [Nethack Client]     [netHUD]

tee.py acted as the proxy and sent any messages received from the
nethack server to the controller, which cached the current state of all
the games and sent updates to any listening netHUD instances. This way,
you connect to nethack as usual and log in, and then in a second window,
you connect to the server again on the netHUD port and get a slew of
information about your current inventory, nearby points of interest (eg.
monsters, items, traps), and other information. There's a lot more we
could add to this over time; one of the ideas thrown around at the
beginning was integration with the nethack wiki, providing additional
information about items, monsters, even entire levels.

.. raw:: html

   </p>

.. _American Greetings Hackathon: http://foss.rit.edu/node/425
.. _Ross Delinger: http://blog.helixoide.com/
.. _Ryan S. Brown: http://www.ryansb.com/
.. _netHUD: http://github.com/ryansb/hetHUD
.. _NetHack 4: http://nethackwiki.com/wiki/NetHack_4
.. _protocol: http://nethackwiki.com/wiki/NetHack_4_Network_Protocol
.. _twisted: http://www.twistedmatrix.com
