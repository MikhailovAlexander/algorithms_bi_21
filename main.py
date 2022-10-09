class ArgumentException(Exception):
    """Exception raised for errors in the input parameter.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def get_min_cost_path(price_table: list[list[float]]) -> \
        dict[str: float, str: list[tuple[int, int]]]:
    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: a matrix with float cell price values.
    :raise ArgumentException: when price_table is not a rectangle float matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost of the
    path, path - an ordered list of tuples with cell indices.
    """
    check_table(price_table)

    num_rows = len(price_table)
    num_cols = len(price_table[0])

    graph = to_graph(price_table)
    costs = initial_costs(price_table)
    parents = initial_parents(price_table)

    processed = []

    node = find_lowest_cost_node(costs, processed)  # Реализация Алгоритма Дейкстры
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    start = (0, 0)
    finish = (num_rows - 1, num_cols - 1)

    parent = finish
    path = [parent]

    while parent != start:
        parent = parents[parent]
        path.append(parent)

    path = list(reversed(path))

    return {'cost': costs[finish], 'path': path}


def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))


def check_table(price_table: list[list[float]]) -> bool:  # Проверяем матрицу
    if type(price_table) is not list:
        raise ArgumentException('The price table is not a rectangular matrix with float values')

    num_rows = len(price_table)
    if num_rows == 0:
        raise ArgumentException('The price table is not a rectangular matrix with float values')

    num_cols_default = len(price_table[0])
    for i in range(1, num_rows):
        num_cols = len(price_table[i])
        if num_cols_default != num_cols:
            raise ArgumentException('The price table is not a rectangular matrix with float values')

    for i, row in enumerate(price_table):
        for j, cost in enumerate(row):
            if type(cost) != float:
                raise ArgumentException('The price table is not a rectangular matrix with float values')
    return True


def to_graph(price_table):  # Преобразовываем матрицу в граф
    graph = {}

    num_rows = len(price_table)
    num_cols = len(price_table[0])

    for i in range(0, num_rows):
        for j in range(0, num_cols):
            key = (i, j)
            graph[key] = {}

            if i > 0:
                graph[key][(i - 1, j)] = price_table[i - 1][j]

            if (i + 1) < num_rows:
                graph[key][(i + 1, j)] = price_table[i + 1][j]

            if j > 0:
                graph[key][(i, j - 1)] = price_table[i][j - 1]

            if (j + 1) < num_cols:
                graph[key][(i, j + 1)] = price_table[i][j + 1]

    return graph


def initial_costs(price_table):  # Определяет, как считаем стоимости
    infinity = float("inf")
    costs = {}

    for i, row in enumerate(price_table):
        for j, cost in enumerate(row):
            if i == 0 and j == 0:
                costs[(i, j)] = cost
            elif (i == 0 and j == 1) or (i == 1 and j == 0):
                costs[(i, j)] = cost + price_table[0][0]
            else:
                costs[(i, j)] = infinity
    return costs


def initial_parents(price_table):  # Создает хэш-таблицу, в которую записываются "удачные соседи", потом из этого путь
    parents = {}

    for i, row in enumerate(price_table):
        for j, cost in enumerate(row):
            if (i == 0 and j == 1) or (i == 1 and j == 0):
                parents[(i, j)] = (0, 0)
            else:
                parents[(i, j)] = None
    return parents


def find_lowest_cost_node(costs, processed):  # Функция находит узел с наименьшей стоимостью
    infinity = float("inf")
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost, lowest_cost_node = cost, node
    return lowest_cost_node


if __name__ == '__main__':
    main()
