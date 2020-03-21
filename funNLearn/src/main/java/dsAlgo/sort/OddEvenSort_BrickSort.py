"""
    Tag: sort
"""
from typing import List


class Solution:
    def oddEvenSort_brickSort(self, A: List[int]) -> List[int]:
        """
            Just like bubble sort but we take care of odds and evens every time. 
        """

        # Initially array is unsorted
        isSorted = 0
        while isSorted == 0:
            isSorted = 1
            for i in range(1, len(A) - 1, 2):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    isSorted = 0

            for i in range(0, len(A) - 1, 2):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    isSorted = 0
        return A


assert Solution().oddEvenSort_brickSort([3, 2, 9, 3, 5, 7, 1, 8]) == [
    1,
    2,
    3,
    3,
    5,
    7,
    8,
    9,
]
print("Tests Passed!")
