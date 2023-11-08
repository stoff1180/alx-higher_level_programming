#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = list(map(lambda x: list(map(lambda e: e**2, x)), matrix))
    return squared_matrix
