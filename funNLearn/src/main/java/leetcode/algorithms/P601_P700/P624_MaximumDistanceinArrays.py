"""
    Tag: dp, array

    Given m arrays, and each array is sorted in ascending order.
    Now you can pick up two integers from two different arrays
    (each array picks one) and calculate the distance. We define the
    distance between two integers a and b to be their absolute
    difference |a-b|. Your task is to find the maximum distance.

    Example 1:  Input:          Output: 4
                [[1,2,3],
                [4,5],
                [1,2,3]]
    Explanation:
    One way to reach the maximum distance 4 is to pick 1 in the first
    or third array and pick 5 in the second array.

    Note:
    -  Each given array will have at least 1 number.
    There will be at least two non-empty arrays.
    -  The total number of the integers in all the m arrays will be
    in the range of [2, 10000].
    -  The integers in the m arrays will be in the range of [-10000, 10000].
"""
from typing import List
import sys


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if not arrays:
            return 0

        mi = arrays[0][0]
        ma = arrays[0][-1]
        ans = 0
        for A in arrays[1:]:
            lo, hi = A[0], A[-1]
            ans = max(ans, abs(ma - lo), abs(hi - mi))
            mi = min(mi, lo)
            ma = max(ma, hi)
        return ans


assert Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]) == 4
assert Solution().maxDistance([[1, 4], [0, 5]]) == 4
print('Tests Passed!!')
