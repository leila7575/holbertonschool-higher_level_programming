#!/usr/bin/python3
"""This module contains the function from_json_string"""


def from_json_string(my_str):
    """eturns an object represented by a JSON string"""
    import json
    return json.loads(my_str)
