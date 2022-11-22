from custom_exception import ArgumentException
"""
1. Сделать проверку 
2. Реализовать функцию get_triangle_path_count
3. Реализовать функцию generate_strings"""

def parametr_a(n):
    if n==1:
        return 0
    return parametr_b(n-1)+parametr_c(n-1)

def parametr_b(n):
    if n==1:
        return 1
    return parametr_a(n-1)+parametr_c(n-1)

def parametr_c(n):
    if n==1:
        return 1
    return parametr_b(n-1)+parametr_a(n-1)

def get_triangle_path_count(length: int) -> int:
    """Calculates the number of closed routes of a target length between three
    vertices A, B and C that start and end at the A vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    :raise ArgumentException: when the parameter length must is not an integer.
    greater than 0
    :return: the number of routes.
    """
    if type(length) != int or length<=0:
        raise ArgumentException('The parameter length must be an integer '
                               'greater than 0')
    return parametr_a(length)

def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if type(length) != int or length<=0:
        raise ArgumentException('The parameter length must be an integer '
                               'greater than 0')
    spisok=[]
    set1("",length, spisok)
    set0("", length, spisok)
    return spisok

def set1(stroka, length, spisok):
    if length == len(stroka)+1:
        spisok.append(stroka+"1")
        return
    set1(stroka+"1", length, spisok)
    set0(stroka+"1", length, spisok)

def set0(stroka, length, spisok):
    if length == len(stroka)+1:
        spisok.append(stroka+"0")
        return
    set1(stroka+"0", length, spisok)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
