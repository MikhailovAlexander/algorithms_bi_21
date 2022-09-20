import time
from typing import Any


def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num <= 2:
        return num - 1
    return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)


def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num < 2:
        return num - 1
    fibonacci_1 = 0
    fibonacci_2 = 1
    i = 3
    while i <= num:
        fibonacci_1, fibonacci_2 = fibonacci_2, (fibonacci_1 + fibonacci_2)
        i = i + 1
    return fibonacci_2


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    if matrix is None or (not is_square_matrix(matrix)):
        raise Exception()
    matrix_size = len(matrix)
    det = 0
    if matrix_size == 1:
        det = matrix[0][0]
    elif matrix_size == 2:
        det = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    else:
        for i in range(matrix_size):
            det += matrix[0][i] * algebraic_complement(matrix, 0, i)
    return det


def minor(matrix, i, j):
    minor_matrix = []
    matrix_size = len(matrix)
    for i2 in range(matrix_size):
        if i2 == i:
            continue
        new_row = []
        for j2 in range(matrix_size):
            if j2 == j:
                continue
            new_row.append(matrix[i2][j2])
        minor_matrix.append(new_row)
    return minor_matrix


def algebraic_complement(matrix, i, j):
    return ((-1) ** (i + j)) * determinant(minor(matrix, i, j))


def is_square_matrix(matrix) -> bool:
    num_rows = len(matrix)
    for i in range(num_rows):
        num_cols = len(matrix[i])
        if num_rows != num_cols:
            return False
    return True


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
