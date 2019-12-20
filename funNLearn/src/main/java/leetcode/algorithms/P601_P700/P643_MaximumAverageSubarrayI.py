"""
    Tag: dp, array

    Given an array consisting of n integers, find the contiguous 
    subarray of given length k that has the maximum average value. 
    And you need to output the maximum average value.

    Example 1: Input: [1,12,-5,-6,50,3], k = 4  Output: 12.75
    Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

    Note:  
    -  1 <= k <= n <= 30,000.
    -  Elements of the given array will be in the range [-10,000, 10,000].
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or k > len(nums):
            return None
        ms = sum(nums[:k])
        ma = ms
        for i, n in enumerate(nums[k:], k):
            ma = ma - nums[i-k] + n
            ms = max(ms, ma)
        return ms/k


assert Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
assert Solution().findMaxAverage([0, 4, 0, 3, 2], 1) == 4.0
print('Tests Passed!!')
