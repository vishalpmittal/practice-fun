"""
    Tag: design ds

    Design a class to find the kth largest element in a stream. 
    Note that it is the kth largest element in the sorted order, 
    not the kth distinct element.

    Your KthLargest class will have a constructor which accepts an integer 
    k and an integer array nums, which contains initial elements from the 
    stream. For each call to the method KthLargest.add, return the element 
    representing the kth largest element in the stream.

    Example:  int k = 3;  int[] arr = [4,5,8,2];
    KthLargest kthLargest = new KthLargest(3, arr);
    kthLargest.add(3);   // returns 4
    kthLargest.add(5);   // returns 5
    kthLargest.add(10);  // returns 5
    kthLargest.add(9);   // returns 8
    kthLargest.add(4);   // returns 8

    Note:
    You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.heap = nums[-k:]
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]


arr = [4, 5, 8, 2]
obj = KthLargest(3, arr)
assert obj.add(3) == 4
assert obj.add(5) == 5
assert obj.add(10) == 5
assert obj.add(9) == 8
assert obj.add(4) == 8
print('Tests Passed!!')
