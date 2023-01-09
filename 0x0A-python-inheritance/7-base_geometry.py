#!/usr/bin/python3
"""defining BaseGeometry"""


class BaseGeometry:
    """defining method area(), integer_validator()
    """
    def area(self):
        """ raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check for intger
        Arg:
            name: name
            value: the value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
