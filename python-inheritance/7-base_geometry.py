#!/usr/bin/python3
"""
This module contains the class BaseGeometry.
"""


class BaseGeometry:
    """class BaseGeometry with method area to be implemented
    and method integer_validator that validates value.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is a positive integer.

        Args:
            name(str)
            value(int)

        Raises:
            TypeError:<name> must be an integer
            ValueError: <name> must be greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
