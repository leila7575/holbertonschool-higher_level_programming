#!/usr/bin/python3
"""
This module contains the function print_square.
"""


def print_square(size):
    """Prints square with the character #
        Args:
            size(int): size of the square
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
