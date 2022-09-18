import time
from typing import Any


def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num == 1:
        return 0
    if num in (2, 3):
        return 1
    return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)


def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num == 1:
        return 0
    if num in (2, 3):
        return 1
    a, b = 0, 1
    for __ in range (2, num):
        a, b = b, a + b
    return b


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    if matrix_exception(matrix):
        raise Exception('')
    n = len(matrix)
    return matrix_determ(matrix, n)



def matrix_exception(matrix: [[int]]) -> bool:
    if matrix is None or len(matrix) == 0:
        return True
    for row in matrix:
        if len(matrix) != len(row):
            return True

def matrix_determ(matrix: [[int]], n) -> int:
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    determ = 0
    for i in range(n):
        minor = []
        for row in range(n):
            part_minor = []
            for column in range(n):
                if row != 0 and column != i:
                    part_minor += [matrix[row][column]]
            if part_minor != []:
                minor += [part_minor]
        determ += matrix[0][i] * matrix_determ(minor, n - 1) * (-1)**i
    return determ



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
