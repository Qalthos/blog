Openshift Troubles Continued
############################
:date: 2012-02-03 06:47
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: FLOSS-seminar, openshift

I figured out the problem I was having with OpenShift.

To put it simply, I didn't pay enough attention.

For reference, when moving an existing TurboGears app to OpenShift, make
sure you add the changes in config/app\_cfg.py

As soon as I saw that, I felt really silly for missing it. I was so sure
that I had gotten all the relevant changes, but apparently I somehow
missed this file.

More detailed directions coming soon.
