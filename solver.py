from sudoku import (
    find_empty_grid,
    get_domain,
    get_neighbors,
    constraints_check,
    initialize_domains
)

def order_values_lcv(board, row, col, domains=None):

    if domains is not None:
        values = domains[(row, col)]
    else:
        values = get_domain(board, row, col)

    neighbors = get_neighbors(row, col)

    def count_impact(value):
        impact = 0

        for r, c in neighbors:

            if board[r][c] == 0:

                if domains is not None:
                    neighbor_domain = domains[(r, c)]
                else:
                    neighbor_domain = get_domain(board, r, c)

                if value in neighbor_domain:
                    impact += 1

        return impact

    return sorted(
        values,
        key=lambda value: (count_impact(value), value)
    )

def backtracking(board, stats, use_mrv=False, inference="none", domains=None):

    if inference == "fc" and domains is None:
        domains = initialize_domains(board)

    cell = select_variable(board, use_mrv)

    if cell is None:
        return True

    row, col = cell

    values = order_values_lcv(board, row, col) 

    for value in values:
        if constraints_check(board, row, col, value):
            board[row][col] = value
            stats["assignments"] += 1

            next_domains = domains

            if inference == "fc":
                next_domains = forward_check(
                    board, domains, row, col, value
                )

            if inference != "fc" or next_domains is not None:

                if backtracking(
                    board, stats, use_mrv, inference, next_domains
                ):
                    return True

            board[row][col] = 0
            stats["backtracks"] += 1


    return False

def select_variable(board, use_mrv=False, domains=None):

    empty_cells = find_empty_grid(board)

    if not empty_cells:
        return None

    if not use_mrv:
        return empty_cells[0]

    def domain_size(cell):
        if domains is not None:
            return len(domains[cell])

        return len(get_domain(board, cell[0], cell[1]))

    return min(empty_cells, key=domain_size)

def forward_check(board, domains, row, col, value):

    #make a copy for the domain because if the value is wrong backtraking will work
    new_domains = {
        cell: values.copy()
        for cell, values in domains.items()
    }

    new_domains[(row, col)] = {value}

    for neighbor in get_neighbors(row, col):

        r, c = neighbor

        if board[r][c] == 0:

            new_domains[neighbor].discard(value)
            if len(new_domains[neighbor]) == 0:
                return None

    return new_domains