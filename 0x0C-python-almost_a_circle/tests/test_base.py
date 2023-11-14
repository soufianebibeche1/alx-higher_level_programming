#!/usr/bin/python3
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_rectangle_instance(self):
        rectangle_dict = {'id': 1, 'width': 10, 'height': 5}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertIsNotNone(rectangle_instance)
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 5)

    def test_create_square_instance(self):
        square_dict = {'id': 1, 'size': 5}
        square_instance = Square.create(**square_dict)
        self.assertIsNotNone(square_instance)
        self.assertEqual(square_instance.size, 5)

    def test_save_to_file(self):
        obj1 = Rectangle(id=1, width=2, height=3)
        obj2 = Square(id=2, size=4)
        Base.save_to_file([obj1, obj2])

        # Cleanup: Remove the created file
        try:
            os.remove('Rectangle.json')
            os.remove('Square.json')
        except FileNotFoundError:
            pass

    def test_to_json_string(self):
        obj = Base(id=1)
        with self.assertRaises(AttributeError):
            Base.to_json_string([obj.to_dictionary()])

if __name__ == '__main__':
    unittest.main()
