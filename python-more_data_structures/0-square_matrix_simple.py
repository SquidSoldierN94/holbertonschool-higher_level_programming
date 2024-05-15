#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for line in matrix:
        squared_line = []
        for element in line:
            squared_line.append(element ** 2)
        squared_matrix.append(squared_line)
    return squared_matrix
