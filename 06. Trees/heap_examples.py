from heapq import heappush, heappop


# Complexity: O(N log N)
def heap_sort(data: list):  # type: ignore

    # Create the heap
    heap = []
    for e in data:  # type: ignore
        heappush(heap, e)  # type: ignore

    # Remove one element at a time from heap
    result = []
    while heap:
        result.append(heappop(heap))  # type: ignore
    return result  # type: ignore


if __name__ == "__main__":
    # h: list[int] = []
    # heappush(h, 6)
    # print(h)
    # heappush(h, 2)
    # print(h)
    # heappush(h, 1)
    # print(h)
    # heappush(h, 4)
    # print(h)
    # heappush(h, 0)
    # print(h)
    # print(heappop(h))
    # print(h)
    # print(heappop(h))
    # print(h)
    # print(heappop(h))
    # print(h)
    print(heap_sort([6, 2, 8, 1, 7, 3, 5, 4, 9]))  # type: ignore