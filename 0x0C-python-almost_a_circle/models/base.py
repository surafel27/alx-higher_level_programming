#!/usr/bin/python3
"""
Module base
Defines class Base
with private class attribute
"""


import json


class Base:
    """
    Functions:
       __init__(self, id=None)
    __nb_objects : private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initilizes instance
        id : assigns if it is not None
        """
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representatioon to file"""
        objs = []
        if list_objs is not None:
            for obj in list_objs:
                objs.append(cls.to_dictionary(obj))
        name = cls.__name__ + ".json"
        with open(name, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """form json string to list of JSON string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        name = cls.__name__ + ".json"
        list_t = []
        try:
            with open(name, "r") as f:
                ins = cls.from_json_string(f.read())
            for i in ins:
                list_t.append(cls.create(**i))
            return list_t
        except FileNotFoundError:
            return list_t
