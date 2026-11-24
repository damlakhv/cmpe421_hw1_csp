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

def backtracking(board, stats):

    empty_cells = find_empty_grid(board)
    if not empty_cells:
        return True

    row, col = empty_cells[0]
    values = order_values_lcv(board, row, col) #find possible values with lcv

    for value in values:
        if constraints_check(board, row, col, value):
            board[row][col] = value

            if backtracking(board, stats):
                return True

            board[row][col] = 0
            stats["backtracks"] += 1

    return False

if __name__ == "__main__":
    from sudoku import grid

    print("Original domain:", get_domain(grid, 0, 1))
    print("LCV order:", order_values_lcv(grid, 0, 1))