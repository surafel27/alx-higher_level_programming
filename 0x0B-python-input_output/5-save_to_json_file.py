#!/usr/bin/python3
"""fuction return json representation of str"""

import json


def save_to_json_file(my_obj, filename):
    """takes the object and write to json string"""
    with open(filename, mode="w", encoding="utf-8") as myFile
    my_obj = json.dump(my_obj)
    myFile.write(my_obj)
