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
        Parameters
        ----------
        size : int, optional
            The size of a side of the square (default is 0).

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
