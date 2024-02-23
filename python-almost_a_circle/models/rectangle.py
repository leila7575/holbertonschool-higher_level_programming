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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieves x of rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x of rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieves y of rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y of rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns rectangle area based on width and height.
        """
        return self.__height * self.__width

    def display(self):
        """Prints Rectangle instance with character #."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns string representation of the rectangle."""
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args):
        """Assign arguments to attributes."""
        attributes = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)
