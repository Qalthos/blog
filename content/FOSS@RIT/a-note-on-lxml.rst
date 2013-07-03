A note on lxml
##############
:date: 2013-06-01 20:46
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: hackathon, python, wat

This post is being written from the `Rochester edition`_ of the
`National Day of Civic Hacking`_ hackathon.

I've been doing a lot of things with `pygal`_ lately. It's a really neat tool
for making SVG graphs in python. One 'problem' is that it needs `lxml`_, and
that has C extensions that need to be compiled. This isn't too bad, though
sometimes it makes me stop and install a compiler. The real problem is the
external header files it needs to compile.

NOTE: this blog post is entirely the result of my own laziness. Had I simply
perused the `documentation`_, I would have found this much sooner. Thus, this
post is solely a marker of my own eagerness to get things running quickly.

After I was asked for the third time how to install lxml, I finally decided I
would figure out how it works so it could be done properly. I did find out
what the needed package was, but I also found that if the shell variable
``STATIC_DEPS=true`` was set prior to installation, lxml would seek out and
download its requirements for you. I don't know how legitimate this is for a
Python install, but it was certainly quite useful for me and the others
trying to use lxml. It even works inside a virtualenv, though I don't know why
it wouldn't.

.. _pygal: http://pygal.org
.. _lxml: http://lxml.de
.. _documentation: http://lxml.de/installation.html#installation
.. _Rochester edition: http://hackforchange.org/fossrit-rochester-civic-hackathon
.. _National Day of Civic Hacking: http://hackforchange.org
