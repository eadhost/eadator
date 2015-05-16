#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" eadator
    try DTD and XSD validation for EAD2002, RNG for EAD3
"""
import inspect
import os
import sys
from collections import namedtuple
from pprint import pprint as pp

import argparse
from lxml import etree


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='EAD validator'
    )
    parser.add_argument(
        'eadfile',
        nargs=1,
        help="EAD XML file to check",
        type=argparse.FileType('r')
    )
    parser.add_argument(
        '--dtd',
        required=False,
        help='use alternate EAD2002 DTD',
    )
    parser.add_argument(
        '--xsd',
        required=False,
        help='use alternate EAD2002 XSD',
    )
    parser.add_argument(
        '--rng',
        required=False,
        help='use alternate EAD3 RelaxNG schema',
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='report ead type and total count of errors',
    )

    if argv is None:
        argv = parser.parse_args()

    result = validate(argv.eadfile[0], argv.dtd, argv.xsd, argv.rng)

    if result.error_count:
        pp(result.error_log)

    if argv.verbose:
        print('Type: {1}, Error count: {0}'.format(
            result.error_count,
            result.validated_by
        ))

    if result.error_count:
        exit(1)


def validate(eadfile, dtd=None, xsd=None, rng=None):
    # named tuple to hold results
    ValidationResults = namedtuple(
        'ValidationResults',
        'validated_by error_count error_log',
    )

    # Info: http://stackoverflow.com/a/6098238/1763984
    # realpath() with make your script run, even if you symlink it :)
    cmd_folder = os.path.realpath(
        os.path.abspath(
            os.path.split(
                inspect.getfile(inspect.currentframe())
            )[0]
        )
    )
    # specify alternative schema files
    if not dtd:
        dtd = "%s/ents/ead.dtd" % cmd_folder
    if not xsd:
        xsd = "%s/ents/ead.xsd" % cmd_folder
    if not rng:
        rng = "%s/ents/ead3.rng" % cmd_folder

    # if it is XML, that's a good start
    eadfile = etree.parse(eadfile)

    # sniff out any xmlns'es
    ead2002ns = eadfile.xpath(
        "//*[namespace-uri()='urn:isbn:1-931666-22-9']"
    )
    ead3ns = eadfile.xpath(
        "//*[namespace-uri()='http://ead3.archivists.org/schema/']"
    )

    # pick the correct validator
    if ead3ns:
        validator = etree.RelaxNG(etree.parse(rng))
        ead_type = 'EAD3'
    elif ead2002ns:
        validator = etree.XMLSchema(etree.parse(xsd))
        ead_type = 'EAD2002-XSD'
    else:
        validator = etree.DTD(dtd)
        ead_type = 'EAD2002-DTD'

    valid = validator.validate(eadfile)

    if valid:
        return ValidationResults(
            validated_by=ead_type,
            error_count=0,
            error_log=None
        )
    else:
        return ValidationResults(
            validated_by=ead_type,
            error_count=len(validator.error_log),
            error_log=validator.error_log
        )


# main() idiom for importing into REPL for debugging
if __name__ == "__main__":
    sys.exit(main())


# Copyright © 2015, Regents of the University of California
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
