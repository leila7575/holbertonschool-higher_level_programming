#!/usr/bin/python3
"""
This module contains the class Rectangle.
"""


class Rectangle():
    """
    This class defines a rectangle class with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initialisation of the attributes of the class
        initializes rectangle with width and height.

        Args:
            width(int): private instance attribute, width of the rectangle.
            height (int): private instance attribute,height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves width of square."""
        return self.__width

    @property
    def height(self):
        """Retrieves height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of rectangle.

        Args:
            value(int): height of rectangle.

        Raises:
            TypeError: height must be an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Retrieves width of square."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of square.

        Args:
            value(int): width of square.

        Raises:
            TypeError: width must be an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
