"""Standard tests."""
from io import StringIO

import pytest
from docutils import nodes
from sphinx.testing.util import SphinxTestApp

from atsphinx import footnotes


@pytest.mark.sphinx("html")
def test__colect_footnotes__standard(
    app: SphinxTestApp, status: StringIO, warning: StringIO
):
    """Test for standard behavior of ``atsphinx.footnotes.collect_footnotes``."""
    app.builder.read_doc("index")
    doctree = app.env.get_doctree("index")
    assert len(list(doctree.findall(nodes.section))) == 3
    footnotes.collect_footnotes(app, doctree)
    assert len(list(doctree.findall(nodes.section))) == 4
