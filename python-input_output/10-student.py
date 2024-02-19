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
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of Student instance.
        """
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {
                    attr: getattr(self, attr)
                    for attr in attrs
                    if hasattr(self, attr)
            }
        return self.__dict__
