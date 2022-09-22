from gcd_gen import GcdGenerator
def gcd_recursive(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers.
    Recursive implementation.

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if a is None or b is None:
        raise Exception("a or b value is None")
    if a == b:
        return a
    if a*b == 0:
        return a + b
    if a < b:
        a, b = b, a
    a -= b
    return gcd_recursive(a, b)




def gcd_iterative_slow(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers.
    Iterative implementation using subtraction.

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if a is None or b is None:
        raise Exception("a or b value is None")
    while a != b and a*b != 0:
        if a < b:
            a, b = b, a
        a -= b
    return max(a, b)


def gcd_iterative_fast(a: int, b: int) -> int:
    """Calculates the greatest common divisor of two numbers
    Iterative implementation using division.

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if a is None or b is None:
        raise Exception("a or b value is None")
    while b:
        a, b = b, a % b
    return a



def lcm(a: int, b: int) -> int:
    """Calculates the least common multiple of two numbers

    :param a: first number
    :param b: second number
    :except Exception: when a or b value is None
    :return: the least common multiple
    """
    return int(a * b / gcd_iterative_fast(a, b))



def main():
    print(gcd_recursive(1005002, 1354))
    gen = GcdGenerator()
    gen.generate_values(9)
    print(gen.a_value, gen.b_value)
    print(lcm(gen.a_value, gen.b_value))


if __name__ == '__main__':
    main()
