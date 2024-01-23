#!/usr/bin/python3
"""Define class for singlt-linked-list."""


class Node:
    """
    This is the Node class for a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.
        Parameters:
            data: The data of the node (must be an integer).
            next_node: The next node in the list (must be a Node or None).
        Raises:
            TypeError: If data is not an integer or next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Gets the current data of the node.
        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.
        Parameters:
            value: The data to set.
        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Gets the next node in the list.
        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the list.
        Parameters:
            value: The next node to set.
        Raises:
            TypeError: If next_node is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object or None")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This is the SinglyLinkedList class.
    It represents a singly linked list and can be used to create and manipulate a linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        Attributes:
            head: The head of the linked list (initially set to None).
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).
        Parameters:
            value: The value to insert into the list.
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")

        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
