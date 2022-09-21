import time
from typing import Any


def fibonacci_rec(num: int) -> int:
    if num <= 0:
        return -1
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)
    pass


def fibonacci_iter(num: int) -> int:
    a = 0
    b = 1
    if num <= 0:
        return -1
    elif num == 1:
        return a
    elif num == 2:
        return b
    else:
        for i in range(3, num + 1):
            c = a + b
            a = b
            b = c
        return b
    pass


def determinant(matrix: [[int]]) -> int:
    i = list(range(len(matrix)))
    result = 0
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    for f in i:
        matrix1 = matrix
        matrix1 = matrix1[1:]
        h = len(matrix1)
        for ind in range(h):
            matrix1[ind] = matrix1[ind][0:f] + matrix1[ind][f + 1:]
        sign = (-1) ** (f % 2)
        result += sign * matrix[0][f] * determinant(matrix1)
    return result


pass


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
