#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = []
        for elem in row:
            row_str.append("{:d}".format(elem))
        print(" ".join(row_str))
