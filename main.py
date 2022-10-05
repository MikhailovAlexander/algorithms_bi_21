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

    exception_message = 'The price table is not a rectangular matrix with float values'
    if (price_table is None) or (len(price_table) == 0):
        raise ArgumentException(exception_message)

    row_length = len(price_table[0])
    for m in price_table:
        if (m is None) or (len(m) != row_length):
            raise ArgumentException(exception_message)
        for j in m:
            if type(j) is not float:
                raise ArgumentException(exception_message)
    new_price_table = [[float('inf')] * (len(price_table[0]) + 1) for i in range(len(price_table) + 1)]
    mas_path = []

    for i in range(1, len(price_table) + 2):
        for g in range(1, len(price_table[0]) + 2):
            if i - 1 < len(price_table) and g - 1 < len(price_table[0]):
                new_price_table[i][g] = price_table[i - 1][g - 1]

    for i in range(1, len(price_table) + 1):
        for g in range(1, len(price_table[0]) + 1):
            if i == 1 and g == 1:
                continue
            new_price_table[i][g] += \
                min(new_price_table[i - 1][g], new_price_table[i][g - 1])

    Min_path = new_price_table[-1][-1]
    mas_path.append((len(price_table) - 1, len(price_table[0]) - 1))
    i, g = len(price_table), len(price_table[0])
    while i * g != 1:
        if new_price_table[i - 1][g] > new_price_table[i][g - 1]:
            g -= 1
        else:
            i -= 1
        mas_path.append((i - 1, g - 1))

    mas_path.reverse()

    return {'cost': Min_path, 'path': mas_path}


def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
