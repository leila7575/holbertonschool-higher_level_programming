#!/usr/bin/python3
"""contains unittests for rectangle."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle("not_an_integer", 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4, 5)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "not_an_integer", 3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4, 5)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "not_an_integer", 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4, 5)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "not_an_integer", 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4, 5)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.display(), None)  # Cannot check output directly

    def test_str(self):
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 2/3")

    def test_update(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_to_dictionary(self):
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.to_dictionary(), {'x': 4, 'y': 5, 'id': 6, 'height': 3, 'width': 2})


if __name__ == "__main__":
    unittest.main()
