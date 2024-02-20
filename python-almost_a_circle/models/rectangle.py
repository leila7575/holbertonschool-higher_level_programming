#!/usr/bin/python3
"""This module contains the class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """This class defines a Rectangle
    and inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of class attributes.
        Attributes:
        width: private instance attribute
        height:private instance attribute
        x: private instance attribute
        y: private instance attribute
        id: inherited from Base class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of rectangle."""
        self.__width = value

    @property
    def height(self):
        """Retrieves height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle."""
        self.__height = value

    @property
    def x(self):
        """Retrieves x of rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x of rectangle."""
        self.__x = value

    @property
    def y(self):
        """Retrieves y of rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y of rectangle."""
        self.__y = value
