#!/usr/bin/python3
"""
This module contains the class Square.
"""


class Square():
    """This class defines a square.
    """
    def __init__(self, size=0):
        """Initialisation of the attributes of the class.

        Args:
            size(int): private instance attribute, size of square
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

    def area(self):
        """Returns square area based on size.

        Returns:
            square area(int)
        """
        return int(self.__size) ** 2
