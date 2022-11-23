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
    if not isinstance(length, int) or length < 1:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return loc_a(length)


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if length is None or not isinstance(length, int) or length < 1:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    itog = []
    __set_one("", length, itog)
    __set_zero("", length, itog)
    return itog


def __set_zero(st, n, mas):
    if n == 1:
        st = st + '0'
        mas.append(st)
        return
    if st == "":
        st = st + '0'
        __set_one(st, n - 1, mas)
    elif st[-1] != '0':
        st = st + '0'
        __set_one(st, n - 1, mas)


def __set_one(st, n, mas):
    if n == 1:
        st = st + '1'
        mas.append(st)
        return
    else:
        st = st + '1'
        __set_zero(st, n - 1, mas)
        __set_one(st, n - 1, mas)


def loc_a(n):
    if n == 1:
        return 0
    if n == 2:
        return 2
    return loc_b(n - 1) + loc_c(n - 1)


def loc_b(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return loc_a(n - 1) + loc_c(n - 1)


def loc_c(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return loc_a(n - 1) + loc_b(n - 1)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()