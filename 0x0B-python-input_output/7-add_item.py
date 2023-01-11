#!/usr/bin/python3
"""function load, add , save json file"""

from sys import argv
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        loadFile = load_from_json_file(filename)
    except FileNotFoundError:
        loadFile = []

    save_to_json_file(loadFile + argv[1:], filename)
