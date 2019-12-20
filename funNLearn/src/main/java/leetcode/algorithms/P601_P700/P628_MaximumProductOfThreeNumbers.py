"""
    Tag: dp, array

    Given an integer array, find three numbers whose product is
    maximum and output the maximum product.

    Example 1: Input: [1,2,3]  Output: 6
    Example 2: Input: [1,2,3,4]  Output: 24

    Note:
    -  The length of the given array will be in range [3,104] and all
       elements are in the range [-1000, 1000].
    -  Multiplication of any three numbers in the input won't exceed the
       range of 32-bit signed integer.
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
            Approach 1: O(n^3) tripple loop comparying each option
            Approach 2: O(n Logn), sort the list, get max(n[0]*n[1]*n[-1], n[-1]*n[-2]*n[-3])
            Approach 3: O(n), Traverse through the list and find mn1, mn2, mx1, mx2 and mx3
                        mn1 is lowest and mx3 is highest
                        max_product = max(mn1*mn2*mx3, mx1*mx2*mx3)
        """
        mn1, mn2, mx1, mx2, mx3 = 1001, 1001, -1001, -1001, -1001
        for n in nums:
            if n <= mn1:
                mn2, mn1 = mn1, n
            elif n <= mn2:
                mn2 = n
            if n >= mx3:
                mx1, mx2, mx3 = mx2, mx3, n
            elif n >= mx2:
                mx1, mx2 = mx2, n
            elif n >= mx1:
                mx1 = n
        return max(mn1*mn2*mx3, mx1*mx2*mx3)


assert Solution().maximumProduct([-4, -3, -2, -1, 60]) == 720
assert Solution().maximumProduct([1, 2, 3]) == 6
assert Solution().maximumProduct([1, 2, 3, 4]) == 24
print('Tests Passed!!')
