#!/usr/bin/python3
"""defining a method """


def inherits_from(obj, a_class):
    """inherits_from checks for inheritance
    Arg:
       obj: argument to be checked
       a_class: type to checked
    """
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
