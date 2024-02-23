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
        self.rect1 = Rectangle(1, 2, 3, 4)
        self.rect1 = Rectangle(5, 6, 7, 8)
        self.square1 = Square(6, 7, 8)
        self.square1 = Square(9, 10, 11)

    def test_to_json_string(self):
        self.assertEqual(Rectangle.to_json_string(None), "[]")
        self.assertEqual(Rectangle.to_json_string([]), "[]")

    def test_from_json_string(self):
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string("[]"), [])

    def test_save_and_load_from_file(self):
        Rectangle.save_to_file([self.rect1, self.rect2])
        Square.save_to_file([self.square1, self.square2])

        rectangles = Rectangle.load_from_file()
        squares = Square.load_from_file()

        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[1].id, 2)

        self.assertEqual(squares[0].id, 3)
        self.assertEqual(squares[1].id, 4)

        new_rect = Rectangle(3, 4, 5, 6)
        new_square = Square(7, 8, 9)

        Rectangle.save_to_file([new_rect])
        Square.save_to_file([new_square])

        new_rectangles = Rectangle.load_from_file()
        new_squares = Square.load_from_file()

        self.assertEqual(new_rectangles[0].id, 3)
        self.assertEqual(new_squares[0].id, 5)

    def tearDown(self):
        """Runs after each test method."""
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
