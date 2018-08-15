#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'KeitaW'
SITENAME = 'Manekiel'
SITEURL = ''
THEME = "pelican-themes/uikit"
PATH = 'content'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'en'
#INDEX_SAVE_AS = 'index.html'
# ipynb configulations
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./pelican-plugins', './plugins']
PLUGINS = ['ipynb.markup', 'render_math', "better_codeblock_line_numbering"]
MARKDOWN = {
    'extensions' : ['markdown.extensions.codehilite', 'markdown.extensions.extra', 'markdown.extensions.meta'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        # if you have nothing to configure there is no need to add a empty config
        #'markdown.extensions.meta': {}, 
    }
    # By default Pelican already sets the output_format to html5 so it is only needed if you want something else
    #'output_format': 'html5',
}
# For line number PLUGINS = ["better_codeblock_line_numbering"]
#PLUGINS = ["render_math"]
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
LOCALE = ('usa', 'jpn',  # On Windows
    'en_US', 'ja_JP'     # On Unix/Linux
    )
DATE_FORMATS = {
    'en': ('en_US','%a, %d %b %Y'),
    'jp': ('ja_JP','%Y-%m-%d(%a)'),
}
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
SIDEBAR_DIGEST = 'A blog written by a PhD Student in a laboratory for Computational Neuroscience'
#FAVICON = 'url-to-favicon'
#DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images', 'files', 'js']
## Pelican 3.7+
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'linenums': None}
    }
}
# For uikit
# control the sidebar-tags/links with a simple setting.
# If the value
# is 0, all links will be displayed
# is negative, no links will be displayed
# is positive, that many links will be displayed

DISPLAY_TAGS_ON_SIDEBAR_LIMIT = 0
DISPLAY_LINKS_ON_SIDEBAR_LIMIT = 0
AUTHOR_IMAGE = "tori.jpeg"
# choose default, gradient or almost-flat:
STYLE = "gradient"
# wether to capitalize article headings
# False means everything is not transformed
CAPITALIZE_HEADINGS = True
# available licenses (see LICENSE['cc_name']):
# licenses in version 4.0
# by-nc
# by-nc-nd
# by-nc-sa
# by-nd
# by-nd-nc
# by-sa
# all icons are included locally,
# however you can use the icon hosted by <https://licensebuttons.net/>.
# compact (80x15) or normal (88x31) icon
LICENSE = {
    'cc_name':"by-sa",
    'hosted':False,
    'compact':True,
    'brief':False
    }
