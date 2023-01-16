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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
