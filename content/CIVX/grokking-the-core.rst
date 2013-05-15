Grokking the Core
#################
:date: 2011-06-21 22:55
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: scrapers, SURS, polyscraper

This week begins the real dive into the core of what makes CIVX. Today
(and yesterday, though yesterday hardly counts as a real day) were spent
adding major functionality to the polyscraper, something that's been
overdue for a long time now.
But what is this magical polyscraper? Well, in short, it's magic. A lot
of magic, actually, and that's half the problem. You see, in ye olden
days of CIVX, each data source had to have its own scraper, and these
were called whenever CIVX decided its data was old enough to get shoved
out and replaced with new data. This was all well and fine, except that
it took a very long time to get a scraper written for a new data source.
You would have to define all the columns, give it a location to look,
make sure you understood the site's particular dialect and scrubbed out
any irregularities in their data. What the poly scraper does is it
replaces all of those individual scrapers and replaces them with one big
scraper which is smart enough to deal with any url it finds.
What I've been doing is adding new sources of data to the polyscraper.
In particular, yesterday was spent adding the ability to read files off
of a local disk and properly store them. This, in turn, exposed a few
holes in the underlying framework which needed to be patched. However,
this is a vitally important function, as things like the SunlightNY
scraper I wrote last year works outside of CIVX proper (in Java, no
less) and cannot be thrown into the polyscraper as easily. But I can
download the files locally, and then work on them when it is convenient.
With proper message passing, I can even seamlessly tell the polyscraper
to pick up the files as soon as they are downloaded.
Previously to this I had been working at the periphery of CIVX, adding
functionality to widgets and individual scrapers. This is my first real
push into the core functionality of CIVX, and it is good to see that I
really have picked enough up in all this time to really start to
understand the underlying structure of everything. Every day I learn
more about what goes on inside this machine, and every day marks another
set of tools I've learned to wield. I can't wait to see how far I get by
the end of the summer.
