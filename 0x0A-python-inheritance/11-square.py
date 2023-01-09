#!/usr/bin/python3
"""creating Square class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class define __init__() and area() """

    def __init__(self, size):
        """initializing the square class
        Arg:
            size: size of the rectangle
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return the area of size * size"""
        return self.__size * self.__size
    
    def __str__(self):
        """returns the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
