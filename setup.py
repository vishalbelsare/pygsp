#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup


setup(
    name = 'pygsp',
    version = '0.0.1',
    description = 'The official Graph Processing Toolbox',
    long_description = open('README.rst').read(),
    author = 'Michaël Defferrard (EPFL LTS2)',
    author_email = 'michael.defferrard@epfl.ch',
    url = 'https://github.com/epfl-lts2/',
    packages = ['pygsp', 'pygsp.tests'],
    test_suite = 'pygsp.tests.test_all.suite',
    install_requires = ['numpy', 'scipy', 'matplotlib'],
    requires = ['numpy'],
    license = "BSD",
    keywords = '',
    platforms = 'any',
    classifiers = [
        'Topic :: Scientific/Engineering :: Mathematics',
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)