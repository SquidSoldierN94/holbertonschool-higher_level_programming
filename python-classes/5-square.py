#!/usr/bin/python3

"""
Module that defines a square with validation, area calculation, and printing functionality.
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
    size(self):
        Gets the current size of the square.
    size(self, value):
        Sets the size of the square with validation.
    area(self):
        Returns the area of the square.
    my_print(self):
        Prints the square using '#' characters.
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
        self.size = size

    @property
    def size(self):
        """
        Gets the current size of the square.

        Returns
        -------
        int
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Parameters
        ----------
        value : int
            The size of the square.

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
        Returns the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' characters. 

        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
