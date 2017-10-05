#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'speedmann'
SITENAME = u'Speedmann.de'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/speedmannde'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TYPOGRIFY = True
TWITTER_USERNAME = "speedmannde"
PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['filetime_from_git', 'gravatar']
PLUGINS = ['gravatar', 'i18n_subsites']
AUTHOR_EMAIL = "speedmann@speedmann.de"
THEME = "pelican-themes/pelican-bootstrap3"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
SHOW_ARTICLE_AUTHOR = True
SHOW_DATE_MODIFIED = False
CC_LICENSE = "CC-BY-SA"
CC_ATTR_MARKUP = True
