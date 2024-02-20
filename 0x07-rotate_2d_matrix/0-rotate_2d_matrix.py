#!/usr/bin/python3
"""
    rotate a 2D matrix 90 degrees clockwise.
    Prototype: def rotate_2d_matrix(matrix):
"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix
    Keyword arguments:
    matrix -- the n x n 2D matrix
    Return: Do not return anything.
    The matrix must be edited in-place.
    """
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError('Matrix is not Square')
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
