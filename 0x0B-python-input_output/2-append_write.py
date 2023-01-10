#!/usr/bin/python3
"""function append string to file and return the length"""


def append_write(filename="", text=""):
    """accepts filename as str and append text in to it"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
        return len(text)
