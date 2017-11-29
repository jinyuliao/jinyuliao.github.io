# -*- coding: utf-8 -*-

# flake8: noqa

import tinkerer
import tinkerer.paths
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx.util import compat
compat.make_admonition = BaseAdmonition

# **************************************************************
# TODO: Edit the lines below
# **************************************************************

# Change this to the name of your blog
project = "Jinyu Liao's Blog"

# Change this to the tagline of your blog
tagline = ''

# Change this to the description of your blog
description = ''

# Change this to your name
author = 'Jinyu Liao'

# Change this to your copyright string
copyright = '2017, ' + author

# Change this to your blog root URL (required for RSS feed)
website = 'https://jinyuliao.github.io/blog/html'

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = "jinyuliao"

# Change your favicon (new favicon goes in _static directory)
html_favicon = '_static/tinkerer.ico'

# Pick another Tinkerer theme or use your own
html_theme = 'tinkerer_rtd'

# Theme-specific options, see docs
html_theme_options = {}

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = None

# Generate full posts for RSS feed even when using "read more"
rss_generate_full_posts = False

# Number of blog posts per page
posts_per_page = 10

# Character use to replace non-alphanumeric characters in slug
slug_word_separator = '_'

# Set to page under /pages (eg. "about" for "pages/about.html")
landing_page = None

# Set to override the default name of the first page ("Home")
first_page_title = None

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Add other Sphinx extensions here
extensions = ['tinkerer.ext.blog', 'tinkerer.ext.disqus', 'sphinxcontrib.fancybox', 'sphinxcontrib.images']

# Add other template paths here
templates_path = ['_templates']

# Add other static paths here
html_static_path = ['_static', tinkerer.paths.static]

# Add other theme paths here
html_theme_path = ['_themes', tinkerer.paths.themes]

# Add file patterns to exclude from build
exclude_patterns = ['drafts/*', '_templates/*']

# Add templates to be rendered in sidebar here
html_sidebars = {
    '**': ['recent.html', 'categories.html', 'tags.html', 'searchbox.html']
}

# Add an index to the HTML documents.
html_use_index = False

# **************************************************************
# Do not modify below lines as the values are required by
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_show_sourcelink = False
html_add_permalinks = ''

fancybox_thumbnail_width = "800"
