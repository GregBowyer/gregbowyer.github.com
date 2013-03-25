#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Greg Bowyer'
SITENAME = u'bonsaichicken.org'
SITEURL = 'http://bonsaichicken.org'
FEED_DOMAIN = 'http://bonsaichicken.org'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = u'Stuff'
DATE_FORMAT = { 'en': '%d %m %Y' }

THEME = "./themes/livingston/"

#Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags.html'),
        ('Projects', 'pages/projects.html'),
        ('About', 'pages/about-me.html')]

NUM_FULL_ARTICLES = 10

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "bonsaichicken"
TWITTER_USERNAME = 'bowyakka'
#LINKEDIN_URL = 'http://en.linkedin.com/in//en'
GITHUB_URL = 'http://github.com/GregBowyer'
GOOGLE_ANALYTICS = "UA-25131621-1"
