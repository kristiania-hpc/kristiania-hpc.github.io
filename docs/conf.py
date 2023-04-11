# Configuration file for the Sphinx documentation builder.

# -- Project information
import sphinx_theme


project = 'Kristiania-HPC'
copyright = '2023, SEIT, Kristiania University College'
author = 'Guru Prasad Bhandari'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]


html_theme = 'sphinx_rtd_theme'
# html_logo = 'images/logo.png'

html_theme_options = {
    'logo_only': False,
    'display_version': False
}