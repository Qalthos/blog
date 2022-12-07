#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Katherine Case"
SITENAME = "Why Not Wingnut?"
SITEURL = "http://0:8000"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"
DEFAULT_DATE = "fs"

# THEME = "notmyidea"
THEME = "themes/notmineeither"
DEFAULT_PAGINATION = 5

PLUGIN_PATHS = [
    "plugins",
    "../pelican-plugins",
]
PLUGINS = [
    "assets",
    "ditaa",
    "gravatar",
    "related_posts",
]
STATIC_PATHS = ["images"]

DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (("resume", "http://qalthos.github.io/resume/resume.pdf"),)

# Blogroll
LINKS = tuple()
# Social widget
SOCIAL = (("Github", "http://github.com/Qalthos"),)

# Tag Cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 30

# Feed settings
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TAG_FEED_ATOM = "feeds/tag/{slug}.atom.xml"

# Generated page settings
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"
