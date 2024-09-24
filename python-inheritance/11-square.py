#!/usr/bin/python3
from 9-rectangle import Rectangle

class Square(Rectangle):
    """
    A class representing a square that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square (width and height).
    """

    def __init__(self, size):
        """
        Initializes a new square with given size.

        Args:
            size (int): The size of the square (both width and height).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A description of the square in the format
            [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
