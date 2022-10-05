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
    cost_table = __calculate_costs(price_table)
    path = __find_path(cost_table)
    return {'cost': cost_table[-1][-1], 'path': path}
def __table_has_errors(price_table: list[list[float]]) -> bool:
    if price_table is None or price_table == [] or __table_is_not_float(price_table):
        return True
    row_dlina = len(price_table[0])
    for row in price_table:
        if row_dlina != len(row):
            return True
    return False

def __table_is_not_float(price_table: list[list[float]]) -> bool:
    for row in price_table:
        for value in row:
            if type(value) == float:
                return False
    return True

def __calculate_costs(price_table: list[list[float]]) -> list[list[float]]:
    new_table = [[float('inf')]*(len(price_table[0]) + 1) for i in range(len(price_table) + 1)]
    new_table[1][1] = price_table[0][0]
    for i in range(1, len(new_table)):
        for j in range(1, len(new_table[0])):
            if i == 1 and j == 1:
                new_table[i][j] = price_table[0][0]
                continue
            new_table[i][j] = min(new_table[i - 1][j], new_table[i][j - 1]) + price_table[i - 1][j - 1]
    return new_table

def __get_path(new_table: list[list[float]], row, col) -> list[tuple[int,int]]:
    list_of_kort = [tuple((row, col))]
    while row != 0 or col != 0:
        cost_up = new_table[row][col + 1]
        cost_left = new_table[row + 1][col]
        if cost_left < cost_up:
            col -= 1
        else:
            row -= 1
        list_of_kort.append(tuple((row, col)))
    return list_of_kort[::-1]

def __find_path(new_table: list[list[float]]) -> list[tuple[int,int]]:
    row = len(new_table) - 2
    col = len(new_table[0]) - 2
    return __get_path(new_table, row, col)


def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
