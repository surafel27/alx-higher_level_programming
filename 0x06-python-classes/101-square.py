#!/usr/bin/python3
"""
Module 6-square
Defines a class Square with private instance atribute,
public instance method, can access and update size, and
can also print square with #
"""


class Square:
    """
    Definition of class square with private instance,
    and public
    Args:
        size : size of the
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initilizes a square with size that has a defualt value of 0
        Attributes:
            size(int) : size of the
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        This function is used to retrieve
        Returns:
             size(int) : size of the
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This function is used to set a
        Args:
            Value(int): size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        this function is used to retrive
        Returns:
            position(tuple): new tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method sets the position
        Args:
          Value(tuple): the new position
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        This method calculates area of the
        Returns:
           area(int) : the current square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        if size is 0 prints empty
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """
        String representation of square so call to print works
        Example: print(my_square)
        """
        string = ""
        if self.__size == 0:
            return string

        string += "\n" * self.position[1]
        for i in range(self.__size):
            string += (" " * self.__position[0]) + ("#" * self.__size)
            if i != self.__size - 1:
                string += "\n"
        return string
