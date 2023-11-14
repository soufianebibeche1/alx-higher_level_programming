#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):
    def setUp(self):
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_display_method(self):
        rectangle = Rectangle(3, 2)
        expected_output = '###\n###\n'
        rectangle.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
