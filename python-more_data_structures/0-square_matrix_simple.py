#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        squares_matrix = map(lambda x: x**2, row)
        new_matrix.append(list(squares_matrix))
    return new_matrix
