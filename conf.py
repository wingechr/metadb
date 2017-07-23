# coding=utf-8

import os
import sphinx_rtd_theme

project = "PROJECT_NAME"
description = "Small file meta data database"
package = "PACKAGE_NAME"
version = "0.1"
copyright = "PROJECT_COPYRIGHT"
url = "https://github.com/wingechr/metadb"
author = "Christian Winger"
author_email = "c@wingechr.de"
license = "GPLv3"
language = "en"

todo_include_todos = True
add_module_names = False
show_authors = True
html_show_sourcelink = False
html_show_sphinx = False
html_search_language = language
html_show_copyright = bool(copyright)
docs_path = 'docs'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {}
html_theme = "sphinx_rtd_theme"  # classic | bootstrap | alabaster | sphinx_rtd_theme
master_doc = 'index'
source_encoding = 'utf-8'
source_suffix = ['.rst', '.md']
pygments_style = 'sphinx'
html_logo = os.path.join(docs_path, '_static/logo.svg')
html_favicon = os.path.join(docs_path, '_static/favicon.ico')
templates_path = [os.path.join(docs_path, '_templates')]
exclude_dirs = []  # do not include in autodoc
nitpicky = True
html_use_index = True
add_function_parentheses = True
html_static_path = [os.path.join(docs_path, '_static')]
graphviz_output_format = 'svg'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',  # GRAPHVIZ: dot must be in PATH
    'sphinxcontrib.napoleon',  # requires sphinxcontrib-napoleon
]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True

# fix warnings about docstring referencing builtin types
nitpick_ignore = [
    ('py:obj', 'int'),
    ('py:obj', 'str'),
    ('py:obj', 'bool'),
    ('py:obj', 'optional')
]
