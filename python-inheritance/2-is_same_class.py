#!/usr/bin/python3
"""
Module that contains is_same_class
checks if object is instance of specified class.
"""


def is_same_class(obj, a_class):
    """returns True if object is instance of specified class
    False otherwise."""
    return type(obj) is a_class
