#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares_matrix = []
    for row in matrix:
        row_squares = []
        for number in row:
            row_squares.append(number**2)
        squares_matrix.append(row_squares)
    return squares_matrix
