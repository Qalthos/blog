Hello, world...
###############
:date: 2010-09-09 18:10
:author: Nathaniel Case
:tags: FOSSRIT, democracymap, CIVX, geowebdns

.. raw:: html

   <p>

This is my first posting despite having been here for a week, because
the zaniness that was my first week did not allow for such silly things
as intorductions. Now I finally have some of the infrastructure things
worked out, and can report on my findings.
Work has been progressing on a scraper for `shapefiles`_ for the Senate.
I've been fairly successful in getting a large amount of data, (up to
7.6 GB of zip files!) so my task today was to clean up the script and
make it readable to commit it back upstream. I had started by adding
more loops to the script for special cases, but that meant repeating the
core download code. Realizing this, I made a generalized downloader
function which gets called by each loop, simplifying individual loops
into a simple

::

    'for URL in $URL_LIST; download $URL $FILE; done'

Well, I think it's simpler...
Each time I tweak away at this file, my bash skill gets better and
better, but whether any of this is going to stick around is another
question. I always forget the simple bashisms, like for loops and
conditionals, and I can never remember quite how variables work. But as
I work more with this file, I get more comfortable with these
conventions. Though I still occasionally pine for the occasional
pythonic statement (and perhaps also for the fjords).

.. raw:: html

   </p>

.. _shapefiles: http://en.wikipedia.org/wiki/Shapefile
