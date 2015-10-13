# coding=utf-8
"""Sphinx documentation generator configuration file.

The full set of configuration options is listed on the Sphinx website:
http://sphinx-doc.org/config.html

"""
from __future__ import unicode_literals

import sys
import os
from packaging.version import Version


# Add the Pulp Smash root directory to the system path. This allows references
# such as :mod:`pulp_smash.whatever` to be processed correctly.
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir
))
sys.path.insert(0, ROOT_DIR)

# Parse the version according to PEP 440. An InvalidVersion exception is raised
# if the version is non-conformant, so the act of generating documentation
# serves as a unit test for the contents of the `VERSION` file.
with open(os.path.join(ROOT_DIR, 'VERSION')) as handle:
    VERSION = Version(handle.read().strip())


# pylint:disable=invalid-name
# Project Information ---------------------------------------------------------

project = 'Pulp Smash'
copyright = '2015, Jeremy Audet'  # pylint:disable=redefined-builtin
version = VERSION.base_version  # e.g. '1.2'
release = type('')(VERSION)  # e.g. '1.2a3.dev4'


# General Configuration -------------------------------------------------------

extensions = ['sphinx.ext.autodoc']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
nitpicky = True
autodoc_default_flags = ['members']


# Format-Specific Options -----------------------------------------------------

htmlhelp_basename = 'PulpSmashdoc'
latex_documents = [(
    master_doc,
    project + '.tex',
    project + ' Documentation',
    'Jeremy Audet',
    'manual'
)]
man_pages = [(
    master_doc,
    project.lower(),
    project + ' Documentation',
    ['Jeremy Audet'],
    1  # man pages section
)]
texinfo_documents = [(
    master_doc,
    project,
    project + ' Documentation',
    'Jeremy Audet',
    project,
    ('Pulp Smash is a GPL-licensed Python library that facilitates easy '
     'testing of Pulp.'),
    'Miscellaneous'
)]