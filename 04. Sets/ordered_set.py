from __future__ import annotations
from collections.abc import Iterator, Iterable
from typing import cast


class _Node[N]:

    info: N | None
    next: _Node[N]
    prev: _Node[N]

    def __init__(self, value: N | None = None) -> None:
        self.info = value
        self.next = self
        self.prev = self


class OrderedSet[T]:

    __sentinel: _Node[T]
    __count: int

    # Complexity: O(N^2)
    def __init__(self, values: Iterable[T] = []) -> None:
        self.__sentinel = _Node()
        self.__count = 0
        for elem in values:
            self.add(elem)

    # Complexity: O(N)
    def __iter__(self) -> Iterator[T]:
        current: _Node[T] = self.__sentinel.next
        while current != self.__sentinel:
            yield cast(T, current.info)
            current = current.next

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity: O(N)
    def __contains__(self, value: T) -> bool:
        for elem in self:
            if elem == value:
                return True
        return False

    # Complexity: O(N)
    def __repr__(self) -> str:
        return f"OrderedSet({list(self) if self else ''})"

    # Complexity: O(N)
    def add(self, value: T ) -> None:
        if value in self:
            return
        self.__count += 1
        new_node: _Node[T] = _Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node


if __name__ == '__main__':
    s: OrderedSet[int] = OrderedSet()
    print(s)
    s.add(4)
    s.add(8)
    s.add(15)
    s.add(42)
    s.add(108)
    print(len(s))
    print(s)
    print(list(s))
    print(108 in s)
    print(107 in s)
    b: OrderedSet[str] = OrderedSet('hello')
    print(b)
    c = b
    c.add('x')
    print(b)
    print(c)
