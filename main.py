import copy

from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """


    return __determinant_rec(matrix)


def __determinant_rec(matrix) -> int:
    """Считает определитель матрицы n-ого порядка"""
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
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


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
