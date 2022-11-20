from custom_exception import ArgumentException

def __param_a(n):
    if n == 1:
        return 0
    if n == 2:
        return 2
    return __param_b(n - 1) + __param_c(n - 1)

def __param_b(n):
    if n == 1 or n == 2:
        return 1
    return __param_a(n - 1) + __param_c(n - 1)

def __param_c(n):
    if n == 1 or n == 2:
        return 1
    return __param_a(n - 1) + __param_b(n - 1)

def get_triangle_path_count(length: int) -> int:
    """Calculates the number of closed routes of a target length between three
    vertices A, B and C that start and end at the A vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    :raise ArgumentException: when the parameter length must is not an integer.
    greater than 0
    :return: the number of routes.
    """
    if type(length) is not int or length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return __param_a(length)

def __set0(string, n, lst: list[str]):
    if n == 1:
        return ['0']
    string = __set1(string, n-1, lst)
    for i in range(len(string)):
        if len(string[i]) == n:
            lst.append(string[i])
        else:
            string[i] += '0'
    return string

def __set1(string, n, lst: list[str]):
    if n == 1:
        return ['1']
    string = __set1(string, n - 1, lst) + __set0(string, n - 1, lst)
    for i in range(len(string)):
        if len(string[i]) == n:
            lst.append(string[i])
        else:
            string[i] += '1'
    return string

def generate_strings(n) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if type(n) is not int or n <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    lst = []
    return __set1('', n, lst) + __set0('', n, lst)

def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
