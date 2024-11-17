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
copyright = "2024-present, codeofandrin"
author = "codeofandrin"

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
        "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/codeofandrin/apininjas.py",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

html_static_path = ["_static"]
html_css_files = [f"styles/{file}" for file in os.listdir("_static/styles")]
html_js_files = [f"scripts/{file}" for file in os.listdir("_static/scripts")]

html_title = "apininjas.py"
html_logo = "_static/assets/apininjaspy_logo.png"
html_favicon = html_logo
