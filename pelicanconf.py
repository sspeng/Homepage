#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'HustMeituanBot'
SITENAME = '美团点评技术俱乐部'
SITESUBTITLE = '华中科技大学'
SITEURL = '/pages/about/index.html'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'
LOCALE = 'zh_CN.UTF-8'

DATE_FORMATS = {
    'en': (('en_US', 'utf8'), '%a %Y-%b-%d'),
    'zh': (('zh_CN', 'utf8'), '%Y年%b%d日 周%a'),
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 友链
LINKS = [
    ('朋友A的博客', 'http://a.blog.com'),
    ('朋友B的博客', 'http://b.blog.com'),
]

THEME = 'theme'
HEADER_COVER = '/images/bg.jpg'
SOCIAL = (('github', 'https://github.com/HUSTMeituanClub'),
          ('envelope', 'mailto:@hustmeituan.club'))

STATIC_PATHS = ['static',
                'images',
                'extra/favicon.ico',
                'static/CNAME']

EXTRA_PATH_METADATA = {
    'static/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

MD_EXTENSIONS = [
    'admonition',
    'toc',
    'codehilite(css_class=highlight)',
    'extra',
]

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

MENUITEMS = [('关于', '/pages/about/index.html')]
