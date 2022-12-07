Remysmoke Improving
###################
:date: 2013-07-26 03:44
:author: Katherine Case
:email: Qalthos@gmail.com
:tags: remysmoke

`Remysmoke`_ has had a few updates over the past week, and I think they've gone
pretty well. Remysmoke is now at version 1.2, here's the changelog for the past
few versions:

Remysmoke 1.0
-------------

* Moved graphs from tw2-protoviz to `pygal`_.

* Moved smoke input form from tw2-forms to hand-crafted HTML5 forms.

* Completely removed Toscawidgets and ToscaWidgets2 from Remysmoke (including
  some very old boilerplate TurboGears code).

Remysmoke 1.1
-------------

* Updated codebase to TurboGears 2.3.

* Redeployed Remysmoke on `OpenShift`_ Python 2.7 Cartridge (was Python 2.6).

Remysmoke 1.2
-------------

* Cleaned up login and smoke forms to be more consistent.

* Themed form checkboxes to be consistent with the rest of the UI.

* Added new theming for disabled input boxes.

* Added new 'unsmoke' option, allowing a user to attest that they have not
  smoked that day.

Remysmoke 1.2 went live late last night, and a  hotfix 1.2.1 will be up shortly
with an OpenShift-specific patch dealing with overriding the database location
at runtime.

.. _Remysmoke: http://remysmoke.linkybook.com/
.. _pygal: http://pygal.org/
.. _OpenShift: http://openshift.com/
