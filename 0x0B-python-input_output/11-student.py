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

    def to_json(self, attrs=None):
        """returns student attribute to JSON representation"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            emptyList = {}
            for elmnt in attrs:
                if type(elmnt) is not str:
                    return self.__dict__
                if elmnt in self.__dict__.keys():
                    emptyList[elmnt] = self.__dict__[elmnt]
        return emptyList

    def reload_from_json(self, json):
        """function reload from JSON"""

        for itm in json.keys():
            self.__dict__[itm] = json[itm]
