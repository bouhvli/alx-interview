#!/usr/bin/python3
"""making change

Keyword arguments:
argument -- description
Return: return_description
"""


def makeChange(coins, total):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if total <= 0:
        return 0
    test, tmp = 0, 0
    coins.sort(reverse=True)
    for i in coins:
        while test < total:
            test += i
            tmp += 1
        if test == total:
            return tmp
        test -= i
        tmp -= 1
    return -1
