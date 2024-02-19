#!/usr/bin/python3
"""This module contains the class Base."""


class Base():
    """This class will be the base of all other classes.
    Attributes:
        __nb_objects: private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation of the attributes of the class.
        Attributes:
            id: public instance attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
