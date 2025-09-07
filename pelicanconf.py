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

MENUITEMS = (
  ('Home', '/'),
  ('Rants', '/category/rants/'),
  ('Tech', '/category/tech/'),
  ('Humans', '/category/humans/'),
  ('Music', '/category/music/'),
)

### Plugins

PLUGINS = [
  "pelican.plugins.image_process",
  "pelican.plugins.minify",
  "pelican.plugins.neighbors",
  # "pelican.plugins.obsidian",
  "pelican.plugins.related_posts",
  "pelican.plugins.seo",
  "pelican.plugins.sitemap",
  "pelican.plugins.statistics",
  "pelican.plugins.webassets",
  "pelican_redirect",
  # "i18n_subsites",
]

CONTENT_REDIRECT_CONFIGURATION = [
    {
        "ARTICLE_URL": "{slug}",
        "PAGE_URL": "{slug}",
    }
]

DEFAULT_LANG = 'it'

# Languages
# I18N_SUBSITES = {
#     'it': {
#         'SITENAME': 'SimoneMessaggi.it',
#         },
#     'en': {
#         'SITENAME': 'SimoneMessaggi.it',
#         }
#     }

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/ico']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

CSS_OVERRIDE = ['theme/css/simonemessaggi.css']

SITENAME = u'SimoneMessaggi.it'
SITESUBTITLE = u'Learn the most from the worst'
SITEURL = "http://127.0.0.1:8000"
SITE_DESCRIPTION = "Il sito personale di Simone Messaggi, blog tecnico opinionistico musicale di uno che di errori ne ha commessi, e tanti."
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
)


# Social widget
SOCIAL = (
  ('Twitter', 'http://twitter.com/simmessa'),
  ('Github', 'https://github.com/simmessa')
)

DEFAULT_PAGINATION = 10

SHOW_TAGS_IN_ARTICLE_SUMMARY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Sitemap
SITEMAP = {
  'format': 'xml',
  'priorities': {
    'articles': 0.5,
    'indexes': 0.5,
    'pages': 0.5
  },
  'changefreqs': {
    'articles': 'monthly',
    'indexes': 'daily',
    'pages': 'monthly'
  }
}

### SLUGS:

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{lang}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{lang}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_URL = '{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_URL = '{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'

# Author
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'author/'
AUTHORS_SAVE_AS = 'author/index.html'

#Archives
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'


# SEO Optimization
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = True # Subfeature of SEO enhancer

# Minify OFF

CSS_MIN = False
JS_MIN = False
HTML_MIN = False
INLINE_CSS_MIN = False
INLINE_JS_MIN = False

# Random cache breakers
JSMIN = ".min"
CB = "?cb=123"