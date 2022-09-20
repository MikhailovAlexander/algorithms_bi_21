import copy
import time
from typing import Any


def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num <= 0:
        raise Exception()
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci_rec(num-1) + fibonacci_rec(num-2)


def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num <= 0:
        raise Exception()
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        a = 0
        b = 1
        c = 0
        for i in range(num-2):
            c = a+b
            b = c
            a = b - a
        return c


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    if (matrix is None) or (not __matrix_is_square(matrix)):
        raise Exception()
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return __second_order(matrix)
    else:
        return __determinant_rec(matrix)


def __matrix_is_square(matrix) -> bool:
    """Проверяет, является ли матрица квадратной"""
    columns = len(matrix)
    for i in range(columns):
        rows = len(matrix[i])
        if rows != columns:
            return False
    return True


def __second_order(matrix) -> int:
    """ Вычисляет определитель матрицы 2х2 """
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def __third_order(matrix) -> int:
    """ Вычисляет определитель матрицы 3х3 """
    return matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + matrix[0][2] * matrix[1][0] * matrix[2][1] - matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][1] * matrix[1][0] * matrix[2][2] - matrix[0][0] * matrix[1][2] * matrix[2][1]


def __determinant_rec(matrix) -> int:
    """Считает определитель матрицы n-ого порядка"""
    if len(matrix) == 2:
        return __second_order(matrix)
    else:
        multipliers = matrix[0]
        result = 0
        character = 1
        column_number = 0
        for multiplier in multipliers:
            result += character * multiplier * __determinant_rec(__smaller_matrix(matrix, 0, column_number))
            character *= -1
            column_number += 1
        return result


def __smaller_matrix(matrix: [[int]], row_number, column_number) -> [[int]]:
    """удаляет строку и столбец из матрицы"""
    matrix_copy = copy.deepcopy(matrix)
    matrix_copy.pop(row_number)
    for i in matrix_copy:
        i.pop(column_number)
    return matrix_copy


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def main():
    for num in [10, 20, 30, 35]:
        print_exec_time(lambda x: print(x, fibonacci_rec(x)), x=num)

    matrix = [[1, 2],
              [3, 4]]
    print(f'determinant: {determinant(matrix)}')


if __name__ == '__main__':
    main()
