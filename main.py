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
    if


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if length <= 0 or length is None or type(length) != int:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    array=[]
    __set_1('',length,array), __set_0('',length,array)
    return array
def __set_1(string,length,array)
    if len(string) == length:
        array.append(string)
    else:
        string += '1'
    __set_1(string, length, array)
    __set_0(string, length, array)

def __set_0(string,length,array)
    if len(string) == length:
        array.append(string)
    else:
        string += '0'
    __set_1(string, length, array)
def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
