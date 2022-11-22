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
    if not __check_input(length):
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return get_a(length)


def __check_input(n) -> bool:
    return not (n is None or not(type(n) is int) or n < 1)


def get_a(n):
    if n == 1:
        return 0
    return get_b(n-1) + get_c(n-1)


def get_b(n):
    if n == 1:
        return 1
    return get_a(n-1) + get_c(n-1)


def get_c(n):
    if n == 1:
        return 1
    return get_b(n-1) + get_a(n-1)


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if lengtn is None or not(type(length) is int) or length < 1:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    output = []
    __add1("", output, length)
    __add0("", output, length)
    return output


def __add1(string, output, length_needed):
    if len(string) + 1 == length_needed:
        output.append(string+"1")
        return
    else:
        __add1(string+"1", output, length_needed)
        __add0(string+"1", output, length_needed)


def __add0(string, output, length_needed):
    if len(string) + 1 == length_needed:
        output.append(string + "0")
        return
    else:
        __add1(string + "0", output, length_needed)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
