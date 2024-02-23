#!/usr/bin/python3
"""contains unittests for square."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_constructor(self):
        s = Square(2, 3, 4, 5)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 5)

    def test_size_validation(self):
        with self.assertRaises(TypeError):
            s = Square("not_an_integer", 2, 3, 4)
        with self.assertRaises(ValueError):
            s = Square(-1, 2, 3, 4)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            s = Square(1, "not_an_integer", 3, 4)
        with self.assertRaises(ValueError):
            s = Square(1, -2, 3, 4)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, "not_an_integer", 4)
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3, 4)

    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_display(self):
        s = Square(2)
        self.assertEqual(s.display(), None)

    def test_str(self):
        s = Square(2, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (5) 3/4 - 2")

    def test_update(self):
        s = Square(1, 1, 1, 1)
        s.update(2, 2, 2, 2)
        self.assertEqual(str(s), "[Square] (2) 2/2 - 2")

    def test_to_dictionary(self):
        s = Square(2, 3, 4, 5)
        self.assertEqual(s.to_dictionary(), {'id': 5, 'x': 3, 'size': 2, 'y': 4})


if __name__ == "__main__":
    unittest.main()
