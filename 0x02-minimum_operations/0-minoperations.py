#!/usr/bin/python3
"""
a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if (n <= 1):
        return (0)
    res = [float('inf')] * (n + 1)
    res[1] = 0

    for i in range(2, n + 1):
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                res[i] = min(res[i], res[j] + i // j, res[i // j] + j)
    return res[n]
