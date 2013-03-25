#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Greg Bowyer'
SITENAME = u'bonsaichicken.org'
SITEURL = 'http://bonsaichicken.org'

FEED_DOMAIN = 'http://bonsaichicken.org'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = u'Stuff'
DATE_FORMAT = { 'en': '%d %m %Y' }

THEME = "./themes/livingston/"

#Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags.html')]

NUM_FULL_ARTICLES = 10

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "bonsaichicken"
TWITTER_USERNAME = 'bowyakka'
#LINKEDIN_URL = 'http://en.linkedin.com/in//en'
GITHUB_URL = 'http://github.com/GregBowyer'
GOOGLE_ANALYTICS = "UA-25131621-1"

STATIC_PATHS = ['images', 'CNAME']

MAIL_USERNAME = 'gbowyer'
MAIL_HOST = 'fastmail.co.uk'
