#!/usr/bin/python3
"""
Module 1-rectangle
Defines class Rectangle
with private attribute property and setter
"""


class Rectangle:
    """
    contains private instance width and height
    """
    def __init__(self, width=0, height=0):
        """
        initilizes width and height
        Args:
          width : width of the rectangle
          height : height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        return the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        Arg:
         value: the size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        Arg:
          value: the size
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
