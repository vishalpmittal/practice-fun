"""
    Tag: array, binary search

    Given an array nums sorted in non-decreasing order, 
    and a number target, return True if and only if target is a 
    majority element. A majority element is an element that 
    appears more than N/2 times in an array of length N.

    Example 1: Input: nums = [2,4,5,5,5,5,5,6,6], target = 5 Output: true
    Explanation: 
    The value 5 appears 5 times and the length of the array is 9.
    Thus, 5 is a majority element because 5 > 9/2 is true.

    Example 2: Input: nums = [10,100,101,101], target = 101 Output: false
    Explanation: 
    The value 101 appears 2 times and the length of the array is 4.
    Thus, 101 is not a majority element because 2 > 4/2 is false.
    
    Note:
    -  1 <= nums.length <= 1000
    -  1 <= nums[i] <= 10^9
    -  1 <= target <= 10^9
"""
from typing import List
import collections


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return collections.Counter(nums)[target] > len(nums)//2

    def isMajorityElement_!(self, nums: List[int], target: int) -> bool:
        # Binary Search
        def search(a, x):
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        N = len(nums)
        if nums[N // 2] != target:
            return False
        lo = search(nums, target)
        hi = search(nums, target + 1)
        return hi - lo > N // 2


assert Solution().isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 5)
assert not Solution().isMajorityElement([10, 100, 101, 101], 101)
print('Tests Passed!!')
