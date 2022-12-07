Shelves and Shoves
##################
:date: 2011-06-21 22:56
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: peopledashboard, widgets, scrapers, SURS

Today is the day to hit `bug #105`_, another of the leftover bugs from
last year.
The story goes something like this: there's a lot of data on
nysenate.gov that is nice to have, but asking for that info on every
call is a little cumbersome. We want to cache as much of the data as we
can, particularly the stuff that's not going to change in the next week
or longer. Previously, I had implemented a simple pylons cache which was
fast, but had no persistent storage, so every time the server went down
it pulled all the info again. And due to the way the scrape was written,
it pulled all the info for all the senators at once, creating quite a
bit of lag before the first page showed up. This clearly wasn't going to
be something we could continue to develop with.
Now, I know nothing about caching data, so I did some poking around in
CIVX to see how it is done elsewhere. Most of the other caches I found
in CIVX code were related to caching text feeds, which were not as
explanatory as I was hoping. Once I felt I had a handle on how things
were done there, I began to try to implement some of it, only to be
shown `this post`_ on `shelve`_, a Python library for storing arbitrary
data. Combined with the decorator, this seemed to do exactly what I
wanted, namely provide a permanent storage area for a bunch of data with
a configurable expire time. I dumped the code into the dashboard, hooked
the proper inputs up and let it run. The results were... promising, but
not astonishing. The file storage worked, once the data was cached, we
stopped looking to nysenate.gov for data and instead used our own data,
even after server restarts.
The problem was that the file storage seemed to be slower than the
previous memory cache. This is all perfectly reasonable, since disk
access is much slower than memory, and a lot of data has to get pulled
for each senator. The first obvious thing I could do is to re-enable the
memory cache, but this did not seem to help as much as I wanted it to.
At this point, `Luke`_ popped up in chat to sat that Moksha had a
`Shove`_ cache it uses for feeds. Sure enough, back in the files I had
been poking through earlier, there were some references to Shove. Back to
the net, I started to explore what Shove was and how it could help me.
It turns out Shove is mostly drop in compatible with shelve, and aims to
be a more extensible replacement for it. Once I got a handle on how
Shove works differently from shelve (answer, not very), I made a few
tiny tweaks and got a version successfully working with Shove and a
sqlite backend. This didn't make the end result any faster (well maybe a
little, but not much), but there is a lot of room for improvement,
particularly if I can hook into Moksha's own stores. Further, Shove has
its own abilities to cache items in memory in addition to storing them,
which I would like to look into. The best route for efficiencies, I
think is to change how the data gets stored in the cache. Currently all
the data gets pulled at once, which was done to pacify the pylons cache.
However, if I can get individual caches for each senator, then I can
pull smaller volumes of data at a time, hopefully speeding up the
process.
We'll see where I get tomorrow, but so far I'm feeling pretty good about
all this.

.. _bug #105: https://fedorahosted.org/civx/ticket/105
.. _this post: http://threebean.wordpress.com/2011/06/08/cached-function-calls-with-expiration-in-python-with-shelve-and-decorator/
.. _shelve: http://docs.python.org/library/shelve.html
.. _Luke: lewk.org
.. _Shove: http://pypi.python.org/pypi/shove
