# O(1)
def is_even(n: int) -> bool:
    return (n & 1) == 0

# O(1)
def turn_uneven(n: int) -> int:
    return n | 1


# O(1)
def is_power_of_2(n: int) -> bool:
    return False if n == 0 else ((n - 1) & n) == 0


# O(log N)
def count_one_bits(n: int) -> int:
    count: int = 0
    while n:
        if n & 1:
            count += 1
        n >>= 1
    return count


# O(log M)
def int_mul(m: int, n: int) -> int:
    negative: bool = (n < 0) ^ (m < 0)
    m = abs(m)
    n = abs(n)
    result: int = 0
    while m:
        result += n if m & 1 else 0
        m >>= 1
        n <<= 1
    return -result if negative else result


# O(log N)
def int_log2(n: int) -> int:
    if n <= 0:
        raise ValueError(f'int_log2 not defined for {n}')
    result: int = 0
    while n > 1:
        result += 1
        n >>= 1
    return result



if __name__ == '__main__':
    print(f'{is_even(15) = }')
    print(f'{is_even(666) = }')
    print(f'{is_even(123) = }')
    print(f'{turn_uneven(123) = }')
    print(f'{turn_uneven(6) = }')
    print(f'{is_power_of_2(5) = }')
    print(f'{is_power_of_2(128) = }')
    print(f'{is_power_of_2(0) = }')
    print(f'{count_one_bits(7) = }')
    print(f'{count_one_bits(0) = }')
    print(f'{count_one_bits(1024) = }')
    print(f'{count_one_bits(1023) = }')
    print(f'{int_mul(5, 6) = }')
    print(f'{int_mul(-222, -3) = }')
    print(f'{int_mul(0, 6) = }')
    print(f'{int_mul(6, 0) = }')
    print(f'{int_log2(8) = }')
    print(f'{int_log2(7) = }')
    print(f'{int_log2(20) = }')
    print(f'{int_log2(32) = }')
    print(f'{int_log2(1024) = }')
