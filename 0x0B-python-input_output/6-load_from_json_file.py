#!/usr/bin/python3
"""function load json file """

import json


def load_from_json_file(filename):
    """filname is the object to be load"""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        return json.load(myFile)
