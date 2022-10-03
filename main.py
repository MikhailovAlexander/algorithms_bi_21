class ArgumentException(Exception):
    """Exception raised for errors in the input parameter.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def get_min_cost_path(price_table: list[list[float]]) ->\
        dict[str: float, str: list[tuple[int, int]]]:
    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: a matrix with float cell price values.
    :raise ArgumentException: when price_table is not a rectangle float matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost of the
    path, path - an ordered list of tuples with cell indices.
    """
    if __table_has_errors(price_table):
        raise ArgumentException('The price table is not a rectangular matrix with float values')
    costs_table = __calculate_costs(price_table)
    path = __find_path(costs_table)
    return {'cost': costs_table[-1][-1], 'path': list(reversed(path))}

def __table_has_errors(price_table: list[list[float]]) -> bool:
    if price_table is None or price_table == []:
        return True
    row_idx = len(price_table[0])
    for row in price_table:
        if row_idx != len(row):
            return True
        for value in row:
            if type(value) != float:
                return True
    return False

def __calculate_costs(price_table: list[list[float]]) -> list[list[float]]:
    help_table = [[float('inf')]*(len(price_table[0]) + 1) for i in range(len(price_table) + 1)]
    help_table[1][1] = price_table[0][0]
    for i in range(1, len(help_table)):
        for j in range(1, len(help_table[0])):
            if i == 1 and j == 1:
                continue
            help_table[i][j] = min(help_table[i - 1][j], help_table[i][j - 1]) + price_table[i - 1][j - 1]
    return help_table

def __find_path(costs_table: list[list[float]]) -> list[tuple[int, int]]:
    path = []
    row = len(costs_table) - 2
    col = len(costs_table[0]) - 2
    path.append(tuple((row, col)))
    while row != 0 or col != 0:
        costs_up = costs_table[row][col+1]
        costs_left = costs_table[row+1][col]
        if costs_up > costs_left:
            col -= 1
        else:
            row -= 1
        path.append(tuple((row, col)))
    return path



def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
