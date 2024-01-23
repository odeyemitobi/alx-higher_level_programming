#!/usr/bin/python3
"""Square class defining"""


class Square:
    """
    This is the Square class.
    It represents a square and can be used as a template
    for creating square objects.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        Parameters:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position values are not positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the current size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Parameters:
            value (int): The size to set.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Gets the current position of the square.
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        Parameters:
            value (tuple): The position to set.
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.
        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square using the character '#'.
        If size is equal to 0, prints an empty line.
        Position is used to add space before printing the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
