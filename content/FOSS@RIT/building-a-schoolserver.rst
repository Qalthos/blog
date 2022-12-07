Building a Schoolserver
#######################
:date: 2013-08-05 02:04
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: sugar, schoolserver

One of my tasks for this summer has been to try and get the FOSSBox's
schoolserver up and running again. We previouly had one a number of years ago,
but the hardware failed some time ago and the system itself was running a
hacked-together Debian build and did not have access to some of the actual
schoolserver scripts.

I first attempted to run the `instructions`_ for the latest proper release of
the XO Schoolserver (henceforth XS), but this did not end very well. For one,
the instructions (and many automated scripts) assume you have two network
cards: one for the internal LAN to which the XO laptops connect, and another
connecting to the Internet. This assumption that the XS would be the gateway
device for a network of XO laptops would be fine in most deployments where
there is no existing infrastructure to get in the way, but at RIT where there
is not only significant infrastructure, but infrastructure I cannot easily
modify or control, it is less applicable.

Here are the steps I have taken to turn a fresh CentOS/RHEL server into an XS:

#. Set up `EPEL`_.
#. Add the `OLPC-XS repository`_ to your yum config.
#. ``yum install ejabberd idmgr ds-backup-server xs-activity-server``
#. ``xs-domain-config <domain name>``
#. ``xs-setup``
#. Use ``system-config-firewall-tui`` to unblock ports 22, 80, 8080, 5222, 5223,
   and 4369

``xs-setup`` is the most trying of the commands, because it does a lot of
background work to set up the OLPC versions of many config files (while still
leaing the originals in place).

There's more to it, ``xs-setup`` tends to have some annoying side effects,
some of the config files need to be manually updated, but this is the general
idea. This post will be further updated as time goes on.

The main problem seen so far is that this is being set up on a RHEL server
backed by XEN, and the OLPC-XS repository keeps wanting to install an
incompatible kernel, hosing the system on a regular basis.

.. _instructions: http://wiki.laptop.org/go/XS_Installing_Software_0.7
.. _EPEL: http://fedoraproject.org/wiki/EPEL
.. _OLPC-XS repository: http://wiki.laptop.org/go/XS_Installing_Software_0.7#Installing_on_top_of_existing_OS_installation
