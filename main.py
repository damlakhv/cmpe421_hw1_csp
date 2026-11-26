from copy import deepcopy
from time import perf_counter
from statistics import mean, median

from sudoku import grid, validate_solution

from solver import backtracking
from visualize import visualize_solutions, visualize_benchmark

# Define the six CSP approaches
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

# Run each algorithm 30 times
for name, use_mrv, inference in methods:

    times = []
    backtracks = []
    assignments = []

    for run in range(repetitions):

        # Use a fresh copy of the original Sudoku
        board = deepcopy(grid)

        stats = {
            "backtracks": 0,
            "assignments": 0
        }

        # Measure execution time
        start = perf_counter()

        solved = backtracking(
            board,
            stats,
            use_mrv=use_mrv,
            inference=inference
        )

        end = perf_counter()
        elapsed_ms = (end - start) * 1000

        # Validate the completed solution
        if not solved or not validate_solution(board, grid):
            raise RuntimeError(f"Invalid Sudoku solution: {name}")

        times.append(elapsed_ms)
        backtracks.append(stats["backtracks"])
        assignments.append(stats["assignments"])

        # Save one solution for visualization
        if run == 0:
            solutions[name] = deepcopy(board)

    # Calculate benchmark statistics
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

    # Store results for performance charts
    benchmark_results.append({
        "name": name,
        "mean_ms": average_time,
        "backtracks": backtracks[0]
    })


# Generate Sudoku and benchmark visualizations
visualize_solutions(solutions, grid)
visualize_benchmark(benchmark_results)