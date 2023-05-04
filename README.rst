==================
atsphinx-footnotes
==================

Powered footnote tools for Sphinx.

Example
=======

When using standard reST, you must write footnotes into last of source to render into last of document.

.. code:: rst

   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. [#]_

   The quick brown fox jumps over the lazy dog [#]_

   .. [#] This is first sentence of "Lorem ipusum"
   .. [#] This is one of pangram.

When you use this extension, you can write footnotes nearby refer contents.

.. code:: rst

   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. [#]_

   .. [#] This is first sentence of "Lorem ipusum"

   The quick brown fox jumps over the lazy dog [#]_

   .. [#] This is one of pangram.

Getting started
===============

(TBD)
