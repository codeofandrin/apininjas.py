# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("extensions"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "apininjas.py"
copyright = "2024-present, Puncher1"
author = "Puncher1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "attributetable",
    "exception_hierarchy",
]

autodoc_member_order = "bysource"
autodoc_typehints = "none"

# Links used for cross-referencing stuff in other documentation
intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "aio": ("https://docs.aiohttp.org/en/stable/", None),
}

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |coroutine_link| replace:: coroutine
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

# templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_experimental_html5_writer = True

furo_css_variables = {
    "icon-pencil": "var(--icon-info)",
    "color-brand-content": "var(--brand-content)",
    "color-foreground-primary": "var(--foreground-primary)",
    "color-api-overall": "var(--color-foreground-primary)",
    "color-api-name": "var(--color-foreground-primary)",
    "color-api-pre-name": "var(--color-foreground-primary)",
    "color-api-keyword": "var(--color-foreground-primary)",
    "color-api-background": "var(--api-background)",
    "color-link--visited": "var(--color-brand-content)",
    "color-link--visited--hover": "var(--color-brand-content)",
    "color-highlight-on-target": "var(--highlight-on-target-background)",
    "color-toc-item-text--active": "var(--color-toc-item-text)",
    "toc-font-size": "var(--font-size--small)",
}

html_theme = "furo"
html_theme_options = {
    "dark_css_variables": {k: v for k, v in furo_css_variables.items()},
    "light_css_variables": {k: v for k, v in furo_css_variables.items()},
}

html_static_path = ["_static"]
html_css_files = [f"styles/{file}" for file in os.listdir("_static/styles")]
html_js_files = [f"scripts/{file}" for file in os.listdir("_static/scripts")]
