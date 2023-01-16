#!/usr/bin/python3
"""defining class square tha inherits from rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square deine class constarctoor
        __init__ with size z y and id attribute
    """
    def __init__(self, size, x=0, y=0, id=None):
        """class attribute that inherits from class Rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """define a property size"""
        return self.height

    @size.setter
    def size(self, value):
        """define a setter to size"""
        self.width = value
        self.height = value

    def __str__(self):
        """prints the property of square"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.height))

    def update(self, *args, **kwargs):
        """assignes attribute"""
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.size = value
                elif key == 2:
                    self.x = value
                else:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return the dictinary representation"""
        dictnry = {}
        dictnry["id"] = self.id
        dictnry["size"] = self.size
        dictnry["x"] = self.x
        dictnry["y"] = self.y
        return dictnry
