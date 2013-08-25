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
        parser.add_argument('--dtd', default="{0}/ents/ead.dtd".format(lib_folder), required=False, )
        parser.add_argument('--xsd', default="{0}/ents/ead.xsd".format(lib_folder), required=False, )

        # test valid instances
        eadator.main(parser.parse_args([os.path.join(cmd_folder,'test-dtd-valid.xml')]))
        eadator.main(parser.parse_args([os.path.join(cmd_folder,'test-xsd-valid.xml')]))

        # test invalid instances
        self.assertRaises(SystemExit, eadator.main, parser.parse_args([os.path.join(cmd_folder,'test-dtd-invalid.xml')]))
        self.assertRaises(SystemExit, eadator.main, parser.parse_args([os.path.join(cmd_folder,'test-dtd-invalid.xml')]))


if __name__ == '__main__':
    unittest.main()
