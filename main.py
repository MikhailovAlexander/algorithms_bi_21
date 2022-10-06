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
        raise ArgumentException('The price table is not a rectangular matrix '
                                'with float values')
    costs_table = __calculate_cost(price_table)
    reverse_path = __find_path(costs_table)
    return {'cost': costs_table[-1][-1], 'path': list(reversed(reverse_path))}


def __table_has_errors(price_table: list[list[float]]) -> bool:
    if price_table is None or price_table == [] or not(__table_is_float(price_table)):
        return True
    row_size = len(price_table[0])
    for row in price_table:
        if row_size != len(row):
            return True
    return False


def __table_is_float(price_table: list[list[float]]) -> bool:
    for row in price_table:
        for value in row:
            if type(value) == float:
                return True
    return False


def __calculate_cost(price_table: list[list[float]]) -> list[list[float]]:
    inf_table = [[float('inf')]*(len(price_table[0])+1) for i in range(len(price_table)+1)]
    for i in range(1, len(inf_table)):
        for j in range(1, len(inf_table[0])):
            if i == j == 1:
                inf_table[1][1] = price_table[0][0]
                continue
            inf_table[i][j] = min(inf_table[i-1][j], inf_table[i][j-1]) + price_table[i-1][j-1]
    return inf_table


def __find_path(costs_table: list[list[float]]) -> list[tuple[int, int]]:
    reverse_path = []
    row_index, col_index = len(costs_table) - 2, len(costs_table[0]) - 2
    reverse_path.append(tuple((row_index, col_index)))
    while row_index != 0 or col_index != 0:
        left_value = costs_table[row_index + 1][col_index]
        upper_value = costs_table[row_index][col_index + 1]
        if left_value > upper_value:
            row_index -= 1
        else:
            col_index -= 1
        reverse_path.append(tuple((row_index, col_index)))
    return reverse_path


def main():
    table = [[1.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
