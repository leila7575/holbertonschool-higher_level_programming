#!/usr/bin/python3
class Square():
    """This class defines a square class with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialisation of the attributes of the class, initializes square with size and position.

        Args:
            size(int): private instance attribute, size of the square.
            position (tuple): private instance attribute, position in square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves position in square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position in  square.

        Args:
            value(tuple): position of square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers.
        """

        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    
    def area(self):
        """Returns square area based on size.

        Returns:
            square area(int)
        """
        return int(self.__size) ** 2

    def my_print(self):
        """prints in stdout the square with the character # based on size and position."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
