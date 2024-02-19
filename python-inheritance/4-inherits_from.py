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
    obj_class = type(obj)
    if obj_class == a_class:
        return False
    return issubclass(obj_class, a_class)
