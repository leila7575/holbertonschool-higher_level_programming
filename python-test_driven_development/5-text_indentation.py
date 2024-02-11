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

    for char in ".?:":
        text = (char + "\n\n").join([line.strip(" ")for line in text.split(char)])

    print("{}".format(text), end=" ")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
