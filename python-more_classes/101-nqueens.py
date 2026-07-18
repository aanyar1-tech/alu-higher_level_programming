#!/usr/bin/python3
"""N queens puzzle solver."""
import sys


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row, board, solutions):
    """Recursively solve the N queens problem using backtracking."""
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(n, row + 1, board, solutions)
            board[row] = -1


def main():
    """Entry point for the N queens program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve(n, 0, board, solutions)

    for solution in solutions:
        result = [[i, solution[i]] for i in range(n)]
        print(result)


if __name__ == "__main__":
    main()
