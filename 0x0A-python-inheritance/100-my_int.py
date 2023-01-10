#!/usr/bin/python3
"""Defining a class that inherit int"""


class MyInt(int):
    """a class that compares and inverts the
    output using __eq__ and __ne__ method"""
    def __eq__(self, value):
        """return the equal
        Arg:
            value: the value to be checked
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """return the not equal
        Arg:
            value: the value to checked
        """
        return super().__eq__(value)
