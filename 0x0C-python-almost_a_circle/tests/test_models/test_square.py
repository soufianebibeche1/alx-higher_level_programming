#!/usr/bin/python3
"""Unit tests for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_init(self):
        """Test initialization of Square class."""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)

        s2 = Square(10, 2, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 1)

        s3 = Square(3, 1, 3, 12)
        self.assertEqual(s3.id, 12)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)

if __name__ == '__main__':
    unittest.main()
