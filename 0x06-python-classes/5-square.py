#!/usr/bin/python3
"""Defining a class called Square"""


class Square:
    """Represent a Square
    Attributes:
            __size (int): size of the Square
    """
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: the square of size
        """
        self.size = size

    @property
    def size(self):
        """These is property retiver
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """These is a setter of value to size
        Args:
             value(int): it is integer type
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """Intializes a method
        Args:
             self: size of the Square
        Return: square of the size
        """
        self = self.__size
        return (self ** 2)

    def my_print(self):
        """Print the the # as the number of
        self.__size"""
        if self.__size == 0:
            print()
        for x in range(self.__size):
            print("#" * self.__size)
