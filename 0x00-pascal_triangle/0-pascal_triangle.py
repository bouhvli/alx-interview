#!/usr/bin/python3
"""pascale traingle
  a function def pascal_triangle(n): that returns a
  list of lists of integers representing the Pascal’s
  triangle of n:

    Returns an empty list if n <= 0
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    traingle = [[1]]
    for i in range(1, n):
        perv_row = traingle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(perv_row[j - 1] + perv_row[j])
        new_row.append(1)
        traingle.append(new_row)
    return traingle
