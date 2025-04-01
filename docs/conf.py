import os
import sys

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rr_docs'
copyright = '2023, Rapyuta Robotics'
author = 'Rapyuta Robotics'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.append(os.path.abspath("./_ext"))

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "logo_only": True,
    "collapse_navigation": False,
}
html_static_path = ['_static']
html_logo = "_static/rr-logo-vertical2022-1100px-transp.png"
html_favicon = "_static/favicon.ico"

# -- Custom CSS
def setup(app):
    app.add_css_file('css/custom.css')
