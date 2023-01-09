#!/usr/bin/python3
"""inheritance"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectnagle class must initialise
    """
    def __init__(self, width, height):
        """this initalize
        Arg:
           width: argument width
           height: argument height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
