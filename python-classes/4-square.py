#!/usr/bin/python3
class Square():
    """This class defines a square, with size and position attribute."""
    def __init__(self, size=0):
        """Initialisation of the attributes of the class.

        Args:
            size(int): private instance attribute, size of the square.
        """
        self.size = size
    @property
    def size(self):
        """Retrieves size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square.

        Args:
            value(int): size of square.

        Raises:
            TypeError: size must be an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns square area based on size.

        Returns:
            square area(int)
        """
        return int(self.__size) ** 2
