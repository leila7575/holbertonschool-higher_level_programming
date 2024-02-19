#!/usr/bin/python3
"""
This module contains the class Student.
"""


class Student():
    """
    This class defines a student.
    Attributes:
        first_name: public instance attribute,
        last_name: public instance attribute
        age: public instance attribute
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialisation of the attributes of the class
        initializes Student with first_name, last_name and age.
        """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of Student instance.
        """
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
