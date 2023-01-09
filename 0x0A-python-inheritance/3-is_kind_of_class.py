#!/usr/bin/python3
"""defining a method is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class function
    Arg:
        obj: object as to be check
        a_class: an arg to check for type
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
