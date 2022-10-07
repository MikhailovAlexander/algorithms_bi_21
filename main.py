import copy


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
    if not __is_readable(price_table):
        raise ArgumentException('The price table is not a rectangular matrix with float values')

    output = __calculate_costs(price_table)
    return output


def __calculate_costs(price_table) -> dict[str: float, str: list[tuple[int, int]]]:
    matrix_copy = copy.deepcopy(price_table)

    length = len(matrix_copy[0])
    new_row = [float("inf")]
    for i in range(length-1):
        new_row.append(float("inf"))
    matrix_copy.insert(0, new_row)

    for row in matrix_copy:
        row.insert(0, float("inf"))

    count_row = len(price_table)
    count_column = len(price_table[0])

    for i in range(count_row):
        for j in range(count_column):
            if (i == 0) and (j == 0):
                matrix_copy[i+1][j+1] = price_table[i][j]

            elif matrix_copy[i+1][j] < matrix_copy[i][j+1]:
                matrix_copy[i+1][j+1] = price_table[i][j] + matrix_copy[i+1][j]
            else:
                matrix_copy[i+1][j+1] = price_table[i][j] + matrix_copy[i][j+1]

    path = [(count_row-1, count_column-1)]
    while count_row != 1 or count_column != 1:
        if matrix_copy[count_row][count_column-1] < matrix_copy[count_row-1][count_column]:
            path.insert(0, (count_row-1, count_column-2))
            count_column -= 1
        else:
            path.insert(0, (count_row - 2, count_column - 1))
            count_row -= 1

    output = {'cost': matrix_copy[-1][-1], 'path': path}
    return output


def __is_readable(matrix) -> bool:
    if matrix is None or __has_string(matrix) or matrix == []:
        return False
    len1 = len(matrix[0])
    for row in matrix:
        if len(row) != len1:
            return False
    return True


def __has_string(matrix) -> bool:
    for row in matrix:
        for element in row:
            if not isinstance(element, float):
                return True
    return False


def main():
    table = [[1., 4., 5., 7.],
             [1., 4., 5., 6.],
             [10., 11., 7., 10.],
             [8., 9., 4., 5.],
             [5., 6., 7., 10.]
             ]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
