# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://www.simonemessaggi.it" # https://simmessa.github.io/simonemessaggi-pelican"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Minify ON

CSS_MIN = True
JS_MIN = False
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "G-Q242MTLMK7"
