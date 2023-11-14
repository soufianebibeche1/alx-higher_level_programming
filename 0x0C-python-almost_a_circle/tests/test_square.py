#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_square_instance_creation(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_size_property(self):
        square = Square(3)
        square.size = 5
        self.assertEqual(square.size, 5)

    def test_update_method(self):
        square = Square(1)
        square.update(2, 2, 2, 2)
        self.assertEqual(square.to_dictionary(), {'id': 2, 'size': 2, 'x': 2, 'y': 2})

    def test_to_dictionary_method(self):
        square = Square(4, 1, 2, 3)
        self.assertEqual(square.to_dictionary(), {'id': 3, 'size': 4, 'x': 1, 'y': 2})

if __name__ == '__main__':
    unittest.main()
