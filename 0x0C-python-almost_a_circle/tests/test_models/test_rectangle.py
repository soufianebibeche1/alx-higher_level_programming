#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_init(self):
        """Test initialization of Rectangle class."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

if __name__ == '__main__':
    unittest.main()
