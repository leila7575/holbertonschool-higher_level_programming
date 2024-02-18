#!/usr/bin/python3
"""This module contains the function append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
