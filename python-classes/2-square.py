#!/usr/bin/python3
"""
This module contains the class Square.
"""


class Square():
    """This class defines a square, with size attribute."""

    def __init__(self, size=0):
        """
        Initialisation of the attributes of the class,
        initializes square with size.

        Args:
            size(int): private instance attribute, size of the square.
        Raises:
            TypeError: size must be an integer.
            ValueError: if size is less than 0.

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
