from custom_exception import ArgumentException


def get_triangle_path_count(length: int) -> int:
    """Calculates the number of closed routes of a target length between three
    vertices A, B and C that start and end at the A vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    :raise ArgumentException: when the parameter length must is not an integer.
    greater than 0
    :return: the number of routes.
    """
    if type(length) != int or length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return param_a(length)

def param_a(n):
    if n == 1:
        return 0
    return param_b(n-1) + param_c(n-1)

def param_b(n):
    if n == 1:
        return 1
    return param_a(n-1) + param_c(n-1)

def param_c(n):
    if n == 1:
        return 1
    return param_b(n-1) + param_a(n-1)
def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if type(length) != int or length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    arr = []
    return generate_set_0('', length, arr) + generate_set_1('', length, arr)


def generate_set_0(string, n, arr: list[str]):
    if n == 1:
        return ['0']
    string = generate_set_1(string, n - 1, arr)
    for i in range(len(string)):
        if len(string[i]) == n:
            arr.append(string[i])
        else:
            string[i] += '0'
    return string

def generate_set_1(string, n, arr: list[str]):
    if n == 1:
        return ['1']
    string = generate_set_0(string, n - 1, arr) + generate_set_1(string, n - 1, arr)
    for i in range(len(string)):
        if len(string[i]) == n:
            arr.append(string[i])
        else:
            string[i] += '1'
    return string
def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
