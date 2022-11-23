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

    is_ok(length)
    return point_a(length)

def point_a(n):
    if n == 1:
        return 0
    return point_b(n-1) + point_c(n-1)


def point_b(n):
    if n == 1:
        return 1
    return point_a(n-1) + point_c(n-1)


def point_c(n):
    if n == 1:
        return 1
    return point_b(n-1) + point_a(n-1)
def is_ok(length: int) -> bool:
    if type(length) != int or length < 1 or length is None:
        raise ArgumentException('The parameter length must be an integer greater than 0')


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    is_ok(length)
    array = []
    __set_1("",length,array)
    __set_0("",length,array)
    return array
def __set_1(string,length,array):
    if len(string)+1 == length:
        return array.append(string+"1")
    __set_1(string+"1", length, array)
    __set_0(string+"1", length, array)

def __set_0(string,length,array):
    if len(string)+1 == length:
        return array.append(string+"0")
    __set_1(string+"0", length, array)

def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
