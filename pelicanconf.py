AUTHOR = 'simmessa'
AUTHOR_META = {
  "simmessa": {
    "name": "Simone Messaggi",
    # "cover": "https://2.gravatar.com/avatar/b17e29eaad304bcbba221784647c34453ea200e7cd901c19023cf0e4d461323b?size=256&d=initials"
    "image": "images/simmessa.png",
    "location": "Italy",
    "linkedin": "simmessa",
    "github": "simmessa",
    "twitter": "simmessa",
    "instagram": "simmessa",
  }
}

CSS_OVERRIDE = ['theme/css/simonemessaggi.css']

SITENAME = u'SimoneMessaggi.it'
SITESUBTITLE = u'Master at Mistakes'
SITEURL = "http://127.0.0.1:8000"
COPYRIGHT_YEAR = "2025"

THEME = 'attila'

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

SHOW_TAGS_IN_ARTICLE_SUMMARY = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# SEO Optimization
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = True # Subfeature of SEO enhancer

# Minify

CSS_MIN = True
JS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True