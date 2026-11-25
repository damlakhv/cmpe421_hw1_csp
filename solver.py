from sudoku import (
    find_empty_grid,
    get_domain,
    get_neighbors,
    constraints_check
)

def order_values_lcv(board, row, col):

    values = get_domain(board, row, col)
    neighbors = get_neighbors(row, col)

    def count_impact(value):
        impact = 0
        for r, c in neighbors:
            if board[r][c] == 0:
                neighbor_domain = get_domain(board, r, c)

                if value in neighbor_domain:
                    impact += 1

        return impact
    return sorted(values, key=lambda value: (count_impact(value), value))

def backtracking(board, stats, use_mrv=False):

    cell = select_variable(board, use_mrv)

    if cell is None:
        return True

    row, col = cell

    values = order_values_lcv(board, row, col) 

    for value in values:
        if constraints_check(board, row, col, value):
            board[row][col] = value
            stats["assignments"] += 1

            if backtracking(board, stats, use_mrv):
                return True

            board[row][col] = 0
            stats["backtracks"] += 1

    return False

def select_variable(board, use_mrv=False):

    empty_cells = find_empty_grid(board)

    if not empty_cells:
        return None

    if not use_mrv:
        return empty_cells[0]

    return min(
        empty_cells,
        key=lambda cell: len(get_domain(board, cell[0], cell[1]))
    )