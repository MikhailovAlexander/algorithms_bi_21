import copy
import time
from typing import Any


def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num < 0:
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1

    return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)



def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """

    if num < 0:
        raise Exception('нет отрицательных чисел')
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    f1 = 0
    f2 = 1

    for i in range (2, num):
        f2 += f1
        f1 = f2 - f1
    return f2



def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    if not __check_matrix(matrix):
        raise Exception('the parametr...')
    order = len(matrix)
    determ = 0
    if order == 1:
        return matrix[0][0]
    for i in range(order):
        if matrix[0][i] == 0:
            continue
        determ += matrix[0][i] * (-1)**i * minor(matrix, i)
    return determ

def minor(matrix, stolb) -> int:
    red_matrix= copy.deepcopy(matrix)
    red_matrix.pop(0)
    for row in red_matrix:
        row.pop(stolb)
    return determinant(red_matrix)

def __check_matrix(matrix) -> bool:
    str = len(matrix)
    for i in range(str):
        stolb = len(matrix[i])
        if str != stolb:
            return False
    return True

def __choose_row(matrix: [[int]]) -> int:
    pass

def __cofactor(matrix: [[int]], row_idx:int, col_idx:int):
    pass

def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
        start_time = time.time()
        func(**kwargs)
        print(f'duration: {time.time() - start_time} seconds')


def main():
    for num in [10, 20, 30, 35]:
        print_exec_time(lambda x: print(x, fibonacci_iter(x)), x=num)

    matrix = [[1, 2],
              [3, 4]]

    print(f'determinant: {determinant(matrix)}')


if __name__ == '__main__':
    main()
