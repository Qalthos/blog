Back up to Speed
################
:date: 2011-06-21 22:56
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: peopledashboard, widgets, scrapers, SURS

I've almost closed `bug #106`_. I've done all I can do for now, until I
can figure out how to attribute actions to senators. Until then, I
should comment out the 'actions' tab tomorrow with a note letting
whoever tries this next what I've already tried.

There is still some work to do in this code, particularly with fixing
the hacky Assembly scraping I wrote last year which also broke. However,
considering that the Assembly is not currently one of the bits we are
trying to expose (and they don't have a nice public API like the
Senate), it probably won't get done for a little while.

When I left yesterday, I had exposed the senator's social page, but none
of the other tabs were showing up. The problem for this turned out to be
that the image representing the tab was corrupted and the text beneath
it was white, making it overall look like the tab was invisible. Once I
got a new image for the tab, they all suddenly appeared, though only the
bills had any information.

The next thing to fix was the scraping of the committees, whose pages
had also changed subtly in the past few months. Fixing this was much
less annoying than building them the first time, and I was able to
remove a lot of old shims in the code from when I was first being
introduced to `BeautifulSoup`_. Some of my later changes made this
particularly easy, and since BeautifulSoup is so powerful, I was able to
restore access to the data with relative ease. As a bonus, as soon as I
had committees back up, the tabs for votes and meetings came with it for
free. Suddenly, I was almost there!

The final problem I encountered today is actually not a new one, but one
we struggled with last year, and one I now feel confident I have
actually fixed and understand now. Once I got all the data pulling
again, a few of the pages would crash the server with
UnicodeDecodeErrors.

As a warning, some heavy Python is about to come down
UnicodeDecodeError is an error which happens (generally) when attempting
to decode a string into a Unicode object. This is generally a great
thing to do, as Python strings are generally encoded in the relatively
restrictive ASCII, which does not have characters for any of the more
exciting characters like accents and non-latin symbols. Unicode has no
such restrictions, and indeed has data for many, many more symbols, at
the cost of a few more bits of storage per character.
So why were we getting this error? The relevant line of code was 's =
unicode(s)' and was contained within `WebOb`_ code, not something I was
going to be able to modify successfully. Still, even this shouldn't be a
problem. The purpose of this function is to turn strings to Unicode
strings.

Except I didn't have a string, I already had a Unicode string.
Even this shouldn't be a problem, except that unicode() tries to
interpret its input as a string and then turn it into a Unicode string.
And while Unicode strings can be easily represented as normal strings,
the default of the unicode() function is to try to interpret those
strings as ASCII strings, and I had accents in the strings. These
strings were representing the names of the senators, so I had to make
sure it came out right.

In order to solve this, I had to reversibly represent these names as a
sequence of ASCII characters.

There are a few ways to replace out-of-bound characters when changing
strings into lesser encodings, and I had two useful ones to chose from.
The obvious one to chose was to change the characters into XML character
entities, however this quickly turned out to be insufficient. While
&#233; correctly showed up as é on the page, this string is used to
represent the name everywhere, including in the internal URL
representing the page. And the ampersand was quickly stripped out as a
broken argument to the URL, leading to a page for a nonexistent Senator.
Looking through the code, there were three distinct uses for the name
string. The first, which had started all this, was as an ASCII key to a
dictionary which needed to be authoritative but not necessarily
accurate. In other words, I needed it to be the same everywhere, but it
didn't necessarily need to be the correct name of the senator. The
second was the use on the generated web page, which needed to be as
accurate as possible to the Senator's actual name, as it is going to be
viewed publicly. The third, and the current stickler was the name in the
URL. Again, this had to be authoritative but not necessarily accurate.
This one, however, had to also only include web-safe characters, of
which &, # and ; do not qualify.

I mulled this over for a while, thinking up more and more elaborate
schemes for intercepting the names before they reached critical areas,
but none of it was terribly good coding practice. After far too much
thinking, I realized the obvious answer: have separate internal and
external names. The system still relies on the senator's name, which is
still a questionable practice given the multiple spellings of names that
occasionally pop up, (but mostly because I remember `this post`_, which
is something you should always keep in mind when programming around
names. The display name, on the other hand, has none of the restrictions
on characters (though it still needs to be ASCII to display properly),
but by using XML entities, we can make any character we want without
problems.

This was a long path to take to get back to where we were, but I think
that I really understand Python's Unicode in a way I never grasped
before. This should definitely help in the future as Unicode is a very
important part of coding portable applications and that's something I
want to do.

.. _bug #106: https://fedorahosted.org/civx/ticket/106
.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/
.. _WebOb: http://pythonpaste.org/webob/#introduction
.. _this post: http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/
