Multiprocessing the PolyScraper
###############################
:date: 2011-06-29 18:04
:author: Nathaniel Case (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, hackfest, FOSSRIT, SURS, polyscraper

Warning: This post was written at 4AM and contains a technical account
of what I have been doing attempting to parallelize CIVX's internals. If
you are looking for a more general overview of what I have been doing
recently, you are better off looking to another one of my posts.
Recently, I have been working on CIVX's PolyScraper, a neat little piece
of code designed to be able to read and understand structured text
without knowing how the text is structured beforehand. On Thursday, I
let a test scrape of a rather large dataset start, figuring it would
finish sometime over the weekend and I'd be able to pick it up on
Monday. Then Monday rolled around, and the scrape was still running.
Worse, it didn't seem to be taking full advantage of the available
resources. Running as it was on the boat, it had four cores at its
disposal, however it was steadfastly using only one core.
Now PolyScraping is not an inherently parallelizable task, but on large
datasets it should benefit from some kind of parallelization,
particularly when using large numbers of small files (less so with small
numbers of large files, those types of tasks are usually sequential as
you have a smaller number of resources blocking on read IO). Clearly
there were other things to look into, but if I could do this, this would
mean a huge win for offline scraping, which was one of the things I had
enabled with my addition of local file support to the PolyScraper.
This all led me to `multiprocessing`_, a library I'd been wanting to try
out in python for some time now. Without going into too much detail,
multiprocessing attempts to get around the `Global Interpreter Lock`_ by
spawning subprocesses instead of threads.
The first attempt was written pretty quickly, as I still remember a lot
from my Parallel Computing class from a while ago. Indeed the main
problem turned out to be SQLAlchemy, or, more specifically our use of
sqlite for a backend db. Sqlite is not the most robust of databases and
can't really handle multiple processes attempting to write to the db at
once. Luke suggested (and I would love to try) moving over to Postgres
as we will eventually be doing on the boat, but unfortunately the boat
has been 'stuck ashore' for some time now due to an extended outage in
CSH's network.
In the meantime I have been whittling the process down to what I think
is the essentials. In the process I have made a complete mess of the
code concerning the PolyScraper, but I should be able to make things at
least look like the way they were before too long.
At this point, though, I have been working on this project for close to
20 hours today now. Luke is in town and we're all posted up in Remy's
new place all hacking on our projects together. With any luck a good
night's sleep will clear my head and give me new ideas for tomorrow.

.. _multiprocessing: http://docs.python.org/library/multiprocessing.html
.. _Global Interpreter Lock: http://docs.python.org/glossary.html#term-global-interpreter-lock
