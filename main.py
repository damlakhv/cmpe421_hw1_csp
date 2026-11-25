from copy import deepcopy
from time import perf_counter
from statistics import mean, median

from sudoku import grid
from solver import backtracking
from visualize import visualize_solutions, visualize_benchmark

methods = [
    ("Backtracking + LCV", False, "none"),
    ("Backtracking + FC + LCV", False, "fc"),
    ("Backtracking + MAC + LCV", False, "mac"),
    ("Backtracking + MRV + LCV", True, "none"),
    ("Backtracking + FC + MRV + LCV", True, "fc"),
    ("Backtracking + MAC + MRV + LCV", True, "mac")
]

solutions = {}
benchmark_results = []
repetitions = 30

for name, use_mrv, inference in methods:

    times = []
    backtracks = []
    assignments = []

    for run in range(repetitions):

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

        if not solved:
            raise RuntimeError(f"Sudoku could not be solved: {name}")

        times.append(elapsed_ms)
        backtracks.append(stats["backtracks"])
        assignments.append(stats["assignments"])

        if run == 0:
            solutions[name] = deepcopy(board)

    average_time = mean(times)
    median_time = median(times)

    print(f"\nAlgorithm: {name}")
    print(f"Solved: True")
    print(f"Average Time: {average_time:.3f} ms")
    print(f"Median Time: {median_time:.3f} ms")
    print(f"Assignments: {assignments[0]}")
    print(f"Backtracks: {backtracks[0]}")

    for row in solutions[name]:
        print(row)

    if len(set(backtracks)) != 1 or len(set(assignments)) != 1:
        print("Warning: operation counts varied between runs.")

    benchmark_results.append({
        "name": name,
        "mean_ms": average_time,
        "backtracks": backtracks[0]
    })


visualize_solutions(solutions, grid)
visualize_benchmark(benchmark_results)
