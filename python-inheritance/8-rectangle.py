#!/usr/bin/python3
"""
This module contains the class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle with width and height attributes.
    """
    def __init__(self, width, height):
        """Initialisation of the attributes of the class, width and height.

        Args:
        width(int): private instance attribute.
        height(int): private instance attribute.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
