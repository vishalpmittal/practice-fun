"""
    Tag: matrix

    Given an m * n matrix M initialized with all 0's and several update operations.

    Operations are represented by a 2D array, and each operation is represented by 
    an array with two positive integers a and b, which means M[i][j] should be added 
    by one for all 0 <= i < a and 0 <= j < b.

    You need to count and return the number of maximum integers in the matrix after 
    performing all the operations.

    Example 1: Input:  m = 3, n = 3  operations = [[2,2],[3,3]]
    Output: 4
    Explanation: 
    Initially, M=        After performing [2,2], M=          After performing [3,3], M=
    [[0, 0, 0],               [[1, 1, 0],                          [[2, 2, 1], 
    [0, 0, 0],                [1, 1, 0],                           [2, 2, 1], 
    [0, 0, 0]]                [0, 0, 0]]                           [1, 1, 1]] 

    So the maximum integer in M is 2, and there are four of it in M. So return 4.

    Note:
    -  The range of m and n is [1,40000].
    -  The range of a is [1,m], and the range of b is [1,n].
    -  The range of operations size won't exceed 10,000.
"""
import collections
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # brute force, time limit exceeds
        if m <= 0 or n <= 0 or ops is None:
            return
        M = [[0 for i in range(n)] for j in range(m)]
        for op in ops:
            for i in range(op[0]):
                for j in range(op[1]):
                    M[i][j] += 1
        count = collections.Counter()
        for i in range(m):
            count.update(M[i])

        return count.get(max(count))

    def maxCount_smart(self, m: int, n: int, ops: List[List[int]]) -> int:
        # ex. if ops are [1, 3], [3, 1], to find common number of incremented element
        # get minimum x and minimum y co-ordinates and then return their product (1*1 = 1)
        for cord in ops:
            m = min(m, cord[0])
            n = min(n, cord[1])
        return m*n


assert Solution().maxCount(3, 3, [[2, 2], [3, 3]]) == 4
assert Solution().maxCount_smart(3, 3, [[2, 2], [3, 3]]) == 4
print("Tests Passed!!")
