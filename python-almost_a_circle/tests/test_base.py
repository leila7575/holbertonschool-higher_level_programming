#!/usr/bin/python3
"""contains unittests for base."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """testing instantiation of Base class."""
    def setUp(self):
        """Runs before each test method."""
        self.rect = Rectangle(1, 2, 3, 4, 5)
        self.square = Square(6, 7, 8, 9)

    def test_to_json_string(self):
        self.assertEqual(Rectangle.to_json_string(None), "[]")
        self.assertEqual(Rectangle.to_json_string([]), "[]")

    def test_from_json_string(self):
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string("[]"), [])

    def test_save_and_load_from_file(self):
        Rectangle.save_to_file([self.rect])
        Square.save_to_file([self.square])

        rectangles = Rectangle.load_from_file()
        squares = Square.load_from_file()

        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(rectangles[0].id, 5)
        self.assertEqual(rectangles[0].width, 1)
        self.assertEqual(rectangles[0].height, 2)
        self.assertEqual(rectangles[0].x, 3)
        self.assertEqual(rectangles[0].y, 4)

        self.assertEqual(squares[0].id, 9)
        self.assertEqual(squares[0].size, 6)
        self.assertEqual(squares[0].x, 7)
        self.assertEqual(squares[0].y, 8)

    def tearDown(self):
        """Runs after each test method."""
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
