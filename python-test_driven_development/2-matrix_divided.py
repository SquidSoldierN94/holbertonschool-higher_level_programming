#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a divisor.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of list of int/float): A matrix to be divided.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix elements are not lists of integers/floats,
                   if rows of the matrix are not of the same size,
                   or if div is not an integer or float.
        ZeroDivisionError: If div is zero.

    Returns:
        list of list of float: A new matrix with all elements divided by div,
                               rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(element / div, 2) for element in row] for row in matrix]
