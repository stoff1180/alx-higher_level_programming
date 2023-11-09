#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squared_matrix = list(map(lambda x: list(map(lambda a: a**2, x)), matrix))
    return squared_matrix
