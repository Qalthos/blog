Diving Deep
###########
:date: 2010-06-30 16:55
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: scrapers

Yesterday had been spent working on a proper dev branch to CIVX. Today
we gave it a home.

Today started off trying to get the current dev CIVX running on our
server. Now, I had some experience setting up a CIVX instance from
getting one running on my box, but my box is mine and I know what's on
it. This server is not, so we had a few troubles along the way. Once
again the instructions proved insufficient (though not actually bad per
se). The server was running Python 2.4 by default, and one of the
scripts wanted to be run from Python 2.6, as it was pulling a few things
from future. Remy and I spent more than a little while wondering why
things weren't happening properly when we had neglected to run a command
or two. `Luke`_ set us straight at every turn, and I can now say that I
actually understand what most of those commands do with respect to the
rest of the system.

The second half of the day was a bit more interesting. Once CIVX was
running, my attention was turned to the scrapers. Most of the scrapers
are v2 scrapers, and one of our tasks for the summer is to get things
running up to v3. On the first try getting the stimulus watcher scraper
running, we had a few problems remembering where everything went and
where to call what when. On the second shot getting a scraper for
howdtheyvote.ca data, it went much faster. I need to remember to source
tg2env when I'm on the server, but mostly, things were good today.
Tomorrow we put together the pieces of v3, and keep on moving towards
our goals.

.. _Luke: "http://lewk.org
