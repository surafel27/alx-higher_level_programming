#!/usr/bin/python3
"""defining class RectangleExtends from class Base
"""


from models.base import Base


class Rectangle(Base):
    """defining __init__()
       defining width()
       defining height()
       defining x()
       defining y() as a public class attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """this method takes Arguments
            width(int): integer
            height(int): intger
            x(int): integer
            y(int): integer
            and id as a public attribute
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """defining a property to width"""
        return self.__width

    @width.setter
    def width(self, value):
        """defining a setter to width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """defining a property to height"""
        return self.__height

    @height.setter
    def height(self, value):
        """defining a setter to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """defining a property to x"""
        return self.__x

    @x.setter
    def x(self, value):
        """defining a setter to x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """defining a property to y"""
        return self.__y

    @y.setter
    def y(self, value):
        """defining a setter to y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """defining area which calc area"""
        return self.__width * self.__height

    def display(self):
        """defining display to print the # in terms of width and height"""
        print("\n".join("#" * self.__width for i in range(self.__height)))

    def __str__(self):
        """defining __str__ """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
               .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """defining update function to update the value of class attribute"""
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 2:
                    self.x = value
                else:
                    self.y = value
            else:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "width" in kwargs:
                    self.width = kwargs["width"]
                if "height" in kwargs:
                    self.height = kwargs["height"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]
