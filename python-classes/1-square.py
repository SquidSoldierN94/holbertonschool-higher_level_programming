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

    def __init__(self, size):
        """
        Parameters
        ----------
        size : int
            The size of a side of the square.
        """
        self.__size = size
