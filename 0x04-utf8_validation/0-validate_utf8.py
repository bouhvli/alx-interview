#!/usr/bin/python3
"""
this methode checks the UTF-8 validity.
"""


def validUTF8(data):
    i = 0
    for v in data:
        if i == 0:
            if v & 128 == 0:
                i = 0
            elif v & 224 == 192:
                i = 1
            elif v & 240 == 224:
                i = 2
            elif v & 248 == 240:
                i = 3
            else:
                return False
        else:
            if v & 192 != 128:
                return False
            i -= 1
    if i == 0:
        return True
    return False
