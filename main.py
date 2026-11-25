from copy import deepcopy
from time import perf_counter

from sudoku import grid
from solver import backtracking


methods = [
    ("Backtracking + LCV", False, "none"),
    ("Backtracking + FC + LCV", False, "fc"),
    ("Backtracking + MAC + LCV", False, "mac"),
    ("Backtracking + MRV + LCV", True, "none"),
    ("Backtracking + FC + MRV + LCV", True, "fc"),
    ("Backtracking + MAC + MRV + LCV", True, "mac")
]

for name, use_mrv, inference in methods:

    # Fresh Sudoku for each algorithm
    board = deepcopy(grid)

    stats = {
    "backtracks": 0,
    "assignments": 0
    }

    start = perf_counter()

    solved = backtracking(
        board,
        stats,
        use_mrv=use_mrv,
        inference=inference
    )

    end = perf_counter()
    elapsed_ms = (end - start) * 1000

    print(f"\nAlgorithm: {name}")
    print(f"Solved: {solved}")
    print(f"Time: {elapsed_ms:.3f} ms")
    print(f"Assignments: {stats['assignments']}")
    print(f"Backtracks: {stats['backtracks']}")


    if solved:
        for row in board:
            print(row)