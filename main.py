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
    #проверка
    costs_table = __calculate_costs(price_table)
    pass


def __calculate_costs(price_table) -> list[list[float]]:
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

            if matrix_copy[i+1][j] < matrix_copy[i][j+1]:
                matrix_copy[i+1][j+1] += matrix_copy[i+1][j]
            else:
                matrix_copy[i+1][j+1] += matrix_copy[i][j+1]

    path = [(count_row, count_column)]
    while count_row != 1 or count_column != 1:
        if matrix_copy[count_row-1][count_column] < matrix_copy[count_row][count_column-1]:
            path.insert(0, (count_row-2, count_column-1))
            count_row -= 1
        else:
            path.insert(0, (count_row-1, count_column - 2))
            count_column -= 1



    print(path)
    return matrix_copy


def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
