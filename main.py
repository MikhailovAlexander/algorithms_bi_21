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
    if checkInput(length):
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return calcA(length)


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if checkInput(length):
        raise ArgumentException('The parameter length must be an integer greater than 0')
    array = []
    addOne("", array, length)
    addZero("", array, length)
    return array


def checkInput(input) -> bool:
    return input is None or input < 1 or not (type(input) is int)


def calcA(n):
    if n == 1:
        return 0
    return calcB(n - 1) + calcC(n - 1)


def calcB(n):
    if n == 1:
        return 1
    return calcA(n-1) + calcC(n-1)


def calcC(n):
    if n == 1:
        return 1
    return calcB(n-1) + calcA(n-1)


def addOne(string, array, requiredLength):
    if len(string)+1 == requiredLength:
        return array.append(string+"1")
    addOne(string+"1", array, requiredLength)
    addZero(string+"1", array, requiredLength)


def addZero(string, array, requiredLength):
    if len(string)+1 == requiredLength:
        return array.append(string+"0")
    addOne(string+"0", array, requiredLength)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
