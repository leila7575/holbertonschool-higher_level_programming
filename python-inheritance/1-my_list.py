#!/usr/bin/python3
"""
This module contains the class MyList.
"""


class MyList(list):
    """class MyList that inherits from list with public istance method print_sorted"""
    def print_sorted(self):
        """Sorts the list in ascending order."""
        self.sort()
        print(self)
