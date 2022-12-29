#!/usr/bin/python3
"""
  add_integer:
       checks if the argument is integer
       Return the sum of the two arguments
"""


def add_integer(a, b=98):
    """
    checks if int, otherwise return sum
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
