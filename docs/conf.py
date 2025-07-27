# noqa: D100
from atsphinx.footnotes import __version__

# -- Project information
project = "atsphinx-footnotes"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = __version__

# -- General configuration
extensions = [
    "atsphinx.footnotes",  # If you want to see default behavior, try comment out.
    "atsphinx.mini18n",
    "sphinx.ext.todo",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for i18n
language = "en"
gettext_compact = False
locale_dirs = ["_locales"]

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for extensions
# atsphinx.footnotes
footnotes_enabled_builders = ["html", "dirhtml", "mini18n-html", "mini18n-dirhtml"]
# atsphinx.mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_basepath = "/footnotes/"


def setup(app):  # noqa: D103
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
