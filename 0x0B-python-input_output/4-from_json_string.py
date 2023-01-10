#!/usr/bin/python3
"""fuction return json representation of str"""

import json


def from_json_string(my_obj):
    """takes the object and encode to json string"""
    my_obj = json.loads(my_obj)
    return my_obj
