"""
    Tag: math, array

    Given an array A of positive lengths, return the largest perimeter 
    of a triangle with non-zero area, formed from 3 of these lengths.

    If it is impossible to form any triangle of non-zero area, return 0.

    Example 1: Input: [2,1,2] Output: 5
    Example 2: Input: [1,2,1] Output: 0
    Example 3: Input: [3,2,3,4] Output: 10
    Example 4: Input: [3,6,2,3] Output: 8

    Note:
    3 <= A.length <= 10000
    1 <= A[i] <= 10^6
"""
from typing import List
from itertools import combinations


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        mp = 0
        tc = combinations(A, 3)
        for t in tc:
            s, ml = 0, -1
            for l in t:
                s += l
                ml = max(ml, l)
            if ml < s - ml:
                mp = max(mp, s)
        return mp

    def largestPerimeter_1(self, A: List[int]) -> int:
        # Similar to above but faster
        # Sort the array. For any c in the array, we choose the largest possible
        # a<=b<=c: these are just the two values adjacent to c.
        # If this forms a triangle, we return the answer.
        A.sort()
        for i in xrange(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0


assert Solution().largestPerimeter([2, 1, 2]) == 5
assert Solution().largestPerimeter([1, 2, 1]) == 0
assert Solution().largestPerimeter([3, 2, 3, 4]) == 10
assert Solution().largestPerimeter([3, 6, 2, 3]) == 8
print('Tests Passed!!')
