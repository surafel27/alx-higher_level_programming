#!/usr/bin/python3
"""class student that defines students name age"""


class Student:
    """student class have a public instance of age, f_name and l_lane
    """
    def __init__(self, first_name, last_name, age):
        """initializing the student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns student attribute to JSON representation"""
        return self.__dict__
