"""
    Tag: TO-DO, string, dp, array, integer, bit, linked list
    Tag: tree, sort, math, matrix, regex, recursive
    Tag: design ds (design data structure), dfs, binary search, algo, game

    In a array A of size 2N, there are N+1 unique elements, 
    and exactly one of these elements is repeated N times.
    Return the element repeated N times.

    Example 1: Input: [1,2,3,3] Output: 3
    Example 2: Input: [2,1,2,5,3,2] Output: 2
    Example 3: Input: [5,1,5,2,5,3,5,4] Output: 5

    Note:
    -  4 <= A.length <= 10000
    -  0 <= A[i] < 10000
    -  A.length is even
"""
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        us = set()
        for a in A:
            if a in us:
                return a
            us.add(a)


assert Solution().repeatedNTimes([1, 2, 3, 3]) == 3
assert Solution().repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2
assert Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5

print('Tests Passed!!')
