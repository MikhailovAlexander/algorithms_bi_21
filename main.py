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
    return fibonacci_rec(num-2) + fibonacci_rec(num-1)


# x = int(input('Какое число Фиббоначи посчитать?'))
# print(f'{x}-е число Фиббоначи = ', fibonacci_rec(x))

def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    fib1, fib2 = 0, 1
    for i in range(2, num+1):
        fib1, fib2 = fib2, fib1+fib2
    return fib1


    # num = int(input('Введите номер числа Фибоначчи: '))
    # print(f'{n}-е число Фиббоначи = ', fibonacci_iter(num))

def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    size = len(matrix)
    determ = 0

    if (len(matrix) != len(matrix[0])):#вылавливаем возможные ошибки
        raise Exception('Матрица не квадратная')
    if matrix is None:
        raise Exception('Ошибка!')
    if size == 1: #случаи с единичной и матрицей 2х2
      determ = matrix[0][0]
    elif size == 2:
        determ = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
    else: #случай для всех остальных матриц
        for x in range(size):
            determ += matrix[0][x]*compl(matrix, 0, x)
    return determ

def minor(matrix, i, j):
    _minor = []
    size = len(matrix)
    for i2 in range(size): #новая матрица для минора
        if i2 == i:
            continue
        row1 = []
        for j2 in range(size):
            if j2 == j:
                continue
            row1.append(matrix[i2][j2])
        _minor.append(row1)
    return _minor

def compl(matrix, i, j):
    return ((-1) ** (i + j)) * determinant(minor(matrix, i, j))


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
