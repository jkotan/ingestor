# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
if os.path.isfile('conf.py'):
    sys.path.insert(0, os.path.abspath('..'))
# sys.path.insert(0, '/home/jkotan/ndts/scingestor/scingestor')


# -- Project information -----------------------------------------------------

project = 'SciCat Dataset Ingestor'
copyright = '2022, DESY, Jan Kotanski'
author = 'Jan Kotanski'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
# html_theme = 'bootstrap'
# html_theme = 'python_docs_theme'
# html_theme = 'bizstyle'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'

# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'scingestor', 'SciCat Dataset Ingestor Documentation',
     [u'Jan Kotanski'], 1),
    ('scicat_dataset_ingestor', 'scicat_dataset_ingestor',
     'Server daemon to ingest SciCat RawDatasets',
     [u'Jan Kotanski'], 1),
    ('scicat_dataset_ingest', 'scicat_dataset_ingest',
     'Reingestion script to upload SciCat RawDatasets',
     [u'Jan Kotanski'], 1),
]

autoclass_content = 'both'

# autodoc_default_flags = [
#     'members',
#     'undoc-members',
#     # 'private-members',
#     # 'special-members',
#     'inherited-members',
#     'show-inheritance',
#     # 'ignore-module-all',
#     # 'exclude-members'
# ]

intersphinx_mapping = {
    'https://docs.python.org/3/': None,
    'https://scipy.github.io/devdocs': None,
    'https://numpy.org/doc/stable/': None,
    # 'http://pytango.readthedocs.io/en/stable': None,
    # 'https://pni-libraries.github.io/python-pninexus/stable': None,
    'https://docs.h5py.org/en/stable': None,
    # 'https://pyqtgraph.readthedocs.io/en/latest': None,
    'https://pyzmq.readthedocs.io/en/stable': None,
    # 'https://docs.python-requests.org/en/master': None,
    # 'https://requests.readthedocs.io/en/master': None,
    'https://requests.readthedocs.io/en/latest': None,
    # 'https://doc.qt.io/qtforpython/': None,
    # 'https://www.silx.org/doc/fabio/latest/': None,
    # 'https://pillow.readthedocs.io/en/stable/': None,
    # 'https://pyfai.readthedocs.io/en/master/': None,
}
