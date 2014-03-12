#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

import wtforms_morefields
import os
import sys


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()
                        if not (i.startswith("http") or i.startswith('#'))]

dependency_links = [i.strip() for i in open("requirements.txt").readlines()
                            if i.startswith("http")]

classifiers = [
    "Development Status :: 3 - Alpha",
    "Environment :: Web Environment",
    "Framework :: Flask",
    "Intended Audience :: Developers",
    "License :: All rights reserved.",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 2.7",
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

try:
    long_description = open('README.md').read()
except:
    long_description = "Custom fields for the WTForms library."

setup(name='wtforms_morefields',
      version=wtforms_morefields.__version__,
      description=wtforms_morefields.__description__,
      long_description=long_description,
      classifiers=classifiers,
      keywords='flask wtforms',
      packages=find_packages(exclude=('doc', 'docs',)),
      package_dir={'wtforms_morefields': 'wtforms_morefields'},
      zip_safe=True,
      install_requires=REQUIREMENTS,
      dependency_links=dependency_links,
      include_package_data=True,
      test_suite='nose.collector',
      entry_points={
        'console_scripts': [
         ]
      })
