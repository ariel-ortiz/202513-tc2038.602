from collections.abc import Iterator


s: str = 'Hi!'
it: Iterator[str] = iter(s)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# try:
#     while True:
#         char: str = next(it)
#         print(char)
# except StopIteration:
#     ...

# for char in it:
#     print(char)

for char in s:
    print(char)

print()


class Pow2Iterator:

    current: int

    def __init__(self):
        self.current = 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current > 1_000_000:
            raise StopIteration()
        result: int = self.current
        self.current *= 2
        return result


for value in Pow2Iterator():
    print(value, end=' ')

print()

print(set(Pow2Iterator()))


def generator_example() -> Iterator[int]:
    var: int = 10
    yield var
    var *= 2
    yield var
    var -= 1
    yield var

print()

it2: Iterator[int] = generator_example()
print(next(it2))
print(next(it2))
print(next(it2))
# print(next(it2))
print()
for value in generator_example():
    print(value)

print(list(generator_example()))

def generator_pow2() -> Iterator[int]:
    current: int = 1
    while current <= 1_000_000:
        yield current
        current *= 2

print(list(generator_pow2()))
