# coding: utf-8
"""
TESTS.

Execute in root dir: python -m unittest discover
"""

import os
import doctest
import unittest

modules = []
for r, ds, fs in os.walk('src'):
    # remove leading src, replace
    r_ = '.'.join(os.path.split(r)[1:])
    for f in fs:
        if f.endswith('.py') and f != '__init__.py':
            f = r_ + '.' + f.replace('.py', '')
            modules.append(f)


# load doctests
def load_tests(loader, tests, ignore):
    """
    Loads doctests for all specified modules.
    """
    for m in modules:
        tests.addTests(doctest.DocTestSuite(m))    
    return tests


class TestTemplate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # EXAMPLE
    def test_TEMPLATE(self):
        self.assertEqual((lambda: 0)(), 0, "Warning message")
