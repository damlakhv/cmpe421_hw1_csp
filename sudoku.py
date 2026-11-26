grid = [
    [2, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 1, 0, 0, 0],
    [7, 8, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 2, 9, 0, 0, 3],
    [0, 0, 0, 0, 5, 0, 0, 7, 0],
    [9, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 2, 9, 0, 5, 0, 7],
]


# Find all empty cells (variables)
def find_empty_grid(grid):
    variables = []

    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                variables.append((row, col))

    return variables


# Find all neighbors of a cell (constraints)
def get_neighbors(row, col):
    neighbors = set()

    # Same row
    for c in range(9):
        if c != col:
            neighbors.add((row, c))

    # Same column
    for r in range(9):
        if r != row:
            neighbors.add((r, col))

    # Same 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if (r, c) != (row, col):
                neighbors.add((r, c))

    return neighbors


# Find possible values for a cell (domain)
def get_domain(grid, row, col):

    if grid[row][col] != 0:
        return {grid[row][col]}

    used_values = set()

    for r, c in get_neighbors(row, col):
        if grid[r][c] != 0:
            used_values.add(grid[r][c])

    domain = set(range(1, 10)) - used_values

    return domain


# Check whether a value satisfies Sudoku constraints
def constraints_check(grid, row, col, value):

    if value not in range(1, 10):
        return False

    for r, c in get_neighbors(row, col):
        if grid[r][c] == value:
            return False

    return True


# Initialize domains for all cells
def initialize_domains(grid):
    domains = {}

    for row in range(9):
        for col in range(9):
            domains[(row, col)] = get_domain(grid, row, col)

    return domains

def validate_solution(board, original_grid):

    digits = set(range(1, 10))

    for row in range(9):
        if set(board[row]) != digits:
            return False

    for col in range(9):
        if {board[row][col] for row in range(9)} != digits:
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):

            box = {
                board[row][col]
                for row in range(box_row, box_row + 3)
                for col in range(box_col, box_col + 3)
            }

            if box != digits:
                return False

    for row in range(9):
        for col in range(9):
            if original_grid[row][col] != 0:
                if board[row][col] != original_grid[row][col]:
                    return False

    return True
