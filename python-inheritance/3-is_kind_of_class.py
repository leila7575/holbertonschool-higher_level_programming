#!/usr/bin/python3
"""
Module that contains is_kind_of_clas
checks if object is instance of a class
or of class that inherited from this class
"""


def is_kind_of_class(obj, a_class):
    """returns True if object is instance of specified class
    or instance of class that inherited from the class
    False otherwise."""
    return isinstance(obj, a_class)
