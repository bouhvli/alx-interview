#!/usr/bin/python3
"""
this module solves the: """
import sys


def print_statistics(ttl_s, status_code_c):
    print('File size: {}'.format(ttl_s))
    for code in sorted(status_code_c):
        print('{}: {}'.format(code, status_code_c[code]))


def parse_line(line):
    try:
        parts = line.split()
        ip_addr = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_addr, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None


def main():
    ttl_size = 0
    stattus_code_counts = {
            200: 0, 301: 0, 400: 0,
            401: 0, 403: 0, 404: 0,
            405: 0, 500: 0
            }
    line_processed = 0
    try:
        for line in sys.stdin:
            ip_addr, status_code, file_size = parse_line(line.strip())
            if ip_addr is not None \
                    and status_code is not None \
                    and file_size is not None:
                ttl_size += file_size
                stattus_code_counts[status_code] += 1
                line_processed += 1
                if line_processed % 10 == 0:
                    print_statistics(ttl_size, stattus_code_counts)
    except KeyboardInterrupt:
        pass
    print_statistics(ttl_size, stattus_code_counts)


if __name__ == "__main__":
    main()
