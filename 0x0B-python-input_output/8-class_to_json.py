#!/usr/bin/python3
"""function returns dictionary representation
with simple data structure
"""


def class_to_json(obj):
    """takes object to return dict discription"""
    return obj.__dict__
