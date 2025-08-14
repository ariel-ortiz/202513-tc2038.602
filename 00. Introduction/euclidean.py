def gcd2(a: int, b: int) -> int:
    while True:
        r: int = a % b
        if r == 0:
            return b
        a, b = b, r


def gcd(a: int, b: int, *rest: int) -> int:
    result: int = gcd2(a, b)
    for n in rest:
        result = gcd2(result, n)
    return result


def are_coprimes(x: int, y: int) -> bool:
    return gcd2(x, y) == 1


def lcm(x: int, y: int) -> int:
    return x * y // gcd2(x, y)


if __name__ == '__main__':
    print(f'{gcd(20, 150) = }')
    print(f'{gcd(1, 2, 3, 4) = }')
    print(f'{gcd(20, 15, 35, 100, 50) = }')
    print(f'{are_coprimes(25, 12) = }')
    print(f'{are_coprimes(25, 15) = }')
    print(f'{lcm(3, 5) = }')
    print(f'{lcm(2, 4) = }')
    print(f'{lcm(666, 777) = }')
