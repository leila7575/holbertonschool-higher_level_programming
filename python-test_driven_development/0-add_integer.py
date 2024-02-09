#!/usr/bin/python3
"""
Module for add_integer method.

Provides a function that adds two integers.
"""



def add_integer(a, b=98):
    """adds two integers.
    Args:
        a: first integer
        b: second integer

    Raises:
        TypeError: a must be an integer or b must be an integer
    
    Returns:
        The addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
