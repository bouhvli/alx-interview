#!/usr/bin/python3

"""
 returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:
                    count += 1
                if c == 0 or grid[r][c - 1] == 0:
                    count += 1
                if r == len(grid) - 1 or grid[r + 1][c] == 0:
                    count += 1
                if c == len(grid[r]) - 1 or grid[r][c + 1] == 0:
                    count += 1
    return count
