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
    if __table_exception(price_table):
        raise ArgumentException('The price table is not a rectangular matrix with float values')
    cost_table = calculate_path(price_table)
    path = get_path(cost_table)
    return {'cost': cost_table[-1][-1], 'path': path}

def __table_exception(price_table: list[list[float]]) -> bool:
    if price_table is None or price_table == [] or __is_string(price_table):
        return True
    row_size = len(price_table[0])
    for row in price_table:
        if row_size != len(row):
            return True
    return False

def __is_string(price_table: list[list[float]]) -> bool:
    for row in price_table:
        for col in row:
            if not isinstance(col, (int, float)):
                return True
    return False
def calculate_path(price_table: list[list[float]]) -> list[list[float]]:
    if len(price_table[0]) > len(price_table):
        costs_table = [[float('inf')] * (len(price_table[0]) + 1) for __ in range(len(price_table) + 1)]
    elif len(price_table) > len(price_table[0]):
        costs_table = [[float('inf')] * (len(price_table[0]) + 1) for __ in range(len(price_table) + 1)]
    else:
        costs_table = [[float('inf')] * (len(price_table) + 1) for __ in range(len(price_table) + 1)]
    for i in range(1, len(costs_table)):
        for j in range(1, len(costs_table[0])):
            if i == 1 and j == 1:
                costs_table[i][j] = price_table[0][0]
                continue
            if costs_table[i - 1][j] < costs_table[i][j - 1]:
                costs_table[i][j] = price_table[i - 1][j - 1] + \
                                                    costs_table[i - 1][j]
            else:
                costs_table[i][j] = price_table[i - 1][j - 1] + costs_table[i][j - 1]
    return costs_table

def get_path(costs_table: list[list[float]]) -> list[tuple[int, int]]:
    row = len(costs_table) - 2
    col = len(costs_table[0]) - 2
    list_of_tuples = [tuple((row, col))]
    while row != 0 or col != 0:
        cost_up = costs_table[row][col+1]
        cost_left = costs_table[row+1][col]
        if cost_up > cost_left:
            col -= 1
        else:
            row -= 1
        list_of_tuples.append(tuple((row, col)))
    return list_of_tuples[::-1]
def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))

if __name__ == '__main__':
    main()
