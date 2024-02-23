#!/usr/bin/python3
"""This module contains the class Base."""
from json import dumps, loads


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """"converts json string to a list of dictionaries."""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy_instance = Rectangle(1, 1)
        elif cls is Square:
            dummy_instance = Square(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_data)
        return [cls.create(**dict_obj) for dict_obj in list_dicts]
