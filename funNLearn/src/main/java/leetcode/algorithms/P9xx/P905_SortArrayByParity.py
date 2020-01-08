"""
    Tag: array, integer

    Given an array A of non-negative integers, return an array 
    consisting of all the even elements of A, followed by all the 
    odd elements of A.

    You may return any answer array that satisfies this condition.

    Example 1: Input: [3,1,2,4] Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
    
    Note:
    -  1 <= A.length <= 5000
    -  0 <= A[i] <= 5000
"""
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        f, b = 0, len(A)-1

        while f < b:
            while f < len(A) and A[f] % 2 == 0:
                f += 1
            while b >= 0 and A[b] % 2 != 0:
                b -= 1
            if f < b:
                A[f], A[b] = A[b], A[f]
        return A

    def sortArrayByParity_1(self, A: List[int]) -> List[int]:
        # sort using custom comparator
        A.sort(key=lambda x: x % 2)
        return A

    def sortArrayByParity_2(self, A: List[int]) -> List[int]:
        # two pass and external array
        return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])

    def sortArrayByParity_3(self, A: List[int]) -> List[int]:
        # In place, similar to sortArrayByParity_0
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1

        return A


assert Solution().sortArrayByParity([3, 1, 2, 4]) == [4, 2, 1, 3]
assert Solution().sortArrayByParity([0, 2]) == [0, 2]
print('Tests Passed!!')
