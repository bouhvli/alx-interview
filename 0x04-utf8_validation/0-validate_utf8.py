#!/usr/bin/python3
"""
this methode checks the validity.
"""


def validUTF8(data):
    i = 0
    while i < len(data):
        if data[i] & 0b10000000 == 0:
            i += 1
        else:
            num_bytes = 0
            while i < len(data) and data[i] &\
                    (0b10000000 >> num_bytes) ==\
                    (0b10000000 >> (num_bytes + 1)):
                num_bytes += 1
            if num_bytes < 1 or num_bytes > 3 or i + num_bytes >= len(data):
                return False
            for j in range(1, num_bytes + 1):
                if data[i + j] & 0b11000000 != 0b10000000:
                    return False
            i += num_bytes + 1
    return True
