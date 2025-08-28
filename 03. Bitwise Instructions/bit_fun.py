# O(1)
def is_even(n: int) -> bool:
    return (n & 1) == 0

# O(1)
def turn_uneven(n: int) -> int:
    return n | 1


def is_power_of_2(n: int) -> bool:
    # O(log N)
    # count: int = 0
    # while n:
    #     if n & 1:
    #         count += 1
    #     n >>= 1
    # return count == 1

    # O(1)
    return False if n == 0 else ((n - 1) & n) == 0



if __name__ == '__main__':
    print(f'{is_even(15) = }')
    print(f'{is_even(666) = }')
    print(f'{is_even(123) = }')
    print(f'{turn_uneven(123) = }')
    print(f'{turn_uneven(6) = }')
    print(f'{is_power_of_2(5) = }')
    print(f'{is_power_of_2(128) = }')
    print(f'{is_power_of_2(0) = }')
