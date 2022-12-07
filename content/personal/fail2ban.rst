Fail2ban woes
#############
:date: 2017-08-24 16:30
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: server

So I had a bit of a scare this morning.

I'm in a hotel in North Carolina, hundreds of miles from my server, when I try to log in and get a "Connection refused" error. Phooey. I hope the hotel wifi is just filtering port 22 for some terrible reason, and hop to a friend's server over a non-standard port and I'm in. Great! I type out the connection again and...

Connection refused

Hmmm. This is starting to get concerning. I briefly freak out that my server might have had a terrible accident, when I realize that all of the other services I rely on all the time are still running. Phew. Still, I don't have ssh access, and that is very troubling. I start poking around with other things and eventually unconsciously try to ssh back in to check something and to my surprise, it works! As soon as I realize what I've done, I pull up journalctl to see if sshd is going crazy and I'm met with hundreds of lines of Chinese IPs plugging away at my server.

But wait! I have fail2ban installed. That should be stopping these, right? Well maybe something broke when the server was upgraded to Debian 9... and now I'm off trying to figure out what is running and where the config is.

Some time later, I finally have a solution. The problem (ultimately) was systemd, though not directly. I had moved this system to systemd some time early in Debian 7, which meant that the standard logging locations were still there, but no loger being written to. So fail2ban was looking for /var/log/auth.log, found a file, read it and found no problems, completely ignoring the fact that the file hadn't been written to since 2013. This isn't really fail2ban's fault, it has support for ingesting the systemd journal, but on Debian, the default backend still tries to use those files. I could set up rsyslog to start writing those files again, but I have no particular need or desire to do that outside of this program, especially as fail2ban knows how to read the journal on its own, if it's configured to do so.

So the solution is pretty simple, though it took me a while to get there. First, I had to ``apt-get install python3-systemd``, to get the proper libraries to actually use the journal. Then, I had to have the following in my jail.local:

.. code-block:: ini

  [sshd]
  backend = systemd

I also put a few other tweaks in there as my config hadn't actually moved over from the previous version, but since it's now in the jail.local instead of editing the system config, this shouldn't be a problem again.
