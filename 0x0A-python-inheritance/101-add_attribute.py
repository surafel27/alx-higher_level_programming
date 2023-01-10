#!/usr/bin/python3
"""Function add_attribute
"""


def add_attribute(a_class, name, value):
    """Adds new attribute to an object if it's possible
    """

    if ('__dict__' in dir(a_class)):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")
