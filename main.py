def gcd_recursive(a: int, b: int) -> int:
    if a is None or b is None:
        raise Exception
    if a == 0 or b == 0:
        return a + b
    if a == b:
        return a
    if a < b:
        a, b = b, a
    a -= b
    return gcd_recursive(a, b)


def gcd_iterative_slow(a: int, b: int) -> int:
    if a is None or b is None:
        raise Exception
    while not (a == 0 or b == 0) and a != b:
        if a < b:
            a, b = b, a
        a -= b
    return a


def gcd_iterative_fast(a: int, b: int) -> int:
    if a is None or b is None:
        raise Exception
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return int(a * b / gcd_iterative_fast(a, b))


def main():
    print(gcd_recursive(1005002, 1354))


if __name__ == '__main__':
    main()
