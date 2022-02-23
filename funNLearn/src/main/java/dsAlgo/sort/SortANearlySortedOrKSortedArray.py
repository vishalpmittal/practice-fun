"""
    tag: sort, list

    Write a function that takes two parameters -- an array `arr` of n elements
    and an integer `k` -- and returns the array `arr` in sorted order.

    Each element in the input array `arr` is at most `k` positions away from
    where it would be if the array were sorted.

    Example:
    arr=[3, 2, 1, 5, 6, 4], k=2  ->  [1, 2, 3, 4, 5, 6]
"""

from typing import List

def insertion_sort(arr: List[int], k: int) -> List[int]:
    """
        like in insertion sort, start from left to right and keep sorting k elements at a time
    """
    if not arr or len(arr) < 2 or k == 0:
        return arr
    
    if k < 0 or k >= len(arr):
        raise ValueError(f"Invalid input value k: {k}")

    for i in range(0, len(arr) -1):
        for j in range(min(i+k, len(arr)-1), i, -1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


from heapq import heappop, heappush, heapify

def sort_k(arr: list, n: int, k: int):
    """
    - sort first k elements into a heap
    - for remaining k+1 to nth elements, heappush one at a time to heap and heappop one from the heap
    """
    heap = arr[:k + 1]
    heapify(heap)
 
    target_index = 0
    for rem_elmnts_index in range(k + 1, n):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[rem_elmnts_index])
        target_index += 1
 
    while heap:
        arr[target_index] = heappop(heap)
        target_index += 1


assert(insertion_sort(arr=[3, 2, 1, 5, 6, 4], k=2) == [1, 2, 3, 4, 5, 6])
assert(insertion_sort(arr=[3, 2, 1, 5, 6, 4], k=3) == [1, 2, 3, 4, 5, 6])
assert(insertion_sort(arr=[1, 2, 3, 4, 5, 6], k=0) == [1, 2, 3, 4, 5, 6])
assert(insertion_sort(arr=[6, 5, 4, 3, 2, 1], k=5) == [1, 2, 3, 4, 5, 6])
assert not(insertion_sort(arr=[3, 2, 1, 5, 6, 4], k=1) == [1, 2, 3, 4, 5, 6])
assert(insertion_sort(arr=[3, 1, 2, 6, 4, 5], k=2) == [1, 2, 3, 4, 5, 6])

assert(sort_k(arr=[3, 2, 1, 5, 6, 4], k=2) == [1, 2, 3, 4, 5, 6])
assert(sort_k(arr=[3, 2, 1, 5, 6, 4], k=3) == [1, 2, 3, 4, 5, 6])
assert(sort_k(arr=[1, 2, 3, 4, 5, 6], k=0) == [1, 2, 3, 4, 5, 6])
assert(sort_k(arr=[6, 5, 4, 3, 2, 1], k=5) == [1, 2, 3, 4, 5, 6])
assert not(sort_k(arr=[3, 2, 1, 5, 6, 4], k=1) == [1, 2, 3, 4, 5, 6])
assert(sort_k(arr=[3, 1, 2, 6, 4, 5], k=2) == [1, 2, 3, 4, 5, 6])


print("Test Passed!!!") 
