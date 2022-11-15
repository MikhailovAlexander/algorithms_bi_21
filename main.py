import copy

from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    if not (__is_readable(matrix)) or not (__correct_digits(matrix)):
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    return __determinant_rec(matrix)


def __is_readable(matrix) -> bool:
    if matrix is None or matrix == []:
        return False
    len1 = len(matrix)
    for row in matrix:
        if len(row) != len1:
            return False
    return True


def __correct_digits(matrix) -> bool:
    if len(matrix) == 1:
        return True
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    if matrix[i][j] != matrix[0][0]:
                        return False
                elif i == j - 1:
                    if matrix[i][j] != matrix[0][1]:
                        return False
                elif i == j + 1:
                    if matrix[i][j] != matrix[1][0]:
                        return False
                elif matrix[i][j] != 0:
                    return False
        return True


def __determinant_rec(matrix) -> int:
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        return matrix[0][0] * __determinant_rec(__smaller_matrix(matrix, -1, -1)) - matrix[0][1]*matrix[1][0] * __determinant_rec(__smaller_matrix(__smaller_matrix(matrix, -1, -1), -1, -1))


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
