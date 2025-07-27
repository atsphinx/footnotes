"""Powered footnotes extension for Sphinx."""

from __future__ import annotations

from typing import TYPE_CHECKING

from docutils import nodes
from sphinx.locale import _

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__version__ = "0.3.0"


def is_allowd_collect(app: Sphinx):
    builder = app.builder
    enabled_builders = app.config.footnotes_enabled_builders
    return builder.name in enabled_builders or builder.format in enabled_builders


def collect_footnotes(app: Sphinx, doctree: nodes.document, docname: str):
    """Collect and display later all footnotes."""
    if not is_allowd_collect(app):
        return
    footnotes = nodes.section()
    rubric = getattr(app.config, "footnotes_rubric", None)
    if rubric is None:
        rubric = _("Footnotes")
    for footnote in doctree.traverse(nodes.footnote):
        footnote.parent.remove(footnote)
        footnotes.append(footnote)
    if len(footnotes.children):
        footnotes.insert(0, nodes.rubric(text=rubric))
        doctree.append(footnotes)


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value("footnotes_rubric", None, "env", [str, None])
    app.add_config_value("footnotes_enabled_builders", ["html"], "env", [list])
    app.connect("doctree-resolved", collect_footnotes)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
