Just another ten-hour day
#########################
:date: 2010-09-09 18:11
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: peopledashboard

Today was another exciting day in CIVX-land.
tl;dr: I spend the day helping other people and being awesome
It started out with the latest in a series of attempts at getting
`Rebecca`_ to a working CIVX repo. As I work through this with her, I am
slowly working out how all this works together (though admittedly it is
largely me flailing while Rebecca watches). With `Luke's`_ help, I
eventually realized that the only thing really needed for CIVX to run is
python-virtualenv (it can run without, but that involves actually
installing python packages to /usr/local, something generally undesired
for a development environment). After some question of whether Rebecca
had sudo permission, we eventually discovered she did, and a short sudo
easy\_install virtualenv later, we were ready to start installing the
CIVX stack.
If you haven't read the `CIVX developer's guide`_ (and I think it's
probably safe to assume you haven't), it's a bit of a mess. Not actually
bad, but short and disorganized. This isn't too bad when you've got a
small, fairly tight development group with the main brain usually a ping
away on IRC, but as people are finding CIVX, I have taken it upon myself
to document every bump in my path. When I was first thrust into CIVX,
the page was much sparser with less detail and fewer sections, I have
added areas whenever there was a question of how to do what that
eventually came down to 'ask Luke'. Any time an arcane set of commands
came up I tried to get them on the page with as much information as I
could figure out, hopefully someone will take pity on my notes and make
them more descriptive.
Around this time `Kate`_ also had a few questions for me, most of which
I could figure out. However, I was still trying to get Rebecca running
and hadn't even touched my own computer more than to turn on IRC and
look a few thins up for Rebecca. Kate was having some trouble as she was
trying to scrape information off the NYS Senate page of senators,
neither of which I had done before. Rebecca had other things to do, and
getting her Mac up to speed was a lot of wait and pray so I switched
over to Kate's task. Now Kate also has a Mac, but she was set up with
CIVX long ago and could never quite explain to me how, thanks again to
arcane commands.
Anyway, her task involved a particular unicode character in a senator's
name not playing well with her scraped name-to-url converter magic.
Having only last night read `Falsehoods Programmers Believe About
Names`_ off StumbleUpon, I immediately recognized this way as a dead
end. Sure, you could force all the current names into this pattern, but
it would never last. Some day, a senator would show up such that the
senate's conversion script and ours didn't match, and then that senator
would disappear from CIVX. After a bit of poking, however, I found that
each senator had a link to their contact page right in the div we were
scraping. A bit of poking around later, and I had a 100% reliable link
to each senator's page, as verified by the senate themselves. Suddenly
every senator's page worked, without any of this needless mucking about
in unicode transformations.
Which brought us to our second problem. Most (with one important
exception) senators have a page hosted on http://www.nysenate.gov, and
most have a contact page at /senators/first-m-last/contact.
What that page contains, however, seems largely up to each senator. Kate
had (and was quite proud of) her 4-line, incredibly complex and
unmaintainable regular expression which she used to mangle each page
into a regular form. However, as we poked further and further, we found
more and more inconsistencies and exceptions to the regular expression.
Clearly this was completely the wrong way again, but what was the right
way.
I suddenly saw an interesting anomaly. Most senators had the contact
info were styled exactly the same, despite having quite varying styles
otherwise. Kate had already seen that most of the addresses are together
in some sort of paragraph tag, and was trying to regex on the contents
of each paragraph on the page. What she hadn't noticed was that every
page had a <div class="field-content"> that contained all the contact
info. Now that, that was something a bit more to go on. Furthermore,
this contained all the contact info- occasionally more, but always the
minimum was their District Office and their Albany Office. Furthermore,
it was already in some form of HTML, which Kate had previously been
stripping and rebuilding manually. If we simply took this HTML as-is and
plugged it into CIVX's contact page, instantly every senator had exactly
what we (and they) wanted!
Well, almost.
It was about at this point that Rebecca went home for the day, CIVX not
yet working. a few important packages were missing from `pypi`_, keeping
us from completing the CIVX setup step so she could get cracking on real
CIVX, without needing me to merge every change she wanted to push. Still
this left me with more time to work on the regular expressions.
Now, most senators worked flawlessly, with two obvious exceptions. the
first, and the one I didn't want to tackle just yet, was the senator I
mentioned briefly above, the page of `Sen. Kemp Hannon`_. Notice
anything different about his page? Well, for one, it's not hosted on
nysenate.gov, and for another, he has no explicit contact page. The
first made our scraper entirely useless without coding in an exception
for senators with separate websites, and the second made such an
exception next to impossible to make general, without reverting back to
the 'check each paragraph for addresses' method.
So Kemp was put on the backburner for now. The other one, which failed
somewhat more spectacularly, didn't even break. Rather, the contact page
of `Sen. John J. Flanagan`_. Putting aside for the moment the excess
content in the div, including the NYS seal, and a few lines about
contact information, this is the worst example against automatically
generated HTML I have had the misfortune of needing to scrape.
Problem 1: <p >&nbsp;<p /><br /> I kid you not, this is on the page a
minimum of 20 times in a row so that his Albany Office is so far below
the fold so as to be nonexistant. Sometimes there's inline styles,
sometimes not. One line has a simple space character instead of the
edgier, hipper &nbsp;. I wanted them all gone.this resulted in five
separate regexes so python wouldn't get too greedy and remove all the
content. One to replace &nbsp; with ' ', another to remove all
whitespace between a closing angle bracket and an opening one, a third
to remove anything matching style="\*", a fourth to rmove all the (now)
empty paragraphs, and a fifth and final one to turn any group of two or
more consective break tags into a single tag. It is probably fortunate
that python would not correctly apply my first attempt which was far
less readable, and more of a one-liner, as I don't know if I could have
understood it now had I not broken it into its component parts.
Problem 2 is a bit more of a WTF moment, both beutiful and frightening,
so I will reproduce it here verbatim::

    <P style="TEXT-ALIGN: center"><SPAN style="COLOR: #012849; FONT-SIZE:
    18pt"><SPAN><SPAN><SPAN style="LINE-HEIGHT: 115%; FONT-FAMILY:
    'Calibri', 'sans-serif'; COLOR: #012849; FONT-SIZE: 16pt;
    mso-fareast-font-family: Calibri; mso-ascii-theme-font: minor-latin;
    mso-fareast-theme-font: minor-latin; mso-hansi-theme-font: minor-latin;
    mso-bidi-font-family: 'Times New Roman'; mso-bidi-theme-font:
    minor-bidi; mso-ansi-language: EN-US; mso-fareast-language: EN-US;
    mso-bidi-language: AR-SA"><SPAN><STRONG><SPAN style="FONT-FAMILY: Times
    New Roman">District Office<BR /></span></strong></span><SPAN
    style="COLOR: #012849; FONT-SIZE: 16pt"><SPAN style="FONT-FAMILY: Times
    New Roman">260 Middle Country Road, Suite 203<BR />Smithtown, New York
    11787<BR />631-361-2154<BR />631-361-5367
    FAX</span></span></span></span></span>

For those of you following along at home, that's
P(text-align) > SPAN(color, font-size) > SPAN > SPAN > SPAN(line-height,
font-family, color, font-size, a bunch of other font styles) >
SPAN > STRONG > SPAN(font-family) >
SPAN(color, font-size) > SPAN(font-family)
Naturally, my first order of business was to remove every single span
from the HTML we take in. Because, frankly, this is preposterous. We
already (by problem 1) strip out all the style information, because
frankly, we don't need it, so this mess just turns into six nested
spans, not a very useful thing. Suddenly, the HTML coming out of the
sanitizer is much more compact, and not just because of all the breaks
and paragraphs I took out.
By the time I finished with this, it was about an hour after most
everyone else had left. I spent the next half hour checking that my
sanitizer didn't break existing pages (it did, but only minorly) and
making sure my code was legible.
At that point, almost ten hours after I had started, I sat back,
commited my final changes, and decompressed. \*This\*- this is why I
love open source.

.. _Rebecca: http://www.rebeccanatalie.com
.. _Luke's: http://lewk.org
.. _CIVX developer's guide: https://fedorahosted.org/civx/wiki/Setup
.. _Kate: http://foss.rit.edu/user/17
.. _Falsehoods Programmers Believe About Names: http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/
.. _pypi: http://pypi.python.org/pypi
.. _Sen. Kemp Hannon: http://www.kemphannon.com/
.. _Sen. John J.  Flanagan: http://www.nysenate.gov/senator/john-j-flanagan/contact
