#!/usr/bin/python3
"""
Module that contains inherits_from
taht checks if object is instance of a class
or of class that inherited from this class
"""


def inherits_from(obj, a_class):
    """returns True if object is instance of specified class
    or instance of class that inherited from the class
    False otherwise."""
    return type(obj) != a_class and issubclass(type(obj), a_class)
