#!/usr/bin/python3
"""Defines Pascal's Triangle function."""


def pascal_triangle(n):
    """Defines Pascal's Triangle of size n.

    Return list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trig = triangles[-1]
        temp = [1]
        for i in range(len(trig) - 1):
            temp.append(trig[i] + trig[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
