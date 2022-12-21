#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines:
    class Node with private instance attribute that has
    property retriver and setter
    class SinglyLinkedList with private instance attribute
"""


class Node:
    """
    Definition of Node
    Args:
        data(int) : memeber of the linked list
        next_node : pointes to the next node
    Functions:
        data(self)
        data(self, value)
        next_node(self)
        next_node(self, value)
    """
    def __init__(self, data, next_node=None):
        """
        Initilizes private attributes
        Attributes:
            data : memeber of the node
            next_node : points to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        property getter
        Returns:
            data(int): member of the list
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        property setter
        Args:
            value(int): integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        property getter
        Returns:
        value(Node): next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        property setter
        Args:
            value(Node): next node
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    definition of class SinglyLinkedList
    Args:
        head: private
    Functions:
        __init__(self)
        sorted_insert(self, value)
    """

    def __init__(self):
        """
        Initializes singly linked list
        Attributes:
           head: private
        """
        self.__head = None

    def __str__(self):
        """
        String representation of singly linked list
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        inserts a node in sorted list
        Args:
            value(Node): node to be inserted
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (new.data > tmp.data):
            prev = tmp
            tmp = tmp.next_node
        if new.data < tmp.data:
            prev.next_node = new
            new.next_node = tmp
            return
        new.next_node = tmp.next_node
        tmp.next_node = new
        return
