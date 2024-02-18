#!/usr/bin/python3
"""This module contains class_to_json
that returns the dictionary description for JSON serialization of an object
"""


def class_to_json(obj):
    """
    function that returns the dictionary description
    for JSON serialization of an object.
    """
    return obj.__dict__
