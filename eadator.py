#!/usr/bin/env python
""" eadator
    try DTD and XSD validation for EAD2002, support EAD3 as well later
"""

import sys, os
import inspect
import argparse
from lxml import etree
from pprint import pprint as pp

def main(argv=None):

    # Info: http://stackoverflow.com/a/6098238/1763984
    # realpath() with make your script run, even if you symlink it :)
    cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))

    parser = argparse.ArgumentParser( description='EAD validator')
    parser.add_argument('eadfile', nargs=1, help="EAD XML file to check",
                        type=argparse.FileType('r'))
    parser.add_argument('--dtd', default="{0}/ents/ead.dtd".format(cmd_folder), required=False, )
    parser.add_argument('--xsd', default="{0}/ents/ead.xsd".format(cmd_folder), required=False, )

    if argv is None:
        argv = parser.parse_args()

    eadfile = etree.parse(argv.eadfile[0])

    ead2002ns = eadfile.xpath("//*[namespace-uri()='urn:isbn:1-931666-22-9']")

    if not ead2002ns:		# looks like DTD style
        dtd = etree.DTD(argv.dtd)
        if not dtd.validate(eadfile):
            pp(dtd.error_log)
            exit(1)
    else:			# looks like XSD style
        xsd = etree.XMLSchema(etree.parse(argv.xsd))
        if not xsd.validate(eadfile):
            pp(xsd.error_log)
            exit(1)

# main() idiom for importing into REPL for debugging 
if __name__ == "__main__":

    sys.exit(main())
