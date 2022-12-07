National Day of Civic Hacking
#############################
:date: 2013-06-02 3:18:00
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: hackathon, timeline, jQuery

One of the projects I worked on during the `Rochester edition`_ of the
`National Day of Civic Hacking`_ hackathon was not actually anything intended
for the hackathon, but a short project I wrote last summer.

If you remember from `my last post`_ on the subject, I had made three files,
one for each of the years that the FOSSBox had been keeping track of its
activities on the `timeline`_. The files were very silly- all the data was
loaded on the fly from a JSON file, so the only thing in the files was the structure and the 'decoration' text.

Clearly this was not something that could stand. Today I finally managet to get
all the files together into one page. Now, when the page loads, it scans the
JSON file for all years mentioned, and populates a drop-down list with all the
years it has found. the first (and usually latest) year's data is then loaded
onto the page.

When the user clicks on another year from the list, the content is reloaded with
data from the apropriate year. If you want to see it in action, the new review
page for timeline now lives `here`_.

.. _Rochester edition: http://hackforchange.org/fossrit-rochester-civic-hackathon
.. _National Day of Civic Hacking: http://hackforchange.org
.. _my last post: introducing-fossrit-timeline-year-in-review.html
.. _timeline: http://foss.rit.edu/timeline
.. _here: http://foss.rit.edu/timeline/summary.html
