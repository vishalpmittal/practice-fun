"""
    tag: list, minimum sum, priority queue

    Minimum Sum 
    Given an array of integers, perform some number k of operations. 
    Each operation consists of removing an element from the array, dividing it by 2 and 
    inserting the ceiling of that result back into the army. 
    Minimize the sum of the elements in the final army.

    Example: nums = [10, 20, 7], k= 4 
    [5, 5, 4]
    The sum of the final array is 5 + 5 + 4 = 14, and that sum is minimal. 

    Constraints 
    - 1 <= ns <= 10^5
    - 1 <= num[i] <= 10^4 (where 0 <= i < n)
    - 1 <= k <= 10^7
"""

from typing import List
import heapq
import math


def minSum_1(A: List[int], k: int) -> int:
    # O(3n + k*(lg n)) => O(lg n):
    if not A or k < 0:
        return

    HA = [-x for x in A]  # heapified array
    heapq.heapify(HA)

    for _ in range(k, 0, -1):
        CMON = math.ceil(-heapq.heappop(HA) / 2)  # current max operated number
        heapq.heappush(HA, -CMON)

    return -(sum(HA))


def heapreplace_max(heap, item):
    returnitem = heap[0]
    heap[0] = item
    heapq._siftup_max(heap, 0)
    return returnitem


def minSum(num, k):
    # O(2n + k*(lg n)) => O(lg n)
    heap = num
    heapq._heapify_max(heap)

    for i in range(k):
        max_value = heap[0]
        heapreplace_max(heap, math.ceil(max_value / 2))

    return sum(heap)


assert minSum([10, 20, 7], 4) == 14
print("Tests Passed!")
