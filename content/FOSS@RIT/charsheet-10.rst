:title: Charsheet 1.0
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: charsheet, openshift

I've been doing some work for `Charsheet`_ recently, fixing old bugs and adding
new features. I figured it was about time for a 1.0, so I tagged it and released
it to the wild. Many thanks to `oddshocks`_ not only for the original 0.1
version of charsheet, but for continued assistance in massaging the site into
something cool.

Notable Features
----------------

* Character classes! You are now given a class based on your favorite language
  (by klocs [#kloc]_), and your top two stats on the page.
* Fixing Github integration. This was technically fixed in August, but it was
  not finalized or pushed upstream until a few weeks ago.
  - Github backend switched from pygithub3 back to pygithub
* Completely removed tw2 from the site [#tw2]_
* Charsheet will now deploy on Openshift!
  - But not with a MySQL database. This is a known `bug`_ with knowledge.
* Gnu-cat Will no longer stick around when the back button is pressed
  - Yes, it is actually called GNU-cat.
* Fixed some incompatibilities with Pyramid 1.5

There's more, but that is the big stuff I'm seeing from the git log. In any
case, the site is live, so just hop over to
https://charsheet-qalthos.rhcloud.com and put in your Github, Ohloh, and/or
Coderwall username(s) and see what your coder character sheet looks like!

.. [#kloc] Kilo-Lines Of Code, or a unit of 1000 lines of code for the
    uninitiated.
.. [#tw2] This bears some explanation, but it was just tw2.forms, and the forms were
    static, meaning they were quite underutilized. Forms are now pure HTML
    forms.

.. _Charsheet: https://charsheet-qalthos.rhcloud.com
.. _oddshocks: http://oddshocks.com
.. _bug: https://github.com/civx/knowledge/issues/5
