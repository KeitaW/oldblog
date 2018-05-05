#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'KeitaW'
SITENAME = 'Manekiel'
SITEURL = ''
THEME = "pelican-themes/pelican-blue"
PATH = 'content'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'
INDEX_SAVE_AS = 'blog_index.html'
# ipynb configulations
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./pelican-plugins']
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/keita-watanabe-b33956141'),
          ('github', 'https://github.com/keitaw'),
          ('twitter', 'https://twitter.com/keitaw09'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Pelican-blue settings
SIDEBAR_DIGEST = 'PhD Student in a laboratory for Computational Neuroscience'
#FAVICON = 'url-to-favicon'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'keitaw09'
MENUITEMS = (('Blog', SITEURL),
             ('Author', SITEURL))

# Blue-penguins settings
# all defaults to True.
#DISPLAY_HEADER = True
#DISPLAY_FOOTER = True
#DISPLAY_HOME   = True
#DISPLAY_MENU   = True
#
## provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
#TAGS_URL           = 'tags'
#TAGS_SAVE_AS       = 'tags/index.html'
#AUTHORS_URL        = 'authors'
#AUTHORS_SAVE_AS    = 'authors/index.html'
#CATEGORIES_URL     = 'categories'
#CATEGORIES_SAVE_AS = 'categories/index.html'
#ARCHIVES_URL       = 'archives'
#ARCHIVES_SAVE_AS   = 'archives/index.html'
#
## use those if you want pelican standard pages to appear in your menu
#MENU_INTERNAL_PAGES = (
#    ('Tags', TAGS_URL, TAGS_SAVE_AS),
#    ('Author', AUTHORS_URL, AUTHORS_SAVE_AS),
#    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
#    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
#)
## additional menu items
#MENUITEMS = (
#    ('GitHub', 'https://github.com/'),
#    ('Twitter', 'https://github.com/'),
#    ('Linkedin', 'https://www.kernel.org/'),
#)

