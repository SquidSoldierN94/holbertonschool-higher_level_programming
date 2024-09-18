#!/usr/bin/env python3
"""
This module defines a Square class used to represent a square with a specific size.
"""

class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    size : int
        The size of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a specific size.

        Parameters
        ----------
        size : int, optional
            The size of a side of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns
        -------
        int
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters
        ----------
        value : int
            The size of a side of the square.

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size * self.__size
