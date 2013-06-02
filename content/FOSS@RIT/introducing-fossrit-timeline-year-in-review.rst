Introducing: FOSS\@RIT Timeline Year in Review
##############################################
:date: 2012-08-22 22:15
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: data alchemy, jQuery, timeline

Yesterday, I sat down with Remy and went over the last of the things we
need to do to close out the summer. There was a long list of items,
split into two sections, each containing the same sort of stuff.
FOSS\@RIT has done a lot of stuff in the past year, and we need to be
able to tell people about it.

The first section concerned the few things we had done that hadn't yet
hit `Timeline`_. This was a fairly sizable chunk of things, and we
needed a good, rapid-entry way of getting more events in there. No
problem, I had done some work on that before, I could get it running and
dump events in there no problem.

The second (and slightly longer) list dealt with things we needed to
compile some information about as a sort of "here's what we've done"
report. The list of things that needed to be in that was... just about
the same as the last one. Remy planned to go through the Timeline site
and add entries from it, categorize them, and push it to foss.rit.edu.

This deeply concerned me on two distinct levels. First was the part of
me that never liked writing. I've mentioned it here once before, and I
feel I've gotten better since then, but the concept of wading through
all that data to write a report was not something that made me happy.
The other part was that all the things in the second list had to be
added to the timeline at some point anyway, or were likewise available
from other sources. When Remy showed me what he had written for 2010, it
was obvious this could be easily replicated in code.

About an hour of JavaScript wrangling later, I had made `this`__. Also
`this`__, and if you're reading this from about a year in the future,
`this`__ should even exist. It's still needs some tweaking, the years are
hardcoded in the documents, the pages aren't linked from the main
timeline page, and I'd rather have them all use one common file than
make a new one each year, but it works, it's fairly similar to what was
handwritten last year, and it gets updated every time something gets
added to Timeline.

.. raw:: html

   </p>

.. _Timeline: http://foss.rit.edu/timeline/
.. __: http://foss.rit.edu/timeline/2011.html
.. __: http://foss.rit.edu/timeline/2010.html
.. __: http://foss.rit.edu/timeline/2012.html
