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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
        for yy in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """defining __str__ """
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

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
                elif key == 3:
                    self.x = value
                else:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                        self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """return the dictionary representation"""
        dictnry = {}
        dictnry["id"] = self.id
        dictnry["width"] = self.width
        dictnry["height"] = self.height
        dictnry["x"] = self.x
        dictnry["y"] = self.y
        return dictnry
