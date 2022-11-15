from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    if matrix_exception(matrix) or wrong_main_diagonal(matrix) or wrong_up_diagonal(matrix) \
            or wrong_low_diagonal(matrix) or wrong_zeroes(matrix):
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    return rec_determinant(matrix, a, b, c, n)

def rec_determinant(matrix: list[list[int]], a: int, b: int, c: int, n: int) -> int:
    if n == 2:
        return a**2 - b * c
    if n == 1:
        return a
    else:
        return a * rec_determinant(matrix, a, b, c, n-1) - b * c * rec_determinant(matrix, a, b, c, n-2)
def matrix_exception(matrix: list[list[int]]) -> bool:
    if matrix is None or matrix == []:
        return True
    for row in matrix:
        if len(matrix) != len(row):
            return True
    return False

def wrong_main_diagonal(matrix: list[list[int]]) -> bool:
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if i == 0 and j == 0:
                comparer = matrix[i][j]
            if i == j and comparer != matrix[i][j]:
                return True
            else:
                continue
    return False

def wrong_low_diagonal(matrix: list[list[int]]) -> bool:
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if i == 1 and j == 0:
                comparer = matrix[i][j]
            if i-j == 1 and comparer != matrix[i][j]:
                return True
            else:
                continue
    return False
def wrong_up_diagonal(matrix: list[list[int]]) -> bool:
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if i == 0 and j == 1:
                comparer = matrix[i][j]
            if j-i == 1 and comparer != matrix[i][j]:
                return True
            else:
                continue
    return False

def wrong_zeroes(matrix: list[list[int]]) -> bool:
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if j-i >= 2 and matrix[i][j] !=0:
                return True
            else:
                continue
    return False
def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
