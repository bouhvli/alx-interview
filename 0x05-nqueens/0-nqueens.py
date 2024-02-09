#!/usr/bin/python3
"""
    this module has a solution of nqueens
"""
import sys


def solve_nq(r, n, cols, neg, board, pos):
    """
        using backtracking to solve the issue, using bitwise operations
    """
    if r == n:
        print([[i, board[i]] for i in range(n)])
        return
    for c in range(n):
        if cols & (1 << c) or \
           pos & (1 << (r + c)) or \
           neg & (1 << (r - c + n - 1)):
            continue
        cols |= (1 << c)
        pos |= (1 << (r + c))
        neg |= (1 << (r - c + n - 1))
        board[r] = c

        solve_nq(r + 1, n, cols, neg, board, pos)
        cols &= ~(1 << c)
        pos &= ~(1 << (r + c))
        neg &= ~(1 << (r - c + n - 1))


def nqueens(N):
    """
        the solution to the nqueens problem
    """
    cols = 0
    pos = 0
    neg = 0
    board = [-1] * N
    solve_nq(0, N, cols, neg, board, pos)


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print('N must be at least 4')
            sys.exit(1)
        nqueens(N)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
