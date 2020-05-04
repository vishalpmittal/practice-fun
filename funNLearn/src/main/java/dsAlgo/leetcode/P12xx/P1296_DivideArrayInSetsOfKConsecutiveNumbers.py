"""
    tag: list,

    Given an array of integers nums and a positive integer k, find whether 
    it's possible to divide this array into sets of k consecutive numbers
    Return True if its possible otherwise return False.
    the final subsets should combinely include all the elements of the 
    initial array

    Example 1: nums = [1,2,3,3,4,4,5,6], k = 4
    Output: true
    Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
    
    Example 2: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
    Output: true
    Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

    Example 3: nums = [3,3,2,2,1,1], k = 3
    Output: true
    
    Example 4: nums = [1,2,3,4], k = 3
    Output: false
    Explanation: Each array should be divided in subarrays of size 3.

    Constraints:
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^9
    - 1 <= k <= nums.length
"""
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        nums.sort()
        from collections import OrderedDict

        num_counts = OrderedDict()
        for n in nums:
            num_counts[n] = num_counts.get(n, 0) + 1

        total = 0
        while len(num_counts) >= k:
            cn = next(iter(num_counts.keys()))
            found = 0
            for inc in range(0, k):
                if cn + inc in num_counts:
                    found += 1
            ul = 1
            if found == k:
                total += 1
                ul = k

            for inc in range(0, ul):
                num_counts[cn + inc] -= 1
                if num_counts[cn + inc] == 0:
                    del num_counts[cn + inc]

        return total * k == len(nums)


assert Solution().isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4)
assert Solution().isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3)
assert Solution().isPossibleDivide(nums=[3, 3, 2, 2, 1, 1], k=3)
assert not Solution().isPossibleDivide(nums=[1, 2, 3, 4], k=3)
assert not Solution().isPossibleDivide([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4], 5)
assert not Solution().isPossibleDivide(
    [15, 16, 17, 18, 19, 16, 17, 18, 19, 20, 6, 7, 8, 9, 10, 3, 4, 5, 6, 20], 5
)
print("Tests Passed!")
