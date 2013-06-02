pyDex on Sugar
##############
:date: 2011-01-19 23:51
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: sugar, pyDex

A warning, this gets very technical with lots of acronyms and jargon.
tl;dr: I have a new pyDex branch which \*should\* run on the OLPC
A few days ago, I decided I'd finally see how well pyDex runs on the
OLPC. Turns out, it runs pretty well, which isn't too surprising as it
is written in pure pyGTK and Glade, both of which are well supported in
Sugar.
So today, I loaded up my dev files and set to work. First, though, I had
to clean up my dev branch and finish committing the few hacks I had
accumulated over the last few months. I finally fixed the zero index bug
and found I had a problem in my new scraper that was causing all the
evolution problems. In any case, that's all fixed, so my dev branch is
nice and clean and almost ready for the Black/White release in a few
weeks.
Getting back to Sugar, I finally found `a good tutorial`_ on \*porting\*
a pyGTK program rather than writing a new one. While admittedly I
haven't looked very hard, I had had a bit of a problem getting past the
example activity before, probably due to my use of Glade as I cannot
replace my top window as easily when it is automatically pulled from
Glade's XML and I really don't feel like defining everything in code.
The most useful thing I found in this tutorial is sending different
parents to the main panel depending on where it is called from. So if we
call the program normally, main\_window is still loaded from Glade, but
if Sugar loads it, we use their prebuilt panel.
It still needs to be tested, and I need to add actual activity
information (and an icon eventually), but I think it should work. I'll
probably get to test it sometime this weekend, maybe even turn it into a
real activity by then. This is still just a small project, and I doubt
it will ever go up on Sugar's activities site, but it has given me a
much better understanding about how non-pygame activities work.

.. _a good tutorial: http://magazine.redhat.com/2007/04/26/building-the-xo-porting-a-pygtk-game-to-sugar-part-two/
