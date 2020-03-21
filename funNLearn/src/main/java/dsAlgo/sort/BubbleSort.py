"""
    Tag: sort
"""
from typing import List


class Solution:
    def bubble_sort(self, A: List[int]) -> List[int]:
        for i in range(len(A) - 1):
            for j in range(i, len(A)):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
        return A


assert Solution().bubble_sort([3, 2, 9, 3, 5, 7, 1, 8]) == [1, 2, 3, 3, 5, 7, 8, 9]
print("Tests Passed!")
