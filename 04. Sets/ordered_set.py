from __future__ import annotations
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

    # Complexity: O(1)
    def __init__(self) -> None:
        self.__sentinel = _Node()
        self.__count = 0

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity: O(N)
    def __repr__(self) -> str:
        result: list[T] = []
        current: _Node[T] = self.__sentinel.next
        while current != self.__sentinel:
            result.append(cast(T, current.info))
            current = current.next
        return f"OrderedSet({result if result else ''})"

    # Complexity: O(1)
    def add(self, value: T ) -> None:
        # TODO: Check if value exists
        # Assume that value doesn't exist, so add at the end
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
