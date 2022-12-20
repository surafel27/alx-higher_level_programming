#!/usr/bin/python3
"""Defining a class called Square"""


class Square:
    """Represent a Square
    Attributes:
            __size (int): size of the Square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: the square of size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
