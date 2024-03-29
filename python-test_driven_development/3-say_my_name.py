#!/usr/bin/python3
"""
This module contains the function say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>
        Args:
            first_name(str): first name
            lest_name(str): last name
        Raises:
            TypeError: first_name must be a string
            TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
