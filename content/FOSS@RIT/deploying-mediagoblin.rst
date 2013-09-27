Deploying MediaGoblin 1: FastCGI vs uWSGI
#########################################
:date: 2013-09-23 13:20
:author: Nathaniel Case
:email: Qalthos@gmail.com
:tags: mediagoblin, yacht, uWSGI

Last week I did a thing I really wasn't expecting to. I deployed
`MediaGoblin`_ to FOSS\@RIT's yacht server `here`_. The initial setup and
`instructions`_ are some of the clearest and straightforward I have seen in an
open-source project.

There are several reasons I haven't written this up earlier. One of the reasons
was the web server configuration file was more complex than I was used to, so
in order to get the server running quickly, I made a new config file for port
8080. Unfortunately, due to various arcane networking policies, while this
allowed anyone inside RIT to access the server, it was still not available to
the outside world.

Also, though the instructions were very clear, they used a few things I had not
used before, and a few things that weren't used in the way I was used to them.
This is the first blog post on the subject, detailing my confusion with
FastCGI and its eventual replacement with uWSGI.

What the ``flup``?
------------------

MediaGoblin, as documented, uses FastCGI to route requests from the web server
to MediaGoblin. The CGI in FastCGI refers to the 'Common Gateway Interface',
a standard developed to allow web servers to act as 'gateways' to serve not
just files but the output of executable programs. The MediaGoblin docs describe
how to use a python module called ``flup`` to enable this communication.

There's a bit more to it than that, but in Python land, this
turns out to be a more questionable prospect than it might seem. Python already
has its own gateway interface (called the web server gateway interface, or
WSGI) which it is using to talk to FastCGI to have the WSGI turned into CGI so
that it can be interpreted by the server and turned into a web page. This would
be fine except that there are other WSGI-specific modules which can translate
the WSGI into a web page directly.

At this point, I assume that you are either skipping ahead past things you
already know or are horribly lost, so I'll just say that I eventually moved
MediaGoblin from the ``paste->flup->FastCGI->nginx`` contraption it was to a more
comprehensible ``uWSGI->nginx``, and this is how I did it.

Enter uWSGI
-----------

First, I changed the nginx config to talk to uWSGI instead of FastCGI.
As I was also trying to move MediaGoblin to a subdirectory, I also added the
``uWSGI_modifier1`` line and altered ``SCRIPT_NAME`` accordingly:

.. code-block:: nginx

    # Load MediaGoblin via uWSGI
    location /mediagoblin/ {
       include uWSGI_params;
       uWSGI_pass 127.0.0.1:26543;

       # our understanding vs nginx's handling of script_name vs
       # path_info don't match :)
       uWSGI_param SCRIPT_NAME "/mediagoblin";
       uWSGI_modifier1 30;
    }

Second, I altered the ``lazystarter.sh`` file to accommodate being run with
uWSGI. This is a bit complicated as ``lazyserver.sh``, ``lazystarter.sh``, and
``lazycelery.sh`` are all actually the same file, with certain things changing
depending on the name by which it is invoked. I changed two sections [#]_,
first:

.. code-block:: bash

    local_bin="./bin"
    case "$selfname" in
        lazyserver.sh)
            starter_cmd=paster
            ini_prefix=paste
            ;;

became:

.. code-block:: bash

    local_bin="./bin"
    case "$selfname" in
        lazyserver.sh)
            starter_cmd=uwsgi
            ini_prefix=paste
            ;;

And then near the very end of the file:

.. code-block:: bash

    export CELERY_ALWAYS_EAGER=true
    case "$selfname" in
        lazyserver.sh)
            $starter serve "$ini_file" "$@" --reload
            ;;

became:

.. code-block:: bash

    export CELERY_ALWAYS_EAGER=true
    case "$selfname" in
        lazyserver.sh)
            $starter --plugin python --virtualenv . --ini-paste "$ini_file" "$@"
            ;;

This method allows you to keep using all the information on how to run
MediaGoblin from paste.ini, while using uWSGI to do all the heavy lifting.
The socket still needs to be defined with the command, though, with
``./lazyserver.sh --socket 127.0.0.1:26543`` or whatever socket you are using.

As a side note, this also allows us to use your system's uWSGI `emperor`_ to
manage bringing up the uWSGI process for you. If you are running `celery as a
separate process`_, this still needs to be done somehow, but otherwise (or if
you've kept ``CELERY_ALWAYS_EAGER=true``), then MediaGoblin should be managed
automatically. This is the format I eventually settled upon, using the
following uWSGI ini file:

.. code-block:: ini

    [uwsgi]
    plugin=python
    uid=mediagoblin
    gid=mediagoblin
    socket=127.0.0.1:26543
    virtualenv=/srv/www/mediagoblin
    chdir=/srv/www/mediagoblin
    ini-paste=/srv/www/mediagoblin/paste.ini
    logto=/srv/www/mediagoblin/mg.log

What Next?
----------

As far as I can tell, this should have been all we needed to get running.
Well, this wouldn't have been necessary either, except for some of the
repercussions of the other big problem that reared it's head, SELinux.

But that is `another post`_.

.. _MediaGoblin: http://mediagoblin.org
.. _here: http://yacht.rit.edu/mediagoblin/
.. _instructions: https://mediagoblin.readthedocs.org/en/v0.5.0/siteadmin/deploying.html
.. _emperor: http://uWSGI-docs.readthedocs.org/en/latest/Emperor.html
.. _celery as a separate process: http://mediagoblin.readthedocs.org/en/v0.5.0/siteadmin/production-deployments.html#separate-celery
.. _another post: deploying-mediagoblin-2-selinux.html
.. [#] This statement is not entirely accurate. I actually made a new link
       named ``lazyuwsgi.sh`` and added the sections instead of altering the
       existing ones. This format was chosen for clarity.
