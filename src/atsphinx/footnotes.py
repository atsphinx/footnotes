"""Powered footnotes extension for Sphinx."""
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.locale import _

__version__ = "0.2.0"


def collect_footnotes(app: Sphinx, doctree: nodes.document):
    """Collect and display later all footnotes."""
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
    app.connect("doctree-read", collect_footnotes)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
