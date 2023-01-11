#!/usr/bin/python3
"""
Module 100-append_after
Define append_after
searchs for a string and adds a text
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line in a text file"""
    with open(filename, mode="r+") as f:
        text = ""
        for line in f:
            text += line
            if search_string in line:
                text += new_string
        f.seek(0)
        f.write(text)
