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
    IsCorrectInput(length)
    return par_a(length)

def IsCorrectInput (length: int) -> bool:
    if type(length) is not int or length < 1 or length is None:
        raise ArgumentException('The parameter length must be an integer greater than 0')

def par_a(n):
    if n == 1:
        return 0
    return par_b(n-1) + par_c(n-1)


def par_b(n):
    if n == 1:
        return 1
    return par_a(n-1)+par_c(n-1)


def par_c(n):
    if n == 1:
        return 1
    return par_b(n-1)+par_a(n-1)


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    IsCorrectInput(length)
    array = []
    add_1('', length, array)
    add_0('', length, array)
    return array


def add_1(string, n, array):
    if len(string) + 1 == n:
        return array.append(string + '1')
    add_1(string + '1', n, array)
    add_0(string + '1', n, array)


def add_0(string, n, array):
    if len(string) + 1 == n:
        return array.append(string + '0')
    add_1(string + '0', n, array)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
