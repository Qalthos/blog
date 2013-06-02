Recent Projects: Democrat & Chronicle
#####################################
:date: 2012-08-22 22:16
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: journalism, data alchemy

One of the new projects I had this summer was a project proposed by the
`Democrat & Chronicle`_. The project involved access to a selection of
emails sent to the Greece school district in the wake of the YouTube
video involving several of their students. The idea was that we would
get a dump of email bodies and try to glean some information out of
them.

The first hurdle, unfortunately, was getting at the information. Shortly
after we were approached with the request, I received an Access file
containing around 5000 email bodies to go through. Being what we are,
most of the resources in the FOSSBox are oriented around Linux, and no
one about had a copy of Access installed to get the data into a more
friendly format.

In theory, there are ODBC drivers for access databases, just like there
are for any other database system. In practice, however, they seem to
only exist for Windows machines which, while not surprising, was
disappointing. This led me to dig out an old VirtualBox VM with Windows
XP on it, install the Access drivers from Microsoft, and throw
LibreOffice on it, too. There's other ways I could have gotten this done
instead of LibreOffice, but I was still hoping this could be a simple
action at the moment.

LibreOffice Base eventually got into the Access file, but then the
troubles started again. It initially prompted me to save a LibreOffice
database file, which sounded great to me... it could export it
immediately, then I could copy it over and finish the task in Linux.
Unfortunately, all this file did was create a small wrapper around the
Access file, telling LibreOffice where the file was located, and what
was needed to open it. So now I was back to trying to export the data.
LibreOffice, though, was not willing to play along. I admit I am less
than familiar with the Base component of LibreOffice, however some
exploration and more searching online led me to believe I could not do
the simple translation of data from one format to another from within
Base.

Instead, I needed to select the table I was interested in (the only
table in the database), tell LibreOffice to copy the table, then open a
new spreadsheet in LibreOffice Calc and save the data that way. While
this makes some sense to me (Base being simply for basic interaction
with databases, Calc for manipulating raw data), I was dismayed that I
could not find some way to export a single table to a common data
format, like CSV, instead of having to go through yet another step. In
any case, once I dumped the data into Calc, I could easily save it to
CSV, drop that into my real computer, stop the VM, and get to work for
real.

The end result is `this`_. I'm not sure it will ever be of any
particular use to anyone other than myself to remind me how to use the
Python NLTK module (whose documentation seems to be geared more towards
researchers than those already familiar with Python), and is hardcoded
to certain facets of the data I was given, but it does manage to do a
few things, and at each step it dumps the state of the data to a file so
I can inspect the process and consider possible improvements.

.. raw:: html

   </p>

.. _Democrat & Chronicle: http://www.democratandchronicle.com/
.. _this: https://github.com/Qalthos/mail_scrape
