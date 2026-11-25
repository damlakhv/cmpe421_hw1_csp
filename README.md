# Sudoku CSP Solver

This project was developed for **CMPE 421 – Artificial Intelligence** at TED University.

The goal is to solve a Sudoku puzzle using six different Constraint Satisfaction Problem (CSP) approaches and compare their performance.

## Implemented Algorithms

1. Backtracking
2. Backtracking + Forward Checking (FC)
3. Backtracking + Maintaining Arc Consistency (MAC)
4. Backtracking + Minimum Remaining Values (MRV)
5. Backtracking + FC + MRV
6. Backtracking + MAC + MRV

All algorithms use **Least Constraining Value (LCV)** for value ordering.

## Project Structure

- `sudoku.py` – Sudoku grid, domains, and constraints
- `solver.py` – CSP algorithms and heuristics
- `main.py` – Execution and performance benchmarking
- `visualize.py` – Solution and performance visualizations
- `results/` – Generated visualizations

## How to Run

Install the required library:

```bash
pip install matplotlib
```

Run the project:

```bash
python main.py
```

Each algorithm is executed 30 times to measure its average execution time. The program also reports the number of assignments and backtracks.

## Output

The program generates three visualizations:

- `sudoku_solutions.png`
- `execution_time.png`
- `backtracks.png`

These files are saved in the `results/` directory.