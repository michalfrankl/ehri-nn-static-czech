import datetime

AUTHOR = 'EHRI'
SITENAME = 'EHRI-CZ'
SITEURL = ''
COUNTRY_CODE = 'CZ'
SITE_TITLE = 'Český uzel Evropské infrastruktury pro výzkum holokaustu'
COPYRIGHT_YEAR = datetime.datetime.now().year

PATH = 'content'

TIMEZONE = 'Europe/Praha'

DEFAULT_LANG = 'cs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('O EHRI', ''),
    ('Český uzel EHRI', 'about'),
    ('Služby', 'services'),
    ('Archivní databáze', 'archivaldata'),
    ('Uživatelé', 'users'),
    ('Novinky', 'news'),
    ('Kontakt', 'contact'),
    )

DEFAULT_PAGINATION = False

THEME = 'ehri-theme'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
