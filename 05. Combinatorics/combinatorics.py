def nicely_sorted[T](s: list[list[T]]) -> list[list[T]]:

    def size_and_content(value: list[T]) -> tuple[int, list[T]]:
        return (len(value), value)

    return sorted(s, key=size_and_content)


def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    recursive: list[list[T]] = power_set(s[:-1])
    return recursive + [e + [s[-1]] for e in recursive]


def combinations[T](s: list[T], k: int) -> list[list[T]]:
    return [t for t in power_set(s) if len(t) == k]


def insert[T](x: T, s: list[T], i: int) -> list[T]:
    return s[:i] + [x] + s[i:]


def insert_everywhere[T](x: T, s: list[T]) -> list[list[T]]:
    return [insert(x, s, i) for i in range(len(s) + 1)]


def permute[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    empty: list[list[T]] = []
    return sum([insert_everywhere(s[-1], e) for e in permute(s[:-1])], empty)


def permutations[T](s: list[T], k: int) -> list[list[T]]:
    empty: list[list[T]] = []
    return sum([permute(e) for e in combinations(s, k)], empty)


if __name__ == '__main__':
    from pprint import pprint
    print(power_set([]))  # type: ignore
    pprint(power_set(['a']))
    pprint(power_set(['a', 'b']))
    pprint(nicely_sorted(power_set(['a', 'b', 'c'])))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd', 'e'])))
    pprint(combinations(['a', 'b', 'c'], 2))
    pprint(combinations(['a', 'b', 'c', 'd'], 4))
    pprint(combinations(['a', 'b', 'c', 'd'], 1))
    pprint(combinations(['a', 'b', 'c', 'd', 'e'], 4))
    print(insert(5, [1, 2, 3], 0))
    print(insert(5, [1, 2, 3], 2))
    print(insert(5, [1, 2, 3], 3))
    print(insert_everywhere(5, [1, 2, 3]))
    pprint(nicely_sorted(permute([1, 2, 3, 4])))
    pprint(nicely_sorted(permutations([1, 2, 3, 4], 2)))
