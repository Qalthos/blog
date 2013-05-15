OpenShift Troubles
##################
:date: 2012-02-03 06:47
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: FLOSS-seminar, openshift

Recently I've been playing with `OpenShift`_, a new(ish) service from
Red Hat as a sort of 'push to cloud' deployment strategy. It's
interesting for people like me who can whip up a site quick, but don't
necessarily have the framework in place to host it.

Due to my work on `CIVX`_, I've gotten pretty familiar with
`TurboGears`_, and the idea of being able to take a site like that and
run it without having to set up apache or fiddle with paster sounded
real nice. Unfortunately, it was not so simple as it seems.

First up was to get something, anything, running. For a while, OpenShift
was throwing a `500 error`_ when you tried to get a new application
registered. A brief poke into their IRC told had them aware of the
problem and it was fixed shortly. Next came the other part that should
have been easy, running TurboGears.

`Luke`_ our favorite wizard around these parts, wrote a bit of `code`_
to get most of the available applications up and running without too
much effort, including the currently unsupported TurboGears. Running
this went off without a problem, but the resulting site gave me another
happy 500 error. After a consult with Remy, we determined there were
some missing version requirements that kept the site from running. After
pulling those edits out of his repo and moving them upstream to Luke's,
I had a working default TurboGears site.

Until I tried to log in. Then I got another 500 error.
I was beginning to get used to this, but it was still annoying to make a
small change, then push it to the server and wait for the server to
update the settings before I could test it. Even more fun was the
occasional `503 error`_ when OpenShift couldn't keep up with my rapidly
building and tearing down sites.

Feeling that that was going to be a project by itself, I set about
moving all my non-db-interfacing files to this new repository. The
prebuilt version assumes that the site internally is named tg2app, and I
was having trouble convincing it to go by anything else. Eventually I
just decided to move files across one by one; first the templates that
don't care what they're named, then the root controller, than the new
model and widget. A lot of frustration, many `403`_ and `404`_ errors
later, I had something that pretended to work as long as I didn't use
the database. But since the database is kind of the point of the site I
was building, this was not exactly acceptable.

So back to the drawing board then. I had a hunch something was wrong
when I saw SQLAlchemy errors scroll by every time I reloaded the site.
My best guess is that SQLAlchemy is failing to create the tables needed
to run the site and continuing on blindly. Once I realized that, I
dumped a test db from my local copy to the mysql db, and suddenly
everything was working. Or almost everything, anyway.

I could read form the db fine, but any time I tried to modify it, I got
another dreaded 500 error. I poked into everything I could find to try
to figure out where it was failing, and finally determined it couldn't
be on my end, as my local copy worked just as expected.

Finally I stumbled across the anwser, almost accidentally. When I moved
the db from local sqlite to mysql, I failed to set the auto increment
setting on the id of my new databases, so when I neglected to provide an
id for the new entries I was making, mysql quite rightly complained at
me. Unfortunately, since I can't find how to re-enable debug mode (nor
should I really try), I wasn't getting any good error messages.
So what is the site that has been giving me all these troubles? It's a
little site I set up to publicly shame Remy into stopping smoking:
`remysmoke-qalthos.rhcloud.com`_

.. _OpenShift: http://openshift.redhat.com/
.. _CIVX: http://civx.us/
.. _TurboGears: http://turbogears.org/
.. _500 error: http://www.flickr.com/photos/girliemac/6509400855/in/set-72157628409467125
.. _Luke: http://lewk.org/
.. _code: https://github.com/lmacken/openshift-quickstarter
.. _503 error: http://www.flickr.com/photos/girliemac/6540643319/in/set-72157628409467125/
.. _403: http://www.flickr.com/photos/girliemac/6508023617/in/set-72157628409467125
.. _404: http://www.flickr.com/photos/girliemac/6508022985/in/set-72157628409467125/
.. _remysmoke-qalthos.rhcloud.com: http://remysmoke-qalthos.rhcloud.com/
