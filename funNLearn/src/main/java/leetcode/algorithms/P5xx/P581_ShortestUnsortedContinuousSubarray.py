"""
    Tag: array, sort

    Given an integer array, you need to find one continuous subarray that 
    if you only sort this subarray in ascending order, then the whole array 
    will be sorted in ascending order, too.

    You need to find the shortest such subarray and output its length.

    Example 1: Input: [2, 6, 4, 8, 10, 9, 15]  Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make 
    the whole array sorted in ascending order.
    
    Note:
    -  Then length of the input array is in range [1, 10,000].
    -  The input array may contain duplicates, so ascending order here means <=.
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # sort and then compare each digit, find first differrent
        # left index and first different right index
        s_nums = sorted(nums)
        l = len(nums)
        if nums == s_nums:
            return 0
        li = 0
        ri = 0
        for i in range(l):
            if nums[i] != s_nums[i]:
                li = i
                break
        for i in range(l):
            if nums[l-1-i] != s_nums[l-1-i]:
                ri = l-i
                break
        return ri-li


assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
print('Tests Passed!!')
