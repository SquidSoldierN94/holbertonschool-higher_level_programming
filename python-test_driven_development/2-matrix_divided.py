#!/bin/bash/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): A list of lists of integers or floats.
    div (int/float): The divisor.

    Returns:
    list of lists: A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats, or if div is not an integer/float.
    TypeError: If rows of the matrix are not of the same size.
    ZeroDivisionError: If div is zero.
    """
    
    # Validate the matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Validate that all rows are of the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    # Validate the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform the division and rounding
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    
    return new_matrix
