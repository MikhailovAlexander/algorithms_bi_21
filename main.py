from custom_exception import ArgumentException


def invest_distribution(profit_matrix: list[list[int]]) -> \
        dict[str: int, str: list[int]]:
    """Calculates the optimal distribution of investments between several
    projects. Investments are distributed in predetermined parts.

    :param profit_matrix: an integer matrix with profit values, investment
    levels as rows and the project index as columns;
    :raise ArgumentException: when parameter is not an integer rectangle matrix.
    :return: a dictionary with keys: profit - the max profit value, parts -
    a list with the part of investments for each project. The result example:
    {'profit': 73, 'parts': [1, 1, 2, 1]}
    """
    #написать проверки
    if __matrix_has_errors(profit_matrix) or __matrix_is_not_int(profit_matrix):
        raise ArgumentException('parameter is not an integer rectangle matrix')

    new_matrix = __create_new_matrix(profit_matrix)
    #создать новую матрицу с доп строчкой 0
    profits = calculate_profits(new_matrix)
    max_profits = profits[-1][-1]
    profit = max_profits["profit"]
    last_part = max_profits['part']
    parts = find_parts(last_part, profits)
    return {"profit": profit, "parts": parts}

def __matrix_has_errors(profit_matrix: list[list[int]]) -> bool:
    if profit_matrix is None or profit_matrix == [] or __matrix_is_not_int(profit_matrix):
        return True
    row_dlina = len(profit_matrix[0])
    for row in profit_matrix:
        if row_dlina != len(row):
            return True
    return False

def __matrix_is_not_int(profit_matrix: list[list[int]]) -> bool:
    for row in profit_matrix:
        for value in row:
            if type(value) != int:
                return True
    return False

def __create_new_matrix(profit_matrix):
    new_matrix = [[0] * len(profit_matrix[0])] + [[value for value in row] for row in profit_matrix]
    return new_matrix

def calculate_profits(new_matrix):
    dic_matrix = [[{"profit": 0, "part": 0}for value in row]for row in new_matrix]
    for project_idx in range(len(new_matrix[0])):
        for part_level in range(len(new_matrix)):
            max_profit = 0
            part_max_profit = 0
            for part_previous in range(part_level + 1):
                part_current = part_level - part_previous
                profit_current = new_matrix[part_current][project_idx]
                profit_previuos = dic_matrix[part_previous][project_idx-1]['profit']
                if max_profit < profit_previuos+profit_current:
                    max_profit = profit_previuos+profit_current
                    part_max_profit = part_current
            dic_matrix[part_level][project_idx] = {"profit": max_profit, "part": part_max_profit}
    return dic_matrix


def find_parts(last_part, dic_matrix):
    count_proj = len(dic_matrix[0])
    parts = [last_part]
    previous_parts = len(dic_matrix) - last_part -1
    for ind_project in range (count_proj-2, -1, -1):
        cur_part = dic_matrix[previous_parts][ind_project]['part']
        parts.append(cur_part)
        previous_parts -= cur_part
    return parts[::-1]

def main():
    profit_matrix = [[1, 2]]

    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
