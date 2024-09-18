#!/usr/bin/python3

"""
Module that defines a square.
"""

class Square:
    """
    A class to represent a square.

    Attributes
    ----------
    size : int
        The size of the square.

    Methods
    -------
    __init__(self, size):
        Initializes the square with a size.
    """
    
    def __init__(self, size):
        """
        Initializes the square with a size.

        Parameters
        ----------
        size : int
            The size of the square.
        """
        self.__size = size
