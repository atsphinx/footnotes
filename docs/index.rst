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

.. todo:: Update after upload to PyPI.

Currently, this is not uploaded to PyPI.
You can install from GitHub directly to use it. [#]_

.. code-block:: console

   pip install git+https://github.com/atsphinx/footnotes#main

.. [#] If you try latest version, change branch from ``#main`` to ``#BRANCH_NAME``.

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

.. todo:: TBD

   I am plannging some config values.
