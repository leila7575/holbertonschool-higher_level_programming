#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2 ,3 ,4]), 4)
        self.assertEqual(max_integer([1, 2 ,3 ,5]), 5)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -5]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1,-2 ,3 ,-5]), 3)

    def test_single_elements(self):
        self.assertEqual(max_integer([5]), 5)


if __name__ == '__main__':
    unittest.main()
