"""Standard tests."""

import pytest
from docutils import nodes
from sphinx.testing.util import SphinxTestApp

from atsphinx import footnotes


@pytest.mark.sphinx("html", confoverrides={"extensions": []})
def test__colect_footnotes__func_only(app: SphinxTestApp):
    """Test for standard behavior of ``atsphinx.footnotes.collect_footnotes``."""
    app.builder.read_doc("index")
    doctree = app.env.get_doctree("index")
    assert len(list(doctree.findall(nodes.section))) == 3
    footnotes.collect_footnotes(app, doctree)
    assert len(list(doctree.findall(nodes.section))) == 4


@pytest.mark.sphinx("html")
def test__colect_footnotes__standard(app: SphinxTestApp):
    """Test behavior as extension with default setteings."""
    app.builder.read_doc("index")
    doctree = app.env.get_doctree("index")
    assert len(list(doctree.findall(nodes.section))) == 4


@pytest.mark.sphinx("html", confoverrides={"language": "ja"})
def test__colect_footnotes__i18n(app: SphinxTestApp):
    """Test for i18n translation."""
    app.builder.read_doc("index")
    doctree = app.env.get_doctree("index")
    footnotes.collect_footnotes(app, doctree)
    section = list(doctree.findall(nodes.section))[-1]
    assert section.children[0].astext() == "注記"


@pytest.mark.sphinx("html", confoverrides={"footnotes_rubric": "脚注"})
def test__colect_footnotes__custom(app: SphinxTestApp):
    """Test for i18n translation."""
    app.builder.read_doc("index")
    doctree = app.env.get_doctree("index")
    footnotes.collect_footnotes(app, doctree)
    section = list(doctree.findall(nodes.section))[-1]
    assert section.children[0].astext() == "脚注"
