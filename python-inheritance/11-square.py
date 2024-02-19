#!/usr/bin/python3
"""
This module contains the class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square with size attributes.
    """
    def __init__(self, size):
        """Initialisation of the attributes of the class, size.

        Args:
        size(int): private instance attribute.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns square area"""
        return self.__size ** 2

    def __str__(self):
        """returns string represetation of rectangle object.        """
        return "[Square] {}/{}".format(self.__size, self.__size)
