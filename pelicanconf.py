#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Nathaniel Case'
SITENAME = u'Why Not Wingnut?'
SITEURL = 'http://0:8000'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

#THEME = 'notmyidea'
THEME = 'themes/notmineeither'
DEFAULT_PAGINATION = 5

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = [
    'assets',
    'ditaa',
    'gravatar',
    'related_posts',
]

DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (('resume', 'http://qalthos.github.io/resume/resume.pdf'),
            )

# Blogroll
LINKS =  (('FOSS@RIT', 'http://foss.rit.edu'),
         )
# Social widget
SOCIAL = (('Github', 'http://github.com/Qalthos'),
          ('Google+', 'http://gplus.to/qalthos'),
         )

# Tag Cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 30
