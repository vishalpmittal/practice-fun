"""
    Tag: sort, array

    Given an array of integers A sorted in non-decreasing order, 
    return an array of the squares of each number, 
    also in sorted non-decreasing order.

    Example 1: Input: [-4,-1,0,3,10] Output: [0,1,9,16,100]
    Example 2: Input: [-7,-3,2,3,11] Output: [4,9,9,49,121]

    Note:
    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.
"""
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x*x for x in A)

    def sortedSquares_1(self, A: List[int]) -> List[int]:
        # Faster. Taking advantage of already sorted A
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans


assert Solution().sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert Solution().sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]

print('Tests Passed!!')
