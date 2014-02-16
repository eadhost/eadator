# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name = "eadator",
    version = "0.3.3",
    packages = find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['lxml', 'argparse'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        'eadator': ['ents/*.dtd', 'ents/*.xsd', 'ents/*.xml', 'ents/*.ent', 'ents/*.dcl' ],
    },
    zip_safe = False,

    # metadata for upload to PyPI
    author = "Brian Tingle",
    author_email = "brian.tingle.cdlib.org@gmail.com",
    description = "EAD2002 (DTD or XSD) universal validator",
    license = "BSD",
    keywords = "validate ead 2002 xml xsd dtd",
    url = "https://github.com/eadhost/eadator",   # project home page, if any
    download_url = "https://github.com/eadhost/eadator/tarball/0.3.3",
    # could also include long_description, download_url, classifiers, etc.
    entry_points = {
        'console_scripts': [
            'eadator = eadator.eadator:main',
        ]
    },
    test_suite = "tests.test_eadator"
)

# Copyright © 2013, Regents of the University of California
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# - Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# - Neither the name of the University of California nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
