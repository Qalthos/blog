#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys

sys.path.append(".")
from pelicanconf import *

SITEURL = "http://blog.katherineca.se"

STATIC_PATHS += ["extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

# DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-40338393-1"
