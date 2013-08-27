#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" eadator
    try DTD and XSD validation for EAD2002, support EAD3 as well later
"""

import sys, os
import inspect
import argparse
from lxml import etree
from pprint import pprint as pp

def main(argv=None):
    parser = argparse.ArgumentParser( description='EAD validator')
    parser.add_argument('eadfile', nargs=1, help="EAD XML file to check",
                        type=argparse.FileType('r'))
    parser.add_argument('--dtd', required=False, )
    parser.add_argument('--xsd', required=False, )

    if argv is None:
        argv = parser.parse_args()

    message, valid = validate(argv.eadfile[0], argv.dtd, argv.xsd)

    if not valid:
        pp(message)
        exit(1)
    
def validate(eadfile, dtd=None, xsd=None):
    # Info: http://stackoverflow.com/a/6098238/1763984
    # realpath() with make your script run, even if you symlink it :)
    cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))

    eadfile = etree.parse(eadfile)

    ead2002ns = eadfile.xpath("//*[namespace-uri()='urn:isbn:1-931666-22-9']")

    validator = None

    if not dtd:
        dtd = "%s/ents/ead.dtd" % cmd_folder
    if not xsd:
        xsd = "%s/ents/ead.xsd" % cmd_folder

    if not ead2002ns:		# looks like DTD style
        validator = etree.DTD(dtd)
    else:			# looks like XSD style
        validator = etree.XMLSchema(etree.parse(xsd))

    message = None
    valid = validator.validate(eadfile)

    if not valid:
        message = validator.error_log

    return message, valid
    

# main() idiom for importing into REPL for debugging 
if __name__ == "__main__":

    sys.exit(main())

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
