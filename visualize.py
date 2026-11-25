import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def visualize_solutions(solutions, initial_grid):

    os.makedirs("results", exist_ok=True)

    fig, axes = plt.subplots(2, 3, figsize=(16, 11))

    for ax, (name, board) in zip(axes.flat, solutions.items()):

        for row in range(9):
            for col in range(9):

                if initial_grid[row][col] != 0:
                    ax.add_patch(
                        Rectangle(
                            (col, row), 1, 1,
                            facecolor="aliceblue"
                        )
                    )

                ax.text(
                    col + 0.5,
                    row + 0.5,
                    str(board[row][col]),
                    ha="center",
                    va="center",
                    fontsize=12,
                    fontweight="bold" if initial_grid[row][col] != 0 else "normal"
                )

        for i in range(10):
            width = 2.5 if i % 3 == 0 else 0.5

            ax.plot([i, i], [0, 9], color="black", linewidth=width)
            ax.plot([0, 9], [i, i], color="black", linewidth=width)

        ax.set_xlim(0, 9)
        ax.set_ylim(9, 0)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(name, fontsize=11, pad=12)

    fig.suptitle("Sudoku Solutions - Six CSP Approaches", fontsize=16)

    plt.tight_layout()
    plt.savefig("results/sudoku_solutions.png", dpi=200)
    plt.close()


def visualize_benchmark(results):

    os.makedirs("results", exist_ok=True)

    names = [result["name"] for result in results]
    times = [result["mean_ms"] for result in results]
    backtracks = [result["backtracks"] for result in results]

    fig, ax = plt.subplots(figsize=(11, 5))

    bars = ax.barh(names, times)
    ax.invert_yaxis()
    ax.set_xlabel("Average Execution Time (ms)")
    ax.set_title("Execution Time Comparison")

    ax.bar_label(bars, fmt="%.3f", padding=3)
    ax.set_xlim(0, max(times) * 1.20)

    plt.tight_layout()
    plt.savefig("results/execution_time.png", dpi=200)
    plt.close()

    fig, ax = plt.subplots(figsize=(11, 5))

    bars = ax.barh(names, backtracks)
    ax.invert_yaxis()
    ax.set_xlabel("Number of Backtracks")
    ax.set_title("Backtrack Comparison")

    ax.bar_label(bars, padding=3)
    ax.set_xlim(0, max(backtracks) * 1.20)

    plt.tight_layout()
    plt.savefig("results/backtracks.png", dpi=200)
    plt.close()