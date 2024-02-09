#!/usr/bin/python3
"""
This module contains the function text_indentation..
"""


def text_indentation(text):
    """prints a text with 2 new lines after characters ., ? and :
        Args:
            text(str): text to be printed
        Raises:
            TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
        else:
            line += char

    if line:
        print(line.strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
