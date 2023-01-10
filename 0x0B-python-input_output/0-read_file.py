#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """function read from a file"""
    with open(filename, encoding="UTF-8") as myFile:
        print(myFile.read())
