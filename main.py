def gcd_recursive(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers.
    Recursive implementation.

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if a is None or b is None:
        raise Exception()
    if a*b == 0:
        return a+b
    if a == b:
        return a
    return gcd_recursive(max(a, b) - min(a, b), min(a, b))


def gcd_iterative_slow(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers.
    Iterative implementation using subtraction.

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if a is None or b is None:
        raise Exception()
    while a != b or a*b != 0:
        max(a, b) - min(a, b)
    return max(a, b)


def gcd_iterative_fast(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers
    Iterative implementation using division.

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    # остаток от целочисленного деления
    if a is None or b is None:
        raise Exception()
    while b != 0:
        a %= b
        a, b = b, a
        #a, b = b, a%b
    return a


def lcm(a: int, b: int) -> int:
    """Calculates the least common multiple of two numbers

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: the least common multiple
    """
    # нок = а*b / нод
    return int(a*b / gcd_iterative_fast(a, b))


def main():
    print(gcd_recursive(1005002, 1354))


if __name__ == '__main__':
    main()
