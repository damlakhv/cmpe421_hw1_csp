from copy import deepcopy
from sudoku import grid
from solver import backtracking

board = deepcopy(grid)
stats = {"backtracks": 0}

solved = backtracking(board, stats)

print("Solved:", solved)
print("Backtracks:", stats["backtracks"])

if solved:
    for row in board:
        print(row)