#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers in a matrix.

    Parameters:
    matrix (list of lists of int): A 2-dimensional array of integers.

    Returns:
    list of lists of int: A new matrix of the same size where each value is the square of the value of the input matrix.
                          The initial matrix should not be modified.
    """
    new_matrix = []
    
    for row in matrix:
        new_row = [x**2 for x in row]
        new_matrix.append(new_row)
    
    return new_matrix
