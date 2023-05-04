"""Powered footnotes extension for Sphinx."""
from docutils import nodes
from sphinx.application import Sphinx

__version__ = "0.1.0"


def collect_footnotes(app: Sphinx, doctree: nodes.document):
    """Collect and display later all footnotes."""
    footnotes = nodes.section()
    for footnote in doctree.traverse(nodes.footnote):
        footnote.parent.remove(footnote)
        footnotes.append(footnote)
    if len(footnotes.children):
        footnotes.insert(0, nodes.rubric(text="Footnotes"))
        doctree.append(footnotes)


def setup(app: Sphinx):  # noqa: D103
    app.connect("doctree-read", collect_footnotes)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
