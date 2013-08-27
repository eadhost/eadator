# -*- coding: utf-8 -*-
import os, inspect
from eadator import eadator
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import argparse
from pprint import pprint as pp

class TestEadator(unittest.TestCase):
    def test_eadator(self):
        cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
        lib_folder = os.path.realpath(os.path.abspath(os.path.split(eadator.__file__)[0]))
        parser = argparse.ArgumentParser( description='EAD validator')
        parser.add_argument('eadfile', nargs=1, help="EAD XML file to check",
                            type=argparse.FileType('r'))
        parser.add_argument('--dtd', default="%s/ents/ead.dtd" % lib_folder, required=False, )
        parser.add_argument('--xsd', default="%s/ents/ead.xsd" % lib_folder, required=False, )

        # test valid instances
        eadator.main(parser.parse_args([os.path.join(cmd_folder,'test-dtd-valid.xml')]))
        eadator.main(parser.parse_args([os.path.join(cmd_folder,'test-xsd-valid.xml')]))
        eadator.validate(os.path.join(cmd_folder,'test-dtd-valid.xml'))
        eadator.validate(os.path.join(cmd_folder,'test-xsd-valid.xml'))

        # test invalid instances
        self.assertRaises(SystemExit, eadator.main, parser.parse_args([os.path.join(cmd_folder,'test-dtd-invalid.xml')]))
        self.assertRaises(SystemExit, eadator.main, parser.parse_args([os.path.join(cmd_folder,'test-dtd-invalid.xml')]))


if __name__ == '__main__':
    unittest.main()

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
