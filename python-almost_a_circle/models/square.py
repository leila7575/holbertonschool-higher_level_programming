#!/usr/bin/python3
"""This module contains the class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a Square
    and inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of square instance..
        Attributes:
        size(int): size of square
        x(int): x-coordinate of square
        y(int): y-coordinate of square
        id(int): identifier of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves size of square."""
        return self.width

    @size.setter
    def size(self, value):
        """sets size of square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string representation of the square."""
        return (
            f"[Square] ({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.size}"
        )

    def update(self, *args, **kwargs):
        """Assign arguments to attributes."""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionnary representation of Square."""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y,
        }
