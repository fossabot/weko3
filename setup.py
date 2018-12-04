# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 NII.
#
# WEKO3 is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""WEKO3"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

INVENIO_VERSION = "3.1.0.dev20181106"

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('weko3', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='weko3',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='weko3 Invenio',
    license='MIT',
    author='NII',
    author_email='weko-dev@nii.ac.jp',
    url='https://github.com/mhaya/weko3',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'weko3 = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'flask_debugtoolbar = flask_debugtoolbar:DebugToolbarExtension',
        ],
        'invenio_base.blueprints': [
            'weko3 = weko3.views:blueprint',
        ],
        'invenio_config.module': [
            'weko3 = weko3.config',
        ],
        'invenio_i18n.translations': [
            'messages = weko3',
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
