from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    if (ReadableMatrix(matrix)) and (NecessaryDiagonals(matrix)):
        n = len(matrix)
        if n == 1:
            a = matrix[0][0]
            b = 0
            c = 0
        else:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[1][0]
        return DeterminantRec(a, b, c, n)
    raise ArgumentException('parameter is not a tridiagonal integer matrix')


def ReadableMatrix(matrix) -> bool:
    if matrix == [] or matrix is None:
        return False
    length = len(matrix)
    for row in matrix:
        if len(row) != length:
            return False
    return True


def NecessaryDiagonals(matrix) -> bool:
    if len(matrix) == 1:
        return True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                if matrix[i][j] != matrix[0][0]:
                    return False
            if i == j - 1:
                if matrix[i][j] != matrix[0][1]:
                    return False
            if i == j + 1:
                if matrix[i][j] != matrix[1][0]:
                    return False
            if (i != j) and (i != j + 1) and (i != j - 1):
                if matrix[i][j] != 0:
                    return False
    return True


def DeterminantRec(a, b, c, n) -> int:
    if n==1:
        return a
    if n == 2:
        return a ** 2 - b * c
    return a * DeterminantRec(a, b, c, n - 1) - b * c * DeterminantRec(a, b, c, n - 2)


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
