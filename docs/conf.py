# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import datetime

import pkg_resources

release = pkg_resources.get_distribution("svmpsp-graphnetviz").version
project = f"svmpsp-graphnetviz-{release}"
copyright = f"{datetime.datetime.utcnow().year}, Sivam Pasupathipillai <sivam.pasupathipillai@gmail.com>"
author = "Sivam Pasupathipillai <sivam.pasupathipillai@gmail.com>"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
