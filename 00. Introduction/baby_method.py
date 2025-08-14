def baby_sqrt(s: float, guess: float=1, delta: float=1e-10) -> float:
    if s < 0:
        raise ValueError(f'Cannot compute the square root of a negative number: {s}')
    previous: float = guess
    while True:
        guess = (previous + s / previous) / 2
        if abs(guess - previous) <= delta:
            return guess
        previous = guess
        print(previous)


if __name__ == '__main__':
    print('Running as a script')
    print(baby_sqrt(9, 2))
else:
    print('Running as a module', __name__)
