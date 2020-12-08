# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

import pprint
import sys

class TestSimple(unittest.TestCase):
    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
