Deploying MediaGoblin 2: SELinux
################################
:date: 2013-09-27 16:09
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: mediagoblin, yacht, SELinux

So, `earlier`_, I wrote about my experience deploying `MediaGoblin`_. None of
this was necessary, I was mostly trying to diagnose some problems I was having
and found uWSGI a more comfortable environment than FastCGI.

And what problem was this, you ask? Well, when I first ran through the
installation instructions, everything worked swimmingly (the port issues
mentioned aside). The server it was running on, however, was running Fedora 17,
while Fedora 20 has just reached alpha status recently. So, in the interest of
retaining compatibility and security fixes, there was a fun afternoon of double
distribution updates.

At first, everything seemed to be working fine, but then MediaGoblin began
inexplicably throwing 'permission denied' errors. As usually happens in these
cases, the culprit was SELinux, an additional security layer which normally
transparently protects your system, until something unexpected shows up.

I don't pretend to understand SELinux, but I do understand the security
improvements it brings. Plus I don't want to disable it on a system I don't
own.

Long, boring story short (and it was very long, being noticed first, and not
fixed until well after I figured out how to get uWSGI running), I got something
reasonably close to what I think I'm supposed to do. The key was the command
``setsebool -P httpd_can_network_connect on``, which re-enabled the ability for
nginx to talk to programs on a network socket, as in the MediaGoblin
documentation.

I initially changed to a file-based Unix socket, but I could not, for the life
of me figure out how to enable this simply without changing a large number of
SELinux booleans. There may be some simpler way of accomplishing this, but alas,
in this case SELinux has once again bested me.

.. _earlier: deploying-mediagoblin-1-fastcgi-vs-uwsgi.html
.. _MediaGoblin: http://mediagoblin.org
