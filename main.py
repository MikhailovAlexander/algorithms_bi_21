from custom_exception import ArgumentException


def parametr_a(n):
    if n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return parametr_b(n - 1) + parametr_c(n - 1)


def parametr_b(n):
    if n == 1 or n == 2:
        return 1
    else:
        return parametr_a(n - 1) + parametr_c(n - 1)


def parametr_c(n):
    if n == 1 or n == 2:
        return 1
    else:
        return parametr_a(n - 1) + parametr_b(n - 1)


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
    return parametr_a(length)


def setter_0(string, n, list1: list[str]):
    if n == 1:
        return ['0']
    string = setter_1(string, n - 1, list1)
    for i in range(len(string)):
        if len(string[i]) == n:
            list1.append(string[i])
        else:
            string[i] += '0'
    return string


def setter_1(string, n, list1: list[str]):
    if n == 1:
        return ['1']
    string = setter_0(string, n - 1, list1) + setter_1(string, n - 1, list1)
    for i in range(len(string)):
        if len(string[i]) == n:
            list1.append(string[i])
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
    list1 = []
    return setter_0('', n, list1) + setter_1('', n, list1)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
