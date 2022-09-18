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
    if num == 2:
        return 1
    return fibonacci_rec(num-2)+fibonacci_rec(num-1)

# print (fibonacci_rec(10))

def fibonacci_iter (num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    predpred, pred = 0, 1
    for i in range (2, num+1):
        predpred, pred = pred, predpred+pred
    return predpred
pass


def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    size = len(matrix)
    if (len(matrix) != len(matrix[0])):
        raise Exception("not square")
    for row in matrix:
        if ((len(matrix) != len(row))):
            raise Exception("jag matrix")
    if size == 1:
        return deter1x1(matrix)
    return sum((-1)**j*matrix[0][j]*determinant(minor(matrix,0,j)) for j in range(size))

def minor (matrix, i, j):
    m=[row for r,row in enumerate(matrix)if r != i]
    m=[col for c,col in enumerate(zip(*m))if c != j]
    return m
def deter1x1(matrix):
    return matrix[0][0]

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