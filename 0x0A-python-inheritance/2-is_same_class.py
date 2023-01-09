#!/usr/bin/python3
"""Defining the method
"""


def is_same_class(obj, a_class):
    """is_same_class: method
    Arg:
       obj: object to ckeck
       a_class: the type to check
    """

    if type(obj) is a_class:
        return True
    else:
        return False
