#!/usr/bin/python3

"""
Module that defines a square with validation and area calculation.
"""

class Square:
    """
    A class to represent a square.

    Attributes
    ----------
    size : int
        The size of the square (must be >= 0).

    Methods
    -------
    __init__(self, size=0):
        Initializes the square with a size.
    area(self):
        Returns the area of the square.
    """
    
    def __init__(self, size=0):
        """
        Initializes the square with a size.

        Parameters
        ----------
        size : int, optional
            The size of the square (default is 0).

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size * self.__size
