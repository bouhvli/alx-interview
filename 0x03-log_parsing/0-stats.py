#!/usr/bin/python3
"""
this module solves the: """
import sys


def print_statistics(ttl_s, status_code_c):
    print('File size: {}'.format(ttl_s))
    for key, value in sorted(status_code_c.items()):
        if value:
            print('{}: {}'.format(key, value))


if __name__ == '__main__':
    file_size, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status = {key: 0 for key in codes}

    try:
        for line in sys.stdin:
            count += 1
            param = line.split()
            try:
                status_code = param[-2]
                if status_code in status:
                    status[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(param[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_statistics(file_size, status)
        print_statistics(file_size, status)
    except KeyboardInterrupt:
        print_statistics(file_size, status)
        raise
