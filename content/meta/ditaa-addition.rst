ditaa Addition
##############
:date: 2013-05-15
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: blog

Recently, while wandering around the Internet, I found a neat little project
called  `ditaa`_. The basic idea is it takes a textual representation of a
diagram, and turns it into a real image. My first thought was that this looked
real neat for use in this blog.

I write this now not in HTML directly, but in `reStructured Text`_, a somewhat
less verbose markup language native to Python. Thankfully, someone had already
made a `directive`_ for ditaa diagrams to be embedded in reST and get rendered
to an image in the final page. With this in hand, I managed to cobble together
a plugin for pelican to add that directive to my posts.

There's only one live example at the moment, which is my
`American Greetings hackathon`_ post. The plugin itself has been added to my
fork of `pelican-plugins`_.

It's not all great, though. One thing I would really like is the ability to
render the diagram to SVG instead of PNG. SVG is much better for things like
simple diagrams, as it is web-native, (all it is is a special kind of XML
document), and it's vector-based, making it inherently scalable for different
sized displays. As near as I can tell, ditaa appears to use SVG internally, at
least to some extent. Ideally, I'd like to try to re-implement it in Python, not
necessarily for any benefit, but because the problem sounds interesting.

.. _ditaa: http://ditaa.sourceforge.net/
.. _directive: https://gist.github.com/dvarrazzo/3807373
.. _reStructured Text: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
.. _American Greetings hackathon: /fossrit/american-greetings-hackathon-followup.html
.. _pelican-plugins: http://github.com/Qalthos/pelican-plugins
