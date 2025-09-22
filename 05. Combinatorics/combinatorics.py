def nicely_sorted[T](s: list[list[T]]) -> list[list[T]]:

    def size_and_content(value: list[T]) -> tuple[int, list[T]]:
        return (len(value), value)

    return sorted(s, key=size_and_content)

def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    recursive: list[list[T]] = power_set(s[:-1])
    return recursive + [e + [s[-1]] for e in recursive]


if __name__ == '__main__':
    from pprint import pprint
    print(power_set([]))  # type: ignore
    pprint(power_set(['a']))
    pprint(power_set(['a', 'b']))
    pprint(nicely_sorted(power_set(['a', 'b', 'c'])))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd', 'e'])))
