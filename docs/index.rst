==================
atsphinx-footnotes
==================

Overview
========

This is Sphinx extension to improve writing experience with footnotes.

It collects footnotes and renders last of document.

.. note:: Doc is good-example to use it.

Installation
============

Install from PyPI.

.. code-block:: console

   pip install atsphinx-footnotes

Usage
=====

Configure your ``conf.py`` and run build.

.. code-block:: python

   extensions = [
       # Other extensions ...
       "atsphinx.footnotes",
   ]

When you write footnotes internal document, generated html render footnotes on last of body. [#]_

.. hint::

   Please see document source.
   Footnotes of document are written nearby refs.

.. [#] If this is not used, every footnotes are rendered at same position of sources.

Configuration
=============

.. confval:: footnotes_rubric

   :Type: ``str | None``
   :Default: ``None``
   :Example: ``My footnotes``

   When this is not None values, extension uses it instead of "Footnotes".
