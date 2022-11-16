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

    a = matrix[0][0]
    size = len(matrix)

    if size == 1:
        return a

    b, c = matrix[0][1], matrix[1][0]
    return __determinant_rec(a, b, c, size)


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
                if i == j and matrix[i][j] != matrix[0][0]:
                    return False
                elif i == j - 1 and matrix[i][j] != matrix[0][1]:
                    return False
                elif i == j + 1 and matrix[i][j] != matrix[1][0]:
                    return False
                elif matrix[i][j] != 0:
                    return False
        return True


def __determinant_rec(a, b, c, dimension) -> int:
    if dimension == 1:
        return a
    elif dimension == 2:
        return a * a - b * c
    else:
        return a * __determinant_rec(a, b, c, dimension - 1) - b * c * __determinant_rec(a, b, c, dimension - 2)


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
