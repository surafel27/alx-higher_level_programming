#!/usr/bin/python3
"""function writes striong to file"""


def write_file(filename="", text=""):
    """accepts filename as str and write text in to it"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
        return len(text)
