#!/usr/bin/env python3


import unittest


from mia.executive import ExecutiveClass
from mia.executive import _private_executive_function
from mia.executive import executive_function


class TestExecutive(unittest.TestCase):

    def test_executive_class_method(self):
        self.assertEqual(ExecutiveClass.method(), 0)

    def test__private_executive_function(self):
        self.assertEqual(_private_executive_function(), 0)

    def test_executive_function(self):
        self.assertEqual(executive_function(), 0)


if __name__ == '__main__':
    unittest.main()
