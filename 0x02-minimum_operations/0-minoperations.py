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
    cp = 0
    cpp = 2
    while cpp <= n:
        if (n % cpp == 0):
            cp += cpp
            n = n / cpp
            cpp -= 1
        cpp += 1
    return cp
