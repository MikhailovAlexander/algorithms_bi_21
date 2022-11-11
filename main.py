from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    if __has_errors(matrix) or __wrong_elements(matrix):
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    if len(matrix) == 1:
        return matrix[0][0]
    a = matrix[0][0]
    b = matrix[1][0]
    c = matrix[0][1]
    n = len(matrix[0])
    return __rec(a, b, c, n)

def __has_errors (matrix: list[list[int]]) -> bool:
    if matrix is None or matrix == []:
        return True
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return True
    for row in matrix:
        for value in row:
            if type(value) != int:
                return True
        return False

def __wrong_elements(matrix) -> bool:
    n=len(matrix[0])
    for i in range (0, n-1):
        for j in range (0, n-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return True
    for i in range(0, n - 2):
        for j in range(0, n - 2):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return True
    if matrix[0].count(0) < n - 2 or matrix[n - 1].count(0) < n - 2:
        return True
    for i in range(n):
        if matrix[i].count(0) < n - 3:
            return True
    return False

def __rec(a, b, c, n):
    if n == 1:
        return a
    if n == 2:
        return a ** 2 - b * c
    else:
        return a * __rec(a, b, c, n-1) - b * c * __rec(a, b, c, n-2)

def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))

if __name__ == '__main__':
    main()
