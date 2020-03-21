"""
    Tag: sort
"""
from typing import List


class Solution:
    def selection_sort(self, A: List[int]) -> List[int]:
        """
            select the shortest element in array and put it in front
        """
        for i in range(len(A) - 1):
            min_idx = i
            for j in range(i + 1, len(A)):
                if A[j] < A[min_idx]:
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]
        return A


assert Solution().selection_sort([3, 2, 9, 3, 5, 7, 1, 8]) == [1, 2, 3, 3, 5, 7, 8, 9]
print("Tests Passed!")
